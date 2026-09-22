"""Compare scalar-only and independently retained matched detector inputs.

Match the actual finite receiver manifest to the owning analytical shapes.
No assertion is made that the API archives its input or that measurements
have actually been performed.
"""
from pathlib import Path
from itertools import permutations,product
from fractions import Fraction
import runpy,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
g=runpy.run_path(str(ROOT/'research/voevodsky/checkers/check_background_two_vacuum_increment_exact.py'))
assert g['result']['passed']
manifest_path=ROOT/'research/grothendieck/results/finite-cubic-observer.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
def frozen(x):return tuple(frozen(y) for y in x) if isinstance(x,list) else x
actual={frozen(row['shape']):(row['sign'],row['coefficient']) for row in manifest['rows']}
assert len(actual)==len(manifest['rows'])==449
assert set(actual)==set(g['J'])|{g['reserve']}
assert all(actual[shape]==(sign,'crossed') for shape,sign in g['J'].items())
assert actual[g['reserve']][1]=='positive'
for numerator,denominator in manifest['coefficients_per_w_squared'].values():assert Fraction(numerator)/Fraction(denominator)!=0
# A specific input block, with one retained seam and one retained buffer
# window, detects the canonical four-event vacuum coefficient individually.
shape=((('e',0,1,1),('e',7,15,0),('e',15,31,0)),(0,1,0,0))
assert shape in actual
row_index=next(i for i,row in enumerate(manifest['rows']) if frozen(row['shape'])==shape)
windows=((0,1),(1,3))
raw3=g['raw3'];f=g['f']
for end in (5,6):
    for word in permutations(range(2,end)):
        full={( (0,1)+word+tuple(range(end,6)), (1,1)+(0,)*4 ):1}
        image=raw3(full)
        assert image.get((shape,windows),0)==int(word==tuple(range(2,end)))
# The source formerly invisible to the signed sum is now detected by this
# actual manifest row. It has canonical coefficient one.
h={((2,3,4,5),(0,)*4):1,((2,3,5,4),(0,)*4):1,((2,4,3,5),(0,)*4):-2}
full=f['multiply']({((0,1),(1,1)):1},h)
assert not g['detector_values'](full)
assert raw3(full).get((shape,windows),0)==1
# The other six witnesses already vanished block-by-block in every context.
D_scalar=[tuple(r['interval']) for r in g['remaining']]
D_raw=[p for p in D_scalar if p!=(2,6)]
assert len(D_raw)==6
for row in g['remaining']:
    if tuple(row['interval']) in D_raw:
        assert not row['nonzero_block_contexts'] and not row['lower_nonzero']
F2=[tuple(p) for p in g['depth_two']]
assert len(F2)==5 and set(F2).issubset(D_raw)
# Explicit ideal and prime-edge actions inherited from the vacuum module.
left=[];right=[]
for k in range(6):
    lm=[(p,(k,p[1])) for p in D_raw if p[0]==k+1]
    rm=[(p,(p[0],k+1)) for p in D_raw if p[1]==k]
    assert all(q in D_raw for p,q in lm+rm)
    left.append({'edge_index':k,'maps':lm});right.append({'edge_index':k,'maps':rm})
ID={(i-2,j) for i,j in D_raw if i>=2};DI={(i,j+2) for i,j in D_raw if j<=4}
assert not ID and DI=={(0,5),(0,6)}
# D_scalar/D_raw is the one-dimensional (2,6) corner, at filtration level
# one only. Its forced lift has a nonzero left action into D_raw.
assert (2,6) in D_scalar and (2,6) not in F2
assert (1,6) in D_raw
# Acquisition nonsplitting persists: the raw two-feature rows still kill k2.
k=f['chain_product']([f['relation']((2*j,2*j+1),0) for j in range(3)])
image=raw3(k)
assert not any(sh in actual for sh,windows in image)
assert image.get((((('e',0,1,0),('e',3,7,0),('e',15,31,0)),(0,0,0,0)),()),0)==1
result={'passed':True,'receiver_manifest_sha256':hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
 'receiver_input_rows':449,'matched_manifest_shapes_and_signs':True,
 'distinguishing_manifest_row_index_zero_based':row_index,'distinguishing_shape':shape,
 'source_witness_raw_value_coefficient':'1','source_witness_combined_value':'0',
 'raw_increment_dimension':6,'raw_inherited_filtration_dimensions':[6,5,1,0],
 'raw_increment_basis_intervals':D_raw,'depth_two_intervals':F2,
 'left_edge_actions':left,'right_edge_actions':right,
 'intrinsic_left_ideal_image':sorted(ID),'intrinsic_right_ideal_image':sorted(DI),
 'scalar_increment_dimension':7,'removed_increment_corner':[12,60060],
 'removed_increment_filtration_level':1,
 'checks':{'raw_acquisition_still_nonsplit':True,
   'quotient_of_scalar_increment_by_raw_increment_nonsplit':True},
 'scope':'Conditional on independently retaining the manifest joint readings and saturations. The evaluator consumes these readings but returns an aggregate; archival policy and actual acquisition are not certified here. Actual nonzero window responses use the owning finite-filter positivity proof.'}
(ROOT/'research/voevodsky/results/raw-matched-readings-vacuum-increment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
