import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("audiofiles/transcript.mp3")
sound.export("audiofiles/transcript.wav", format="wav")


