"""Prefix tests for actual principal-port completion-gated successor release."""
import contextlib,io,json,random
from copy import deepcopy
from pathlib import Path
from four_cell_completion_gate_net import construct
with contextlib.redirect_stdout(io.StringIO()):
    import check_four_cell_continuation_rewrite_probe as source
net=construct(source.records);meaning=net.live_meanings()
# Publish all answers without running cleanup or successor gates.
while True:
    choices=[p for p in net.enabled() if net.nodes[p[0]][0] in ('EB','VALUE')]
    if not choices:break
    net.step(choices[0])
rows,complete,released=net.observe_public()
assert all(v is not None and not c and not r for _,v,c,r in rows)
assert not complete and not released
assert all(net.nodes[p[0]][0]=='CLEAN' for p in net.enabled())
# One cleanup enables exactly its gate; no other successor can release.
net.step(net.enabled()[0])
gates=[p for p in net.enabled() if net.nodes[p[0]][0]=='DONE']
assert len(gates)==1
rows,_,_=net.observe_public();assert sum(c for _,_,c,_ in rows)==1
assert not any(r for _,_,_,r in rows)
consumed=gates[0];net.step(consumed)
rows,_,_=net.observe_public();assert sum(r for _,_,_,r in rows)==1
try:net.step(consumed)
except ValueError:pass
else:raise AssertionError('completion replayed')
while net.enabled():net.step(net.enabled()[0])
terminal=net.observe_public()
assert terminal[1:] == (True,True)
assert all(k in ('OUT','ANSWER','NEXT','READY') for k,_ in net.nodes.values())
steps=0
for seed in range(100):
    trial=construct(source.records);rng=random.Random(seed)
    while trial.enabled():
        before=trial.observe_public()
        trial.step(rng.choice(trial.enabled()));steps+=1
        state=deepcopy(trial.__dict__);after=trial.observe_public()
        assert state==trial.__dict__ and trial.live_meanings()==meaning
        for old,new in zip(before[0],after[0]):
            label,value,complete,released=new
            assert not released or complete
            assert not complete or value is not None
            assert not old[2] or complete
            assert not old[3] or released
            assert old[1] is None or old[1]==value
    assert trial.observe_public()==terminal
report={'passed':True,'all_answers_can_precede_all_releases':True,
 'one_cleanup_enables_only_its_own_successor':True,
 'completion_token_consumed_once':True,'random_schedules':100,'transitions':steps,
 'scope':'Per-channel DONE-driven release witnesses. No all-channel join, retained-source return, geometric successor execution or physical contour inference.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/four-cell-completion-gate-net.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
