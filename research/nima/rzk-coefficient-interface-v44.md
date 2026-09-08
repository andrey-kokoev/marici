# v44: native endpoint and Q projection vectors

**Support/regulator update:** [`rzk-coefficient-interface-v45.md`](rzk-coefficient-interface-v45.md)
separates the central shifted Gysin channel, constructs the three-pair PC Q
section, and records the beta-zero `(beta,X35)` supported-map difference.

Iteration 4 replaces the remaining symbolic projection labels by finite Rzk
vectors in the unit-linearized, common-prefactor frame.

`rzk/56-d03-native-endpoint-q-vectors.rzk.md` defines the complete normalized Q
coordinate vector

    T - h03 - h14 - h25.

Its boundary map sends `T` to the three long facets and each marked normal to
its matching facet. Rzk proves the four-term vector is a cycle and that its top
coordinate is the primitive integer one.

The endpoint projection is the two-coordinate vector

    E_minus + E_plus_occ,

where the positive coordinate is explicitly the separate occurrence partner,
not the native marked-35 state. Its endpoint differential has six separately
labelled connector coordinates, three on each endpoint packet.

Finally, finite linear projections from the specialized packet are defined and
Rzk proves that `Z=Hmu-S` has exactly the displayed four Q coordinates and two
endpoint coordinates. The common polynomial prefactors and unit frame are
absorbed into the homogeneous coordinate bases, as in the certificate's
oriented unit-linearized presentation; no coefficient is evaluated to one
outside that declared frame.

A fresh 71-file transitive closure passed in 30.61 seconds. Evidence:
`results/56-d03-native-endpoint-q-vectors.typecheck.json`.

Together modules 53--56 now cover the four requested steps: specialization,
full supported-cone exactness, three-carrier separation, and native finite
endpoint/Q projections. The remaining 41 short-support correction terms and
full 430-state realization are still certificate-backed and are a larger
future refinement rather than part of this four-iteration objective.
