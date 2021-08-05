# -*- coding:utf-8 -*-

import pyaudio

import speech_recognition as sr

r = sr.Recognizer()

CHUNK=1024*2
RATE=44100
p=pyaudio.PyAudio()

stream=p.open(	format = pyaudio.paInt16,
		channels = 1,
		rate = RATE,
		frames_per_buffer = CHUNK,
		input = True,
		output = True) # inputとoutputを同時にTrueにする


def audio_trans(input):
    with sr.AudioFile(input) as source:
        audio = r.record(source)

    print('音声データの文字起こし結果：\n\n', r.recognize_google(audio, language='ja'))
    return

while stream.is_active():
	input = stream.read(CHUNK)
    
	audio_trans(input)

	output = stream.write(input)

stream.stop_stream()
stream.close()
p.terminate()

print ("Stop Streaming")