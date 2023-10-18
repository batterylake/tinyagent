from tiny_agent import *

class LocalVectorEmbeddings(MemoryModule):

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.model = config["model"]
        self.vector_store = pd.DataFrame(columns=["embedding", "text"])
        self.lookup_table = {}

    def embed(self, text: str) -> Any:
        return get_embedding(text, self.model)

    def learn(self, text: str):
        embedding = self.embed(text)
        self.vector_store = pd.concat([self.vector_store, pd.DataFrame([[embedding, text]], columns=["embedding", "text"])], ignore_index=True)

    def retrieve(self, text: str) -> str:
        n = self.config["n"]
        if self.config["lookup"] == "cosine":
            embedding = self.embed(text)
            self.vector_store["similarities"] = self.vector_store["embedding"].apply(lambda x: cosine_similarity(x, embedding))
            res = self.vector_store.sort_values('similarities', ascending=False).head(n)
            return " ".join(res["text"])

def get_memory_module(config: Dict[str, Any]) -> MemoryModule:
    service = config.get("service")
    if service == "LocalVectorEmbeddings":
        return LocalVectorEmbeddings(config)
    else:
        raise NotImplementedError(f"Memory module for service {service} not implemented")