# plot the ion-ion pmf between the ions in the target, GT and LMF system

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from matplotlib import rc, font_manager
import scipy.integrate as integrate



VR1pn_Ewald_NaCl=np.loadtxt("VR1NaCl_Ewald.txt",unpack=True)
VR1pn_Ewald_CaCl=np.loadtxt("VR1CaCl_Ewald.txt",unpack=True)

fVR1pn_Ewald_NaCl=interp.InterpolatedUnivariateSpline(VR1pn_Ewald_NaCl[0,:],VR1pn_Ewald_NaCl[1,:])
fVR1pn_Ewald_CaCl=interp.InterpolatedUnivariateSpline(VR1pn_Ewald_CaCl[0,:],VR1pn_Ewald_CaCl[1,:])

plt.rc('text', usetex=True)
plt.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman']})

r=np.linspace(0.2,2.98/2,100)
plt.figure()
ax1 = plt.subplot(111)
#ax1.plot(r,138.935485*(fVR1pn(r)-fVR1pn(2.98/2)),color="black",lw=3,label=r"$q_{\mathrm{Na}}q_{\mathrm{Cl}}v_{\tilde{R}1,\mathrm{NaCl}}(r) $")
#ax1.plot(r,138.935485*(fVR1pn_Ewald(r)-fVR1pn_Ewald(2.98/2)),color='red',ls='--',lw=3,dashes=(8, 8),label=r"$\phi^{\mathrm{Ewald}}_{\tilde{R}1,\mathrm{NaCl}}(r) $")

ax1.plot(r,138.935485*(fVR1pn_Ewald_NaCl(r)-fVR1pn_Ewald_NaCl(2.98/2)),color="black",lw=3,label=r"$\phi^{\mathrm{Ewald}}_{\tilde{R}1,\mathrm{NaCl}}(r) $")
ax1.plot(r,138.935485*(fVR1pn_Ewald_CaCl(r)-fVR1pn_Ewald_CaCl(2.98/2)),color='red',ls='--',lw=3,dashes=(8, 8),label=r"$\phi^{\mathrm{Ewald}}_{\tilde{R}1,\mathrm{CaCl}}(r) $")

legend=ax1.legend(bbox_to_anchor=(1, 0.49),prop={'size':25})
frame=legend.get_frame()


ax1.tick_params(axis='both', which='major',length=5, pad=12,top='off', right='off')
plt.xticks( fontsize = 15)
plt.yticks( fontsize = 15)
plt.xlabel(r"$r$(nm)",fontsize=20)
plt.ylabel(r"kJ/mole",fontsize=19)
plt.xlim(0.2,1.49)
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig("VR1pn_2.pdf")
plt.show()
