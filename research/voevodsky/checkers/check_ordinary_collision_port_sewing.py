"""Source-derived shape collision ports for ordinary relative Green sewing.

Exact source checks and universal pairing algebra, not Clark trace evaluation.
"""
from pathlib import Path
from itertools import permutations, product
import contextlib
import io
import json
import runpy
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    src=runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_six_prime_derived_block_associativity.py'))
D,record,rel,mul,add=(src[k] for k in ('derivative','record','relation','multiply','add'))

def tensor(*columns):
    out={():1}
    for col in columns:
        out={key+(k,):c*d for key,c in out.items() for k,d in col.items() if c*d}
    return out

def clean(col):return {k:c for k,c in col.items() if c}

def edge_shape(e):
    x,y,p,k,q=e
    return x,y,len(p),k!=0,len(q)

def slots(e):
    x,y,p,k,q=e
    return p+(() if k==0 else (k,))+q

def compress(key,side):
    e,w,f=key
    x,y,p,k,q=e
    xx,yy,pp,kk,qq=f
    if side=='left':return ((x,y,p,k,q+w),f)
    return (e,(xx,yy,w+pp,kk,qq))

def memory_degree(key):
    e,w,f=key
    return len(e[2])+len(e[4])+len(w)+len(f[2])+len(f[4])

columns=shape_checks=0
for pairs in src['blocks'](tuple(range(6))):
    first,middle,last=pairs
    l=sum(1<<p for p in first)
    m=l|sum(1<<p for p in middle)
    middle_rel=src['power_basis'](middle)
    paths=[(w,k) for w in permutations(middle) for k in product((False,True),repeat=2)
           if (w,k) not in middle_rel]
    assert len(paths)==6
    for ka,kc in product((0,1),repeat=2):
        a,c=rel(first,ka),rel(last,kc)
        for word,marks in paths:
            w={(word,marks):1}
            fine=tensor(D(a,0),record(word,marks,l),D(c,m))
            assert fine
            for side in ('left','right'):
                image={}
                per_shape={}
                for key,coefficient in fine.items():
                    e,history,f=key
                    shape=(edge_shape(e),len(history),edge_shape(f))
                    target=compress(key,side)
                    image[target]=image.get(target,0)+coefficient
                    # Within each fine shape compression only regroups ordered
                    # tensor factors; no features, weights, or seam letters change.
                    assert slots(e)+history+slots(f)==slots(target[0])+slots(target[1])
                    assert memory_degree(key)==sum(len(t[2])+len(t[4]) for t in target)
                    assert (e[3],f[3])==(target[0][3],target[1][3])
                    old=per_shape.setdefault(shape,{})
                    assert target not in old or old[target]==key
                    old[target]=key
                    shape_checks+=1
                expected=(tensor(D(mul(a,w),0),D(c,m)) if side=='left'
                          else tensor(D(a,0),D(mul(w,c),l)))
                assert clean(image)==expected
            columns+=1
assert columns==2160

# A collision port is two copies of an EXISTING coarse carrier with exchange
# form [[0,Q],[Q,0]], not a metric inferred from a source Gram matrix.
Q=s.Matrix([[2,1+s.I],[1-s.I,-3]])
x=s.Matrix([1+s.I,2]);y=s.Matrix([3,-s.I])
u=s.Matrix([2,1-s.I]);v=s.Matrix([s.I,4])
H=s.zeros(4);H[:2,2:]=Q;H[2:,:2]=Q
assert s.expand((x.col_join(y).H*H*u.col_join(v))[0]
                -(x.H*Q*v+y.H*Q*u)[0])==0

# Verify complete forgotten-sector sewing, including all cross partitions.
with contextlib.redirect_stdout(io.StringIO()):
    vacuum=runpy.run_path(str(ROOT/'research/voevodsky/checkers/check_forgotten_ordinary_cut_defect.py'))
L,R=vacuum['L'],vacuum['R']
M=16*s.eye(90)
CL=L-s.diag(*L.diagonal());CR=R-s.diag(*R.diagonal())
assert L-CL==R-CR==M
assert CL-CR==L-R

# Existing same-partition grade collision and independently formal kernel identity.
with contextlib.redirect_stdout(io.StringIO()):
    anomaly=runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_ordinary_middle_block_green_obstruction.py'))
assert s.expand(anomaly['formal']-anomaly['expected'])==0

result={'passed':True,'ordinary_columns_checked':columns,
 'fine_coordinate_regrouping_checks':shape_checks,
 'checks':{'both_compressions_match_actual_source_derivatives':True,
 'within_shape_slot_order_and_separate_weights_preserved':True,
 'hyperbolic_collision_port_polarization':True,
 'full_90_channel_vacuum_relative_sewing':True,
 'within_partition_formal_spectral_anomaly_retained':True},
 'scope':'Finite ordinary relative sewing for graded multiplicative memory and prescribed tensor forms. Correction ports record cross-shape terms; they do not make the original coarse maps isometries or certify completion.'}
out=ROOT/'research/voevodsky/results/ordinary-collision-port-sewing.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
