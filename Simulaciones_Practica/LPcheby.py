from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as ss

from pytc2.sistemas_lineales import analyze_sys, pretty_print_bicuad_omegayq, tf2sos_analog, pretty_print_SOS

from pytc2.general import print_subtitle

#----------------------Definicion de las variables---------------------

xi = 0.349
n = 3
alpha_max = 0.5

#---------------------------Definicion de H-------------------------

[z, p, k] = ss.cheb1ap(n, alpha_max)
[num, den] = ss.zpk2tf(z, p, k)

sos_lp = tf2sos_analog(num, den)
sos_lp[sos_lp < 1e-6] = 0.0

#-----------------------------Visualizacion----------------------------

pretty_print_SOS(sos_lp, mode='omegayq')
print("z = ", z, "\n", "p = ", p, "\n", "k =", k)
analyze_sys(sos_lp, "Cheby")
  
