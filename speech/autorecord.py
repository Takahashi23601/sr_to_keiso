import pyaudio
import numpy
import matplotlib.pyplot as plt
import numpy as np
import time
import wave 
import SP_rec as sr
import cv2
import sys
from msvcrt import getch

flag = False;
WAVE_OUTPUT_FILENAME = "sample.wav"

chunk = 1024
FORMAT = pyaudio.paInt16
threshold = 0.03#しきい値
CHANNELS = 1 #モノラル（2にするとステレオ）
RATE = 44100 #サンプルレート（録音の音質）
RECORD_SECONDS = 3 #録音時間

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

start = 0
finish =0
#レコード開始
print("Recording Standby...")
all = []



while True:
    data = stream.read(chunk) #音声を読み取って、
    x = np.frombuffer(data, dtype="int16") / 32768.0
    xmax = x.max()
    
    if (xmax > threshold):
    #for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
        flag = True
        start = time.time()
        
    if (xmax <= threshold):
    #for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
        flag = False
        finish = time.time()
        
    if(flag == True or time.time() - start <= 1):
        all.append(data) #データを追加

    if(2 >= finish - start >= 1):
        break            #1秒たったら終了
    
    key = ord(getch())
    if key == 27:
        sys.exit()
        print("Finished")
    
        

#レコード終了
print("Finished Recording.")

stream.close()
p.terminate()

#data = ''.join(all) #Python2用
data = b"".join(all) #Python3用

#録音したデータを配列に変換
result = numpy.frombuffer(data,dtype="int16") / float(2**15)

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(p.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(all))
waveFile.close()

sr.SP_rec(WAVE_OUTPUT_FILENAME)

plt.plot(result)
plt.show()