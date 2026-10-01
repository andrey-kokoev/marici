"""Candidate rung4 readout in the existing fixed Gram G4=10I+J.

Coordinates count ancestral endpoint occurrences: promoting uv adds their
four-component vectors. Spatial contrasts have zero sum, eliminating J.
Lengths are reported in units of a seed edge (squared Gram length20).
Alternative averaging retains total weight separately and changes the readout.
Clock candidates are declared conventions, not a derived proper-time law.
"""
from pathlib import Path
from collections import defaultdict, Counter
from itertools import combinations
from fractions import Fraction
from contextlib import redirect_stdout
import io
import json
import runpy

HERE = Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    kernel = runpy.run_path(str(HERE/'check_label_from_to_fibration_tower.py'))
original = kernel['original']


def gram(x,y):
    return 10*sum(a*b for a,b in zip(x,y))+sum(x)*sum(y)


def length_squared(x,y):
    delta = tuple(a-b for a,b in zip(x,y))
    assert sum(delta)==0
    # Gram norm of a seed-edge contrast is20.
    return Fraction(gram(delta,delta),20)


basis = [tuple(int(i==j) for i in range(4)) for j in range(4)]
assert all(length_squared(x,y)==1 for x,y in combinations(basis,2))
# Common and contrast channels are Gram-orthogonal.
for x in basis:
    contrast = tuple(Fraction(v)-Fraction(1,4) for v in x)
    assert gram(contrast,(1,1,1,1))==0

edges = {(0,1),(0,2),(1,2),(0,3)}
positions = basis
reports = []
for cycle in range(8):
    weight = 2**cycle
    assert all(sum(p)==weight for p in positions)
    distinct = sorted(set(positions))
    diameter2 = max(length_squared(a,b) for a,b in combinations(distinct,2))
    normalized2 = diameter2/(weight*weight)
    if reports:
        # Averaged child points are midpoints in the fixed reference frame.
        assert normalized2 <= Fraction(reports[-1]['mean_readout_diameter_squared'])
    edge_lengths = Counter(length_squared(positions[a],positions[b]) for a,b in edges)
    zero_edges = edge_lengths.get(Fraction(0),0)
    # Test the candidate length on every actual directed packet after descent.
    for i,(a,b) in enumerate(pair for edge in sorted(edges) for pair in (edge,edge[::-1])):
        leaf = (i,a,b)
        row = leaf
        for depth in range(8): row = (leaf[depth%3],row)
        restored = original(row,8)
        assert restored == leaf
        assert length_squared(positions[restored[1]],positions[restored[2]]) == length_squared(positions[a],positions[b])
    result = {
        'cycle':cycle,'records':len(positions),'distinct_readout_positions':len(distinct),
        'sum_readout_diameter_squared':str(diameter2),
        'mean_readout_diameter_squared':str(normalized2),
        'retained_endpoint_occurrences_per_record':weight,
        'common_mode_elapsed_candidate':weight-1,
        'witness_tick_elapsed_candidate':8*cycle,
        'zero_length_graph_edges':zero_edges,
        'edge_squared_length_histogram':{str(k):v for k,v in sorted(edge_lengths.items())},
        'physical_proper_time':None,
    }
    reports.append(result)
    print(cycle,len(positions),len(distinct),f'{float(diameter2)**0.5:.6f}',
          f'{float(normalized2)**0.5:.6f}',weight-1,8*cycle,zero_edges,flush=True)
    if cycle==7: break
    incident = defaultdict(list)
    children = []
    for i,(a,b) in enumerate(sorted(edges)):
        incident[a].append(i);incident[b].append(i)
        children.append(tuple(x+y for x,y in zip(positions[a],positions[b])))
    edges = {tuple(sorted(pair)) for ids in incident.values() for pair in combinations(ids,2)}
    positions = children

out = {'status':'passed','reference_gram':'10I4+J4',
       'length_unit':'one seed-edge Gram length, sqrt(20) in coefficient units',
       'coordinate_rule':'child ancestral multiplicities = parent1 + parent2',
       'comparison_readout':'divide coordinates by their common total weight; retain that weight separately',
       'spatial_dimension':'three-dimensional zero-sum contrast subspace',
       'cycles':reports,
       'scope':'Conditional readouts in a fixed four-probe frame. The coordinate normalization and physical clock selection are unresolved; no Lorentzian metric or FLRW solution is derived.'}
(HERE.parent/'results/rung4-ancestry-metric.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('PASS: fixed-Gram spatial contrasts, all-packet rung4 transport, and averaging control.')
