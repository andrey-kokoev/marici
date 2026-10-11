"""Exact readout-preserving conjugacy of left/right record rotation laws.

The bank map is the signed factor interchange determined by the existing
Clifford multiplication table. Source path order is retained separately.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib
from check_four_packet_cycle import UNIT,E1,E2,tensor,basis_product
from check_four_packet_record_feedback import basis,matrix_of,mm,transpose,readout,left_rotate
from check_record_return_selection import right_rotate,update
ROOT=Path(__file__).resolve().parents[1]


def braided_swap(t):
    out=[F(0)]*16
    for i in range(4):
        for j in range(4):
            sign1,k1=basis_product(i,j)
            sign2,k2=basis_product(j,i)
            assert k1==k2
            out[4*j+i]=sign1*sign2*t[4*i+j]
    return tuple(out)


def main():
    B=matrix_of(braided_swap,16);I16=tuple(basis(16));I20=tuple(basis(20))
    assert mm(B,B)==I16 and mm(transpose(B),B)==I16
    C=tuple(zip(*(readout(e) for e in basis(16))))
    assert mm(C,B)==C
    L=matrix_of(left_rotate,16);R=matrix_of(right_rotate,16)
    assert mm(B,L)==mm(R,B)
    S=matrix_of(lambda v:v[:4]+braided_swap(v[4:]),20)
    UL=matrix_of(lambda v:sum(update(left_rotate,v[:4],v[4:]),()),20)
    UR=matrix_of(lambda v:sum(update(right_rotate,v[:4],v[4:]),()),20)
    assert mm(S,S)==I20 and mm(transpose(S),S)==I20
    assert mm(S,UL)==mm(UR,S)
    assert mm(mm(S,UL),S)==UR
    # Combined current active carrier plus record readout is unchanged.
    O=tuple(tuple(F(i==j) for j in range(20)) for i in range(4))+tuple((F(0),)*4+row for row in C)
    assert mm(O,S)==O
    left_power=I20;right_power=I20
    for n in range(13):
        assert mm(right_power,S)==mm(S,left_power)
        assert mm(mm(O,right_power),S)==mm(O,left_power)
        left_power=mm(UL,left_power);right_power=mm(UR,right_power)
    # The successful two tetrahedral fixtures are fixed by this transformation.
    for t in (tensor(UNIT,UNIT),tensor(E2,E2)):
        assert braided_swap(t)==t
    # The previous distinguishing SAME-COORDINATE input must transform too.
    t=tensor(UNIT,E1);bt=braided_swap(t)
    assert bt==tensor(E1,UNIT) and bt!=t
    assert update(left_rotate,UNIT,t)[0]!=update(right_rotate,UNIT,t)[0]
    assert update(left_rotate,UNIT,t)[0]==update(right_rotate,UNIT,bt)[0]
    # A bank-coordinate transformation is not reversal of a typed source route.
    # Original tensor factor order is (later 12, earlier 01).
    first=(0,1);later=(1,2)
    assert first[1]==later[0]
    assert later[1]!=first[0]  # attempting execution 12 then 01 fails matching
    result=dict(schema='marici.nima.record-return-equivalence.v1',status='pass',
        bank_map='B(e_i tensor e_j)=sigma(i,j)*sigma(j,i) e_j tensor e_i, with sigma from existing Clifford table',
        identities=['B^2=I','B^T B=I','C B=C','B L_left=L_right B',
                    'S=diag(I4,B)','S U_left=U_right S','O S=O for O(x,t)=(x,Ct)'],
        consequence='Exact all-step observed equivalence by induction from the intertwiner; powers 0 through 12 also checked directly.',
        fixture_banks_fixed=True,separating_bank_transforms=True,
        disposition='Left/right numerical updates are orthogonally conjugate with the active carrier and current sewing readout fixed. With transported adapter t_right=B*t_left they predict identical observed trajectories.',
        role_boundary='B changes numerical bank coordinates; it does not assert that source edges 01 and 12 may be executed in reverse order. Fixed untransported adapters remain different models. Original path labels and witnesses must stay retained.',
        physical_boundary='This removes this particular numerical ambiguity if the displayed bank-coordinate equivalence is admitted. It does not select the record port, metric, schedule, physical equivalence policy or gravity coefficients.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_cycle.py','checkers/check_four_packet_record_feedback.py',
            'checkers/check_record_return_selection.py','checkers/check_record_return_equivalence.py')})
    (ROOT/'results/record-return-equivalence.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
