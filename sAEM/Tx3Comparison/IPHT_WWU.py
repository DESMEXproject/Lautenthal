#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 18:51:18 2023

@author: nazari
"""

import numpy as np
from saem import CSEMSurvey, CSEMData

IPHT=CSEMData('Tx3IPHT_32_8_4BxByBz.npz')
WWU= CSEMData('Tx3WWU_4_8_16BxByBz.npz')
IPHT.showField("line",label='IPHT')
WWU.showField("line",label='WWU')



# %% Soundings

x=4000
y=0

IPHT.setPos(position=[x,y], show=True)
WWU.setPos(position=[x,y], show=True)

cmpx = [1, 0, 0]
cmpy = [0, 1, 0]
cmpz = [0, 0, 1]

ax=IPHT.showSounding(position=[x,y], cmp=cmpx, color="red", label="Bx IPHT")
IPHT.showSounding(position=[x,y], cmp=cmpy, color="g", label="By IPHT", ax=ax)
IPHT.showSounding(position=[x,y], cmp=cmpz, color="orange", label="Bz IPHT" , ax=ax)

ax=WWU.showSounding(position=[x,y], cmp=cmpx, color="red", label="Bx WWU")
WWU.showSounding(position=[x,y], cmp=cmpy, color="g", label="By WWU", ax=ax)
WWU.showSounding(position=[x,y], cmp=cmpz, color="orange", label="Bz WWU" , ax=ax)

ax=WWU.showSounding(position=[x,y], cmp=cmpx, color="red", label="Bx WWU")
IPHT.showSounding(position=[x,y], cmp=cmpx, color="g", label="Bx IPHT", ax=ax)

ax=WWU.showSounding(position=[x,y], cmp=cmpy, color="red", label="By WWU")
IPHT.showSounding(position=[x,y], cmp=cmpy, color="g", label="By IPHT", ax=ax)

ax=WWU.showSounding(position=[x,y], cmp=cmpz, color="red", label="Bz WWU")
IPHT.showSounding(position=[x,y], cmp=cmpz, color="g", label="Bz IPHT", ax=ax)
# %% remove Lines
# IPHT.line[IPHT.line==7] = 0
# IPHT.removeNoneLineData()
# WWU.line[WWU.line==5] = 0
# WWU.removeNoneLineData()
# IPHT.showField("line",label='IPHT')
# WWU.showField("line",label='WWU')
# %%
IPHTline=1.
WWUline=1.
# freqs=[32,64,128,256,521,1024]
IPHTfreq=[4,6,8,10,12,14]
WWUfreq= [13,11,9,7,5,3]

IPHT.showData(nf=IPHTfreq[5], amphi=False, radius=50.)
WWU.showData(nf=WWUfreq[5], amphi=False, radius=50.)

fig ,ax =IPHT.showLineFreq(line=IPHTline,nf=IPHTfreq[0])
WWU.showLineFreq(line=WWUline,nf=WWUfreq[0],ax=ax)

fig ,ax =IPHT.showLineFreq(line=IPHTline,nf=IPHTfreq[3])
WWU.showLineFreq(line=WWUline,nf=WWUfreq[3],ax=ax)

fig ,ax =IPHT.showLineFreq(line=IPHTline,nf=IPHTfreq[5])
WWU.showLineFreq(line=WWUline,nf=WWUfreq[5],ax=ax)


# %% Show Data after Denoising

IPHT.deactivateNoisyData(rErr=0.5)
IPHT.estimateError()  # 5%+1pV/A
IPHT.deactivateNoisyData(rErr=0.5)
# %% Show Data after Denoising

WWU.deactivateNoisyData(rErr=0.5)
WWU.estimateError()  # 5%+1pV/A
WWU.deactivateNoisyData(rErr=0.5)
# %%

fig ,ax =IPHT.showLineFreq(line=IPHTline,nf=IPHTfreq[5])
WWU.showLineFreq(line=WWUline,nf=WWUfreq[5],ax=ax)
# %%
print(IPHT.f)
print(WWU.f)
print(WWU.f[WWUfreq],IPHT.f[IPHTfreq])
