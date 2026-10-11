# Iteration 5: sheets and seam derived from the actual projector

## Input and scope

The complete iteration-4 attachment packet was freshly read and reverified. The operator is the same source-bound L_AB, not a replacement. The domain remains the real potential-direction sphere, with the explicitly declared ABCD vertex alignment.

This iteration classifies its entire point fibers and constructs a compatible fold atlas. It does not infer a neutron from the existence of two sheets.

## 1. Exact fiber classification

The real kernel of L_AB is the line spanned by n=(1,1,-1). Its restriction to the tangent plane n-perp is injective, as follows from the exact recovery matrix retained in iteration 4.

Given an admissible selected mode z, recover its unique tangent representative w with n dot w=0 and L_AB w=z. Every real vector with that same mode is therefore

```text
d = w + alpha n.
```

The tetrahedron inequalities are lambda_i(d)=(1+POINTS[i] dot d)/4 >= 0. Since A dot n=B dot n=C dot n=1 and D=-n, they reduce to

```text
alpha_lower = -1 - min(A dot w, B dot w, C dot w),
alpha_upper = 1/3.
```

There is no fiber when alpha_lower>alpha_upper. When the interval is nonempty, its two endpoints are exactly its intersections with the tetrahedron boundary. All strict intermediate points have positive tetrahedral barycentric coordinates and are not direction-sphere points.

Consequently:

- Inside the triangular mode image: exactly two distinct direction points.
- On its boundary: the endpoints coincide, giving exactly one point.
- Outside: no direction point.

This is a classification from the inequalities, not an extrapolation from sampled vertices. The checker additionally tests all 290 denominator-12 boundary points and a 91-point image grid, finding 55 double fibers and 36 single fibers.

## 2. The two actual sheets

The upper sheet is the potential face ABC. The lower sheet is the union of the other three potential faces. Both map homeomorphically to the same closed triangular mode disk. Their common boundary is the cycle A-B-C-A.

Thus the potential direction sphere is a double of a disk, with its two boundary copies identified. A selected mode plus an upper/lower selector reconstructs a direction in the image interior. On the seam there is only one direction: retaining two distinct tagged seam points would be an incorrect reconstruction.

These sheets are **not** the earlier two conjugate coefficient presentations. Their selected coefficient outputs are equal, not conjugate-distinct.

## 3. A fold-preserving atlas

The original upper face has six barycentric flag triangles; the lower disk has eighteen. Exchanging fiber endpoints does not preserve the original 24-triangle subdivision as a simplicial automorphism.

The checker constructs the needed common refinement rather than pretending otherwise:

| Complex | Vertices | Edges | Triangles |
| --- | ---: | ---: | ---: |
| Refined potential sphere | 20 | 54 | 36 |
| Projected mode disk | 13 | 30 | 18 |

All fourteen original direction vertices remain. Each of the six original upper flags is subdivided into three cells; the eighteen lower flags remain unchanged. Every refined cell retains its original vertex-edge-face-body fold owner. No original inward-fold flag is lost.

Fiber exchange is now a simplicial involution. It preserves the selected mode, fixes the six subdivided seam vertices and reverses the sphere orientation. The reconstructed sphere and image disk have checked consistent orientations and mod-2 homology S2 and D2 respectively.

The sheet codec round-trips all 290 tested boundary points and rejects a spurious second seam point. It is a point codec plus a separately retained flag atlas, not a claim that a sheet bit encodes every fold-history distinction by itself.

## 4. Does this derive the belt or nontrivial transport?

It derives a **fold seam**: the common boundary of the two potential sheets. Under the retained barycentric convention, that seam has six edges. A collar of it can be represented as an annulus, but a particular collar width is additional data.

The seam is not automatically the same geometric object as the six-panel belt around the new host vertex. Here it lies on the potential ABC face boundary; the mode image corresponds to the full ABC face, while the selected host triangle is the smaller (F_ABC,A,B). Equal combinatorial edge counts do not supply an identification map.

The interior mode image has two globally defined sections, alpha_lower and alpha_upper. Every loop lifts separately on those sections and returns to its starting sheet. This remains true if a point is removed from the image, because the same sections still exist.

An exchange of sheets is an available global involution; it is **not** the monodromy forced by traversing the belt. The two explicitly constructed closed lifts illustrate this distinction. No nontrivial transport is required by the actual projector-induced folding.

## 5. What is now established, and what remains

There is now a two-sheet structure derived from the actual coefficient interface, rather than inserted as an independent C2 model. It explains precisely which direction information the local-mode selection forgets and where the sheet distinction disappears.

The remaining attachment question is substantive: the full potential mode image and the selected small host triangle are different domains. Next, form their coefficient-matched base change explicitly and inspect its fibers at the realized host vertex. This must check whether imposing mode equality still retains all the required inward folds, rather than silently replacing the prior depth pullback by a smaller object.

The original depth pullback, resolved direction-bearing pullback, and coefficient-fold atlas remain separately retained. None is yet a complete electron operator or an H-1/H-2 arrow-count derivation.

## Verification and artifacts

All 20 checks passed, including full source replay, exact interval endpoints, topology, orientation, all fold owners, deck involution, point reconstruction, outside-image and seam controls, closed lifts, honestly rehashed mutations and serialized replay.

```text
python research/voevodsky/checkers/check_projector_fold_sheets.py
```

- `research/voevodsky/checkers/check_projector_fold_sheets.py`
- `research/voevodsky/results/projector_fold_sheets_store.json`
- `research/voevodsky/results/projector_fold_sheets.json`

Root: `bc961dbb2749859a1352f57d493193a0f712d1de29951a76412ddbed59faa2a2`.
