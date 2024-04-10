# LLM Workflow Engine (LWE) Azure OpenAI Chat Provider plugin

Azure OpenAI Chat Provider plugin for [LLM Workflow Engine](https://github.com/llm-workflow-engine/llm-workflow-engine)

Access to [Azure OpenAI Chat](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models) models.

## Installation

### Azure setup

You'll need to create a service resource and deploy models see [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal).

You'll also need a key and endpoint for the resource, see [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-python#retrieve-key-and-endpoint)

### From packages

Install the latest version of this software directly from github with pip:

```bash
pip install git+https://github.com/llm-workflow-engine/lwe-plugin-provider-azure-openai-chat
```

### From source (recommended for development)

Install the latest version of this software directly from git:

```bash
git clone https://github.com/llm-workflow-engine/lwe-plugin-provider-azure-openai-chat.git
```

Install the development package:

```bash
cd lwe-plugin-provider-azure-openai-chat
pip install -e .
```

## Configuration

The following provider variables/environment variables need to be set:

* `export AZURE_OPENAI_API_KEY=[key]`
* `export AZURE_ENDPOINT=[endpoint]`
* `export AZURE_OPENAI_API_VERSION=2024-02-01`

Add the following to `config.yaml` in your profile:

```yaml
plugins:
  enabled:
    - provider_azure_openai_chat
    # Any other plugins you want enabled...
```

## Usage

From a running LWE shell:

```
/provider azure_openai_chat
/model deployment_name gpt-35-turbo
# Instead of environment variables, these values can also be set directly on the model:
/model openai_api_key [key]
/model openai_endpoint [endpoint]
/model openai_api_version 2023-05-15
```
