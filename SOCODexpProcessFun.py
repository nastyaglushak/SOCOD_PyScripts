import re
import numpy as np
from matplotlib import pyplot as plt
from array import *

def DataPrep10 (ChNum, mode):
    THRArrFile10 = []
    THRArrFile20 = []
    THRArrFile30 = []
    THRArrFile40 = []
    THRArrFile50 = []
    THRArrFile70 = []
    THRArrFile90 = []
    THRArrFile110 = []

    Count10 = []

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr10_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile10.extend(line.rstrip().split(':'))
    

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr20_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile20.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr30_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile30.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr40_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile40.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr50_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile50.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr70_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile70.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr90_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile90.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr110_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile110.extend(line.rstrip().split(':'))
    
    THRArr10, THRArrSensor10 = DataProcessing(THRArrFile10)
    THRArr20, THRArrSensor20 = DataProcessing(THRArrFile20)
    THRArr30, THRArrSensor30 = DataProcessing(THRArrFile30)
    THRArr40, THRArrSensor40 = DataProcessing(THRArrFile40)
    THRArr50, THRArrSensor50 = DataProcessing(THRArrFile50)
    THRArr70, THRArrSensor70 = DataProcessing(THRArrFile70)
    THRArr90, THRArrSensor90 = DataProcessing(THRArrFile90)
    THRArr110, THRArrSensor110 = DataProcessing(THRArrFile110)

    if (mode==False):
        return THRArr10, THRArrSensor10, THRArr20, THRArrSensor20, THRArr30, THRArrSensor30, THRArr40, THRArrSensor40, THRArr50, THRArrSensor50, THRArr70, THRArrSensor70, THRArr90, THRArrSensor90, THRArr110, THRArrSensor110 

    if (mode==True):
        #Count10=[THRArrSensor10[ChNum], THRArrSensor20[ChNum], THRArrSensor30[ChNum], THRArrSensor40[ChNum], THRArrSensor50[ChNum], THRArrSensor70[ChNum], THRArrSensor90[ChNum], THRArrSensor110[ChNum]]
        Count10=[THRArr10[ChNum], THRArr20[ChNum], THRArr30[ChNum], THRArr40[ChNum], THRArr50[ChNum], THRArr70[ChNum], THRArr90[ChNum], THRArr110[ChNum]]
        return Count10

def DataPrep17 (ChNum, mode):
    THRArrFile10 = []
    THRArrFile20 = []
    THRArrFile30 = []
    THRArrFile40 = []
    THRArrFile50 = []
    THRArrFile60 = []
    THRArrFile70 = []
    THRArrFile80 = []
    THRArrFile90 = []
    THRArrFile100 = []
    THRArrFile120 = []
    THRArrFile140 = []
    THRArrFile160 = []
    THRArrFile180 = []

    Count17 = []

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr10_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile10.extend(line.rstrip().split(':'))
    

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr20_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile20.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr30_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile30.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr40_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile40.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr50_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile50.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr60_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile60.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr70_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile70.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr80_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile80.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr90_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile90.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr100_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile100.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr120_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile120.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr140_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile140.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr160_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile160.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr180_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile180.extend(line.rstrip().split(':'))
    
    THRArr10, THRArrSensor10 = DataProcessing(THRArrFile10)
    THRArr20, THRArrSensor20 = DataProcessing(THRArrFile20)
    THRArr30, THRArrSensor30 = DataProcessing(THRArrFile30)
    THRArr40, THRArrSensor40 = DataProcessing(THRArrFile40)
    THRArr50, THRArrSensor50 = DataProcessing(THRArrFile50)
    THRArr60, THRArrSensor60 = DataProcessing(THRArrFile60)
    THRArr70, THRArrSensor70 = DataProcessing(THRArrFile70)
    THRArr80, THRArrSensor80 = DataProcessing(THRArrFile80)
    THRArr90, THRArrSensor90 = DataProcessing(THRArrFile90)
    THRArr100, THRArrSensor100 = DataProcessing(THRArrFile100)
    THRArr120, THRArrSensor120 = DataProcessing(THRArrFile120)
    THRArr140, THRArrSensor140 = DataProcessing(THRArrFile140)
    THRArr160, THRArrSensor160 = DataProcessing(THRArrFile160)
    THRArr180, THRArrSensor180 = DataProcessing(THRArrFile180)

    if (mode==False):
        return THRArr10, THRArrSensor10, THRArr20, THRArrSensor20, THRArr30, THRArrSensor30, THRArr40, THRArrSensor40, THRArr50, THRArrSensor50, THRArr60, THRArrSensor60, THRArr70, THRArrSensor70, THRArr80, THRArrSensor80, THRArr90, THRArrSensor90, THRArr100, THRArrSensor100, THRArr120, THRArrSensor120, THRArr140, THRArrSensor140, THRArr160, THRArrSensor160, THRArr180, THRArrSensor180

    if (mode==True):
        #Count17=[THRArrSensor10[ChNum], THRArrSensor20[ChNum], THRArrSensor30[ChNum], THRArrSensor40[ChNum], THRArrSensor50[ChNum], THRArrSensor60[ChNum], THRArrSensor70[ChNum], THRArrSensor80[ChNum], THRArrSensor90[ChNum], THRArrSensor100[ChNum], THRArrSensor120[ChNum], THRArrSensor140[ChNum], THRArrSensor160[ChNum], THRArrSensor180[ChNum]]
        Count17=[THRArr10[ChNum], THRArr20[ChNum], THRArr30[ChNum], THRArr40[ChNum], THRArr50[ChNum], THRArr60[ChNum], THRArr70[ChNum], THRArr80[ChNum], THRArr90[ChNum], THRArr100[ChNum], THRArr120[ChNum], THRArr140[ChNum], THRArr160[ChNum], THRArr180[ChNum]]
        return Count17

def DataPrep25 (ChNum, mode):

    THRArrFile20 = []
    THRArrFile40 = []
    THRArrFile60 = []
    THRArrFile80 = []
    THRArrFile100 = []
    THRArrFile120 = []
    THRArrFile140 = []
    THRArrFile160 = []

    Count25 = []

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr20_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile20.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr40_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile40.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr60_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile60.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr80_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile80.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr100_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile100.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr120_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile120.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr140_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile140.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCODn_thr160_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile160.extend(line.rstrip().split(':'))
        
    THRArr20, THRArrSensor20 = DataProcessing(THRArrFile20)
    THRArr40, THRArrSensor40 = DataProcessing(THRArrFile40)
    THRArr60, THRArrSensor60 = DataProcessing(THRArrFile60)
    THRArr80, THRArrSensor80 = DataProcessing(THRArrFile80)
    THRArr100, THRArrSensor100 = DataProcessing(THRArrFile100)
    THRArr120, THRArrSensor120 = DataProcessing(THRArrFile120)
    THRArr140, THRArrSensor140 = DataProcessing(THRArrFile140)
    THRArr160, THRArrSensor160 = DataProcessing(THRArrFile160)

    if (mode==False):
        return THRArr20, THRArrSensor20, THRArr40, THRArrSensor40, THRArr60, THRArrSensor60, THRArr80, THRArrSensor80, THRArr100, THRArrSensor100, THRArr120, THRArrSensor120, THRArr140, THRArrSensor140, THRArr160, THRArrSensor160
    if (mode==True):
        #Count25=[THRArrSensor20[ChNum], THRArrSensor40[ChNum], THRArrSensor60[ChNum], THRArrSensor80[ChNum], THRArrSensor100[ChNum], THRArrSensor120[ChNum], THRArrSensor140[ChNum], THRArrSensor160[ChNum]]
        Count25=[THRArr20[ChNum], THRArr40[ChNum], THRArr60[ChNum], THRArr80[ChNum], THRArr100[ChNum], THRArr120[ChNum], THRArr140[ChNum], THRArr160[ChNum]]
        return Count25

def DataProcessing (THRArrFile):

    THRArrClear = []
    THRArr = []
    THRArrSensor =[]

    for i in range (0, 96):
        THRArrSensor.append(0)

    for i in range (0,95*2+2):
        THRArrClear.append(THRArrFile[i].split(" "))

    for i in range (0, 9):
        THRArr.append(int(THRArrClear[2*i+1][2]))

    for i in range (9, 96):
        THRArr.append(int(THRArrClear[2*i+1][1]))

    for i in range (0, len(THRArr)-1):
        if (i<48): THRArrSensor[2*i]=THRArr[i]
        if (i>=48): THRArrSensor[(95-i)*2+1]=THRArr[i]
    # print(THRArrClear[19])
    # print(THRArrClear[19])
    #print(THRArr, len (THRArr))
    #print(THRArrSensor, len(THRArrSensor), len (THRArrX))
    return THRArrSensor, THRArr

def DataDraw (THRArrSensor, THRArr):
    THRArrX=[]

    for i in range (0, 96):
        THRArrX.append(i+1)

    fig,(ch1,ch2)=plt.subplots(1,2)
    
    ch1.bar(THRArrX, THRArrSensor, width=0.1)
    ch1.set_title ("Sensor", fontsize=24)
    ch1.set_xlabel ("THR")
    ch1.set_ylabel ("Counts")
    ch1.grid(which='minor', 
            color = 'k', 
            linestyle = ':')
    ch1.grid(True)

    ch2.bar(THRArrX, THRArr, width=0.08)
    ch2.set_title ("THR Electornics", fontsize=24)
    ch2.grid(which='minor', 
            color = 'k', 
            linestyle = ':')
    ch2.grid(True)
    plt.show()

def CountChar (THRmass, Count1, Count2, ChNum1, ChNum2):
    plt.plot (THRmass, Count1, '--',THRmass, Count2)
    plt.title ("Counting Characteristics")
    plt.xlabel ("THR")
    plt.ylabel ("Counts")
    plt.legend(["Channel_{0}".format(ChNum1), "Channel_{0}". format(ChNum2)])
    plt.grid (True)
    plt.show()

def CountCharAll (THRmass, Count1, Count2, THRmass2, Count3, Count4, THRmass3,Count5, Count6, ChNum1, ChNum2):
    plt.plot (THRmass, Count1, '--',THRmass, Count2, '--', THRmass2, Count3, THRmass2, Count4, THRmass3, Count5, 'o-', THRmass3, Count6, 'o-', )
    plt.title ("Counting Characteristics")
    plt.xlabel ("THR")
    plt.ylabel ("Counts")
    plt.legend(["10keV {0}".format(ChNum1), "10keV {0}".format(ChNum2),"17keV {0}".format(ChNum1), "17keV {0}".format(ChNum2),"25keV {0}".format(ChNum1), "25keV {0}".format(ChNum2),])
    plt.grid (True)
    plt.show()