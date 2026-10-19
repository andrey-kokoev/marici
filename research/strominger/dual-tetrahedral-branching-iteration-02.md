# Iteration2/10: exponential flags versus task-relative reconstruction

## Fresh state and claim boundary

Fresh current-pointer/v2 and graph readback identify the sole executable source
`flag-family-reconstruction-scaling`, test:2110be12520436715a89, still planned.
Reapply EXACTLY the two flag moves and canonical incidence preparation/reader in
dimensions2..6. Only d4 has tetrahedral facets. This is a mathematical family
control, not changing physical space dimension between electron shells.

No old source file, iteration1 operator or prior receipt is changed. Do not use
a large symbolic quotient whose output is untracked: this checker is exact
integer/rational arithmetic, with a full Walsh similarity certificate represented
by its action on EVERY source basis function.

## Source and predicted distinction

Vertices are +/-e_i; facets have signs sigma in{-1,+1}^d; a flag is(sigma,i).
Its neighbors change the marked vertex within the facet or flip one sign other
than its marked coordinate. Thus N=d2^d, degree2(d-1).

Let m=2^(d-1), B[f,v]=1 at the flag's vertex, D=B^T/m, and Hv the ordinary
cross-polytope vertex Laplacian. Compute H and B BEFORE comparing predictions.
The target identities are

    DB=I_(2d),   DHB=Hv/2,
    K=HB-BHv/2,   K^T K/m=(d-1)P_odd,
    DH^2B-(DHB)^2=(d-1)P_odd.

Use L=2K to retain integer arithmetic. Choose the d positive vertices, L+, and
W=[B,L+]. The predicted Gram is diag(m I_(2d),2m(d-1)I_d). Its positive diagonal
proves independent rank3d; no fitted rank computation or desired capacity is
inserted. Verify 2HW=W A2, where

    A2 = [[Hv, 2(d-1)S^T], [S,6I_d]],

and S maps each antipodal vertex pair to its signed difference. Since L is
obtained from B and HB, this invariant W is the MINIMAL continuation carrier.
All other N-3d full flag modes remain; they are not declared gauge.

## General source proof, not extrapolation

For a flag with marked axis i, the column of L associated with positive vertex
j is zero if i=j and -sigma_j otherwise. Summing its products over independent
sign vectors gives its norm2m(d-1), cross norms zero and orthogonality to B.
The same local moves give

    H B= B Hv/2 + L/2,
    H L+ = (d-1)B S^T +3L+.

These are counting identities for arbitrary d>=2. They prove the Gram and
intertwiner laws generally; the bounded computation checks their realized
sources and explicit vectors for ALL d2..6. The restriction d>=2 is declared
before testing: at d1 there is no memory sector.

The source vertex even subspace has a constant line and a(d-1)-space at eigenvalue
d. Each of d odd/memory pairs has matrix [[d-1,d-1],[1,3]]. Hence the closure
polynomial is

    x (x-d)^(d-1) [x^2-(d+2)x+2(d-1)]^d.

Use the actual small closed matrix to certify this, not an assumed infinite
shell sequence. Optional spin doubles ranks but is not derived here.

## Full source and d4 compatibility

Verify the source action on every Walsh character chi_T(sigma) at every marked
axis. The resulting block is(d+2|T|)I-2diag(T)-J. Character orthogonality proves
this transform keeps ALL N modes. Characteristic-polynomial factors of each
small block are checked from exact matrix trace/Newton identities; full factor
multiplicities are retained without requiring expensive global simplification.

For d4 explicitly reconstruct the bijection with iteration1's original sign/axis
flags. Check every edge, the canonical lift and the full closure projector under
that same source map. Equal size or equal rank alone is not sufficient. Retain
an actual two-application coarse-composition failure for every d and a source
vector forgotten now but detected by the next H reader. Full shared-plus-residual
encoding remains reconstructible.

## DPC and disposition criterion

Problem: a single4D result could hide a fitted projection or confuse exponential
flag count with capacity. Bold candidate: frozen incidence yields raw d2^d labels
but a3d minimal vertex-initiated continuation carrier, with d memory directions.
Rivals:2d is already closed; every raw flag is required for that restricted task;
quadratic shell capacities follow by reindexing d; changing d changes old source
incidence unnoticed. Risk: check all graph/Gram/intertwiner laws, direct source
reader witnesses, full retained transforms and d4 source recovery. Strongest
falsifier: any family member violates the predicted Gram/rank/composition identity;
retain that d and residual, never retune moves. Disposition is recorded in
`results/flag-family-reconstruction/verification.json` and `disposition.md`.

## Reproduce and enabled successor

    python research/strominger/checkers/check_flag_family_reconstruction.py

Standard library only. Use tracked asynchronous execution if duration is unknown.
The next nonredundant source question, if scaling survives, is the minimum number
of ACTUAL tetrahedral face readers needed to reconstruct the fixed d4 closed
12-mode task. Count reader ranks and dependencies, not4 independent channels
per attachment by fiat. Native P/N/E, physical charge/occupation and shell grading
remain blocked, not waiting-only leaves.
