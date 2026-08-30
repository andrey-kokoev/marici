# A Riemann Zero Is Where the Additive-to-Connected Comparison Loses Meaning

## The multiplicative discrepancy in source space

Let

\[
\psi(x)=\sum_{n\le x}\Lambda(n)
\]

be the prime-power counting current. In \(\Re s>1\),

\[
-\frac{\zeta'(s)}{\zeta(s)}
=
\int_{1^-}^{\infty}x^{-s}\,d\psi(x).
\]

Subtract the continuum multiplicative density \(dx\) and define

\[
d\nu_{\mathrm{mult}}=d\psi-dx.
\]

Its Mellin readout is

\[
\mathcal M\nu_{\mathrm{mult}}(s)
=
-\frac{\zeta'(s)}{\zeta(s)}
-\frac1{s-1}.
\]

The pole at \(s=1\) cancels. Every remaining pole in the critical strip is
a nontrivial zeta zero, with residue equal to minus its multiplicity.

Equivalently,

\[
\mathcal M\nu_{\mathrm{mult}}(s)
=
1+s\int_1^\infty
(\psi(x)-x)x^{-s-1}\,dx
\]

where the integral initially converges in the Euler chamber.

## The additive source and the connected current

The completed theta construction produces the additive lattice--Haar defect
section \(\xi(s)\). Its logarithmic derivative is

\[
\frac{\xi'(s)}{\xi(s)}
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\frac{\Gamma'(s/2)}{\Gamma(s/2)}
+\frac{\zeta'(s)}{\zeta(s)}.
\]

Therefore

\[
\mathcal M\nu_{\mathrm{mult}}(s)
=
-\frac{\xi'(s)}{\xi(s)}
+\frac1s
-\frac12\log\pi
+\frac12\frac{\Gamma'(s/2)}{\Gamma(s/2)}.
\]

The archimedean correction on the right is holomorphic throughout the open
critical strip. Hence the multiplicative prime discrepancy and the
logarithmic connection of the additive theta section have exactly the same
nontrivial singularities.

## Loss of meaning is literal

For a line-valued section \(\sigma\), the operation

\[
d\log\sigma=\frac{d\sigma}{\sigma}
\]

is defined only on the invertible locus \(\sigma\ne0\). It converts the
additive section into its connected multiplicative current. At
\(\sigma=0\), this comparison is not merely numerically large: the
operation itself is undefined.

Applied to \(\xi\), a Riemann zero is precisely a point where the passage

from the completed additive lattice--Haar section to the connected
prime-density current loses meaning. The connected current records the loss
as a quantized pole whose residue is the zero multiplicity.

This distinguishes two objects that scalar notation had made look like one:

1. the additive completed section, which may vanish;
2. its multiplicative logarithmic connection, which exists only where the
   section is invertible.

## Relation to the two-sector programme

On each open reciprocal sector, strict unit completion makes
\(d\log\xi\) a valid holomorphic comparison. At the unitary seam the two
sectorwise logarithmic charts may meet through singular boundary data.

RH can therefore be stated as:

> The additive-to-connected comparison loses meaning only on the unitary
> Fourier--Tate interface.

This formulation explains what fails at a zero and why two sector charts are
needed. It does not yet prove that the failure locus is confined to their
interface.

## Why positivity does not transfer directly

The additive theta defect is represented by a positive lattice--Haar deficit.
The multiplicative current is represented by the signed measure
\(d\psi-dx\). The passage between them uses a logarithm and a derivative;
it is nonlinear and requires inversion of the additive section.

Consequently positivity of the theta deficit cannot simply be pushed through
the comparison. The missing theorem must control the logarithmic comparison
before inversion fails, or derive sectorwise primitive units whose
invertibility makes the comparison legitimate.

## Sharp target and falsifier

Construct from labelled theta/Tate data a sectorwise connection
\(\nabla_\pm\) such that:

1. it agrees with \(d\log\xi\) in the Euler chamber after the canonical
   Fock--Mellin comparison;
2. it is holomorphic throughout the corresponding open sector;
3. its primitive component has Mellin measure \(d\psi-dx\);
4. reciprocal sewing relates the two sector connections;
5. no division by \(\xi\) is used in its construction.

A pole of the constructed connection off the seam, exhaustion dependence, or
use of \(\xi^{-1}\) before proving invertibility falsifies the proposed
explanation.

