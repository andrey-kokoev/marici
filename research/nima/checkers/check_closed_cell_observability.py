# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Exact observability of closed two-factor cells through the triangle view.

Find the missing linear directions and complete the view with retained source
cell coordinates. Coordinate selection is a labelled implementation choice.
"""
from pathlib import Path
from fractions import Fraction as F
import runpy
from biclique_complex import apply

model=runpy.run_path(str(Path(__file__).with_name('check_two_factor_weighted_chain_transport.py')))
B2=model['bd'][2]; B3=model['bd'][3]; Z=model['Z']; T=model['T2']
add=model['add']; dot=model['dot']


def admit(pivots,column):
    vector={i:F(v) for i,v in column.items() if v}
    while vector:
        p=min(vector)
        if p in pivots:
            vector=add(vector,pivots[p],-vector[p])
        else:
            a=vector[p]; pivots[p]={i:v/a for i,v in vector.items()}
            return True
    return False


def rows(columns,size):
    result=[{} for _ in range(size)]
    for j,column in enumerate(columns):
        for i,v in column.items(): result[i][j]=v
    return result


# Independent source closed-chain columns, retaining their original generators.
pivots={}; basis=[]
for column in B3:
    if admit(pivots,column): basis.append(column)
assert len(basis)==1037
for column in Z:
    assert admit(pivots,column)
    basis.append(column)
assert len(basis)==1039
assert all(not apply(B2,column) for column in basis)
images=[apply(T,column) for column in basis]
image_pivots={}
for column in images[:-2]: admit(image_pivots,column)
internal_visible=len(image_pivots)
for column in images[-2:]: assert admit(image_pivots,column)
visible=len(image_pivots); hidden=len(basis)-visible
assert (internal_visible,visible,hidden)==(277,279,760)
print(f'Closed state dimension1039; internal image rank={internal_visible}; full triangle-view rank={visible}; hidden closed directions={hidden}.',flush=True)

# Explicit fixed-context indistinguishable states even with total cost included.
zero_images=[column for column in B3 if not apply(T,column)]
assert zero_images
b=zero_images[0]
assert not apply(B2,b) and all(dot(z,b)==0 for z in Z)
negative={i:-v for i,v in b.items()}
assert b!=negative and apply(T,b)==apply(T,negative)=={}
assert 84*dot(b,b)==84*dot(negative,negative)>0

# Start with target-coordinate observations on the closed-chain basis, then
# greedily add individual retained source-cell readouts until they separate it.
observation_pivots={}
for row in rows(images,model['ddims'][2]): admit(observation_pivots,row)
assert len(observation_pivots)==visible
chosen=[]
for i,row in enumerate(rows(basis,len(B2))):
    if admit(observation_pivots,row): chosen.append(i)
assert len(observation_pivots)==1039
assert len(chosen)==hidden
# Full-rank observation matrix proves uniqueness on the entire closed space;
# each selected row increases rank, so deleting any one loses uniqueness.
assert any(b.get(i,F(0))!=negative.get(i,F(0)) for i in chosen)
# Constructive decode from actual observed values, carrying right-hand sides
# through exact row elimination. Test a state using every basis coordinate.
coefficients={j:F((j%11)-5,7) for j in range(len(basis))}
x=apply(basis,coefficients); y=apply(T,x)
target_rows=rows(images,model['ddims'][2]); source_rows=rows(basis,len(B2))
equations=[(row,y.get(i,F(0))) for i,row in enumerate(target_rows)]
equations += [(source_rows[i],x.get(i,F(0))) for i in chosen]
decoder={}
for row,value in equations:
    vector=dict(row)
    while vector:
        p=min(vector)
        if p in decoder:
            pivot_row,pivot_value=decoder[p]; factor=vector[p]
            vector=add(vector,pivot_row,-factor); value-=factor*pivot_value
        else:
            factor=vector[p]
            decoder[p]=({i:v/factor for i,v in vector.items()},value/factor)
            break
    else:
        assert value==0
recovered={}
for p in reversed(range(len(basis))):
    row,value=decoder[p]
    recovered[p]=value-sum((v*recovered[i] for i,v in row.items() if i!=p),F(0))
assert recovered==coefficients and apply(basis,recovered)==x
print('Exact decoder reconstructs a state using all1039 basis coordinates from the triangle view and760 extra readings.')
print(f'{len(zero_images)} local3-boundaries individually vanish in the triangle view.')
print(f'Explicit b and -b have identical class coordinates, triangle view and budget={84*dot(b,b)}, but distinct retained cells.')
print(f'Adding {len(chosen)} selected source-cell coordinates completes the view to rank1039, meeting the linear lower bound.')
print(f'First selected cell IDs: {chosen[:16]}')
print('The complete labelled cell state remains reconstructible; class/view/budget summaries alone are not injective.')
