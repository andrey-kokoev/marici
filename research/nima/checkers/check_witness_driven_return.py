"""Prepared witness comparison drives reference control at the seed return.

The question and coupling policy are explicit; no external flip-bit stream is
needed once they and the source package are fixed. Not a physical derivation.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
from check_natural_tower_return import PACKETS,LABELS
from check_seed_return_trigger import cycle_cover
from check_four_packet_cycle import UNIT,E2,tensor,MAX_DEPTH
from check_four_packet_record_feedback import basis,budget
from check_reference_controlled_return import step as response,undo as undo_response
ROOT=Path(__file__).resolve().parents[1]


def control(edge_flip,probe,reference):return edge_flip ^ probe ^ reference


def main():
    proof=ROOT/'agda/TetrahedralWitnessControl.agda'
    receipt=json.loads((ROOT/'results/agda-TetrahedralWitnessControl.json').read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['inputs_stable_during_check'] and receipt['ignore_interfaces']
    assert receipt['source_sha256']==hashlib.sha256(proof.read_bytes()).hexdigest()
    # The Boolean function is the explicit finite contract in the Agda source.
    covariance=0
    for e,p,r,g0,g1 in product((0,1),repeat=5):
        assert control(e,p,r)==control(g1^e^g0,p^g0,r^g1)
        covariance+=1
    route=cycle_cover(PACKETS,LABELS);previous={t:s for s,(occ,t) in route.items()}
    root='A';reports=[]
    for name,e,t in (('ordinary',0,tensor(UNIT,UNIT)),('twisted',1,tensor(E2,E2))):
        probe=reference=0
        event='A' if control(e,probe,reference) else 'none'
        def advance(state):
            vertex,a,b,v=state;occ,target=route[vertex]
            if target==root:a,b,v=response(a,b,v,event)
            return (target,a,b,v),occ
        def undo(state):
            vertex,a,b,v=state
            if vertex==root:a,b,v=undo_response(a,b,v,event)
            return previous[vertex],a,b,v
        for vertex,a,b in product(LABELS,(F(1),F(-1)),(F(1),F(-1))):
            for v in basis(20):
                s=(vertex,a,b,v);n,_=advance(s)
                assert undo(n)==s and budget(n[3][:4],n[3][4:])==budget(v[:4],v[4:])
        initial=(root,F(1),F(1),UNIT+t);state=initial;parents=[];word=[];carriers=[]
        for _ in range(4*MAX_DEPTH):
            parents.append(state);state,occ=advance(state);word.append(occ)
            if state[0]==root:carriers.append(state[3][:4])
        assert len(carriers)==3 and word==['AD','DB','BC','CA']*3
        for parent in reversed(parents):
            state=undo(state);assert state==parent
        assert state==initial
        reports.append(dict(package=name,prepared_probe=probe,target_reference=reference,
                            witness_control=bool(control(e,probe,reference)),
                            reference_action=event,return_carriers=[[str(v) for v in x] for x in carriers],
                            primitive_history=word,inverse_recovery=True))
    assert reports[0]['return_carriers'][0]==reports[1]['return_carriers'][0]
    assert reports[0]['return_carriers'][1]!=reports[1]['return_carriers'][1]
    result=dict(schema='marici.nima.witness-driven-return.v1',status='pass',
        proof_receipt='results/agda-TetrahedralWitnessControl.json',
        selector='Compare transport along the retained first edge on a prepared source probe with the prepared target reference; flip the first reference iff they disagree.',
        selector_covariance_checks=covariance,fixtures=reports,
        disposition='The retained witness answers a prepared comparison question, and its answer controls the existing reference/exchange operation at cycle completion. The flip stream is computed from retained input rather than supplied independently. The complete source package is retained by the formal question/answer constructor.',
        limits='The probe/reference preparation, selected edge, cycle-cover criterion and policy mapping disagreement to reference conjugation remain explicit choices. This does not establish their unique WG selection, full coupled-model frame covariance, a physical clock or G. Numeric verification uses a proved finite contract, not extracted Agda execution.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'agda/TetrahedralWitnessControl.agda','checkers/check_reference_controlled_return.py',
            'checkers/check_seed_return_trigger.py','checkers/check_witness_driven_return.py')})
    (ROOT/'results/witness-driven-return.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
