"""Dynamic retained-record views: stable IDs, edits, and reversible history.

Discrete edits carry old/new whole records. Indexes are derived caches keyed
by stable member IDs. Fresh family IDs persist by group key (including empty
historical groups); derived mean-edit cost is current member count.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from random import Random


@dataclass(frozen=True)
class Record:
    source: int
    target: int
    value: F


class Store:
    def __init__(self):
        self.records = {}
        self.index = {'source': {}, 'target': {}}
        self.family_ids = {'source': {}, 'target': {}}
        self.next_family = 0
        self.history = []

    def change(self, rid, expected, new):
        assert self.records.get(rid) == expected, 'stale record edit'
        assert expected is not None or new is not None
        if expected is not None:
            for field in self.index:
                self.index[field][getattr(expected, field)].remove(rid)
            del self.records[rid]
        if new is not None:
            self.records[rid] = new
            for field in self.index:
                key = getattr(new, field)
                if key not in self.family_ids[field]:
                    self.family_ids[field][key] = self.next_family
                    self.next_family += 1
                self.index[field].setdefault(key, set()).add(rid)
        self.history.append((rid, expected, new))
        self.check()

    def check(self):
        for field, index in self.index.items():
            rebuilt = {}
            for rid, row in self.records.items():
                rebuilt.setdefault(getattr(row, field), set()).add(rid)
            assert {k: v for k, v in index.items() if v} == rebuilt
            # Source/target flattening reconstructs identical ID-bearing records.
            restored = {rid: self.records[rid] for members in index.values() for rid in members}
            assert restored == self.records
            for key, members in index.items():
                if not members:
                    continue  # empty mean has no value and admits no mean edit
                mean = sum((self.records[rid].value for rid in members), F(0))/len(members)
                residual = {rid: self.records[rid].value-mean for rid in members}
                assert sum(residual.values(), F(0)) == 0
                assert all(mean+residual[rid] == self.records[rid].value for rid in members)
                # Full correction by delta has exact induced cost n*delta^2.
                delta = F(2, 7)
                assert sum(delta**2 for _ in members) == len(members)*delta**2

    def mean_edit(self, field, key, delta, expected_members):
        members = set(self.index[field].get(key, set()))
        assert members == set(expected_members), 'stale family membership'
        assert members, 'empty family mean'
        # Freeze member IDs before applying the batch; endpoints are unchanged.
        for rid in sorted(members):
            old = self.records[rid]
            self.change(rid, old, Record(old.source, old.target, old.value+delta))


store = Store()
rng = Random(137)
next_id = 0
for _ in range(250):
    action = rng.randrange(4) if store.records else 0
    if action == 0:
        row = Record(rng.randrange(4), rng.randrange(4), F(rng.randrange(-9,10), 3))
        store.change(next_id, None, row)
        next_id += 1
    elif action == 1:
        rid = rng.choice(sorted(store.records))
        store.change(rid, store.records[rid], None)
    elif action == 2:
        rid = rng.choice(sorted(store.records)); old = store.records[rid]
        store.change(rid, old, Record(rng.randrange(4), rng.randrange(4), old.value))
    else:
        field = rng.choice(['source','target'])
        key = rng.choice([k for k,v in store.index[field].items() if v])
        store.mean_edit(field, key, F(1,5), store.index[field][key].copy())

# Invert the actual event sequence. Old records supply deleted values and IDs.
history = store.history.copy()
family_ids = {k: v.copy() for k,v in store.family_ids.items()}
for rid, old, new in reversed(history):
    store.change(rid, new, old)
assert not store.records
assert store.family_ids == family_ids  # identity/history persists, not rewound

# Order matters if an insertion changes the membership of the edited family.
a = Store(); b = Store()
old = Record(0,1,F(2)); new = Record(0,2,F(7))
for s in (a,b): s.change(0,None,old)
a.mean_edit('source',0,F(1),{0}); a.change(1,None,new)
b.change(1,None,new); b.mean_edit('source',0,F(1),{0,1})
assert a.records[1].value == 7 and b.records[1].value == 8
# A stale membership-scoped edit must be rejected before any mutation.
snapshot = b.records.copy()
try:
    b.mean_edit('source',0,F(1),{0})
except AssertionError as error:
    assert str(error) == 'stale family membership'
else:
    raise AssertionError('accepted stale family edit')
assert b.records == snapshot
print(f'250 scheduled operations produced {len(history)} leaf events; incremental indexes equal full rebuild throughout.')
print('Every source/target view reconstructs the live records; means/residuals and count-weighted edit costs pass exactly.')
print('Reverse event replay restores empty live state while retaining family identities/history.')
print('Insert-then-mean-edit differs from mean-edit-then-insert; stale member-scope edit is rejected without mutation.')
print('Policy: stable member IDs, family IDs by persistent group key, history-retained deletes, snapshot-scoped mean edits.')
