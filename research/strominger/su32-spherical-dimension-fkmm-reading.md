# Two new sources: reversal changes the classification question

## Question and scope

Operator supplied `C:/Users/andrey/Downloads/Spherical_dimension.pdf` and `references/1603.09421v2.pdf`, adding: “i sense we're touching our way to new understandings.” This is retained as a sensed, non-evidential search direction: read the two sources for a construction or discriminator relevant to the global comparison problem, not as evidence that a physical identification has succeeded.

The first PDF also appeared as `references/Spherical_dimension.pdf`. Its SHA-256 matches the Downloads file exactly: `9f67c7edbfbddaa9099aba1de1079dbd6e5912745bb807948d6fdddad4fb1286`. Main index rebuilt to 5,779 pages / 72 PDFs. Page numbers below are PDF pages. This was targeted reading, not a full review of the 87 new pages.

## 1. Spherical dimension is an equivariant-map invariant

**Bogdan Chornomaz, Shay Moran, Tom Waknine, *Spherical dimension*, arXiv:2503.10240v1 (2025).** Read pp. 1–2, 5–10.

For a concept class H, the authors construct the space of realizable distributions and its reversal-stable subspace `Delta_ant(H)=Delta(H) intersect -Delta(H)`. Reversal flips labels. The spherical dimension measures the existence of equivariant maps from antipodal spheres into that space (Definition 9, p. 9). It is a Z2-coindex, not a Betti number, and the map need not be an embedding (p. 10). The precise lower bound uses `VC-1`, not VC, with their sphere-dimension convention (p. 9).

The actionable condition is on p. 8: for an antipodal simplicial complex, no simplex may contain a vertex together with its reversed partner. A fixed-point-free permutation of vertices alone does not ensure a free action on the realization.

### Apply that distinction to our support diagram

Use the previous packet's cyclic vertex order

```
0=P+, 1=E+, 2=P-, 3=E-.
tau=(0 2)(1 3).
```

This is a specified local direction-reversal candidate, not an already constructed global involution of all native cells.

- On the incoming channel square `01,12,23,30`, tau acts freely. If X consists of the two features P and E, and H consists of all four binary assignments, its realizable-distribution complex is precisely this square: each edge contains one sign per feature. It is an antipodal circle.
- On the four-triangle comparison sphere, both diagonal edges `02` and `13` exist. Their midpoints are fixed. Every comparison triple contains an opposite-sign pair, so this larger complex is not the realizable-distribution complex of that same two-feature class.

The full fixed-point calculation uses barycentric coordinates. A fixed point has

```
(x0,x1,x2,x3)=(a,b,a,b),  a,b>=0,  2a+2b=1.
```

To lie on the tetrahedron boundary, at least one coordinate must be zero. Thus either `(a,b)=(1/2,0)` or `(0,1/2)`. These are exactly the two diagonal midpoints. They are points in the geometric realization of supports, not identification or averaging of native payload records.

**Consequence:** a sphere found in the comparison complex is not automatically an antipodal sphere. Borsuk–Ulam/coindex arguments require the action, not merely the shape or the count of homology classes.

## 2. The second paper classifies the two-fixed-point case

**Giuseppe De Nittis and Kiyonori Gomi, *The cohomological nature of the Fu–Kane–Mele invariant*, arXiv:1603.09421v2 (2017).** Read pp. 1–6, 8–10, 12, 19, 27–28.

Their object is a complex vector bundle E over an involutive space `(X,tau)` with an anti-linear lift

```
Theta_x : E_x -> E_tau(x),
Theta_tau(x) Theta_x = -id.
```

This is their “Quaternionic” structure (Definition 2.2, p. 8). A label permutation or a complex-linear map squaring to -1 does not by itself supply it. No physical-time interpretation of our direction reversal is assumed.

For even rank, the determinant is a Real line bundle with a canonical section on the fixed locus. The pair determines the FKMM class

```
kappa(E,Theta) in H^2_Z2(X, X^tau; Z(1)).
```

See pp. 10, 12. The relative fixed-locus datum is essential. The general classification map need not be surjective; the paper gives a lens-space counterexample on p. 27. For the particular low-dimensional spheres, it supplies explicit classifications.

### Identify the local involutive sphere, not just S2

The paper defines `S^{p,q}` using p unchanged and q negated coordinates (p. 6). Our tetrahedron boundary with tau is equivariantly homeomorphic to **S^{1,2}**, not the free antipodal sphere S^{0,3}:

- The permutation on R4 has +1 eigenspace dimension 2 and -1 eigenspace dimension 2.
- Remove the constant barycentric direction. The centered three-dimensional space has eigen-dimensions `(1,2)`.
- Radial projection from the tetrahedron center to its unit sphere is equivariant.

Equation (4.13) and the following paragraph on p. 28 distinguish the consequences:

- Over **S^{0,3}**, odd-rank Quaternionic bundles have odd Chern number; even-rank ones have even Chern number.
- Over **S^{1,2}**, even-rank Quaternionic bundles have a **Z2 classification**. Fixed points exclude odd complex rank (p. 9).

For the second case, an ordinary Chern-number test can miss the distinction. Anti-linearity implies `c1(E)=-tau* c1(E)`. Our tau is orientation-preserving on S2, so its action on H2 is +1 and `2c1(E)=0`. Since H2(S2;Z)=Z, the ordinary c1 vanishes, including for the nontrivial Quaternionic class.

Thus **zero ordinary Chern number need not mean trivial symmetry-compatible comparison data**. This is conditional on constructing the anti-linear square-minus-one lift; it does not establish one for Su-32. In particular, it does not retroactively invalidate the circle-bundle classification in the Nikolai Mnëv reading: that classified a different bundle category.

## What changes in the next test

The immediate discriminating input is a **global involution and its lift**, rather than selecting a Hopf integer from the local sphere alone.

1. Construct an action on the native occurrence/carrier object, retaining how it maps charts. Determine its fixed simplices and its action on cochains. Local simultaneous sign reversal is the candidate analyzed here, not the admitted answer.
2. Test whether a supplied payload lift is anti-linear and has square +1 or -1. These give different Real/Quaternionic categories; a direction sign does not decide them.
3. If the Quaternionic conditions hold, retain the determinant line together with its fixed-locus section and use integral, twisted equivariant relative cohomology. Our earlier rational ranks `(43,36,7)` cannot detect Z2 torsion and cannot replace this computation.

The existing signed-reference audit already prevents assigning reading-independent signs to every charged cell under the uniform-cone extension. Therefore a global action cannot be manufactured by independently repeating each chart's partner swap. It may need to permute charts and retain occurrence information. This is a concrete compatibility problem, not a reason to discard the local calculation.

## Disposition and provenance

These sources yield a new discriminator: **adding the layer-4 comparison supports changes the candidate reversal from free on the square to a two-fixed-point action on the sphere**. The second paper then tells us which classification applies if a compatible anti-linear lift exists. No global involution, lift or FKMM invariant was computed in this reading pass; the local fixed-point and representation arguments above are explicit mathematical derivations, not a new executed checker.

Searches used `pnpm pdf:search` with separate book filters: `coindex|cohomological|simplicial complex|Definition 3|Borsuk` and `sewing|Pfaffian|fixed point|antipodal|canonical section`. Full indexed pages were then read. Main rebuild execution: `structured_command_execution:e_29164_1793125932938968900_62`; source-copy hash check: `structured_command_execution:e_29164_1793125965349493500_67`.

A preliminary direct extraction attempt failed; the canonical reindex succeeded and included both PDFs. No scientific code, old result packet or SCC model was changed.
