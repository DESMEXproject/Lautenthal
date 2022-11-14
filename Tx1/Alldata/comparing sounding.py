#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:46:05 2022

@author: nazari
"""
import numpy as np
from saem import CSEMData
# %% comparing sounding

# txpos = np.genfromtxt("Tx1.pos").T[:, ::-1]
# data1 = CSEMData(datafile="Tx1_1/tf/*.mat", txPos=txpos) # 1 Cycle
# data1.setOrigin([580000., 5740000.])
# data1.filter(fmin=12, fmax=2000)

txpos = np.genfromtxt("Tx1.pos").T[:, ::-1]
data2 = CSEMData(datafile="Tx1_2/*.mat", txPos=txpos) # 2 Cycle
data2.setOrigin([580000., 5740000.])
data2.filter(fmin=12, fmax=2000)

txpos = np.genfromtxt("Tx1.pos").T[:, ::-1]
data4 = CSEMData(datafile="Tx1_4/*.mat", txPos=txpos) # 4 Cycle
data4.setOrigin([580000., 5740000.])
data4.filter(fmin=12, fmax=2000)

txpos = np.genfromtxt("Tx1.pos").T[:, ::-1]
data8 = CSEMData(datafile="Tx1_8/*.mat", txPos=txpos) # 8 Cycle
data8.setOrigin([580000., 5740000.])
data8.filter(fmin=12, fmax=2000)

# txpos = np.genfromtxt("Tx1.pos").T[:, ::-1]
# data16 = CSEMData(datafile="Tx1_16/tf/*.mat", txPos=txpos) # 16 Cycle
# data16.setOrigin([580000., 5740000.])
# data16.filter(fmin=12, fmax=2000)

txpos = np.genfromtxt("Tx1.pos").T[:, ::-1]
data32 = CSEMData(datafile="Tx1_32/*.mat", txPos=txpos) # 32 Cycle
data32.setOrigin([580000., 5740000.])
data32.filter(fmin=12, fmax=2000)

# txpos = np.genfromtxt("Tx1.pos").T[:, ::-1]
# data64 = CSEMData(datafile="Tx1_64/tf/*.mat", txPos=txpos) # 64 Cycle
# data64.setOrigin([580000., 5740000.])
# data64.filter(fmin=12, fmax=2000)

x=8000
y=12000

data2.setPos(position=[x,y], show=True)
data4.setPos(position=[x,y], show=True)
data8.setPos(position=[x,y], show=True)
data32.setPos(position=[x,y], show=True)
# data64.setPos(position=[x,y], show=True)

print(data32.rx[data32.nrx],data4.rx[data4.nrx],data8.rx[data8.nrx])
print(data32.ry[data32.nrx],data4.ry[data4.nrx],data8.ry[data8.nrx])

# %% Bx

cmpx = [1, 0, 0]
ax = data2.showSounding(position=[x,y], cmp=cmpx, color="g", label="Bx (N=2)")
data4.showSounding(position=[x,y], cmp=cmpx, color="orange", label="Bx (N=4)", ax=ax)
data8.showSounding(position=[x,y], cmp=cmpx, color="k", label="Bx (N=8)", ax=ax)
# data16.showSounding(position=[x,y], cmp=cmpx, color="lightblue", label="Bx (N=16)", ax=ax)
data32.showSounding(position=[x,y], cmp=cmpx, color="blue", label="Bx (N=32)", ax=ax)
# data64.showSounding(position=[x,y], cmp=cmpx, color="m", label="Bx (N=64)", ax=ax)

# %% By

cmpy = [0, 1, 0]
ax = data2.showSounding(position=[x,y], cmp=cmpy, color="g", label="By (N=2)")
data4.showSounding(position=[x,y], cmp=cmpy, color="orange", label="By (N=4)" , ax=ax)
data8.showSounding(position=[x,y], cmp=cmpy, color="k", label="By (N=8)", ax=ax)
# data16.showSounding(position=[x,y], cmp=cmpy, color="lightblue", label="By (N=16)", ax=ax)
data32.showSounding(position=[x,y], cmp=cmpy, color="blue", label="By (N=32)", ax=ax)
# data64.showSounding(position=[x,y], cmp=cmpy, color="m", label="By (N=64)", ax=ax)

# %% Bz

cmpz = [0, 0, 1]
ax = data2.showSounding(position=[x,y], cmp=cmpz, color="g", label="Bz (N=2)")
data4.showSounding(position=[x,y], cmp=cmpz, color="orange", label="Bz (N=4)", ax=ax)
data8.showSounding(position=[x,y], cmp=cmpz, color="k", label="Bz (N=8)", ax=ax)
# data16.showSounding(position=[x,y], cmp=cmpz, color="lightblue", label="Bz (N=16)", ax=ax)
data32.showSounding(position=[x,y], cmp=cmpz, color="blue", label="Bz (N=32)", ax=ax)
# data64.showSounding(position=[x,y], cmp=cmpz, color="m", label="Bz (N=64)", ax=ax)

# %% All
ax = data4.showSounding(position=[x,y], cmp=cmpx, color="blue", label="Bx (N=4)")
data32.showSounding(position=[x,y], cmp=cmpx, color="lightblue", label="Bx (N=32)", ax=ax)
ax=data4.showSounding(position=[x,y], cmp=cmpy, color="red", label="By (N=4)", ax=ax)
data32.showSounding(position=[x,y], cmp=cmpy, color="orange", label="By (N=32)", ax=ax)
ax=data4.showSounding(position=[x,y], cmp=cmpz, color="g", label="Bz (N=4)", ax=ax)
data32.showSounding(position=[x,y], cmp=cmpz, color="m", label="Bz (N=32)", ax=ax)