"""Ordered two-seam derivative for the first filtered attachment."""
from pathlib import Path
from itertools import combinations,product
from collections import defaultdict
import runpy
import json
ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))
rel,mul,D,record=(b[k] for k in ('relation','multiply','derivative','record'))

def D2(start,col):
    out=defaultdict(int)
    for (word,marks),coef in col.items():
        states=[start]
        for p in word:states.append(states[-1]|(1<<p))
        for i,j in combinations(range(len(word)),2):
            buffers=(record(start,word[:i],marks[:i]),
                     record(states[i+1],word[i+1:j],marks[i+1:j]),
                     record(states[j+1],word[j+1:],marks[j+1:]))
            seams=(('e',states[i],states[i+1],marks[i]),
                   ('e',states[j],states[j+1],marks[j]))
            for entries in product(*(v.items() for v in buffers)):
                key=(seams,tuple(k for k,c in entries))
                value=coef
                for k,c in entries:value*=c
                out[key]+=value
    return {k:c for k,c in out.items() if c}

def joint(left,right):
    out=defaultdict(int)
    for (x,y,u,k,v),a in left.items():
        for (xx,yy,uu,kk,vv),c in right.items():
            out[(('e',x,y,k),('e',xx,yy,kk)),(u,v+uu,vv)]+=a*c
    return {k:c for k,c in out.items() if c}

product_checks=triple_checks=0
for ka,kc in product((0,1),repeat=2):
    a,c=rel((0,1),ka),rel((2,3),kc)
    ac=mul(a,c)
    image=D2(0,ac)
    assert image==joint(D(0,a),D(3,c)) and image
    assert not b['balanced_boundary'](image)
    assert not D(0,ac)
    product_checks+=1
    for kd in (0,1):
        triple=mul(ac,rel((4,5),kd))
        assert triple and not D2(0,triple)
        triple_checks+=1

# Nonminimal products: an extra event is moved across the factor interface.
nonminimal=0
for ka,kc,mark in product((0,1),repeat=3):
    a,c=rel((0,1),ka),rel((3,4),kc)
    e={((2,),(mark,)):1}
    left=joint(D(0,mul(a,e)),D(7,c))
    right=joint(D(0,a),D(3,mul(e,c)))
    assert left==right==D2(0,mul(mul(a,e),c)) and left
    assert not b['balanced_boundary'](left)
    nonminimal+=1

# Any source-equivariant homotopy H from the degree-zero middle term into
# the I-annihilated target would obey H(ac)=rho(a)H(c)=0, contradicting D2(ac).
witness=D2(0,mul(rel((0,1),0),rel((2,3),0)))
assert witness and any(coef==1 for coef in witness.values())
result={'passed':True,'product_derivative_comparisons':product_checks,
 'third_power_vanishings':triple_checks,'nonminimal_balanced_comparisons':nonminimal,
 'checks':{'single_derivative_kills_product':True,
 'two_seam_image_is_closed':True,'source_equivariant_nullhomotopy_obstructed':True},
 'scope':'Exact source derivative fixtures. Bounded extension and quasi-isomorphic-roof interpretation are proved in the companion note; no topological projectivity claim.'}
out=ROOT/'research/voevodsky/results/completed-filtered-attachment-map.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
