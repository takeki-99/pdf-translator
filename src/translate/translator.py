from dotenv import load_dotenv
import os
import deepl

def add_newline(text: str, width: int, font_size: int) -> str:
    # calculate char_num_per_line
    char_num_per_line = int(width / font_size)
    # every line has char_num_per_line characters
    lines = [text[i:i+char_num_per_line] for i in range(0, len(text), char_num_per_line)]
    return "\n".join(lines)

# tlanslate text to target language
# def translate_text(text: str, lang: str) -> str:
def translate_text(text: str, lang: str, text_area_width: int, font_size: int) -> str:
    # make translator
    load_dotenv()
    api_key = os.getenv("DEEPL_API_KEY")
    if api_key is None:
        raise ValueError("DEEPL_API_KEY is not set")
    translator = deepl.Translator(api_key)

    # remove newline
    text = text.replace("\n", " ")
    result = translator.translate_text(text, target_lang=lang)
    
    # output result
    print(f"{text} -> {result.text}")

    # add newline
    translated_text = add_newline(result.text, text_area_width, font_size)
    return translated_text
    