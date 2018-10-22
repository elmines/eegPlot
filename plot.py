import sys
import matplotlib
import matplotlib.pyplot as plt
import json

fileName = sys.argv[1]
with open(fileName, "r", encoding="utf-8") as notes:
    eegGood = json.load(notes)

numPackets = len(eegGood)
samplesPerPacket = len(eegGood[0]["data"][0])
samplingRate = 256 #Hz
assert samplesPerPacket == samplingRate
timestamps = []
for i in range(numPackets):
    timestamps.extend([i + j/samplingRate for j in range(samplingRate) ])

channels = eegGood[0]["info"]["channelNames"]
for i, channel in enumerate(channels):
     samples = []
     for packet in eegGood:
         samples.extend(packet["data"][i])
     plt.plot(timestamps, samples, label=channel)
plt.xlabel("Time (s)")
plt.ylabel(u"Voltage (\u03bcV)")
plt.legend()
plt.show()

