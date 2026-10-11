# Full-cell coefficient attachment: a four-dimensional relation

## Construction

Extend the same maps used for the direction pullback to the actual local solids:

- H is the host attachment star: the tetrahedral region with vertices O,A,B,C, subdivided into its six retained flag tetrahedra. Its marked attachment vertex is F_ABC on the boundary. The rest of the host remains unchanged.
- E is the complete new electron tetrahedron, with all 24 retained flag tetrahedra.
- Use the original local projector P=L_AB and the already derived phase registration D.

The full relation is the pullback

```text
Q_full = {(x,e) in H×E : P(x-F_ABC)=D conjugate(P)e}.
```

No independent radial-depth equality is imposed. This is a space of compatible pairs, not a claim that two solids occupy one ordinary three-dimensional region.

## Exact coordinates

The verified identity D conjugate(P)=P R, where R exchanges electron vertices A and B, reduces the condition to equality of the quotient coordinates

```text
u = (λ_A+λ_D/3, λ_B+λ_D/3, λ_C+λ_D/3).
```

Write m=min(u_A,u_B,u_C). Every compatible pair is uniquely represented by

```text
u_i >= 0, sum(u_i)=1,
0 <= a <= m,
0 <= b <= m,

host barycentrics     = (u_A-a/4,u_B-a/4,u_C-a/4,3a/4),
electron barycentrics = swap_AB(u_A-b,u_B-b,u_C-b,3b).
```

Here a and b independently parameterize the two coefficient-kernel chords. They are not uniform radial expansion/contraction parameters. At fixed u, changing one moves its point along the local projector's kernel without moving the other point.

These formulas are an exact inverse parameterization of the pullback. The host inequalities λ_i>=λ_D characterize its attachment star; the electron inequalities are its usual nonnegative barycentric coordinates.

## Dimension and fibers

The image triangle contributes two coordinates. Over its interior, the compatible positions form the square [0,m]², contributing two more. The full relation is therefore **four-dimensional**.

It is a convex polytope in (u_A,u_B,a,b), with u_C=1-u_A-u_B and affine inequalities a,b>=0 and u_i>=a,b. The point (u_A,u_B,a,b)=(1/3,1/3,1/6,1/12) satisfies all these inequalities strictly, proving full dimension rather than relying only on a dimension count.

On the image boundary m=0 the square collapses to one point. The preceding direction pullback is the sublocus a=m and b=0 or b=m. Those two corners of each fiber form the previously constructed sphere; they are not the complete full-cell fiber.

The marked pair (host F_ABC, electron barycenter) is retained at u=(1/3,1/3,1/3), a=0, b=1/12. The mode constraint does not isolate this pair from all other compatible pairs.

## Retained cells

Refine by the original host and electron barycentric ordering planes. Six orderings of u specify the host sectors. Inserting electron coordinate D into each three-coordinate order gives four electron possibilities, hence 24 full-dimensional owner cells.

The exact polytopal complex has:

| Dimension | Cells |
|---|---:|
| 0 | 24 |
| 1 | 103 |
| 2 | 164 |
| 3 | 108 |
| 4 | 24 |

All six host-star flag owners and all 24 electron flag owners occur. Both projections are onto: for a given host point one may take b=0, and for a given electron point one may take a=0.

There are 36 internal three-faces, each with two owners, and 72 outer three-faces, each with one. The outer boundary has no unmatched two-faces. Cellular boundaries square to zero over F2, and the Betti numbers are (1,0,0,0,0). Convexity also establishes contractibility directly.

Every vertex and every owner-cell interior sample satisfies the actual source coefficient equations. Since both maps are affine on these convex cells, the vertex checks establish equality throughout them.

## Outcome

The direction relation now extends to a complete retained cell relation. It closes with no additional carrier. Its extra dimension is freedom in compatible configurations, not a new spatial particle or an identified neutron.

This construction still does not supply two isotope closures. Choosing a three-dimensional section, locking the two kernel coordinates together, or selecting a dynamical subset would be a new law, not a consequence of coefficient equality. The next substantive question is what operation, if any, selects configurations within this four-dimensional relation. Counting its cells or naming one fiber coordinate “neutron” does not answer that question.

## Reproduce

```text
python research/voevodsky/checkers/check_full_cell_attachment.py
```

Fourteen exact checks pass. `results/full_cell_attachment_store.json` contains all parameter vertices, their host/electron projections, the complete polytopal face inventory, original sector owners, and the marked root pair. `results/full_cell_attachment.json` records dimension, boundary ranks, Betti numbers, face-owner counts, formulas and source/checker hashes. Existing sources are unchanged.
