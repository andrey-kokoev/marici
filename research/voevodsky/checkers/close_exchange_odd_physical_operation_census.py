#!/usr/bin/env python3
"""Close the current-source census of exchange/deck-odd physical operations relevant to v_alg."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3];B=R/'research/benincasa'
shape=json.loads((R/'research/voevodsky/results/exchange_odd_physical_shape_response.json').read_text())
inf=json.loads((B/'results/infinity-physical-leray-covector.json').read_text())
a3=json.loads((B/'results/endpoint-a3-log-residue.json').read_text())
tri=json.loads((B/'soft-triangle-supported-antitrace-cone.json').read_text())
top=json.loads((R/'research/voevodsky/results/top_sector_triple_leray_valg_pairing_audit.json').read_text())
rows=[
 {'operation':'exchange-odd q_G12 shape derivative','physical_odd':True,'typed_to_mixed_family':True,'v_alg_status':'candidate nonzero after lowering','blocker':'filtered IBP lowering'},
 {'operation':'top-sector triple logarithmic tube','physical_odd':False,'typed_to_mixed_family':True,'v_alg_status':'zero','blocker':'physical occurrence weights are (1,1)'},
 {'operation':'physical infinity Leray line','physical_odd':True,'typed_to_mixed_family':False,'v_alg_status':'zero','blocker':'canonical covector annihilates v_alg'},
 {'operation':'one-sided endpoint A3 log residue','physical_odd':True,'typed_to_mixed_family':False,'v_alg_status':'untyped','blocker':'no comparison from odd Milnor line to mixed marked extension'},
 {'operation':'soft-triangle supported antitrace','physical_odd':True,'typed_to_mixed_family':False,'v_alg_status':'untyped','blocker':'only local costalks; physical global image is diagonal and global pushforward absent'},
]
checks={'shape_is_sourced_primitive_odd':shape['principal_part_covector']==[1,-1] and shape['passed'],'infinity_kills_valg':'v_alg' in inf['kernel_annihilated'],'a3_is_physical_odd':'reflection-odd' in a3['classification'],'triangle_global_period_not_claimed':'no claim of a nonzero global period' in tri['scope'],'top_rejected':top['status'].startswith('rejected'),'unique_typed_nonzero_candidate':sum(r['physical_odd'] and r['typed_to_mixed_family'] and r['v_alg_status'].startswith('candidate') for r in rows)==1}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.exchange-odd-physical-operation-census-closure.v1','audited_operations':rows,'result':'Within the serialized source envelope, the q_G12 exchange-odd shape derivative is the unique physical odd operation already typed to the mixed marked family and not known to have zero v_alg projection.','frontier_returns_to':'VA0_construct_filtered_IBP_lowering','why_not_redundant':'Alternative discriminant families have now been exhausted or shown untyped; lowering the already sourced doubled-wall response is the sole admitted continuation.','acceptance_contract':{'input_basis':['q_g23^-2','q_g31^-2'],'input_covector':[1,-1],'output_basis':['g101','g110'],'must_preserve':['exchange-odd character','relative exact quotient','source physical cycle','integral lattice'],'success':'output has nonzero antisymmetric component'},'checks':checks,'passed':True}
d=R/'research/voevodsky/results/exchange_odd_physical_operation_census_closure.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'unique':'exchange-odd q_G12 shape derivative','frontier':out['frontier_returns_to']}))
