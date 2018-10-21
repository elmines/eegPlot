import sys
import matplotlib
import matplotlib.pyplot as plt
import json

fileName = sys.argv[1]
with open(fileName, "r", encoding="utf-8") as notes:
    eegGood = json.load(notes)

channels = eegGood[0]["info"]["channelNames"]
numSamples = len(eegGood[0]["data"][0])
timestamps = [i for i in range(numSamples)]
for packet in eegGood:
    for i, channel in enumerate(channels):
        samples = packet["data"][i]
        plt.plot(timestamps, samples, label=channel)
        plt.legend()
    plt.show()
