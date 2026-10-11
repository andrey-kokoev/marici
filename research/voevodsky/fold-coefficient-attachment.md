# Iteration 4: the direction fiber meets the actual proton coefficient frame

## Fresh source and attachment contract

The complete iteration-3 resolved-pullback packet was reread and reverified. The selected outer triangle is still AB=(F_ABC,A,B). This experiment extracts its actual raw-to-local projector L_AB from the retained 1836-arrow source, binding all nine arrow references and all six typed source/target ports. No substitute projector is introduced.

The existing source explicitly treats x,y,z as spatial/contrast coefficient coordinates. To connect the potential chart, declare the vertex alignment (0,1,2,3)->(A,B,C,D) and the bridge

```text
d(v) = sum_i v_i POINTS[alignment_i],
J_dir(x,v) = L_AB d(v).
```

Here v is a retained real boundary direction in the potential tetrahedron. Its three spatial coordinates are interpreted as inputs at the original raw/AB/x,y,z ports; the output belongs to local/AB/x,y,z. This is a specified geometric-to-coefficient interface, not a physical coupling law forced by the 1836 count. All 24 vertex-label alignments are audited rather than claiming the displayed choice is uniquely selected.

Equivalently, pull the constant three-coordinate coefficient bundle over the host triangle back along Q->T. The inherited operator is the same L_AB at every base point. The direction vector d(v) is a section of that pulled-back raw bundle, and J_dir is its image. The operator and the section are different pieces of data.

## The actual projector loses inward-direction information

The host normal is n=(1,1,-1). Exact arithmetic verifies L_AB n=0. In particular, these two retained direction vertices have identical selected-mode output:

```text
v_face = (1/3,1/3,1/3,0),  d(v_face) = n/3,
v_back = (0,0,0,1),        d(v_back) = -n.

L_AB d(v_face) = L_AB d(v_back) = 0.
```

They are distinct points in the literal sphere fiber of iteration 3. Thus simply feeding that fiber through the original local-mode projector does not preserve all its folds.

For every one of the 24 vertex-label alignments, exactly two of the fourteen direction vertices have zero mode: one potential vertex and its opposite face barycenter. The information loss is not removed by relabelling the tetrahedron.

## A sufficient real residual, with an exact inverse

For real geometric input d, retain both its selected mode z=L_AB d and its normal coordinate r=n dot d. Define

```text
M = Re(L_AB) + n n^T / (n dot n).
d = M^(-1) [Re(z) + r n / (n dot n)].
v_i = (1 + POINTS[alignment_i] dot d) / 4.
```

The recovery matrix is nonsingular and stored exactly. The two lost directions above have normal readouts 1 and -3. Recovery is checked on all fourteen direction vertices and one interior point of each of the 864 pullback cells: 878 samples in total. The displayed linear inverse supplies the general real-input formula, beyond those checks.

This is a sufficient retained residual, not a minimality claim. On the boundary sphere a more economical discrete sheet selector may suffice away from a seam; that requires an actual fiber classification, not an assumption.

The source projector is not the circular-polarization projector for an equilateral triangle: its underlying reference triangle is isosceles. The recovery uses its exact coefficients rather than assuming 2 Re(L_AB) is the tangent-plane projector.

## Do not confuse real geometry with arbitrary coefficient states

The preceding inverse uses d real. It is not an inverse for arbitrary z in Q(sqrt(-3))^3. The checker constructs a nonzero complex vector killed by both L_AB and the normal functional.

For a lossless interface on the full coefficient space, retain

```text
L_AB z  and  (I-L_AB)z.
```

Their sum reconstructs z exactly. The residual has complex rank two, unlike the one-real-scalar residual sufficient for geometric directions. These two typing contracts cannot be substituted for one another when counting coefficient arrows.

The complementary matrix is stored as an interface witness. This does not introduce a neutron operator, declare new particle degrees of freedom or claim that the entire extended network has the original pruning theorem.

## Position readout versus retained direction readout

There are two different maps:

```text
J_pos(x,v) = h_T(x) L_AB d(v),
J_dir(x,v) = L_AB d(v).
```

The positional map commutes with radial blowdown to the original point realization. It vanishes for every direction at the realized center.

The directional map remains informative at that center, but does not descend through its collapse to a single old point: different points of the collapsed sphere give different mode outputs. Using the directional map therefore genuinely requires the resolved interface or equivalent retained direction data. It is not recoverable from the old point alone.

This makes precise what is being retained by the fold-bearing vertex.

## Belt and transport consequence

The coefficient operator is the actual fixed AB projector and the chosen alignment is global. Holding a potential direction fixed while traversing the host's six-link circle returns exactly the same coefficient state. The actual frame attachment therefore admits trivial transport and does not require the earlier invented conjugate-state swap.

The six-panel belt remains the annular truncation of the host's flagged sectors. The flat-extension obstruction across each retained host disk section is unchanged. No charge, spin or particle identity is inferred from the coefficient interface or its lost modes.

## Verification and next substantive obligation

All 15 checks passed: source-arrow/port binding, exact projector and kernel, loss witnesses, real reconstruction, complex noninjectivity control, full complementary recovery, all 24 alignments, blowdown compatibility, belt return, rehashed mutations and full serialized replay.

```text
python research/voevodsky/checkers/check_fold_coefficient_attachment.py
```

- `research/voevodsky/checkers/check_fold_coefficient_attachment.py`
- `research/voevodsky/results/fold_coefficient_attachment_store.json`
- `research/voevodsky/results/fold_coefficient_attachment.json`

Root: `3bbf2fbe12b9ea8641d253d66f830357340fa6e0f3891a34f43412a4f6a7c915`.

Next: classify the exact fibers and seam of the projector-induced folding of the potential direction sphere. That will determine whether a two-sheet witness follows from the actual interface, and where it must be retained, rather than assuming the independent C2 holonomy model. No complete electron operator or H-1/H-2 arrow total is yet assigned.
