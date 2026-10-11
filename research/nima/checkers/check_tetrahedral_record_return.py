"""Exact fixture adapter from proved Boolean edge actions to prior record return.

The ordered port is (edge12, edge01), so sewing reads their composition.
This is a declared adapter, not a uniquely selected physical interaction.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_four_packet_cycle import UNIT, E2, tensor, matrix, sew
from check_four_packet_record_feedback import readout, cycle, inverse_cycle, budget

ROOT = Path(__file__).resolve().parents[1]


def permutation_matrix(truth):
    # Counting basis ordered false, true; columns are input basis states.
    return tuple(tuple(F(truth[j] == i) for j in range(2)) for i in range(2))


def clifford_coefficients(m):
    a,b=m[0]; c,d=m[1]
    return ((a+d)/2, (a-d)/2, (b+c)/2, (b-c)/2)


def main():
    proof=ROOT/'agda/TetrahedralEdgeReadout.agda'
    receipt=json.loads((ROOT/'results/agda-TetrahedralEdgeReadout.json').read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['inputs_stable_during_check'] and receipt['ignore_interfaces']
    assert receipt['source_sha256']==hashlib.sha256(proof.read_bytes()).hexdigest()
    # These tables are the explicit interface contract proved for all Bool
    # inputs by ordinary01/12 and twisted01/12. This is not Agda code extraction.
    identity=(0,1); flip=(1,0)
    I=clifford_coefficients(permutation_matrix(identity))
    X=clifford_coefficients(permutation_matrix(flip))
    assert I==UNIT and X==E2
    assert matrix(I)==permutation_matrix(identity) and matrix(X)==permutation_matrix(flip)
    t0=tensor(I,I);t1=tensor(X,X)
    assert t0!=t1 and sew(t0)==sew(t1)==UNIT
    assert readout(t0)==readout(t1)==tuple(v/2 for v in UNIT)
    x=UNIT
    out0=cycle(x,t0);out1=cycle(x,t1)
    assert out0[0]==tuple(v/2 for v in UNIT)
    assert out1[0]==tuple(-v/2 for v in UNIT)
    assert out0[0]!=out1[0]
    assert budget(x,t0)==budget(x,t1)==F(2)
    for t,out in ((t0,out0),(t1,out1)):
        assert budget(*out)==budget(x,t)
        assert inverse_cycle(*out)==(x,t)
    # Collapsing the record to its sewn product would erase this prediction.
    assert sew(t0)==sew(t1) and cycle(x,t0)[0]!=cycle(x,t1)[0]
    dependencies=('checkers/check_four_packet_cycle.py','checkers/check_four_packet_record_feedback.py',
                  'agda/TetrahedralEdgeReadout.agda','agda/RetainedTetrahedralPackage.agda',
                  'agda/MarkedTetrahedronCoherence.agda','agda/GradedBoundaryCoherence.agda')
    result=dict(schema='marici.nima.tetrahedral-record-return.v1',status='pass',
        source_packages=['RetainedTetrahedralPackage.LossyDiagonal.ordinary','RetainedTetrahedralPackage.LossyDiagonal.twisted'],
        proof_receipt='results/agda-TetrahedralEdgeReadout.json',
        adapter='Boolean edge transport -> counting-basis permutation matrix -> existing Cl(2,0) coefficients -> edge12 tensor edge01 record bank',
        initial_carrier=[str(v) for v in x],
        shared_initial_readout=[str(v) for v in readout(t0)],
        ordinary_next_carrier=[str(v) for v in out0[0]],
        twisted_next_carrier=[str(v) for v in out1[0]],
        shared_total_budget='2',inverse_recovery=True,
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        disposition='Same marked vertex, diagonal, composed edge action, initial numerical carrier, initial sewn record readout and total budget; different next carrier under the unchanged prior update.',
        limits='New declared two-edge port adapter and reused supplied numerical law. Not an encoding of all tetrahedral witnesses or a uniquely sourced physical coupling. Boolean proof contract is checked separately from exact Python arithmetic, not extracted Agda execution. Source packages must remain retained separately from this lossy observation.')
    (ROOT/'results/tetrahedral-record-return.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
