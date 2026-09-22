"""Actual old-observer collision and minimal source-derived repairs.

Exact forgotten three-diamond slice. Distinguishes target identification
from complete reconstruction; no source archive is supplied to the decoder.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from math import prod
import runpy,json
ROOT=Path(__file__).resolve().parents[3]
g=runpy.run_path(str(ROOT/'research/voevodsky/checkers/check_diamond_cube_residual_retention.py'))
v=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_minimal_matched_retention.py'))
f=g['f'];basis=g['basis'];source=g['source'];mode=g['mode'];vacuum=g['vacuum']
manifest=json.loads((ROOT/'research/grothendieck/results/finite-cubic-observer.json').read_text())
old_shapes=[v['frozen'](r['shape']) for r in manifest['rows']]+list(v['other_shapes']())
assert all(sum(edge[3] for edge in shape[0])+sum(shape[1])==2 for shape in old_shapes)
# On this full six-event, all-forgotten corner, cubic contexts must be
# identities and every old cubic seed requires two retained features.
# The unchanged old stages at lengths two and four cannot fit the input.
assert all(len(w)==6 and not any(m) for col in basis for w,m in col)
for col in basis:
    image=v['profile'](col)
    assert not any(sh in old_shapes for sh,windows in image)

# Both sources lie in I and have old readout zero and vacuum value one.
k=g['k']
x=mode(3) # (P-Q)(P-Q)P: in I^2 but not I^3
triple=g['selected_row'](7)
def reading(col,shape):return f['vacuum_rows'](0,63,col,len(shape)).get(shape,Fraction(0))
assert k!=x and not f['rho_column'](0,k) and not f['rho_column'](0,x)
assert reading(k,vacuum)==reading(x,vacuum)==1
assert reading(k,triple)==-1 and reading(x,triple)==0
assert not f['vacuum_rows'](0,63,x,1) and f['vacuum_rows'](0,63,x,2)
assert not f['vacuum_rows'](0,63,k,2)
# A certified I^3 prior changes identifiability: on every minimal forgotten
# cubic product, the reversed and canonical readings are negatives.
pure_cubic_checks=0
for pairs in f['pairings'](tuple(range(6))):
    col={ ((),()):Fraction(1) }
    for pair in pairs:col=f['multiply'](col,f['relation'](pair,0))
    assert reading(col,triple)==-reading(col,vacuum)
    pure_cubic_checks+=1
assert pure_cubic_checks==90

def vector(shape):return tuple(reading(col,shape) for col in basis)
def restrict_I(row):return tuple(row[j]-row[0] for j in range(1,8))
def rank(rows):return f['rank']([{j:c for j,c in enumerate(row) if c} for row in rows])
def spans(rows,target):return rank(rows+[target])==rank(rows)
V=vector(vacuum);T=vector(triple);VI=restrict_I(V);TI=restrict_I(T)
assert not spans([VI],TI) and rank([VI,TI])==2
# All distinct primitive order-two row restrictions, not merely the
# handpicked moment rows. Duplicate seam representations are removed.
shapes=sorted(set().union(*(set(col) for col in g['records'][2])))
unique={}
for sh in shapes:unique.setdefault(vector(sh),sh)
candidates=list(unique.items())
assert len(candidates)==18
# All primitive order-one signatures already occur among these order-two
# signatures on the fixed cube; order zero vanishes on I.
first_shapes=set().union(*(set(col) for col in g['records'][1]))
assert all(vector(sh) in unique for sh in first_shapes)
rejected_subsets=0
for size in (0,1,2):
    for chosen in combinations(candidates,size):
        assert not spans([VI]+[restrict_I(row) for row,sh in chosen],TI)
        rejected_subsets+=1
# Three primitive order-two rows along 000--001--011--111.
# R1=a000+a001; R2=a001+a011; R3=a011+a111.
r1=(('e',3,7,0),('e',15,31,0))
r2=(('e',0,2,0),('e',15,31,0))
r3=(('e',0,2,0),('e',3,11,0))
R1,R2,R3=map(vector,(r1,r2,r3))
assert tuple(R1[i]-R2[i]+R3[i]-V[i] for i in range(8))==T
assert spans([VI]+[restrict_I(r) for r in (R1,R2,R3)],TI)
# Thus one NEW cubic primitive row suffices, or three lower-order primitive
# rows; their one signed aggregate is not one primitive acquisition.

# Complete source reconstruction needs seven independent readings on I.
# With V and T already available, choose five actual lower-order rows.
chosen_shapes=[vacuum,triple];matrix=[VI,TI]
for row,sh in candidates:
    candidate=restrict_I(row)
    if rank(matrix+[candidate])>len(matrix):
        matrix.append(candidate);chosen_shapes.append(sh)
    if len(matrix)==7:break
assert len(matrix)==7 and rank(matrix)==7

def invert(matrix):
    n=len(matrix)
    a=[[Fraction(c) for c in row]+[Fraction(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        scalar=a[j][j];a[j]=[x/scalar for x in a[j]]
        for i in range(n):
            if i!=j:
                scalar=a[i][j];a[i]=[x-scalar*y for x,y in zip(a[i],a[j])]
    assert all(a[i][j]==int(i==j) for i in range(n) for j in range(n))
    return [row[n:] for row in a]
inv=invert(matrix)

def decode(values):
    if len(values)!=7:raise ValueError('seven labelled readings required')
    values=list(map(Fraction,values))
    coefficients=[sum((a*b for a,b in zip(row,values)),Fraction(0)) for row in inv]
    return source([-sum(coefficients)]+coefficients)

samples=[mode(t) for t in range(1,8)]+[k,x]
# One nontrivial rational combination of the full ideal basis.
a=[Fraction(i,2*i+1) for i in range(1,8)]
samples.append(source([-sum(a)]+a))
for col in samples:
    values=json.loads(json.dumps([str(reading(col,sh)) for sh in chosen_shapes]))
    assert decode(values)==col
    assert reading(col,triple)==reading(col,r1)-reading(col,r2)+reading(col,r3)-reading(col,vacuum)

primes=(2,3,5,7,11,13)
def vertex(mask):return 2*prod(p for i,p in enumerate(primes) if mask&(1<<i))
def describe(shape):
    return {'mask_seams':shape,'arithmetic_seams':[[vertex(a),vertex(b),'forgotten'] for _,a,b,mark in shape],
            'outer_corner':[2,60060],'buffers':'vacuum'}
def terms(col):
    return [{'event_primes':[primes[i] for i in w],'marks':list(m),'coefficient':str(c)} for (w,m),c in sorted(col.items())]
report={'passed':True,'source_domain':'I intersect the fixed eight-path forgotten three-diamond cube',
 'target_definition':'coefficient of H1 H2 H3 in the specified P/H cube basis, H=Q-P; not a canonical splitting of the full filtered source',
 'ambiguous_pair':{'pure_cubic':terms(k),'lower_order_source':terms(x),
                   'old_observations':[0,0],'vacuum_readings':[1,1],
                   'triple_interaction_coefficients':[-1,0],'pure_cubic_basis_coefficients':[1,0],
                   'source_ideal_orders':[3,2]},
 'certified_I3_prior':{'extra_readings_required_for_target':0,
   'identity':'reversed vacuum = -canonical vacuum on I^3 at the minimal six-event corner',
   'all_forgotten_minimal_cubic_products_checked':pure_cubic_checks},
 'new_direct_target_row':describe(triple),
 'minimal_additional_primitive_rows_for_target_with_cubic_rows_allowed':1,
 'minimal_additional_primitive_rows_for_target_with_order_at_most_two':3,
 'distinct_lower_order_row_vectors':len(candidates),'insufficient_lower_row_subsets_checked':rejected_subsets,
 'three_lower_rows':[describe(sh) for sh in (r1,r2,r3)],
 'target_reconstruction':'m123 = R1 - R2 + R3 - existing_vacuum',
 'remaining_source_ambiguity_dimension_after_direct_target_row':5,
 'complete_reconstruction':{'source_dimension':7,'rows':[describe(sh) for sh in chosen_shapes],
   'extra_rows_beyond_existing_vacuum':6,'matrix_on_basis_path_b_minus_path_0':[[str(c) for c in row] for row in matrix],
   'inverse_matrix':[[str(c) for c in row] for row in inv],
   'source_archive_required':False,'serialized_test_sources':len(samples)},
 'scope':'Exact finite source and unit-vacuum readings. New rows require acquisition or source-dependent justification; not derivable from the old retained values. Full reconstruction assumes the declared seven-dimensional source domain. Not a global observer equivalence or a physical noise certificate.'}
(ROOT/'research/voevodsky/results/vacuum-coefficient-identifiability.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('ambiguous_pair','complete_reconstruction')},indent=2))
