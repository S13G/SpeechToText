import speech_recognition as sr

# create a new recognizer instance
r = sr.Recognizer()

# open the audio filev
with sr.AudioFile("voice2.wav") as source:
    # read the entire audio file
    audio_data = r.record(source)

    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio_data)

# write the transcribed text to a file
with open("transcribed_text.txt", "w") as text_file:
    text_file.write(text)
