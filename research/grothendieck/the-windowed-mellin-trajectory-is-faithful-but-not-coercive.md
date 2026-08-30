# The windowed Mellin trajectory is faithful but not coercive

Author: marici.Grothendieck

Date: 2026-08-28

## Generating object

For a finite or absolutely summable labelled packet \(c=(c_n)\), define its
vertical Mellin trajectory

\[
F_c(t)=\sum_{n\ge1}c_n n^{it}.
\]

This is the generating function of the Mellin jet tower:

\[
\partial_t^kF_c(0)=i^k\sum_n c_n(\log n)^k.
\]

Thus the complete trajectory retains every jet without choosing or inverting
a growing Vandermonde basis.

## Faithfulness theorem

Let \(w(t)>0\) for almost every real \(t\), with \(w\) integrable. Define

\[
\mathcal E_w(c)=\int_{\mathbb R}w(t)|F_c(t)|^2\,dt.
\]

For every nonzero finite complex measure

\[
\mu_c=\sum_n c_n\delta_{\log n}
\]

of finite total variation,

\[
\mathcal E_w(c)>0.
\]

Indeed, zero energy would imply \(F_c(t)=0\) almost everywhere. The
Fourier--Stieltjes transform of a finite measure is continuous, hence it
would vanish everywhere. Uniqueness of Fourier transforms of finite
measures then gives \(\mu_c=0\), and distinct logarithmic labels give
\(c_n=0\) for every \(n\).

Therefore a fixed nonzero completed coefficient measure cannot disappear
from the full vertical Mellin trajectory.

## Gaussian window

For the heat window \(w_a(t)=e^{-t^2/(4a)}\), \(a>0\), direct integration
gives

\[
\mathcal E_a(c)
=
\sqrt{4\pi a}\sum_{n,m}c_n\overline{c_m}
e^{-a(\log n-\log m)^2}.
\]

The logarithmic Gaussian kernel is strictly positive definite on every
finite set of distinct arithmetic labels. This is the integrated, basis-free
form of Entry 4101's centered Vandermonde theorem.

## Noncoercivity theorem

Faithfulness does not yield a lower frame bound against the ordinary
coefficient \(\ell^2\) norm. Let

\[
c^{(n)}=\frac{e_{n+1}-e_n}{\sqrt2}.
\]

Then \(\|c^{(n)}\|_{\ell^2}=1\), while for the Gaussian window

\[
\mathcal E_a(c^{(n)})
=
\sqrt{4\pi a}
\left(1-e^{-a(\log(1+1/n))^2}\right)
\longrightarrow0.
\]

The same conclusion holds for broad continuous windows by dominated
convergence. Adjacent labels remain arithmetically distinct but become
analytically indistinguishable at large scale.

## Meaning for the RH programme

This separates two completion claims:

- pointwise faithfulness survives for every fixed finite-variation source
  measure;
- uniform coercivity fails in the unaugmented analytic coefficient norm.

Thus an RH argument at a fixed spectral parameter may use strict positivity
of a full trajectory energy, provided the zero-state belongs to this measure
class. It may not claim a cutoff-uniform lower bound without retaining an
additional discrete arithmetic port.

The Gaussian window is presently a canonical model of archimedean heat
sampling, not yet the derived theta/Tate energy. The next acceptance gate is
to derive the actual window and boundary terms from the completed theta
source and check that it is positive almost everywhere. If that succeeds,
completion faithfulness follows without finite determinant certification.
