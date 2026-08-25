# The adelic bridge factors through the arithmetic phase circle

## Question

What geometric object remains after the standard adelic vacuum annihilates
all nonintegral rational characters?

## Spectral factorization

Let `G=A/Q` and let `K_f` be the operator of packet 101.  Its Pontryagin dual
is `Q`.  Denote by `P_Z` the orthogonal projection onto

\[
 \mathcal H_{\mathbb Z}
 =\overline{\operatorname{span}}\{\chi_n:n\in\mathbb Z\}
 \subset L^2(G).
\]

On this subspace define the number operator

\[
 N\chi_n=n\chi_n.
\]

The multiplier calculation of packet 101 gives the exact factorization

\[
 \boxed{K_f=P_{\mathbb Z}e^{-\pi N^2}P_{\mathbb Z}.}
\]

There is no approximation or zero input in this identity.  The finite
adelic factors supply `P_Z`; the real Gaussian supplies the heat operator.

## Identification of the surviving geometry

By Pontryagin duality, the Hilbert space with Fourier labels `Z` is

\[
 \mathcal H_{\mathbb Z}\cong L^2(\mathbb R/\mathbb Z).
\]

Equivalently, if `Z^perp` is the annihilator in `G` of the subgroup
`Z subset Q=G^`, then

\[
 G/\mathbb Z^\perp\cong\widehat{\mathbb Z}\cong\mathbb R/\mathbb Z.
\]

Thus the canonical bridge has the geometric factorization

\[
 L^2(\mathbb A/\mathbb Q)
 \xrightarrow{\;P_{\mathbb Z}\;}
 L^2(\mathbb R/\mathbb Z)
 \xrightarrow{\;e^{-\pi N^2}\;}
 L^2(\mathbb R/\mathbb Z)
 \hookrightarrow L^2(\mathbb A/\mathbb Q).
\]

The first arrow is arithmetic selection.  The middle arrow is diffusion on a
circle.  They are different operations and should not be compressed into a
single unexplained positivity claim.

## Interpretation of the operator stimulus

The operator suspected that changing the angle between two half-plane
presentations might reveal a circle.  The exact survivor is not a Euclidean
circle obtained by visually rescaling an oval in a zeta plot.  It is the
Pontryagin-dual phase circle of the integral character lattice.  The two
Clifford charts meet through this compact quotient only after the finite-place
vacuum has enforced integrality.

This supplies a typed meaning for the intuition:

\[
 \boxed{
 \text{integral charge lattice}
 \longleftrightarrow
 \text{compact phase circle}.}
\]

The conjugate observables are integer winding `N` and phase on
`R/Z`.  Fourier quarter-turn exchanges their current and covector
descriptions.  What looked like two planar sectors is therefore more naturally
a polarization of one phase-space relation.

## Consequence for zeros

The operator `e^{-pi N^2}` has strictly positive eigenvalues on the integral
sector, so it has no kernel there.  All kernel vectors of `K_f` arise before
circle diffusion, from failure of integrality:

\[
 \ker K_f=\ker P_{\mathbb Z}.
\]

Therefore Riemann zeros cannot be identified with this elementary kernel.
They would have to be losses of transversality in a later comparison of
dilated circle heat traces, after Mellin transformation and modular sewing.
This separates two meanings of zero:

1. **inadmissibility zero:** removed by the finite-place integrality projector;
2. **spectral-incidence zero:** a possible failure in the completed relative
   comparison inside the admitted sector.

Conflating them was the hidden categorical error.

## Next gate

The next construction should retain the entire dilation family on the circle,
not only its scalar trace.  The hard question is whether modular inversion
acts as a source-derived correspondence between the winding and phase
polarizations whose relative determinant is `Xi` up to explicit units.

The smallest falsifier is a source-compatible modular correspondence whose
relative determinant has an off-seam zero.  Finding one would show that the
circle factorization explains completion and integrality but supplies no RH
coercivity.
