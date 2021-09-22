!pip install speechrecognition

import speech_recognition as sp

sp.__version__

recog=sp.Recognizer()

speech=sp.AudioFile('/content/recording.wav')

with speech as noisesource:
  recog.adjust_for_ambient_noise(noisesource)
  audio=recog.record(noisesource)

recog.recognize_google(audio)

recog.recognize_google(audio,show_all=True)
