"""Seven-event balancing with source-enumerated relative Green collisions."""
from pathlib import Path
from itertools import product
from functools import lru_cache
import runpy
import json
ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))
rel,mul,D,raw,balanced=(b[k] for k in ('relation','multiply','derivative','raw_joint','balanced'))

# An exact non-diagonal signed feature fixture. Not an actual Clark Gram.
def G(i,j):return i*j + ((-1)**i if i==j else 0)

def fine_shape(key):
    cuts,*edges=key
    return (cuts,)+tuple((x,y,len(u),keep,len(v)) for x,y,u,keep,v in edges)

@lru_cache(None)
def normalize(key):
    values=balanced({key:1})
    assert len(values)==1
    return next(iter(values))

def kernel(a,b):
    seams,words=a;seams2,words2=b
    if seams!=seams2 or tuple(map(len,words))!=tuple(map(len,words2)):return 0
    value=1
    for (_,x,y,keep) in seams:
        if keep:
            value*=G(y,y)-(G(x,y)+G(y,x)-G(x,x) if x else 0)
    for word,other in zip(words,words2):
        for i,j in zip(word,other):value*=G(i,j)
    return value

def normal_shape(key):
    seams,words=key
    return seams,tuple(map(len,words))

def buckets(column,raw_input=False):
    out={}
    for key,c in column.items():
        normal=normalize(key) if raw_input else key
        shape=fine_shape(key) if raw_input else None
        out.setdefault(normal_shape(normal),[]).append((normal,shape,c))
    return out

def pair_normal(a,b):
    aa,bb=buckets(a),buckets(b)
    return sum(c*d*kernel(k,l) for shape,entries in aa.items()
               for k,_,c in entries for l,_,d in bb.get(shape,()))

def pair_parts(a,b):
    original=collision=0
    aa,bb=buckets(a,True),buckets(b,True)
    for shape,entries in aa.items():
        for k,fk,c in entries:
            for l,fl,d in bb.get(shape,()):
                value=c*d*kernel(k,l)
                if fk==fl:original+=value
                else:collision+=value
    return original,collision

blocks=((0,1),(3,4),(5,6));e=2
checks=pair_checks=nonzero_collisions=0
for kinds in product((0,1),repeat=3):
    for mark in (0,1):
        a,c,d=[rel(pair,kind) for pair,kind in zip(blocks,kinds)]
        arrow={((e,),(mark,)):1}
        m2=sum(1<<j for j in blocks[0]);m3=m2|(1<<e)
        m4=m2|sum(1<<j for j in blocks[1]);m5=m4|(1<<e)
        cases=(
          ((m3,m5),(D(0,mul(a,arrow)),D(m3,c),D(m5,d)),
           (m2,m5),(D(0,a),D(m2,mul(arrow,c)),D(m5,d))),
          ((m2,m4),(D(0,a),D(m2,c),D(m4,mul(arrow,d))),
           (m2,m5),(D(0,a),D(m2,mul(c,arrow)),D(m5,d))))
        for cuts_l,dl,cuts_r,dr in cases:
            left,right=raw(cuts_l,dl),raw(cuts_r,dr)
            common=balanced(left)
            assert common==balanced(right) and common
            target=pair_normal(common,common)
            corrected=[]
            for u,v in ((left,left),(left,right),(right,left),(right,right)):
                original,collision=pair_parts(u,v)
                assert original+collision==target
                corrected.append(original+collision)
                nonzero_collisions+=bool(collision)
                pair_checks+=1
            # The balancing difference is radical for the corrected pullback.
            assert corrected[0]-corrected[1]==0
            assert corrected[2]-corrected[3]==0
            # Relative correction is necessary, not a descended raw form.
            assert pair_parts(left,right)[0]==0
            checks+=1
assert checks==32
result={'passed':True,'balancing_moves':checks,'relative_pairing_checks':pair_checks,
 'nonzero_collision_fixtures':nonzero_collisions,
 'checks':{'corrected_pairing_agrees_with_balanced_normal_form':True,
 'balancing_differences_annihilated_by_corrected_pairing':True,
 'raw_cross_cut_pairing_zero_before_correction':True},
 'scope':'Exact non-diagonal feature fixtures for all 32 seven-event moves. General cross-spectral transfer uses source-current sewing and coefficientwise faithful balanced normal forms, not this fixture Gram.'}
out=ROOT/'research/voevodsky/results/balanced-relative-green-descent.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
