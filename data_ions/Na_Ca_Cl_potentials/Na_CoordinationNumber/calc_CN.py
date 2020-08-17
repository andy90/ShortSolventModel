# this python file is used to calculate the coordination number around the Na ion

import numpy as np
import matplotlib.pyplot as plt

def funcsprik(k,rc,r):
	f=1.0/(1.0+np.exp(k*(r-rc)))
	return f

r1,rdf1=np.loadtxt("rdfNaO_1.xvg",unpack=True)
r125,rdf125=np.loadtxt("rdfNaO_125.xvg",unpack=True)
r150,rdf150=np.loadtxt("rdfNaO_150.xvg",unpack=True)
r175,rdf175=np.loadtxt("rdfNaO_175.xvg",unpack=True)
r185,rdf185=np.loadtxt("rdfNaO_185.xvg",unpack=True)
r195,rdf195=np.loadtxt("rdfNaO_195.xvg",unpack=True)
r2,rdf2=np.loadtxt("rdfNaO_2.xvg",unpack=True)

rc1=0.322
rc125=0.316 # position of the first minimum of rdfNaO
rc150=0.308
rc175=0.318
rc185=0.318
rc195=0.308
rc2=0.31

rhobulk1=881.0/2.97947**3
rhobulk125=881.0/2.97914**3
rhobulk150=881.0/2.97949**3
rhobulk175=881.0/2.97932**3
rhobulk185=881.0/2.97964**3
rhobulk195=881.0/2.97936**3
rhobulk2=881.0/2.97901**3

k=100

CN1=0.0
delr=0.002
for i in range(len(r1)-1):
	#if (r1[i+1]<rc1):
	#	CN1+=(rdf1[i]+rdf1[i+1])/2*4*np.pi*(0.001+i*delr)**2*delr*rhobulk1
	ri=0.001+i*delr
	CN1+=(rdf1[i]+rdf1[i+1])/2*4*np.pi*(ri)**2*delr*rhobulk1*funcsprik(k,rc1,ri)

CN125=0.0
delr=0.002
for i in range(len(r125)-1):
	#if (r125[i+1]<rc125):
	#	CN125+=(rdf125[i]+rdf125[i+1])/2*4*np.pi*(0.001+i*delr)**2*delr*rhobulk125
	ri=0.001+i*delr
	CN125+=(rdf125[i]+rdf125[i+1])/2*4*np.pi*(ri)**2*delr*rhobulk125*funcsprik(k,rc125,ri)

CN150=0.0
for i in range(len(r150)-1):
	#if (r150[i+1]<rc150):
	#	CN150+=(rdf150[i]+rdf150[i+1])/2*4*np.pi*(0.001+i*delr)**2*delr*rhobulk150
	ri=0.001+i*delr
	CN150+=(rdf150[i]+rdf150[i+1])/2*4*np.pi*(ri)**2*delr*rhobulk150*funcsprik(k,rc150,ri)

CN175=0.0
for i in range(len(r175)-1):
	#if (r175[i+1]<rc175):
	#	CN175+=(rdf175[i]+rdf175[i+1])/2*4*np.pi*(0.001+i*delr)**2*delr*rhobulk175
	ri=0.001+i*delr
	CN175+=(rdf175[i]+rdf175[i+1])/2*4*np.pi*(ri)**2*delr*rhobulk175*funcsprik(k,rc175,ri)

CN185=0.0
for i in range(len(r185)-1):
	#if (r175[i+1]<rc175):
	#	CN175+=(rdf175[i]+rdf175[i+1])/2*4*np.pi*(0.001+i*delr)**2*delr*rhobulk175
	ri=0.001+i*delr
	CN185+=(rdf185[i]+rdf185[i+1])/2*4*np.pi*(ri)**2*delr*rhobulk185*funcsprik(k,rc185,ri)

CN195=0.0
for i in range(len(r195)-1):
	#if (r175[i+1]<rc175):
	#	CN175+=(rdf175[i]+rdf175[i+1])/2*4*np.pi*(0.001+i*delr)**2*delr*rhobulk175
	ri=0.001+i*delr
	CN195+=(rdf195[i]+rdf195[i+1])/2*4*np.pi*(ri)**2*delr*rhobulk195*funcsprik(k,rc195,ri)

CN2=0.0
for i in range(len(r2)-1):
	#if (r2[i+1]<rc2):
	#	CN2+=(rdf2[i]+rdf2[i+1])/2*4*np.pi*(0.001+i*delr)**2*delr*rhobulk2
	ri=0.001+i*delr
	CN2+=(rdf2[i]+rdf2[i+1])/2*4*np.pi*(ri)**2*delr*rhobulk2*funcsprik(k,rc2,ri)


print "CN1",CN1
print "CN125",CN125
print "CN150",CN150
print "CN175",CN175
print "CN185",CN185
print "CN195",CN195
print "CN2",CN2


plt.plot([1,1.25,1.5,1.75,1.85,1.95,2],[CN1,CN125,CN150,CN175,CN185,CN195,CN2],"o",ms=12)
plt.ylim(4,6)
plt.xlim(1,2)
plt.xlabel(r"$Q_{Na}$",fontsize=20)
plt.ylabel("Coordinate Number around Na",fontsize=20)
plt.savefig("CN_Q.pdf")
plt.show()