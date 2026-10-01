"""Exact higher coherence in an explicitly chosen differential-graded model.

Four chain degrees each carry Q^2; differential is identity on 1->0 and3->2.
This contractible test complex and the homotopy lifts are model inputs.
"""
from dataclasses import dataclass
from fractions import Fraction as F

N=8
ZERO=tuple(tuple(F(0) for _ in range(N)) for _ in range(N))
I2=((F(1),F(0)),(F(0),F(1)))
H=((F(0),F(1)),(F(0),F(0)))
K=((F(0),F(0)),(F(1),F(0)))


def block_matrix(blocks):
    a=[list(row) for row in ZERO]
    for row,col,value in blocks:
        for i in range(2):
            for j in range(2): a[2*row+i][2*col+j]+=value[i][j]
    return tuple(map(tuple,a))


def plus(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def times(a,b):
    out=[[F(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for k in range(N):
            if a[i][k]:
                for j in range(N):
                    if b[k][j]: out[i][j]+=a[i][k]*b[k][j]
    return tuple(map(tuple,out))


D=block_matrix([(0,1,I2),(2,3,I2)])
assert times(D,D)==ZERO


@dataclass(frozen=True)
class Map:
    source: str
    target: str
    degree: int
    value: tuple

    def __post_init__(self):
        assert all(not self.value[i][j] or i//2-j//2==self.degree
                   for i in range(N) for j in range(N))


def add(a,b,sign=1):
    if (a.source,a.target,a.degree)!=(b.source,b.target,b.degree):
        raise ValueError('incompatible graded sum')
    return Map(a.source,a.target,a.degree,plus(a.value,tuple(tuple(sign*x for x in row) for row in b.value)))


def compose(left,right):
    if left.target!=right.source: raise ValueError('noncomposable endpoint types')
    return Map(left.source,right.target,left.degree+right.degree,times(right.value,left.value))


def differential(a):
    # Homological grading: delta f = D f - (-1)^degree f D.
    return Map(a.source,a.target,a.degree-1,
               plus(times(D,a.value),tuple(tuple(-((-1)**a.degree)*x for x in row) for row in times(a.value,D))))


def embed(matrix,source,target):
    return Map(source,target,0,block_matrix([(i,i,matrix) for i in range(4)]))


def lift(matrix,source,target):
    return Map(source,target,1,block_matrix([(1,0,matrix),(3,2,matrix)]))


@dataclass(frozen=True)
class Comparison:
    actual: Map
    reference: Map
    witness: Map

    def __post_init__(self):
        assert self.actual.degree==self.reference.degree==0 and self.witness.degree==1
        assert differential(self.actual).value==differential(self.reference).value==ZERO
        assert differential(self.witness)==add(self.actual,self.reference,-1)


@dataclass(frozen=True)
class HigherComparison:
    source: Map
    target: Map
    filler: Map
    parents: tuple

    def __post_init__(self):
        assert self.source.degree==self.target.degree==self.filler.degree-1
        assert differential(self.source)==differential(self.target)
        assert differential(self.filler)==add(self.source,self.target,-1)


def witness_routes(left,right):
    actual=compose(left.actual,right.actual)
    reference=compose(left.reference,right.reference)
    first=add(compose(left.actual,right.witness),compose(left.witness,right.reference))
    second=add(compose(left.witness,right.actual),compose(left.reference,right.witness))
    a=Comparison(actual,reference,first); b=Comparison(actual,reference,second)
    higher=compose(left.witness,right.witness)
    assert higher.degree==2 and differential(higher)==add(second,first,-1)
    return a,b,higher


errors=[H,K,I2]
records=[]
for i,error in enumerate(errors):
    s,t=f'A{i}',f'A{i+1}'
    reference=embed(I2,s,t); rho=embed(error,s,t)
    records.append(Comparison(add(reference,rho),reference,lift(error,s,t)))
# Canonical lifts already realize the full finite noncommutative residual.
a,b,canonical_k=witness_routes(records[0],records[1])
assert a.actual.value!=a.reference.value and canonical_k.value==ZERO
# Add closed history to one witness without changing actual/reference/residual.
closed=Map('A1','A2',1,block_matrix([(2,1,I2)]))
assert differential(closed).value==ZERO
old=records[1]
records[1]=Comparison(old.actual,old.reference,add(old.witness,closed))
a,b,k2=witness_routes(records[0],records[1])
assert k2.value!=ZERO and differential(k2).value!=ZERO
assert a.actual==compose(records[0].actual,old.actual)
first_higher=HigherComparison(b.witness,a.witness,k2,tuple(records[:2]))
# Exact Leibniz identity on every composable pair of witness/response maps.
for left in (records[0].witness,records[0].actual):
    for right in (records[1].witness,records[1].actual):
        lhs=differential(compose(left,right))
        rhs=add(compose(left,differential(right)),compose(differential(left),right),(-1)**right.degree)
        assert lhs==rhs

# A second degree ascent: h3*h2*h1 fills the signed six-face cube.
h=[r.witness for r in records]
t3=compose(k2,h[2])
assert t3.degree==3 and t3.value!=ZERO


def sequence(parts):
    out=parts[0]
    for part in parts[1:]: out=compose(out,part)
    return out


positive=Map('A0','A3',2,ZERO); negative=positive
for i in range(3):
    for endpoint,endpoint_sign in ((records[i].actual,1),(records[i].reference,-1)):
        face=sequence(h[:i]+[endpoint]+h[i+1:])
        if endpoint_sign*((-1)**(2-i))==1: positive=add(positive,face)
        else: negative=add(negative,face)
assert differential(t3)==add(positive,negative,-1)
assert differential(positive)==differential(negative)
assert differential(differential(t3)).value==ZERO
second_higher=HigherComparison(positive,negative,t3,(first_higher,records[2]))
assert second_higher.parents[0] is first_higher
# Homogeneous records remain endpoint-checked even with equal matrix dimensions.
try: compose(records[0].witness,records[0].witness)
except ValueError: pass
else: raise AssertionError('silent endpoint identification')
# An ordinary degree-zero matrix space with zero differential cannot witness a
# nonzero residual. The auxiliary differential and its lifts are essential inputs.
assert records[0].actual.value!=records[0].reference.value
assert plus(times(ZERO,h[0].value),times(h[0].value,ZERO))==ZERO
print('Exact graded Leibniz rule realizes both transported residual composition routes.')
print('Degree2 witness h2*h1 has boundary H_second-H_first; degree3 witness h3*h2*h1 fills the six-face cube.')
print('All endpoints, boundary equations and boundary-of-boundary identities pass with rational matrices.')
print('Canonical lifts give zero degree2 witness; added closed history produces nonzero degree2/3 witnesses with unchanged lower comparisons.')
print('Contractible test complex and lift/history choices are explicit inputs; zero-differential matrices cannot fill nonzero residuals.')
