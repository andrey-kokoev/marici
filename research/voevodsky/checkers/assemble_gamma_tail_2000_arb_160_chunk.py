#!/usr/bin/env python3
"""Resumable row chunk of the directed rank-160 gamma-tail matrix."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb
flint.ctx.prec=1024;start=int(sys.argv[1]);stop=int(sys.argv[2]);root=Path(__file__).parents[1]/'results';mom=json.loads((root/'gamma_tail_moments_2000_arb_320.json').read_text())['moments'];bc=json.loads((root/'spherical_bessel_inverse_power_expansions_159.json').read_text());S=bc['S'];C=bc['C'];L=arb('.55');binet=arb('1e-56') # doubled rank amplitude maximum
def M(q,k):return arb(mom[str(k)][q])
def conv(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[i+j]+=x*y
 return out
def entry(m,n):
 ss=conv(S[m],S[n]);cc=conv(C[m],C[n]);sc=conv(S[m],C[n]);cs=conv(C[m],S[n]);v=arb(0)
 for k in range(max(map(len,(ss,cc,sc,cs)))):
  x=ss[k] if k<len(ss) else 0;y=cc[k] if k<len(cc) else 0;z=(sc[k] if k<len(sc) else 0)+(cs[k] if k<len(cs) else 0)
  if x or y:v+=L**(-k)*((x+y)*M('plain',k)/2+(y-x)*M('cos',k)/2)
  if z:v+=L**(-k)*z*M('sin',k)/2
 return 4*L*((2*m+1)*(2*n+1)/(4*L**2)).sqrt()*((-1)**(m//2+n//2))*v/(2*arb.pi())+arb(0,binet)
rows={};maxrad=0.
for i in range(start,stop):
 row=[]
 for j in range(160):
  q=entry(i,j);row.append(str(q));maxrad=max(maxrad,float(q.rad()))
 rows[str(i)]=row
out={'schema':'marici.voevodsky.gamma-tail-2000-arb-160-chunk.v1','start':start,'stop_exclusive':stop,'rows':rows,'maximum_entry_radius':maxrad,'budget':'5e-11','passed':maxrad<5e-11}
p=root/f'gamma_tail_2000_arb_160_rows_{start}_{stop-1}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'start':start,'stop':stop,'maximum_entry_radius':maxrad,'passed':out['passed']},indent=2))
