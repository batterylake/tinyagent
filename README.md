# TinyAgent: A Modular Cognitive Architecture
## Introduction
TinyAgent is designed as a lightweight, modular cognitive framework that aims to emulate the core functionalities of an intelligent agent.

## Philosophy
The library adopts a "small pieces, loosely joined" philosophy, wherein each component (or 'module') of the system is designed to do one thing well and to interface cleanly with other components. This allows you to mix and match different sub-agents and memory modules, making the architecture highly extensible and customizable.

## Components
The core of TinyAgent includes the following components:

- Agent: The orchestrator that coordinates the activities between different sub-agents.
- AgentCode: Contains the main control flow logic and high-level templates for the Agent.
- LLM: Responsible for text generation and action execution.
- Memory Modules: Extensible modules for storing and retrieving information.

### Memory Modules
To create your own memory module, you have to:

- Inherit from the MemoryModule base class.
- Implement the learn and retrieve methods.
- Optionally, include any other methods that your module requires.

Example:

```
class MyMemoryModule(MemoryModule):
    def __init__(self, config):
        super().__init__(config)
        # Any other initialization

    def learn(self, text):
        # Your code here

    def retrieve(self, text):
        # Your code here
```
Then, update the factory function get_memory_module to include your new module:
```
def get_memory_module(config):
    service = config.get("service")
    if service == "MyMemoryModule":
        return MyMemoryModule(config)
    # existing code
```
## Configuration
Remember to include the necessary configuration details for your custom modules in the main configuration file. For example, if you've created a new memory module, add a new block under the memory_modules section in your config.json or equivalent:

```
{
  "memory_modules": {
    "MyMemoryModule": {
      "service": "MyMemoryModule",
      "some_parameter": "value",
      "another_parameter": "another_value"
    }
  }
}
```
By following the aforementioned steps, you can expand TinyAgent's capabilities while maintaining its modularity and flexibility.

## Testing
After adding your module, remember to write relevant unit tests. This ensures that your new module integrates well with the existing architecture and behaves as expected.

## Documentation
Don't forget to document your module. Include:
- Explanation of what your module does
- How to configure it
- Examples of how to use it
- This will make it easier for others to understand how to use your module and how it fits into the larger ecosystem of TinyAgent.

## Contribution Guidelines
If you think your module could be beneficial to the wider community, consider submitting a pull request. Ensure your code adheres to the existing coding standards and passes all unit tests.

## Final Words
The design philosophy behind TinyAgent encourages a community-driven approach where developers can contribute their specialized modules, thereby enriching the collective capabilities of the framework. Whether you're interested in natural language processing, robotic control, or data analytics, TinyAgent provides a solid foundation on which to build and experiment.