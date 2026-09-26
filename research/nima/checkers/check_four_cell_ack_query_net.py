"""Prefix-time publication versus completion tests for acknowledged component queries."""
from copy import deepcopy
from pathlib import Path
import contextlib,io,json,random
from four_cell_ack_query_net import construct
with contextlib.redirect_stdout(io.StringIO()):
    import check_four_cell_continuation_rewrite_probe as source

net=construct(source.records);expected=net.live_meanings()
assert all(value is None and not ack for _,value,ack in net.observe_public()[0])
# Finish cancellations and publish every answer while deliberately withholding cleanup.
while True:
    choices=[p for p in net.enabled() if net.nodes[p[0]][0]!='CLEAN']
    if not choices:break
    net.step(choices[0]);assert net.live_meanings()==expected
before=deepcopy(net.__dict__)
snapshot=net.observe_public()
assert before==net.__dict__
assert all(value is not None and not ack for _,value,ack in snapshot[0])
assert not snapshot[1] and len(net.enabled())==4
published=snapshot
while net.enabled():net.step(net.enabled()[0])
assert net.observe_public()[1]
assert [v for _,v,_ in net.observe_public()[0]]==[v for _,v,_ in published[0]]
assert all(k in ('OUT','ANSWER','ACK','DONE') for k,_ in net.nodes.values())
# Random interleavings test prefix semantics; not exhaustive scheduling proof.
steps=0
for seed in range(100):
    trial=construct(source.records);rng=random.Random(seed)
    while trial.enabled():
        trial.step(rng.choice(trial.enabled()));steps+=1
        assert trial.live_meanings()==expected
        state=deepcopy(trial.__dict__);obs=trial.observe_public()
        assert trial.__dict__==state
        for label,value,ack in obs[0]:
            assert value is None or value==expected[label]
            assert not ack or value is not None
    assert trial.observe_public()==net.observe_public()
# Zero-valued published answers must not be mistaken for pending.
zero=deepcopy(source.records)
for r in zero.values():r['value']=(0,0)
trial=construct(zero)
while trial.enabled():trial.step(trial.enabled()[0])
assert all(value==(0,0) and ack for _,value,ack in trial.observe_public()[0])
report={'passed':True,'all_four_answers_visible_before_any_completion':True,
 'cleanup_delayed_without_changing_answers':True,'read_only_immutable_snapshot':True,
 'random_schedules':100,'random_schedule_steps':steps,'zero_is_not_pending':True,
 'scope':'Explicit modeled cleanup tokens, not geometric obligation certification. No retained-source return, successor gates or contour selection yet.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/four-cell-ack-query-net.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
