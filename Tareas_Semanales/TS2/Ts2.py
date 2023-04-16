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
R2=[3, 1/np.sqrt(2)]
R3=1 #Norma de impedancia
C=1

w0=1/C*R3 #Frecuencia normalizada -> Norma de frec wo=1/(C*R3)
Q=[C*R2[0], C*R2[1]]

K=1/((C**2)*R1*R3)

plt.close('all')

#Filtro Pasabajo generico con Q=3 y w0=1
TFPB=TransferFunction([K], [1, w0/Q[0], w0**2])
bodePlot(TFPB, fig_id=1)
pzmap(TFPB, fig_id=2 )
GroupDelay(TFPB, fig_id=3)

#Filtro Butterworth de segundo orden
TFPBbut=TransferFunction([K], [1, w0/Q[1], w0**2])
bodePlot(TFPBbut, fig_id=5)
pzmap(TFPBbut, fig_id=6 )
GroupDelay(TFPBbut, fig_id=7)

#Filtro Pasabanda
TFPBand=TransferFunction([1/(C*R1), 0], [1, w0/Q[0], w0**2])
bodePlot(TFPBand, fig_id=8 )
pzmap(TFPBand, fig_id=9 )
GroupDelay(TFPBand, fig_id=10 )


