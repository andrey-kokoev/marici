# Erratum: kinematic C13 is a mesh charge, not a proved Schwarz trace

## Source definition

The scattering transcript defines the discrete wave equation on every causal mesh by

\[
X_{ij}+X_{i+1,j+1}-X_{i,j+1}-X_{i+1,j}=C_{ij}.
\]

Here \(C_{ij}\) is introduced explicitly as a constant source/charge associated with the mesh. Summing small diamonds telescopes to the integrated charge of a larger diamond.

At four points this gives

\[
X_{13}+X_{24}=C_{13},
\]

with positivity imposed on the source and channel coordinates to obtain the associahedral interval.

## Retraction

No reviewed source identifies

\[
C_{13}=\operatorname{tr}S_L(p).
\]

The trace/eigenvalue dictionary is a valid abstract parametrization of a two-by-two Hermitian matrix, but its assignment to the kinematic symbols \(C_{13},X_{13},X_{24}\) is conjectural and was previously stated too strongly.

Likewise, the transcript does not identify the mesh charge with a prime observer, a prime-prime observer, or their Schwarz determinant.

## Exact missing comparison

To use the positive-geometry theorem for RH, one must construct a source map satisfying

\[
C_{13}^{\mathrm{mesh}}=a+c,
\qquad
X_{13}^{\mathrm{mesh}}X_{24}^{\mathrm{mesh}}=ac-|b|^2,
\]

where \(a,b,c\) are the primitive/prime-prime observation readings.

Neither equality follows from the discrete wave equation. They are the proposed comparison theorem, not prior input.

## Search disposition

Repository search and `pnpm pdf:search` found:

- the transcript definition of \(C_{ij}\) as a mesh charge;
- generic positive-geometry and associahedron background;
- no source establishing a Gram, trace, determinant, or spectral-channel interpretation of \(C_{13}\).

Thus the existing positive associahedral interval cannot yet be used to infer rung-four Schwarz positivity.
