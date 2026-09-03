#!/usr/bin/env python3
"""Classify C3-equivariant integral splittings of the colour-forgetful map."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_two_colour_occurrence_refinement.json').read_text())['passed']
# A C3-equivariant 3x3 block is circulant, determined by its first column a.
# A splitting is (A,I-A). Classify minimum column l1 norm in a bounded domain;
# the triangle inequality proves this minimum globally.
records=[]
for a in itertools.product(range(-3,4),repeat=3):
 b=(1-a[0],-a[1],-a[2]);norm=sum(map(abs,a))+sum(map(abs,b));records.append((norm,a,b))
mn=min(x[0] for x in records);mins=[x for x in records if x[0]==mn]
assert mn==1 and {(x[1],x[2]) for x in mins}=={((0,0,0),(1,0,0)),((1,0,0),(0,0,0))}
shadow=(0,-1,1)
S=(0,0,-1,0,1,0);P=(0,0,0,-1,0,1)
out={'schema':'marici.benincasa.cosmology-cyclic-equivariant-coloured-shadow-splitting.v1','classification':'all C3-equivariant integral splittings are (A,I-A) with A an integral circulant matrix','parameter_lattice':'Z^3','minimum_column_l1':mn,'minimum_splitting_count':2,'minimum_splittings':[{'name':'all-P','A_first_column':[0,0,0],'shadow_lift':list(P)},{'name':'all-S','A_first_column':[1,0,0],'shadow_lift':list(S)}],'mixed_minimal_lifts_extend_equivariantly':False,'reason':'equivariance forces one colour rule around the full cyclic orbit; minimum norm forbids off-axis circulant terms','residual_ambiguity':'C2 choice between all-S and all-P','source_selected':False,'next_test':'inspect the literal joint generator denominator provenance to determine whether it selects singleton-complement or same-pair colour','passed':True};(R/'cosmology_cyclic_equivariant_coloured_shadow_splitting.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
