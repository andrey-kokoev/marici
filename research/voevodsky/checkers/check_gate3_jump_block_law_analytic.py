#!/usr/bin/env python3
"""Analytic Bernstein bound for continuum value-jump blocks."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
from numpy.polynomial.legendre import legval
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];L=.6495;k=np.arange(1000);sc=np.sqrt((2*k+1)/(2*L));fp=np.array([legval(1,Z[:,j]*sc) for j in range(40)]);fm=np.array([legval(-1,Z[:,j]*sc) for j in range(40)]);atoms=[]
for p in (2,3):
 a=math.log(p);c=math.log(p)/math.sqrt(p);atoms.extend([((L-a)/L,.5*c*np.linalg.norm(fp)),((-L+a)/L,.5*c*np.linalg.norm(fm))])
# Bernstein bound with 1.01 slack for n>=1000. Combining fac and two Legendre terms gives C(t)/n.
C=sum(1.01*row*math.sqrt(L/math.pi)*(1-t*t)**(-.25) for t,row in atoms);# sum_{n=1000m}^{1000(m+1)-1} n^-2 <= 1/(1000*m*(m+1-1/1000))
def block(m):return C/math.sqrt(1000*m*(m+1-1/1000))
rows=[{'m':m,'bound':block(m),'scaled_m_bound':m*block(m)} for m in range(1,21)];uniform=max(x['scaled_m_bound'] for x in rows);out={'schema':'marici.voevodsky.gate3-jump-block-law-analytic.v1','atom_count':len(atoms),'coefficient_constant_C':C,'rows':rows,'uniform_C_over_m':uniform,'target_C_over_m':.205,'passed':bool(uniform<.205),'scope':'Bernstein Legendre bound for exact value-jump coefficient matrix, n>=1000','rh_proved':False};p=root/'gate3_jump_block_law_analytic.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
