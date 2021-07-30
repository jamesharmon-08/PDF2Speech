import pyttsx3


class Speech():
    def __init__(self) -> None:
        super().__init__()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.karen')  # woman's voice
        # self.engine.setProperty('rate', 205)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()