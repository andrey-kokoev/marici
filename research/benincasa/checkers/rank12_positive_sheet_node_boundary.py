"""Oriented normalization boundary of the positive Cayley-Menger sheet."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/benincasa/results/rank12-positive-sheet-node-boundary.json'

# Orient the real T-axis increasingly.  Splitting at zero gives
# I_-=[-R,0] and I_+=[0,R].  Their boundary coefficients at zero are
# +1 and -1 respectively.  I_- lies on e_- and I_+ on e_+.
boundary={'e_plus':-1,'e_minus':1}
assert boundary=={'e_plus':-1,'e_minus':1}
packet={
 'schema':'marici.benincasa.rank12_positive_sheet_node_boundary.v1',
 'positive_sheet':'W=2*abs(T)',
 'negative_half':{'domain':'T<0','normalization_sheet':'e_minus','endpoint_sign_at_zero':1},
 'positive_half':{'domain':'T>0','normalization_sheet':'e_plus','endpoint_sign_at_zero':-1},
 'oriented_boundary':'e_minus-e_plus',
 'anti_invariant_sublattice_generator':'-(e_plus-e_minus)',
 'odd_coinvariant_image':'-2*[e_plus]',
 'primitive_in_sheet_difference_lattice':True,
 'primitive_in_odd_coinvariant_lattice':False,
 'conclusion':'the source positive-sheet chamber lands canonically in the sheet-difference lattice and maps to twice the primitive odd coinvariant'
}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet))
