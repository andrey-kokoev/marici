#!/usr/bin/env python3
"""Correct the invariant/coinvariant comparison by separating projection from norm."""
import json
from pathlib import Path
# For the permutation module Z{g+,g-}: q(sum)=2[g], while Norm([g])=sum.
projection_on_invariant=2
norm_on_coinvariant=1
assert projection_on_invariant==2
assert norm_on_coinvariant==1
assert norm_on_coinvariant in (1,-1)
out={'schema':'marici.benincasa.qg12-root-pair-norm-transfer-correction.v1','problem':'Does the factor two in the projection from invariants to coinvariants prevent a canonical primitive comparison of the unordered root target?','bold_conjecture':'The Z/2 cokernel of invariant inclusion followed by quotient implies invariants and coinvariants can only be compared after inverting two.','named_rivals':['the norm map from coinvariants to invariants is an integral isomorphism for the transitive permutation module','projection and norm are distinct comparison arrows','primitivity depends on which arrow represents the physical map'],'risky_consequences':['every canonical comparison must multiply by two','no integral map may send the coinvariant generator to the invariant sum primitively'],'strongest_falsification_attempt':{'projection_q_on_invariant_generator':'q(gamma_plus+gamma_minus)=2[gamma]','projection_matrix':[2],'norm_on_coinvariant_generator':'N([gamma])=gamma_plus+gamma_minus','norm_matrix':[1],'norm_is_integral_isomorphism':True},'disposition':{'status':'bold conjecture falsified; prior scope corrected','surviving_scope':'the projection invariants-to-coinvariants has cokernel Z/2, but the reverse norm is an integral isomorphism for this permutation module','remaining_gate':'the source contour must specify whether its chain map is projection-like, norm-like, or another correspondence; target type alone does not decide the multiplicity'},'corrects':'research/benincasa/results/qg12_invariants_coinvariants_primitivity_dpc.json','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'qg12_root_pair_norm_transfer_correction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
