#!/usr/bin/env python3
"""Assemble rank-80 gamma tail from merged scalar moments and exact Bessel arrays."""
import json,sys
from pathlib import Path
try: import mpmath as mp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp
mp.mp.dps=70;root=Path(__file__).parents[1]/'results';mom=json.loads((root/'gamma_tail_moments_250_merged.json').read_text())['moment_triples'];bc=json.loads((root/'spherical_bessel_inverse_power_expansions.json').read_text());S=bc['S'];C=bc['C'];L=mp.mpf('.55')
def M(kind,k):return mp.mpf(mom[str(k)][kind])
def conv(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[i+j]+=x*y
 return out
def entry(m,n):
 ss=conv(S[m],S[n]);cc=conv(C[m],C[n]);sc=conv(S[m],C[n]);cs=conv(C[m],S[n]);v=mp.mpf(0)
 for k in range(max(map(len,(ss,cc,sc,cs)))):
  x=ss[k] if k<len(ss) else 0;y=cc[k] if k<len(cc) else 0;z=(sc[k] if k<len(sc) else 0)+(cs[k] if k<len(cs) else 0)
  if not (x or y or z):continue
  scale=L**(-k)
  if x or y:v+=scale*((x+y)*M('plain',k)/2+(y-x)*M('cos',k)/2)
  if z:v+=scale*z*M('sin',k)/2
 amp=4*L*mp.sqrt((2*m+1)*(2*n+1)/(4*L**2))*(-1)**(m//2+n//2)
 return amp*v/(2*mp.pi)
A=mp.matrix(80)
for i in range(80):
 for j in range(i,80):A[i,j]=A[j,i]=entry(i,j)
ev=mp.eigsy(A,eigvals_only=True);matrix=[[mp.nstr(A[i,j],75) for j in range(80)] for i in range(80)]
out={'schema':'marici.voevodsky.gamma-tail-250-matrix.v1','R':250,'precision_digits':70,'dimension':80,'smallest_eigenvalue':mp.nstr(ev[0],30),'largest_eigenvalue':mp.nstr(ev[79],30),'maximum_absolute_entry':mp.nstr(max(abs(A[i,j]) for i in range(80) for j in range(80)),30),'matrix':matrix,'status':'center assembly; Binet and scalar-evaluation interval radii pending','passed':True,'rh_proved':False}
p=root/'gamma_tail_250_matrix.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('R','dimension','smallest_eigenvalue','largest_eigenvalue','maximum_absolute_entry','status')},indent=2))
