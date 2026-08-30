# Schatten-three norm completion confines failure to the seam

## Operator completion theorem

Let (K_N(z)) be analytic (mathcal S_3)-valued sector operators. Suppose that
for every compact subset (C) of an open half-plane,

\[
\sup_{z\in C}
\lVert K_N(z)-K(z)\rVert_3
\longrightarrow0.
\]

Continuity of the regularized determinant in the Schatten norm implies

\[
\det_3(I+K_N(z))
\longrightarrow
\det_3(I+K(z))
\]

uniformly on (C).

Thus locally uniform determinant completion follows from a concrete
operator-norm completion law. It need not be separately assumed at the scalar
level.

## Accretive stability

Suppose every cutoff operator is accretive:

\[
\operatorname{Re}\langle v,K_N(z)v\rangle\ge0.
\]

Schatten-norm convergence implies operator-norm convergence, so the limiting
operator (K(z)) is accretive. Then

\[
\operatorname{Re}\langle v,(I+K(z))v\rangle
\ge
\lVert v\rVert^2.
\]

The same lower bound holds for the adjoint. Hence (I+K(z)) is bounded below,
has closed dense range, and is invertible.

Therefore

\[
\det_3(I+K(z))\ne0
\]

throughout the open sector.

This gives zero confinement without applying positivity to the completed
entire scalar.

## Cauchy formulation

The source need not present the limiting operator in advance. It is sufficient
to prove that for every compact (C),

\[
\sup_{z\in C}
\lVert K_N(z)-K_M(z)\rVert_3
\longrightarrow0
\]

as (N,M\) tend to infinity, together with one cutoff-independent analytic
bound. Completeness of (mathcal S_3) then constructs (K(z)).

This is the direct hostile gate for the labelled cutoff system.

## Why seam zeros remain possible

The theorem applies only inside a sector. Suppose instead that the same
(mathcal S_3)-norm convergence and accretivity extended through a
neighborhood of a seam point (z_0). Suppose also that all retained
countercurrents converged there to finite analytic functions. Then the relative
determinant

\[
e^{J_1+J_2+J_{\partial}}
\det_3(I+K)
\]

would be nonzero at (z_0).

Consequently an actual seam zero forces at least one boundary failure:

- no cross-seam (mathcal S_3)-norm limit exists;
- accretivity is only sector-local and has no common boundary extension;
- a primitive, square, seam, endpoint, or continuation countercurrent diverges;
- the determinant line changes kernel or cokernel at the boundary;
- the sewn scalar is not represented by the same relative determinant across
  the seam.

Critical-line zeros are therefore boundary singularities of the two-sector
representation. They are not ordinary kernels of a regularly extended
accretive operator.

## Completion-at-infinity gate

The earlier modulation and adjacent-label hostiles now have a precise target.
They must be tested against the actual (mathcal S_3) operator family, not
against an unrestricted coefficient norm.

For every compact (C), define

\[
\Delta_{N,M}(C)
=
\sup_{z\in C}
\lVert K_N(z)-K_M(z)\rVert_3.
\]

The route fails if one source-admissible packet sequence has

\[
\limsup_{N,M\to\infty}\Delta_{N,M}(C)>0.
\]

Pointwise convergence of matrix entries, scalar traces, or completed products
does not repair this failure.

## Countercurrent convergence

The determinant norm theorem does not control the removed first two currents.
They require separate locally uniform convergence after the declared relative
renormalization:

\[
J_{1,N}+J_{2,N}+J_{\partial,N}.
\]

Their exponential remains zero-free wherever the renormalized sum is finite.
If it diverges at the seam, that divergence is typed boundary data and cannot
be silently cancelled after scalar projection.

## Decisive next audit

For the proposed labelled theta/Tate operators:

1. choose one compact subset of each open half-plane;
2. compute or bound (Delta_{N,M}(C));
3. verify cutoff accretivity;
4. verify the finite Schatten-three countercurrent identity;
5. control the renormalized boundary exponential separately;
6. identify the exact topology that fails when approaching the seam.

An off-seam failure of the (mathcal S_3)-Cauchy law closes the Hurwitz route.
Sector-local convergence with a precisely typed seam failure is the required
architecture, not a defect.
