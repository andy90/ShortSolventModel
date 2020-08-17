# plot the ion-ion pmf between the ions in the target, GT and LMF system

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from matplotlib import rc, font_manager
import scipy.integrate as integrate

pmf_1=np.loadtxt("pmf_1.xvg",unpack=True)
pmf_125=np.loadtxt("pmf_125.xvg",unpack=True)
pmf_150=np.loadtxt("pmf_150.xvg",unpack=True)
pmf_175=np.loadtxt("pmf_175.xvg",unpack=True)
pmf_185=np.loadtxt("pmf_185.xvg",unpack=True)
pmf_195=np.loadtxt("pmf_195.xvg",unpack=True)
pmf_2=np.loadtxt("pmf_2.xvg",unpack=True)




pmf_1=interp.InterpolatedUnivariateSpline(pmf_1[0,:],pmf_1[1,:])
pmf_125=interp.InterpolatedUnivariateSpline(pmf_125[0,:],pmf_125[1,:])
pmf_150=interp.InterpolatedUnivariateSpline(pmf_150[0,:],pmf_150[1,:])
pmf_175=interp.InterpolatedUnivariateSpline(pmf_175[0,:],pmf_175[1,:])
pmf_185=interp.InterpolatedUnivariateSpline(pmf_185[0,:],pmf_185[1,:])
pmf_195=interp.InterpolatedUnivariateSpline(pmf_195[0,:],pmf_195[1,:])
pmf_2=interp.InterpolatedUnivariateSpline(pmf_2[0,:],pmf_2[1,:])

kT=300.0/120.0

plt.rc('text', usetex=True)
plt.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman']})

r=np.linspace(0.23,1.25,500)
plt.figure()
ax1 = plt.subplot(111)
ax1.plot(r,np.exp(-(pmf_1(r)-pmf_1(1.25))),color="black",lw=3,label="Q=1")
ax1.plot(r,np.exp(-(pmf_125(r)-pmf_125(1.25))),color='red',ls='--',lw=3,dashes=(8, 8),label="Q=1.25")
ax1.plot(r,np.exp(-(pmf_150(r)-pmf_150(1.25))),color='green',ls='--',lw=3,dashes=(4, 4),label="Q=1.5")
ax1.plot(r,np.exp(-(pmf_175(r)-pmf_175(1.25))),color='magenta',ls='--',lw=3,dashes=(2, 2),label="Q=1.75")
ax1.plot(r,np.exp(-(pmf_185(r)-pmf_185(1.25))),color='cyan',ls='--',lw=3,dashes=(1, 1),label="Q=1.85")
ax1.plot(r,np.exp(-(pmf_195(r)-pmf_195(1.25))),color='brown',ls='--',lw=3,dashes=(0.5, 0.5),label="Q=1.95")
ax1.plot(r,np.exp(-(pmf_2(r)-pmf_2(1.25))),color='blue',ls='--',lw=3,dashes=(0.2, 0.2),label="Q=2.0")


#ax1.plot(np.linspace(0.2,1.25,100),np.ones(100),color='black',ls='--',dashes=(16,16))

legend=ax1.legend(bbox_to_anchor=(0.65, 1.01),prop={'size':18})
frame=legend.get_frame()


ax1.tick_params(axis='both', which='major',length=5, pad=12,top='off', right='off')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r"$r$(nm)",fontsize=25)
plt.xlim(0.2,0.6)
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig("rdfNaCl_increasecharge.pdf")
plt.show()