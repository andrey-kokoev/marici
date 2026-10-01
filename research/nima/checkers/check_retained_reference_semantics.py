"""Distinguish reference marking/slot masking from carrier-edge deletion.

Local marked primitive arrows model the eleven-leg selection. The separate
matrix assembly supplies its direct A->B reference explicitly. No adapter
identifying those local marks with that direct channel is assumed here.
"""
from copy import deepcopy
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import runpy
from biclique_complex import analyze, dowker


class MarkedCarrier:
    def __init__(self):
        self.records={edge:F(1) for edge in product(range(4),repeat=2) if edge[0]!=edge[1]}
        self.reference=(0,1)
        self.versions={edge:0 for edge in self.records}

    def counted(self): return tuple(edge for edge in self.records if edge!=self.reference)

    def edit(self, edge, value, expected_version, *, reference_edit=False):
        if edge not in self.records or self.versions[edge]!=expected_version:
            return False
        if edge==self.reference and reference_edit is not True:
            return False
        value=F(value)
        self.records[edge]=value
        self.versions[edge]+=1
        return True


def betti(relation):
    dimensions,differentials=dowker(relation)
    _,homology=analyze(dimensions,differentials)
    return {d:n for d,n in homology.items() if n}


left=MarkedCarrier(); right=MarkedCarrier()
assert len(left.records)==12 and len(left.counted())==11
assert betti(list(left.records))=={0:1,2:1}
assert betti(list(left.counted()))=={0:1}
assert left.reference in left.records
# The full relation is retained; only the countable/readout domain is masked.
full_pairs=set(product(left.records,right.records))
counted_pairs=set(product(left.counted(),right.counted()))
reference_touching=full_pairs-counted_pairs
assert len(full_pairs)==144 and len(counted_pairs)==121 and len(reference_touching)==23
assert full_pairs==counted_pairs|reference_touching
states=set(product(range(4),repeat=2))
assert len(counted_pairs)+len(states)==137
assert len(full_pairs)+len(states)==160
assert all(a==left.reference or b==right.reference for a,b in reference_touching)
# Marking another edge changes selection, leaving relation data/topology intact.
original=dict(left.records)
left.reference=(2,3)
assert left.records==original and betti(list(left.records))=={0:1,2:1}
assert len(left.counted())==11
left.reference=(0,1)
# Reference-fixing is an edit policy, separate from membership deletion.
before=deepcopy(left.__dict__)
assert not left.edit(left.reference,2,0)
assert left.__dict__==before
assert left.edit(left.reference,2,0,reference_edit=True)
assert left.reference in left.records and len(left.counted())==11
assert not left.edit(left.reference,3,0,reference_edit=True)
assert left.edit((1,0),3,0)
assert betti(list(left.records))=={0:1,2:1}

# Reuse the previously admitted direct-reference assembly, including its
# explicit direct-channel perturbation. Its counted slots stay137 throughout.
assembly=runpy.run_path(str(Path(__file__).with_name('check_comparison_slot_reference_assembly.py')))
I,H=assembly['I'],assembly['H']
add,scale,assemble=assembly['add'],assembly['scale'],assembly['assemble']
comparison=assemble([I]*11,[I]*11,[I]*4,[I]*4)
reference=I
assert add(comparison,scale(-1,reference))==assembly['ZERO']
assert add(comparison,scale(-1,add(reference,H)))==scale(-1,H)
print('Retained carrier: 12 edges, primitive b2=1; counted primitive view: 11 edges, b2=0.')
print('Full pair relation: 144 arrows; mask selects121 and excludes23 reference-touching pairs; with16 states the count is137.')
print('Changing the reference mark preserves all carrier records; pinned/default and explicit reference edits have separate checks.')
print('The existing direct-reference assembly changes residual by -H under reference-only change, with137 slots unchanged.')
print('Local marked-edge selection and the direct A->B reference remain distinct typed roles pending a carrier adapter.')
