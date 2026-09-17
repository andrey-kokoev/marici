#!/usr/bin/env python3
"""Floating scout of weighted variation for dangerous prime images."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import roots_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import roots_legendre
from numpy.polynomial.legendre import legval,legder
root=Path(__file__).parents[1]/'results';U=np.load(root/'gamma_floor_rank1000_dangerous_vectors.npz')['vectors'][:,:4];L=.55;scales=np.sqrt((2*np.arange(1000)+1)/(2*L));co=[U[:,j]*scales for j in range(4)];dco=[legder(c)/L for c in co];terms=[(math.log(p),math.log(p)/math.sqrt(p)) for p in (2,3)];breaks=sorted(set([-L,L]+[-L+a for a,c in terms]+[L-a for a,c in terms]));z,w=roots_legendre(2200);deriv=np.zeros(4)
for left,right in zip(breaks[:-1],breaks[1:]):
 x=(left+right)/2+(right-left)*z/2;ww=(right-left)*w/2;gp=np.zeros((len(x),4))
 for a,c in terms:
  plus=x+a;minus=x-a
  for j in range(4):
   gp[:,j]-=.5*c*(np.where(plus<=L,legval(plus/L,dco[j]),0)+np.where(minus>=-L,legval(minus/L,dco[j]),0))
 weight=(1-(x/L)**2)**(-.25);deriv+=np.sum(ww[:,None]*abs(gp)*weight[:,None],axis=0)
jumps=np.zeros(4)
for a,c in terms:
 for x,side in ((L-a,1),(-L+a,-1)):
  weight=(1-(x/L)**2)**(-.25)
  for j in range(4):jumps[j]+=.5*c*abs(legval((L if side==1 else -L)/L,co[j]))*weight
J=deriv+jumps;caps=[0.008634854229806576,0.1415864057776234,1.4161216649038253,10.30795292233664]
out={'schema':'marici.voevodsky.dangerous-prime-weighted-variation-scout.v1','gauss_order_per_smooth_segment':2200,'breakpoints':breaks,'derivative_variations':[float(x) for x in deriv],'jump_variations':[float(x) for x in jumps],'total_weighted_variations':[float(x) for x in J],'ratios_to_sufficient_caps':[float(J[i]/caps[i]) for i in range(4)],'status':'floating absolute-value quadrature scout','passed':True,'rh_proved':False};p=root/'dangerous_prime_weighted_variation_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
