"""Stronger named-boundary observations expose a joint-summary collision."""
import contextlib, io, itertools, json
from copy import deepcopy
from pathlib import Path
from four_cell_port_net import construct
with contextlib.redirect_stdout(io.StringIO()):
    import check_four_cell_continuation_rewrite_probe as source

original = construct(source.records)
channels = original.observe_channels()
joint = original.observe()
# An abstract admitted payload perturbation, NOT a second physical target.
changed = deepcopy(source.records)
x,y = changed['zero2_E_B'],changed['zero2_F_B']
x['value'] = (x['value'][0]+1, x['value'][1])
y['value'] = (y['value'][0]-1, y['value'][1])
alternative = construct(changed)
assert alternative.observe() == joint
assert alternative.observe_channels() != channels

def normalize(net, retain):
    while net.active():
        net.reduce(net.active()[0], retain_channels=retain)
    return net

coarse = normalize(deepcopy(original), False)
coarse_alt = normalize(deepcopy(alternative), False)
assert coarse.boundary_normal_form() == coarse_alt.boundary_normal_form()
try:
    coarse.observe_channels()
except ValueError:
    coarse_probe_rejected = True
else:
    raise AssertionError('coarse remainder claimed unavailable channels')

finals=[]
probe_checks=0
for order in itertools.permutations(('zero2','zero3')):
    net=deepcopy(original)
    for family in order:
        pair=next(p for p in net.active() if net.nodes[p[0]][1]['family']==family)
        net.reduce(pair, retain_channels=True)
        assert net.observe_channels()==channels and net.observe()==joint
        # Exhaust all subsets of the four named outputs as read-only contexts.
        labels=list(channels)
        for mask in range(16):
            selected=[key for i,key in enumerate(labels) if mask & (1<<i)]
            assert {k:net.observe_channels()[k] for k in selected}=={k:channels[k] for k in selected}
            probe_checks+=1
    finals.append(net.boundary_normal_form())
assert finals[0]==finals[1]
fine=normalize(deepcopy(original),True)
fine_alt=normalize(deepcopy(alternative),True)
assert fine.boundary_normal_form()!=fine_alt.boundary_normal_form()
# Wrong boundary assignment preserves aggregate values but is detected by probes.
for _,(kind,payload) in fine.nodes.items():
    if kind=='REM' and payload['family']=='zero2':
        payload['channels']['p'],payload['channels']['o']=payload['channels']['o'],payload['channels']['p']
assert fine.observe()==joint and fine.observe_channels()!=channels
report={'passed':True,'coarse_summary_collision':True,
 'collision_is_synthetic_payload_control_not_physical_target':True,
 'coarse_channel_probe_explicitly_rejected':coarse_probe_rejected,
 'two_slot_remainder_preserves_named_channels':True,
 'subset_probe_checks':probe_checks,'reduction_orders':2,
 'boundary_slot_swap_detected':True,
 'scope':'Read-only finite boundary contexts on attributed agents; not arbitrary context equivalence, destructive reusable query implementation, finite-alphabet compilation or contour determination.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/four-cell-port-net-channel-contexts.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
