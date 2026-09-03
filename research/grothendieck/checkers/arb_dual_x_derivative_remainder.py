"""Core order-11 t remainder for the xi derivative of the dual witness."""
import json,math
from pathlib import Path
from flint import arb,acb,arb_series,acb_series,ctx
ctx.dps=45;ctx.cap=13
T=arb('.299','.001');H=arb('.001');X=arb('4.5025');P=512;K=11;Y=arb(8);A=arb('6817744927666.86');B=arb('-997228471888.1238')
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
ts=arb_series([T,1],K+2);rt=ts.sqrt();pi=arb.pi();scale=2*pi.sqrt()*rt;ph=ts*X;pref=(ts/4-ts*X*X).exp();rx=scale*pref*(-2*ts*X*ph.cos()-ts*ph.sin());rxx=scale*pref*((4*ts*ts*X*X-2*ts-ts*ts)*ph.cos()+4*ts*ts*X*ph.sin())
for n,lp,ln in terms:
 w=lp/arb(n).sqrt()*(-(ln*ln)/(4*ts)).exp();rx+=w*ln*(X*ln).sin();rxx+=w*ln*ln*(X*ln).cos()
def ci(y,xorder):
 z0=arb('.25')+acb(X+y/T.sqrt())*.5j;zs=acb_series([arb('.25')],K+2)+(X+y/rt)*.5j;dz=zs-z0;o=acb_series([0],K+2);p=acb_series([1],K+2)
 for m in range(K+2):o+=p*z0.polygamma(m+xorder)*(.5j)**xorder/math.factorial(m);p*=dz
 return (-y*y).exp()*o[K]
rx[K]+=acb.integral(lambda y,a:ci(y,1),-Y,Y,abs_tol=arb('1e-32')).real/(2*pi.sqrt());rxx[K]+=acb.integral(lambda y,a:ci(y,2),-Y,Y,abs_tol=arb('1e-32')).real/(2*pi.sqrt());coef=A*rx[K]-B*rxx[K];rem=abs(coef)*H**K
step=arb('.05');tr=arb(0);tx=arb(0)
for sign in (-1,1):
 for j in range(240):
  y=arb(str(sign*(8+(j+.5)*.05)),'.025');tr+=abs(ci(y,1))*step/(2*pi.sqrt());tx+=abs(ci(y,2))*step/(2*pi.sqrt())
tail_8_20=(abs(A)*tr+abs(B)*tx)*H**K
out={'schema':'marici.arb-dual-x-derivative-remainder.v1','status':'finite_tail_enclosed','order':K,'core_coefficient':str(coef),'core_remainder_upper':str(rem),'mixed_tail_8_20_remainder_upper':str(tail_8_20),'far_tail_envelope_evidence':'mixed-t-coefficient-envelope.json and mixed-t-polygamma-far-tail.json'};(Path(__file__).parents[1]/'results'/'arb-dual-x-derivative-remainder.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
