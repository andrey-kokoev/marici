"""Two three-packet triangles sharing one oriented edge: exact seam tests.

Independent simultaneous, ordered serial, and synchronized mirrored protocols
are kept separate. No geometric 3D embedding or physical identification.
"""
from fractions import Fraction as F
from math import acos, sqrt, pi
from pathlib import Path
import json
from check_triangle_half_phase import TwoPacket, cycle_from_packets, transpose, mm, mv, add, sub, scale, norm2
from check_four_packet_record_feedback import rank


def identity(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def power(a,n):
    out=identity(len(a))
    for _ in range(n): out=mm(a,out)
    return out

def tr(a): return sum(a[i][i] for i in range(len(a)))
def matjson(a): return [[str(v) for v in row] for row in a]

def characteristic(a):
    traces=[tr(power(a,k)) for k in range(1,len(a)+1)]
    c=[F(1)]
    for k in range(1,len(a)+1):
        c.append(-sum(c[k-i]*traces[i-1] for i in range(1,k+1))/k)
    return tuple(c)

def main():
    left=(TwoPacket('AB','A','B'),TwoPacket('BC','B','C'),TwoPacket('CA','C','A'))
    right=(TwoPacket('BA','B','A'),TwoPacket('AD','A','D'),TwoPacket('DB','D','B'))
    C=cycle_from_packets(left)
    assert cycle_from_packets(right)==C
    assert len({frozenset((p.source,p.target)) for p in left+right})==5
    assert len({p.label for p in left+right})==6
    assert len({p.source for p in left+right})==4
    I3,I5=identity(3),identity(5)
    Q=scale(add(add(I3,C),mm(C,C)),F(1,3));P=sub(I3,Q)
    S=add(add(Q,scale(P,F(1,2))),scale(sub(C,transpose(C)),F(1,2)))
    # Cochain coordinates (AB,BC,CA,AD,DB); BA is the negative reading of AB.
    R1=(I5[0],I5[1],I5[2]);R2=(tuple(-v for v in I5[0]),I5[3],I5[4])
    assert mm(R1,transpose(R1))==I3 and mm(R2,transpose(R2))==I3
    def embed(T,R): return add(I5,mm(mm(transpose(R),sub(T,I3)),R))
    C1,C2=embed(C,R1),embed(C,R2)
    S1,S2=embed(S,R1),embed(S,R2)
    common=(F(1),F(1),F(1),F(-1),F(-1))
    for T in (C1,C2,S1,S2):
        assert mm(transpose(T),T)==I5 and mv(T,common)==common
    assert mm(S1,S1)==C1 and mm(S2,S2)==C2
    plane1=mm(mm(transpose(R1),P),R1);plane2=mm(mm(transpose(R2),P),R2)
    assert tr(mm(plane1,plane2))==F(4,9)
    assert mm(plane1,plane2)!=mm(plane2,plane1)
    assert power(S1,6)==I5 and power(S2,6)==I5
    joint_constraints=sub(C1,I5)+sub(C2,I5)
    assert 5-rank(joint_constraints)==1
    # Independent local updates propose incompatible values for the common edge.
    witness=I5[1]
    left_local=mv(C,mv(R1,witness));right_local=mv(C,mv(R2,witness))
    assert left_local[0]==1 and -right_local[0]==0
    left_half=mv(S,mv(R1,witness));right_half=mv(S,mv(R2,witness))
    assert left_half[0]==F(2,3) and -right_half[0]==0
    assert mm(C2,C1)!=mm(C1,C2) and mm(S2,S1)!=mm(S1,S2)
    # Protocol A: serial whole triangle cycles.
    G=mm(C2,C1)
    assert all(power(G,k)!=I5 for k in range(1,5)) and power(G,5)==I5
    assert characteristic(G)==(1,0,0,0,0,-1)
    # Protocol B: serial local short-half-phase operators.
    U=mm(S2,S1)
    assert mm(transpose(U),U)==I5 and mm(U,U)!=G
    assert characteristic(U)==(F(1),F(-28,9),F(44,9),F(-44,9),F(28,9),F(-1))
    assert tr(U)==F(28,9) and tr(U).denominator!=1
    # Exact theorem: a rational finite-order matrix has integer trace.
    # Nonintegral trace therefore proves U has infinite order, not just long period.
    assert 5-rank(sub(U,I5))==1
    # Nontrivial eigenpairs have cosines (19 +/- sqrt(109))/36.
    cosine_sum=F(19,18);cosine_product=F(7,36)
    assert -2*cosine_sum==F(-19,9) and 2+4*cosine_product==F(25,9)
    # Alternate protocol: synchronize on the mirror-compatible 3D subspace.
    K=((F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)),
       (F(0),F(-1),F(0)),(F(0),F(0),F(-1)))
    assert mm(R1,K)==I3 and mm(R2,K)==scale(I3,-1)
    seam_rows=[]
    for T in (C,mm(C,C),S):
        row=tuple(a+b for a,b in zip(mm(T,R1)[0],mm(T,R2)[0]))
        seam_rows.append(row)
        assert mv((row,),mv(K,(F(2),F(3),F(5))))==(0,)
    assert seam_rows[:2]==[(F(0),F(1),F(0),F(1),F(0)),(F(0),F(0),F(1),F(0),F(1))]
    assert rank(tuple(seam_rows))==2
    # Both local outputs are compatible for any shared 3-vector and T=C or S.
    for T in (C,S):
        assert mm(T,mm(R1,K))==mm(R1,mm(K,T))
        assert mm(T,mm(R2,K))==mm(R2,mm(K,T))
    M=add(mm(transpose(R1),R1),mm(transpose(R2),R2))
    assert M==tuple(tuple(F((2 if i==0 else 1)*(i==j)) for j in range(5)) for i in range(5))
    assert mm(mm(transpose(K),M),K)==scale(I3,2)
    assert mm(transpose(K),K)==((1,0,0),(0,2,0),(0,0,2))
    for T in (C,S):
        x=mv(K,I3[0]);y=mv(K,mv(T,I3[0]))
        assert sum(a*b for a,b in zip(x,mv(M,x)))==sum(a*b for a,b in zip(y,mv(M,y)))
    assert norm2(mv(K,I3[0]))==1 and norm2(mv(K,mv(C,I3[0])))==2
    # Orientation-gauge change cannot change serial spectral conclusions.
    flip=tuple(tuple(F((-1 if i==0 else 1)*(i==j)) for j in range(5)) for i in range(5))
    Uflip=mm(mm(flip,U),flip)
    assert characteristic(Uflip)==characteristic(U)
    report={'status':'passed','primitive':{'left':[p.__dict__ for p in left],'right':[p.__dict__ for p in right]},
            'vertices':4,'undirected_edges':5,'directed_triangle_occurrences':6,
            'coefficient_coordinates':['AB','BC','CA','AD','DB'],'shared_edge_convention':'BA=-AB',
            'common_fixed_line':[str(v) for v in common],
            'triangle_plane_overlap_trace':'4/9','triangle_plane_projectors_commute':False,
            'simultaneous_counterexample':{'input':list(witness),'left_AB':str(left_local[0]),'right_AB':str(-right_local[0])},
            'serial_full':{'matrix':matjson(G),'order':5,'characteristic_polynomial_descending':['1','0','0','0','0','-1']},
            'serial_half':{'matrix':matjson(U),'trace':str(tr(U)),'order':'infinite',
                           'characteristic_polynomial_descending':[str(v) for v in characteristic(U)],
                           'cosines':'(19 +/- sqrt(109))/36',
                           'angles_degrees_illustrative':[acos((19+s*sqrt(109))/36)*180/pi for s in (1,-1)],
                           'is_square_root_of_serial_full':False},
            'synchronized_mirror':{'constraints':['AD=-BC','DB=-CA'],
                                   'full_period':3,'half_period':6,
                                   'metric':'counts both occurrences of shared edge: diag(2,1,1,1,1)'},
            'scope':'Serial order, synchronization constraint and coefficient metric are distinct declared protocols. No tetrahedral filling, spatial dimension or proton prediction.'}
    # Keep all stored exact coefficients textual, including the counterexample.
    report['simultaneous_counterexample']['input']=[str(v) for v in witness]
    dest=Path(__file__).resolve().parents[1]/'results'/'two-triangle-half-phase.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: shared-edge compatibility, one common fixed mode, serial full period 5, serial half infinite order, synchronized period 3/6 with explicit metric.')

if __name__=='__main__': main()
