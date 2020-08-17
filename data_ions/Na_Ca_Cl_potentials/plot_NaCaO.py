# compare rdfNaO rdfCaO

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from matplotlib import rc, font_manager
import scipy.integrate as integrate

rrdfNaO=np.loadtxt("rdfNaO.xvg",unpack=True)
rrdfCaO=np.loadtxt("rdfCaO.xvg",unpack=True)


plt.rc('text', usetex=True)
plt.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman']})
plt.figure()
ax1 = plt.subplot(111)
ax1.plot(rrdfCaO[0,:],rrdfCaO[1,:],color="red",lw=3,label=r"$g_{\mathrm{CaO}}(r) $")
ax1.plot(rrdfNaO[0,:],rrdfNaO[1,:],color="blue",lw=3,label=r"$g_{\mathrm{NaO}}(r) $")

legend=ax1.legend(bbox_to_anchor=(1, 1),prop={'size':25})
frame=legend.get_frame()


ax1.tick_params(axis='both', which='major',length=5, pad=12,top='off', right='off')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r"$r$(nm)",fontsize=25)
plt.xlim(0.2,0.6)
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig("rdf_NaCaO.pdf")
plt.show()