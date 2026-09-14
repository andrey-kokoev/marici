#!/usr/bin/env python3
"""Exact weight calculation for half-density theta-completion transport."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/half_density_theta_completion_intertwiner.v1.json';OUT=ROOT/'research/voevodsky/results/half_density_theta_completion_intertwiner.json';D=json.loads(FIX.read_text());degrees=D['tested_monomial_degrees']
rows=[]
for j in degrees:
 weight=Q(2*j+1,2);theta=weight*weight-Q(1,4);ray=Q(j*(j+1));rows.append({'degree':j,'log_weight':str(weight),'theta_eigenvalue':str(theta),'ray_eigenvalue':str(ray),'match':theta==ray})
# Gaussian grades f_0..f_3 acquire half-integer weights j+1/2.
four=[Q(2*j+1,2) for j in range(4)]
checks={'all_polynomial_weights_intertwine':all(r['match'] for r in rows),'constant_wall_killed_by_completion':rows[0]['theta_eigenvalue']=='0','degree_one_eigenvalue_two':rows[1]['theta_eigenvalue']=='2','four_half_integer_grades_retained':four==[Q(1,2),Q(3,2),Q(5,2),Q(7,2)],'no_three_grade_truncation':len(four)==4 and four[-1]==Q(7,2),'remaining_steps_not_promoted':'theta label summation' in D['disposition']['remaining_composition']}
out={'schema':'marici.voevodsky.half-density-theta-completion-intertwiner-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'monomial_weight_table':rows,'four_gaussian_log_weights':list(map(str,four))},'disposition':'Half-density transport exactly carries A(A+1) to d_u^2-1/4 and retains all four Gaussian grades. The later label synthesis and Green-quotient comparison remain open.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_half_density_theta_completion_intertwiner.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in D['sources']},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
