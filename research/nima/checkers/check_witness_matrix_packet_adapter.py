"""Keep finite comparison witnesses alongside the actual matrix responses.

The block encoding is an explicit data adapter, not a physical new field or a
claim that the supplied matrix amplitudes arise from finite permutations.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import io
import json
import runpy

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/witness-matrix-packet-adapter.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    m=runpy.run_path(str(Path(__file__).with_name('check_shared_leg_dg_realization.py')))
I,Z=m['I'],m['Z']; add,scale,mul=m['add'],m['scale'],m['mul']
d=m['values']['d']; r=scale(F(1,2),I)
unit=tuple(range(4)); H=tuple(g for g in permutations(unit) if g[0]==0)
def compose(b,a): return tuple(b[a[i]] for i in unit)
def inverse(a): return tuple(a.index(i) for i in unit)
def swap(i,j): return tuple(j if k==i else i if k==j else k for k in unit)

# Standard faithful S3 action on the sum-zero plane of the three unmarked
# coordinates, in basis e1-e3,e2-e3. The metric is recorded but not physical.
def rho(g):
    return tuple(tuple(F((g[j]==i)-(g[3]==i)) for j in (1,2)) for i in (1,2))
def transpose(a): return tuple(zip(*a))
metric=((F(2),F(1)),(F(1),F(2)))
assert len({rho(g) for g in H})==6
for a,b in product(H,repeat=2): assert rho(compose(b,a))==mul(rho(b),rho(a))
for a in H: assert mul(mul(transpose(rho(a)),metric),rho(a))==metric

def block(c,h):
    w=rho(h)
    return tuple(tuple(c[i][j] if i<2 and j<2 else
                       w[i-2][j-2] if i>=2 and j>=2 else F(0)
                       for j in range(4)) for i in range(4))
def mm(b,a):
    return tuple(tuple(sum((b[i][k]*a[k][j] for k in range(4)),F(0))
                       for j in range(4)) for i in range(4))
D=block(d,unit); R=block(r,unit)
assert mm(D,R)==block(I,unit)

# Give the four typed primitive objects distinct pointed-package values.
ports={'A':0,'U':1,'V':2,'B':3}
tau={i:unit if i==0 else swap(0,i) for i in unit}
def arrow_witness(source,target,h):
    g=compose(tau[ports[target]],compose(h,inverse(tau[ports[source]])))
    assert g[ports[source]]==ports[target]
    return g

packets=[]; witnesses=[]; matrices=[]
for tag,size,mid in (('a',11,'U'),('s',4,'V')):
    for i,j in product(range(size),repeat=2):
        # Declared admissible sample witnesses, not a source-selected assignment.
        hx,hy=H[i%6],H[(2*j+1)%6]
        x=m['values'][f'{tag}x{i}']; y=m['values'][f'{tag}y{j}']
        gx=arrow_witness('A',mid,hx); gy=arrow_witness(mid,'B',hy)
        h=compose(hy,hx); g=arrow_witness('A','B',h)
        assert compose(gy,gx)==g
        C=mul(y,x); packet=block(C,h)
        assert mm(block(y,hy),block(x,hx))==packet
        assert tuple(tuple(packet[a][b] for b in range(2)) for a in range(2))==C
        assert tuple(tuple(packet[a+2][b+2] for b in range(2)) for a in range(2))==rho(h)
        packets.append(packet); witnesses.append(h); matrices.append(C)
assert len(packets)==137

# Original source/target matrix blocks survive exactly, including every mixed
# rectangle. Added witness data does not change the original matrix readout.
for offset,size in ((0,11),(121,4)):
    for i,j in product(range(size),repeat=2):
        indexes=(offset+size*i+j,offset+size*i,offset+j,offset)
        def rectangle(values):
            a,b,c,e=(values[k] for k in indexes)
            return add(add(a,e),scale(-1,add(b,c)))
        decoded=[tuple(tuple(p[a][b] for b in range(2)) for a in range(2)) for p in packets]
        assert rectangle(decoded)==rectangle(matrices)

# Reference-bridged packet composition preserves both products. Include a zero
# matrix to ensure witnesses are not erased when the original readout vanishes.
for C1,C2 in ((matrices[0],matrices[12]),(Z,I)):
    for h1,h2 in product(H,repeat=2):
        assert mm(mm(block(C2,h2),R),block(C1,h1))==block(mul(mul(C2,r),C1),compose(h2,h1))
assert len({block(Z,h) for h in H})==6

# Obstruction to identifying the original readout with a functor from this
# finite groupoid: every normalized isotropy has sixth power identity. The
# original base slot is I relative to d=2I, so its normalized value is I/2.
base=m['values']['ay0']; assert mul(base,m['values']['ax0'])==I
normalized=mul(r,I); power=I
for _ in range(6): power=mul(power,normalized)
assert power==scale(F(1,64),I)!=I
for h in H:
    g=unit
    for _ in range(6): g=compose(h,g)
    assert g==unit

# Multiplying witness matrices into unrestricted response matrices is not an
# injective adapter; averaging the witness channel is not faithful either.
t=swap(1,2)
assert mul(I,rho(t))==mul(rho(t),I)  # distinct packets (I,t) and(rho(t),identity)
assert block(I,t)!=block(rho(t),unit)
average=Z
for h in H: average=add(average,scale(F(1,6),rho(h)))
assert average==Z
half=scale(F(1,2),add(I,rho(t)))
assert half[0][0]*half[1][1]-half[0][1]*half[1][0]==0

result={
 'status':'passed',
 'classification':'faithful_witness_response_packet_with_finite_functor_identification_obstruction',
 'obligation':'typed witness attachment and composition before readout',
 'stratum':'Actual137-slot shared-leg matrices plus supplied S3 witness coordinates and declared pointed-object frames; no physical coupling inferred',
 'checks':{'faithful_s3_matrix_representation':True,'typed_primitive_witness_composition':True,
           'slots':137,'original_matrices_and_rectangles_preserved':True,
           'bridge_composition_in_both_channels':True,'zero_response_witness_retention':True,
           'pure_finite_groupoid_matrix_identification_falsified':True,
           'witness_absorption_and_averaging_not_faithful':True},
 'unsupported':['physical assignment of the witness labels',
                'response amplitudes derived from finite equivalences',
                'physical meaning of block dimensions or representation metric',
                'DG witness realization or completed physical rung transport'],
 'next_constructor':'Supply a source operation for response amplitudes and their interaction with retained equivalence witnesses; the two channels cannot simply be identified.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
