#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:39:56 2023

@author: dlugano
"""
# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
import module_MP_HP as mp2

from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

#wp=1
ws=4
alfa_max=1
alfa_min=30

N,D = mp2.MP_aprox_hp(ws, alfa_max, alfa_min)
T = TransferFunction(N, D)


bodePlot(T, fig_id=1)
pzmap(T, fig_id=2 )
GroupDelay(T, fig_id=3)