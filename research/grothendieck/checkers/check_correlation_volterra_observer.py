"""Exact panel certificates; no continuum or physical theta claim."""
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def load(name, path):
    import sys
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

v = load('volterra', 'research/grothendieck/correlation_volterra_observer.py')
s = load('stream', 'research/voevodsky/four_prime_correlation_observer.py')

def panels(word, start=0):
    vertex = start
    out = []
    for k, j in enumerate(word):
        edge = (vertex, vertex | (1 << j), j)
        duration = F(k+1, k+2)
        out.append((duration,
                    tuple(F(edge == a)/duration for a, _ in s.PROBES),
                    tuple(F(edge == b)/duration for _, b in s.PROBES)))
        vertex = edge[1]
    return out

checks = {}
count = 0
for start in range(16):
    unused = [j for j in range(4) if not start & (1 << j)]
    for length in range(len(unused)+1):
        for word in itertools.permutations(unused, length):
            p = panels(word, start)
            assert v.observe(p)[1] == s.observe_route(word, start)
            for cut in range(len(p)+1):
                right = p[cut:]
                mass = tuple(sum(dt*b[i] for dt, _, b in right) for i in range(6))
                assert v.concatenate(v.observe(p[:cut]), v.observe(right), mass) == v.observe(p)
            count += 1
checks['all_168_paths_match_streaming_observer'] = count == 168
checks['all_path_cuts_obey_chen_law'] = True

first = tuple(F(i-2, 3) for i in range(6))
second = tuple(F(3-i, 5) for i in range(6))
p = [(F(7, 3), first, second)]
q = [(F(2, 3), first, second), (F(5, 3), first, second)]
assert v.observe(p) == v.observe(q)
checks['overlapping_signed_channels_subdivision_exact'] = True
for i, value in enumerate(v.observe(p)[1]):
    assert abs(value) <= abs(F(7,3)*first[i]) * abs(F(7,3)*second[i])
checks['panel_L1_product_bound'] = True

def edges(word):
    mask = 0
    result = []
    for j in word:
        result.append((mask, mask | (1 << j), j))
        mask |= 1 << j
    return result

words = [(0,1,2,3), (1,0,3,2), (0,1,3,2), (1,0,2,3)]
from collections import Counter
assert Counter(edges(words[0])+edges(words[1])) == Counter(edges(words[2])+edges(words[3]))
outputs = [v.observe(panels(w))[1] for w in words]
difference = tuple(outputs[0][i]+outputs[1][i]-outputs[2][i]-outputs[3][i] for i in range(6))
assert difference == (1,0,0,0,0,0)
checks['equal_additive_responses_separated_before_aggregation'] = True
# A mixed signal's quadratic observation is not the linear mixture readout.
u = [(F(1), (F(1),)+(F(0),)*5, (F(0),)*6)]
w = [(F(1), (F(0),)*6, (F(1),)+(F(0),)*5)]
combined = [(F(1), u[0][1], w[0][2])]
assert v.observe(u)[1][0] + v.observe(w)[1][0] == 0
assert v.observe(combined)[1][0] == F(1,2)
checks['signal_superposition_is_not_source_mixture'] = True
try:
    v.observe([(-1, first, second)])
except ValueError:
    checks['negative_duration_rejected'] = True
else:
    raise AssertionError('negative duration accepted')
assert all(checks.values())
result = {'schema': 'marici.grothendieck.correlation-volterra.v1',
          'passed': True, 'checks': checks, 'paths': count,
          'collision_difference': list(map(str, difference)),
          'scope': 'Exact rational panel realization. L1 continuity proved in note; physical theta adapter not constructed.'}
path = ROOT / 'research/grothendieck/results/correlation-volterra-observer.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
