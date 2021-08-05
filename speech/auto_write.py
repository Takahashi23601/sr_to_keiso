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
#import Print_text as pt

flag = False     #発言中True
pro_flag = False #処理中TrueTrue

#img = np.zeros((512,512,3), np.uint8) #黒背景

name = "data\Voicedata_"

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
all = []
record_times = 0;

while True:
    print("Recording Standby...\n")
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
            record_times += 1;
            WAVE_OUTPUT_FILENAME = name + str(record_times) + ".wav"
            break            #1秒たったら終了
        
        key = ord(getch())
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stream.close()
            p.terminate()
            print("Finished")
            sys.exit()
            
        
            
    
    #レコード終了
    print("Transcription Now.\n")
    
    #stream.close()
    #p.terminate()
    
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
    all = []
    
    sr.SP_rec(WAVE_OUTPUT_FILENAME)
    #pt.Print_text(img,text)
    
    plt.plot(result)
    plt.show()

    key = ord(getch())
    if key == 27:
        stream.close()
        p.terminate()
        print("Finished")
        sys.exit()
        

stream.close()
p.terminate()