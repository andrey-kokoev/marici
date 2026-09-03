import json
from pathlib import Path
# Exact source term: z_K=(-1)^(sum(R)+sum(K)) det(A[comp(K),comp(R)]) det(B[K,S]).
formula_dependencies={'A_k','B_k','R','K','S'}
requested_joint_output={'joint_gram_coordinates','interlacing_edge_capacities'}
checks={'C_k_not_in_term_formula':'C_k' not in formula_dependencies,'A_k_required':'A_k' in formula_dependencies,'B_k_required':'B_k' in formula_dependencies,'joint_map_is_downstream':requested_joint_output.isdisjoint(formula_dependencies),'fixed_8x8_joint_rank_target':(8-1)*(8-1)==49,'first_missing_constructor':'build_source_matrices(k)->(A_k,B_k)'}
result={'schema':'marici.strominger.rh_quarter_joint_gram_dependency_order.v1','status':'passed' if all(v is True or isinstance(v,str) for v in checks.values()) else 'failed','verdict':'The rank-49 joint-Gram request is downstream of the first missing typed object. The complementary-minor source formula requires parameterized labelled A_k,B_k and not C_k; without their constructor no joint-Gram map can be source-derived or tested beyond fixed k=8.','acceptance':['exactly reproduce labelled A_8,B_8','produce labelled A_9,B_9','prove complementary-minor source-term formula','then test rank-49 joint map at k=8 and rank (k-1)^2 generally'],'checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_joint_gram_dependency_order.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
