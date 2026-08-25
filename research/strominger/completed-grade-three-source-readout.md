# The grade-three source readout is a magnetic fourth-order incidence port

> Functional-completion refinement: this packet uses the local coordinate
> trivialization and scalar magnetic projection. The globally covariant object
> is the paired spin-four map derived in `global-grade-three-spin-spectrum.md`.
> Its smooth/distributional completion has additional `l=2,3,4` low-mode
> kernels that have zero intersection with the finite point-supported packet
> treated here.

## Operator

For a spin-two pair `(C+,C-)`, define the complex curl representative

\[
 \mathfrak M_3(C^+,C^-)
 =\partial_{\bar z}D_z^3C^+
  -\partial_zD_{\bar z}^3C^-.
\]

On the real slice this is `2i` times the imaginary grade-three density, up to
the fixed normalization convention.  For the invariant puncture generators
`(Khat^+_xi,Khat^-_xi)`, exact differentiation yields a rational function
with denominator

\[
 (z-\xi)^4(\bar z-\bar\xi)^4
 (1+\xi\bar\xi)(1+z\bar z)^7.
\]

Its factored numerator is recorded by the checker rather than expanded into
the theorem statement.  It is not identically zero.  At the centered
puncture,

\[
 \boxed{
 \mathfrak M_3(\widehat K^+_0,\widehat K^-_0)
 =-\frac{6(z-\bar z)(z+\bar z)(z^2+\bar z^2)(5z\bar z-1)}
 {z^4\bar z^4(1+z\bar z)^7}.}
\]

Thus the coherent physical point source is not a grade-three zero mode.

## Source jets

The observation differential operator has coefficients independent of the
source labels. Therefore

\[
 \mathfrak M_3(\partial_\xi^r\partial_{\bar\xi}^s\widehat K^+,
 \partial_\xi^r\partial_{\bar\xi}^s\widehat K^-)
 =\partial_\xi^r\partial_{\bar\xi}^s
 \mathfrak M_3(\widehat K^+,\widehat K^-).
\]

The grade-three map is consequently a continuous filtered morphism from each
finite source-jet stage to finite-order puncture distributions, and hence from
the strict LF union to the finite-order distributional union.

## Parity factorization

Helicity/reflection exchange reverses the two terms:

\[
 \mathfrak M_3(Qh)=-\mathfrak M_3(h).
\]

It follows that

\[
 \boxed{\mathfrak M_3=\mathfrak M_3\Pi_M,
 \qquad \mathcal H_{Q=+1}\subseteq\ker\mathfrak M_3.}
\]

This electric kernel is forced by the chosen magnetic readout.  It is the
same complementary-port alias classified in the parity theorem, not new rank
loss.  Any additional kernel must be sought inside the magnetic eigenspace.

## First-nonfaithful-arrow refinement

The map factors as

\[
 \mathcal H\xrightarrow{\Pi_M}\mathcal H_{Q=-1}
 \xrightarrow{\widetilde{\mathfrak M}_3}\mathcal D'_{\rm punct}(S^2).
\]

The first arrow explains the universal electric kernel.  The open
classification question is now sharply reduced to whether the second arrow
is injective before conservation and collision specialization.

## Evidence

`checkers/completed_grade_three_source_readout_checks.py` verifies the exact
rational response, the centered formula, source/observation derivative
commutation, fourth-order incidence support, and magnetic projector
factorization.
