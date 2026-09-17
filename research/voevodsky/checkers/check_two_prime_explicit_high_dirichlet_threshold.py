#!/usr/bin/env python3
"""Compute the conservative high-Dirichlet coercivity threshold from registered constants."""
import json,math
from pathlib import Path
L=.55
# Unit-normalized multiplier is (Re psi-log pi)/2.
digamma_correction=(4+.5*math.log(20)+math.log(math.pi))/2
boundary_carleman=math.pi
prime=sum(math.log(p)/math.sqrt(p) for p in (2,3))
C=digamma_correction+boundary_carleman+prime
# .5 log(1+pi*M/(2L)) > C
M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1
margin=.5*math.log(1+math.pi*M/(2*L))-C
out={'schema':'marici.voevodsky.two-prime-explicit-high-dirichlet-threshold.v1','L':L,'constants':{'digamma_and_logpi':digamma_correction,'boundary_carleman':boundary_carleman,'absolute_prime_norm':prime,'total':C},'sufficient_mode_threshold':M,'strict_margin':margin,'conclusion':'Under the registered interval log-operator comparison, the pure high Dirichlet block is positive above this mode.','endpoint_requirement':'adjoin the two endpoint representers to the finite space','remaining_band':f'certify coupled modes 160 through {M-1}','passed':margin>0,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_explicit_high_dirichlet_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
