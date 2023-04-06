#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:39:34 2023

@author: dlugano
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

#Componentes
C1=1
R1=[1,1,2]
R2=[1,2,1]
R3=1

w0 = 1/(R3*C1)

plt.close('all')


for ii in range(len(R1)):
    
    my_tf = TransferFunction( [1, -R2[ii]/(R1[ii]*R3*C1)], [1, 1/(R3*C1)] )
    
    bodePlot(my_tf, fig_id=1, filter_description = 'R1={:d} ; R2={:d}'.format(R1[ii], R2[ii])  )
    
    pzmap(my_tf, fig_id=2, filter_description = 'R1={:d} ; R2={:d}'.format(R1[ii], R2[ii]) )
