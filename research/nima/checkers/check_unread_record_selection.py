"""Check whether retention alone forces pointwise preservation of unread data.

The alternative negates ker(C), retaining it reversibly rather than erasing it.
It is an audit countercandidate, not a newly adopted physical law.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_four_packet_cycle import UNIT,E2,tensor,rotate
from check_four_packet_record_feedback import (
    readout,lift,left_rotate,add,sub,scale,basis,matrix_of,transpose,mm,rank,budget,
)
ROOT=Path(__file__).resolve().parents[1]


def exchange(kernel_sign,x,t):
    a=readout(t);k=sub(t,lift(a))
    return a,add(lift(x),scale(k,kernel_sign))


def update(kernel_sign,x,t):return exchange(kernel_sign,rotate(x),left_rotate(t))


def inverse(kernel_sign,x,t):
    a,b=exchange(kernel_sign,x,t)
    return rotate(a),left_rotate(b)


def main():
    I=tuple(basis(20));Z4=(F(0),)*4;Z16=(F(0),)*16
    C=tuple(zip(*(readout(e) for e in basis(16))))
    bank_reader=tuple(Z4+row for row in C)
    carrier_reader=tuple(tuple(F(i==j) for j in range(20)) for i in range(4))
    t0=tensor(UNIT,UNIT);t1=tensor(E2,E2)
    reports=[]
    for sign in (F(1),F(-1)):
        U=matrix_of(lambda v:sum(update(sign,v[:4],v[4:]),()),20)
        V=matrix_of(lambda v:sum(inverse(sign,v[:4],v[4:]),()),20)
        assert mm(transpose(U),U)==I and mm(V,U)==mm(U,V)==I
        power=I;periods=[]
        for n in range(1,7):
            power=mm(U,power)
            if power==I:periods.append(n)
        assert periods==[6]
        fixed=20-rank(tuple(sub(row,e) for row,e in zip(U,I)))
        assert fixed==6
        for x in basis(4):
            assert exchange(sign,x,lift(x))==(x,lift(x))
            assert exchange(sign,x,Z16)==(Z4,lift(x))
        # Full-domain observable identity, not just a tested preparation:
        # x after two cycles = kernel_sign * C t initially.
        assert mm(carrier_reader,mm(U,U))==tuple(scale(row,sign) for row in bank_reader)
        paths=[]
        for t in (t0,t1):
            state=(UNIT,t);trajectory=[state[0]]
            for _ in range(2):
                previous=state;state=update(sign,*state)
                assert inverse(sign,*state)==previous
                assert budget(*state)==2
                trajectory.append(state[0])
            paths.append([[str(v) for v in x] for x in trajectory])
        assert paths[0][1]!=paths[1][1]
        reports.append(dict(kernel_sign=str(sign),orthogonal=True,inverse=True,exact_order=6,
                            fixed_dimension=fixed,readable_agreement_fixed=True,full_agreement_fixed=(sign==1),empty_record_projection=True,
                            ordinary_carrier_history=paths[0],twisted_carrier_history=paths[1]))
    k=sub(t0,lift(readout(t0)))
    assert k!=Z16 and readout(k)==Z4
    assert exchange(F(-1),Z4,k)==(Z4,scale(k,F(-1)))
    assert exchange(F(-1),*exchange(F(-1),Z4,k))==(Z4,k)
    result=dict(schema='marici.nima.unread-record-selection.v1',status='pass',candidates=reports,
        exact_identity='active_carrier_projection * U_s^2 = s * initial_bank_readout',
        no_readout_preserving_conjugacy='If S preserves O(x,t)=(x,Ct) and intertwines the two laws, applying the two-step carrier identity forces Ct=-Ct for every bank. The existing fixture has Ct=UNIT/2, contradiction.',
        disposition='Reversible retention alone permits a distinguishable kernel negation. It passes pure-readable agreement but fails full agreement: Ct=x must fix the whole exchange state, including its unread complement. The inherited zero-discrepancy/no-update condition therefore excludes it.',
        source_boundary='Full agreement E(x,t)=(x,t) whenever Ct=x implies E(0,k)=(0,k) for Ck=0. Thus the unread-fixing assumption follows from this full-state agreement law, not from lossless retention alone. The criterion applies to the exchange stage, not its preceding bank rotation. No alternative is adopted.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_record_feedback.py','checkers/check_unread_record_selection.py')})
    (ROOT/'results/unread-record-selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
