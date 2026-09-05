"""Test first-contact curvature against a relaxed positive-tail jet cone."""
import json,math
from pathlib import Path
import mpmath as mp
mp.mp.dps=50;P=8192
SLICES=[(mp.mpf('.7'),mp.mpf(12),mp.mpf('.1')),(mp.mpf(1),mp.mpf(16),mp.mpf('.1')),(mp.mpf('1.5'),mp.mpf(40),mp.mpf('.2')),(mp.mpf(2),mp.mpf(140),mp.mpf('.5')),(mp.mpf(3),mp.mpf(150),mp.mpf(1))]

def pps(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,math.isqrt(n)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 a=[]
 for p in range(2,n+1):
  if s[p]:
   lp=mp.log(p);q=p
   while q<=n:a.append((lp/mp.sqrt(q),mp.log(q)));q*=p
 return a

def ub(t,j):
 L=mp.log(P);return L**(j+1)/mp.sqrt(P)*mp.exp(-L*L/(4*t))+mp.quad(lambda y:y**(j+1)*mp.exp(y/2-y*y/(4*t)),[L,mp.inf])
terms=pps(P);yn,yw=mp.gauss_quadrature(96,'hermite');rows=[]
for t,xmax,step in SLICES:
 c=1/(2*mp.sqrt(mp.pi*t));rt=mp.sqrt(t);pw=[(a*mp.exp(-l*l/(4*t)),l) for a,l in terms];U0=ub(t,0);U2=ub(t,2);vs=0;jet=0;worst=None;x=mp.mpf(0)
 while x<=xmax:
  z=[mp.mpf('.25')+mp.j*(x+yn[k]/rt)/2 for k in range(len(yn))]
  phi=[mp.re(mp.digamma(q)) for q in z];phi2=[mp.re(-mp.polygamma(2,q)/4) for q in z]
  q0=mp.fsum(yw[k]*phi[k] for k in range(len(yn)));q1=mp.fsum(yw[k]*yn[k]*phi[k] for k in range(len(yn)));q2=mp.fsum(yw[k]*phi2[k] for k in range(len(yn)))
  g0=-mp.log(mp.pi)/(4*mp.sqrt(mp.pi*t))+q0/(4*mp.pi*rt);g1=q1/(2*mp.pi);g2=q2/(4*mp.pi*rt)
  p=mp.exp(t/4-t*x*x);co=mp.cos(t*x);si=mp.sin(t*x);e=p*co;e1=p*(-2*t*x*co-t*si);e2=p*((4*t*t*x*x-2*t-t*t)*co+4*t*t*x*si)
  rp=mp.fsum(w*mp.cos(x*l) for w,l in pw);ip=mp.fsum(w*l*mp.sin(x*l) for w,l in pw);r2p=mp.fsum(w*l*l*mp.cos(x*l) for w,l in pw)
  r=(e+g0)/c-rp;i=-(e1+g1)/c-ip;q=-(e2+g2)/c-r2p
  ell=r*r/(U0*U0)+i*i/(U0*U2)-1
  if ell<=0:
   vs+=1
   upper=U2-i*i/(U0+r) if U0+r>0 else -mp.inf
   residual=q-upper
   if residual<=0:jet+=1
   if worst is None or residual<worst[0]:worst=(residual,x,q,upper)
  x+=step
 rows.append({'t':mp.nstr(t,10),'value_slope_feasible':vs,'first_contact_jet_feasible':jet,'curvature_excluded':vs-jet,'worst_curvature_residual':mp.nstr(worst[0],25) if worst else None,'worst_xi':mp.nstr(worst[1],15) if worst else None})
 print(json.dumps(rows[-1]))
out={'schema':'marici.high-precision-first-contact-jet-scout.v1','certified':False,'prefix':P,'digits':50,'rows':rows,'inequality':'I1^2 <= (U0+R)(U2-R2); first contact requires R2tail >= -(E2+G2)/c-R2prefix','limitations':['finite grid','Gauss-Hermite quadrature not interval enclosed','uses only curvature, not deformation-order sign']};(Path(__file__).parents[1]/'results'/'high-precision-first-contact-jet-scout.json').write_text(json.dumps(out,indent=2)+'\n')
