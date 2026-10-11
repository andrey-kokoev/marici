"""Two existing Clifford half-turns and the observable return normal form.

Keep carrier R and exchange fixed; compare left bank conjugation by J and e1.
The signed bank permutation preserves C but transports the hidden readout.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_four_packet_cycle import UNIT,E1,E2,tensor,basis_product,rotate,multiply
from check_four_packet_record_feedback import basis,matrix_of,mm,transpose,readout,exchange,left_rotate,rank,sub
ROOT=Path(__file__).resolve().parents[1]


def e1_left(t):
    signs=(1,1,-1,-1)
    return tuple(signs[i]*t[4*i+j] for i in range(4) for j in range(4))


def bank_change(t):
    # Within each fixed product-index fiber, interchange left indices 1,3.
    # The multiplication signs determine the compensation uniquely here.
    perm=(0,3,2,1);out=[F(0)]*16
    for i in range(4):
        for j in range(4):
            s,k=basis_product(i,j);ip=perm[i];jp=ip^k
            sp,kp=basis_product(ip,jp);assert kp==k
            out[4*ip+jp]=s*sp*t[4*i+j]
    return tuple(out)


def update(L,v):return sum(exchange(rotate(v[:4]),L(v[4:])),())


def main():
    for i,e in enumerate(basis(4)):
        assert multiply(E1,multiply(e,E1))==tuple((1,1,-1,-1)[i]*v for v in e)
    C=tuple(zip(*(readout(e) for e in basis(16))))
    I16=tuple(basis(16));I20=tuple(basis(20));zero4=tuple((F(0),)*4 for _ in range(4))
    B=matrix_of(bank_change,16)
    LJ=matrix_of(left_rotate,16);L1=matrix_of(e1_left,16)
    assert mm(B,B)==I16 and mm(transpose(B),B)==I16 and mm(C,B)==C
    assert mm(B,L1)==mm(LJ,B)
    S=matrix_of(lambda v:v[:4]+bank_change(v[4:]),20)
    UJ=matrix_of(lambda v:update(left_rotate,v),20)
    U1=matrix_of(lambda v:update(e1_left,v),20)
    assert mm(S,U1)==mm(UJ,S)
    reports=[]
    for name,L in (('J',left_rotate),('e1',e1_left)):
        M=matrix_of(L,16);U=matrix_of(lambda v:update(L,v),20)
        assert mm(M,M)==I16 and mm(transpose(M),M)==I16
        assert mm(mm(C,M),transpose(C))==zero4
        assert mm(transpose(U),U)==I20
        # Observation N(v)=(x,a,b), a=Ct, b=CLt.
        X=tuple(tuple(F(i==j) for j in range(20)) for i in range(4))
        A=tuple((F(0),)*4+row for row in C)
        H=tuple((F(0),)*4+row for row in mm(C,M))
        N=X+A+H
        target=H+tuple(tuple(rotate(e)[i] for e in basis(4))+(F(0),)*16 for i in range(4))+A
        assert mm(N,U)==target
        assert rank(N)==12
        U3=mm(mm(U,U),U)
        RX=tuple(tuple(rotate(e)[i] for e in basis(4))+(F(0),)*16 for i in range(4))
        assert mm(X,U3)==RX and mm(U3,U3)==I20
        assert 20-rank(tuple(sub(row,eye) for row,eye in zip(U,I20)))==6
        for t in (tensor(UNIT,UNIT),tensor(E2,E2)):
            assert bank_change(t)==t
        ordinary=update(L,UNIT+tensor(UNIT,UNIT))[:4]
        twisted=update(L,UNIT+tensor(E2,E2))[:4]
        assert ordinary==tuple(v/2 for v in UNIT) and twisted==tuple(-v/2 for v in UNIT)
        reports.append(dict(mixer=name,coisometric_hidden_port=True,normal_form=True,
                            observation_rank=12,unobserved_dimension=8,tetrahedral_response=True))
    diagnostic=tensor(E1,UNIT)
    assert update(e1_left,UNIT+diagnostic)[:4]!=update(left_rotate,UNIT+diagnostic)[:4]
    assert update(e1_left,UNIT+diagnostic)[:4]==update(left_rotate,UNIT+bank_change(diagnostic))[:4]
    result=dict(schema='marici.nima.bank-mixing-normal-form.v1',status='pass',candidates=reports,
        normal_form='(x,a,b) -> (b,Rx,a), a=Ct, b=CLt',
        recurrence='x_(n+3)=R x_n; x_0=x, x_1=CLt, x_2=Ct',
        intertwiner='S=diag(I4,B), C B=C, B L_e1=L_J B, S U_e1=U_J S',
        disposition='These two bank mixers give equivalent observed dynamics under the explicit transported adapter. The source-sensitive remaining choice is the hidden readout b(P)=CL E(P), not another scalar correction to closure.',
        limits='The general normal-form derivation assumes orthogonal involutive L and CLC^T=0; those conditions are checked here, not derived universally from WG. The signed bank coordinate map need not preserve separate ordered edge-factor meanings. No physical gauge policy or gravitational coefficient inferred.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_cycle.py','checkers/check_four_packet_record_feedback.py',
            'checkers/check_bank_mixing_normal_form.py')})
    (ROOT/'results/bank-mixing-normal-form.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
