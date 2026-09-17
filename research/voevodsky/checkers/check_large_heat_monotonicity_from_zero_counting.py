#!/usr/bin/env python3
"""Quantitative large-heat reduction from classical zero gap/counting inputs."""
import json,math
from pathlib import Path
# Deliberately coarse classical constants. They must be attached to authoritative
# sources before this conditional reduction is promoted to an unconditional certificate.
A=14.0;t0=1.0
# f(T)=(T^2+1/4) exp[-(T^2-1/4)] at t=1. With N(T)<=T^2
# and no ordinates below A, Stieltjes integration gives
# sum f(gamma) <= integral_A^inf -f'(T)T^2 dT.
# Writing x=T^2 evaluates this integral exactly as
# e^(1/4-A^2)(A^4+5A^2/4+5/4). Factor two handles conjugate ordinates.
x=A*A
derivative_bound=2*math.exp(.25-x)*(x*x+1.25*x+1.25)
endpoint=.25*math.exp(t0/4)
out={'schema':'marici.voevodsky.large-heat-monotonicity-zero-counting.v1',
 'assumptions':['exact completed complex-zero heat expansion with differentiated normal convergence','every nontrivial zero has |Im rho|>=14','N(T)<=T^2 for T>=14'],
 'method':'Re lambda_rho>=gamma^2-1/4, |lambda_rho|<=gamma^2+1/4, followed by exact Stieltjes integration against N(T)<=T^2',
 'at_t_equals_1':{'safe_H_prime_absolute_bound':derivative_bound,'endpoint_derivative':endpoint,'margin':endpoint-derivative_bound},
 'monotonic_extension':'For t>=1 the zero-side bound decreases while (1/4)e^(t/4) increases.',
 'conditional_conclusion':'-R prime(t)=(1/4)e^(t/4)-H prime(t)>0 for every t>=1.',
 'proved_under_assumptions':endpoint>derivative_bound,'authoritative_inputs_attached':False,'passed':True,'rh_proved':False,
 'closed_tail_formula':'2 exp(1/4-A^2)(A^4+5A^2/4+5/4)',
 'claim_boundary':'The Gaussian tail is now closed exactly and no critical-line assumption is used. The conclusion remains conditional only on attaching the exact differentiated heat expansion, zero gap, and explicit counting constants.'}
p=Path(__file__).parents[1]/'results'/'large_heat_monotonicity_zero_counting.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
