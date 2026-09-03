"""Arb proof of all-integer majorants for M0 and M2 beyond 512."""
import json
from pathlib import Path
from flint import arb,acb,ctx
ctx.dps=70
P=512;T=arb('.299');L=arb(P).log();Y=arb(20)
def bound(j):
 def f(y,analytic): return y**(j+1)*(y/2-y*y/(4*T)).exp()
 integral=acb.integral(f,L,Y,abs_tol=arb('1e-60')).real
 first=L**(j+1)/arb(P).sqrt()*(-(L*L)/(4*T)).exp()
 decay=Y/(2*T)-arb('.5')-arb(j+1)/Y
 far=f(Y,True)/decay
 return first+integral+far,first,integral,far
u0,f0,i0,r0=bound(0);u2,f2,i2,r2=bound(2);b0=arb('1.3e-13');b2=arb('5e-12')
out={'schema':'marici.integer-tail-moment-arb-bound.v1','status':'passed' if u0.upper()<b0 and u2.upper()<b2 else 'failed','domain':{'n_strictly_greater_than':P,'t_upper':'.299'},'M0_upper':str(u0),'M2_upper':str(u2),'declared_bounds':[str(b0),str(b2)],'far_integral_bounds':[str(r0),str(r2)],'derivation':'Lambda(n)<=log n; decreasing-sum integral test; certified acb.integral to y=20; exponential log-derivative tail bound thereafter'}
(Path(__file__).parents[1]/'results'/'integer-tail-moment-arb-bound.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
