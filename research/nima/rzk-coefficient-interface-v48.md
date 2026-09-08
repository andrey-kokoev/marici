# v48: beta endpoint-Q transgression

**Cubical dual completion:** [`rzk-coefficient-interface-v49.md`](rzk-coefficient-interface-v49.md)
adds the actual complementary-support relative edge realizing the primitive
reverse short-to-generic transgression.

`rzk/63-beta-endpoint-q-transgression.rzk.md` records the forced compatibility
between the two endpoint-leading top-cycle directions and the generic quotient.
The negative-endpoint direction has Q order beta squared; the positive-endpoint
direction has zero Q projection. These are distinct leading endpoint labels,
not the older fixed-beta endpoint signature type.

The short attaching class is represented by a beta-graded two-state packet
with

    d W = beta^2 chi.

Rzk proves every beta-squared multiple is a boundary and defines a detector
which evaluates `beta*chi` to one while vanishing on every boundary. Hence the
lower obstruction concealed by the Q-nullhomotopy is mechanically retained as
nonzero. A separate framing classifier records that ordinary short-boundary
homology has beta-square annihilator, whereas strict endpoint-coordinate
framing makes the same generated class faithful by excluding the endpointful
primitive.

A fresh 73-file transitive closure passed in 37.77 seconds. Evidence:
`results/63-beta-endpoint-q-transgression.typecheck.json`.

Scope: the native 18-term chi vector, 41-term W vector, endpoint corrections,
full beta-dependent four-term Q cycle, beta^48 completeness minor, and twelve
first-order endpoint-fixed obstructions remain certificate-backed. No claim is
made that strict coordinate framing is the physical homotopy-coherent endpoint
category, and the class is not identified with physical Delta_J.
