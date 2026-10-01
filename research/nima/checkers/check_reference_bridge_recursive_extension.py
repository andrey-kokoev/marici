"""Recursive DG path closure using an explicitly invertible direct reference.

Adjoin r:B->A with r=d^-1, delta(r)=0 and strict inverse reductions. This
extends the shared-leg graph without identifying endpoint types or adding
independent copies. Invertibility is a new, checked sector assumption.
"""
from pathlib import Path
import runpy
from fractions import Fraction as F

m=runpy.run_path(str(Path(__file__).with_name('check_shared_leg_dg_realization.py')))
plus,minus,word=m['plus'],m['minus'],m['word']
add,scale,mul=m['add'],m['scale'],m['mul']
I,Z,H=m['I'],m['Z'],m['H']
arrows,old_delta,bases,rectangles,routes=m['build']({'a':(0,0),'s':(0,0)})
boundaries={a:old_delta(word(a)) for a in arrows}
arrows=dict(arrows); arrows['return']=('B','A',0); boundaries['return']={}


def degree(path): return sum(arrows[a][2] for a in path)
def signature(path):
    assert path and all(arrows[a][1]==arrows[b][0] for a,b in zip(path,path[1:]))
    return arrows[path[0]][0],arrows[path[-1]][1],degree(path)


def normal(path):
    signature(path)
    result=[]
    for a in path:
        if result and (result[-1],a) in (('d','return'),('return','d')): result.pop()
        else: result.append(a)
    # All chains used below have external type A->B, so reduction cannot be empty.
    assert result and signature(tuple(result))==signature(path)
    return tuple(result)


def canonical(chain):
    result={}
    for path,c in chain.items():
        p=normal(path); result[p]=result.get(p,F(0))+c
        if not result[p]: del result[p]
    return result


def delta(chain):
    result={}
    for path,c in chain.items():
        signature(path)
        for i,a in enumerate(path):
            for replacement,b in boundaries[a].items():
                result=plus(result,{path[:i]+replacement+path[i+1:]:c*b*((-1)**degree(path[i+1:]))})
    return canonical(result)


def star(left,right):
    result={}
    for p,c in left.items():
        assert signature(p)[:2]==('A','B')
        for q,b in right.items():
            assert signature(q)[:2]==('A','B')
            result=plus(result,{p+('return',)+q:c*b})
    return canonical(result)


def inverse(matrix):
    a,b=matrix[0]; c,d=matrix[1]; det=a*d-b*c
    if not det: raise ValueError('reference must be invertible; no partial inverse substituted')
    return ((d/det,-b/det),(-c/det,a/det))


values=dict(m['values']); values['return']=inverse(values['d'])
assert mul(values['return'],values['d'])==mul(values['d'],values['return'])==I
assigned=dict(values)
for a,(_,_,k) in arrows.items():
    if k==1: assigned[a]=m['evaluate'](boundaries[a],values)
def evaluate(chain): return m['evaluate'](chain,assigned)
reference=word('d')
C=word('ax1','ay1'); h=routes('a',1,1)[0]
assert delta(h)==plus(C,minus(reference))
assert star(reference,C)==star(C,reference)==C

# One record-composition rule used twice, with the same retained reference.
for _ in range(2):
    new_C=star(C,C)
    first=plus(star(C,h),h)
    second=plus(star(h,C),h)
    higher=star(h,h)
    assert delta(first)==delta(second)==plus(new_C,minus(reference))
    assert delta(higher)==plus(second,minus(first))
    rho=add(evaluate(C),scale(-1,values['d']))
    expected=add(add(rho,rho),mul(mul(rho,values['return']),rho))
    assert evaluate(first)==expected
    C,h=new_C,first

# The same bridge also supports a genuine cube from three existing witnesses.
witnesses=[routes('a',1,1)[0],routes('s',1,1)[0],routes('a',2,2)[0]]
cube=star(star(witnesses[0],witnesses[1]),witnesses[2])
assert all(degree(p)==3 for p in cube)
assert delta(cube) and not delta(delta(cube))
assert evaluate(cube)!=Z
# Associativity holds on retained formal paths, without commuting matrices.
assert star(star(*witnesses[:2]),witnesses[2])==star(witnesses[0],star(*witnesses[1:]))

# Apply one higher-product rule twice to the original local rectangle witness.
local=word('ah1','ak1')
levels=[local]
for _ in range(2): levels.append(star(levels[-1],levels[-1]))
assert [next(iter({degree(p) for p in chain})) for chain in levels]==[2,4,8]
for chain in levels:
    assert delta(chain) and not delta(delta(chain))
    assert evaluate(chain)!=Z
# Eight witness occurrences still depend on only the same two witness labels.
assert {a for p in levels[-1] for a in p if arrows[a][2]}=={'ah1','ak1'}
assert len(next(iter(levels[-1])))==11  # eight witnesses and three return bridges
# Graded Leibniz rule for the bridge product.
for left,right in ((local,local),(witnesses[0],local),(local,witnesses[1])):
    k=next(iter({degree(p) for p in right}))
    expected=plus(star(left,delta(right)),{p:((-1)**k)*c for p,c in star(delta(left),right).items()})
    assert delta(star(left,right))==expected
# Both composition orders are now typed; their discrepancy is a reference-
# transported commutator of residuals, with the affine terms cancelling.
a=word('ax1','ay0'); b=word('ax0','ay1')
ra=plus(a,minus(reference)); rb=plus(b,minus(reference))
commutator=plus(star(a,b),minus(star(b,a)))
assert commutator==plus(star(ra,rb),minus(star(rb,ra)))
assert evaluate(commutator)!=Z
# Zero leg variation kills this entire repeated local-witness branch.
zeroed=dict(assigned); zeroed['ah1']=Z
assert all(m['evaluate'](chain,zeroed)==Z for chain in levels)
# Endpoint basis changes transport the bridge, rather than identifying objects.
g={'A':((F(2),F(0)),(F(0),F(1))),'U':I,'V':I,'B':add(I,H)}
transformed={a:mul(mul(g[t],value),inverse(g[s])) for a,value in assigned.items() for s,t,_ in [arrows[a]]}
for chain in levels+[cube]:
    assert m['evaluate'](chain,transformed)==mul(mul(g['B'],evaluate(chain)),inverse(g['A']))
try: inverse(((F(1),F(0)),(F(0),F(0))))
except ValueError: pass
else: raise AssertionError('singular reference admitted')
print('Reference bridge closes existing A->B records under C2*d^-1*C1; d is the exact unit and external types remain distinct.')
print('One record law passes two applications with rho_new=rho1+rho2+rho2*d^-1*rho1 and both higher comparison routes.')
print('A nonzero degree3 cube is available; repeating the same local higher-product rule gives degrees2,4,8.')
print('All graded boundaries square to zero; basis covariance and noncommutative associativity pass exactly.')
print('Degree8 reuses two witness labels; degree/occurrence doubling introduces no independent carrier copies.')
print('Reversing two bridge-compositions gives the typed residual commutator rho2*d^-1*rho1-rho1*d^-1*rho2; a nonzero example passes.')
print('Singular reference rejected. Strict invertibility is an added sector assumption; no metric or physical coupling is selected.')
