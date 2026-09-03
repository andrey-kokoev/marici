"""Enclose the order-11 t-Taylor coefficient over the full weakest cell."""
import json,math
from pathlib import Path
from flint import arb,acb,arb_series,acb_series,ctx
ctx.dps=50;ctx.cap=13
TB=arb('.299','.001');H=arb('.001');X=arb('4.5025');P=512;K=11;Y=arb(8);A=arb('6817744927666.86');B=arb('-997228471888.1238')
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
ts=arb_series([TB,1],K+2);rt=ts.sqrt();pi=arb.pi();scale=2*pi.sqrt()*rt
r=scale*(ts/4-ts*X*X).exp()*(ts*X).cos()-arb_series([pi.log()/2],K+2);rx=scale*(ts/4-ts*X*X).exp()*(-2*ts*X*(ts*X).cos()-ts*(ts*X).sin())
for n,lp,ln in terms:
 w=lp/arb(n).sqrt()*(-(ln*ln)/(4*ts)).exp();r-=w*(X*ln).cos();rx+=w*ln*(X*ln).sin()
def integrand(y,k,xder=False):
 rt0=TB.sqrt();z0=arb('.25')+acb(X+y/rt0)*.5j;zs=acb_series([arb('.25')],K+2)+(X+y/rt)*.5j;dz=zs-z0;o=acb_series([0],K+2);p=acb_series([1],K+2)
 for m in range(K+2):
  o+=p*z0.polygamma(m+(1 if xder else 0))*(.5j if xder else 1)/math.factorial(m);p*=dz
 return (-y*y).exp()*o[k]
r[K]+=acb.integral(lambda y,a:integrand(y,K,False),-Y,Y,abs_tol=arb('1e-35')).real/(2*pi.sqrt());rx[K]+=acb.integral(lambda y,a:integrand(y,K,True),-Y,Y,abs_tol=arb('1e-35')).real/(2*pi.sqrt())
dk=A*r[K]-B*rx[K];remainder=abs(dk)*H**K
# Direct interval rectangles enclose the mixed coefficient on 8 <= |y| <= 20.
step=arb('.05');tail_r=arb(0);tail_rx=arb(0)
for sign in (-1,1):
 for j in range(240):
  y=arb(str(sign*(8+(j+.5)*.05)),'.025')
  tail_r+=abs(integrand(y,K,False))*step/(2*pi.sqrt())
  tail_rx+=abs(integrand(y,K,True))*step/(2*pi.sqrt())
mixed_remainder=(abs(A)*tail_r+abs(B)*tail_rx)*H**K
out={'schema':'marici.arb-t-remainder-bound.v1','status':'finite_tail_enclosed','t_box':'0.299 +/- 0.001','order':K,'combined_core_coefficient':str(dk),'core_remainder_upper':str(remainder),'mixed_tail_8_20_r_coefficient_upper':str(tail_r),'mixed_tail_8_20_rx_coefficient_upper':str(tail_rx),'mixed_tail_8_20_remainder_upper':str(mixed_remainder),'condition':'bound |y|>20 mixed t-polygamma contribution','method':'order-11 Arb series coefficient over full t box plus direct interval rectangles on 8<=|y|<=20'};(Path(__file__).parents[1]/'results'/'arb-t-remainder-bound.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
