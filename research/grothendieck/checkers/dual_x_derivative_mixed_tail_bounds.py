"""Bounds omitted mixed tails in the xi-derivative t polynomial."""
import json,math
from pathlib import Path
from flint import arb,ctx
ctx.dps=70
Y=arb(8);H=arb('.001');t=arb('.298');A=abs(arb('6817744927666.86'));B=abs(arb('-997228471888.1238'));pi=arb.pi();MAX=10
def I(n):
 if n==0:return pi.sqrt()/2*Y.erfc()
 if n==1:return (-Y*Y).exp()/2
 return Y**(n-1)*(-Y*Y).exp()/2+arb(n-1)*I(n-2)/2
total=arb('1e-12') # order-zero allowance from polygamma-gaussian-tail-bounds.json
for order in range(1,MAX+1):
 s1=arb(0);s2=arb(0)
 for k in range(1,order+1):
  comp=arb(math.comb(order-1,k-1));prod=arb('.5')**k*t**(-arb(order)-arb(k)/2)
  q1=arb('.5')*arb(k+1)*(arb(4)**(k+2)+arb(4)**(k+1)/(k+1))
  q2=arb('.25')*arb(k+2)*arb(k+1)*(arb(4)**(k+3)+arb(4)**(k+2)/(k+2))
  s1+=comp*prod*q1;s2+=comp*prod*q2
 coef=(A*s1+B*s2)/(2*pi.sqrt());total+=2*coef*arb(2)**order*I(order)*H**order
bound=total
out={'schema':'marici.dual-x-derivative-mixed-tail-bounds.v1','status':'passed' if bound.upper()<arb('1e-6') else 'failed','orders_0_10_tail_upper':str(total),'total_derivative_error_bound':str(bound),'order_0_evidence':'polygamma-gaussian-tail-bounds.json','order_11_evidence':'arb-dual-x-derivative-remainder.json and mixed-t-coefficient-envelope.json'};(Path(__file__).parents[1]/'results'/'dual-x-derivative-mixed-tail-bounds.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
