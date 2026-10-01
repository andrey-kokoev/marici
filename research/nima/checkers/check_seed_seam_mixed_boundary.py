"""Actual seam path rectangle, using existing formal path-chain operations.
No numerical edge response or freely adjoined seed comparison witness.
"""
from fractions import Fraction as F
import check_seed_typed_execution as seed
from check_shared_leg_dg_realization import plus, minus, word

x0=('AB',); x1=('AD','DB')
y0=('BA',); y1=('BC','CA')
assert frozenset((x0,x1))==seed.forward
assert frozenset((y0,y1))==seed.returns

def endpoints(path):
    assert path and all(seed.registry[a][1]==seed.registry[b][0] for a,b in zip(path,path[1:]))
    return seed.registry[path[0]][0],seed.registry[path[-1]][1]

def product(after,before):
    # Same chronological word convention as the shared-leg DG checker.
    result={}
    for p,a in before.items():
        for q,b in after.items():
            assert endpoints(p)[1]==endpoints(q)[0]
            result=plus(result,{p+q:a*b})
    return result

C={(i,j):word(*(x+y)) for i,x in enumerate((x0,x1)) for j,y in enumerate((y0,y1))}
assert all(endpoints(p)==('A','A') for c in C.values() for p in c)
rectangle=plus(C[1,1],minus(C[1,0]),minus(C[0,1]),C[0,0])
factored=product(plus(word(*y1),minus(word(*y0))),
                 plus(word(*x1),minus(word(*x0))))
assert rectangle==factored
assert rectangle=={
    ('AD','DB','BC','CA'):F(1), ('AD','DB','BA'):F(-1),
    ('AB','BC','CA'):F(-1), ('AB','BA'):F(1)}
assert sum(rectangle.values())==0
# The mixed record is invisible to EVERY additive primitive-arrow readout,
# not only equal unit costs. Check all six basis coefficient readings.
for label in seed.registry:
    assert sum(c*p.count(label) for p,c in rectangle.items())==0
assert sum(c*len(p) for p,c in rectangle.items())==0
# Arbitrary independent forward/return leg offsets cancel as well.
for x in (x0,x1):
    assert sum(c for p,c in rectangle.items() if p[:len(x)]==x)==0
for y in (y0,y1):
    assert sum(c for p,c in rectangle.items() if p[-len(y):]==y)==0
# A full-word indicator separates the formal chain; it is only an information
# witness, not an independently admitted physical probe.
assert rectangle.get(x1+y1)==1
# Swapping the seam endpoints transports the four words to B-based loops.
def rename(path):
    return tuple(seed.edge_by_endpoints[(seed.swap[seed.registry[e][0]],
                                        seed.swap[seed.registry[e][1]])] for e in path)
moved={rename(p):c for p,c in rectangle.items()}
assert all(endpoints(p)==('B','B') for p in moved)
assert {rename(p):c for p,c in moved.items()}==rectangle
print('PASS: actual seed has a nonzero retained-word rectangle, factoring into the two leg differences.')
print('PASS: every additive edge cost and separate-leg offset annihilates that rectangle.')
print('PASS: seam reversal transports the entire boundary without selecting a preferred orientation.')
print('BOUNDARY: numerical mixed response and DG leg-comparison fillers are not supplied by endpoint incidence.')

# Reuse the bilinear mean/fluctuation identity on the actual typed path ports.
# X:A->B and Y:B->A; no reference inverse is needed for YX. Do NOT import
# X+Y or the same-Hom residual update, which would have mismatched types here.
def scaled(chain,c): return {p:c*v for p,v in chain.items() if c*v}
mean_x=scaled(plus(word(*x0),word(*x1)),F(1,2))
mean_y=scaled(plus(word(*y0),word(*y1)),F(1,2))
mean_product=product(mean_y,mean_x)
assert mean_product==scaled(plus(*C.values()),F(1,4))
# Equal marginals leave a full interval of joint laws. t is a free MODEL
# parameter here, not a physical coupling or a probability inferred from paths.
for t in (F(0),F(1,8),F(1,4),F(3,8),F(1,2)):
    weights={(0,0):t,(1,1):t,(0,1):F(1,2)-t,(1,0):F(1,2)-t}
    assert all(v>=0 for v in weights.values())
    assert all(sum(v for (i,j),v in weights.items() if i==k)==F(1,2) for k in (0,1))
    assert all(sum(v for (i,j),v in weights.items() if j==k)==F(1,2) for k in (0,1))
    joint=plus(*(scaled(C[key],weight) for key,weight in weights.items()))
    assert plus(joint,minus(mean_product))==scaled(rectangle,t-F(1,4))
# The supplied triangle records pick the OFF-diagonal corners as an incidence
# relation, unlike the full endpoint pullback. Equal weighting remains explicit.
original_triangles={('AB','BC','CA'),('AD','DB','BA')}
triangle_corners={key for key,chain in C.items() if next(iter(chain)) in original_triangles}
assert triangle_corners=={(0,1),(1,0)}
triangle_mean=scaled(plus(C[0,1],C[1,0]),F(1,2))
other_mean=scaled(plus(C[0,0],C[1,1]),F(1,2))
assert plus(triangle_mean,minus(mean_product))==scaled(rectangle,F(-1,4))
assert plus(other_mean,minus(mean_product))==scaled(rectangle,F(1,4))
assert plus(triangle_mean,minus(other_mean))==scaled(rectangle,F(-1,2))
print('PASS: bilinear covariance identity applies to the seam ports; independent all-pairs weighting gives zero correction.')
print('PASS: equal-weight supplied-triangle incidence gives -Delta/4 relative to product means; complementary cycles give +Delta/4.')
print('BOUNDARY: choosing original-triangle composition versus full path pairing is an operation choice, not inferred from retention alone.')
