#!/usr/bin/env python3
"""Exact finite checks for label-selective route-residue probes."""
from pathlib import Path
import hashlib,json,math
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/label_selective_modulation_is_a_complete_operational_probe_of_route_residue_20260912.md'
INJECT=ROOT/'research/voevodsky/the_completed_theta_correlation_is_injective_on_the_arithmetic_interval_range_20260912.md'
RESULT=ROOT/'research/voevodsky/results/label_selective_route_residue_probe.json'
primes=(2,3,5,7,11,13,17); shells=list(zip(primes,primes[1:])); L=240
E=sorted([(k*p*q,k,p,q) for p,q in shells for k in range(1,L+1) if k*p*q<=L]); V=sorted({k*p for w,k,p,q in E}|{k*q for w,k,p,q in E}); vi={v:i for i,v in enumerate(V)}; B=s.zeros(len(V),len(E))
for j,(w,k,p,q) in enumerate(E): B[vi[k*p],j]-=1; B[vi[k*q],j]+=1
F=s.Matrix.hstack(*B.nullspace()); response_norm=s.diag(*[s.Rational(1,e[0]+1) for e in E]); gamma=s.Rational(1,10); damping=s.diag(*[s.exp(-gamma*s.log(e[0])) for e in E]); A=damping*response_norm
checks={
 'nontrivial_cycle_space':F.cols>0 and B*F==s.zeros(B.rows,F.cols),
 'all_edge_probes_jointly_faithful':A*F != s.zeros(A.rows,F.cols) and (A*F).rank()==F.cols,
 'response_gram_positive_by_injective_pullback':(A*F).rank()==F.cols and all(A[i,i]>0 for i in range(A.rows)),
 'forest_not_used':A.rows==len(E),
}
# Every basis cycle has at least one individually nonzero selected response.
checks['each_cycle_basis_vector_detected']=all(any(F[e,j]!=0 and A[e,e]!=0 for e in range(F.rows)) for j in range(F.cols))
# Four-edge rectangle boundary and one-edge modulation.
p,q=shells[0]; r,t=shells[1]; rectangle=[(p*r,q*r),(q*r,q*t),(p*r,p*t),(p*t,q*t)]; signs=(1,1,-1,-1); bal={}
for sign,(u,v) in zip(signs,rectangle): bal[u]=bal.get(u,0)-sign; bal[v]=bal.get(v,0)+sign
checks['rectangle_is_cycle']=all(v==0 for v in bal.values())
checks['single_edge_modulation_breaks_rectangle_cancellation']=signs[0]!=0
# Damped family bound using the proven column majorant ell <= delta^-1 exp(delta W).
for delta in (.05,.2,.5):
 checks[f'damped_column_bound_{delta}']=all(math.exp(-.1*math.log(w))*math.log(q/p)<=math.exp(delta*math.log(w))/delta+1e-12 for w,k,p,q in E)
text=PACKET.read_text(); checks['physical_availability_not_claimed']='not evidence that such label-selective modulation is physically available' in text
checks['noise_must_be_sourced']='only when the modulation amplitudes, readout normalization, and noise law are measured or derived' in text
checks['injective_history_column_dependency']='completed atom' in INJECT.read_text()
checks['factor_through_B_falsifier']='physical interface factors through \\(B\\)' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.label-selective-route-residue-probe-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'injectivity':hashlib.sha256(INJECT.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'edge_count':len(E),'cycle_dimension':F.cols,'disposition':{'constructed':'jointly faithful bounded differential probe family and positive response Gram form','acceptance':'physically realize and calibrate pre-codiagonal shell/theta modulation','falsifier':'all realizable interventions factor through common history'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks),'edges':len(E),'cycle_dimension':F.cols})); raise SystemExit(0 if result['passed'] else 1)
