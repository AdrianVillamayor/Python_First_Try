from typing import Text
import pyttsx3
import speech_recognition as sr
# install $ brew install portaudio

engine = pyttsx3.init()


def speak(frase):
    engine.say(frase)
    engine.runAndWait()


def define_lang(lang):
    engine.setProperty("voice", "spanish")


def initRecognizer():
    r = sr.Recognizer()
    m = sr.Microphone()
    try:
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source:
                audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                value = r.recognize_google(audio, language="es-ES")
                if str is bytes:
                    print(u"You said {}".format(value).encode("utf-8"))
                else:
                    print("You said {}".format(value))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print(
                    "Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


def main():
    define_lang("spanish")
    speak("Hola me llamo adrii")

    initRecognizer()


if __name__ == "__main__":
    main()
