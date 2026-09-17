#!/usr/bin/env python3
"""Directed assembly of the rank-80 gamma tail at R=250."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,arb_mat
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';mom=json.loads((root/'gamma_tail_moments_250_arb.json').read_text())['moments'];bc=json.loads((root/'spherical_bessel_inverse_power_expansions.json').read_text());S=bc['S'];C=bc['C'];L=arb('.55')
def M(kind,k):return arb(mom[str(k)][kind])
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
  if not (x or y or z):continue
  scale=L**(-k)
  if x or y:v+=scale*((x+y)*M('plain',k)/2+(y-x)*M('cos',k)/2)
  if z:v+=scale*z*M('sin',k)/2
 amp=4*L*((2*m+1)*(2*n+1)/(4*L**2)).sqrt()*((-1)**(m//2+n//2))/(2*arb.pi())
 return amp*v
A=arb_mat(80,80)
# Common Binet multiplier remainder bound, applied after cancellation.
binet=arb('3.285e-39')
for i in range(80):
 for j in range(i,80):
  q=entry(i,j)+arb(0,binet);A[i,j]=q;A[j,i]=q
maxrad=max(float(A[i,j].rad()) for i in range(80) for j in range(80));matrix=[[str(A[i,j]) for j in range(80)] for i in range(80)]
out={'schema':'marici.voevodsky.gamma-tail-250-arb-matrix.v1','precision_bits':flint.ctx.prec,'R':250,'dimension':80,'common_binet_entry_radius':'3.285e-39','maximum_entry_radius':maxrad,'allocated_budget':'5e-11','budget_met':maxrad<5e-11,'matrix':matrix,'passed':maxrad<5e-11,'rh_proved':False}
p=root/'gamma_tail_250_arb_matrix.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('precision_bits','R','dimension','common_binet_entry_radius','maximum_entry_radius','allocated_budget','budget_met','passed')},indent=2));assert out['passed']
