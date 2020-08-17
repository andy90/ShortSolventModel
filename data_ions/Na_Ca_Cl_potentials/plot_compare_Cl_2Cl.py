# compare the pmf Ca Cl with one or 2 Cl in the box

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from matplotlib import rc, font_manager
import scipy.integrate as integrate

pmf1Cl=np.loadtxt("pmf_CaCl.xvg",unpack=True)
pmf2Cl=np.loadtxt("pmf_CaCl_2Cl.xvg",unpack=True)

pmf1=interp.InterpolatedUnivariateSpline(pmf1Cl[0],pmf1Cl[1])
pmf2=interp.InterpolatedUnivariateSpline(pmf2Cl[0],pmf2Cl[1])

kT=300.0/120.0

plt.rc('text', usetex=True)
plt.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman']})

r=np.linspace(0.26,1.25,100)
plt.figure()
ax1 = plt.subplot(111)
ax1.plot(r,np.exp(-(pmf1(r)-pmf1(1.25))),color="black",lw=3,label=r"$g_{\mathrm{CaCl}}(r) $")
ax1.plot(r,np.exp(-(pmf2(r)-pmf2(1.25))),color="blue",lw=3,label=r"$g_{\mathrm{CaCl}}(r) $, 2 Cl")

legend=ax1.legend(bbox_to_anchor=(1, 1),prop={'size':20})
frame=legend.get_frame()


ax1.tick_params(axis='both', which='major',length=5, pad=12,top='off', right='off')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r"$r$(nm)",fontsize=25)
plt.xlim(0.2,1.25)
plt.ylim(0,7)
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig("comp_2Cl.pdf")
plt.show()