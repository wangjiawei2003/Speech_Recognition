import datetime
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os

samplerate = 16000
duration = 5 # 录音秒数

print("开始录音...")

recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
sd.wait()

print("录音结束")

if not os.path.exists("audio"):
    os.mkdir("audio")

now = datetime.datetime.now()
filename = now.strftime("audio/%Y-%m-%d_%H%M%S.wav")
wv.write(filename, recording, samplerate, sampwidth=2)

print("保存为音频文件:", filename)