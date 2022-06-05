import re
import numpy as np
from matplotlib import pyplot as plt
from array import *

from SOCODexpProcessFun import DataProcessing

def DataPrep10u (ChNum, mode):

    THRArrFile40 = []
    THRArrFile60 = []
    THRArrFile80 = []
    THRArrFile100 = []
    THRArrFile120 = []
    THRArrFile140 = []
    THRArrFile160 = []
    THRArrFile180 = []
    THRArrFile200 = []
    THRArrFile220 = []

    Count10 = []

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr220_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile220.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr200_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile200.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr40_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile40.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr60_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile60.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr80_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile80.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr100_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile100.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr120_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile120.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr140_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile140.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr160_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile160.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr180_10keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile180.extend(line.rstrip().split(':'))
    
    THRArr40, THRArrSensor40 = DataProcessing(THRArrFile40)
    THRArr60, THRArrSensor60 = DataProcessing(THRArrFile60)
    THRArr80, THRArrSensor80 = DataProcessing(THRArrFile80)
    THRArr100, THRArrSensor100 = DataProcessing(THRArrFile100)
    THRArr120, THRArrSensor120 = DataProcessing(THRArrFile120)
    THRArr140, THRArrSensor140 = DataProcessing(THRArrFile140)
    THRArr160, THRArrSensor160 = DataProcessing(THRArrFile160)
    THRArr180, THRArrSensor180 = DataProcessing(THRArrFile180)
    THRArr200, THRArrSensor200 = DataProcessing(THRArrFile200)
    THRArr220, THRArrSensor220 = DataProcessing(THRArrFile220)

    if (mode==False):
        return THRArr40, THRArrSensor40, THRArr60, THRArrSensor60, THRArr80, THRArrSensor80, THRArr100, THRArrSensor100, THRArr120, THRArrSensor120, THRArr140, THRArrSensor140, THRArr160, THRArrSensor160, THRArr180, THRArrSensor180, THRArr200, THRArrSensor200, THRArr220, THRArrSensor220

    if (mode==True):
        #Count10=[THRArrSensor40[ChNum], THRArrSensor60[ChNum], THRArrSensor80[ChNum], THRArrSensor100[ChNum], THRArrSensor120[ChNum], THRArrSensor140[ChNum], THRArrSensor160[ChNum], THRArrSensor180[ChNum], THRArrSensor200[ChNum], THRArrSensor220[ChNum]]
        Count10=[THRArr40[ChNum], THRArr60[ChNum], THRArr80[ChNum], THRArr100[ChNum], THRArr120[ChNum], THRArr140[ChNum], THRArr160[ChNum], THRArr180[ChNum], THRArr200[ChNum], THRArr220[ChNum]]
        return Count10

def DataPrep17u (ChNum, mode):

    THRArrFile20 = []
    THRArrFile40 = []
    THRArrFile60 = []
    THRArrFile80 = []
    THRArrFile100 = []
    THRArrFile120 = []
    THRArrFile140 = []
    THRArrFile160 = []
    THRArrFile180 = []
    THRArrFile200 = []
    THRArrFile220 = []

    Count17 = []

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr20_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile20.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr220_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile220.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr200_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile200.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr40_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile40.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr60_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile60.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr80_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile80.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr100_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile100.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr120_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile120.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr140_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile140.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr160_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile160.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr180_17keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile180.extend(line.rstrip().split(':'))
    
    THRArr20, THRArrSensor20 = DataProcessing(THRArrFile20)
    THRArr40, THRArrSensor40 = DataProcessing(THRArrFile40)
    THRArr60, THRArrSensor60 = DataProcessing(THRArrFile60)
    THRArr80, THRArrSensor80 = DataProcessing(THRArrFile80)
    THRArr100, THRArrSensor100 = DataProcessing(THRArrFile100)
    THRArr120, THRArrSensor120 = DataProcessing(THRArrFile120)
    THRArr140, THRArrSensor140 = DataProcessing(THRArrFile140)
    THRArr160, THRArrSensor160 = DataProcessing(THRArrFile160)
    THRArr180, THRArrSensor180 = DataProcessing(THRArrFile180)
    THRArr200, THRArrSensor200 = DataProcessing(THRArrFile200)
    THRArr220, THRArrSensor220 = DataProcessing(THRArrFile220)

    if (mode==False):
        return THRArr20, THRArrSensor20, THRArr40, THRArrSensor40, THRArr60, THRArrSensor60, THRArr80, THRArrSensor80, THRArr100, THRArrSensor100, THRArr120, THRArrSensor120, THRArr140, THRArrSensor140, THRArr160, THRArrSensor160, THRArr180, THRArrSensor180, THRArr200, THRArrSensor200, THRArr220, THRArrSensor220

    if (mode==True):
        #Count17=[THRArrSensor20[ChNum], THRArrSensor40[ChNum], THRArrSensor60[ChNum], THRArrSensor80[ChNum], THRArrSensor100[ChNum], THRArrSensor120[ChNum], THRArrSensor140[ChNum], THRArrSensor160[ChNum], THRArrSensor180[ChNum], THRArrSensor200[ChNum], THRArrSensor220[ChNum]]
        Count17=[THRArr20[ChNum], THRArr40[ChNum], THRArr60[ChNum], THRArr80[ChNum], THRArr100[ChNum], THRArr120[ChNum], THRArr140[ChNum], THRArr160[ChNum], THRArr180[ChNum], THRArr200[ChNum], THRArr220[ChNum]]
        return Count17

def DataPrep25u (ChNum, mode):

    THRArrFile20 = []
    THRArrFile30 = []
    THRArrFile50 = []
    THRArrFile70 = []
    THRArrFile90 = []
    THRArrFile100 = []
    THRArrFile120 = []
    THRArrFile140 = []
    THRArrFile150 = []
    THRArrFile170 = []
    THRArrFile190 = []
    THRArrFile200 = []
    THRArrFile220 = []
    THRArrFile240 = []
    THRArrFile250 = []

    Count25 = []

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr20_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile20.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr30_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile30.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr50_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile50.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr70_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile70.extend(line.rstrip().split(':'))    

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr90_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile90.extend(line.rstrip().split(':'))
         
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr100_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile100.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr120_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile120.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr140_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile140.extend(line.rstrip().split(':'))      

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr150_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile150.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr170_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile170.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr190_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile190.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr200_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile200.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr220_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile220.extend(line.rstrip().split(':'))
    
    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr240_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile240.extend(line.rstrip().split(':'))

    with open ("/home/glushak/Desktop/SOCOD/SOCOD_thr250_25keV_100ms.txt",'r') as f:
        for line in f.readlines():
            THRArrFile250.extend(line.rstrip().split(':'))



    THRArr20, THRArrSensor20 = DataProcessing(THRArrFile20)
    THRArr30, THRArrSensor30 = DataProcessing(THRArrFile30)
    THRArr50, THRArrSensor50 = DataProcessing(THRArrFile50)
    THRArr70, THRArrSensor70 = DataProcessing(THRArrFile70)
    THRArr90, THRArrSensor90 = DataProcessing(THRArrFile90)
    THRArr100, THRArrSensor100 = DataProcessing(THRArrFile100)
    THRArr120, THRArrSensor120 = DataProcessing(THRArrFile120)
    THRArr140, THRArrSensor140 = DataProcessing(THRArrFile140)
    THRArr150, THRArrSensor150 = DataProcessing(THRArrFile150)
    THRArr170, THRArrSensor170 = DataProcessing(THRArrFile170)
    THRArr190, THRArrSensor190 = DataProcessing(THRArrFile190)
    THRArr200, THRArrSensor200 = DataProcessing(THRArrFile200)
    THRArr220, THRArrSensor220 = DataProcessing(THRArrFile220)
    THRArr240, THRArrSensor240 = DataProcessing(THRArrFile240)
    THRArr250, THRArrSensor250 = DataProcessing(THRArrFile250)

    #if (mode==False):
        #return THRArr20, THRArrSensor20, THRArr40, THRArrSensor40, THRArr60, THRArrSensor60, THRArr80, THRArrSensor80, THRArr100, THRArrSensor100, THRArr120, THRArrSensor120, THRArr140, THRArrSensor140, THRArr160, THRArrSensor160, THRArr180, THRArrSensor180, THRArr200, THRArrSensor200, THRArr220, THRArrSensor220

    if (mode==True):
        #Count25=[THRArrSensor20[ChNum], THRArrSensor30[ChNum],  THRArrSensor50[ChNum], THRArrSensor70[ChNum], THRArrSensor90[ChNum], THRArrSensor100[ChNum], THRArrSensor120[ChNum], THRArrSensor140[ChNum], THRArrSensor150[ChNum], THRArrSensor170[ChNum], THRArrSensor190[ChNum], THRArrSensor200[ChNum], THRArrSensor220[ChNum], THRArrSensor240[ChNum],THRArrSensor250[ChNum]]
        Count25=[THRArr20[ChNum], THRArr30[ChNum],  THRArr50[ChNum], THRArr70[ChNum], THRArr90[ChNum], THRArr100[ChNum], THRArr120[ChNum], THRArr140[ChNum], THRArr150[ChNum], THRArr170[ChNum], THRArr190[ChNum], THRArr200[ChNum], THRArr220[ChNum], THRArr240[ChNum],THRArr250[ChNum]]

        return Count25