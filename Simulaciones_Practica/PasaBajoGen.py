#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 13:30:16 2023

@author: dlugano
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

w0=1
H=2 # Nivel en la banda de paso

plt.close('all')

qq_parametro=[0.5, np.sqrt(2)/2, 10]

for qq in range(len(qq_parametro)):
    
    Tf=TransferFunction(H*[w0**2], [1, w0/qq_parametro[qq], w0**2])
    bodePlot(Tf, fig_id=1, filter_description='Q={:3.3f}'.format(qq_parametro[qq]) )
    pzmap(Tf, fig_id=2, filter_description='Q={:3.3f}'.format(qq_parametro[qq]) )


