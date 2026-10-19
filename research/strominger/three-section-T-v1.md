# T with three section choices: first incidence model

The conjecture asks whether P/N/E are restrictions of one object, selected by
which of three configuration coordinates is held fixed.

## What the actual four-position readers supply

All three bodies contain the common C1/M1 edge. Retain that common core and
inspect the remaining positions:

| Reader | Remaining positions |
|---|---|
| P | C0, M0 |
| N | M0, C2 |
| E | C2, M2 |

These pairs form an open chain of four labels. Three coordinate planes in a
three-coordinate reference would instead have pairs (a,b), (b,c), (c,a).

The checker enumerates all six possible identifications of one pair among
C0,M0,C2,M2. Exactly one gives three distinct two-coordinate sections with no
collapsed section: the **C0/M2 seam**.

Introduce abstract reference classes

```
a = [C0 ~ M2]
b = [M0]
c = [C2]
```

Then the reader incidence is

| Presentation | Varying coordinates | Fixed coordinate |
|---|---|---|
| P | a,b | c |
| N | b,c | a |
| E | c,a | b |

This is a precise combinatorial realization of the proposed three-section
pattern, conditional on the explicit seam. It is not yet a geometric manifold
or proof that the classes are the physical/configuration M,C,R coordinates.

## Why the seam is a substantive condition

C0 and M2 have distinct spatial coordinates in every one of the 24 hydrogen
reference embeddings. They also have different C/M roles and occurrence
indices. Identifying them as one physical vertex would violate the existing
reader checks. The proposed identification is instead a cycle-boundary gluing
between reference presentations; its role/index/metric transition needs an
explicit law. A chosen abstract quotient is not itself that law.

No coefficient amplitude equality between C0 and M2 is imposed. M2 is outside
the original five-slot coefficient reference, so the original invertible maps
cannot be advertised as directly supplying this six-label gluing.

## Reversal is compatible with the incidence pattern

The earlier six-label involution exchanges C0/M2, M0/C2, C1/M1. It preserves
the seam and acts on the abstract classes as

```
a -> a, b <-> c
```

Therefore it exchanges the P and E sections and preserves N, exactly as in the
previous reader reversal. This agreement is a useful compatibility check on
the proposed section model.

## Coefficient triangle

The existing PN and NE maps admit a formally closing E->P chart transition
chosen to be their inverse composite, `[3,4,2,0,1]`. The three maps compose to
identity. This is algebraic chart completion by definition, not a discovered
native E-outgoing operation or a derivation of the C0/M2 seam. Native incidence,
coefficient transition and reference-support contraction remain distinct layers.

## Next mathematical question

Supply an admissible boundary transition for C0/M2 that carries its roles,
indices, geometry and coefficient reference. Then determine whether its three
section classes can be assigned to M,C,R and whether the native channel maps
(12/3, 3/12, electron sectors) arise as restrictions of the same object.

Production/viewer unchanged.

```sh
node research/strominger/checkers/probe_three_section_T.mjs
```

Evidence: `results/three-section-T/verification.json`.
