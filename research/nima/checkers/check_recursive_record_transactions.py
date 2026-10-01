"""Two-level retained-family promotion and optimistic edit transactions.

Explicit endpoint policy: a promoted record's endpoints are interned sets of
its children's source/target IDs. It retains child IDs and all descendant IDs.
Level1 groups by source, level2 by target. Single-process transaction model;
interleavings are tested, not threaded locking or durable storage.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from random import Random
from uuid import uuid4


@dataclass(frozen=True)
class Row:
    source: object
    target: object
    value: F
    version: int
    children: tuple = ()
    leaves: frozenset = frozenset()
    child_versions: tuple = ()


@dataclass(frozen=True)
class VectorRequest:
    store_id: str
    cursor: int
    entries: tuple  # (leaf ID, expected version, rational increment)
    parent: object = None
    transport_events: tuple = ()


class Store:
    def __init__(self):
        self.leaves = {}
        self.levels = [{}, {}]
        self.ids = {}
        self.serial = 0
        self.versions = {}
        self.events = []
        self.active_events = []
        self.store_id = str(uuid4())
        self.vector_events = {}  # accepted event index -> immutable request/provenance

    def intern(self, key):
        if key not in self.ids:
            self.ids[key] = ('generated', self.serial)
            self.serial += 1
        return self.ids[key]

    def bump(self, rid):
        self.versions[rid] = self.versions.get(rid, 0)+1
        return self.versions[rid]

    def rebuild(self):
        lower = self.leaves
        output = []
        for depth, field in enumerate(('source', 'target')):
            groups = {}
            for rid, row in lower.items():
                groups.setdefault(getattr(row, field), []).append(rid)
            level = {}
            for key, members in groups.items():
                members = tuple(sorted(members, key=repr))
                rid = self.intern(('family', depth, field, key))
                src = self.intern(('endpoint', depth, 'source', frozenset(lower[m].source for m in members)))
                tgt = self.intern(('endpoint', depth, 'target', frozenset(lower[m].target for m in members)))
                leaves = frozenset().union(*(lower[m].leaves for m in members))
                mean = sum((self.leaves[m].value for m in leaves), F(0))/len(leaves)
                child_versions = tuple(lower[m].version for m in members)
                signature = (src, tgt, mean, members, leaves, child_versions)
                old = self.levels[depth].get(rid)
                oldsig = None if old is None else (old.source,old.target,old.value,old.children,old.leaves,old.child_versions)
                version = old.version if oldsig == signature else self.bump(rid)
                level[rid] = Row(src,tgt,mean,version,members,leaves,child_versions)
            output.append(level)
            lower = level
        self.levels = output

    @staticmethod
    def payload(row):
        return None if row is None else (row.source, row.target, row.value)

    def finish_event(self, before, kind):
        self.rebuild()
        self.check()
        changes = tuple((m, before.get(m), self.leaves.get(m))
                        for m in sorted(set(before) | set(self.leaves), key=repr)
                        if before.get(m) != self.leaves.get(m))
        self.events.append((kind, changes))
        self.active_events.append(len(self.events)-1)

    def set_leaf(self, rid, source, target, value):
        before = self.leaves.copy()
        self.leaves[rid] = Row(source,target,F(value),self.bump(rid),leaves=frozenset({rid}))
        self.finish_event(before, 'set')

    def delete(self, rid):
        before = self.leaves.copy()
        del self.leaves[rid]
        self.bump(rid)
        self.finish_event(before, 'delete')

    def undo_last(self):
        # Serialized LIFO compensation. Values return; versions never rewind.
        if not self.active_events:
            return False
        event_index = self.active_events[-1]
        _, changes = self.events[event_index]
        assert all(self.payload(self.leaves.get(m)) == self.payload(new)
                   for m, old, new in changes)
        before = self.leaves.copy()
        for m, old, new in changes:
            version = self.bump(m)
            if old is None:
                self.leaves.pop(m, None)
            else:
                self.leaves[m] = Row(old.source, old.target, old.value, version,
                                     leaves=frozenset({m}))
        self.rebuild()
        self.check()
        self.active_events.pop()
        compensation = tuple((m, before.get(m), self.leaves.get(m)) for m, _, _ in changes)
        self.events.append((f'compensate:{event_index}', compensation))
        return True

    def snapshot(self, level, rid, delta):
        row = self.levels[level][rid]
        versions = {m:self.leaves[m].version for m in row.leaves}
        return level,rid,row.version,versions,F(delta)

    def commit(self, request):
        level,rid,version,versions,delta = request
        row = self.levels[level].get(rid)
        if row is None or row.version != version or row.leaves != frozenset(versions):
            return False
        if any(self.leaves[m].version != v for m,v in versions.items()):
            return False
        # All validation precedes mutation: this method models one atomic commit.
        before = self.leaves.copy()
        for m in versions:
            old = self.leaves[m]
            self.leaves[m] = Row(old.source,old.target,old.value+delta,self.bump(m),leaves=old.leaves)
        self.finish_event(before, 'mean-edit')
        return True

    def snapshot_vector(self, deltas):
        # Explicit member scope; omitted members are not read or written.
        if not set(deltas) <= self.leaves.keys():
            return None
        entries = tuple((m, self.leaves[m].version, F(deltas[m]))
                        for m in sorted(deltas, key=repr))
        return VectorRequest(self.store_id, len(self.events), entries)

    def rebase_vector(self, request, *, approved=False):
        # Trusted local API: approval is an explicit policy choice, not an
        # authentication mechanism. Follow actual events, never final IDs alone.
        if approved is not True or request.store_id != self.store_id:
            return None
        if not 0 <= request.cursor <= len(self.events):
            return None
        live = {m: delta for m, _, delta in request.entries}
        for _, changes in self.events[request.cursor:]:
            for m, old, new in changes:
                if old is not None and new is None:
                    live.pop(m, None)  # later restoration must not resurrect scope
        if not set(live) <= self.leaves.keys():
            return None
        fresh = self.snapshot_vector(live)
        return VectorRequest(self.store_id, fresh.cursor, fresh.entries, request,
                             tuple(range(request.cursor, len(self.events))))

    def commit_vector(self, request):
        if request is None or request.store_id != self.store_id:
            return False
        if not 0 <= request.cursor <= len(self.events):
            return False
        members = [m for m, _, _ in request.entries]
        if len(set(members)) != len(members):
            return False
        if any(m not in self.leaves or self.leaves[m].version != version
               for m, version, _ in request.entries):
            return False
        # Validate numeric inputs for the whole batch before mutating anything.
        deltas = {m: F(delta) for m, _, delta in request.entries}
        before = self.leaves.copy()
        for m, _, _ in request.entries:
            old = self.leaves[m]
            self.leaves[m] = Row(old.source, old.target, old.value+deltas[m],
                                 self.bump(m), leaves=old.leaves)
        event_index = len(self.events)
        self.finish_event(before, 'member-vector')
        self.vector_events[event_index] = request
        return True

    def check(self):
        lower = self.leaves
        for depth, level in enumerate(self.levels):
            covered = set()
            for row in level.values():
                assert not covered.intersection(row.children)
                covered.update(row.children)
                descendants = frozenset().union(*(lower[m].leaves for m in row.children))
                assert descendants == row.leaves
                assert row.value == sum((self.leaves[m].value for m in descendants),F(0))/len(descendants)
                assert row.child_versions == tuple(lower[m].version for m in row.children)
            assert covered == set(lower)
            lower = level
        # Full rebuild is stable in identity, values, versions and endpoints.
        before = [level.copy() for level in self.levels]
        self.rebuild()
        assert before == self.levels


s = Store()
# Sources0 and1 have matching target footprints and thus share an upper family.
for i,(a,b,v) in enumerate(((0,2,1),(0,3,3),(1,2,5),(1,3,7),(4,5,9))):
    s.set_leaf(i,a,b,v)
upper = next(rid for rid,row in s.levels[1].items() if len(row.leaves)==4)
a = s.snapshot(1,upper,1)
b = s.snapshot(1,upper,2)
assert s.commit(a)
before = dict(s.leaves)
assert not s.commit(b) and before == s.leaves
# A disjoint edit can commit despite intervening activity elsewhere.
other = next(rid for rid,row in s.levels[1].items() if len(row.leaves)==1)
c = s.snapshot(1,other,3)
assert s.commit(s.snapshot(1,upper,1))
assert s.commit(c)
# Moving an endpoint changes footprints and invalidates old parent requests.
stale = s.snapshot(1,upper,1)
s.set_leaf(0,0,8,s.leaves[0].value)
before = dict(s.leaves)
assert not s.commit(stale) and before == s.leaves
# ABA: restore a leaf's old value; version still advances, rejecting old edits.
rid = next(iter(s.levels[0]))
aba = s.snapshot(0,rid,1)
m = next(iter(s.levels[0][rid].leaves)); old = s.leaves[m]
s.set_leaf(m,old.source,old.target,old.value+1)
s.set_leaf(m,old.source,old.target,old.value)
assert not s.commit(aba)

rng = Random(137)
next_id = 5
for _ in range(100):
    op = rng.randrange(4) if s.leaves else 0
    if op == 0:
        s.set_leaf(next_id,rng.randrange(5),rng.randrange(5),F(rng.randrange(10),3)); next_id+=1
    elif op == 1:
        s.delete(rng.choice(list(s.leaves)))
    elif op == 2:
        m=rng.choice(list(s.leaves)); row=s.leaves[m]
        s.set_leaf(m,rng.randrange(5),rng.randrange(5),row.value)
    else:
        level=rng.randrange(2); rid=rng.choice(list(s.levels[level]))
        request=s.snapshot(level,rid,F(1,7))
        old=s.levels[level][rid].value
        assert s.commit(request)
        assert s.levels[level][rid].value == old+F(1,7)
print('Two promotion levels preserve descendant membership, leaf-weighted means, endpoint references, and rebuild-stable versions.')
print('100 dynamic operations passed recursive reconstruction and idempotent rebuild checks.')
print('Overlapping stale edits and endpoint-change edits rejected before mutation; disjoint edits accepted.')
print('ABA value restoration does not revive an old edit version.')
print('Explicit policy: endpoint footprints, persistent family IDs by grouping key, descendant versions, optimistic atomic commit.')
print('Concurrency result is an interleaving model, not a threaded or distributed implementation.')
