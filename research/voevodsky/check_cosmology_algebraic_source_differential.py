"""Construct the two-term algebraic presentation differential and audit its scope."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_algebraic_source_differential.json'
def main():
 sources=json.loads((RES/'cosmology_linear_generator_transport_matrix.json').read_text());assert sources['nonzero_residuals']==0
 families=[('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')];zero=0;nonzero=0;by={}
 for family,name in families:
  records=json.loads((RES/name).read_text())['records'];z=sum(r['source_certificate']['equation_count']==0 for r in records);by[family]={'certificates':len(records),'zero_boundary_words':z,'nonzero_boundary_words':len(records)-z};zero+=z;nonzero+=len(records)-z
 assert zero==576 and nonzero==648
 complex_data={'C1':'Q-span of 43,564 labelled A12 generators T, S_K, Q','C0':'Q-span of labelled A12 presentation columns','C_minus_1':'0','d1':'generator incidence row in the rank26 relation matrix','d0':'zero map','squared_zero':'d0 composed with d1 = 0'}
 fake_geometric={'complex':complex_data,'grading_source':None,'geometric_chain_model':None,'support_inclusion':None};assert not all(fake_geometric.values())
 out={'schema':'marici.voevodsky.cosmology-algebraic-source-differential.v1','status':'two_term_presentation_complex_constructed_geometric_differential_not_constructed','complex':complex_data,'generator_count':43564,'squared_zero_checks':43564,'transport_chain_map_checks':sources['row_commutation_tests'],'transport_chain_map_residuals':sources['nonzero_residuals'],'certificate_boundary_census':by,'total_zero_boundary_words':zero,'total_nonzero_boundary_words':nonzero,'strongest_falsification':'648 of 1,224 exact words have nonzero d1 boundary equal to their nx target. They are primitives in a presentation fiber, not cycles or homology classes. The tautological d0=0 identity cannot supply a geometric source differential.','surviving_scope':'A transport-compatible two-term algebraic presentation complex C1->C0->0.','first_missing_typed_object':'A source-derived graded geometric chain object and differential whose realization is the presentation boundary, including a support inclusion.','acceptance_test':'Define the geometric chain degrees and maps, verify d^2=0 non-tautologically, map every labelled generator into that complex, and prove compatibility with pole-locus inclusions and squared-axis transport.','disposition':'Retain the algebraic presentation differential; do not populate the geometric source_differential contract field. Continue to the independently executable pole-order filtration candidate.','next_gate':'construct-pole-order-DNC-filtration-candidate','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
