"""Bind the prior controlled return to completion of the actual seed cycle.

The unique cycle cover selects routing under its declared criterion. The
choice 'flip reference A and exchange on return to the marked root' remains
an explicit coupling hypothesis, not a consequence of cycle-cover uniqueness.
"""
from itertools import product,permutations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_natural_tower_return import PACKETS,LABELS
from check_four_packet_cycle import UNIT,E2,tensor,MAX_DEPTH
from check_four_packet_record_feedback import basis,budget
from check_reference_controlled_return import step as response,undo as undo_response
ROOT=Path(__file__).resolve().parents[1]


def cycle_cover(packets,labels):
    fibers=[tuple(p for p in packets if p[1]==v) for v in labels]
    covers=[choice for choice in product(*fibers) if len({p[2] for p in choice})==len(labels)]
    assert len(covers)==1
    return {s:(name,t) for name,s,t in covers[0]}


def main():
    routing=cycle_cover(PACKETS,LABELS)
    assert set(name for name,t in routing.values())=={'AD','DB','BC','CA'}
    root='A';inverse={t:s for s,(name,t) in routing.items()}

    def step(state):
        vertex,a,b,v=state;occ,target=routing[vertex]
        if target==root:a,b,v=response(a,b,v,'A')
        return (target,a,b,v),occ,(target==root)

    def undo(state):
        vertex,a,b,v=state
        if vertex==root:a,b,v=undo_response(a,b,v,'A')
        return inverse[vertex],a,b,v

    for vertex in LABELS:
        for a,b in product((F(1),F(-1)),repeat=2):
            for v in basis(20):
                state=(vertex,a,b,v);new,occ,event=step(state)
                assert undo(new)==state
                assert budget(v[:4],v[4:])==budget(new[3][:4],new[3][4:])
    # Trigger derives from the pointed cycle, not the spelling of the labels.
    for perm in permutations(LABELS):
        rename=dict(zip(LABELS,perm))
        pp=tuple((name,rename[s],rename[t]) for name,s,t in PACKETS)
        rr=cycle_cover(pp,perm);here=rename[root]
        flags=[]
        for _ in range(4):
            _,here=rr[here];flags.append(here==rename[root])
        assert flags==[False,False,False,True]
    histories=[]
    for t in (tensor(UNIT,UNIT),tensor(E2,E2)):
        state=(root,F(1),F(1),UNIT+t);initial=state
        parents=[];occurrences=[];events=0;direct=(F(1),F(1),UNIT+t)
        for _ in range(4*MAX_DEPTH):
            parents.append(state);state,occ,event=step(state)
            occurrences.append(occ)
            if event:
                events+=1;direct=response(*direct,'A')
                assert state[1:]==direct
                assert events<=MAX_DEPTH
        assert events==MAX_DEPTH==3
        assert occurrences==['AD','DB','BC','CA']*3
        for prior in reversed(parents):
            state=undo(state);assert state==prior
        assert state==initial
        histories.append(dict(primitive_traversals=len(occurrences),response_events=events,
                              occurrences=occurrences,reverse_recovery=True))
    result=dict(schema='marici.nima.seed-return-trigger.v1',status='pass',
        routing='unique one-in/one-out seed cover A->D->B->C->A',
        coupling_hypothesis='On completing a return to the marked root, flip reference A then apply the prior controlled exchange. No body operation is assigned to intermediate edge traversals.',
        trigger_word=[False,False,False,True],all_vertex_relabellings_checked=24,
        all_controller_phases_and_reference_signs_inverse_checked=True,
        histories=histories,
        disposition='The trigger is computed from retained cycle completion rather than supplied as an independent event stream. Routing selection and return triggering are explicit; the choice of what response to execute at that trigger remains a declared coupling.',
        limits='This is a discrete autonomous controller once the cover criterion, mark and on-return action are supplied. It is not a WG-derived physical clock, edge-payload dynamics or gravitational law. Only three body advances are traced; no old history bound is bypassed. Nonselected primitive rows AB/BA remain retained in the original source.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_natural_tower_return.py','checkers/check_reference_controlled_return.py',
            'seed-endpoint-sections-and-unique-return-cycle.md','checkers/check_seed_return_trigger.py')})
    (ROOT/'results/seed-return-trigger.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
