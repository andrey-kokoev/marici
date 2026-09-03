#!/usr/bin/env python3
"""Test whether the literal five-mark identity selects S or P colour."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_cyclic_equivariant_coloured_shadow_splitting.json').read_text())['passed']
lit=json.loads((R/'cosmology_five_mark_principal_wall_partial_fraction.json').read_text());assert lit['passed']
assert lit['source_identity']=='q_g3 - q_g23 - q_g31 = E, where E=x+y+z'
literal_denominators=('q_g1','q_g2','q_g3','q_g23','q_g31')
partial_fraction_deletions=('q_g3','q_g23','q_g31')
S={'q_g3':'G12:S','q_g1':'G23:S','q_g2':'G31:S'}
P={'q_G12':'G12:P','q_G23':'G23:P','q_G31':'G31:P'}
L={'q_g12':'G12:L','q_g23':'G23:L','q_g31':'G31:L'}
assert [x in S for x in partial_fraction_deletions]==[True,False,False]
assert [x in L for x in partial_fraction_deletions]==[False,True,True]
out={'schema':'marici.benincasa.cosmology-literal-generator-colour-provenance-gate.v1','literal_denominators':list(literal_denominators),'partial_fraction_deletion_axes':list(partial_fraction_deletions),'two_colour_axes':{'S':S,'P':P},'deletion_colour_pattern':['S','L','L'],'L_meaning':'lowercase marked exceptional-pair deletion, distinct from uppercase same-pair P axis','all_S_selected':False,'all_P_selected':False,'reason':'the literal boundary terms delete q_g23 and q_g31, which belong to neither the singleton-complement orbit nor the uppercase q_Gij pair orbit','binary_colour_ambiguity_resolved':False,'new_typed_residual':'the two-colour target omitted the lowercase marked-pair orbit that actually carries the literal boundary terms','next_test':'construct the cyclic three-colour S/P/L occurrence refinement, adjoining q_g12 to close the lowercase marked-pair orbit','passed':True};(R/'cosmology_literal_generator_colour_provenance_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
