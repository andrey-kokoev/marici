# Mutual singularity forces every arithmetic multiplication intertwiner to vanish

## Question

Can the missing bulk–corona cross operator be constructed canonically by requiring compatibility with the common finite-place multiplication algebra?

## Claim boundary

No. Mutual singularity of additive and multiplicative Haar measures forces every bounded intertwiner of their multiplication representations to be zero. A nonzero cross operator must fail full multiplication covariance and therefore requires a smaller source algebra plus an independently derived kernel or correspondence.

## Theorem

Let `X` carry mutually singular measures `mu_+` and `mu_x`. Write

\[
H_+=L^2(X,\mu_+),
\qquad
H_\times=L^2(X,\mu_\times).
\]

Let `M_+(f)` and `M_x(f)` denote multiplication by a bounded measurable function `f`. If a bounded operator

\[
C:H_+\longrightarrow H_\times
\]

satisfies

\[
C M_+(f)=M_\times(f)C
\]

for every bounded measurable `f`, then `C=0`.

## Proof

Mutual singularity gives a measurable set `A` with

\[
\mu_+(A^c)=0,
\qquad
\mu_\times(A)=0.
\]

Hence

\[
M_+(1_A)=I_{H_+},
\qquad
M_\times(1_A)=0_{H_\times}.
\]

Intertwining with `f=1_A` gives

\[
C=C M_+(1_A)=M_\times(1_A)C=0.
\]

## Application to the conductor corona

Prior research proves that additive Haar and the multiplicative conductor-corona measure are globally singular. Therefore their direct-sum carrier retains both sectors, but the full arithmetic multiplication algebra cannot produce a nonzero off-diagonal block.

The vanishing Hellinger affinity is the finite-level shadow of the same obstruction: local density intertwiners converge toward orthogonality, while the limiting multiplication representations are disjoint.

## What a surviving cross operator must contain

A nonzero cross operator must relax at least one premise. Since boundedness on the final form domain is needed for an elementary Schur estimate, the viable relaxation is not arbitrary unboundedness. It must instead replace the full multiplication algebra by a smaller source-authorized algebra and supply a nonlocal correspondence not represented by multiplication.

Candidates must state:

1. the exact smaller algebra `A_0` being intertwined;
2. why `A_0` is source-derived rather than selected to admit the operator;
3. the kernel or correspondence defining `C`;
4. its closability and domain;
5. the block lower bound including `C`;
6. the differentiable vertical action needed to retain the Mellin generator.

Compatibility only with fixed Mellin shifts is insufficient because the Haar-corona representation is discontinuous in their parameter and has no generator.

## Strongest falsification attempt

The theorem does not rule out integral transforms, Fourier correspondences, derivations, correspondences between different algebras, or unbounded closable operators on proper domains. It rules out only the most canonical-looking module map over the common multiplication algebra. Any proposed nonlocal operator must exhibit exactly which covariance law replaces this impossible one.

## Disposition

The instruction to construct the cross operator reaches a first typed obstruction: no nonzero bounded full-multiplication intertwiner exists. Construction cannot proceed by choosing an off-diagonal rank-one map, phase, ultrafilter, or renormalization without source authority. Reopen with a source-derived smaller algebra and explicit correspondence; otherwise the branch remains blocked.