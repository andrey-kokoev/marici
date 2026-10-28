# Co-moving observations are not tetrahedral edge relabelings

## Fresh scope

The preceding invariant-core result supplies three moving preparations B_t = R^t B for the actual proton sector permutation R. This test reads those current embeddings, the12 fixed geometric tangent rows H, their ordered patch/parent-face descriptors, and the checked geometric marking action.

Set H_t = H R^-t. The algebraic equality H_t B_t = H B holds at every frame. The question is whether that equality also has the intended fixed-tetrahedron geometric interpretation.

## All geometric relabelings tested

Each of the24 vertex permutations induces a signed permutation of the12 edge occurrences, including edge orientation and which parent-face occurrence is selected. For each frame the checker tests both

    H_t = W_permutation H

on the full36-coordinate field space, and

    H_t B_t = W_permutation H B_t

on the actual moving preparation.

At the two nonidentity frames, no vertex permutation satisfies either equation. The moving row patch assignments also fail to arise from any single tetrahedral vertex relabeling. This failure is not inferred solely from an unrestricted field counterexample; the moving-domain equation is checked separately.

A positive control reproduces the existing BADC geometric marking covariance H Q = W_BADC H, demonstrating that genuine geometric covariance is accepted by the same comparison convention.

## Local support is not enough

Every moving row is still supported on one physical patch. Therefore it would be inaccurate to describe these particular rows as multi-patch nonlocal observations. The obstruction is that the complete support assignment is not a consistent geometric vertex/edge relabeling, and the transported covectors are not the declared edge-tangent family under such a relabeling.

This concerns the fixed tetrahedral geometry and the declared tangent convention. Changing geometry, permitting different covectors, or adding observations is a different policy and is not ruled out.

## Fixed trace channels also lose information

On the full36-coordinate field space, the moving readout does not factor through the fixed12 trace channels. Since H H* = 8 I, the checker projects every moving row into row(H) exactly. A nonzero residual supplies a field vector k with

    H k = H 0 = 0,
    H_t k != H_t 0.

The receipt stores these explicit witnesses. This rules out any recovery function from the fixed channels alone on that full domain, not just a signed permutation or linear map. Those witness vectors are not asserted to lie in B_t; only the separate geometric-relabeling test is claimed on the moving preparation.

## Consequence and next step

The moving family remains an algebraically coherent retained-context observation system, but cannot yet be called geometric edge restriction on the fixed tetrahedron. In particular, co-moving equality cannot substitute for the missing geometric cell.

A concrete next test is to compute the minimal observation space containing H and closed under the actual order-three source action: the row span of H, H R and H R^2. Its patchwise ranks will show exactly which additional covector data are necessary for a closed observation interface. Any such repair must retain its support and distinguish added patch measurements from the original one-scalar edge convention.

## Verification

- Contract: `contracts/ramsey-moving-edge-geometry-attempt.v1.json`.
- Checker: `checkers/check_ramsey_moving_edge_geometry.py`.
- Receipt: `results/ramsey-moving-edge-geometry-v1.json`.
- Passing freeze: `scc-freezes/ramsey-moving-edge-geometry-v1.4cd9d405c4914c3e.json`.

The frozen exact-runtime challenge passes all finite geometric tests, positive controls and fiber witnesses with fresh direct source pins. No new kernel interpretation, graph verdict or Git checkpoint is claimed. The persisted net remains revision21 and broader descent remains open.
