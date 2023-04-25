import os
import json

from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def __translate(*, language, text):
        return language_translator.translate(
        text=text,
        model_id=language,
    ).get_result().get('translations')[0].get('translation')


def english_to_french(*, english_text):
    return __translate(language='en-fr', text=english_text)


def french_to_english(*, french_text):
    return __translate(language='fr-en', text=french_text)
