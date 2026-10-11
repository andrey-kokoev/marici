"""Whole-state covariance with retained endpoint-relative orientations."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import json
from check_four_packet_cycle import UNIT,E1,E2,J,matrix,rotate
from check_four_packet_record_feedback import (basis,matrix_of,mm,transpose,rank,scale,exchange,left_rotate,budget,ZERO16)
from check_local_frame_mixer_obstruction import endpoint_frames,determinant
from check_tetrahedral_record_return import clifford_coefficients
ROOT=Path(__file__).resolve().parents[1]

def act(m,v):return tuple(sum(a*b for a,b in zip(row,v)) for row in m)
def carrier_frame(q0,q2):
    return matrix_of(lambda x:clifford_coefficients(mm(mm(q2,matrix(x)),transpose(q0))),4)
def block(a,b):
    return tuple(tuple(row)+(F(0),)*16 for row in a)+tuple((F(0),)*4+tuple(row) for row in b)
def update(v,o02,o12):
    x,t=exchange(scale(rotate(v[:4]),o02),scale(left_rotate(v[4:]),o12))
    return x+t

def main():
    identity=basis(20)
    operators={(a,b):matrix_of(lambda v:update(v,a,b),20) for a,b in product((-1,1),repeat=2)}
    for U in operators.values():assert mm(transpose(U),U)==identity
    frames=[matrix(v) for v in (UNIT,E1,E2,J)]
    count=0;bank_only_failures=0
    U=operators[1,1]
    for q0,q1,q2 in product(frames,repeat=3):
        H=block(carrier_frame(q0,q2),endpoint_frames(q0,q1,q2))
        a=determinant(q2)*determinant(q0);b=determinant(q2)*determinant(q1)
        assert mm(operators[a,b],H)==mm(H,U)
        if mm(operators[1,b],H)!=mm(H,U):bank_only_failures+=1
        # Three advances only, retaining orientations rather than refactorizing t.
        z=UNIT+ZERO16;w=act(H,z);B=budget(z[:4],z[4:])
        for depth in range(1,4):
            z=update(z,1,1);w=update(w,a,b)
            assert w==act(H,z)
            assert budget(z[:4],z[4:])==B==budget(w[:4],w[4:])
            if depth==1:assert rank(tuple(z[4+4*i:8+4*i] for i in range(4)))==4
        count+=1
    assert bank_only_failures==32
    # Coordinate changes between times need an inter-time connector, not just
    # conjugation of the update at one time. Test a pure middle-fiber flip.
    I=matrix(UNIT);X=matrix(E2)
    Hnext=block(carrier_frame(I,I),endpoint_frames(I,X,I))
    assert mm(Hnext,U)!=U
    assert mm(Hnext,U)!=operators[1,-1]
    # The correct moving-chart matrix is H_(n+1) U H_n^-1.
    result=dict(schema='marici.nima.attached-record-dynamics.v1',status='pass',
        update='U_o=E diag(o02 Ad_J, o12 L)',
        attachment_types={'o02':'det(Q2)det(Q0)','o12':'det(Q2)det(Q1)'},
        whole_matrix_covariance_assignments=count,bank_only_repair_failures=bank_only_failures,
        orthogonal_attachment_choices=4,trajectory_depth=3,first_bank_tensor_rank=4,
        conclusion='Retained orientation signs suffice for a conservative static-frame-covariant update on arbitrary banks; re-extracting two edge factors is neither necessary nor generally possible.',
        boundary='This is a conditional extension of the selected law, not source-selected physical time evolution. A changing frame requires the inter-time comparison H_(n+1) H_n^-1. Static covariance alone does not supply it.',
        normalization='All four sign choices are frame-conjugate. No physical duration, energy calibration, matter coupling or G is selected.')
    (ROOT/'results/attached-record-dynamics.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
