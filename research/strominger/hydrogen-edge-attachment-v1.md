# H-1 / H-2 edge-attachment probe

## Result

The proposed P–E **edge geometry is already present** in the existing native
P->N->E construction. In all 24 ordered root markings, the proton and electron
share exactly the edge **C1–M1**, not a face.

The protocol's full tetrahedra are:

- P: C0, M0, C1, M1;
- N: M0, C1, M1, C2;
- E: M1, C1, C2, M2.

Thus retaining P and E while leaving N unoccupied gives a non-face-sharing
1P/0N/1e geometry with the original global C/M role guards intact. Occupying
that same reference N gives the native 1P/1N/1e construction without moving
the P or E endpoints. Across the 24 markings, 8 E cells have regular-tetrahedron
geometry and 16 have split geometry; these are shapes, not proton species.

This confirms the geometric part of the conjecture. **It does not yet supply
an admitted direct P->E transfer.**

## What the source rules certify

For every marking:

- [P,N,E] passes original whole-configuration contact/exit inspection and is
  rooted by its two actual face transfers;
- [P,E] passes the occupancy/context/contact guards but fails exit certification:
  the proton cannot reach the electron through selected native operations;
- attempting a `PE-edge` operation is rejected as an unknown native transfer.

The shared body edge must not be confused with a shared ordered active window.
P's active window is C0 M0 C1 and E's is M1 C1 C2: their active windows share
only C1. M1 is P's context vertex and an active E-window vertex. An edge rule
therefore needs an explicit context-to-window identification, not just a new
neighbor predicate.

## Candidate reference-mediated map

The already validated full-coordinate permutations compose as

```
PN = [3,1,2,0,4]
NE = [0,4,2,3,1]
NE after PN = [3,4,2,0,1]
```

For every marking the composite reproduces the native final E packet at the
same origin and retains all five coefficient coordinates. But it depends on
the intervening N reference/chart. Algebraic composition of two certified face
maps is not proof that transfer can occur with that intermediate carrier
unoccupied. Nor does it uniquely derive an edge-local interaction from just two
shared vertices. No virtual neutron or physical electron-binding mechanism is
inferred.

The concrete candidate hypothesis is to separate **reference availability**
from **occupied transport-carrier availability** for this composed map. That
would be a new, explicit admission law. It has not been silently added to the
generator, solver, hydrogen viewer or isotope selectors.

## Relation to N-14

This demonstrates a general representational gap using H-1 independently of
N-14: the current native face-path grammar needs an occupied N to connect these
P/E endpoints. The N-15-minus-one-neutron probes also lose rooted paths, but
the two promising deleted neutrons supply inverse-PN access to proton branches,
not merely NE exits. Therefore a P->E edge rule alone is not yet shown to repair
those N-14 arrangements. Their nuclear entry connections must still be checked.

Nuclear spins are 1/2 for H-1 and N-15, and 1 for H-2 and N-14. No angular
momentum representation or spin-composition law was derived in this probe, so
these values cannot be used as a geometric certificate.

## Evidence and reproduction

```sh
node research/strominger/checkers/probe_hydrogen_edge_attachment.mjs
```

`results/hydrogen-edge-attachment/verification.json` saves every marking,
actual coordinates, shared edge, packet permutations, native operation maps,
H-1/H-2 inspection results and source hashes. The finite scope is the existing
uniform subdivision and the grade-zero PN/NE pair, not arbitrary hydrogen
representations or physical binding. Production and viewer remain unchanged.
