"""C7: positive rank-four target cannot fit a fixed-energy three-channel fiber."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from check_three_port_completeness import audit as completeness_audit

ROOT=Path(__file__).resolve().parents[3];HOME=ROOT/'research/scattering/low-energy'
PROOF=HOME/'CHANNEL-RANK-OBSTRUCTION.md';RESULT=HOME/'results/channel-rank.v1.json'


def audit():
    completeness=completeness_audit()
    assert completeness==json.loads((HOME/'results/three-port-completeness.v1.json').read_text(encoding='utf-8'))
    source=json.loads((HOME/'contracts/low-energy-scattering-conjectures.v4.json').read_text(encoding='utf-8'))
    G=[[Q(x) for x in row] for row in source['models']['glued_one_step']['G_gamma']]
    assert G==[[Q(3),Q(0)],[Q(0),Q(1)]]
    H=[[x*y for x in a for y in b] for a in G for b in G]
    diagonal=[H[i][i] for i in range(4)]
    assert diagonal==[9,3,3,1] and all(H[i][j]==0 for i in range(4) for j in range(4) if i!=j)
    determinant=Q(1)
    for d in diagonal:assert d>0;determinant*=d
    assert determinant==81 and min(diagonal)==1
    sources=set(completeness['source_sha256'])|{
        PROOF.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix(),
        'research/scattering/low-energy/results/three-port-completeness.v1.json',
        'research/nima/photon-two-packet-construction.md'}
    # The target's exact value is checked above; omit the mutable whole net hash
    # so the mathematical certificate need not depend on its own status update.
    return {'schema':'marici.scattering.channel-rank.v1','status':'pass','C7_disposition':'established',
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)},
            'target_metric':[[str(x) for x in row] for row in H],'target_determinant':str(determinant),
            'target_rank':4,'target_metric_lower_bound':1,'outgoing_fiber_rank':3,
            'scope':'Almost every fixed E in (0,4), single-excitation fiber, full positive target metric.',
            'C2_source_inputs_replayed':True,'C3_or_C8_existence_used':False,
            'whole_Hilbert_space_embedding_excluded':False,'physical_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale C7 certificate'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: C7 fixed-energy rank obstruction: positive target rank 4 > outgoing fiber rank 3.')


if __name__=='__main__':main()
