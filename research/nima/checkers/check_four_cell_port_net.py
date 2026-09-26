"""Executable principal-port experiment on exact four-cell payloads."""
import contextlib, io, itertools, json
from copy import deepcopy
from pathlib import Path
import sympy as s
from four_cell_port_net import construct
with contextlib.redirect_stdout(io.StringIO()):
    import check_four_cell_continuation_rewrite_probe as source

initial = construct(source.records)
expected = initial.observe()
finals = []
steps = 0
for order in itertools.permutations(('zero2', 'zero3')):
    net = deepcopy(initial)
    boundary = {n: data for n, data in net.nodes.items() if data[0] == 'OUT'}
    for family in order:
        pair = next(p for p in net.active() if net.nodes[p[0]][1]['family'] == family)
        before = len(net.nodes)
        net.reduce(pair)
        assert len(net.nodes) == before - 1
        assert net.observe() == expected
        assert all(net.nodes[n] == data for n, data in boundary.items())
        steps += 1
        try:
            net.reduce(pair)
        except ValueError:
            pass
        else:
            raise AssertionError('consumed pair reused')
    assert not net.active()
    finals.append(net.boundary_normal_form())
assert finals[0] == finals[1]
assert all(s.factor(v) != 0 for f, values in expected.items()
           for v in [values[0] if f == 'zero2' else values[1]])
# Invalid wiring and payloads must be refused before mutation.
refusals = []
def refuse(label, operation):
    try:
        operation()
    except ValueError:
        refusals.append(label)
    else:
        raise AssertionError(label)
a,b = initial.active()[0]
refuse('double wiring', lambda: initial.link((a,'o'), (b,'o')))
bad = deepcopy(initial); del bad.wires[a,'o']
refuse('dangling/asymmetric boundary', bad.validate)
bad = deepcopy(initial); bad.nodes[b][1]['pole'] = bad.nodes[a][1]['pole']
refuse('noncancelling pole', lambda: bad.reduce((a,b)))
bad = deepcopy(initial); bad.nodes[b][1]['family'] = 'foreign'
refuse('cross-family merge', lambda: bad.reduce((a,b)))
bad = deepcopy(initial); bad.nodes[b][1]['members'] = bad.nodes[a][1]['members']
refuse('duplicated source ownership', lambda: bad.reduce((a,b)))
# Retaining wiring but erasing the remainder payload fails the observer.
for n,(kind,payload) in net.nodes.items():
    if kind == 'REM': payload['value'] = (0,0)
assert net.observe() != expected
report = {'passed': True, 'principal_pair_rule': 'EB.p--FB.p -> REM with two preserved boundary connections',
          'orders_checked': 2, 'steps_checked': steps,
          'joint_component_observer_preserved': True,
          'terminal_nets_equal_modulo_fresh_names': True,
          'negative_controls_rejected': refusals,
          'payload_erasure_detected': True,
          'contour_weights': 'alpha and beta remain external free family weights',
          'scope': 'Attributed port-net with exact arithmetic payloads at one target. Joint family observer only; not individual-output equivalence, finite-alphabet arithmetic compilation, full superform semantics or physical contour.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/four-cell-port-net.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
