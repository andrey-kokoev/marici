# Joint NE covariance with the electron spin lift retained

## Fresh source binding

The existing NE constructor supplies a neutron contrast frame K (36-by2), an electron frame E=J W (8-by2), and a metric-unitary joint exchange. The actual electron store supplies four face projectors and the binary-tetrahedral spin action. These mutable source files and their live direct hashes were read for this attempt; no particle operation or source-owned constructor was changed.

Use the explicit spin lift U=i sigma_x of the spatial complementary rotation diag(1,-1,-1). Conjugation of the actual stored face projectors derives the permutation `[1,0,3,2]`. The resulting8-coordinate action Q_E combines that face permutation with U on each spinor block. Exact checks give

    Q_E* Q_E = I8,
    Q_E J = J U,
    Q_E^2 = -I8.

The numerical face permutation is not a proof that these electron face labels are the Ramsey geometric facets. That binding remains separate.

## Target exchange reconstructed from its frames

The target logical alignment is U W and the target electron frame is E_B=J U W. This is independently checked to equal Q_E E_A. The neutron contrast frame has unchanged coefficients in the reconstructed moving intrinsic basis from the PN step.

Reconstruct the target partial coupling S_B=E_B Ksharp and the joint exchange

    X_B = [[I36-K Ksharp, K E_B*],
           [E_B Ksharp, I8-E_B E_B*]].

The target exchange is not seeded as a conjugate of X_A. The constructor output verifies

    X_B diag(I36,Q_E) = diag(I36,Q_E) X_A

in all1,936 entries. It is involutive and satisfies `X_B* M44 X_B=M44`, with M44=diag(M_N,I8). All36 neutron coordinates and all8 E coordinates are included, not only their contrast/return subspaces.

Keeping the original target exchange unchanged violates the covariance square at576 entries.

## Five coefficients and complement retention

The source-bound five-slot NE permutation remains `[0,4,2,3,1]`. Rotating the full joint output binding gives the target binding. The exact NE binding square holds for all five inputs, and its metric Gram remains I5. The E and retained baryon Gram projectors have ranks2 and3 respectively. The six raw E complement directions also remain present in the full44-dimensional exchange.

These are conditional equations for the declared target spin frame and existing contrast ansatz. They do not derive the physical selection of that ansatz or an independently preferred lift.

## New coherence boundary: central sign

The other lift -U gives a different target coupling and also satisfies the covariance square. Neither choice is selected by the spatial rotation alone.

In the present moving-N/fixed-electron-frame convention, the full marking action squares to

    diag(I36,Q_E)^2 = diag(I36,-I8),

not I44. This is a relative sign between the neutron and electron blocks, not a common scalar on the whole direct sum. It must therefore be retained as comparison data; it cannot simply be identified with an ordinary order-two action on the joint field.

The next discriminating step is to test composition including this central action on the joint coupling, prepared states and readouts. An explicit lift/context extension may supply coherent descent, but an unrecorded sign quotient is not licensed by these calculations. Native higher-WG restriction witnesses and geometric edge/vertex incidence data are still missing.

## Verification history

The first frozen run reached the metric check but used the wrong expected matrix: its helper computes `X* M X`, so the result must be M, not I. This was a checker convention error, not evidence against the field candidate. The assertion was corrected without changing the candidate or source data, then refrozen.

Passing freeze: `scc-freezes/ramsey-moving-carrier-NE-v1.b27a974de54e0270.json`.
Contract: `contracts/ramsey-moving-carrier-NE-attempt.v1.json`.
Checker: `checkers/check_ramsey_moving_carrier_NE.py`.
Receipt and exact target matrices: `results/ramsey-moving-carrier-NE-v1.json`.

The SCC challenge passes after the correction. This is exact multiradical computation, not a proof-assistant derivation or experimental result. General face-chart descent, whole-space admission and the Ramsey root remain open. No graph verdict, net revision or Git checkpoint was changed.
