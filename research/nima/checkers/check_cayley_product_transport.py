"""Exact eight-fiber source algebra controls; no native admission inferred."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import hashlib

ROOT=Path(__file__).resolve().parents[1]
Z=(F(0),)*8
B=[tuple(F(i==j) for i in range(8)) for j in range(8)]
ONE=(F(1),)*8
weights=(1,1,1,1,1,2,2,7)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def scale(c,x): return tuple(c*a for a in x)
def mul(x,y): return tuple(a*b for a,b in zip(x,y))
def norm(x): return sum(w*a*a for w,a in zip(weights,x))
def transport(x,inverse=False):
    c,s=F(-7,25),F(24,25)
    if inverse: s=-s
    a,b=(x[1]-x[2])/2,(x[3]-x[4])/2
    A,Bb=c*a+s*b,-s*a+c*b
    result=list(x)
    result[1]+=A-a; result[2]-=A-a
    result[3]+=Bb-b; result[4]-=Bb-b
    return tuple(result)
def moved_product(x,y):
    return transport(mul(transport(x,True),transport(y,True)))
def generator(x):
    a,b=(x[1]-x[2])/2,(x[3]-x[4])/2
    return (F(0),2*b,-2*b,-2*a,2*a,F(0),F(0),F(0))
def main():
    out=ROOT/'results/cayley-product-transport.json'
    out.unlink(missing_ok=True)
    b1=add(B[1],scale(-1,B[2])); b2=add(B[3],scale(-1,B[4]))
    assert transport(ONE)==ONE and transport(B[0])==B[0]
    assert mul(b1,b2)==Z and mul(transport(b1),transport(b2))!=Z
    assert moved_product(transport(b1),transport(b2))==Z
    for x in B+[ONE,b1,b2]:
        assert transport(transport(x),True)==x
        assert norm(transport(x))==norm(x)
        assert moved_product(ONE,x)==x
    for x,y in product(B,repeat=2):
        assert moved_product(transport(x),transport(y))==transport(mul(x,y))
        assert moved_product(x,y)==moved_product(y,x)
        assert transport(moved_product(x,y),True)==mul(transport(x,True),transport(y,True))
        assert norm(transport(add(x,y)))==norm(add(x,y))
    for x,y,z in product(B,repeat=3):
        assert moved_product(moved_product(x,y),z)==moved_product(x,moved_product(y,z))
    # A derivation of Q^8 must kill every primitive idempotent. K does not.
    defects=[add(generator(mul(x,y)),scale(-1,add(mul(generator(x),y),mul(x,generator(y)))))
             for x,y in product(B,repeat=2)]
    assert any(v!=Z for v in defects)
    assert generator(B[1])!=Z
    # Conjugate-coordinate connection cancels motion of each transported vector.
    assert generator(transport(b1))==transport(generator(b1))
    result={
      'schema':'marici.nima.cayley-product-transport.v1',
      'classification':'fixed_pointwise_product_rejects_cayley_map_conjugated_product_accepts_only_a_transported_presentation',
      'checks':{'basis_sewing':64,'basis_associativity':512,'weighted_norm':'preserved','fixed_product_hostile':'rejected','generator_derivation_hostile':'rejected'},
      'scope':'Exact Q^8 model of the documented eight source fibers, retaining their counting weights. This is not an implementation of native admission, a selection of Clifford multiplication, or physical active evolution.',
      'input_sha256':{str(p.relative_to(ROOT.parent.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),ROOT.parent/'voevodsky/source-algebra-selection-boundary.md')}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
