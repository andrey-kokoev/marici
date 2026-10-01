"""Conditional four-packet cycle using the existing real Cl(2,0) product.

Not a proton model. The active cycle law is a new explicit trial; the algebra
is reused from clifford-retained-order-recursion.md. All arithmetic is exact.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

Vector = tuple[F, F, F, F]
BASIS = tuple(tuple(F(i == j) for i in range(4)) for j in range(4))
UNIT, E1, E2, J = BASIS
MAX_DEPTH = 3

def vector(values):
    if len(values) != 4:
        raise ValueError('Exactly four real rational coefficients required')
    return tuple(F(x) for x in values)

def basis_product(i, j):
    # Index a+2*b labels e1^a e2^b. Move the second e1 past the first e2.
    return (-1 if (i & 2) and (j & 1) else 1), i ^ j

def multiply(x, y):
    out = [F(0)] * 4
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            sign, k = basis_product(i, j)
            out[k] += sign*a*b
    return tuple(out)

def tensor(x, y):
    return tuple(a*b for a in x for b in y)

def sew(pair):
    if len(pair) != 16:
        raise ValueError('Sewing requires all sixteen ordered coefficient slots')
    out = [F(0)]*4
    for i in range(4):
        for j in range(4):
            sign,k = basis_product(i,j)
            out[k] += sign*pair[4*i+j]
    return tuple(out)

def rotate(x):
    # Ad_J fixes the scalar unit and J, negates e1,e2.
    return (x[0], -x[1], -x[2], x[3])

def norm2(x): return sum(a*a for a in x)

def matrix(x):
    s,q,p,z=x
    return ((s+q,p+z),(p-z,s-q))

def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

@dataclass(frozen=True)
class PacketState:
    coefficients: Vector
    depth: int = 0
    parent: 'PacketState | None' = None
    rotated_operand: Vector | None = None
    ordered_pair: tuple | None = None
    operation: str = 'present'

    def advance(self):
        if self.depth >= MAX_DEPTH:
            raise ValueError('Retained depth 3 reached: no history is silently dropped')
        rotated=rotate(self.coefficients)
        pair=tensor(rotated,self.coefficients)
        return PacketState(sew(pair), self.depth+1, self, rotated, pair,
                           'sew(rotated-left tensor original-right)')

def closed_formula(x):
    s,q,p,z=x
    return (s*s-q*q-p*p-z*z, 2*p*z, -2*q*z, 2*s*z)

def main():
    assert multiply(E1,E1)==UNIT and multiply(E2,E2)==UNIT
    assert multiply(J,J)==tuple(-v for v in UNIT)
    assert multiply(E1,E2)==J and multiply(E2,E1)==tuple(-v for v in J)
    for a,b,c in product(BASIS,repeat=3):
        assert multiply(multiply(a,b),c)==multiply(a,multiply(b,c))
    samples=[vector(x) for x in product((F(-1),F(0),F(1,2),F(1)),repeat=4)]
    for x in samples:
        assert multiply(UNIT,x)==x and multiply(x,UNIT)==x
        assert multiply(multiply(J,x),tuple(-v for v in J))==rotate(x)
        assert norm2(rotate(x))==norm2(x)
        y=rotate(x)
        assert matrix(multiply(y,x))==mm(matrix(y),matrix(x))
        assert sew(tensor(y,x))==closed_formula(x)
        assert norm2(tensor(y,x))==norm2(x)**2
        # Frobenius submultiplicativity; coefficient norm is Frobenius / sqrt(2).
        assert norm2(closed_formula(x)) <= 2*norm2(x)**2
    for a,b in product(BASIS,repeat=2):
        assert rotate(multiply(a,b))==multiply(rotate(a),rotate(b))
    # Distinct independent tensor slots collapse under sewing; preserve pair data.
    t00=tensor(UNIT,UNIT);t11=tensor(E1,E1)
    assert t00!=t11 and sew(t00)==sew(t11)==UNIT
    assert tensor(E1,E2)!=tensor(E2,E1)
    # Real fixed-point classification is proved in the accompanying note.
    zero=vector([0,0,0,0])
    assert closed_formula(zero)==zero and closed_formula(UNIT)==UNIT
    # Identity is radially unstable; arbitrarily small positive perturbations grow.
    for denominator in (10,100,1000):
        x=vector([1+F(1,denominator),0,0,0])
        assert closed_formula(x)[0]-1 > x[0]-1
    seeds={'small':vector([F(1,4),F(1,8),F(1,8),F(1,8)]),
           'unit':UNIT, 'radially_above_unit':vector([F(11,10),0,0,0]),
           'bivector':J, 'nilpotent':vector([0,1,0,1])}
    trajectories={}
    for name,seed in seeds.items():
        state=PacketState(seed);history=[state.coefficients]
        for depth in range(1,MAX_DEPTH+1):
            previous=state;state=state.advance()
            assert state.parent is previous and state.depth==depth
            assert state.ordered_pair==tensor(state.rotated_operand,previous.coefficients)
            assert sew(state.ordered_pair)==state.coefficients
            if name=='small': assert norm2(state.coefficients)<norm2(previous.coefficients)
            history.append(state.coefficients)
        try: state.advance()
        except ValueError: pass
        else: raise AssertionError('Depth limit must refuse, not erase, history')
        trajectories[name]=[[str(v) for v in x] for x in history]
    report={'status':'passed','model':'conditional Cl(2,0) four-coefficient cycle, not proton',
            'cycle':'F(s,q,p,z)=(s²-q²-p²-z²,2pz,-2qz,2sz)',
            'retained_depth_limit':MAX_DEPTH,'exact_sample_count':len(samples),
            'pair_slots':16,'sewing_rank':4,'sewing_kernel_dimension':12,
            'real_fixed_points':['0','1'],'unit_fixed_point':'unstable to scalar perturbation',
            'zero_basin':'||x|| < 1/sqrt(2) is sufficient for contraction to zero',
            'scope':'Fixed points classified analytically in note; periodic attractors not classified. No spatial, charge, spin, color or mass model.',
            'trajectories':trajectories}
    path=Path(__file__).resolve().parents[1]/'results'/'four-packet-cycle.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: exact product, 256 cycle samples, pair retention, three-cycle depth gate, fixed-point controls. No nonzero attracting fixed point for this trial.')

if __name__=='__main__': main()
