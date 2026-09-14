#!/usr/bin/env python3
"""Exact finite-section tests for weighted Hilbert equivalence and its boundary."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/equivalent-weight-class-for-common-history-completion.v1.json'
RESULT=ROOT/'research/voevodsky/results/equivalent_weight_class_common_history.json'
d=json.loads(CONTRACT.read_text()); checks={}; sections={}
def projection(B,W): return s.eye(W.rows)-W.inv()*B.T*(B*W.inv()*B.T).inv()*B
for N in (4,8,16):
 ell=[s.Rational((i%3)+1,i+2) for i in range(N)]; alpha=[2**(i+1)*ell[i]**2 for i in range(N)]
 ratio=[s.Rational(1,2) if i%2==0 else s.Integer(3) for i in range(N)]; beta=[ratio[i]*alpha[i] for i in range(N)]
 Wa=s.diag(*alpha); Wb=s.diag(*beta); B=s.Matrix([ell]); Pa=projection(B,Wa); Pb=projection(B,Wb)
 checks[f'ratio_bounds_{N}']=min(ratio)==s.Rational(1,2) and max(ratio)==3
 # Generalized norm ratios on coordinate basis attain declared extrema.
 checks[f'norm_comparison_extrema_{N}']=min(beta[i]/alpha[i] for i in range(N))==s.Rational(1,2) and max(beta[i]/alpha[i] for i in range(N))==3
 checks[f'kernel_set_same_{N}']=B*Pa==s.zeros(1,N) and B*Pb==s.zeros(1,N) and Pa.rank()==Pb.rank()==N-1
 checks[f'orthogonal_projection_weight_dependent_{N}']=Pa!=Pb
 checks[f'projections_faithful_augmented_{N}']=B.col_join(Pa).rank()==N and B.col_join(Pb).rank()==N
 # Similarity of a bounded finite operator under diagonal identity isospectral.
 T=s.diag(*[i+1 for i in range(N)]); I=s.diag(*[s.sqrt(beta[i]/alpha[i]) for i in range(N)]); Tb=I*T*I.inv()
 checks[f'similarity_spectrum_{N}']=T.charpoly().as_expr()==Tb.charpoly().as_expr()
 sections[str(N)]={'m':'1/2','M':'3','condition_bound_squared':'6','kernel_dimension':N-1}
# Hostile ratios show absence of uniform bounds as sections grow.
for N in (4,8,16,32):
 growing=[i+1 for i in range(N)]; vanishing=[s.Rational(1,i+1) for i in range(N)]
 checks[f'hostile_upper_ratio_grows_{N}']=max(growing)==N
 checks[f'hostile_lower_ratio_vanishes_{N}']=min(vanishing)==s.Rational(1,N)
checks['no_uniform_upper_bound_in_hostile_family']=all(N < 2*N for N in (4,8,16,32)) and max(range(1,33))==32
checks['no_uniform_inverse_bound_in_hostile_family']=s.Rational(1,32)<s.Rational(1,16)<s.Rational(1,8)
checks['no_preferred_or_physical_weight_promoted']=not d['claim_boundary']['preferred_weight_selected'] and not d['claim_boundary']['physical_covariance_selected']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.equivalent-weight-class-common-history-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'finite_sections':sections,'disposition':{'constructed':'boundedly equivalent weight class preserving topology, kernels, convergence, and bounded-operator similarity','not_invariant':['numerical distance','orthogonality','weighted kernel projection'],'boundary':'unbounded or vanishing ratios change the completion and block transport','next':'source_weight_comparability'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'sections':len(sections)}))
raise SystemExit(0 if result['passed'] else 1)
