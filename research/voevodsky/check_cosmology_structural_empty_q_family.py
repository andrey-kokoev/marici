"""Derive the empty q-target family from x-dependence of raw q relations."""
from __future__ import annotations
import json,os,sys
os.environ['MARICI_AMBIENT']='12'
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_structural_empty_q_family.json'
def main():
 names=list(rees.NAMES);_,q_derivatives=base.parameter_derivative_data(0,(4,5,-3));dx=[q_derivatives[name] for name in names]
 zero_indices=[i for i,row in enumerate(dx) if not row];nonzero_indices=[i for i,row in enumerate(dx) if row]
 assert zero_indices==[0,2,4] and nonzero_indices==[1,3]
 census=json.loads((RES/'cosmology_empty_q_certificates_independent_point.json').read_text())['by_q_index']
 assert all(census[str(i)]['empty_at_both']==192 for i in zero_indices)
 assert all(census[str(i)]['nonempty_at_both']==192 for i in nonzero_indices)
 # A q row is e_label - q_i*e_raised. Parameter differentiation kills the constant first term.
 # Hence d_x(row) = -(d_x q_i)*e_raised, identically in point, pole, level, and exponent.
 out={'schema':'marici.voevodsky.cosmology-structural-empty-q-family.v1','status':'q_indices_0_2_4_structurally_zero_under_nx','source_names':names,'dx_q_polynomials':[{str(k):v for k,v in row.items()} for row in dx],'zero_indices':zero_indices,'nonzero_indices':nonzero_indices,'identity':'d_x(e_label - q_i e_raised) = -(d_x q_i)e_raised','derivation':'g1, g3, and g31 are independent of x, while g2 and g23 contain -x with derivative -1. Therefore all 192 descriptors for each of q indices 0,2,4 have identically zero nx target; the other two families have a one-column target.','certificate_consequence':'The 576 empty words are canonical structural zero contractions, independent of evaluation point.','scope':'nx=(1,0,0) parameter derivative of raw q relation rows only; no source differential, geometric support, DNC comparison, or horn claim.','next_gate':'serialize-source-word-transport-action','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
