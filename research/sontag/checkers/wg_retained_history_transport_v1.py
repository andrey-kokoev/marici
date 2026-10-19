"""Finite transcription of ProofDependentFixture; not an Agda proof checker."""
import itertools
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]

def flatten(x): return (x[0][0],x[0][1],x[1])
def unflatten(x): return ((x[0],x[1]),x[2])
def generated_flat(x):
    s,p,q=x
    return (not s,not p,not q), (True,p,True)
def generated_nested(x):
    (s,p),q=x
    return ((not s,not p),not q), ((True,p),True)
def edge_flat(w): return ((w[0][0],w[0][1],w[1]))
def valid_flat(x,y,w):
    # Bool stands for the fixture's base equality and second-layer equality
    # certificates. Validation checks the propositions, not arbitrary proofs.
    s,p,q=x
    t,p2,q2=y
    r,e,f=w
    return r is True and t == (not s) and f is True and e == p

def run_flat(x,n):
    records=[]
    for _ in range(n):
        y,w=generated_flat(x)
        if not valid_flat(x,y,w): raise ValueError('invalid fixture edge')
        records.append((x,y,w)); x=y
    return x,records

def run_nested(x,n):
    records=[]
    for _ in range(n):
        y,w=generated_nested(x)
        records.append((x,y,w)); x=y
    return x,records

states=list(itertools.product((False,True),repeat=3))
checks={}
checks['state_roundtrips']=all(flatten(unflatten(x))==x for x in states)
checks['generated_state_and_witness_square']=all(
    (flatten(generated_nested(unflatten(x))[0]),edge_flat(generated_nested(unflatten(x))[1]))==generated_flat(x)
    for x in states)
checks['all_generated_edges_admitted']=all(valid_flat(x,*generated_flat(x)) for x in states)
checks['finite_history_replay_and_payloads']=all(
    flatten(run_nested(unflatten(x),n)[0])==run_flat(x,n)[0] and
    [(flatten(a),flatten(b),edge_flat(w)) for a,b,w in run_nested(unflatten(x),n)[1]]==run_flat(x,n)[1]
    for x in states for n in range(9))
checks['concatenation_replay']=all(
    run_flat(run_flat(x,m)[0],n)[0]==run_flat(x,m+n)[0]
    for x in states for m,n in itertools.product(range(5),repeat=2))
x=(False,True,False)
y,w=generated_flat(x)
checks['source_wrong_payload_rejected']=not valid_flat(x,y,(w[0],False,w[2]))
checks['same_endpoint_does_not_repair_payload']=valid_flat(x,y,w) and not valid_flat(x,y,(True,False,True))
# An observer selecting the actual first extra payload sees the difference.
checks['payload_observer_transport']=all(
    generated_nested(unflatten(x))[1][0][1]==generated_flat(x)[1][1] for x in states)
out={'schema':'marici.sontag.wg-retained-history-transport.v1',
     'scope':'Boolean source-fixture transcription, 8 initial states, generated histories length 0..8; not fresh Agda verification',
     'checks':checks,'passed':all(checks.values())}
p=ROOT/'research/sontag/results/wg-retained-history-transport-v1.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
