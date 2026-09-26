"""Retained observer-square/cube regression on the existing 18-value source.
Cubical incidence is finite; genuine HoTT cells are checked separately in Agda.
"""
import contextlib
import io
from itertools import product, permutations, combinations
from collections import Counter
from pathlib import Path
import hashlib
import json

with contextlib.redirect_stdout(io.StringIO()):
    import check_observer_source_power_comparisons as old

BASE = Path(__file__).resolve().parents[1]

# A cell uses None for each interval direction. All faces retain coordinates.
def boundary(cell):
    out = Counter()
    for k, i in enumerate(j for j, x in enumerate(cell) if x is None):
        for value, sign in ((1, 1), (0, -1)):
            face = list(cell)
            face[i] = value
            out[tuple(face)] += (-1)**k * sign
    return {c: n for c, n in out.items() if n}

def boundary_chain(chain):
    out = Counter()
    for cell, coefficient in chain.items():
        for face, sign in boundary(cell).items():
            out[face] += coefficient*sign
    return {c: n for c, n in out.items() if n}

cell_checks = 0
for n in range(1, 5):
    for cell in product((0, 1, None), repeat=n):
        assert boundary_chain(boundary(cell)) == {}
        cell_checks += 1
full = (None,)*3
faces = boundary(full)
assert len(faces) == 6
missing_face = dict(faces)
del missing_face[next(iter(missing_face))]
assert boundary_chain(missing_face) != {}

Q = old.Q
pairs = [(0, 0), (0, 1), (1, 0), (2, 2), (5, 9), (17, 17)]
observers = [old.encode_observer(Q[i], Q[j]) for i, j in pairs]

def step(mask, values, direction):
    if mask[direction]:
        raise ValueError('observer already expanded')
    next_mask, next_values = list(mask), list(values)
    next_mask[direction] = 1
    next_values[direction] = old.decode_observer(values[direction])
    return tuple(next_mask), tuple(next_values)

def recover(mask, values):
    return tuple(old.encode_observer(*v) if bit else v for bit, v in zip(mask, values))

route_count = square_count = 0
for original in product(observers, repeat=3):
    final_values = None
    histories = []
    for order in permutations(range(3)):
        mask, values = (0, 0, 0), original
        history = [(mask, values)]
        for direction in order:
            mask, values = step(mask, values, direction)
            assert recover(mask, values) == original
            history.append((mask, values))
        assert mask == (1, 1, 1)
        if final_values is None:
            final_values = values
        assert values == final_values
        histories.append((order, history))
        route_count += 1
    assert len({order for order, _ in histories}) == 6  # never erase schedules
    # Six squares: choose two variable directions and fix the third at 0 or 1.
    for i, j in combinations(range(3), 2):
        k = next(k for k in range(3) if k not in (i, j))
        for bit in (0, 1):
            state = ((0, 0, 0), original)
            if bit:
                state = step(*state, k)
            ij = step(*step(*state, i), j)
            ji = step(*step(*state, j), i)
            assert ij == ji
            square_count += 1
    for index, (left, right) in enumerate(final_values):
        assert old.compatible(original[index]) == (left == right)

try:
    state = step((0, 0, 0), (observers[0],)*3, 0)
    step(*state, 0)
except ValueError:
    duplicate_refused = True
else:
    raise AssertionError('duplicate expansion admitted')
# Free observer vertices exist even when the attachment fibre is empty.
assert not old.compatible(observers[1])
assert old.compatible(observers[0])
# Combinatorial connectedness uses all 12 edges, without inferring that the
# ambient type universe has no nontrivial loops.
reached = {(0, 0, 0)}
for _ in range(3):
    reached |= {tuple(1 if j == i else bit for j, bit in enumerate(v))
                for v in list(reached) for i in range(3)}
assert len(reached) == 8

files = [Path(__file__), BASE/'agda/ObserverCoherenceCube.agda',
         BASE/'agda/DependentSigmaPiCoherence.agda',
         BASE/'checkers/check_observer_source_power_comparisons.py']
packet = {
    'status': 'retained-observer-square-and-cube-checked',
    'source_values': len(Q), 'selected_observers': len(observers),
    'observer_triples': len(observers)**3, 'retained_routes': route_count,
    'square_checks': square_count, 'cube_cells_by_dimension': [8, 12, 6, 1],
    'boundary_squared_checks_dimensions_1_to_4': cell_checks,
    'hostiles': {'missing_face_detected': True, 'duplicate_expansion_refused': duplicate_refused,
                 'free_vertex_does_not_imply_attachment': True},
    'sample_schedules': [list(p) for p in permutations(range(3))],
    'scope': 'Fixed canonical full chains; finite product-expansion diagrams, not a complete free infinity-groupoid or numerical positivity theorem',
    'sha256': {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
}
(BASE/'results/observer-coherence-cube.json').write_text(json.dumps(packet, indent=2)+'\n', encoding='utf-8')
print('Observer cube: 216 triples, 1296 retained routes, 1296 squares; boundary and attachment controls passed.')
