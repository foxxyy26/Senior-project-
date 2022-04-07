import sys
import os
from mido import MidiFile, MidiTrack

track = MidiTrack()  #
mid = MidiFile('VampireKillerCV1.mid')  #
for i, track in enumerate(mid.tracks):  # enumerate()：创建索引序列，索引初始为0
    print('Track {}: {}'.format(i, track.name))
    for msg in track:  #
        fw = open("Data.txt", 'w')
        print(msg)
        fw.write(msg)




mid.tracks.append(track)
# track.append(Message('program_change',channel=0,program= X,time=0))
# track.append(Message('note_on', note=XX, velocity=64, time=XX,channel=0))
# track.append(Message('note_off', note=XX, velocity=64, time=XX,channel=0))
fw.close()
mid.save('new.mid')

# class Logger(object):
# def __init__(self,filename="Default.log"):
# self.terminal = sys.stdout
# self.log = open(filename,"Data")
# def write(self.message):
# self.terminal.write(message)
# self.log.write(message)
# def flush(self):
#   pass
# path = os.path.abspath(os.path.dirname(_file_))
# type = sys.getfilesystemencoding()
# sys.stdout = Logger('Data.txt')
# print(os.path.dirname(_file_))
# print('⋯⋯⋯⋯⋯⋯⋯')
