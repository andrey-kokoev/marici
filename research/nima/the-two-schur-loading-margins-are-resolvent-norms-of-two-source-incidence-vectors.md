# The two Schur-loading margins are resolvent norms of two source incidence vectors

## Rank-two endpoint reduction

Let the endpoint basis be \(e_1,e_2\), and define the two independently
typed auxiliary incidence vectors

\[
c_{1,p}=C_p^*e_1,
\qquad
c_{2,p}=C_p^*e_2.
\]

For either reciprocal sheet,

\[
R_{p,\pm}=C_pD_{p,\pm}^{\dagger}C_p^*.
\]

Its diagonal entries are exactly

\[
r_{jj,p}^{\pm}
=
\left\langle
c_{j,p},
D_{p,\pm}^{\dagger}c_{j,p}
\right\rangle
=
\left\|
D_{p,\pm}^{\dagger/2}c_{j,p}
\right\|^2,
\]

after radical descent.

Thus the two Pauli loading margins require no full endpoint operator norm.
They are two source-vector resolvent estimates.

## Exact criterion

Write

\[
a_{1,p}=a_p,
\qquad
a_{2,p}=b_p.
\]

The Pauli-observed endpoint frame survives the Schur short uniformly exactly
when there is \(\varepsilon>0\) such that

\[
\left\|
D_{p,\pm}^{\dagger/2}c_{j,p}
\right\|^2
\le
a_{j,p}-\varepsilon
\]

for

\[
j\in\{1,2\},
\qquad
\pm,
\qquad
p.
\]

Equivalently, the dimensionless source-vector loadings

\[
\ell_{j,p}^{\pm}
=
\frac{
\|D_{p,\pm}^{\dagger/2}c_{j,p}\|^2
}{
a_{j,p}
}
\]

must satisfy

\[
\sup_{p,j,\pm}\ell_{j,p}^{\pm}<1.
\]

This is the sharp local criterion in the declared Pauli frame.

## Quarter-gap bound

The source half-density operator gives

\[
S_p\ge\frac14I.
\]

If the internal reciprocal perturbation satisfies

\[
\left\|
S_p^{-1/2}(iT_p)S_p^{-1/2}
\right\|
\le1-\delta_{\mathrm{aux}},
\]

then both sheets obey

\[
D_{p,\pm}
\ge
\frac{\delta_{\mathrm{aux}}}{4}I
\]

on reduced support. Hence

\[
r_{jj,p}^{\pm}
\le
\frac4{\delta_{\mathrm{aux}}}
\|c_{j,p}\|^2.
\]

A concrete sufficient source estimate is therefore

\[
\|c_{j,p}\|^2
\le
\frac{\delta_{\mathrm{aux}}}{4}
(1-\eta)a_{j,p}
\]

for one uniform \(\eta>0\). It yields

\[
\ell_{j,p}^{\pm}\le1-\eta.
\]

Because \(a_{j,p}\ge m_\nu^2\), an absolute incidence bound strictly below

\[
\frac{\delta_{\mathrm{aux}}m_\nu^2}{4}
\]

is sufficient, though the relative estimate is sharper.

## Spectral alignment

The quarter-gap estimate discards the spectral position of \(c_{j,p}\).
The exact resolvent norm may remain small even when the coarse absolute bound
fails.

Accordingly the audit order is:

1. compute the source incidence vectors \(c_{1,p},c_{2,p}\);
2. determine their reciprocal parity;
3. evaluate their sheetwise spectral measures for \(D_{p,\pm}\);
4. compute the two resolvent norms;
5. use the quarter-gap bound only as a fallback majorant.

This replaces a full matrix Birman--Schwinger calculation by two scalar
Stieltjes transforms of source spectral measures.

## Spectral-measure form

Let \(E_{p,\pm}(\lambda)\) be the spectral resolution of
\(D_{p,\pm}\). Then

\[
r_{jj,p}^{\pm}
=
\int_{(0,\infty)}
\lambda^{-1}
\,d\mu_{j,p}^{\pm}(\lambda),
\]

where

\[
d\mu_{j,p}^{\pm}(\lambda)
=
d\langle
c_{j,p},
E_{p,\pm}(\lambda)c_{j,p}
\rangle.
\]

The completion problem is therefore infrared concentration of two incidence
measures, not the entire auxiliary spectrum. A soft auxiliary mode is harmless
if both incidence vectors are orthogonal to it.

## Radical condition

Before writing the resolvent integral, prove

\[
c_{j,p}\perp\ker D_{p,\pm}.
\]

Equivalently,

\[
\ker D_{p,\pm}\subseteq\ker C_p.
\]

Otherwise the pseudoinverse formula can conceal an ill-defined or dark
coupling.

## Minimal hostiles

1. Uniform quarter-gap, but one incidence norm saturates its endpoint budget.
2. A soft auxiliary spectral mode carrying no endpoint incidence: the coarse
   inverse bound diverges while the exact resolvent loading stays finite.
3. Small incidence norms with mass concentrated near a shrinking auxiliary
   eigenvalue.
4. One reciprocal sheet passes and the reflected incidence on the other does
   not.
5. Both diagonal loadings pass while an untraced mixed linking block has the
   wrong orientation.

## Verdict

Pauli-twirled Schur survival is controlled by only two source incidence
vectors. The next executable theorem is not a full endpoint Gram comparison;
it is the pair of sheetwise estimates

\[
\|D_{p,\pm}^{\dagger/2}C_p^*e_j\|^2<a_{j,p}.
\]

The canonical quarter-gap supplies a uniform resolvent denominator. What
remains source-specific is the magnitude and spectral support of the
primitive and square incidence vectors.
