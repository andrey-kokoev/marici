"""Arb center certificate for the weakest frozen dual witness.

Conditional only on explicit analytic bounds for the truncated Gaussian tails
and the all-integer prime-tail moments.
"""
import json,math
from pathlib import Path
from flint import arb,acb,ctx
ctx.dps=70
T=arb('.299');X=arb('4.5025');P=512;A=arb('6817744927666.86');B=arb('-997228471888.1238');Y=arb(8);GERR=arb('1e-27');U0=arb('1.3e-13');U2=arb('5e-12')
def primes(n):
 s=[True]*(n+1);s[0]=s[1]=False
 for p in range(2,math.isqrt(n)+1):
  if s[p]:
   for k in range(p*p,n+1,p):s[k]=False
 return [p for p in range(2,n+1) if s[p]]
terms=[]
for p in primes(P):
 n=p;lp=arb(p).log()
 while n<=P:terms.append((n,lp,arb(n).log()));n*=p
rt=T.sqrt();pi=arb.pi();c=1/(2*pi.sqrt()*rt);pref=(T/4-T*X*X).exp();e=pref*(T*X).cos();e1=pref*(-2*T*X*(T*X).cos()-T*(T*X).sin())
def fun0(y,analytic):
 u=X+y/rt;return (-y*y).exp()*(arb('.25')+(u/2)*1j).digamma()
def fun1(y,analytic):return y*fun0(y,analytic)
q0=acb.integral(fun0,-Y,Y,abs_tol=arb('1e-60')).real;q1=acb.integral(fun1,-Y,Y,abs_tol=arb('1e-60')).real
g0=-pi.log()/(4*pi.sqrt()*rt)+q0/(4*pi*rt)+arb(0,GERR);g1=q1/(2*pi)+arb(0,GERR)
rp=arb(0);ip=arb(0)
for n,lp,ln in terms:
 w=lp/arb(n).sqrt()*(-(ln*ln)/(4*T)).exp();rp+=w*(X*ln).cos();ip+=w*ln*(X*ln).sin()
rr=(e+g0)/c-rp;ii=-(e1+g1)/c-ip;support=(A*A*U0*U0+B*B*U0*U2).sqrt();D=A*rr+B*ii-support
out={'schema':'marici.arb-dual-witness-center.v1','status':'conditional_certificate' if D.lower()>0 else 'failed','center':['.299','4.5025'],'prefix':P,'exact_terms':len(terms),'dual_margin':str(D),'required_tail_R':str(rr),'required_tail_I1':str(ii),'conditions':['prove truncated |y|>8 contribution to each gamma coordinate <=1e-27','prove tail M0<=1.3e-13 and M2<=5e-12 at t=.299'],'method':'certified acb.integral on [-8,8] and Arb arithmetic'};(Path(__file__).parents[1]/'results'/'arb-dual-witness-center.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
