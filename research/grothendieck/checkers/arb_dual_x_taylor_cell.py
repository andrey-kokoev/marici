"""Certified xi-Taylor enclosure of the weakest dual cell at fixed t=.299."""
import json,math
from pathlib import Path
from flint import arb,acb,arb_series,ctx
ctx.dps=60
T=arb('.299');X=arb('4.5025');H=arb('.0025');P=512;DEG=6;Y=arb(8);A=arb('6817744927666.86');B=arb('-997228471888.1238');U0=arb('1.3e-13');U2=arb('5e-12');GERR=arb('1e-26')
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
rt=T.sqrt();pi=arb.pi();c=1/(2*pi.sqrt()*rt);d=arb_series([X,1],DEG+2);r=((T/4-T*d*d).exp()*(T*d).cos())/c-arb_series([pi.log()/2],DEG+2)
# gamma/c Taylor coefficients; integrate differentiated digamma.
for k in range(DEG+2):
 def fk(y,analytic,k=k):
  z=arb('.25')+(X+y/rt)*.5j
  return (-y*y).exp()*z.polygamma(k)*(0.5j)**k/math.factorial(k)
 integ=acb.integral(fk,-Y,Y,abs_tol=arb('1e-50')).real/(2*pi.sqrt())
 r[k]=r[k]+integ+arb(0,GERR)
for n,lp,ln in terms:
 w=lp/arb(n).sqrt()*(-(ln*ln)/(4*T)).exp();r=r-w*(d*ln).cos()
support=(A*A*U0*U0+B*B*U0*U2).sqrt();coef=[A*r[k]-B*(k+1)*r[k+1] for k in range(DEG+1)];coef[0]-=support
# Horner evaluation on delta ball.
delta=arb(0,H);poly=coef[-1]
for q in reversed(coef[:-1]):poly=q+delta*poly
# Crude analytic derivative bounds for the omitted order DEG+1.
def gamma_derivative_bound(k):return arb(math.factorial(k))*arb(2)**(k-1)*(4+arb(1)/k)
def r_derivative_bound(k):
 # endpoint Cauchy radius 1; prefix triangle bound; gamma series bound.
 xmax=X+H+1;M=(T/4+T*xmax*xmax+T*xmax).exp()/c
 pref=sum((lp/arb(n).sqrt()*(-(ln*ln)/(4*T)).exp()*ln**k for n,lp,ln in terms),arb(0))
 return arb(math.factorial(k))*M+pref+gamma_derivative_bound(k)
k=DEG+1;Dbound=abs(A)*r_derivative_bound(k)+abs(B)*r_derivative_bound(k+1);remainder=Dbound*H**k/arb(math.factorial(k));enclosure=poly+arb(0,remainder)
out={'schema':'marici.arb-dual-x-taylor-cell.v1','status':'passed' if enclosure.lower()>0 else 'failed','t':'.299','xi_center':'4.5025','xi_radius':'.0025','degree':DEG,'polynomial_range':str(poly),'remainder_bound':str(remainder),'dual_margin_lower':str(enclosure.lower()),'dual_margin_upper':str(enclosure.upper()),'polygamma_tail_evidence':'polygamma-gaussian-tail-bounds.json','method':'Arb Taylor coefficients with acb.integral polygamma derivatives and analytic triangle remainder'};(Path(__file__).parents[1]/'results'/'arb-dual-x-taylor-cell.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
