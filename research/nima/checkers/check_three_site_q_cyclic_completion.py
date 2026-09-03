"""Verify cyclic completion of the ten three-site physical q rows."""
import json
from pathlib import Path
ROOT=Path('research')
census=json.loads((ROOT/'benincasa/generic_lower_positive_chain_census_result.json').read_text())
link=json.loads((ROOT/'benincasa/three-site-physical-residue-link.json').read_text())
rows={k:v['coefficient_vector_a_b_c_X1_X2_X3'] for k,v in census['source_poles'].items()}
rho={'q_G':'q_G','q_g1':'q_g2','q_g2':'q_g3','q_g3':'q_g1','q_G12':'q_G23','q_G23':'q_G31','q_G31':'q_G12','q_g12':'q_g23','q_g23':'q_g31','q_g31':'q_g12'}
# Source relabelling a->b->c->a and X1->X2->X3->X1.
dest=[1,2,0,4,5,3]
def act(v,perm=dest):
 out=[0]*6
 for i,j in enumerate(perm):out[j]=v[i]
 return out
def defects(perm=dest):return [k for k,v in rows.items() if act(v,perm)!=rows[rho[k]]]
baseline=defects();assert baseline==[] and len(rows)==10
cycle=link['labelled_link_cycle'];rot=[rho[x] for x in cycle]
assert rot==cycle[4:]+cycle[:4]
signs=link['exact_result']['source_order_residue_signs'];assert signs[4:]+signs[:4]==signs
wrong=defects([1,0,2,4,3,5]);assert wrong
out={'schema':'marici.nima.three-site-q-cyclic-completion.v1','status':'passed','row_count':10,'cyclic_row_defects':baseline,'label_orbits':[['q_G'],['q_g1','q_g2','q_g3'],['q_G12','q_G23','q_G31'],['q_g12','q_g23','q_g31']],'link_cycle_rotation_offset':4,'residue_sign_sequence_preserved':True,'hostile_noncyclic_permutation_defects':wrong,'result':'all four previously missing rows are present and belong to the sourced cyclic orbits','next_missing':'exact normalized single and sequential residue maps, not divisor coefficients','claim_boundary':'coefficient-row and incidence equivariance only; no integrated factorization theorem'}
(ROOT/'nima/results/three-site-q-cyclic-completion.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
