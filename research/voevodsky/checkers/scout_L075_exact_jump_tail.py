#!/usr/bin/env python3
"""Exact step-coefficient scout for the extracted L=.75 prime jumps."""
import json,math
from pathlib import Path
import numpy as np
L=.75;jumps=[(.05685281944005469,8.111559538921806e-8),(-.05685281944005469,-8.111559538921806e-8),(-.3486122886681097,1.0497302737793973e-7),(.3486122886681097,-1.0497302737793973e-7),(-.6362943611198906,5.735738755970034e-8),(.6362943611198906,-5.735738755970034e-8)];N=200000;coef=np.zeros(N)
for x,J in jumps:
 y=x/L;p0=1.;p1=y
 for n in range(1,N-1):
  p2=((2*n+1)*y*p1-n*p0)/(n+1)
  # coefficient degree n uses P_(n-1)-P_(n+1)
  coef[n]+=J*math.sqrt((2*n+1)/(2*L))*L*(p0-p2)/(2*n+1);p0,p1=p1,p2
rows=[]
for m in (1000,2000,5000,10000,50000,100000,200000):rows.append({'exclusive_upper':m,'norm_1000_to_upper':float(np.linalg.norm(coef[1000:m]))})
out={'schema':'marici.voevodsky.L075-exact-jump-tail-scout.v1','rows':rows,'norm_1000_to_200000':rows[-1]['norm_1000_to_upper'],'status':'floating exact-step coefficient recurrence; directed infinite remainder open','passed':rows[-1]['norm_1000_to_upper']<4.267829461527579e-9,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'L075_exact_jump_tail_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
