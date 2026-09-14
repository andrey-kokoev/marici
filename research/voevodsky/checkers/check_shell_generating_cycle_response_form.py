#!/usr/bin/env python3
"""Exact finite shadows of the shell-generating response Gram form."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/shell_generating_readouts_induce_a_positive_cycle_response_form_20260912.md'
PROBE=ROOT/'research/voevodsky/a_countable_shell_generating_family_detects_the_completed_cycle_residue_20260912.md'
RESULT=ROOT/'research/voevodsky/results/shell_generating_cycle_response_form.json'
primes=(2,3,5,7,11,13,17); shells=list(zip(primes,primes[1:])); checks={}
for L in (120,240,480):
 E=sorted([(k*p*q,j+1,k,p,q,k*p,k*q) for j,(p,q) in enumerate(shells) for k in range(1,L+1) if k*p*q<=L]); V=sorted({e[5] for e in E}|{e[6] for e in E}); vi={v:i for i,v in enumerate(V)}; B=s.zeros(len(V),len(E))
 for col,e in enumerate(E): B[vi[e[5]],col]-=1; B[vi[e[6]],col]+=1
 F=s.Matrix.hstack(*B.nullspace()); shell_count=len({e[1] for e in E}); blocks=[]; Q=s.zeros(F.cols)
 for n in range(shell_count):
  t=s.Rational(1,2)+s.Rational(1,n+3); alpha=s.Rational(1,2)**(n+1); D=s.diag(*[t**e[1] for e in E]); A=B*D*F; blocks.append(A); Q += alpha**2*A.T*A
 stacked=s.Matrix.vstack(*blocks)
 checks[f'joint_response_rank_{L}']=stacked.rank()==F.cols
 checks[f'positive_definite_pullback_{L}']=stacked.rank()==F.cols and Q.det()!=0
 # Coordinate congruence under a fixed unimodular shear when dimension permits.
 C=s.eye(F.cols)
 if F.cols>1: C[0,1]=1
 FU=F*C; QU=C.T*Q*C; QU_direct=s.zeros(F.cols)
 for n in range(shell_count):
  t=s.Rational(1,2)+s.Rational(1,n+3); alpha=s.Rational(1,2)**(n+1); AU=B*s.diag(*[t**e[1] for e in E])*FU; QU_direct += alpha**2*AU.T*AU
 checks[f'presentation_congruence_{L}']=QU==QU_direct
 checks[f'finite_cutoff_restriction_{L}']=Q.rows==F.cols and Q.is_symmetric()
checks['damping_sum']=s.summation(s.Rational(1,4)**(s.symbols('n',integer=True,nonnegative=True)+1),(s.symbols('n',integer=True,nonnegative=True),0,s.oo))==s.Rational(1,3)
text=PACKET.read_text(); probe_text=PROBE.read_text(); checks['probe_dependency']='joint faithfulness' in text.lower() and 'identity theorem' in probe_text
checks['correlated_noise_allowed']='Correlated noise is allowed' in text
checks['physical_calibration_not_claimed']='physical interpretation requires three measured arrows' in text
checks['design_nonuniqueness']='Changing \\((t_n,\\alpha_n)\\) changes \\(Q_{\\rm resp}\\)' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.shell-generating-cycle-response-form-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'probe_theorem':hashlib.sha256(PROBE.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'constructed':'positive reciprocal presentation-independent response form from countable probe design','physical_gate':['realize t^j modulation','validate differential history readout','measure joint noise operator']}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)
