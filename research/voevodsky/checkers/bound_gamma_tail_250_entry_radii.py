#!/usr/bin/env python3
"""Propagate scalar and Binet remainder radii through the exact tail assembly."""
import json,sys
from pathlib import Path
try: import mpmath as mp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp
mp.mp.dps=100;root=Path(__file__).parents[1]/'results';bc=json.loads((root/'spherical_bessel_inverse_power_expansions.json').read_text());S=bc['S'];C=bc['C'];L=mp.mpf('.55');R=mp.mpf(250);Nbin=10
# |Binet remainder(u)| <= Cbin*u^(-2N-1).
zeta_upper=1+mp.mpf(2)**(-20);Cbin=8*2**(2*Nbin)*mp.factorial(2*Nbin+1)*zeta_upper/(2*mp.pi)**(2*Nbin+2)
# Stored decimals carry 70 significant digits. Bound rounding relative to an
# absolute integral majorant at each inverse power.
dig=json.loads((root/'digamma_real_asymptotic_coefficients.json').read_text())
def asym_moment_majorant(k):
 lead=R**(1-k)*(mp.log(R/(2*mp.pi))/(k-1)+1/(k-1)**2)
 return lead+sum(abs(mp.mpf(c))*R**(1-k-int(j))/(k+int(j)-1) for j,c in dig['coefficients'].items())
def rad(k):return mp.mpf('1e-68')*asym_moment_majorant(k)
def conv(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[i+j]+=x*y
 return out
def er(m,n):
 ss=conv(S[m],S[n]);cc=conv(C[m],C[n]);sc=conv(S[m],C[n]);cs=conv(C[m],S[n]);v=mp.mpf(0)
 for k in range(max(map(len,(ss,cc,sc,cs)))):
  x=ss[k] if k<len(ss) else 0;y=cc[k] if k<len(cc) else 0;z=(sc[k] if k<len(sc) else 0)+(cs[k] if k<len(cs) else 0)
  # plain/cos coefficients after trig reduction; sum absolute propagation.
  weight=abs(x+y)+abs(y-x)+abs(z)
  if weight:
   assert k>=2
   v+=L**(-k)*weight*rad(k)/2
 amp=4*L*mp.sqrt((2*m+1)*(2*n+1)/(4*L**2))/(2*mp.pi)
 return amp*v
mx=mp.mpf(0);arg=None
for i in range(80):
 for j in range(80):
  q=er(i,j)
  if q>mx:mx=q;arg=(i,j)
# The Binet remainder is one common multiplier and must be bounded before the
# inverse-power expansion. From |j_n(x)|<=1 on the real axis, normalized
# amplitude products are at most 2*sqrt((2m+1)(2n+1)); maximize at m=n=79.
binet_direct=2*159/(2*mp.pi)*Cbin*R**(-2*Nbin)/(2*Nbin)
out={'schema':'marici.voevodsky.gamma-tail-250-entry-radius.v1','R':250,'dimension':80,'scalar_decimal_radius':'1e-68','Binet_order':Nbin,'Binet_constant':mp.nstr(Cbin,30),'direct_common_multiplier_binet_entry_radius':mp.nstr(binet_direct,30),'independent_scalar_rounding_propagation_upper':mp.nstr(mx,30),'maximizing_entry':arg,'allocated_budget':'5e-11','binet_budget_met':binet_direct<mp.mpf('5e-11'),'scalar_rounding_budget_met':mx<mp.mpf('5e-11'),'diagnosis':'Significant-digit-scaled moment radii propagate safely; a directed evaluator for the scalar moments is still required because mpmath centers do not certify their own rounding.','conditional_budget_met':binet_direct+mx<mp.mpf('5e-11'),'passed':False,'rh_proved':False}
p=root/'gamma_tail_250_entry_radius.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
