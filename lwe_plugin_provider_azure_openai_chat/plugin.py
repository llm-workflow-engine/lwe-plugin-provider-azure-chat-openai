import os

from langchain.chat_models import AzureChatOpenAI

from lwe.core.provider import Provider, PresetValue

AZURE_OPENAI_CHAT_DEFAULT_DEPLOYMENT_NAME = "gpt-35-turbo"
AZURE_OPENAI_CHAT_TYPES = [
    "azure",
    "azure_ad",
    "azuread",
]

class ProviderAzureOpenaiChat(Provider):
    """
    Access to OpenAI chat models via the OpenAI API
    """

    @property
    def model_property_name(self):
        return 'deployment_name'

    @property
    def capabilities(self):
        return {
            'chat': True,
            'validate_models': False,
            'models': {
                'gpt-35-turbo': {
                    'max_tokens': 4096,
                },
                'gpt-35-turbo-16k': {
                    'max_tokens': 16384,
                },
                'gpt-4': {
                    'max_tokens': 8192,
                },
                'gpt-4-32k': {
                    'max_tokens': 32768,
                },
            }
        }

    @property
    def default_model(self):
        return AZURE_OPENAI_CHAT_DEFAULT_DEPLOYMENT_NAME

    def default_customizations(self, defaults=None):
        defaults = {
            'openai_api_key': 'placeholder',
            'openai_api_base': 'placeholder',
            'openai_api_version': 'placeholder',
        }
        return super().default_customizations(defaults)

    def prepare_messages_method(self):
        return self.prepare_messages_for_llm_chat

    def llm_factory(self):
        return AzureChatOpenAI

    def make_llm(self, customizations=None, use_defaults=False):
        customizations = customizations or {}
        final_customizations = self.get_customizations()
        final_customizations.update(customizations)
        final_customizations['openai_api_key'] = final_customizations.get('openai_api_key', os.environ['AZURE_OPENAI_API_KEY'])
        final_customizations['openai_api_base'] = final_customizations.get('openai_api_base', os.environ['AZURE_OPENAI_API_BASE'])
        final_customizations['openai_api_type'] = final_customizations.get('openai_api_type', os.environ['AZURE_OPENAI_API_TYPE'])
        final_customizations['openai_api_version'] = final_customizations.get('openai_api_version', os.environ['AZURE_OPENAI_API_VERSION'])
        return super().make_llm(final_customizations, use_defaults)

    def customization_config(self):
        return {
            'verbose': PresetValue(bool),
            'deployment_name': PresetValue(str, options=self.available_models),
            'temperature': PresetValue(float, min_value=0.0, max_value=2.0),
            'openai_api_key': PresetValue(str, include_none=True, private=True),
            'openai_api_base': PresetValue(str, include_none=True),
            'openai_api_type': PresetValue(str, options=AZURE_OPENAI_CHAT_TYPES, include_none=True),
            'openai_api_version': PresetValue(str, include_none=True),
            'openai_organization': PresetValue(str, include_none=True),
            'openai_proxy': PresetValue(str, include_none=True),
            'request_timeout': PresetValue(int),
            'max_retries': PresetValue(int, 1, 10),
            'n': PresetValue(int, 1, 10),
            'max_tokens': PresetValue(int, include_none=True),
            'model_kwargs': {
                'top_p': PresetValue(float, min_value=0.0, max_value=1.0),
                'presence_penalty': PresetValue(float, min_value=-2.0, max_value=2.0),
                'frequency_penalty': PresetValue(float, min_value=-2.0, max_value=2.0),
                'logit_bias': dict,
                'stop': PresetValue(str, include_none=True),
                'user': PresetValue(str),
                'functions': None,
                'function_call': None,
            },
        }
