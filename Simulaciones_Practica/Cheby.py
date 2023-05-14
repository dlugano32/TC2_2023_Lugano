#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:34:22 2023

@author: dlugano
"""
import scipy.signal as sig
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot


alfa_max = 0.4
ws = 3

# cuentas auxiliares

# epsilon cuadrado
ee = 10**(alfa_max/10)-1

alfa_min_c=[]

for nn in range(2,9):
    alfa_min_c.append(10*np.log10(1 + ee * np.cosh(nn * np.arccosh(ws))**2 ))

# elijo un orden luego de iterar ...
nn = 5

# verificación Cheby
z,p,k = sig.cheb1ap(nn, alfa_max)
num_cheb, den_cheb = sig.zpk2tf(z,p,k)

T=TransferFunction(num_cheb, den_cheb)

bodePlot(T, fig_id=1)
pzmap(T, fig_id=2 )
GroupDelay(T, fig_id=3)
