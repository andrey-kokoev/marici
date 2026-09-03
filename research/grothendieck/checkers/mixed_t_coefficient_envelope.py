"""Finite Arb derivation of the order-11 mixed-tail coefficient envelope."""
import json,math
from pathlib import Path
from flint import arb,ctx
ctx.dps=70
K=11;tmin=arb('.298');A=abs(arb('6817744927666.86'));B=abs(arb('-997228471888.1238'));pi=arb.pi()
# Every positive-order coefficient of (x+y/sqrt(t))/2 is at most C|y|:
# central-binomial/4^m <=1 and m<=K.
C=arb('.5')*tmin**(-arb(K)-arb('.5'))
s0=arb(0);s1=arb(0);s2=arb(0)
for k in range(1,K+1):
 compositions=arb(math.comb(K-1,k-1))
 # |psi^(k)|/k!
 q0=arb(4)**(k+1)+arb(4)**k/k
 # 0.5 |psi^(k+1)|/k! for the xi derivative
 q1=arb('.5')*arb(k+1)*(arb(4)**(k+2)+arb(4)**(k+1)/(k+1))
 q2=arb('.25')*arb(k+2)*arb(k+1)*(arb(4)**(k+3)+arb(4)**(k+2)/(k+2))
 s0+=compositions*C**k*q0
 s1+=compositions*C**k*q1
 s2+=compositions*C**k*q2
combined=(A*s0+B*s1)/(2*pi.sqrt())
derivative_combined=(A*s1+B*s2)/(2*pi.sqrt())
limit=arb('1e100')
out={'schema':'marici.mixed-t-coefficient-envelope.v1','status':'passed' if combined.upper()<limit and derivative_combined.upper()<limit else 'failed','order':K,'t_lower':'.298','coefficient_of_t_inverse_sqrt_upper_per_abs_y':str(C),'gamma_coefficient_envelope':str(s0/(2*pi.sqrt())),'gamma_x_coefficient_envelope':str(s1/(2*pi.sqrt())),'combined_frozen_witness_envelope':str(combined),'dual_x_derivative_envelope':str(derivative_combined),'declared_envelope':'1e100','derivation':'composition count binomial(10,k-1), central-binomial coefficient bound for t^-1/2, and absolutely convergent polygamma-series bounds'}
(Path(__file__).parents[1]/'results'/'mixed-t-coefficient-envelope.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
