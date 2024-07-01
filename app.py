from gtts.lang import tts_langs
from gtts import gTTS
import streamlit as st
from googletrans import Translator
import logging

# Translator
translator = Translator()

# Defining Page Title,Icon
st.set_page_config(
    page_title="Lingua Speak",
    page_icon="logo.png",
    menu_items={
        "About":"LinguaSpeak offers seamless text-to-speech conversion and translation services in numerous languages. Generate audio files from text and translate them instantly to your desired language. Download your creations effortlessly for use in presentations, education, or personal projects. Experience the power of multilingual communication with LinguaSpeak!"
    }
)

# Get the dictionary of supported languages
languages = tts_langs()
lang=[f"{code} : {name}" for code, name in languages.items()]

st.write("<h3 style='color:#FF8A08;'>Transform Text into Dynamic Multilingual Speech & Translation</h3>",unsafe_allow_html=True)

text=st.text_input("Enter Your Text")

selected_lang_input=st.selectbox("Specify the language for the above text",lang,index=lang.index("en : English"))

selected_lang_output=st.selectbox("Select language for translation",lang,index=lang.index("en : English"))

btn=st.button("Generate")

if btn:
    try:
        # Converting the text to desired language
        translated_text = translator.translate(text, src=selected_lang_input.split(":")[0].strip(), dest=selected_lang_output.split(":")[0].strip())
        # Using Google Translator to speak
        tts = gTTS(text=translated_text.text, lang=selected_lang_output.split(":")[0].strip(), slow=False)
        # Saving the file
        tts.save("output.mp3")
        st.markdown("### :green[Output Text:]")
        st.code(translated_text.text)
        # Audio File
        st.markdown("### :green[Your Audio:]")
        st.audio("output.mp3",autoplay=True)
        # Download Button
        st.download_button(label="Download", data=open("output.mp3","rb").read(), file_name="VocalizeNow.mp3")
    # except:
    #     st.error("Please Enter Something...")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        st.error("An error occurred. Please try again.")
