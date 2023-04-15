#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:01:12 2023

@author: dlugano
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

#Red normalizada
R1=1/10
R2=3
R3=1 #Norma de impedancia
C=1

w0=1/C*R3 #Frecuencia normalizada -> Norma de frec wo=1/(C*R3)
Q=C*R2

K=1/((C**2)*R1*R3)

plt.close('all')
    
Tf=TransferFunction([K], [1, w0/Q, w0**2])
bodePlot(Tf, fig_id=1 )
pzmap(Tf, fig_id=2 )
GroupDelay(Tf, fig_id=3)


