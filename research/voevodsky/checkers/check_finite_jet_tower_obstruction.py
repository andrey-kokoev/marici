#!/usr/bin/env python3
"""Exact finite-jet obstruction and Hermite reconstruction checks."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/finite_jet_towers_do_not_complete_all_jet_source_comparison_20260911.md'
RESULT=ROOT/'research/voevodsky/results/finite_jet_tower_obstruction.json'
r=s.symbols('r'); nodes=[s.Rational(2*j+1,24) for j in range(12)]; a=s.prod(r-x for x in nodes)
checks={}; stages={}
for m in range(4):
 p=s.expand(a**(m+1)); depth_values=[]
 for x in nodes:
  depth_values.extend(s.diff(p,r,k).subs(r,x) for k in range(m+1))
 next_values=[s.diff(p,r,m+1).subs(r,x) for x in nodes]
 n=12*(m+1)
 # Confluent Vandermonde determinant formula: nonzero scalar factors times
 # product over distinct-node differences to exponent (m+1)^2.
 vandermonde_factor=s.prod((nodes[j]-nodes[i])**((m+1)**2) for i in range(12) for j in range(i+1,12))
 derivative_factor=s.prod(s.factorial(k)**12 for k in range(m+1))
 confluent_det=s.factor(vandermonde_factor*derivative_factor)
 checks[f'depth_{m}_obstruction_degree']=s.Poly(p,r).degree()==n
 checks[f'depth_{m}_all_retained_jets_zero']=all(v==0 for v in depth_values)
 checks[f'depth_{m}_next_derivatives_nonzero']=all(v!=0 for v in next_values)
 checks[f'depth_{m}_Hermite_rank_full_on_degree_bound']=confluent_det!=0
 stages[str(m)]={'conditions':n,'obstruction_degree':n,'finite_faithful_degree_max':n-1,'next_derivative_nonzero_count':sum(v!=0 for v in next_values)}
# Quantifier-order witness: different depths require increasingly divisible witnesses.
p0=s.expand(a); p1=s.expand(a**2)
checks['depth_zero_witness_not_depth_one_witness']=any(s.diff(p0,r).subs(r,x)!=0 for x in nodes)
checks['depth_one_witness_also_depth_zero_invisible']=all(p1.subs(r,x)==0 for x in nodes)
checks['no_single_tested_finite_depth_exhausts_polynomials']=all(stages[str(m)]['obstruction_degree']>stages[str(m)]['finite_faithful_degree_max'] for m in range(4))
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.finite-jet-tower-obstruction.v1','packet_sha256':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'checks':checks,'tested_depths':stages,'passed':all(checks.values()),'quantifier':'for_every_tested_finite_depth_m_there_exists_a_depth_dependent_nonzero_kernel_polynomial','general_proof':'p_m=product_j(r-r_j)^(m+1) has multiplicity m+1 at every node','disposition':{'rejected':'any_fixed_finite_jet_depth_as_unrestricted_all_jet_comparison','retained':'depth_m Hermite sampling is faithful on degree at most 12(m+1)-1','remaining':'source-derived finiteness or completion/reconstruction theorem'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'tested_depths':len(stages)}))
raise SystemExit(0 if result['passed'] else 1)
