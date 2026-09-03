"""Arb proof of the omitted |y|>8 digamma-Gaussian tail bounds."""
import json
from pathlib import Path
from flint import arb,ctx
ctx.dps=70
Y=arb(8);TMIN=arb('.298');XMAX=arb('4.505');pi=arb.pi()
# psi(z+1)=-gamma+sum_{n>=1} z/[n(n+z)] and psi(z)=psi(z+1)-1/z.
# Re z=1/4 gives |psi(z)| <= gamma+4+(pi^2/6)|z|.
A=arb.const_euler()+4+pi*pi/6*(arb('.25')+XMAX/2)
B=pi*pi/(12*TMIN.sqrt())
e=(-Y*Y).exp();J0=pi.sqrt()/2*Y.erfc();J1=e/2;J2=Y*e/2+pi.sqrt()/4*Y.erfc()
# Symmetric tails; |psi| <= A+B|y|.
I0=2*(A*J0+B*J1);I1=2*(A*J1+B*J2)
g0=I0/(4*pi*TMIN.sqrt());g1=I1/(2*pi)
threshold=arb('1e-27')
out={'schema':'marici.digamma-gaussian-tail-bound.v1','status':'passed' if g0.upper()<threshold and g1.upper()<threshold else 'failed','domain':{'abs_y_lower':8,'t_lower':'.298','xi_abs_upper':'4.505'},'psi_majorant_A':str(A),'psi_majorant_B':str(B),'gamma_value_tail_upper':str(g0),'gamma_slope_tail_upper':str(g1),'threshold':'1e-27','derivation':'digamma recurrence and absolutely bounded convergent series; closed Gaussian tail moments evaluated by Arb'}
(Path(__file__).parents[1]/'results'/'digamma-gaussian-tail-bound.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
