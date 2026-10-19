# P/E contraction coherence cube

The guarded support rewrite C commutes with endpoint half-turn G and reader
reversal B under the explicit carried-reference convention.

Tested 30 local rewrite instances:
- 24 hydrogen markings;
- 3 shortcuts across two experimental N-14 configurations;
- 3 shortcuts across two experimental Ne-21 configurations.

All six faces of each cube commute: 180 full-state equalities. Both involutions
square to identity before and after contraction. Ninety corrupt-reference,
wrong-boundary and coefficient-mismatch controls are rejected.

## Actions and guards

G permutes the six reference vertex positions in the C0/M2, M0/C2, C1/M1 pairs,
carrying reader identities and coefficient bases unchanged. For isotope cases
it is a local coordinate permutation of that reference patch within the saved
coordinate dictionary; it is not an eversion of the entire nucleus. All other
coordinate entries stay fixed.

B exchanges M/C and P/E reader roles, reflects indices, reorders context/window
slots, exchanges entry/exit, reverses selected native arrows and inverts maps.

C replaces the same-origin two-factor reference path with its composed PE map,
removing occupied N support while preserving reference support. Vacancy,
endpoint edge and selected-reader boundary conditions are checked explicitly.

The backward boundary condition is the **incoming-arrow counterpart** of the
forward outgoing-arrow condition. It is transported with B, not independently
assumed to retain its forward wording. This is why an entry-side dual of a
terminal rewrite belongs in the same square.

The compared states include marked frames, boundary, reference coordinates,
selected native arrows, environment occupancy, support sets and coefficient
maps—not merely isotope counts.

## Meaning and limits

Within these definitions, contracting then reversing equals reversing then
applying the transported contraction. This provides a coherent experimental
rewrite in all four endpoint descriptions. The backward rule is defined by
transport; agreement checks implementation consistency rather than deriving
that rule independently. The coordinate action carries a fixed reference basis;
a geometry-induced coefficient representation remains separate.

This local cube does not certify transformed whole-isotope shape admission,
interior isotopy, global field sewing or arbitrary simultaneous contractions.
The occupancy permission remains the explicit experimental rule. Production
and viewer remain unchanged.

```sh
node research/strominger/checkers/check_contraction_coherence_cube.mjs
```

Receipt: `results/contraction-coherence-cube/verification.json`.
