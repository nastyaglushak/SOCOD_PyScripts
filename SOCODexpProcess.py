import re
import numpy as np
from matplotlib import pyplot as plt
from array import *

from SOCODexpProcessFun import DataPrep10, DataPrep17, DataPrep25, DataDraw, CountChar, CountCharAll
from SOCODexpProcessFunUsual import DataPrep10u, DataPrep17u, DataPrep25u

#Narrow beam
#10keV
THRmass10 = [10, 20, 30, 40, 50, 70, 90, 110 ]

ChNum1=75
ChNum2=63

#THRArr10, THRArrSensor10, THRArr20, THRArrSensor20, THRArr30, THRArrSensor30, THRArr40, THRArrSensor40, THRArr50, THRArrSensor50, THRArr70, THRArrSensor70, THRArr90, THRArrSensor90, THRArr110, THRArrSensor110 = DataPrep10(ChNum1,False)

#DataDraw (THRArr10, THRArrSensor10)

Count10_1 = DataPrep10(ChNum1,True)
Count10_2 = DataPrep10(ChNum2,True)

#CountChar(THRmass10, Count10_1, Count10_2, ChNum1, ChNum2)

#17keV
THRmass17 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180 ]

ChNum1_17=75
ChNum2_17=63

THRArr10, THRArrSensor10, THRArr20, THRArrSensor20, THRArr30, THRArrSensor30, THRArr40, THRArrSensor40, THRArr50, THRArrSensor50, THRArr60, THRArrSensor60, THRArr70, THRArrSensor70, THRArr80, THRArrSensor80, THRArr90, THRArrSensor90, THRArr100, THRArrSensor100, THRArr120, THRArrSensor120, THRArr140, THRArrSensor140, THRArr160, THRArrSensor160, THRArr180, THRArrSensor180 = DataPrep17(ChNum1_17,False)

#DataDraw (THRArr90, THRArrSensor90)

Count17_1 = DataPrep17(ChNum1_17,True)
Count17_2 = DataPrep17(ChNum2_17,True)

#CountChar(THRmass17, Count17_1, Count17_2, ChNum1_17, ChNum2_17)

#25keV
THRmass25 = [20, 40, 60, 80, 100, 120, 140, 160 ]

ChNum1_25=75#41#75
ChNum2_25=63#65#63

Count25_1 = DataPrep25(ChNum1_25,True)
Count25_2 = DataPrep25(ChNum2_25,True)

#CountChar(THRmass25, Count25_1, Count25_2, ChNum1_25, ChNum2_25)
CountCharAll(THRmass10, Count10_1, Count10_2, THRmass17, Count17_1, Count17_2, THRmass25, Count25_1, Count25_2,ChNum1_25,ChNum2_25)

#Usual beam
THRmass10u = [40, 60, 80, 100, 120, 140, 160, 180, 200, 220 ]

ChNum1_10u=75
ChNum2_10u=63

Count10u_1 = DataPrep10u(ChNum1_10u,True)
Count10u_2 = DataPrep10u(ChNum2_10u,True)

#CountChar(THRmass10u, Count10u_1, Count10u_2, ChNum1_10u, ChNum2_10u)

THRmass17u = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220 ]

ChNum1_17u=75
ChNum2_17u=63

Count17u_1 = DataPrep17u(ChNum1_17u,True)
Count17u_2 = DataPrep17u(ChNum2_17u,True)

#CountChar(THRmass17u, Count17u_1, Count17u_2, ChNum1_17u, ChNum2_17u)

THRmass25u = [20, 30, 50, 70, 90, 100, 120, 140, 150, 170, 190, 200, 220, 240, 250 ]

ChNum1_25u=75
ChNum2_25u=63

Count25u_1 = DataPrep25u(ChNum1_25u,True)
Count25u_2 = DataPrep25u(ChNum2_25u,True)

#CountChar(THRmass25u, Count25u_1, Count25u_2, ChNum1_25u, ChNum2_25u)
CountCharAll(THRmass10u, Count10u_1, Count10u_2, THRmass17u, Count17u_1, Count17u_2, THRmass25u, Count25u_1, Count25u_2, ChNum1_25u, ChNum2_25u)
