import pyaudio
import numpy
import matplotlib.pyplot as plt
import numpy as np

flag = False;

chunk = 1024
FORMAT = pyaudio.paInt16

CHANNELS = 1 #モノラル（2にするとステレオ）
RATE = 44100 #サンプルレート（録音の音質）
RECORD_SECONDS = 3 #録音時間

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

#レコード開始
print("Now Recording...")
all = []
for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
    data = stream.read(chunk) #音声を読み取って、
    x = np.frombuffer(data, dtype="int16") / 32768.0
    xmax = x.max()

    if(xmax > 0.001 and flag == False):
        print(xmax)
        flag = True
    all.append(data) #データを追加

#レコード終了
print("Finished Recording.")

stream.close()
p.terminate()

#data = ''.join(all) #Python2用
data = b"".join(all) #Python3用

#録音したデータを配列に変換
result = numpy.frombuffer(data,dtype="int16") / float(2**15)

plt.plot(result)
plt.show()