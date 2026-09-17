#!/usr/bin/env python3
"""Rigorous normalization-level relative bound for the prime tail above mode 160."""
import json,math
from pathlib import Path
L=.55;N=160;mass=sum(math.log(p)/math.sqrt(p) for p in (2,3));d=math.log1p((N+1)*math.pi/(2*L));relative=mass/d
out={'schema':'marici.voevodsky.rank160-prime-relative-form-bound.v1','L':L,'first_tail_mode':N+1,'prime_operator_norm_bound':mass,'dirichlet_log_floor':d,'relative_log_form_bound':relative,'gamma_principal_log_coefficient':.5,'remaining_principal_coercivity':.5-relative,'normalization':'-sum log(p)/sqrt(p)*(T+T*)/2','passed':relative<.5,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'rank160_prime_relative_form_bound.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
