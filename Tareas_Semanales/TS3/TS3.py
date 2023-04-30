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
import module_MP as mp

from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

#wp=1
ws=2
alfa_max=1
alfa_min=12

N,D = mp.MP_aprox(ws, alfa_max, alfa_min)
T = TransferFunction(N, D)

bodePlot(T, fig_id=1)
pzmap(T, fig_id=2 )
GroupDelay(T, fig_id=3)