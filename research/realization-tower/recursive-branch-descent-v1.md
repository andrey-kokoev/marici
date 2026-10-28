# Recursive branch promotion and connectivity re-probing

## Tested interpretation

Operator instruction: after stepping into a coherence-path branch, descend and
probe connectivity again, rather than keep extending one fixed-level object.

A relevant existing constructor is the
[retained line-graph promotion](../nima/retained-line-graph-cycles.md): each
relationship becomes a record holding its endpoints, and new relationships
retain their shared prior endpoint as a witness. This is an established
candidate generative rule, not an already-proved identification with numerical
rung descent or the whole WG system.

The test imports the owner's actual `promote` implementation and runs its
regression checks. Its receipt is captured locally; the owner's receipt is not
overwritten. Every comparison-selected shortest path is then tested separately.

## Recursive procedure

1. Take one path produced by the compare-first search, with both marked poles.
2. Promote its actual relationship graph using the owner constructor.
3. Transport each marked probe to the new records incident to its preceding
   marked records.
4. Recompute connectivity and distance in the NEW graph.
5. Retain all endpoint ancestry and shared-record witnesses; repeat until the
   two transported probe sets share a record, or connectivity fails.

No arbitrary decrement of a distance variable is used: BFS computes distance
from the actual generated incidence at each level. Every prior edge is
reconstructed from the promoted records.

## Fresh results

| Initial separation | Tested branches | Record counts by depth | Re-probed separation |
|---:|---:|---|---|
| 4 | 36 | 5,4,3,2,1 | 4,3,2,1,0 |
| 6 | 400 | 7,6,5,4,3,2,1 | 6,5,4,3,2,1,0 |

Every branch reaches one final retained record containing recoverable ancestry
of both poles and every intermediate path vertex. Each new adjacency's witness
is checked against the actual intersection of predecessor endpoint records.
Two disconnected edges remain disconnected under the same rule.

This is the expected identity L(P_n)=P_(n-1) for path graphs, executed with the
existing retained constructor and marked probes. It demonstrates a genuine
change of representation and re-probing, not a newly discovered connection
between previously disconnected objects.

## What survives, and what is not closed

The operator's recursive pattern has a concrete working instance: a relationship
at one level becomes an object at the next, and the probe relation is tested
there with all history retained.

However:

- The input branches were already connected paths. This procedure does not
  independently discover their existence or select one physical branch.
- Each four-step terminal record is distinct from the other 35; each six-step
  terminal record is distinct from the other 399. Equal singleton dimensions
  do not identify them.
- This promotes the selected branch, not the full surrounding lattice, all
  comparison slots or the complete cellular object. Promotion depth is not
  silently labelled rung12, rung11, etc.
- Cross-branch comparison/fillers are still needed to construct one complete
  coherence package from these results. No particle census follows merely
  from 400 terminal branch records.

The new narrower gate is **compatibility among the retained descended branch
records**, with their common source, interfaces and witnesses—not another
fixed-level P→N→E path attempt.

## Verification

`python research/realization-tower/check_recursive_branch_descent.py` freshly
passes. [Receipt and complete ancestry archives](results/recursive-branch-descent-v1.json).
No formal proof-assistant closure or isotope identification is claimed. No
prior graph proof outcome or glossary definition was changed.
