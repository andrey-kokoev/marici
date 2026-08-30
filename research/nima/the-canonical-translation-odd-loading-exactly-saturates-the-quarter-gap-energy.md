# The canonical translation-odd loading exactly saturates the quarter-gap energy

## Benchmark problem

The bare odd auxiliary energy on the half-density line is

\[
S=-\partial_u^2+\frac14.
\]

Before estimating the source causal-history operator, the simplest
reciprocal-odd perturbation is the translation generator

\[
T=\partial_u,
\qquad
T^*=-T.
\]

Hence \(iT\) is Hermitian. Its normalized loading is

\[
K
=
S^{-1/2}(i\partial_u)S^{-1/2}.
\]

## Exact Fourier multiplier

Under the unitary Fourier transform, \(S\) has multiplier

\[
\xi^2+\frac14,
\]

while \(i\partial_u\) has multiplier \(-\xi\), up to the fixed Fourier
sign convention. Therefore \(K\) has multiplier

\[
m(\xi)
=
-\frac{\xi}{\xi^2+\frac14}.
\]

Its norm is

\[
\|K\|
=
\sup_{\xi\in\mathbb R}
\frac{|\xi|}{\xi^2+\frac14}
=
1,
\]

with saturation at \(|\xi|=\frac12\).

Thus the canonical unweighted translation-odd perturbation is only
non-strictly dominated by the quarter-gap energy.

## Scaled loading

For a source coefficient \(\alpha\), let

\[
D_\alpha
=
S+\alpha i\partial_u.
\]

Then

\[
\left\|
S^{-1/2}(\alpha i\partial_u)S^{-1/2}
\right\|
=
|\alpha|.
\]

Consequently,

\[
D_\alpha>0
\]

with a uniform normalized margin precisely when

\[
|\alpha|<1.
\]

At \(|\alpha|=1\), the lower spectral symbol touches zero:

\[
\xi^2+\frac14-\xi
=
\left(\xi-\frac12\right)^2
\]

for the saturating polarization. Finite test packets can appear positive
while approximate Fourier modes near \(\xi=\frac12\) destroy coercivity.

## Interpretation

The quarter-gap theorem fixes the absolute auxiliary scale, but it does not
supply strict contractivity for free. A causal-history perturbation with the
full strength of the translation generator exactly consumes the available
gap.

Therefore the source must provide at least one of:

1. an exact coefficient \(|\alpha|<1\);
2. a history operator strictly smaller than \(\partial_u\) in the
   \(S\)-relative norm;
3. an authorized boundary condition or spectral exclusion removing
   neighborhoods of \(|\xi|=\frac12\);
4. an additional positive even-history term increasing \(S\).

None may be inserted merely to obtain positivity.

## Relation to the actual comoving connection

The transported ray derivative is not automatically the constant translation
generator. It carries the degree-minus-one factor described by

\[
\mathcal M_n\partial_x
=
n^{-1} e^{-u}
\left(\partial_u-\frac12\right)\mathcal M_n
\]

with the convention fixed by the half-density map. The multiplication factor
\(e^{-u}\) changes the relative-bound problem and can destroy translation
invariance.

Hence the calculation above is an exact benchmark, not an identification of
the source causal-history operator.

## New hostile

Replace the actual causal history by \(\partial_u\), verify positivity on
every finite Fourier window avoiding \(\xi=\frac12\), and infer a uniform
margin. As the windows approach the saturating frequency, the margin tends to
zero.

## Frontier

The remaining auxiliary theorem is now quantitative:

\[
\kappa_{\mathrm{hist}}
=
\left\|
S_{\mathrm o}^{-1/2}
(iT_{\mathrm{hist}})
S_{\mathrm o}^{-1/2}
\right\|.
\]

The Adams cell requires a source proof that

\[
\kappa_{\mathrm{hist}}<1
\]

uniformly over primes and compact off-seam regions. The simplest canonical
odd generator gives equality, so strictness must come from genuine source
structure rather than the quarter-gap alone.
