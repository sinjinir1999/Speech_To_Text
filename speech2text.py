!pip install speechrecognition

import speech_recognition as sp

sp.__version__

recog=sp.Recognizer()

speech=sp.AudioFile('/content/recording.wav')

with speech as filesource:
  audio=recog.record(filesource,offset=6.7)

recog.recognize_google(audio)

with speech as filesource:
  audio1=recog.record(filesource,duration=2)
  audio2=recog.record(filesource,offset=6.7,duration=5)

recog.recognize_google(audio1)

recog.recognize_google(audio2)
