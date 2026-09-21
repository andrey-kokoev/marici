"""Actual source-coordinate ordinary observation; no Green isometry claim."""
from pathlib import Path
from itertools import permutations, product
from fractions import Fraction
import contextlib
import io
import json
import runpy

ROOT = Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    src = runpy.run_path(str(ROOT / 'research/grothendieck/checkers/check_six_prime_derived_block_associativity.py'))
record, relation = src['record'], src['relation']
derivative, add = src['derivative'], src['add']

def history(column, start):
    out = {}
    for (word, marks), coefficient in column.items():
        out = add(out, record(word, marks, start), coefficient)
    return out

def rank(columns):
    pivots = {}
    for column in columns:
        v = {key: Fraction(value) for key, value in column.items()}
        while v:
            key = min(v)
            if key not in pivots:
                scale = v[key]
                pivots[key] = {k: c/scale for k, c in v.items()}
                break
            v = add(v, pivots[key], -v[key])
    return len(pivots)

partitions = lift_checks = killed = 0
for first, middle, last in src['blocks'](tuple(range(6))):
    start = sum(1 << p for p in first)
    end = start | sum(1 << p for p in middle)
    paths = [(w, m) for w in permutations(middle)
             for m in product((False, True), repeat=2)]
    histories = [history({p: 1}, start) for p in paths]
    assert rank(histories) == 6
    for kind in (0, 1):
        b = relation(middle, kind)
        assert not history(b, start)
        killed += 1
        for path, image in zip(paths, histories):
            assert history(add({path: 1}, b, 1), start) == image
            lift_checks += 1
    # Independence of each outer pair of actual seam cycles gives tensor rank 24.
    assert rank([derivative(relation(first, k), 0) for k in (0, 1)]) == 2
    assert rank([derivative(relation(last, k), end) for k in (0, 1)]) == 2
    partitions += 1
assert partitions == 90
print(json.dumps({
    'passed': True,
    'labelled_partitions': partitions,
    'middle_relations_killed': killed,
    'middle_lift_checks': lift_checks,
    'ordinary_coefficient_rank_by_tensor_factors': partitions * 2 * 6 * 2,
    'scope': 'D(a) tensor terminal_history(w) tensor D(c), in actual source potential coordinates. Analytical transfer requires the admitted faithful typed history carrier. No identification with full coarse Green observations or forms.'
}, indent=2))
