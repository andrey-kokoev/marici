# Convergence and codiagonal naturality do not select the G4 arithmetic loading

## Question

Can the current G4 arithmetic-loading slot be filled uniquely from absolute Green summability and commutation with the oriented radial codiagonal?

## Claim boundary

No. At least two source-derived coefficient families satisfy those analytic requirements but are not proportional and encode different constructions. The first missing typed object is a source arrow selecting one loading for the G4 radial feature. No coefficient should be installed without that arrow.

## Problem

The retained radial packet admits a codiagonal

\[
C_pX_p
=E_{p,+}+E_{p,-}
-
\frac12(W_{p,+}+W_{p,-}).
\]

Any loading \(\omega_p\) satisfying the prime majorant

\[
\sum_p|\omega_p|
\bigl(1+(\log p)^{M_j}\bigr)<\infty
\]

for every fixed jet order can be summed before or after applying \(C\). This is a continuity theorem, not a selection principle.

## Bold conjecture

Absolute convergence together with codiagonal commutation uniquely determines the canonical G4 loading up to one scalar.

## Named rivals

1. The mixed primitive--square loading and Euler-to-theta loading are distinct admissible families.
2. Their difference is a harmless nowhere-zero scalar normalization.
3. One is selected only after specifying whether G4 compiles the relative determinant cumulants or the forward theta shell incidence.

## Two admissible loadings

The mixed primitive--square coefficient is

\[
\omega_p^{\rm mix}(\sigma)
=
\frac12p^{-3/2-\sigma},
\qquad \sigma\ge0.
\]

The Euler-to-theta coefficient is

\[
c_p
=
2(\log p)
\sum_{k\ge1}p^{-k/2}\Phi'(k\log p).
\]

The first has fixed polynomial Euler decay. The second carries the completed-theta derivative and has superexponential prime-power decay under the declared Gaussian/theta estimates. Both satisfy every compact-local polynomial majorant and commute with the same codiagonal by absolute convergence.

## Strongest falsification attempt

If the two families differed by one nonzero scalar \(A\), then

\[
c_p=A\omega_p^{\rm mix}(0)
\]

would force their ratio to remain constant. Instead the theta derivative contributes superexponential decay beyond the factor \(p^{-1/2}\), while

\[
\omega_p^{\rm mix}(0)=\frac12p^{-3/2}
\]

has only polynomial decay. Consequently

\[
\frac{c_p}{\omega_p^{\rm mix}(0)}
\longrightarrow0
\]

along the prime labels under the cited source estimates, unless the theta derivative packet is identically degenerate. It is therefore not a fixed nonzero scalar normalization.

The bold conjecture is rejected: convergence and codiagonal naturality admit inequivalent loadings.

## Typed distinction

The two coefficients answer different source questions:

- \(\omega^{\rm mix}\) weights a renormalized primitive--square Adams block;
- \(c_p\) is a forward Euler-to-theta incidence coefficient.

A G4 constructor must specify which source object is mapped into the radial feature packet. Equal codomain and common summability do not provide that map.

## First missing object

The absent authority is a source-derived loading arrow

\[
L_{\rm G4}:\mathcal E_{\rm declared}
\longrightarrow
\bigoplus_p\mathbb C X_p
\]

whose prime coordinates are fixed by its source incidence and whose codomain is the retained oriented radial packet. Its acceptance test is:

1. declare whether the source is the relative-determinant cumulant block, forward theta shell, or another named object;
2. derive the coefficient at each \((p,k)\);
3. preserve prime, grade, orientation, and type-fiber labels;
4. prove codiagonal and cutoff naturality;
5. compare rather than identify any rival loading.

## Disposition

The G4 arithmetic-loading slot cannot be filled from existing analytic criteria. Two inequivalent source-derived families pass them. This branch stops at the missing typed loading arrow; further normalization arguments cannot select between the rivals. The retained observer remains compatible with either loading as a convergent map, but external G4 identification requires the source declaration.
