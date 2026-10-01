"""Integrate event-derived scope transport with fresh member-vector commits."""
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import runpy

here=Path(__file__).parent
Store=runpy.run_path(str(here/'check_recursive_record_transactions.py'))['Store']
Change=runpy.run_path(str(here/'check_scoped_edit_transport.py'))['Change']

s=Store()
s.set_leaf(0,0,1,F(2)); s.set_leaf(1,0,1,F(4))
request=s.snapshot_vector({0:2,1:2})
s.set_leaf(2,0,1,F(10))
# Rebase is never automatic, even if the original vector can still commit:
# insertion outside an explicit vector's scope does not invalidate its reads.
before=deepcopy(s.__dict__)
assert s.rebase_vector(request) is None
assert s.__dict__==before
fresh=s.rebase_vector(request,approved=True)
insert=Change(frozenset({0,1}),frozenset({0,1,2}),{0:0,1:1},{2:F(10)})
expected=insert.edit({0:F(2),1:F(2)})
assert {m:dict((i,d) for i,_,d in fresh.entries).get(m,F(0)) for m in s.leaves}==expected
before_values={m:r.value for m,r in s.leaves.items()}
assert s.commit_vector(fresh)
assert {m:r.value-before_values[m] for m,r in s.leaves.items()}==expected
assert s.leaves[2].value==10
rid=next(iter(s.levels[0]))
assert s.levels[0][rid].value==F(20,3)
event_index=len(s.events)-1
assert s.vector_events[event_index]==fresh
assert fresh.parent==request and fresh.transport_events==(request.cursor,)
# Every member is validated before ANY mutation, including late stale entries.
stale=s.snapshot_vector({0:1,1:3})
s.set_leaf(1,0,1,F(8))
before=deepcopy(s.__dict__)
assert not s.commit_vector(stale)
assert s.__dict__==before
approved=s.rebase_vector(stale,approved=True)
assert approved.entries!=stale.entries
# Approval/snapshot is not a reservation; another write can invalidate it.
s.set_leaf(0,0,1,F(20))
before=deepcopy(s.__dict__)
assert not s.commit_vector(approved)
assert s.__dict__==before
approved_again=s.rebase_vector(approved,approved=True)
before_values={m:r.value for m,r in s.leaves.items()}
assert s.commit_vector(approved_again)
assert s.undo_last()
assert {m:r.value for m,r in s.leaves.items()}==before_values
assert not s.commit_vector(approved_again)
assert s.vector_events  # compensation did not erase accepted provenance

# Deletion followed by compensation restores content but not transported scope.
restoration_request=s.snapshot_vector({0:7,1:9})
s.delete(0)
assert s.undo_last()
restored=s.rebase_vector(restoration_request,approved=True)
assert {m for m,_,_ in restored.entries}=={1}
original_value=s.leaves[0].value
assert s.commit_vector(restored)
assert s.leaves[0].value==original_value
# Successive explicit rebases compose on scope just like a single rebase.
origin=s.snapshot_vector({0:1,1:2,2:3})
s.delete(2)
mid=s.rebase_vector(origin,approved=True)
s.set_leaf(3,0,1,F(100))
last=s.rebase_vector(mid,approved=True)
direct=s.rebase_vector(origin,approved=True)
assert last.entries==direct.entries
assert last.parent==mid and direct.parent==origin
assert s.commit_vector(last)
assert s.leaves[3].value==100
# Foreign store snapshots are not admissible local requests.
foreign=Store(); foreign.set_leaf(0,0,1,F(0))
before=deepcopy(s.__dict__)
assert not s.commit_vector(foreign.snapshot_vector({0:1}))
assert s.rebase_vector(foreign.snapshot_vector({0:1}),approved=True) is None
assert s.__dict__==before
print('Transported vectors commit atomically in the recursive Store; inserted values remain untouched.')
print('Actual event-derived insertion transport matches the pure partial-injection model.')
print('Unapproved rebase, stale batch, intervening post-approval write, and foreign-store request leave full store unchanged.')
print('Vector compensation restores values with fresh versions and retains accepted provenance.')
print('Delete/restore drops old scope; repeated rebases compose on entries while retaining distinct provenance chains.')
print('Local trusted, serialized model only: no authentication, threaded locking, or crash-safe journal.')
