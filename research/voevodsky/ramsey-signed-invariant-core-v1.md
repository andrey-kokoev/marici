# The fixed signed-compatible preparation has zero invariant core

Fresh state: local net revision21 selects the invariant-image test. The prior signed-compatible proton domain is the image of the36-by3 matrix B obtained from the first three columns of the checked proton five-channel embedding. R is the actual36-coordinate order-three source sector permutation, not a PN-conjugated neutron action.

## Full-image certificate

Using the pinned proton metric, the checker constructs L and verifies L B = I3. Thus B L is a projector onto image(B). Define

    E = R B - B L R B.

For a prepared coefficient vector x, E x = 0 precisely when R B x remains in image(B). Rows0,1,2 of E have determinant

    -5 sqrt(3) / 486,

which is exactly nonzero. Therefore E has column rank3 and its kernel is zero. In particular,

    image(B) intersect R(image(B)) = {0}.

This stronger result settles the requested invariant test without needing to solve a second intersection: every R-invariant subspace contained in image(B) must be zero. The original signed-compatible3-dimensional restriction has **no nonzero smaller fixed invariant repair** under this actual source operation.

The membership test is in the full36-coordinate field space. It does not confuse vanishing signed edge discrepancies with membership in the original prepared image.

## Moving domains survive

Define B_t = R^t B for t=0,1,2, with decoders L_t = L R^-t. Exact checks establish:

- L_t B_t = I3 for each frame;
- R^(u-t) B_t = B_u for all9 frame pairs;
- decoder compatibility on those pairs;
- all27 ambient composition triangles.

The three images are pairwise disjoint except for zero, but each is3-dimensional and they are explicitly transported into one another. A fixed state space and a frame-indexed family are therefore materially different here.

These moving domains are not all signed-compatible for the original fixed readout. Recovering signed matching would require transporting the readout convention as well. Algebraic transport alone does not show that those transported observations are restrictions to the same geometric edges.

## Scope and next action

The result excludes a nonzero invariant subspace *inside this particular signed-compatible preparation*. It does not refute all edge conventions, retained-context incidence or moving-domain semantics, and it does not close the broader descent node.

Next test whether the co-moving observation family can be realized by actual geometric edge/face relabelings with the required orientation and law-domain data, or instead requires genuinely different/nonlocal observation supports. Do not simply rename conjugated field rows as geometric restriction maps.

## Reproduction

- Contract: `contracts/ramsey-signed-invariant-core-attempt.v1.json`.
- Checker: `checkers/check_ramsey_signed_invariant_core.py`.
- Receipt: `results/ramsey-signed-invariant-core-v1.json`.
- Passing freeze: `scc-freezes/ramsey-signed-invariant-core-v1.4361016b7262d24c.json`.

The frozen exact-runtime challenge passes with fresh direct source pins. The receipt retains B, L, the full membership residual, its minor and determinant, and all moving embeddings/decoders. This is not a new kernel interpretation of the multiradical carrier. Net revision21 and all scientific verdicts remain unchanged; no graph mutation or Git checkpoint occurred.
