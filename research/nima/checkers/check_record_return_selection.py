"""Exact selection audit with the tetrahedral two-edge port held fixed.

Compare the prior left-factor rotation with a right-factor alternative.
Neither candidate is claimed uniquely WG-selected or physically gravitational.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_four_packet_cycle import UNIT, E1, E2, tensor, rotate
from check_four_packet_record_feedback import (
    basis, exchange, left_rotate, cycle, readout, lift, budget,
    matrix_of, transpose, mm, rank, sub,
)
ROOT=Path(__file__).resolve().parents[1]


def right_rotate(t):
    signs=(1,-1,-1,1)
    return tuple(signs[j]*t[4*i+j] for i in range(4) for j in range(4))


def update(rotation,x,t):
    return exchange(rotate(x),rotation(t))


def inverse(rotation,x,t):
    a,b=exchange(x,t)
    return rotate(a),rotation(b)


def main():
    I=tuple(basis(20));reports=[];matrices=[]
    t0=tensor(UNIT,UNIT);t1=tensor(E2,E2)
    for name,rotation in (('prior_left_factor',left_rotate),('alternative_right_factor',right_rotate)):
        U=matrix_of(lambda v:sum(update(rotation,v[:4],v[4:]),()),20)
        V=matrix_of(lambda v:sum(inverse(rotation,v[:4],v[4:]),()),20)
        assert mm(transpose(U),U)==I and mm(V,U)==I and mm(U,V)==I
        power=I;identity_powers=[]
        for n in range(1,7):
            power=mm(U,power)
            if power==I:identity_powers.append(n)
        assert identity_powers==[6]
        fixed_dimension=20-rank(tuple(sub(row,eye) for row,eye in zip(U,I)))
        assert fixed_dimension==6
        # Identical source port and fixed readout C; rotated readable sector
        # is orthogonal to the original one, for either factor choice.
        assert all(readout(rotation(lift(e)))==(F(0),)*4 for e in basis(4))
        observed=tuple(readout(t) for t in basis(16))
        second=tuple(readout(rotation(t)) for t in basis(16))
        observation_matrix=tuple(zip(*observed))+tuple(zip(*second))
        assert rank(observation_matrix)==8
        out0=update(rotation,UNIT,t0);out1=update(rotation,UNIT,t1)
        assert out0[0]==tuple(v/2 for v in UNIT)
        assert out1[0]==tuple(-v/2 for v in UNIT)
        for t,out in ((t0,out0),(t1,out1)):
            assert inverse(rotation,*out)==(UNIT,t)
            assert budget(*out)==budget(UNIT,t)==2
        hidden=rotation(lift(UNIT))
        assert readout(hidden)==(F(0),)*4
        assert update(rotation,(F(0),)*4,hidden)==(UNIT,(F(0),)*16)
        reports.append(dict(name=name,orthogonal=True,inverse=True,exact_order=6,
                            fixed_dimension=fixed_dimension,record_observation_rank=8,
                            hidden_record_return=True,tetrahedral_witness_response=True))
        matrices.append(U)
    assert matrices[0]!=matrices[1]
    # Legal general-bank state in the prior model; no new fitted amplitude.
    # This is not asserted to be another geometrically sourced tetrahedron.
    diagnostic=tensor(UNIT,E1)
    left=update(left_rotate,UNIT,diagnostic)
    right=update(right_rotate,UNIT,diagnostic)
    assert left[0]==tuple(v/2 for v in E1)
    assert right[0]==tuple(-v/2 for v in E1)
    assert left[0]!=right[0]
    assert update(left_rotate,UNIT,t0)==cycle(UNIT,t0)
    result=dict(schema='marici.nima.record-return-selection.v1',status='pass',
        fixed_data='Same C=Clifford sewing/2, carrier half-turn R, ordered two-edge port, exchange operation and positive counting metric.',
        candidates=reports,distinct_full_updates=True,
        separating_bank='1 tensor e1 (general retained-bank domain)',
        left_next=[str(v) for v in left[0]],right_next=[str(v) for v in right[0]],
        disposition='These tested gates do not uniquely select the prior left-factor law. Both candidates even agree on the ordinary/twisted tetrahedral fixture.',
        residual='Need a source law selecting where the existing half-turn acts, or an admissible equivalence identifying the full updates while preserving the declared port/readout. The diagnostic separator is in the prior general bank domain, not proved to be in a restricted physically selected tetrahedral image. No universal WG nonuniqueness or physical coupling claim.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_cycle.py','checkers/check_four_packet_record_feedback.py',
            'checkers/check_record_return_selection.py')})
    (ROOT/'results/record-return-selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
