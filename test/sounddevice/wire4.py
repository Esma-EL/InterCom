# Basic wire using blocking I/O. Python buffers are used.

import sounddevice as sd

stream = sd.RawStream(samplerate=44100, channels=2, dtype='int16')
stream.start()

while True:
    chunk, overflowed = stream.read(stream.read_available)
    if overflowed:
        print("Overflow")
    stream.write(chunk)
