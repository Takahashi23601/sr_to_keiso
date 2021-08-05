import speech_recognition as sr

AUDIO_FILE = 'sample.wav' #ここを変更。アップロードした音声ファイル（.wav形式）名に変更してください。

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

print('Transcription result of voice data:\n', r.recognize_google(audio, language='ja'))
print('\n')