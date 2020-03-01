# this program does not print the frequencies
# vtrigSettings.mode = vtrig.VTRIG_U_TXMODE__LOW_RATE( LOW-20,MED,10,HIGH- 4 antennas)
# Power + Frequency for a single antenna 
import unittest
import itertools
import ctypes
import argparse
import sys
from imp import load_source
from os.path import join
import csv,cmath,math

def DefaultModulePath():
    if sys.platform == 'win32':
        modulePath = join('C:/', 'Program Files', 'Vayyar', 'vtrigU', 'python', 'vtrigU.py')
    elif sys.platform.startswith('linux'):
        modulePath = join('/usr', 'share', 'vtrigU', 'python', 'vtrigU.py')
    else:
        raise BaseException('Unsupported platform: ' + sys.platform)
    return modulePath

def Import_vtrigU():
    global vtrig
    vtrig = load_source('vtrigU', DefaultModulePath())

if __name__ == '__main__':
    Import_vtrigU()

vtrig.Init()
# apply settings:
vtrigSettings = vtrig.RecordingSettings(
    vtrig.FrequencyRange(65.0*1000, 66.0*1000, 2), # 101 points, from 65.0-66.0 GHz
    30.0, # RBW (in KHz)
    vtrig.VTRIG_U_TXMODE__LOW_RATE #
    ) 
vtrig.ApplySettings(vtrigSettings)

vtrig.Record() # one recording
print (vtrig.Record)

    # modify settings
vtrigSettings.rbw_khz = 30.5
vtrigSettings.mode = vtrig.VTRIG_U_TXMODE__HIGH_RATE
vtrig.ApplySettings(vtrigSettings)

actual_freqs = vtrig.GetFreqVector_MHz()
pair_list = vtrig.GetAntennaPairs(vtrigSettings.mode)
# record a bunch of times
for i in range(1):
    vtrig.Record() 
recording = vtrig.GetRecordingResult()
print (actual_freqs)
print(pair_list)
#print (recording)
x=recording
print (x)
g=len(x)
print("length of x=",g)
print(type(x))

print (x[4,40])
test=x[4,40][0]
I=x[4,40][0]
Q=x[4,40][1]
print("I=",I)
print("Q=",Q)
print ("Real part is ",I.real)
print ("Imaginary part is ",I.imag)
angle=I.imag/I.real
#addi=(I.real**2+I.imag**2)
power=10*math.log10( I.real**2+I.imag**2 )
print("power/ 65GHZ =",power)
print ("angle/65 Ghz =",angle)
# writing to csv file
with open('test.csv', 'w') as f:
    for key in x.keys():
        f.write("%s,%s\n"%(key,x[key]))

with open('data.csv', 'w') as f:
    for key in x.keys():
     f.write("%s,%s\n"%(key,x[key]))

