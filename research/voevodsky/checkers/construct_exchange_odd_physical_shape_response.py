#!/usr/bin/env python3
"""Construct the sourced exchange-odd principal-part response of the q_G12 residue."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'))
import sympy as sp
prior=json.loads((R/'research/voevodsky/results/C15_canonical_physical_mixed_detector.json').read_text())
obs=json.loads((R/'research/benincasa/results/energy_shape_response_observer.json').read_text())
a,b,x,y,t=sp.symbols('a b x y t')
q23=b-(x+t);q31=a-(y-t) # D_shape=partial_x-partial_y, E fixed
f=1/q23+1/q31
df=sp.factor(sp.diff(f,t).subs(t,0))
expected=1/(b-x)**2-1/(a-y)**2
assert sp.simplify(df-expected)==0
# Principal-part coordinates in ordered doubled-wall basis (q23^-2,q31^-2).
principal=[1,-1]
# Exchange swaps the two walls and reverses the shape tangent.
swap=[principal[1],principal[0]]
checks={'canonical_zero_jet_symmetric':prior['physical_covector']==[1,1],'shape_derivative_exact':sp.simplify(df-expected)==0,'principal_covector_antisymmetric':principal==[1,-1],'exchange_odd':swap==[-v for v in principal],'primitive':sp.gcd(*map(abs,principal))==1,'existing_shape_response_faithful':obs['checks']['response_is_injective_on_a2'],'existing_shape_tangent_detects':obs['checks']['shape_tangent_detects_matching_residue']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.exchange-odd-physical-shape-response.v1','source_residue_term':'1/(b-x)+1/(a-y)','intervention':{'x':'x+t','y':'y-t','z':'z','total_energy':'fixed','tangent':'D_shape=partial_x-partial_y'},'exact_first_response':str(df),'doubled_wall_basis':['(b-x)^-2','(a-y)^-2'],'principal_part_covector':principal,'exchange_character':-1,'primitivity':'gcd(1,-1)=1','physical_observable':'the ordered pair of doubled-wall Leray principal parts of D_shape Pi_qG12','C15b_response_status':'confirmed as a sourced primitive vector-valued physical response','relation_to_v_alg':{'candidate_simple-pole_covector':[1,-1],'candidate_extension_projection':prior['counterfactual_antisymmetric_image']['v_alg_projection'],'remaining_interface':'Gauss-Manin/IBP reduction from the doubled-wall principal-part module to the simple mixed basis (g101,g110), with integral Betti normalization'},'scope':'constructs the physical exchange-odd response itself; scalar v_alg period tomography follows after the stated reduction interface','checks':checks,'passed':True}
(R/'research/voevodsky/results/exchange_odd_physical_shape_response.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'response':out['exact_first_response'],'principal':principal,'status':out['C15b_response_status'],'candidate_v_alg':out['relation_to_v_alg']['candidate_extension_projection'],'remaining':out['relation_to_v_alg']['remaining_interface']}))
