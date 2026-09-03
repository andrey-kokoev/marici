#!/usr/bin/env python3
"""Test the third tau residue against boundary-only constrained corrections."""
import json
from pathlib import Path
# R0=X^2(X-6)=X^3-6X^2. For a=s*a1, third residue is A(a1)=R0*a1'-R0'*a1.
# A(X^j)=(j-3)X^(j+2)+6(2-j)X^(j+1).
# Target P=-27X^6-486X^5+3888X^4. Degree forces deg(a1)<=4.
# X^6 requires coefficient -27 on X^4, which forces X^5 coefficient +324,
# inconsistent with target -486. X^3 is resonant and contributes only -6X^4.
target={6:-27,5:-486,4:3888};forced_x4=-27;forced_x5=-12*forced_x4
assert forced_x5==324 and forced_x5!=target[5]
out={'schema':'marici.benincasa.cosmology-rees-third-residue-boundary-image.v1','problem':'decide whether tau third residue is removed by boundary corrections preserving the first two residues','bold_conjecture':'a boundary tangential correction a=s a1 matches the third residue','named_rivals':['boundary correction suffices','boundary image has a resonant coefficient obstruction','lower K-level constrained inputs are essential'],'risky_consequences':['the coefficient equations for a1 must be consistent','the forced X5 coefficient after matching X6 must equal -486'],'strongest_falsification_attempt':{'boundary_third_operator':'A(a)=R0 a prime-R0 prime a','monomial_action':'A(X^j)=(j-3)X^(j+2)+6(2-j)X^(j+1)','target':'-27X^6-486X^5+3888X^4','forced_a_X4':-27,'forced_target_X5':324,'actual_target_X5':-486,'exact_residual_X5':-810},'disposition':'boundary-only constrained corrections cannot match tau third residue','surviving_scope':'full nonmembership is not proved because lower K-level constrained inputs may enlarge the third-residue image','next_test':'derive the complete third-residue operator including lower inputs and solve its exact polynomial coefficient system','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_third_residue_boundary_image.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
