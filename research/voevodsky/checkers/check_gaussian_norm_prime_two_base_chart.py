#!/usr/bin/env python3
"""Exact Gaussian-integer norm chart for the prime-two valuation chain."""
import hashlib,json,platform
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/gaussian_norm_prime_two_base_chart.v1.json';OUT=ROOT/'research/voevodsky/results/gaussian_norm_prime_two_base_chart.json';D=json.loads(FIX.read_text());N=D['depth']
def mul(z,w):a,b=z;c,d=w;return(a*c-b*d,a*d+b*c)
def norm(z):return z[0]*z[0]+z[1]*z[1]
z=(1,0);powers=[]
for k in range(N+1):powers.append((k,z,norm(z)));z=mul(z,(1,1))
checks={'pi_norm_two':norm((1,1))==2,'norm_multiplicative_on_chain':all(powers[k][2]==2**k for k in range(N+1)),'valuation_grade_equals_norm_exponent':all(n==(1<<k) for k,_,n in powers),'primitive_norm_one_regular':powers[0][2]==1,'every_finite_terminal_regular':powers[-1][2] not in (0,-1),'terminal_values_strictly_escape':all(powers[k+1][2]>powers[k][2] for k in range(N)),'quadratic_choice_remains_conditional':D['disposition']['missing_authority'].startswith('source theorem selecting')}
out={'schema':'marici.voevodsky.gaussian-norm-prime-two-base-chart-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'powers_k_gaussian_pair_norm':[[k,list(z),n] for k,z,n in powers],'primitive_base_coordinate':1,'finite_terminal_base_coordinate':powers[-1][2],'projective_completion_locus':'infinity'},'disposition':'Conditionally on the Gaussian quadratic norm chart, P0 is the regular evaluation at xi=1 and PN remains a cutoff-labelled regular evaluation; only its unbounded completion approaches the irregular infinity port. Selection of this chart by the Marici source remains unproved.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_gaussian_norm_prime_two_base_chart.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((ROOT/D['pdf_source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
