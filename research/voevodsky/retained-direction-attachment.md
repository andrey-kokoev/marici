# Direction interaction: an explicit coefficient-matched pullback

## Domains and maps

The point attachment left two direction complexes at the root F_ABC: the host's disk link H and the electron's sphere link E. Keep both, and define their interaction using the already generated coefficient interface.

Use the actual source projector P=L_AB and the derived local phase registration D. For host-link position x and electron boundary vector e, define

```text
f_H(x) = P(x-F_ABC),
f_E(e) = D conjugate(P)e.
```

The relation is the literal set of pairs with equal readout:

```text
Q = {(x,e) in H × E : f_H(x)=f_E(e)}.
```

This is a pullback of direction maps. Unlike the preceding point pushout, it specifies which retained directions are compatible. H is the fixed link of the host's existing face-center vertex, not a new inward-growth construction. Its vectors use the barycentric link representatives; no unit-length normalization is silently applied.

## A useful exact identity

Let R exchange tetrahedron vertices A and B while fixing C and D. The checker derives from the actual coefficients

```text
D conjugate(P) = P R.
```

This is an identity for the selected local mode. It does not contradict the previous failure of a single rigid permutation to match the full 36-coordinate return: the present domains and operator are local.

Also P F_ABC=0. Thus the equal-readout condition can be expressed in the same triangular quotient chart used by P, after swapping the electron's A/B barycentric coordinates.

## Entire fibers, not just samples

For electron barycentric coordinates λ, define

```text
u = quotient(swap_AB(λ)),
quotient(λ) = (λ_A+λ_D/3, λ_B+λ_D/3, λ_C+λ_D/3),
m = min(u_A,u_B,u_C).
```

The real kernel of P is the normal line to ABC; the real rank is two. Therefore equality in this chart is equivalent to equality of the actual coefficient outputs.

The host link maps bijectively to the image triangle. Its inverse is

```text
x_H(u) = (u_A-m/4, u_B-m/4, u_C-m/4, 3m/4)
```

in host tetrahedron barycentric coordinates. Indeed the host link is characterized by λ_D=min(λ_A,λ_B,λ_C), and the displayed formula uniquely solves that condition together with quotient(λ)=u.

The electron sphere supplies

```text
e_upper(u) = swap_AB(u_A,u_B,u_C,0),
e_lower(u) = swap_AB(u_A-m,u_B-m,u_C-m,3m).
```

These are the two endpoints of the kernel chord through the electron tetrahedron. For m>0 they are distinct; for m=0 they coincide. These formulas give the complete fiber, not a selected pair out of an unexamined larger set.

Consequently every electron direction determines exactly one compatible host-link point. Q is the graph of that map and is homeomorphic to the electron sphere. Its host projection is two-to-one in the image interior and one-to-one on the seam. The pullback's pair representation supplies its universal property; the formulas provide the explicit realization.

## Retained finite atlas

Construct a common subdivision rather than identifying original flags that cross the fold:

| Complex | Vertices | Edges | Triangles |
|---|---:|---:|---:|
| Refined host link | 13 | 30 | 18 |
| Coefficient image chart | 13 | 30 | 18 |
| Paired direction pullback | 20 | 54 | 36 |

All original host-link vertices and all fourteen electron direction vertices remain. Each new triangle records its original electron flag owner, and all 24 owners occur. The additional triangles refine retained cells; they are not an extra solid carrier.

The host/electron maps are affine on each refined triangle. The checker verifies the actual coefficient equality on its vertices and an interior point, and verifies a common minimum-coordinate branch on every triangle. Exact rational chain ranks give disk homology for the host/chart and sphere homology for Q. The graph construction and explicit inverse establish the sphere topology beyond the homology check.

## What changed

The two retained direction complexes now have a specified interaction: matching the generated coefficient readout. This does not collapse the electron sphere to the host disk. Both compatible electron directions remain in Q, and their seam identification is explicit.

The two sheets belong to one connected direction sphere. They are not hydrogen and deuterium, nor do they require a neutron. They are also different from the two conjugate coefficient presentations: the phase alignment has already been applied, so paired directions have equal readout.

This completes the direction-level relation. It does not identify radial parameters, impose a host-depth profile, or assert that the full solid attachment is this same two-dimensional pullback. Extending the relation to full cells requires specifying their maps, rather than reinstating the earlier arbitrary equal-depth constraint.

## Reproduce

```text
python research/voevodsky/checkers/check_retained_direction_attachment.py
```

Fifteen exact checks pass. The `retained_direction_attachment_store.json` artifact contains all paired vertices, the 36 triangles, their original flag owners, and both maps. `retained_direction_attachment.json` records chain ranks, formulas, source and checker hashes. No prior source or visualization is modified.
