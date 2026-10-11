"""State-sensitive conditional two-qubit calculation, not a Born-rule derivation.
uv run --with sympy python research/nima/checkers/check_entanglement.py
The full legacy implementation is retained in the quantum-readout quarantine.
"""
import json
from itertools import combinations,product
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
I2 = s.eye(2)
X = s.Matrix([[0,1],[1,0]])
Z = s.diag(1,-1)
ALICE = [Z,X]
BOB = [(Z+X)/s.sqrt(2),(Z-X)/s.sqrt(2)]


def validate_density(rho):
    if rho.shape != (4,4) or rho != rho.H or s.trace(rho) != 1:
        raise ValueError('A normalized Hermitian state on the declared two-qubit space is required')
    if not all(s.simplify(rho.extract(ix,ix).det()) >= 0
               for k in range(1,5) for ix in combinations(range(4),k)):
        raise ValueError('The supplied state is not positive')


def expectation(rho,a,b):
    return s.simplify(s.trace(rho*s.kronecker_product(a,b)))


def joint_table(rho):
    validate_density(rho)
    table = {}
    for x,y,a,b in product(range(2),range(2),(-1,1),(-1,1)):
        pa,pb = (I2+a*ALICE[x])/2,(I2+b*BOB[y])/2
        k = s.kronecker_product(pa,pb)
        continuation = s.simplify(k*rho*k.H)
        probability = s.simplify(s.trace(continuation))
        assert probability >= 0
        assert probability == expectation(rho,pa,pb)
        table[x,y,a,b] = probability
    for x,y in product(range(2),repeat=2):
        assert sum(table[x,y,a,b] for a,b in product((-1,1),repeat=2)) == 1
    for x,a in product(range(2),(-1,1)):
        assert s.simplify(sum(table[x,0,a,b]-table[x,1,a,b] for b in (-1,1))) == 0
    for y,b in product(range(2),(-1,1)):
        assert s.simplify(sum(table[0,y,a,b]-table[1,y,a,b] for a in (-1,1))) == 0
    return table


def chsh(rho):
    table = joint_table(rho)
    return s.simplify(sum((1 if (x,y) != (1,1) else -1)*a*b*p
                          for (x,y,a,b),p in table.items()))


def states():
    bell = s.Matrix([1,0,0,1])/s.sqrt(2)
    p00,p01,p11 = (s.eye(4)[:,j]*s.eye(4)[:,j].T for j in (0,1,3))
    return {'bell':bell*bell.H,'product00':p00,'product01':p01,'classical_mixture':(p00+p11)/2}


def verify():
    st = states()
    vals = {name:chsh(rho) for name,rho in st.items()}
    assert vals == {'bell':2*s.sqrt(2),'product00':s.sqrt(2),
                    'product01':-s.sqrt(2),'classical_mixture':s.sqrt(2)}
    assert expectation(st['product00'],X,X) == 0
    assert vals['bell'] != vals['product01']  # The old state-replacement hostile must now change the readout.
    mixed = st['classical_mixture']
    assert mixed == (st['product00']+s.diag(0,0,0,1))/2
    assert mixed != s.kronecker_product(I2/2,I2/2)
    partial_transpose = s.Matrix(4,4,lambda i,j:st['bell'][2*(i//2)+j%2,2*(j//2)+i%2])
    assert partial_transpose.eigenvals() == {-s.Rational(1,2):1,s.Rational(1,2):3}
    assert set(a0*b0+a0*b1+a1*b0-a1*b1 for a0,a1,b0,b1 in product((-1,1),repeat=4)) == {-2,2}
    refused = False
    try:
        validate_density(s.diag(1,1,-1,0))
    except ValueError:
        refused = True
    assert refused
    return {'schema':'marici.nima.entanglement-repaired.v1','status':'pass',
            'classification':'state-sensitive Born/Lueders comparison on supplied two-qubit states',
            'CHSH':{k:str(v) for k,v in vals.items()},'product_same_x_correlation':'0',
            'nonproduct_mixture_is_separable':True,'invalid_density_refused':refused,
            'given_not_derived':['two-qubit tensor factors','prepared density matrix','local analyzers',
                                 'Born trace and Lueders continuation'],
            'physical_record_map':'not established by this calculation',
            'superseding_packet':'gram-interference-and-bell-readout-comparison.md'}


def main():
    out = ROOT/'results/entanglement-repaired.json'
    out.unlink(missing_ok=True)
    result = verify()
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
