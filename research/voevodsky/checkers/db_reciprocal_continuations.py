"""One typed customer/product pair. Minimize by equality of future match traces."""
from itertools import product
from pathlib import Path
import json

VALUES = ('yes', 'no', 'unknown')
STATES = list(product(VALUES, repeat=2))  # supplier first, customer second

def step(state, action):
    side, conditional = action
    s = list(state)
    if not conditional or s[side] == 'unknown':
        s[side] = 'yes'
    return tuple(s)

def classes(conditional):
    actions = list(product(range(2), (False, True) if conditional else (False,)))
    partition = {s: int(s == ('yes', 'yes')) for s in STATES}
    while True:
        groups = {}
        refined = {s: groups.setdefault((partition[s], tuple(partition[step(s,a)] for a in actions)), len(groups)) for s in STATES}
        if len(groups) == len(set(partition.values())):
            return [[list(s) for s in STATES if refined[s] == g] for g in groups.values()]
        partition = refined

if __name__ == '__main__':
    results = {k: classes(flag) for k,flag in [('set_yes_then_match',False),('also_fill_unknown_then_match',True)]}
    assert [len(v) for v in results.values()] == [4,9]
    path = Path(__file__).resolve().parents[1]/'results/db_reciprocal_continuations.json'
    path.write_text(json.dumps(results, indent=2)+'\n', encoding='utf-8')
    print({k: len(v) for k,v in results.items()})
