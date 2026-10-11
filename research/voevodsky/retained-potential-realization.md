# Completed finite construction: potential tetrahedron, retained realization and pullback

## Scope of completion

The three requested mathematical obligations are now constructed and checked **under the explicit barycentric-fold, normalized-depth and geometric-coordinate interface conventions**. This is a finite information-structural model, not a derivation of a physical electron or neutron.

The distinction between a visible geometric vertex and its retained information is essential: the visible endpoint is one point; its retained direction fiber is not one point. No equality between these different information types is asserted.

Fresh closure: **8 isolated checker processes, 163 checks passed**. The local checker sources were unchanged during closure, and all recorded input hashes still matched afterward. The closure includes the rejected fixed-position candidate as a measured negative result, not as an accepted realization.

## 1. Potential complex and inward folds

The potential tetrahedron is C=sd(Delta^3). Its 15 vertices are the nonempty vertex-subset barycenters, and its 24 maximal cells retain every flag

```text
vertex < edge < face < body.
```

Its barycenter is b=(1/4,1/4,1/4,1/4). Inward depth is h_C(y)=1-4 min(y_i). The four primary face-to-body cones, with their full flag subdivision, are retained.

Let B be its direction sphere. The coefficient-fold atlas refines B to 20 vertices, 54 edges and 36 triangles while preserving all 24 original flag owners. The resolved potential is C_hat=I x B, where I=[0,1]. It keeps an inward direction v even at depth zero. Its explicit blowdown is

```text
beta_C(t,v) = (1-t)b + t v.
```

The body barycenter is therefore a single visible point, with a retained sphere of approach directions before applying the forgetful blowdown.

## 2. Actual host and coefficient interfaces

The host is the original proton-like outer triangle T=(F_ABC,A,B), barycentrically subdivided into six flags. Its new visible barycenter is

```text
q = (7/9,1/9,-1/9) in the original spatial coordinates,
q = (1/3,1/3,1/3) in host barycentric coordinates.
```

The surrounding proton surface was conformingly refined, without changing its volume or silently reassigning the 1836 source arrows.

The coefficient map Gamma(v)=L_AB d(v) uses the **actual retained nine-arrow AB local projector**, with its typed raw/local x,y,z ports and the declared potential vertex alignment. Z is its real geometric mode-image disk.

The successful host interface is H=T x Z: a location and a coefficient value are separate variables. The actual maps are

```text
mu: H -> I x Z,        mu(x,z) = (h_T(x),z),
nu: C_hat -> I x Z,    nu(t,v) = (t,Gamma(v)),
h_T(x) = 1-3 min(x_i).
```

Their pullback Q is explicitly T x B, via

```text
(x,v) -> ((x,Gamma(v)),(h_T(x),v)).
```

The inverse mediator takes any compatible pair ((x,z),(t,v)) to (x,v). Compatibility gives both missing equalities, so existence and uniqueness hold for arbitrary compatible PL maps, not merely for sampled vertices.

Both interface maps, both projections and the bare-host projection are checked as typed simplicial maps on the retained product triangulations.

### What is retained at the vertex?

- Over the bare location q: the complete direction sphere B, with all fold owners active.
- Over a fixed mode-bearing state (q,z): two direction points for an interior mode, one on its seam.
- After the radial point-only blowdown: the single old pullback vertex (q,b).

The earlier restriction z=j(x), fixing mode from geometric position, retained only eight fold interiors and was rejected. It is not silently reinstated.

## 3. The inward realization itself

For 0<=s<=1, define

```text
R_s(x) = (1-s)x+s*q,

H_s(x,z) = (R_s(x),z),
C_s(t,v) = ((1-s)t,v),
J_s(t,z) = ((1-s)t,z),
Q_s(x,v) = (R_s(x),v).
```

The depth identity

```text
h_T(R_s(x)) = (1-s) h_T(x)
```

follows directly because all barycentric coordinates receive the same offset s/3 and their differences are multiplied by 1-s. It makes the entire interface square commute throughout realization. Gamma(v), v, and the original potential fold owner remain unchanged.

Every host flag contains q. Thus every product of a host flag with a direction flag is an invariant carrier for the realization. There are 216 such carriers; each contains six staircase cells. The map is not falsely required to remain inside one staircase simplex when its true invariant carrier is larger.

The maps satisfy the exact semigroup law

```text
Q_s Q_r = Q_(s+r-s*r).
```

At s=1 the result is a retraction to {q} x B. It fixes that entire fiber pointwise and is idempotent. All 24 original potential fold interiors remain active at the final visible vertex. The original host location is intentionally contracted; an endpoint alone does not recover its approach history.

### Compatibility with the old point realization

The comparison is

```text
beta_Q(x,v) = (x,(1-h_T(x))b+h_T(x)v).
```

Realizing first and then blowing down equals blowing down first and contracting the original host and potential coordinates. This identity is checked symbolically as a rational polynomial identity, as well as on all 1296 product-cell interiors at five parameters.

At the endpoint, beta_Q sends all (q,v) to (q,b). Its loss of direction information is explicit. Keeping the retained realization packet is not the same operation as keeping only that visible point.

### Category and interpretation limits

For each fixed s the square maps are PL, allowing compatible subdivision. The parameterized family and radial blowdown are continuous semialgebraic maps; their mixed products are not silently called PL maps on finite product triangulations.

The parameter is a geometric deformation parameter, not physical time. This is not an interaction equation, energy model or wavefunction.

## 4. Is the belt required? Is its transport nontrivial?

The host's complete vertex-edge-face flag convention has a six-edge link around q. Truncating its six inward sectors between two positive depths produces a six-quadrilateral annulus. Hence the belt is a derived available collar of the flagged realization.

Annular topology comes from the punctured host disk. Six panels come from the retained flag convention; topology alone allows a three-sector presentation. Neither a particular width nor an independent neutron object is forced.

The potential coefficient fold has its own six-edge seam. It is not the host belt. Their interface maps were constructed explicitly: restricting the global potential seam to the fixed-position host candidate gives only the edge AB, not the host annulus.

The actual coefficient fold has two globally defined sheets over the interior of Z. Every loop returns on its original sheet. In the successful pullback, a host-belt loop can keep v and Gamma(v) fixed, and the realization above explicitly fills that loop by a disk at fixed v.

Therefore **nontrivial sheet-swap transport is not required by this construction**. An odd flat C2 swap would contradict extension over those retained disk sections. Adding it requires new data or a changed domain/transport law; it is not derived as a neutron here.

## 5. Retained artifacts and reproducibility

The final realization packet contains its complete source chain, the explicit family, endpoint maps, invariant carriers and visible/retained endpoint distinction.

```text
python research/voevodsky/checkers/check_realization_closure.py
```

Primary artifacts:

- `research/voevodsky/checkers/check_inward_realization.py`: realization family, exact polynomial certificates, endpoint maps and mutation controls.
- `research/voevodsky/results/inward_realization_store.json`: full retained realization.
- `research/voevodsky/results/inward_realization.json`: 20 realization checks.
- `research/voevodsky/results/realization_closure.json`: fresh eight-process closure, 163 checks, source hashes.

Final root:

```text
1bd4a613e85104bf78a344e402a465af3973c49dca1b8c8847aa1f13f7ebe5f9
```

Detailed stages:

1. `potential-complex-pullback.md`: original potential, inward depth and point realization.
2. `pullback-retention.md`: lossless reconstruction and point-fiber limitation.
3. `fold-bearing-vertex.md`: actual retained direction fiber.
4. `fold-coefficient-attachment.md`: source-bound coefficient interface and lost-mode witnesses.
5. `projector-fold-sheets.md`: derived two-sheet fibers, seam and compatible refinement.
6. `host-coefficient-pullback.md`: explicit rejected restriction and its lost folds.
7. `open-mode-pullback.md`: the accepted fold-preserving interface square.

The requested construction and belt/transport derivation are complete for this declared model. Physical particle identification, neutron-specific selection, unrestricted reconstruction minima and H-1/H-2 coefficient-arrow totals are separate unresolved objectives; no cell count in these packets is offered as an atomic mass.
