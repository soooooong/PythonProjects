__author__ = 'song'
import  serial
import  sys
import  os
import  time
import  re



def sendAT_Cmd(serlnstance,atCmdStr,waitforOK):
    print("Command : %s"%atCmdStr)
    serlnstance.write(atCmdStr.encode('utf-8'))

    if(waitforOK ==1)
        waitFor

ser =serial.Serial("COM3",115200,timeout=30)
sendAT_Cmd(ser,'setenv opaddr 192.168.1.149 \r\n',1)
ser.close()
