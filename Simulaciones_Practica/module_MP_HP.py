#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:53:37 2023

@author: dlugano
"""

import numpy as np
import scipy.signal as sig

def MP_aprox_hp(ws, alpha_max, alpha_min):    #Funciones de aproximacion por maxima planicida:

    xi = ( np.sqrt( 10**(alpha_max / 10) - 1 ))    #Por lo general w_p=1    

    order=np.ceil( 0.5 * ( np.log10( ( 10**(alpha_min * 0.1) - 1 ) / xi**2)  / np.log10(ws) ) ) 

    z,p,k = sig.buttap (order)
    N, D = sig.zpk2tf(z, p, k)
    N, D = sig.lp2hp(N, D, xi**(-1/order) ) #Esta funcion cambia el filtro para otra frecuencia. Es la renormalización del filtro para epsilon distinto de 1
    
    z,p,k=sig.tf2zpk(N,D)
    
    return N, D
