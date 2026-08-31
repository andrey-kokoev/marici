# The forced Stokes--Wronskian comparison has dense nonclosed range in the declared Köthe source

## Declared source topology

On prime labels, the existing projective exponential source is

\[
\mathcal A_{\exp}
=
\bigcap_{\delta>0}\ell^1(\mathbb P,p^\delta),
\qquad
q_\delta(x)=\sum_p|x_p|p^\delta.
\]

Finite prime packets are dense in every seminorm.

The forced local Stokes-to-Wronskian scalar is

\[
T e_p=\lambda_p e_p,
\qquad
\lambda_p=\frac{-\kappa_p}{2s_p}>0,
\]

and \(\lambda_p\) tends to zero faster than every inverse power of \(p\).

## Forward continuity

The sequence \((\lambda_p)\) is bounded.  Therefore

\[
q_\delta(Tx)
\le \sup_p\lambda_p\,q_\delta(x)
\]

for every \(\delta>0\).  Thus

\[
T:\mathcal A_{\exp}\to\mathcal A_{\exp}
\]

is continuous and injective.

## The inverse is not source-continuous

Unlike the previously studied odd Jacobi coefficient, whose inverse loses
only a finite polynomial order, \(\lambda_p^{-1}\) grows faster than every
power of \(p\).  Consequently there are no \(\delta,\delta'>0\) and \(C>0\)
such that

\[
q_\delta(T^{-1}y)\le Cq_{\delta'}(y)
\]

on the range.  Testing on one basis vector would require

\[
p^\delta\lambda_p^{-1}
\le Cp^{\delta'},
\]

contradicting superpolynomial growth of \(\lambda_p^{-1}\).

Hence \(T\) is not a Köthe automorphism of the declared projective
exponential source.

## Explicit nonclosed-range witness

The coefficient sequence

\[
y=(\lambda_p)_p
\]

belongs to \(\mathcal A_{\exp}\), since \(\lambda_p\) decays faster than every
power and therefore

\[
\sum_p\lambda_pp^\delta<\infty
\]

for every \(\delta>0\).

Let \(P_X\) be the finite-prime cutoff.  Each

\[
y^{(X)}=P_Xy
\]

lies in the range, because

\[
y^{(X)}=T(P_X\mathbf1)
\]

and \(P_X\mathbf1\) has finite support.  Moreover,

\[
y^{(X)}\to y
\]

in every Köthe seminorm.

But \(y\notin\operatorname{ran}T\).  Its only coordinatewise preimage is

\[
T^{-1}y=\mathbf1=(1,1,\ldots),
\]

which does not belong to \(\mathcal A_{\exp}\).  Therefore

\[
{
\operatorname{ran}(T:\mathcal A_{\exp}\to\mathcal A_{\exp})
\text{ is not closed}.
}
\]

Because all finite packets lie in the range and are dense in
\(\mathcal A_{\exp}\), the range is in fact dense.

## Reconciliation with the pullback completion

The weighted Hilbert pullback completion with norm

\[
\sum_p\lambda_p^2|x_p|^2
\]

makes \(T\) unitary onto \(\ell^2\).  That statement remains correct, but it
changes the source object.  It does not establish closed range in the already
declared projective exponential Köthe topology.

This specializes and strengthens the earlier theorem that the theta-sampling
pullback metric is not equivalent to the Euler half-density topology.  Here
the exact Stokes denominator does not repair the mismatch: it decays only on
the logarithmic-Gaussian scale, while the theta numerator decays on the
\(e^{-Bp^2}\) scale.

## Consequence

The isolated Stokes-to-Wronskian comparison cannot close the full G1.1
pushout in the current source topology.  A valid repair must be independently
source-authorized and must do at least one of the following:

1. replace the domain by the theta pullback object;
2. enlarge the projective Köthe scale to include the inverse theta-sampling
   growth;
3. retain another noncompact arithmetic port that jointly restores closed
   range.

No such repair is proved here.  No RH conclusion is authorized.
