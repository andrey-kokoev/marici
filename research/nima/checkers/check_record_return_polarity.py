"""Audit exchange polarity, not a replacement for the prior chosen law.

Test +/- readable-port exchange with the same metric, record adapter and
rotation. Distinguish conservation from selection of calibrated response.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_four_packet_cycle import UNIT,E2,tensor,rotate
from check_four_packet_record_feedback import (
    readout,lift,left_rotate,scale,add,sub,basis,matrix_of,mm,transpose,rank,budget,cycle,
)
ROOT=Path(__file__).resolve().parents[1]


def exchange(sign,x,t):
    return scale(readout(t),sign),add(scale(lift(x),sign),sub(t,lift(readout(t))))


def update(sign,x,t):return exchange(sign,rotate(x),left_rotate(t))


def inverse(sign,x,t):
    a,b=exchange(sign,x,t)
    return rotate(a),left_rotate(b)


def main():
    I=tuple(basis(20));reports=[]
    # O retains BOTH currently active carrier and current calibrated bank readout.
    O=tuple(tuple(F(i==j) for j in range(20)) for i in range(4))
    C=tuple(zip(*(readout(e) for e in basis(16))))
    O+=tuple((F(0),)*4+row for row in C)
    # Readable-bank component after one step is +/- R*x, independently of t.
    Rx=tuple(tuple(rotate(e)[i] for e in basis(4))+(F(0),)*16 for i in range(4))
    bank_reader=O[4:]
    t0=tensor(UNIT,UNIT);t1=tensor(E2,E2)
    matrices=[]
    for sign in (F(1),F(-1)):
        U=matrix_of(lambda v:sum(update(sign,v[:4],v[4:]),()),20)
        V=matrix_of(lambda v:sum(inverse(sign,v[:4],v[4:]),()),20)
        assert mm(transpose(U),U)==I and mm(V,U)==mm(U,V)==I
        power=I;identity_powers=[]
        for n in range(1,7):
            power=mm(U,power)
            if power==I:identity_powers.append(n)
        assert identity_powers==[6]
        fixed=20-rank(tuple(sub(row,eye) for row,eye in zip(U,I)))
        assert fixed==6
        assert mm(bank_reader,U)==tuple(scale(row,sign) for row in Rx)
        out0=update(sign,UNIT,t0);out1=update(sign,UNIT,t1)
        assert out0[0]==scale(UNIT,sign/2) and out1[0]==scale(UNIT,-sign/2)
        for t,out in ((t0,out0),(t1,out1)):
            assert budget(*out)==budget(UNIT,t)==2
            assert inverse(sign,*out)==(UNIT,t)
        reports.append(dict(polarity=str(sign),orthogonal=True,inverse=True,
                            exact_order=6,fixed_dimension=fixed,
                            ordinary_next=[str(v) for v in out0[0]],
                            twisted_next=[str(v) for v in out1[0]],
                            next_bank_readout_for_x_unit=[str(v) for v in readout(out0[1])]))
        matrices.append(U)
    assert update(F(1),UNIT,t0)==cycle(UNIT,t0)
    # Any map S (even nonlinear) with O S=O preserves x and Ct.
    # If S U+ = U- S, applying Ct gives Rx=-Rx for every x, impossible
    # at x=UNIT. The matrix identities above prove the premises uniformly
    # over the entire bank; this is stronger than testing a candidate S.
    assert rotate(UNIT)!=scale(rotate(UNIT),F(-1))
    # Inherited source gate: q'=q+r(z-a), z'=a fixes an already agreed
    # longitudinal value z=a. Apply this to the EXCHANGE stage, not the
    # entire cycle including its separately supplied rotations.
    for x in basis(4):
        for e in basis(16):
            k=sub(e,lift(readout(e)))
            assert readout(k)==(F(0),)*4
            agreed=add(lift(x),k)
            assert readout(agreed)==x
            assert exchange(F(1),x,agreed)==(x,agreed)
            assert exchange(F(-1),x,agreed)!=(x,agreed)
    result=dict(schema='marici.nima.record-return-polarity.v1',status='pass',
        fixed_data='Same Clifford C, positive metric, carrier R, left bank rotation L and ordered two-edge adapter.',
        candidates=reports,
        no_readout_preserving_intertwiner='With O(x,t)=(x,Ct), O S=O and S U+=U- S imply Rx=-Rx for all x. Counterexample x=UNIT. Does not assume S linear.',
        inherited_source_gate='The prior same-coordinate memory lift fixes agreement: z=a implies unchanged comparison state. Positive exchange fixes (x,C^T x+k) for Ck=0; negative exchange fails for nonzero x. Tested on basis-generated agreed states; algebraic argument in packet.',
        source_gate_locator='research/nima/comparison-update-dynamics-and-energy-normalization.md#exact-memory-lift-of-the-projection',
        disposition='Structural gates alone do not select polarity, and calibrated readouts distinguish the candidates. The inherited agreement-fixing comparison law selects positive polarity among this pair; negative polarity is not a faithful extension of that same source convention.',
        limits='Opposite polarity is an audit countercandidate, not a newly adopted law or a derived WG rule. A coarser sign-insensitive observation or different source admission policy changes the equivalence question. No gravitational coupling derived.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_record_feedback.py','checkers/check_four_packet_cycle.py',
            'checkers/check_record_return_polarity.py',
            'comparison-update-dynamics-and-energy-normalization.md')})
    (ROOT/'results/record-return-polarity.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
