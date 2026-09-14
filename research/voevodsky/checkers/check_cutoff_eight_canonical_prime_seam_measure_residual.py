#!/usr/bin/env python3
"""Exact symbolic finite canonical-prime versus continuous seam mass residual."""
import hashlib,json,platform
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/cutoff_eight_canonical_prime_seam_measure_residual.v1.json';OUT=ROOT/'research/voevodsky/results/cutoff_eight_canonical_prime_seam_measure_residual.json';D=json.loads(FIX.read_text());X=D['cutoff']
def prime_power_base(n):
 for p in range(2,n+1):
  if any(p%d==0 for d in range(2,p)):continue
  x=p
  while x<n:x*=p
  if x==n:return p
 return None
# Vectors are rational coefficients of log(2),log(3),log(5),log(7).
primes=[2,3,5,7];arith={p:Fraction(0) for p in primes};atoms=[]
for n in range(2,X+1):
 p=prime_power_base(n)
 if p is not None:
  arith[p]+=Fraction(1,n);atoms.append((n,p,Fraction(1,n)))
continuous={p:Fraction(0) for p in primes};continuous[2]=Fraction(3)
residual={p:arith[p]-continuous[p] for p in primes}
expected={2:Fraction(-17,8),3:Fraction(1,3),5:Fraction(1,5),7:Fraction(1,7)}
# The interval (log 2,log 3) has no prime-power log since no integer lies strictly in (2,3).
checks={'von_mangoldt_prime_power_atoms':[(n,p) for n,p,_ in atoms]==[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)],'arithmetic_mass_coefficients':arith=={2:Fraction(7,8),3:Fraction(1,3),5:Fraction(1,5),7:Fraction(1,7)},'continuous_mass_coefficients':continuous[2]==3 and all(continuous[p]==0 for p in [3,5,7]),'residual_coefficients':residual==expected,'residual_nonzero_by_unique_factorization':any(v for v in residual.values()),'prime_power_free_open_interval_2_3':not any(2<n<3 for n in range(2,X+1)),'mate_explicitly_blocked':D['disposition']['mate_status'].startswith('blocked')}
def fmt(v):return str(v)
out={'schema':'marici.voevodsky.cutoff-eight-canonical-prime-seam-measure-residual-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'atoms_n_prime_weight':[[n,p,fmt(w)] for n,p,w in atoms],'arithmetic_log_prime_coefficients':{str(p):fmt(v) for p,v in arith.items()},'continuous_log_prime_coefficients':{str(p):fmt(v) for p,v in continuous.items()},'residual_log_prime_coefficients':{str(p):fmt(v) for p,v in residual.items()}},'disposition':'Canonical arithmetic incidence does not equal continuous seam accumulation even on the constant test at cutoff eight. The mismatch is retained as a defect component; constructing the completed mate is blocked pending independent sampling faithfulness or a source coboundary.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_cutoff_eight_canonical_prime_seam_measure_residual.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in D['sources']},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
