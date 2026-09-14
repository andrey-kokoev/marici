#!/usr/bin/env python3
"""Exact finite-sampling obstruction to all-jet trace identification."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
TRACE=ROOT/'research/voevodsky/contracts/radial-jointly-faithful-sampled-four-trace.v1.json'
RH=ROOT/'research/aspect/contracts/theta-rh-interaction-net-state.v3.json'
RESULT=ROOT/'research/voevodsky/results/finite_samples_vs_all_jet_response.json'
t=json.loads(TRACE.read_text()); h=json.loads(RH.read_text()); r=s.symbols('r')
nodes=[s.Rational(2*j+1,24) for j in range(12)]
p=s.prod(r-a for a in nodes).expand(); samples=[p.subs(r,a) for a in nodes]; derivatives=[s.diff(p,r).subs(r,a) for a in nodes]
checks={}
checks['twelve_distinct_nodes']=len(set(nodes))==12
checks['obstruction_polynomial_degree_12']=s.Poly(p,r).degree()==12 and p!=0
checks['all_point_samples_zero']=samples==[0]*12
checks['all_first_derivatives_nonzero']=all(x!=0 for x in derivatives)
checks['sampling_not_injective_on_degree_12']=p!=0 and all(x==0 for x in samples)
# Degree <=11 interpolation is faithful: Vandermonde determinant is nonzero.
V=s.Matrix([[a**k for k in range(12)] for a in nodes])
checks['degree_at_most_11_reconstruction_available']=V.det()!=0 and V.rank()==12
# Removing one sample destroys degree <=11 square reconstruction.
checks['eleven_samples_insufficient_for_degree_11']=V[:-1,:].rank()==11
constructors={x['id']:x['status'] for x in h['constructors']}
checks['source_claims_all_jet_readout_constructed']=constructors.get('all_jet_laplace_readout')=='constructed'
checks['synthetic_carrier_only_retains_12_samples']=t['trace_family']['P_shadow']['dimension']==12 and t['trace_family']['Q_shadow']['dimension']==12
serialized=TRACE.read_text()+RH.read_text()
checks['no_finite_determination_theorem_declared']=not any(x in serialized for x in ('degree_at_most_11','bandlimited_reconstruction','sampling_isomorphism','finite_determination_theorem'))
# Hostile promotion must be rejected even though the finite chain itself is faithful.
checks['finite_internal_faithfulness_not_all_jet_faithfulness']=t['comparison']['jointly_faithful'] and checks['sampling_not_injective_on_degree_12']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.finite-samples-vs-all-jet-response.v1','input_digests':{'trace':hashlib.sha256(TRACE.read_bytes()).hexdigest(),'rh_v3':hashlib.sha256(RH.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'obstruction':{'polynomial':str(s.factor(p)),'degree':12,'sample_values':[str(x) for x in samples],'nonzero_first_derivatives':[str(x) for x in derivatives]},'disposition':{'synthetic_chain':'faithful_on_declared_26_coordinate_retained_lattice_carrier','source_comparison':'noninjective_if_source_carrier_contains_degree_12_obstruction','reopening':['degree_at_most_11_source_bound','invertible_source_evaluation_matrix','bandlimit_plus_sampling_theorem','jointly_conservative_derivative_family','retain_full_function_valued_trace']}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'obstruction_degree':12,'nonzero_derivatives':len(derivatives)}))
raise SystemExit(0 if result['passed'] else 1)
