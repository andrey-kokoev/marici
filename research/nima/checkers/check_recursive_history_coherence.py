"""Integrated recursive transactions, compensation, and serialized event replay.

Exercises the existing Store rather than a separate return implementation.
History serialization is an audit roundtrip, not crash-safe database storage.
"""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import json
import runpy
import tempfile

module=runpy.run_path(str(Path(__file__).with_name('check_recursive_record_transactions.py')))
Store=module['Store']
s=Store()
for i,(a,b,v) in enumerate(((0,2,1),(0,3,3),(1,2,5),(1,3,7),(4,5,9))):
    s.set_leaf(i,a,b,v)


def payloads(store): return {i:store.payload(r) for i,r in store.leaves.items()}


def compare_routes(store):
    parent=next(i for i,r in store.levels[1].items() if len(r.leaves)>1)
    row=store.levels[1][parent]
    direct,staged=deepcopy(store),deepcopy(store)
    assert direct.commit(direct.snapshot(1,parent,F(2,7)))
    # Each child gets the same leaf shift under the uniform mean-return rule.
    for child in row.children:
        assert staged.commit(staged.snapshot(0,child,F(2,7)))
    assert payloads(direct)==payloads(staged)
    assert direct.levels[1][parent].value==staged.levels[1][parent].value
    # They are different histories. No equality of transaction/version histories
    # is required to establish equality of the resulting member values.
    assert len(direct.events) != len(staged.events) or len(row.children)==1


compare_routes(s)
s.set_leaf(5,0,2,F(11))
compare_routes(s)
s.delete(5)
compare_routes(s)
parent=next(i for i,r in s.levels[1].items() if len(r.leaves)>1)
stale=s.snapshot(1,parent,1)
before=payloads(s)
assert s.commit(s.snapshot(1,parent,2))
assert s.undo_last()
assert payloads(s)==before
assert not s.commit(stale)  # restored values have new versions
# Unwind all remaining live operations, retaining compensation records.
while s.undo_last(): pass
assert not s.leaves and not s.levels[0] and not s.levels[1]
assert s.events and s.ids


def encode(row):
    if row is None: return None
    return [row.source,row.target,row.value.numerator,row.value.denominator,row.version]

packet=[{'kind':kind,'changes':[[rid,encode(old),encode(new)] for rid,old,new in changes]}
        for kind,changes in s.events]


def replay(events):
    state={}
    for event in events:
        # Validate complete batch before applying any part.
        assert all(state.get(rid)==old for rid,old,new in event['changes'])
        for rid,old,new in event['changes']:
            if new is None: state.pop(rid,None)
            else: state[rid]=new
    return state

with tempfile.TemporaryDirectory() as directory:
    path=Path(directory)/'events.json'
    path.write_text(json.dumps(packet),encoding='utf-8')
    loaded=json.loads(path.read_text(encoding='utf-8'))
    assert replay(loaded)=={}
    corrupted=deepcopy(loaded)
    # First insertion falsely expects an existing row.
    corrupted[0]['changes'][0][1]=[0,0,0,1,1]
    try: replay(corrupted)
    except AssertionError: pass
    else: raise AssertionError('corrupt event precondition accepted')
print('Direct upper return and staged child returns agree before insertion, after insertion, and after deletion.')
print('Compensation restores leaf values while advancing versions; stale pre-compensation requests stay invalid.')
print(f'{len(packet)} events including compensation serialize and replay to the empty live state.')
print('Corrupt event preconditions rejected before replay batch application.')
print('State equivalence across presentation routes does not imply identical version or event history.')
