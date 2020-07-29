import pyaudio
import numpy as np
import random
import math


# Train absolute pitch

def randrange(min, max):
    r = random.random()
    range = max - min
    r *= range

    return r + min

def randrangesquare(min, max):
    r = random.random()
    r = r ** 2
    range = max - min
    r *= range

    return r + min

# http://pages.mtu.edu/~suits/notefreqs.html
# https://en.wikipedia.org/wiki/Piano_key_frequencies
# c0 starts at 16.35
def convert_freq_to_myscale(x):
    #A4 = 440 Hz,C0	=16.35160
    divided = x / 16.35160
    log = math.log(divided, 2.0)
    return log


p = pyaudio.PyAudio()

fs = 44100       # sampling rate, Hz, must be integer
duration = 4.5   # in seconds, may be float

# paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

while True:
    volume = randrangesquare(0.05, 0.1)  # range [0.0, 1.0]
    volume *= 0.1
    f = randrange(100.0, 4500.0)  # Frequency of sine wave,
    print("*****")

    samples = (volume * np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32).tobytes()

    stream.write(samples)
    conv = convert_freq_to_myscale(f)
    print(conv, "frequency", f, "volume", volume)
    stream.write(samples)


