"""Exact Clark radical reduction, marked-arrow duality, and cone sign.

Finite coefficient matrices verify the identities. Faithfulness of shell
features after reduction is proved by holomorphic Fourier uniqueness in the
associated note, not by this one-spectral-fiber fixture.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]


def creation(dimension,feature,depth=2):
    words=[()]
    for r in range(1,depth+1):words.extend(product(range(dimension),repeat=r))
    idx={w:i for i,w in enumerate(words)}
    A=sp.zeros(len(words))
    for w in words:
        if len(w)<depth:
            for j in range(dimension):A[idx[w+(j,)],idx[w]]=feature[j]
    return A


def main():
    B=sp.Matrix([[1,1,-1,1],[1,1,1,-1]])/2
    J=sp.diag(1,-1)
    C=B.conjugate().T*J*B
    P=B.conjugate().T*B
    assert B*B.conjugate().T==sp.eye(2)
    assert P*P==P and C*C==P
    assert C.rank()==2 and P.rank()==2
    assert B*C==J*B
    assert C.nullspace()==B.nullspace()
    tau=sp.Rational(1,2)
    quotient=sp.diag(sp.ones(1),B,sp.kronecker_product(B,B))
    full_form=sp.diag(sp.ones(1),tau**2*C,tau**4*sp.kronecker_product(C,C))
    reduced_form=sp.diag(sp.ones(1),tau**2*J,tau**4*sp.kronecker_product(J,J))
    assert quotient.shape==(7,21)
    assert quotient*quotient.conjugate().T==sp.eye(7)
    assert quotient.conjugate().T*reduced_form*quotient==full_form
    assert full_form.rank()==7 and reduced_form.rank()==7

    features=[sp.Matrix([1+sp.I,2-sp.I,-1+2*sp.I,3]),
              sp.Matrix([2-sp.I,1,3+sp.I,-2*sp.I])]
    operators=[]; mates=[]
    for feature in features:
        original=creation(4,feature)
        reduced=creation(2,B*feature)
        assert quotient*original==reduced*quotient
        mate=reduced_form.inv()*reduced.conjugate().T*reduced_form
        # Direct signed contraction, including degree-weight ratio.
        signed_feature=J*B*feature
        direct=tau**2*creation(2,signed_feature).conjugate().T
        assert mate==direct
        assert reduced.conjugate().T*reduced_form==reduced_form*mate
        assert mate*reduced!=sp.eye(7)
        operators.append(reduced);mates.append(mate)
        # Contravariant cochain dual of Cone(A) has differential -A^*.
        # Riesz identification changes it to -A^sharp, as in Fib(A^sharp).
        assert reduced_form.inv()*(-reduced.conjugate().T)*reduced_form==-mate
    composite=operators[1]*operators[0]
    composite_mate=reduced_form.inv()*composite.conjugate().T*reduced_form
    assert sp.simplify(composite_mate-mates[0]*mates[1])==sp.zeros(7)
    # Degree-zero forgotten arrow has identity record component.
    assert reduced_form.inv()*sp.eye(7).conjugate().T*reduced_form==sp.eye(7)
    # The literal feature reversal swaps sheets; it is not this adjoint.
    swap=sp.Matrix([[0,1],[1,0]])
    Ptail=sp.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
    assert B*Ptail==swap*B
    assert swap.T*J*swap==-J
    result={
        'schema':'marici.voevodsky.marked-clark-duality-square.v1',
        'passed':True,
        'sheet_matrix':[[str(x) for x in B.row(i)] for i in range(2)],
        'exact_checks':[
            'B B*=I and C=B* J B', 'C^2=B*B is the radical-complement projection',
            'degree-two quotient 21->7 is coisometric',
            'signed form factors through the quotient',
            'creation descends through the quotient',
            'unique signed mate equals weighted J-contraction',
            'contragredient reverses composition',
            'forgotten record arrow has identity mate',
            'dual cone differential agrees with the shifted fiber differential',
            'sheet polarity remains separately typed'],
        'full_four_port_record_dimension':21,
        'reduced_two_sheet_record_dimension':7,
        'ambient_radical_dimension':14,
        'faithfulness_scope':'Actual shell-feature image on an open spectral disk, by the accompanying analytic proof; not every arbitrary vector in the four-port carrier.',
        'scope':'Bounded marked-arrow duality and its two-term cone comparison. No full derived equivalence, physical event access, or inverse/adjoint identification.',
    }
    out=ROOT/'research/voevodsky/results/marked-clark-duality-square.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
