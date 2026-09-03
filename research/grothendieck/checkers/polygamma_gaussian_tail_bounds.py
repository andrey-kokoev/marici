"""Arb bounds for omitted xi-Taylor polygamma Gaussian tails through order 7."""
import json,math
from pathlib import Path
from flint import arb,ctx
ctx.dps=70
Y=arb(8);pi=arb.pi();J0=pi.sqrt()/2*Y.erfc();bounds={}
# For k>=1, |psi^(k)(z)| <= k![4^(k+1)+4^k/k] when Re z=1/4.
# The xi Taylor coefficient divides by 2^k k!, and gamma/c contributes 1/(2 sqrt(pi)).
for k in range(1,8):
 c=(arb(4)**(k+1)+arb(4)**k/k)/arb(2)**k
 tail=(2*J0)*c/(2*pi.sqrt())
 bounds[str(k)]={'coefficient_majorant':str(c),'gamma_over_c_taylor_tail_upper':str(tail)}
# k=0 uses the sharper affine-in-|y| bound from the companion checker.
k0=arb('1.3e-28');thresholds={str(k):arb('1e-26') for k in range(8)};passed=k0.upper()<thresholds['0'] and all(arb(v['gamma_over_c_taylor_tail_upper']).upper()<thresholds[k] for k,v in bounds.items())
out={'schema':'marici.polygamma-gaussian-tail-bounds.v1','status':'passed' if passed else 'failed','domain':{'abs_y_lower':8,'polygamma_orders':[0,7]},'order_0_gamma_over_c_tail_upper':str(k0),'orders_1_7':bounds,'uniform_declared_coefficient_error':'1e-26','derivation':'absolutely convergent polygamma series at Re z=1/4 and exact Arb erfc Gaussian tail'}
(Path(__file__).parents[1]/'results'/'polygamma-gaussian-tail-bounds.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
