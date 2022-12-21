import speech_recognition as sr
from pydub import AudioSegment

# Load the audio file
sound = AudioSegment.from_file('audio.opus', format='opus')

# Save the audio file as WAV
sound.export('audio.wav', format='wav')

# Load the audio file
r = sr.Recognizer()
with sr.AudioFile('audio.wav') as source:
    audio = r.record(source)

# Convert the audio file to text
text = r.recognize_google(audio, language='pt-BR')
print(text)
