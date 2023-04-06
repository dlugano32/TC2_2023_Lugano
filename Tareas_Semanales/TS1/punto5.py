#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:54:01 2023

@author: dlugano
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

#Componentes
C1=1e-6
R1=1
R2=1
R3=1000

w0 = 1/(R3*C1)

plt.close('all')

my_tf = TransferFunction( [1, -R2/(R1*R3*C1)], [1, 1/(R3*C1)] )

bodePlot(my_tf, fig_id=1, filter_description = 'R1=R2 , C=1uF , R3=1K' )

pzmap(my_tf, fig_id=2, filter_description = 'R1=R2 , C=1uF , R3=1K' )
