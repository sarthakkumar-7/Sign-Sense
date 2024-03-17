from googletrans import Translator
from gtts import gTTS
from playsound import playsound


def translate(text, source_lang='en', target_lang='hi'):
       translator = Translator()
       translated_text = translator.translate(text, src=source_lang, dest=target_lang).text
       print(translated_text)
       return translated_text


def speak(text,target_lang='hi'):
       tts = gTTS(text=text, lang=target_lang)
       tts.save("translated_text.mp3")
       playsound("translated_text.mp3")


if __name__ == "__main__":
   word_detected = "water"
   t = translate(word_detected)
   # speak(word_detected)
   speak(t)