#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:46:05 2022

@author: nazari
"""
import numpy as np
from saem import CSEMData
# %% reading Data

txpos = np.genfromtxt("Tx1.pos").T[:, ::-1]
Nvec = [2, 4, 8, 32]
DATA = []
for i in Nvec:
    data = CSEMData(datafile=f"tfN{i}/*.mat", txPos=txpos) 
    data.setOrigin([580000., 5740000.])
    data.filter(fmin=12, fmax=2000)
    DATA.append(data)

# %% sounding position

x=8000
y=12000

for data in DATA:
    data.setPos(position=[x, y])

data.showPos()
print([data.rx[data.nrx] for data in DATA])
print([data.ry[data.nrx] for data in DATA])

# %% components

cmpx = [1, 0, 0]
cmpy = [0, 1, 0]
cmpz = [0, 0, 1]

# %% 
cols = ["green", "orange", "black", "blue"]
for cmp, xx in zip([cmpx, cmpy, cmpz], ["x", "y", "z"]):
    ax = DATA[0].showSounding(cmp=cmp, color=cols[0], label=f"B{xx} (N={Nvec[0]})")
    for i in range(1, len(DATA)):
        DATA[i].showSounding(cmp=cmp, color=cols[i], label=f"B{xx} (N={Nvec[i]})", ax=ax)

# %%
ax = DATA[2].showSounding(cmp=cmpx, color="blue", label="Bx (N=4)")
DATA[3].showSounding(cmp=cmpx, color="lightblue", label="Bx (N=32)", ax=ax)
ax=DATA[2].showSounding(cmp=cmpy, color="red", label="By (N=4)", ax=ax)
DATA[3].showSounding(cmp=cmpy, color="orange", label="By (N=32)", ax=ax)
ax=DATA[2].showSounding(cmp=cmpz, color="green", label="Bz (N=4)", ax=ax)
DATA[3].showSounding(cmp=cmpz, color="lightgreen", label="Bz (N=32)", ax=ax);

# %% Show Data before Denoising
for f in range(0, len(data.f)):
    data.showData(nf=f, amphi=False )
# %% Show Data after Denoising
data.deactivateNoisyData(rErr=0.5)
data.estimateError()  # 5%+1pV/A
data.deactivateNoisyData(rErr=0.5)

for f in range(0, len(data.f)):
    data.showData(nf=f, amphi=False)