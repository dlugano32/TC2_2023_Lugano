#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:34:22 2023

@author: dlugano
"""
import numpy as np
import matplotlib as mpl
import scipy.signal as sig
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction

from pytc2.sistemas_lineales import analyze_sys, pretty_print_lti, tf2sos_analog, pretty_print_SOS
from pytc2.general import print_latex, print_subtitle
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot


alfa_max = 1
ws = 4

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
num_cheb, den_cheb = sig.lp2hp(num_cheb, den_cheb ) #Esta funcion cambia el filtro para otra frecuencia. Es la renormalización del filtro para epsilon distinto de 1

T=TransferFunction(num_cheb, den_cheb)

bodePlot(T, fig_id=1)
pzmap(T, fig_id=2 )
GroupDelay(T, fig_id=3)
