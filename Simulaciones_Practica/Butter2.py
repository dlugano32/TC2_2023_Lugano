#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 22:49:10 2023

@author: dlugano
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import scipy.signal as sig
import numpy as np

from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot, analyze_sys, pretty_print_lti, tf2sos_analog, pretty_print_SOS
from pytc2.general import print_latex, print_subtitle

#wp=1
ws=2.16
alpha_max=3
alpha_min=20

xi = ( np.sqrt( 10**(alpha_max / 10) - 1 ))    #Por lo general w_p=1    
order=np.ceil( 0.5 * ( np.log10( ( 10**(alpha_min * 0.1) - 1 ) / xi**2)  / np.log10(ws) ) ) 
z,p,k = sig.buttap (order)
N, D = sig.zpk2tf(z, p, k)
N,D = sig.lp2bp(3.16*N,D, 1, 0.45)

T = TransferFunction(N, D)
z,p,k=sig.tf2zpk(N, D)

bodePlot(T, fig_id=1)
pzmap(T, fig_id=2 )
GroupDelay(T, fig_id=3)