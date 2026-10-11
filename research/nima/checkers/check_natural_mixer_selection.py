"""Classify common-frame-natural unital algebra automorphisms of M2(R).

Exact rational commutant certificate plus a real algebra argument reduces
all candidates to identity and R(X)=tr(X)I-X^T. The hidden-port gate selects R.
This assumes the declared common O(2) frame policy and fixed positive metric.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib
from check_four_packet_cycle import UNIT,E2,J,matrix,multiply
from check_four_packet_record_feedback import basis,matrix_of,mm,transpose,rank,readout
from check_tetrahedral_record_return import clifford_coefficients
ROOT=Path(__file__).resolve().parents[1]


def conjugation(q):
    return matrix_of(lambda v:clifford_coefficients(mm(mm(q,matrix(v)),transpose(q))),4)


def diag(vals):return tuple(tuple(v if i==j else F(0) for j in range(len(vals))) for i,v in enumerate(vals))


def act(a,x):return tuple(sum(u*v for u,v in zip(row,x)) for row in a)


def commutator_constraints(generators):
    images=[]
    for e in basis(16):
        T=tuple(e[4*i:4*i+4] for i in range(4));out=[]
        for D in generators:
            a,b=mm(T,D),mm(D,T)
            out.extend(x-y for rowa,rowb in zip(a,b) for x,y in zip(rowa,rowb))
        images.append(tuple(out))
    return tuple(zip(*images))


def main():
    I2=matrix(UNIT);I4=tuple(basis(4))
    q=((F(3,5),F(-4,5)),(F(4,5),F(3,5)))
    reflection=matrix(E2)
    for g in (q,reflection):assert mm(transpose(g),g)==I2
    Ds=[conjugation(q),conjugation(reflection)]
    equations=commutator_constraints(Ds)
    assert rank(equations)==13
    spans=[diag((F(1),F(0),F(0),F(0))),diag((F(0),F(0),F(0),F(1))),diag((F(0),F(1),F(1),F(0)))]
    assert rank([sum(T,()) for T in spans])==3
    for T in spans:
        for D in Ds:assert mm(T,D)==mm(D,T)
    # Therefore every natural real-linear T is diag(a,c,c,b).
    # Unitality: a=1. e1^2=1: c^2=1. e1*e2=J: b=c^2=1.
    candidates=[('identity',I4),('trace_minus_transpose',diag((F(1),F(-1),F(-1),F(1))))]
    C=tuple(zip(*(readout(e) for e in basis(16))))
    results=[]
    for name,T in candidates:
        assert act(T,UNIT)==UNIT and mm(T,T)==I4 and mm(transpose(T),T)==I4
        for x in basis(4):
            for y in basis(4):
                assert act(T,multiply(x,y))==multiply(act(T,x),act(T,y))
        L=matrix_of(lambda t:sum((tuple(sum(T[i][k]*t[4*k+j] for k in range(4)) for j in range(4)) for i in range(4)),()),16)
        compressed=mm(mm(C,L),transpose(C))
        hidden=compressed==tuple((F(0),)*4 for _ in range(4))
        assert hidden==(name=='trace_minus_transpose')
        if name=='identity':assert compressed==I4
        else:
            for x in basis(4):
                X=matrix(x);tr=X[0][0]+X[1][1]
                formula=tuple(tuple(tr*I2[i][j]-X[j][i] for j in range(2)) for i in range(2))
                assert matrix(act(T,x))==formula
        for g in (q,reflection,matrix(J),I2):
            D=conjugation(g);assert mm(T,D)==mm(D,T)
        results.append(dict(candidate=name,unital_algebra_automorphism=True,
                            orthogonal_involution=True,hidden_port_condition=hidden))
    # The earlier e1 half-turn fails this stronger common-frame criterion.
    e1_rotation=diag((F(1),F(1),F(-1),F(-1)))
    assert mm(e1_rotation,Ds[0])!=mm(Ds[0],e1_rotation)
    result=dict(schema='marici.nima.natural-mixer-selection.v1',status='pass',
        policy='Real-linear unital algebra automorphism, natural under simultaneous orthogonal conjugation in the existing M2(R) metric; L=T tensor I; CLC^T=0.',
        commutant_constraint_rank=13,commutant_dimension=3,
        general_form='T(s,q,p,z)=(a*s,c*q,c*p,b*z)',
        selection_equations=['a=1','c^2=1','b=c^2=1'],candidates=results,
        selected='R(X)=tr(X)I-X^T=Ad_J(X); L=R tensor I',
        frame_consequence='No orientation sign or preferred orthonormal common-frame axis is required for this R. The formula is O(2)-equivariant.',
        limits='Selection is relative to the stated naturality policy, algebra, metric and one-factor lift. It does not classify all 16D bank operations, admit independent local port-frame changes, derive a physical framing, or fix gravitational normalization.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_cycle.py','checkers/check_four_packet_record_feedback.py',
            'checkers/check_natural_mixer_selection.py')})
    (ROOT/'results/natural-mixer-selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
