"""Exact local-frame audit of the existing two-edge hidden-readout adapter.

This tests a candidate frame-equivalence policy, not its physical admission.
It retains the closing diagonal and transports the inserted J operators.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import hashlib
from check_four_packet_cycle import UNIT,E2,J,matrix,tensor
from check_four_packet_record_feedback import readout,left_rotate,mm,transpose
ROOT=Path(__file__).resolve().parents[1]
I=matrix(UNIT);X=matrix(E2);j=matrix(J)


def mul(*factors):
    out=I
    for f in factors:out=mm(out,f)
    return out


def half(m):return tuple(tuple(v/2 for v in row) for row in m)


def negative(m):return tuple(tuple(-v for v in row) for row in m)


def main():
    assert mul(X,X)==I and mul(X,j,X)==negative(j)
    # Existing ordinary edges are identity. Twist the frame at vertex 1.
    g=(I,X,I,I)
    edges={(a,b):mul(g[b],transpose(g[a])) for a,b in ((0,1),(1,2),(0,2),(2,3),(1,3),(0,3))}
    assert edges=={(0,1):X,(1,2):X,(0,2):I,(2,3):I,(1,3):X,(0,3):I}
    # Exactly matches all six stored twisted-edge actions, not merely two.
    baseline=half(I);frozen_failures=0;covariant_checks=0
    for bits in product((0,1),repeat=4):
        G=tuple(X if b else I for b in bits)
        u=mul(G[1],transpose(G[0])) # 01
        v=mul(G[2],transpose(G[1])) # 12
        d=mul(G[2],transpose(G[0])) # 02 closing diagonal
        assert mul(v,u)==d
        ordinary_closed=half(mul(transpose(d),v,u))
        assert ordinary_closed==baseline
        frozen=half(mul(transpose(d),j,v,transpose(j),u))
        j1=mul(G[1],j,transpose(G[1]))
        j2=mul(G[2],j,transpose(G[2]))
        transported=half(mul(transpose(d),j2,v,transpose(j1),u))
        expected=mul(G[0],baseline,transpose(G[0]))
        assert transported==expected
        covariant_checks+=1
        if frozen!=expected:frozen_failures+=1
    assert covariant_checks==16 and frozen_failures==8
    # The previously reported +/- response is recovered with a frozen J.
    old_ordinary=matrix(readout(left_rotate(tensor(UNIT,UNIT))))
    old_twisted=matrix(readout(left_rotate(tensor(E2,E2))))
    assert old_ordinary==baseline and old_twisted==negative(baseline)
    # Correct transport for the vertex-1 change uses J1'=-J, J2'=J.
    transported_twisted=half(mul(j,X,transpose(negative(j)),X))
    assert transported_twisted==baseline
    result=dict(schema='marici.nima.tetrahedral-hidden-readout-frames.v1',status='pass',
        source_frame_change='G1=Boolean flip; G0=G2=G3=identity',
        six_edge_action_match=True,
        closed_hidden_readout='b0(P;J1,J2)=1/2 * d02^-1 * J2 * u12 * J1^-1 * u01',
        frame_rule='uij -> Gj uij Gi^-1; Ji -> Gi Ji Gi^-1',
        closed_covariance='b0 -> G0 b0 G0^-1',
        checked_frame_assignments=covariant_checks,frozen_frame_failures=frozen_failures,
        original_frozen_outputs=['+I/2','-I/2'],transported_outputs=['+I/2','+I/2'],
        disposition='The earlier sign distinction is not invariant under this local Boolean frame-change policy if the inserted J operators are transported with the edges. It remains a distinction when those J references are physically held fixed.',
        limits='Exact edge-action and readout audit, not a proved equivalence of complete Agda tetrahedral fillers or a declaration that all local frame changes are physical gauge. The diagonal closes the numerical port at vertex 0; it does not derive a four-cycle physical law. A source-selected frame/reference policy is required.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'agda/MarkedTetrahedronCoherence.agda','agda/TetrahedralEdgeReadout.agda',
            'checkers/check_four_packet_cycle.py','checkers/check_tetrahedral_hidden_readout_frames.py')})
    (ROOT/'results/tetrahedral-hidden-readout-frames.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
