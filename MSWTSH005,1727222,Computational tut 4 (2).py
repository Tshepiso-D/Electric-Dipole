from __future__ import division
from vpython import*

##constants
oofpez=9e9
qproton=1.6e-19
print(" "+str(oofpez)+" ")
qelectron=-1.6e-19
Escale=0.0000000009
##objects
minus=sphere(pos=vector(-1e-9,0,0),radius=3e-10,color=vector(0,0,1),charge=-1.6e-19)
plus=sphere(pos=vector(1e-9,0,0),radius=3e-10,color=vector(1,0,0),charge=-1.6e-19)          
charges=[plus,minus]
locations=[vector(0,3e-9,0),vector(0,-3e-9,0),vector(3e-9,0,0),vector(-3e-9,0,0),vector(2.121e-9,2.121e-9,0),vector(2.121e-9,-2.121e-9,0),vector(-2.121e-9,-2.121e-9,0),vector(-2.121e-9,2.121e-9,0),vector(0,0,3e-9),vector(0,0,-3e-9),vector(3e-9,0,0),vector(-3e-9,0,0),vector(2.121e-9,0,2.121e-9),vector(2.121e-9,0,-2.121e-9),vector(-2.121e-9,0,2.121e-9),vector(-2.121e-9,0,-2.121e-9)]

##calculations
for pt in locations:
    re=pt-minus.pos
    print("relative position vector is "+str(re)+"")
    ##rearrow = arrow(pos=minus.pos,axis= re,color=color.green)
    remag=sqrt(re.x**2+re.y**2+re.z**2)
    print("magnitude of re is "+str(remag)+"")
    rehat=re/remag
    print("unit vector rehat is "+str(rehat)+"")

    rp=pt-plus.pos
    print("relative position vector is "+str(rp)+"")
    ##rparrow = arrow(pos=plus.pos,axis= rp,color=color.green)
    rpmag=sqrt(rp.x**2+rp.y**2+rp.z**2)
    print("magnitude of rp is "+str(rpmag)+"")
    rphat=rp/rpmag
    print("unit vector rphat is "+str(rphat)+"")

    Ep=oofpez*qproton*rphat/rpmag
    print("Electric field due to proton"+str(Ep)+"")
    Ee=oofpez*qelectron*rehat/remag
    print("Electric field due to electron"+str(Ee)+"")

    E=Ep+Ee
    Earrow = arrow(pos=pt,axis=E*Escale,color=color.orange)
    print("Electric field is "+str(E)+"")
