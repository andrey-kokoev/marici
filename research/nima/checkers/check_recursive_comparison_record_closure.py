"""Conditional closure of comparison records under typed composition.

The same constructor carries actual and reference maps through both levels.
It supplies residual propagation, not a higher-cell or all-pairs generator.
"""
from dataclasses import dataclass
from fractions import Fraction as F

Z=((F(0),F(0)),(F(0),F(0)))
I=((F(1),F(0)),(F(0),F(1)))
H=((F(0),F(1)),(F(0),F(0)))
K=((F(0),F(0)),(F(1),F(0)))


def add(a,b): return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def neg(a): return tuple(tuple(-v for v in row) for row in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b): return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)),F(0)) for j in range(2)) for i in range(2))
def scale(c,a): return tuple(tuple(c*v for v in row) for row in a)


@dataclass(frozen=True)
class Comparison:
    name: str
    source: str
    target: str
    actual: tuple
    reference: tuple
    children: tuple = ()

    @property
    def residual(self): return sub(self.actual,self.reference)

    @property
    def leaves(self):
        if not self.children: return (self.name,)
        return tuple(name for child in self.children for name in child.leaves)


def compose(left,right):
    if left.target!=right.source:
        raise ValueError('comparison endpoints do not compose')
    result=Comparison(f'({right.name} after {left.name})',left.source,right.target,
                      mul(right.actual,left.actual),mul(right.reference,left.reference),(left,right))
    predicted=add(add(mul(right.reference,left.residual),mul(right.residual,left.reference)),
                  mul(right.residual,left.residual))
    assert result.residual==predicted
    return result


# Four genuinely composable records are an explicit network input.
references=[I,add(I,K),add(I,H),scale(F(2),I)]
errors=[scale(F(2,3),H),scale(F(3,5),K),scale(F(-1,7),H),scale(F(5,11),K)]
leaves=[Comparison(str(i),f'A{i}',f'A{i+1}',add(ref,error),ref)
        for i,(ref,error) in enumerate(zip(references,errors))]
first=[compose(leaves[0],leaves[1]),compose(leaves[2],leaves[3])]
second=compose(*first)
assert second.leaves==('0','1','2','3')
assert (second.source,second.target)==('A0','A4')
# All five bracketings of four inputs have identical actual/reference/residual.
variants=[second,
    compose(compose(compose(leaves[0],leaves[1]),leaves[2]),leaves[3]),
    compose(compose(leaves[0],compose(leaves[1],leaves[2])),leaves[3]),
    compose(leaves[0],compose(compose(leaves[1],leaves[2]),leaves[3])),
    compose(leaves[0],compose(leaves[1],compose(leaves[2],leaves[3])))]
assert all((v.actual,v.reference,v.residual)==(second.actual,second.reference,second.residual) for v in variants)
assert len({v.name for v in variants})==5  # retained histories remain distinct
# Agreement is stable at both levels, including nonidentity references.
agree=[Comparison(str(i),f'A{i}',f'A{i+1}',ref,ref) for i,ref in enumerate(references)]
assert compose(compose(*agree[:2]),compose(*agree[2:])).residual==Z
# Residual-only multiplication omits reference transport terms.
assert first[0].residual!=mul(leaves[1].residual,leaves[0].residual)
# Two comparisons in the original common Hom(A,B) do not compose automatically.
a=Comparison('a','A','B',add(I,H),I)
b=Comparison('b','A','B',add(I,K),I)
try: compose(a,b)
except ValueError: pass
else: raise AssertionError('equal matrix size silently identified endpoint types')
# Declaring an endomorphism frame makes self-reuse legal, but adds no new leaf.
endo=Comparison('seed','V','V',add(I,H),I)
one=compose(endo,endo); two=compose(one,one)
assert len(two.leaves)==4 and set(two.leaves)=={'seed'}
assert two.actual==mul(mul(endo.actual,endo.actual),mul(endo.actual,endo.actual))
# Algebraic degree doubling can therefore count repeated occurrences, not inputs.
# With I references, composing two errors is r1+r2+r2*r1, not just r2*r1.
u=Comparison('u','V','V',add(I,H),I); v=Comparison('v','V','V',add(I,K),I)
uv=compose(u,v)
assert uv.residual==add(add(H,K),mul(K,H))
assert compose(v,u).residual!=uv.residual
# Actual slot composition y*x versus independently retained d requires a
# factorization of d to be generated from reference-decorated leg records.
x=Comparison('x','A','U',add(I,H),I)
y=Comparison('y','U','B',add(I,K),add(I,H))
root=compose(x,y)
assert root.reference!=I
assert root.residual!=sub(root.actual,I)
y_matched=Comparison('y','U','B',y.actual,I)
assert compose(x,y_matched).residual==sub(root.actual,I)
# A common intermediate change of basis transports both actual/reference maps.
g=((F(2),F(0)),(F(0),F(1)))
g_inv=((F(1,2),F(0)),(F(0),F(1)))
x_changed=Comparison('x_changed','A','U',mul(g,x.actual),mul(g,x.reference))
y_changed=Comparison('y_changed','U','B',mul(y.actual,g_inv),mul(y.reference,g_inv))
changed=compose(x_changed,y_changed)
assert (changed.actual,changed.reference,changed.residual)==(root.actual,root.reference,root.residual)
# Composition by itself supplies no additive norm-budget law.
norm2=lambda matrix: sum((v*v for row in matrix for v in row),F(0))
assert norm2(uv.residual)==3
assert norm2(u.residual)+norm2(v.residual)==2
print('One typed constructor applied twice: four leaves, composed endpoints and reference, exact three-term residual law.')
print('All five bracketings agree on values and residuals while retaining distinct histories; agreement propagates through both levels.')
print('Common Hom(A,B) records are rejected as composable inputs without an additional endpoint adapter/network.')
print('Endomorphism self-reuse gives four leaf occurrences but only one independent seed; no new cell degree is generated.')
print('Residual-only multiplication drops transported terms. Reference factorization at primitive legs remains an explicit input.')
