# Pentachoron contact interfaces and reversible boundary reconnection

Date: 2026-10-11
Status: Constructive extension of the supplied classical collision toy.

## Result

A complete triangular interface appears in the nearest-nonoverlapping comparison configuration on the fastest of three tested trajectories. A new, explicitly declared local face-pairing rule then admits either the original two boundary components or one connected closed boundary. The connected boundary is a candidate merging intermediate, not an identified or stable particle.

Neither a transition probability nor a physical collision speed is inferred.

## Inherited inputs

- The five marked vertices of `andrey-kokoev/marici/research/voevodsky/electron-pentachoron-attachment.md`; source blob `68bd9714ad40b5ebc0512ab69f7de873714014a2`.
- A pair mirrored across the spatial collision midplane, with common x–w internal rotation.
- The preceding nearest-nonoverlapping retained-vertex comparator, its metric-derived inertia, and zero alignment energy. The baseline script SHA is checked before reuse.
- The right-hand input boundary has the orientation induced by its spatial reflection. This remains a model convention, not a derived positron transformation.

The source notes distinguish geometric port identification from equality of independent phase states. Their retained-provenance and matched/mismatch approach is used here as an interface principle. No native electron spinor adapter is supplied by the new calculation.

## 1. Exact contact geometry

In length units ell, the centered vertices are

    A=(1, 1, 1,-1/sqrt(5))
    B=(1,-1,-1,-1/sqrt(5))
    C=(-1,1,-1,-1/sqrt(5))
    D=(-1,-1,1,-1/sqrt(5))
    E=(0,0,0,4/sqrt(5)).

After an x–w rotation, the maximum positive x extent is

    a(delta)=max(cos(delta)-sin(delta)/sqrt(5),
                 4 sin(delta)/sqrt(5))

on the orientation interval studied here. At center distance 2a(delta), the mirrored pair meets along:

| Internal angle | Full retained interface |
|---|---|
| Below atan(1/sqrt(5)) | Edge AB |
| Exactly atan(1/sqrt(5)) | Triangle ABE |
| Above atan(1/sqrt(5)), on the tested branch | Vertex E |

The critical angle is 24.0948425521 degrees. At that angle, E projects to the midpoint of AB. Nevertheless, E differs from that midpoint by sqrt(6) ell in w. The full triangular Gram matrix, based at A, is

    ell^2 [[8,4],[4,8]].

Its determinant is 48 ell^4 and its area is 2 sqrt(3) ell^2. The spatially projected Gram determinant is zero. The retained triangle must not be replaced by its projected segment, or E identified with the midpoint record.

Enumerating all vertex bijections gives one zero-displacement matching in the frozen mirrored pose for each interface. Abstract intrinsic isometries of a face are not extra zero-cost arrows at that pose.

## 2. Contact identification is not yet recombination

The direct quotient of two pentachoron boundaries along the shared vertex, edge or triangle is a singular junction. Exact link checks expose the singularities. Mere boundary identification is therefore not advertised as a smooth outgoing boundary.

The new rule resolves only fully coincident triangular faces:

1. Keep all ten original tetrahedra and their occurrence records.
2. Cut the two existing tetrahedron adjacencies across the common triangle, one in each constituent.
3. Pair the resulting four triangular face occurrences, preserving the fixed induced orientations.
4. Retain the old pairing and the new instruction so the operation can be reversed.

At F=ABE, each input has exactly two adjacent tetrahedra: the cells omitting C and D. The original pairing is

    L_omit_C <-> L_omit_D
    R_omit_C <-> R_omit_D.

The orientation-compatible crossed pairing is

    L_omit_C <-> R_omit_C
    L_omit_D <-> R_omit_D.

There are three raw perfect pairings of four face occurrences. Exactly two preserve the frozen input orientations: the original and this crossed pairing. The third is not admitted under that rule.

Vertex and edge contacts contain no full triangular face, hence supply no such switch under this particular rule. This is not a general prohibition on other interactions at those contacts.

## 3. Exact boundary verification

| Allowed pairing | V,E,F,T | Rational Betti numbers | Connected components |
|---|---|---|---:|
| Original | 10,20,20,10 | 2,0,0,2 | 2 |
| Crossed | 7,17,20,10 | 1,0,0,1 | 1 |

Both have two incident tetrahedra at every triangle, circular edge links, and spherical vertex links. The fixed oriented top-dimensional chain closes. The crossed result is consequently a connected closed orientable three-dimensional boundary complex with rational sphere homology. This calculation does not infer its stable physical realization, a four-dimensional filling, or a photon interpretation.

Two distinct triangular face occurrences in the crossed result have the same vertex labels. They remain separate cells of a face-paired delta-complex. Deduplicating cells merely by vertex sets would destroy the resolution and recreate the singular contact quotient.

An exact serialization/replay check recovers every original cell occurrence, and restoring the recorded pairings inverts the switch. A unitary matched/mismatch transform on independent boundary-coordinate slots also passes exact inversion and norm tests:

    (x,y) -> ((x+y)/sqrt(2), (x-y)/sqrt(2)).

This coordinate transform is not a dynamical transition amplitude. Discarding the mismatch would erase independent inputs.

## 4. Collision-path annotations

The relevant interface during penetrative soft contact belongs to the nearest admissible comparator, not to a separately realized physical configuration. The variational comparator can stay at the critical angle for a finite interval even while the actual angle continues changing.

Reintegrating the preceding unmodified collision dynamics gives:

| Speed in previous v0 units | Comparator contact sequence |
|---|---|
| 0.70 | AB, then separation |
| 0.90 | AB, separation, E, separation |
| 1.20 | AB, ABE, E, separation |

Here v0=sqrt(2 E_*/m), not c. In time units ell sqrt(m/E_*), the last run's triangular-comparator interval is

    0.753086169436 < t < 0.962598995088.

An independent RK45 integration reproduced the endpoints within 1.5e-10 time units. The interval endpoints were located from the one-sided derivative conditions at the comparator's support-function corner, then checked against the full comparator. They are not defined by an adjustable angular tolerance.

These are opportunities for the proposed reconnection along the original trajectories. The face-pairing switch has not been coupled back to motion, and no post-reconnection outgoing trajectory is calculated.

## Scope and next construction

Established within the declared model: exact retained contact faces, a reversible orientation-compatible boundary-reconnection instruction, its topology checks, and a speed-dependent opening of that instruction on the three tested classical paths.

Not established: native spinor sewing, the reconnection trigger or its complex amplitude, a force law after reconnection, bound-state/stability criteria, two- or three-photon production, or a relativistic/physical speed scale. Two allowed pairings do not imply equal probabilities.

The next construction is the phase-compatible transition operator between the unjoined pair and the connected boundary, retaining the comparison and gluing records rather than deleting their independent information.
