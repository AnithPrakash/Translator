# translation web app 
# 🌏 Translation Web App

This repository contains a **Streamlit**-based web application for translating text between five popular languages using the **facebook/mbart-large-50-many-to-many-mmt** model. The supported languages are **Hindi**, **French**, **English**, **Malayalam**, and **Spanish**.

## Features

- **Translate** text between **Hindi**, **French**, **English**, **Malayalam**, and **Spanish**.
- Utilizes the **MBartForConditionalGeneration** model from **Hugging Face**.
- Simple and user-friendly **web interface**.
- **Dynamic language selection** for both input and output languages.

## Setup Instructions

1. **Clone** the repository:
    ```sh
    git clone https://github.com/anithprakash/translation-web-app.git
    cd translation-web-app
    ```

2. **Install** the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run** the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Usage

1. **Select** the input language from the dropdown menu.
2. **Select** the output language from the second dropdown menu.
3. **Enter** the text you want to translate in the text area.
4. **Click** the "Translate" button to get the translated text.

## Code Overview

The main translation logic is handled in the `translate_text` function. Here is a brief summary of the code structure:

- **translate_text**: This function takes the input language, output language, and text as arguments. It uses the **MBartForConditionalGeneration** model and **MBart50TokenizerFast** tokenizer to perform the translation.

- ### Summary:
This project is a **Streamlit**-based web application for translating text between five popular languages: **Hindi**, **French**, **English**, **Malayalam**, and **Spanish**. It leverages the **facebook/mbart-large-50-many-to-many-mmt** model to perform translations. The application features a simple user interface that allows users to select input and output languages, enter text, and receive translations instantly. The code is modular and easy to maintain, making it a good starting point for anyone interested in building translation applications.
