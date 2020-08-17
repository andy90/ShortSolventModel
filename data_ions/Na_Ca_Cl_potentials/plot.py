# plot the ion-ion pmf between the ions in the target, GT and LMF system

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from matplotlib import rc, font_manager
import scipy.integrate as integrate

pmf_pn_target=np.loadtxt("pmf_CaCl.xvg",unpack=True)
pmf_pn_GT=np.loadtxt("pmf_CaCl_GT.xvg",unpack=True)

VR1pnEwald=np.loadtxt("VR1CaCl_Ewald.txt",unpack=True)


pmf_target=interp.InterpolatedUnivariateSpline(pmf_pn_target[0,:],pmf_pn_target[1,:])
pmf_GT=interp.InterpolatedUnivariateSpline(pmf_pn_GT[0,:],pmf_pn_GT[1,:])
VR1=interp.InterpolatedUnivariateSpline(VR1pnEwald[0,:],VR1pnEwald[1,:])

kT=300.0/120.0

plt.rc('text', usetex=True)
plt.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman']})

r=np.linspace(0.26,1.25,100)
plt.figure()
ax1 = plt.subplot(111)
ax1.plot(r,np.exp(-(pmf_target(r)-pmf_target(1.25))),color="black",lw=3,label=r"$g_{\mathrm{CaCl}}(r) $")
ax1.plot(r,np.exp(-(pmf_GT(r)-pmf_GT(1.25)+(VR1(r)-VR1(1.25))/kT*138.9)),color='red',ls='--',lw=3,dashes=(8, 8),label=r"$g_{\tilde{R},\mathrm{CaCl}}(r) $")
ax1.plot(r,np.exp(-(pmf_GT(r)-pmf_GT(1.25))),color='green',ls='-.',lw=3,dashes=(2, 2),label=r"$g_{0,\mathrm{CaCl}}(r) $")
ax1.plot(np.linspace(0.2,1.25,100),np.ones(100),color='black',ls='--',dashes=(16,16))

legend=ax1.legend(bbox_to_anchor=(1, 1),prop={'size':25})
frame=legend.get_frame()


ax1.tick_params(axis='both', which='major',length=5, pad=12,top='off', right='off')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r"$r$(nm)",fontsize=25)
plt.xlim(0.2,1.25)
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig("rdf_CaCl.pdf")
plt.show()