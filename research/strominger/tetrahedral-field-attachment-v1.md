# Attaching the channel field to tetrahedral geometry

## Derived P attachment

Reconstructed the prior native proton construction from its four geometric
vertices and two oriented seed cycles, then compared every full L/G/return
coefficient with the retained native protocol. All match exactly.

1. Split each tetrahedral face into three triangles by joining its centroid
   to its corners. This gives 12 outward-oriented small triangles, one per
   directed outer edge.
2. Each triangle carries a complex three-component spatial vector. Its local
   selected line is `v_g = X_g (1, omega, omega^2)`, where X_g contains its
   three vertex positions and omega is the chosen nonreal cube root of unity.
3. Let R_g rotate the reference triangle to that triangle. Then
   `v_g = R_g v_0`, and alignment transports the vectors into one frame.
4. The native operators are exactly

```
L[g,h] = delta(g,h) P_g
G[g,h] = R_g R_h^T / 12
P_g    = v_g v_g^dagger / (v_g^dagger v_g)
```

Their product equals the native rank-one return operator, coefficient by
coefficient. Thus the 36 entries really can be pictured as three spatial
components attached to each of 12 surface patches for this P construction.

## What the grid columns mean geometrically

The three reference axes connect midpoints of opposite edge pairs:
AB/CD, AC/BD, AD/BC. Each R_g is a signed permutation in this frame.

All 12 rows of the previously reconstructed support grid coincide with the
12 geometric patch labels. Its three columns coincide exactly with the three
**co-moving reference axes**, not necessarily the same ambient x/y/z component
on each patch. The checker verifies every one of these assignments.

Back-transporting a field by `y_g=R_g^T x_g` gives

```
L' = I_12 tensor P_0
G' = (J_12 / 12) tensor I_3.
```

The earlier return-column rescaling additionally converts P_0 to a weighted
mean on three components. Consequently the abstract grid factorization and
this spatial field construction are two coordinate descriptions of the same
native P operators.

This uses cyclic complex phases and frame transport, not merely incidence
between face/corner flags and opposite-edge matchings. That distinction is
why bare incidence previously gave the wrong rank.

## Binding to the actual P facet of T

Every saved T metric makes the P facet `abuv` a regular tetrahedron with edge
square 2. The source tetrahedron has edge square 8. Scaling its coordinates by
1/2 gives exactly the P metric, and does not change the local projectors or
rotation transport.

A concrete marked binding is `A->a, B->b, C->u, D->v`. Its choice is explicit;
unmarked T does not select a unique seed orientation or nonreal character.
All 24 saved metric cases pass this metric test.

## Extension gate: N is not a mere relabelled copy

N has the same two-direction factorization with projection roles exchanged,
but its source weights differ. A permutation plus any invertible diagonal
phase/amplitude rescaling preserves the multiset of return-projector diagonal
entries. P and N have different such multisets.

Therefore a simple facet relabelling with only diagonal fiber gauge cannot
convert the full P pair into the native N pair, even after exchanging L/G.
This does not contradict the previously established abstract metric-unitary
equivalence: that equivalence can mix coordinates beyond a monomial change.

A global field must derive that additional mixing or the neutron-specific
geometric/occupation data. E requires its own rank-two internal field as well.
The common-edge restriction maps between these native fields remain open.

## Verification

```sh
python research/strominger/checkers/derive_tetrahedral_field_attachment.py
```

Evidence: `results/tetrahedral-field-attachment/verification.json`.

This is a fresh reconstruction and T-facet binding of an existing geometric
proton law, not a claim that the native producer's geometry was newly discovered.
Production/viewer unchanged.
