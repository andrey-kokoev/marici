"""Delayed-channel and randomized scheduling tests for the global join."""
from copy import deepcopy
from pathlib import Path
import contextlib,io,json,random
from four_cell_completion_barrier_net import construct
with contextlib.redirect_stdout(io.StringIO()):
    import check_four_cell_continuation_rewrite_probe as source
net=construct(source.records);meaning=net.live_meanings()
# Publish all outputs before any cleanup.
while True:
    choices=[p for p in net.enabled() if net.nodes[p[0]][0] in ('EB','VALUE')]
    if not choices:break
    net.step(choices[0])
assert all(v is not None for _,v in net.observe_barrier()[0])
held=next(p for p in net.enabled() if net.nodes[p[0]][0]=='CLEAN')
while True:
    choices=[p for p in net.enabled() if p!=held]
    if not choices:break
    net.step(choices[0])
    assert not net.observe_barrier()[1]
assert net.enabled()==[held]
assert net.live_meanings()==meaning
net.step(held)
while net.enabled():net.step(net.enabled()[0])
expected=net.observe_barrier()
assert expected[1]
assert sum(k=='READY' for k,_ in net.nodes.values())==1
assert all(k in ('OUT','ANSWER','READY','BARRIER') for k,_ in net.nodes.values())
steps=0
for seed in range(100):
    trial=construct(source.records);rng=random.Random(seed)
    gates=0;cleanups=0
    while trial.enabled():
        pair=rng.choice(trial.enabled());kind=trial.nodes[pair[0]][0]
        gates+=int(kind=='DONE');cleanups+=int(kind=='CLEAN')
        trial.step(pair);steps+=1
        assert trial.live_meanings()==meaning
        before=deepcopy(trial.__dict__);snapshot=trial.observe_barrier()
        assert before==trial.__dict__
        if snapshot[1]:assert gates==cleanups==4
    assert trial.observe_barrier()==expected
report={'passed':True,'three_completed_channels_cannot_release_barrier':True,
 'all_answers_visible_while_one_cleanup_withheld':True,
 'one_final_ready_token':True,'random_schedules':100,'transitions':steps,
 'scope':'Four-input fixed join tree, attributed data, no successor body or reusable source return. Completion covers model tokens only, not geometric or physical contour obligations.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/four-cell-completion-barrier-net.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
