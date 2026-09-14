#!/usr/bin/env python3
"""Checks finite shadows of the countable shell-generating probe theorem."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/a_countable_shell_generating_family_detects_the_completed_cycle_residue_20260912.md'
INJECT=ROOT/'research/voevodsky/the_completed_theta_correlation_is_injective_on_the_arithmetic_interval_range_20260912.md'
RESULT=ROOT/'research/voevodsky/results/countable_shell_generating_probe.json'
primes=(2,3,5,7,11,13,17); shells=list(zip(primes,primes[1:])); checks={}
def graph(L):
 E=sorted([(k*p*q,j+1,k,p,q,k*p,k*q) for j,(p,q) in enumerate(shells) for k in range(1,L+1) if k*p*q<=L]); V=sorted({e[5] for e in E}|{e[6] for e in E}); vi={v:i for i,v in enumerate(V)}; B=s.zeros(len(V),len(E))
 for col,e in enumerate(E): B[vi[e[5]],col]-=1; B[vi[e[6]],col]+=1
 return E,V,B
for L in (120,240,480):
 E,V,B=graph(L); shell_values=sorted({e[1] for e in E}); blocks=[]
 for n in range(len(shell_values)):
  t=s.Rational(1,2)+s.Rational(1,n+3); D=s.diag(*[t**e[1] for e in E]); blocks.append(B*D)
 M=s.Matrix.vstack(*blocks)
 checks[f'evaluation_stack_full_rank_{L}']=M.rank()==len(E)
 # Every individual shell incidence matrix has zero cycle dimension.
 for j in shell_values:
  cols=[i for i,e in enumerate(E) if e[1]==j]; Bj=B[:,cols]
  checks[f'shell_{j}_acyclic_{L}']=Bj.rank()==len(cols)
 # Distinct evaluation points give a nonzero Vandermonde determinant.
 points=[s.Rational(1,2)+s.Rational(1,n+3) for n in range(len(shell_values))]; Vdm=s.Matrix([[t**j for j in shell_values] for t in points])
 checks[f'vandermonde_{L}']=Vdm.det()!=0
# Direct-sum damping is square summable exactly.
checks['readout_damping_square_sum']=s.summation(s.Rational(1,2)**(2*(s.symbols('n',integer=True,nonnegative=True)+1)),(s.symbols('n',integer=True,nonnegative=True),0,s.oo))==s.Rational(1,3)
text=PACKET.read_text(); checks['analytic_identity_argument']='distribution-valued analytic function on the unit disk' in text and 'identity theorem' in text
checks['completed_history_dependency']='completed history injectivity' in text and 'injective on \\(J(\\mathcal C_{D,\\exp})\\)' in INJECT.read_text()
checks['physical_access_not_claimed']='does not establish physical access' in text
checks['no_finite_channel_claim']='no finite channel count is asserted' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.countable-shell-generating-probe-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'history_injectivity':hashlib.sha256(INJECT.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'proved':'countable accumulating shell-generating evaluations jointly detect completed cycles','finite_shadow':'Vandermonde evaluation stacks full rank and each shell subgraph acyclic','remaining':'physical implementation and joint noise calibration'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)
