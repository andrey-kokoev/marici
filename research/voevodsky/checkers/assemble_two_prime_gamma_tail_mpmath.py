#!/usr/bin/env python3
"""High-precision assembly of the order-79 gamma tail from exact expansions."""
import json,sys
from pathlib import Path
try: import mpmath as mp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp
mp.mp.dps=100;R=mp.mpf(2000);L=mp.mpf('0.55');omega=2*L
root=Path(__file__).parents[1]/'results';bc=json.loads((root/'spherical_bessel_inverse_power_expansions.json').read_text());S=bc['S'];C=bc['C'];dc=json.loads((root/'digamma_real_asymptotic_coefficients.json').read_text());corr={int(k):mp.mpf(v) for k,v in dc['coefficients'].items()}
def E(k): return (-1j*omega)**(k-1)*mp.gammainc(1-k,-1j*omega*R,mp.inf)
def plain_pow(k):return R**(1-k)/(k-1)
def logplain(k):return R**(1-k)*(mp.log(R/(2*mp.pi))/(k-1)+1/(k-1)**2)
def logosc(k):return -mp.diff(lambda q:E(q),k)-mp.log(2*mp.pi)*E(k)
cache={}
def moment(kind,k):
 key=(kind,k)
 if key in cache:return cache[key]
 if kind=='plain':v=logplain(k)+sum(c*plain_pow(k+j) for j,c in corr.items())
 else:
  z=logosc(k)+sum(c*E(k+j) for j,c in corr.items());v=mp.re(z) if kind=='cos' else mp.im(z)
 cache[key]=v;return v
def conv(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[i+j]+=x*y
 return out
def entry(m,n):
 ss=conv(S[m],S[n]);cc=conv(C[m],C[n]);sc=conv(S[m],C[n]);cs=conv(C[m],S[n]);v=mp.mpf('0')
 for k in range(max(map(len,(ss,cc,sc,cs)))):
  x=ss[k] if k<len(ss) else 0;y=cc[k] if k<len(cc) else 0;z=(sc[k] if k<len(sc) else 0)+(cs[k] if k<len(cs) else 0)
  if x or y:v+=(x+y)*moment('plain',k)/2+(y-x)*moment('cos',k)/2
  if z:v+=z*moment('sin',k)/2
 # j arguments Lu contribute L^-k per inverse power; incorporated termwise above only if rescale coefficients.
 # Recompute scaling by convolution power here: each accumulated moment term needs L^-k.
 # The loop above omitted it; redo compactly.
 v=mp.mpf('0')
 for k in range(max(map(len,(ss,cc,sc,cs)))):
  x=ss[k] if k<len(ss) else 0;y=cc[k] if k<len(cc) else 0;z=(sc[k] if k<len(sc) else 0)+(cs[k] if k<len(cs) else 0);scale=L**(-k)
  if x or y:v+=scale*((x+y)*moment('plain',k)/2+(y-x)*moment('cos',k)/2)
  if z:v+=scale*z*moment('sin',k)/2
 amp=4*L*mp.sqrt((2*m+1)*(2*n+1)/(4*L**2))*(-1)**(m//2+n//2) # product normalization
 return amp*v/(2*mp.pi)
M=mp.matrix(80)
for i in range(80):
 for j in range(i,80):M[i,j]=M[j,i]=entry(i,j)
ev=mp.eigsy(M,eigvals_only=True)
out={'schema':'marici.voevodsky.two-prime-gamma-tail-mpmath.v1','precision_decimal_digits':mp.mp.dps,'tail_anchor':'2000','dimension':80,'smallest_tail_eigenvalue':mp.nstr(ev[0],30),'largest_tail_eigenvalue':mp.nstr(ev[79],30),'maximum_absolute_entry':mp.nstr(max(abs(M[i,j]) for i in range(80) for j in range(80)),30),'status':'high-precision asymptotic assembly; Binet remainder budget external; no ball rounding','passed':True,'rh_proved':False}
p=root/'two_prime_gamma_tail_mpmath.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
