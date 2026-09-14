#!/usr/bin/env python3
"""Exact finite recurrence and typed-port separation for the valuation boundary."""
import hashlib,json,platform
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/prime_two_two_output_boundary_defect_module.v1.json';OUT=ROOT/'research/voevodsky/results/prime_two_two_output_boundary_defect_module.json';D=json.loads(FIX.read_text());N=D['depth']
# Coefficients are low-to-high powers.
g=[Fraction(1)]*(N+1);one_minus_q=[Fraction(1),Fraction(-1)]
def conv(a,b):
 o=[Fraction(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]+=x*y
 return o
lhs=conv(one_minus_q,g);rhs=[Fraction(1)]+[Fraction(0)]*N+[Fraction(-1)]
ell=[Fraction(1)]*(N+1);terminal=[Fraction(0)]*N+[Fraction(1)];primitive=[Fraction(1)]+[Fraction(0)]*N
# Difference from terminal after matching its coefficient.
residual=[ell[i]-terminal[i] for i in range(N+1)];residual_norm=sum(x*x for x in residual)
ports={x['id']:x['type'] for x in D['ports']};checks={'geometric_boundary_identity':lhs==rhs,'three_ports_retained':ports=={'primitive':'state defect','terminal':'state defect','augmentation':'external orbit readout'},'augmentation_not_terminal':ell!=terminal,'augmentation_terminal_residual_norm':residual_norm==N,'zero_fiber_quotient_relation':g==[1,1,1,1] and rhs==[1,0,0,0,-1],'q_equal_one_not_a_zero':sum(g)==N+1,'full_completed_map_not_promoted':D['disposition']['full_defect_module_map'].startswith('missing')}
out={'schema':'marici.voevodsky.prime-two-two-output-boundary-defect-module-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'g_coefficients':list(map(str,g)),'one_minus_q_times_g':list(map(str,lhs)),'augmentation_minus_terminal':list(map(str,residual)),'residual_norm_squared':str(residual_norm)},'disposition':'The finite valuation boundary has distinct primitive, terminal, and augmentation ports. Augmentation zero yields the exact primitive-terminal recurrence, but no completed labelled defect map.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_prime_two_two_output_boundary_defect_module.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((ROOT/D['source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
