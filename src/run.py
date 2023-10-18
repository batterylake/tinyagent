from src.tiny_agent import *
def main(path):
    with open(path, "r") as f: config = json.load(f)
    if validate_config(config): Agent(config).run()

if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Run TinyAgent with a config file.").add_argument("config_path", type=str, help="Path to the config file.").parse_args()
    main(args.config_path)