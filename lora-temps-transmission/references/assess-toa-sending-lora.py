"""
    File : assess-toa-sending-lora.py
    Author : Sébastien Bindel
    email : sebastien.bindel@uha.fr
"""
import machine
import os
from network import LoRa
import socket
import pycom
import utime
import time

# determine the maximal data size
def ComputeMaxDataSize(sf,bw):
    max_size = 0
    if bw == 125:
        if sf == 7 :
            max_size = 222
        elif sf == 8 :
            max_size = 222
        elif sf == 9 :
            max_size = 115
        elif sf == 10 :
            max_size = 51
        elif sf == 11 :
            max_size = 51
        elif sf == 12 :
            max_size = 51
    elif bw == 250 :
        if sf == 7 :
            max_size = 222
    return max_size

# create a message with the selected length
def create_mess(length):
    mess = 'ÿ'*length
    return mess

# declare variable
display = "TIteration;TBlock;TMessGen;TMessSend;TDisplay;TOA;Essai;TxPower;SF;Bandwidth;CodingRate;Taille\n"
info = ""
infoLog = ""
mess = ""
data_max_size=0

""" time variables related to time capture """
begin_it = None
time_blocking = None
mess_generated_time = None
send_mess = None

""" variables related to the lora configuration """
preamble_length=8

""" Variables à modifier """
idx = 1
taille=0
spreading_factor=7
bandwith=250
coding_rate="4_6"
data_max_size = ComputeMaxDataSize(spreading_factor,bandwith)

# Configure LED color (BLUE=LoRA)
pycom.heartbeat(False)
pycom.rgbled(0x00007f)

# mount SD card (only first time)
sd = machine.SD()
os.mount(sd, '/sd')
filename = "/sd/assess-toa-send/sending-test-"+str(spreading_factor)+"-"+str(preamble_length)+"-"+coding_rate+"-"+str(bandwith)+"-EU868.csv"
desc = open(filename, 'w')
desc.write(display)
display=""

#Configure LORA connection
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)

if bandwith == 125 :
    if coding_rate == "4_8":
        lora.init(region=LoRa.EU868, bandwidth=LoRa.BW_125KHZ, sf=spreading_factor, preamble=preamble_length, coding_rate=LoRa.CODING_4_8)
    elif coding_rate == "4_7":
        lora.init(region=LoRa.EU868, bandwidth=LoRa.BW_125KHZ, sf=spreading_factor, preamble=preamble_length, coding_rate=LoRa.CODING_4_7)
    elif coding_rate == "4_6":
        lora.init(region=LoRa.EU868, bandwidth=LoRa.BW_125KHZ, sf=spreading_factor, preamble=preamble_length, coding_rate=LoRa.CODING_4_6)
    elif coding_rate == "4_5":
        lora.init(region=LoRa.EU868, bandwidth=LoRa.BW_125KHZ, sf=spreading_factor, preamble=preamble_length, coding_rate=LoRa.CODING_4_5)
elif bandwith == 250 :
    if spreading_factor == 7 :
        if coding_rate == "4_8":
            lora.init(region=LoRa.EU868, bandwidth=LoRa.BW_250KHZ, sf=spreading_factor, preamble=preamble_length, coding_rate=LoRa.CODING_4_8)
        elif coding_rate == "4_7":
                lora.init(region=LoRa.EU868, bandwidth=LoRa.BW_250KHZ, sf=spreading_factor, preamble=preamble_length, coding_rate=LoRa.CODING_4_7)
        elif coding_rate == "4_6":
                lora.init(region=LoRa.EU868, bandwidth=LoRa.BW_250KHZ, sf=spreading_factor, preamble=preamble_length, coding_rate=LoRa.CODING_4_6)
        elif coding_rate == "4_5":
                lora.init(region=LoRa.EU868, bandwidth=LoRa.BW_250KHZ, sf=spreading_factor, preamble=preamble_length, coding_rate=LoRa.CODING_4_5)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

#avoid overflow
if taille > data_max_size:
    taille = data_max_size

#Send Info
while taille <= data_max_size:
    """ Begin Iteration """
    begin_it = utime.ticks_cpu()

    """ Block socket """
    s.setblocking(True)
    time_blocking = utime.ticks_cpu()

    """ Generate message """
    mess = create_mess(taille) # generate message
    mess_generated_time = utime.ticks_cpu()

    """ Send Mess """
    result = s.send(mess)
    send_mess = utime.ticks_cpu()

    """ Catch sending info """
    #info= "TIt:"+str(begin_it)
    #info+=",TSB:"+str(time_blocking)
    #info+=",TMessGen:"+str(mess_generated_time)
    #info+=",TimeSend:"+str(send_mess)
    #info+=",TimeDisplay:"+str(utime.ticks_cpu())
    #info+=",TxPower:"+str(lora.stats().tx_power)
    info="TOA:"+str(lora.stats().tx_time_on_air)
    info+=",Essai:"+str(lora.stats().tx_trials)
    info+=",SF:"+str(lora.stats().sftx)
    info+=",BW:"+str(bandwith)
    info+=",CR:"+str(coding_rate)
    info+=",Taille:"+str(result)+"/"+str(data_max_size)+"\n"
    print(info)
    infoLog+=str(begin_it)
    infoLog+=";"+str(time_blocking)
    infoLog+=";"+str(mess_generated_time)
    infoLog+=";"+str(send_mess)
    infoLog+=";"+str(utime.ticks_cpu())
    infoLog+=";"+str(lora.stats().tx_time_on_air)
    infoLog+=";"+str(lora.stats().tx_trials)
    infoLog+=";"+str(lora.stats().tx_power)
    infoLog+=";"+str(lora.stats().sftx)
    infoLog+=";"+str(bandwith)
    infoLog+=";"+str(coding_rate)
    infoLog+=";"+str(result)+"\n"
    desc.write(infoLog)
    infoLog=""
    taille+=1

desc.close()
