# Crystal refinement of the RH relative-boundary candidate

Date: 2026-09-08

## Why plain IndCoh is not the closest type

The completed theta packet carries differential equations, a logarithmic connection, Fourier transport, and endpoint distributions.  Volume II defines crystals by

\[
\operatorname{Crys}(X)=\operatorname{IndCoh}(X_{\mathrm{dR}}),
\]

and identifies crystals with D-modules on smooth schemes.  Its correspondence functoriality includes pullback and de Rham direct image.  These operations are closer to the source constructions than an ordinary coherent sheaf on the parameter base.

The speculative object should therefore be a crystal `F_theta` on the realified parameter base

\[
X=\operatorname{Spec}\mathbb R[x,y],
\qquad z=x+iy,
\]

with the reciprocal involution `(x,y)↦(-x,y)`, rather than merely an object of `IndCoh(X)`.

## Boundary category

For the seam embedding `i:Z=V(x)→X`, the closed-embedding discussion in Volume II recalls Kashiwara equivalence: D-modules on `X` set-theoretically supported on `Z` are equivalent to D-modules on `Z`.  Thus a comparison fibre proved supported on the seam has a canonical boundary realization; it need not be converted into an endpoint scalar by hand.

The candidate chain becomes

\[
F_\theta
\longmapsto
B_{\mathrm{rel}}(F_\theta)
=
\operatorname{fib}(F_\theta\to j_{\mathrm{dR},*}j_{\mathrm{dR}}^!F_\theta)
\longmapsto
i^!_{\mathrm{dR}}B_{\mathrm{rel}}(F_\theta)
\longmapsto
D_{\mathrm{bw}}.
\]

The first two maps belong to the crystal/D-module formalism.  Only the last Hermitian realization is sector-specific.

## Square-zero seam jet

Volume II's square-zero-extension calculation describes an object by an underlying object plus a null-homotopy for the action of the shifted conormal datum.  This matches the already checked first-order factorization

\[
D_{\mathrm{bw}}=-2xB.
\]

A first seam thickening `x^2=0` retains the coefficient `-2B` as conormal data.  It does not prove that the theta divisor is supported on `x=0`; it only gives the correct recipient for a boundary jet if support is independently established.

## Strongest test

Construct a finite-cutoff differential module carrying:

1. the plus and minus regularized determinant connections;
2. their determinant-three transition;
3. the four-channel Poisson section;
4. the first seam jet under `x^2=0`.

Restrict it to `X\setminus Z`.  The crystal candidate survives only if the fibre of the plus/minus comparison restricts to zero there.  A nonzero generic horizontal solution is the exact residual and rejects seam support.

## Scope

Crystals improve the type of the candidate but do not solve transversality.  The polynomial reciprocal-equivariant hostile with an off-seam zero still applies.  No automatic functor sends reciprocal symmetry, holonomicity, or a flat connection to seam-supported divisor data.

## PDF locators

- `Derived algebraic geometry Vol2.pdf`, Chapter 4 introduction, Sections 0.2.1--0.2.5;
- Chapter 4, Section 1.1--1.2 for `Crys(X)=IndCoh(X_dR)`;
- Chapter 4, Section 4.4 for closed embeddings and Kashiwara equivalence;
- Section 6.4 for square-zero extensions and the canonical fibre sequence.
