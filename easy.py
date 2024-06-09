import streamlit as st 
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import warnings

warnings.filterwarnings("ignore")

def translate_text(input_lang, output_lang, text):
    lang_codes = {
        "Hindi": "hi_IN", 
        "French": "fr_XX", 
        "English": "en_XX", 
        "Malayalam": "ml_IN", 
        "Spanish": "es_XX"
    }
    
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    
    tokenizer.src_lang = lang_codes[input_lang]
    encoded_input = tokenizer(text, return_tensors="pt")
    forced_bos_token_id = tokenizer.lang_code_to_id[lang_codes[output_lang]]
    
    generated_tokens = model.generate(
        **encoded_input,
        forced_bos_token_id=forced_bos_token_id
    )
    
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return translated_text[0]

def main():
    st.set_page_config(
        page_title="Translation",
        page_icon="🌏",
        layout="centered"
    )

    st.title("🌏 Translation")

    col1, col2 = st.columns(2)

    with col1:
        input_language = ("Hindi", "French", "English", "Malayalam", "Spanish")
        input_lang = st.selectbox("Select input language", options=input_language)

    with col2:
        output_language = [lang for lang in input_language if lang != input_lang]
        output_lang = st.selectbox("Select output language", options=output_language)

    text = st.text_area(f"Enter the {input_lang.lower()} text")
    
    if st.button("Translate"):
        translated_text = translate_text(input_lang, output_lang, text)
        st.write(translated_text)

if __name__ == "__main__":
    main()
