"""Weak reference returns, fixed-reference composition and higher coherence.

Exact finite DG example with nonzero homology and singular homotopy-equivalent
reference. Unit witnesses, their edits and reference drift are kept explicitly.
"""
from dataclasses import dataclass
from fractions import Fraction as F

# One surviving degree-zero coordinate plus two contractible Q^2 pairs.
grades=(0,0,0,1,1,2,2,3,3)
spaces={'A':grades,'B':grades,'X':(0,1)}
diffs={'A':{(1,3):F(1),(2,4):F(1),(5,7):F(1),(6,8):F(1)}}
diffs['B']=dict(diffs['A']); diffs['X']={}


@dataclass(frozen=True)
class Map:
    source: str
    target: str
    degree: int
    entries: dict

    def __post_init__(self):
        assert all(v and spaces[self.target][i]-spaces[self.source][j]==self.degree
                   for (i,j),v in self.entries.items())


def identity(obj): return Map(obj,obj,0,{(i,i):F(1) for i in range(len(spaces[obj]))})
def zero(s,t,k): return Map(s,t,k,{})
def add(a,b,sign=1):
    assert (a.source,a.target,a.degree)==(b.source,b.target,b.degree)
    values=dict(a.entries)
    for key,value in b.entries.items():
        values[key]=values.get(key,F(0))+sign*value
        if not values[key]: del values[key]
    return Map(a.source,a.target,a.degree,values)


def mul(a,b):  # a after b
    assert b.target==a.source
    values={}
    for (i,k),x in a.entries.items():
        for (l,j),y in b.entries.items():
            if k==l: values[i,j]=values.get((i,j),F(0))+x*y
    return Map(b.source,a.target,a.degree+b.degree,{key:v for key,v in values.items() if v})


def prod(*maps):
    out=maps[0]
    for m in maps[1:]: out=mul(out,m)
    return out


def delta(a):
    da=Map(a.source,a.source,-1,diffs[a.source])
    db=Map(a.target,a.target,-1,diffs[a.target])
    return add(mul(db,a),mul(a,da),-((-1)**a.degree))


# d is identity on surviving homology, zero on the lower contractible pair,
# and twice identity on the upper pair. It is singular as a matrix.
d=Map('A','B',0,{(0,0):F(1),**{(i,i):F(2) for i in (5,6,7,8)}})
r=Map('B','A',0,identity('A').entries)
u_values={(3,1):F(-1),(4,2):F(-1),(7,5):F(1),(8,6):F(1),(5,3):F(1),(6,4):F(1)}
u=Map('A','A',1,u_values)
v=Map('B','B',1,dict(u_values))
assert not delta(d).entries and not delta(r).entries
p=add(mul(r,d),identity('A'),-1)
q=add(mul(d,r),identity('B'),-1)
assert delta(u)==p and delta(v)==q
assert len(d.entries)==5<9 and d.entries[0,0]==1
assert len(grades)-2*len(diffs['A'])==1  # one surviving homology direction

# Two unit witnesses can disagree on their triangle. An explicit closed-history
# edit makes a coherent triangle available, retaining the original v as a parent.
t=add(mul(d,u),mul(v,d),-1)
assert t.entries and not delta(t).entries
v_adjusted=add(v,mul(t,r))
triangle=mul(t,u)
assert delta(v_adjusted)==q
assert delta(triangle)==add(mul(d,u),mul(v_adjusted,d),-1)
assert triangle.entries

# The fixed-reference drift and its retained filler.
e=mul(d,u)
drift=add(prod(d,r,d),d,-1)
assert delta(e)==drift and drift.entries


@dataclass(frozen=True)
class Record:
    actual: Map
    witness: Map
    parents: tuple=()

    def __post_init__(self):
        assert not delta(self.actual).entries
        assert delta(self.witness)==add(self.actual,d,-1)


def combine(left,right):
    actual=prod(right.actual,r,left.actual)
    first=add(add(prod(right.witness,r,left.actual),prod(d,r,left.witness)),e)
    second=add(add(prod(right.actual,r,left.witness),prod(right.witness,r,d)),e)
    assert delta(first)==delta(second)==add(actual,d,-1)
    higher=prod(right.witness,r,left.witness)
    assert delta(higher)==add(second,first,-1)
    rho1=add(left.actual,d,-1); rho2=add(right.actual,d,-1)
    expected=add(add(add(drift,prod(d,r,rho1)),prod(rho2,r,d)),prod(rho2,r,rho1))
    assert add(actual,d,-1)==expected
    return Record(actual,first,(left,right))


# Exact agreement becomes agreement with a retained unit witness, not equality.
agree=Record(d,zero('A','B',1))
returned=combine(agree,agree)
assert returned.actual!=d and returned.witness==e
# Four distinct comparison records on the same Hom(A,B), no endpoint relabelling.
records=[]
for n in range(1,5):
    h=Map('A','B',1,{(3,2):F(n,3),(7,6):F(n,5),(5,3):F(n,7)})
    records.append(Record(add(d,delta(h)),h))
p1,p2,p3,p4=records
first_left=combine(p1,p2); first_right=combine(p3,p4)
second=combine(first_left,first_right)
assert len(second.parents)==2 and second.parents[0].parents==(p1,p2)

# Associator: both bracketings have equal actual maps, with a2-witness between
# their retained degree1 histories.
def associator(first): return add(prod(d,u,u),prod(e,r,first.witness))
left=combine(combine(p1,p2),p3)
right=combine(p1,combine(p2,p3))
a=associator(p1)
assert left.actual==right.actual
assert delta(a)==add(left.witness,right.witness,-1) and a.entries

# Pentagon: the two composites of associators are compared by a degree3 filler.
p23=combine(p2,p3)
long_route=add(add(prod(d,r,associator(p1)),associator(p1)),prod(associator(p2),r,p1.actual))
short_route=add(associator(first_left),associator(p1))
three=add(prod(d,u,u,u),prod(d,u,u,r,p1.witness))
assert delta(three)==add(long_route,short_route,-1) and three.entries
assert not delta(delta(three)).entries
# Explicit four-input endpoints certify both routes, beyond the identity above.
v0=combine(combine(combine(p1,p2),p3),p4)
v1=combine(combine(p1,p23),p4)
v2=combine(p1,combine(p23,p4))
v3=combine(p1,combine(p2,combine(p3,p4)))
v4=combine(first_left,first_right)
assert all(v.actual==v0.actual for v in (v1,v2,v3,v4))
assert delta(long_route)==delta(short_route)==add(v0.witness,v3.witness,-1)
assert delta(prod(d,r,associator(p1)))==add(v0.witness,v1.witness,-1)
assert delta(associator(p1))==add(v1.witness,v2.witness,-1)
assert delta(prod(associator(p2),r,p1.actual))==add(v2.witness,v3.witness,-1)

# Round-trip laws alone do not cohere arbitrary retained unit histories.
ix=identity('X'); ux=Map('X','X',1,{(1,0):F(1)}); vx=zero('X','X',1)
assert not delta(ux).entries and not delta(vx).entries
obstruction=add(mul(ix,ux),mul(vx,ix),-1)
assert obstruction.entries and not diffs['X']  # no differential boundary can fill it
# The history edit changes vx to ux; it is not an exact/invisible edit here.
vx_adjusted=add(vx,mul(obstruction,ix))
assert vx_adjusted==ux and not add(mul(ix,ux),mul(vx_adjusted,ix),-1).entries
print('Singular reference with nonzero surviving homology satisfies both witnessed round-trip laws; strict invertibility does not follow.')
print('Fixed-reference composition needs e=d*u with boundary d*r*d-d; the exact four-term residual law passes two applications.')
print('Nonzero degree2 associator and degree3 pentagon filler reconcile retained histories across all five bracketings.')
print('Unit triangles can be supplied after an explicit closed-history edit; arbitrary pre-existing unit witnesses can obstruct the triangle.')
print('Reference drift and history edits remain recorded. No automatic strictification, zero-cost quotient or physical normalization is assumed.')
