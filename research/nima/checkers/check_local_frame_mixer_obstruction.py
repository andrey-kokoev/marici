"""Full-bank obstruction to an unframed, intermediate-port-natural mixer.

Four exact orthogonal frame changes suffice: their average is the readable
projector. The selected hidden port is their determinant-character sector.
This tests all invertible bank mixers via a general projector argument, not
just the previously considered one-factor lifts.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_four_packet_cycle import UNIT,E1,E2,J,matrix,tensor
from check_four_packet_record_feedback import basis,matrix_of,mm,transpose,rank,readout,left_rotate
from itertools import product
from check_tetrahedral_record_return import clifford_coefficients
ROOT=Path(__file__).resolve().parents[1]


def endpoint_frames(q0,q1,q2):
    cols=[]
    for v in basis(4):
        for u in basis(4):
            vv=clifford_coefficients(mm(mm(q2,matrix(v)),transpose(q1)))
            uu=clifford_coefficients(mm(mm(q1,matrix(u)),transpose(q0)))
            cols.append(tensor(vv,uu))
    return transpose(tuple(cols))


def determinant(q):return q[0][0]*q[1][1]-q[0][1]*q[1][0]


def intermediate_frame(q):
    # Bank order: V:1->2 tensor U:0->1.
    # Passive middle frame Q sends V to V Q^T and U to Q U.
    cols=[]
    for v in basis(4):
        for u in basis(4):
            vv=clifford_coefficients(mm(matrix(v),transpose(q)))
            uu=clifford_coefficients(mm(q,matrix(u)))
            cols.append(tensor(vv,uu))
    return transpose(tuple(cols))


def average(matrices,weights):
    return tuple(tuple(sum(w*M[i][j] for w,M in zip(weights,matrices))/len(matrices)
                       for j in range(16)) for i in range(16))


def main():
    I16=tuple(basis(16));I4=tuple(basis(4))
    C=tuple(zip(*(readout(v) for v in basis(16))))
    P=mm(transpose(C),C)
    assert mm(C,transpose(C))==I4
    qs=[matrix(v) for v in (UNIT,E1,E2,J)]
    determinants=[q[0][0]*q[1][1]-q[0][1]*q[1][0] for q in qs]
    assert determinants==[1,-1,-1,1]
    G=[intermediate_frame(q) for q in qs]
    for g in G:
        assert mm(transpose(g),g)==I16 and mm(C,g)==C
    assert average(G,[F(1)]*4)==P and rank(P)==4
    # So any K commuting with all G commutes with P. If C K C^T=0,
    # K C^T = P K C^T = C^T (C K C^T)=0, impossible for invertible K.
    L=matrix_of(left_rotate,16)
    D=average(G,determinants)
    assert mm(D,D)==D and rank(D)==4
    assert mm(P,D)==tuple((F(0),)*16 for _ in range(16))
    assert D==mm(mm(L,P),transpose(L))
    residual=tuple(tuple(I16[i][j]-P[i][j]-D[i][j] for j in range(16)) for i in range(16))
    assert mm(residual,residual)==residual and rank(residual)==8
    for sign,g in zip(determinants,G):
        assert mm(mm(g,L),transpose(g))==tuple(tuple(sign*x for x in row) for row in L)
        # Retaining orientation o allows an equivariant FAMILY L_o=o*L:
        # L_(det(Q)*o) = Gamma_Q L_o Gamma_Q^-1.
        for o in (F(1),F(-1)):
            Lo=tuple(tuple(o*x for x in row) for row in L)
            target=tuple(tuple(sign*o*x for x in row) for row in L)
            assert mm(mm(g,Lo),transpose(g))==target
    # With all endpoint frames independent the needed datum is RELATIVE:
    # o12 transforms by det(Q2)*det(Q1), not an absolute orientation.
    for q0,q1,q2 in product(qs,repeat=3):
        g=endpoint_frames(q0,q1,q2);sign=determinant(q2)*determinant(q1)
        assert mm(mm(g,L),transpose(g))==tuple(tuple(sign*x for x in row) for row in L)
    # The already retained invertible orthogonal edge V supplies such a datum
    # canonically: o12=det(V). No sign is selected from the metric alone.
    # On orthogonal edge actions this repair makes o12*R(V)=V.
    for v in qs:
        coeff=clifford_coefficients(v);o=determinant(v)
        adapted=tuple(o*x for x in clifford_coefficients(mm(mm(matrix(J),v),transpose(matrix(J)))))
        assert adapted==coeff
        for u in qs:
            t=tensor(coeff,clifford_coefficients(u))
            assert tuple(o*x for x in left_rotate(t))==t
    # An unframed metric supplies no fixed nonzero orientation under reflection.
    assert determinants[1]==-1
    assert all(determinants[1]*o!=o for o in (F(1),F(-1)))
    result=dict(schema='marici.nima.local-frame-mixer-obstruction.v1',status='pass',
        frame_action='Gamma_Q(V tensor U)=(V Q^T) tensor (Q U)',
        exact_average='(Gamma_I+Gamma_e1+Gamma_e2+Gamma_J)/4=C^T C',
        obstruction='Any invertible K natural under these independent middle-port frame changes preserves im(C^T), and therefore cannot satisfy C K C^T=0.',
        scope='All real-linear invertible 16D bank maps under the stated local O(2) policy, not only one-factor lifts.',
        sector_dimensions={'readable_trivial_character':4,'selected_hidden_determinant_character':4,'residual':8},
        hidden_projector='P_det=(sum det(Q)*Gamma_Q)/4=L P_readable L^T',
        mixer_transform='Gamma_Q L Gamma_Q^-1=det(Q)*L',
        minimal_repair='For independent endpoint frames retain relative orientation o12 transforming by det(Q2)*det(Q1); L_o=o12*L is covariant. The unpointed metric cannot select it, but a retained orthogonal edge V:1->2 supplies o12=det(V).',
        source_edge_repair='For orthogonal V, det(V)*Ad_J(V)=V, so this canonical self-orientation makes the hidden readout equal the ordinary readout on V tensor U. It removes the old ordinary/twisted sign distinction, not the retained histories.',
        independent_frame_assignments_checked=64,
        disposition='The common-frame selector cannot be promoted to an unframed independently local mixer. The missing reference has a concrete type: a relative orientation-line datum.',
        residual='The edge supplies a relative orientation without selecting an absolute physical frame, but the self-attached hidden readout carries no extra signal on the orthogonal two-edge source. Further evolution needs retained attachment data once the bank ceases to factor. Physical metric, matter readout and gravitational normalization remain open.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_cycle.py','checkers/check_four_packet_record_feedback.py',
            'checkers/check_local_frame_mixer_obstruction.py')})
    (ROOT/'results/local-frame-mixer-obstruction.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
