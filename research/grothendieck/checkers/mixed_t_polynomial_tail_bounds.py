"""Arb majorants for omitted |y|>8 t-series coefficients 1 through 10."""
import json,math
from pathlib import Path
from flint import arb,ctx
ctx.dps=70
Y=arb(8);H=arb('.001');tmin=arb('.298');A=abs(arb('6817744927666.86'));B=abs(arb('-997228471888.1238'));pi=arb.pi();MAX=10
def I(n):
 if n==0:return pi.sqrt()/2*Y.erfc()
 if n==1:return (-Y*Y).exp()/2
 return Y**(n-1)*(-Y*Y).exp()/2+arb(n-1)*I(n-2)/2
rows=[];total=arb(0)
for order in range(1,MAX+1):
 s0=arb(0);s1=arb(0)
 for k in range(1,order+1):
  comp=arb(math.comb(order-1,k-1));product_bound=arb('.5')**k*tmin**(-arb(order)-arb(k)/2);q0=arb(4)**(k+1)+arb(4)**k/k;q1=arb('.5')*arb(k+1)*(arb(4)**(k+2)+arb(4)**(k+1)/(k+1));s0+=comp*product_bound*q0;s1+=comp*product_bound*q1
 # (1+y)^order <= 2^order y^order for y>=8; both tails.
 coeff=(A*s0+B*s1)/(2*pi.sqrt());term=2*coeff*arb(2)**order*I(order)*H**order;total+=term;rows.append({'order':order,'combined_coefficient_envelope':str(coeff),'normalized_polynomial_tail_contribution':str(term)})
out={'schema':'marici.mixed-t-polynomial-tail-bounds.v1','status':'passed' if total.upper()<arb('1e-6') else 'failed','domain':{'abs_y_lower':8,'t_interval':['.298','.300'],'orders':[1,10]},'total_normalized_margin_error':str(total),'rows':rows,'derivation':'uniform t^-1/2 coefficient bound, composition counts, polygamma series, and closed Gaussian moments'};(Path(__file__).parents[1]/'results'/'mixed-t-polynomial-tail-bounds.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'total':out['total_normalized_margin_error']},indent=2))
