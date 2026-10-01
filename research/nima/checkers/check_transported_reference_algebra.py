"""Audit the two-frame 3+12 response interpretation of the triangle lift.

The embedding diag(S,1) and adjoint readout on sl4 are explicit trial adapters.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_triangle_half_phase import TwoPacket, cycle_from_packets, mm, mv, transpose, add, sub, scale
from check_four_packet_record_feedback import rank


def eye(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def power(a,n):
    r=eye(len(a))
    for _ in range(n): r=mm(a,r)
    return r

def unit(i,j): return tuple(tuple(F(a==i and b==j) for b in range(4)) for a in range(4))
H=tuple(sub(unit(i,i),unit(3,3)) for i in range(3))
PAIRS=tuple((i,j) for i in range(4) for j in range(4) if i!=j)
BASE=H+tuple(unit(i,j) for i,j in PAIRS)

def coordinates(m):
    assert sum(m[i][i] for i in range(4))==0
    return tuple(m[i][i] for i in range(3))+tuple(m[i][j] for i,j in PAIRS)

def adjoint_matrix(u):
    columns=tuple(coordinates(mm(mm(u,b),transpose(u))) for b in BASE)
    return transpose(columns)


def main():
    I3,I4,I15=eye(3),eye(4),eye(15)
    C=cycle_from_packets((TwoPacket('AB','A','B'),TwoPacket('BC','B','C'),TwoPacket('CA','C','A')))
    Q=scale(add(add(I3,C),mm(C,C)),F(1,3));P=sub(I3,Q)
    S=add(add(Q,scale(P,F(1,2))),scale(sub(C,transpose(C)),F(1,2)))
    u=tuple(tuple(S[i][j] if i<3 and j<3 else F(i==j) for j in range(4)) for i in range(4))
    assert mm(mm(u,I4),transpose(u))==I4 # Algebra unit never moves.
    # Endpoint-potential bridge for the actual ABC triangle.
    # B maps four state values to (x_B-x_A,x_C-x_B,x_A-x_C).
    B=tuple(tuple(F(j==v)-F(j==w) for j in range(4))
            for w,v in ((0,1),(1,2),(2,0)))
    assert rank(B)==2
    assert mm(B,u)==mm(S,B)
    # The kernel consists of the triangle constant and the spectator D.
    k1=(F(1),F(1),F(1),F(0)); k2=(F(0),F(0),F(0),F(1))
    assert mv(u,k1)==k1 and mv(u,k2)==k2
    assert mm(transpose(u),u)==I4
    # Fixing the kernel covectors (triangle total and spectator value) makes
    # the intertwining lift unique, since these stacked constraints have rank4.
    lift_constraints=B+(k1,k2)
    assert rank(lift_constraints)==4
    assert mm(lift_constraints,u)==mm(S,B)+(k1,k2)
    # It also induces an exact reversible operation on all seed gradient data.
    seed=((0,1),(1,2),(2,0),(0,3),(3,1),(1,0))
    incidence=tuple(tuple(F(j==v)-F(j==w) for j in range(4)) for w,v in seed)
    assert rank(incidence)==3 and power(u,6)==I4
    # A connected seed loses only the common potential; u fixes it.
    assert mv(u,(F(1),)*4)==(F(1),)*4
    assert mm(incidence,power(u,6))==incidence
    # Arbitrary directed packet values include three independent cycle sums.
    cycle_rows=((F(1),F(1),F(1),F(0),F(0),F(0)),
                (F(0),F(0),F(0),F(1),F(1),F(1)),
                (F(1),F(0),F(0),F(0),F(0),F(1)))
    assert rank(cycle_rows)==3
    assert mm(cycle_rows,incidence)==tuple((F(0),)*4 for _ in range(3))
    # Extend the SAME triangle step to arbitrary six-arrow values by exact
    # endpoint increments. This freezes the cycle sums without erasing them.
    I6=eye(6)
    local=tuple(I6[i] for i in range(3))
    change=sub(mm(S,local),local)
    da=tuple(-(2*change[0][j]+change[1][j])/3 for j in range(6))
    db=tuple(da[j]+change[0][j] for j in range(6))
    dc=tuple(db[j]+change[1][j] for j in range(6))
    W=(da,db,dc,(F(0),)*6)
    assert all(da[j]+db[j]+dc[j]==0 for j in range(6))
    full=add(I6,mm(incidence,W))
    assert mm(local,full)==mm(S,local)
    assert mm(cycle_rows,full)==cycle_rows
    assert mm(full,incidence)==mm(incidence,u)
    assert power(full,6)==I6
    assert all(power(full,k)!=I6 for k in range(1,6))
    assert mm(power(full,5),full)==I6
    # Positive invariant metric by full-orbit averaging; not claimed physical.
    metric=tuple(tuple(sum(mm(transpose(power(full,k)),power(full,k))[i][j]
                           for k in range(6)) for j in range(6)) for i in range(6))
    assert mm(mm(transpose(full),metric),full)==metric
    # Positive definiteness follows since the k=0 summand is I, others PSD.
    assert rank(metric)==6
    # Nonzero circulation is retained, rather than projected to a gradient.
    sample=(F(1),F(2),F(4),F(8),F(16),F(32))
    assert mv(cycle_rows,sample)==(F(7),F(56),F(33))
    assert mv(cycle_rows,mv(full,sample))==mv(cycle_rows,sample)
    T=adjoint_matrix(u);Ti=adjoint_matrix(transpose(u))
    assert mm(T,Ti)==I15
    D=tuple(tuple(F(i==j and i<3) for j in range(15)) for i in range(15))
    Gamma=sub(scale(D,2),I15)
    D1=mm(mm(T,D),Ti);Gamma1=sub(scale(D1,2),I15)
    assert Gamma1!=Gamma and mm(Gamma1,Gamma1)==I15
    assert mm(mm(T,Gamma1),Ti)==Gamma
    assert mm(power(T,2),Gamma)==mm(Gamma,power(T,2))
    assert power(T,2)!=I15 and power(T,6)==I15
    assert all(power(T,n)!=I15 for n in range(1,6))
    assert power(power(T,2),3)==I15
    # Return of the decomposition carries nontrivial order-three transport.
    before=coordinates(H[0]);after=mv(power(T,2),before)
    assert before!=after and not any(after[3:])
    # Frobenius principal-angle compression of the diagonal sector.
    compression=mm(mm(D,D1),D)
    expected=add(Q,scale(P,F(1,9)))
    assert tuple(tuple(compression[i][j] for j in range(3)) for i in range(3))==expected
    assert rank(D)+rank(D1)-rank(tuple(a+b for a,b in zip(D,D1)))==1
    assert 15-rank(D+D1)==10
    # A0 is all block-preserving endomorphisms, dimension 3²+12².
    allowed=tuple((i,j) for i in range(15) for j in range(15) if (i<3)==(j<3))
    assert len(allowed)==153
    # Endomorphisms preserving both frames commute with both gradings.
    rows=[[F(0)]*153 for _ in range(225)]
    for column,(a,b) in enumerate(allowed):
        for j in range(15): rows[15*a+j][column]+=Gamma1[b][j]
        for i in range(15): rows[15*i+b][column]-=Gamma1[i][a]
    common_dimension=153-rank(rows)
    assert common_dimension==105
    # Adding transported grading to A0 generates all mixed matrix units:
    # E_ia Gamma1 E_bj = Gamma1[a,b] E_ij within the selected source/target blocks.
    forward=next((a,b) for a in range(3) for b in range(3,15) if Gamma1[a][b])
    backward=next((a,b) for a in range(3,15) for b in range(3) if Gamma1[a][b])
    for a,b in (forward,backward):
        source=range(3) if a<3 else range(3,15)
        target=range(3) if b<3 else range(3,15)
        for i in source:
            for j in target:
                assert (i,a) in allowed and (b,j) in allowed and Gamma1[a][b]!=0
    report={'status':'passed','adapter':'diag(triangle short root S,1), conjugation on real sl4',
            'endpoint_bridge':{'triangle_incidence_rank':2,'seed_gradient_rank':3,
                               'intertwining_Bu_equals_SB':True,
                               'unique_given_triangle_total_and_spectator_preservation':True,
                               'independent_seed_cycle_coordinates':3},
            'cycle_retaining_extension':{'dimension':6,'fixed_cycle_sums':3,
                                         'exact_order':6,'triangle_update_preserved':True,
                                         'gradient_restriction_matches_u':True,
                                         'matrix':[[str(x) for x in row] for row in full],
                                         'policy':'exact endpoint increment; triangle-total increment zero; spectator increment zero'},
            'unit':'fixed I4','moving_object':'traceless diagonal reference sector and its off-diagonal complement',
            'frame_period':2,'within_frame_return_order':3,'labelled_operator_period':6,
            'frame_response_dimension':153,'mixed_response_dimension':72,
            'responses_preserving_both_frames':common_dimension,
            'algebra_generated_by_both_frame_algebras':225,
            'reference_principal_cosines':['1','1/3','1/3'],
            'reference_common_dimension':1,'relationship_common_dimension':10,
            'scope':'Exact finite conjugation model; not an identification with native packet maps or a physical response algebra.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'transported-reference-algebra.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: full six-arrow extension preserves three arbitrary cycle sums and has exact order six.')
    print('PASS: endpoint-gradient intertwiner; unique lift with preserved triangle total and spectator; cycle-data control.')
    print('PASS: two-frame return with order-three holonomy, fixed unit, reference-plane cosine 1/3, response dimensions 153 / 105 / 225.')

if __name__=='__main__': main()
