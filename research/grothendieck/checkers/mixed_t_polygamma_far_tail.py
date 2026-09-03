"""Coarse Arb envelope for the |y|>20 order-11 mixed t tail."""
import json,math
from pathlib import Path
from flint import arb,ctx
ctx.dps=70
Y=arb(20);H=arb('.001')
# Finite-combinatorial envelope: t in [.298,.300], orders <=12.
# Bounds binomial coefficients of t^-1/2, all Faa-di-Bruno partitions,
# polygamma by k![4^(k+1)+4^k/k], witness coefficients, and normalizations.
C=arb('1e100')
# For y>=20, (1+y)^11 <= 2^11 y^11. Repeated integration by parts:
# I_n(Y)=.5 Y^(n-1)e^-Y^2 + .5(n-1)I_(n-2)(Y).
def I(n):
 if n==0:return arb.pi().sqrt()/2*Y.erfc()
 if n==1:return (-Y*Y).exp()/2
 return Y**(n-1)*(-Y*Y).exp()/2+arb(n-1)*I(n-2)/2
bound=2*C*arb(2)**11*I(11)*H**11
out={'schema':'marici.mixed-t-polygamma-far-tail.v1','status':'passed' if bound.upper()<arb('1e-20') else 'failed','domain':{'abs_y_lower':20,'t_interval':['.298','.300'],'order':11},'combined_coefficient_envelope':'1e100*(1+|y|)^11','normalized_remainder_upper':str(bound),'coefficient_envelope_evidence':'mixed-t-coefficient-envelope.json','envelope_basis':'t^-1/2 coefficients, composition counts, polygamma series, frozen witness, and normalizations; proved bound 2.36e83 enlarged to 1e100','gaussian_tail_method':'closed recurrence for integral y^11 exp(-y^2)'}
(Path(__file__).parents[1]/'results'/'mixed-t-polygamma-far-tail.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
