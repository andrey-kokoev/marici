"""Arb t-series scout for the weakest dual witness at fixed xi.

Coefficients are enclosed; the unmaterialized order-7 remainder and mixed
rectangle composition prevent certificate status.
"""
import json,math
from pathlib import Path
from flint import arb,acb,arb_series,acb_series,ctx
ctx.dps=50
T=arb('.299');H=arb('.001');X=arb('4.5025');P=512;DEG=10;Y=arb(8);A=arb('6817744927666.86');B=arb('-997228471888.1238');U0=arb('1.3e-13');U2=arb('5e-12')
def primes(n):
 s=[True]*(n+1);s[0]=s[1]=False
 for p in range(2,math.isqrt(n)+1):
  if s[p]:
   for q in range(p*p,n+1,p):s[q]=False
 return [p for p in range(2,n+1) if s[p]]
terms=[]
for p in primes(P):
 n=p;lp=arb(p).log()
 while n<=P:terms.append((n,lp,arb(n).log()));n*=p
ts=arb_series([T,1],DEG+1);rt=ts.sqrt();pi=arb.pi();scale=2*pi.sqrt()*rt
r=scale*(ts/4-ts*X*X).exp()*(ts*X).cos()-arb_series([pi.log()/2],DEG+1)
rx=scale*(ts/4-ts*X*X).exp()*(-2*ts*X*(ts*X).cos()-ts*(ts*X).sin())
for n,lp,ln in terms:
 w=lp/arb(n).sqrt()*(-(ln*ln)/(4*ts)).exp();r-=w*(X*ln).cos();rx+=w*ln*(X*ln).sin()
# Build digamma and x-derivative series at each integration argument.
def coeff_integrand(y,k,xder=False):
 rt0=T.sqrt();z0=arb('.25')+(X+y/rt0)*.5j
 zseries=acb_series([arb('.25')],DEG+1)+(X+y/rt)*.5j;dz=zseries-z0
 out=acb_series([0],DEG+1);power=acb_series([1],DEG+1)
 for m in range(DEG+1):
  order=m+1 if xder else m;factor=.5j if xder else 1
  out+=power*(z0.polygamma(order)*factor/math.factorial(m));power*=dz
 return (-y*y).exp()*out[k]
for k in range(DEG+1):
 q=acb.integral(lambda y,a,k=k:coeff_integrand(y,k,False),-Y,Y,abs_tol=arb('1e-40')).real/(2*pi.sqrt())
 qx=acb.integral(lambda y,a,k=k:coeff_integrand(y,k,True),-Y,Y,abs_tol=arb('1e-40')).real/(2*pi.sqrt())
 r[k]+=q;rx[k]+=qx
support=(A*A*U0*U0+B*B*U0*U2).sqrt();d=A*r-B*rx;d[0]-=support;delta=arb(0,H);poly=d[DEG]
for k in range(DEG-1,-1,-1):poly=d[k]+delta*poly
high_order_budget=sum((abs(d[k])*H**k for k in range(7,DEG+1)),arb(0))
out={'schema':'marici.arb-dual-t-series-scout.v1','status':'coefficients_enclosed','t_center':'.299','t_radius':'.001','xi':'4.5025','degree':DEG,'polynomial_range_lower':str(poly.lower()),'polynomial_range_upper':str(poly.upper()),'degree_7_10_absolute_contribution_bound':str(high_order_budget),'conditions':['bound order-11 t remainder','bound omitted mixed t-polygamma Gaussian tails','compose with xi Taylor model for rectangle'],'method':'Arb series with acb.integral of composed polygamma series'};(Path(__file__).parents[1]/'results'/'arb-dual-t-series-scout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
