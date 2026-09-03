"""Enclose the xi derivative of the frozen dual witness along the t interval."""
import json,math
from pathlib import Path
from flint import arb,acb,arb_series,acb_series,ctx
ctx.dps=50;ctx.cap=12
T=arb('.299');H=arb('.001');X=arb('4.5025');P=512;DEG=10;Y=arb(8);A=arb('6817744927666.86');B=arb('-997228471888.1238')
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
ts=arb_series([T,1],DEG+1);rt=ts.sqrt();pi=arb.pi();scale=2*pi.sqrt()*rt;ph=ts*X;pref=(ts/4-ts*X*X).exp();rx=scale*pref*(-2*ts*X*ph.cos()-ts*ph.sin());rxx=scale*pref*((4*ts*ts*X*X-2*ts-ts*ts)*ph.cos()+4*ts*ts*X*ph.sin())
for n,lp,ln in terms:
 w=lp/arb(n).sqrt()*(-(ln*ln)/(4*ts)).exp();rx+=w*ln*(X*ln).sin();rxx+=w*ln*ln*(X*ln).cos()
def ci(y,k,xorder):
 z0=arb('.25')+(X+y/T.sqrt())*.5j;zs=acb_series([arb('.25')],DEG+1)+(X+y/rt)*.5j;dz=zs-z0;o=acb_series([0],DEG+1);p=acb_series([1],DEG+1)
 for m in range(DEG+1):o+=p*z0.polygamma(m+xorder)*(.5j)**xorder/math.factorial(m);p*=dz
 return (-y*y).exp()*o[k]
for k in range(DEG+1):
 rx[k]+=acb.integral(lambda y,a,k=k:ci(y,k,1),-Y,Y,abs_tol=arb('1e-40')).real/(2*pi.sqrt());rxx[k]+=acb.integral(lambda y,a,k=k:ci(y,k,2),-Y,Y,abs_tol=arb('1e-40')).real/(2*pi.sqrt())
d=A*rx-B*rxx;z=arb(0,H);poly=d[DEG]
for k in range(DEG-1,-1,-1):poly=d[k]+z*poly
out={'schema':'marici.arb-dual-x-derivative-t-series.v1','status':'coefficients_enclosed','t_interval':['.298','.300'],'xi':'4.5025','degree':DEG,'derivative_lower':str(poly.lower()),'derivative_upper':str(poly.upper()),'absolute_polynomial_bound':str(max(abs(poly.lower()),abs(poly.upper()))),'condition':'bound order-11 t remainder and omitted mixed tails for x derivative','rectangle_test':'need absolute derivative bound below t-line lower margin / .0025'};(Path(__file__).parents[1]/'results'/'arb-dual-x-derivative-t-series.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
