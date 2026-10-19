# Structural synthesis: reversibility versus occupied support

## The question resolved

Does the demonstrated local reversal imply that a terminal P/E connection can
remain when its intervening neutron is unoccupied?

**No: these are separate structural properties.** Reversal is compatible with
the proposed shortcut, but does not derive its occupancy rule.

## Three layers that must remain distinct

1. **Reference geometry:** positions, C/M marks, context and full coefficient
   coordinates needed to specify a reader and its transfer map.
2. **Occupied support:** which bodies must actually be retained for that map to
   be an admitted construction operation.
3. **Directed reading and boundary:** which way the map is traversed and which
   reader records act as entries or exits.

The earlier reversal experiment changes layer 3 and transforms the roles in
layer 1. The successful terminal shortcut changes layer 2. Conflating these
would hide the actual new assumption.

## Algebra with support retained

Annotate a native transfer by its endpoints, coefficient map and occupied-body
support. Then

```
PN: P -> N, support {P,N}
NE: N -> E, support {N,E}
NE after PN: P -> E, support {P,N,E}
```

Composition unions support. Reversal inverts the map and exchanges endpoints,
but retains the same occupied support:

```
reverse(NE after PN) = reverse(PN) after reverse(NE)
support remains {P,N,E}
```

The candidate edge rule is a different operation on this annotated structure:

```
keep the composed map and reference geometry
change required occupied support {P,N,E} -> {P,E}
```

This is **reference-mediated support contraction**. It is not ordinary path
composition and not merely turning an arrow around. In these tested triples,
contraction commutes with reversal, so both the three-body rule and the
contracted two-body rule are reversible. Symmetry cannot select between them.

## Checks on the actual witnesses

The checker verifies the support/map identities on all 24 hydrogen markings
and all 14 eligible shortcut terms across the saved N-15/Ne-22 neutron-deletion
families. Each term has exactly one missing support body: the reference N.
The full five-coordinate composite is unchanged by contraction.

As a separate diagnostic, allow EVERY selected native edge to run in both
directions. This is more permissive than an admitted directional construction.
Even then, the four successful terminal-shortcut candidates retain disconnected
records:

| Target/source deletion | Unrooted records after all native arrows become bidirectional | Experimental PE shortcuts |
|---|---:|---:|
| N-14, N-15 cell 16 removed | 1 | 1 |
| N-14, N-15 cell 17 removed | 2 | 2 |
| Ne-21, Ne-22 cell 16 removed | 2 | 2 |
| Ne-21, Ne-22 cell 29 removed | 1 | 1 |

Thus these particular failures are not repaired by arrow reversal alone. The
edge shortcut supplies missing adjacency, not merely the direction of an
existing occupied connection.

## What is now a coherent candidate principle?

A direction-independent formulation would refer to a boundary reader, not a
privileged physical electron or a last construction step:

> A boundary transfer may be represented by a composed reference path whose
> intermediate geometric carrier need not be occupied, provided an explicit
> support-contraction law admits it.

In the forward examples this is a terminal P-reader -> E-reader edge. Under
the tested dual it becomes an entry-edge counterpart. This is a proposed
principle, not yet an admission law derived from the prior mode-space math.

The specificity matters. The present checks justify neither arbitrary removal
of internal neutron bridges nor contraction of arbitrary chains. Terminality,
full coefficient/reference preservation and global selected-body consistency
are candidate restrictions. Their necessity and sufficiency must be derived or
tested separately; the positive examples alone cannot establish uniqueness.

## Consequence for the research direction

The next foundational question is **when reference geometry must be occupied**,
not whether all arrows should simply be reversible. The prior grammar already
allows reference-only proton geometry; the proposed rule would permit a
particular reference-only neutron-mediated map as well. That analogy motivates
an investigation, but does not automatically transfer the permission.

No new native witness, isotope stability claim or viewer admission follows from
this support bookkeeping. The experimental N-14 and Ne-21 successes retain
exactly the added premise identified above. Production remains unchanged.

## Evidence

```sh
node research/strominger/checkers/probe_reversal_support.mjs
```

`results/reversal-support/verification.json` stores hydrogen cases, native and
contracted support terms, reversed maps, bidirectional reachability diagnostics
and source hashes. Related reports: `terminal-pe-probe-v1.md`,
`isotope-reversal-v1.md`, `dual-isotope-rules-v1.md`.
