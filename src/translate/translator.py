from dotenv import load_dotenv
import os
import deepl

# tlanslate text to target language
def translate_text(text: str, lang: str) -> str:
    # make translator
    load_dotenv()
    api_key = os.getenv("DEEPL_API_KEY")
    if api_key is None:
        raise ValueError("DEEPL_API_KEY is not set")
    translator = deepl.Translator(api_key)
    result = translator.translate_text(text, target_lang=lang)
    return result.text
    