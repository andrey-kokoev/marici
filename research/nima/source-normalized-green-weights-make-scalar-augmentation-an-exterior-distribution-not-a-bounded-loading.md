# Source-normalized Green weights make scalar augmentation an exterior distribution, not a bounded loading

## Actual diagonal scaling

The transported source and history metrics scale quadratically with the Euler half-density. For the label \((p,k)\),

\[
a_{\sigma,p,k}
=
\frac1k p^{-k(1/2+\sigma)},
\]

and the source-derived diagonal Green weight has the form

\[
g_{\sigma,p,k}
=
|a_{\sigma,p,k}|^2g_{0,k},
\]

where \(g_{0,k}\) is the normalized base-fiber energy, uniformly comparable on the declared local incidence plane.

This follows from isometric Mellin translation: label displacement changes the object fiber but not its normalized base energy.

## Normalized augmentation

The scalar augmentation uses the same coefficient \(a_{\sigma,p,k}\). Therefore its normalized coordinate is

\[
\frac{a_{\sigma,p,k}}
{\sqrt{g_{\sigma,p,k}}}
=
\frac{a_{\sigma,p,k}}
{|a_{\sigma,p,k}|\sqrt{g_{0,k}}}.
\]

Its magnitude is independent of the prime decay:

\[
\left|
\frac{a_{\sigma,p,k}}
{\sqrt{g_{\sigma,p,k}}}
\right|
=
g_{0,k}^{-1/2}.
\]

If infinitely many prime labels share a nonzero comparable base energy, then

\[
\sum_{p,k}
\frac{|a_{\sigma,p,k}|^2}
{g_{\sigma,p,k}}
=
\sum_{p,k}
\frac1{g_{0,k}}
\]

diverges.

Thus common scalar summation is not a bounded functional on the source-normalized Hilbert direct sum, even off seam.

## Category correction

The rank-one operator

\[
U_\sigma^{*}U_\sigma
\]

exists on an unweighted label Hilbert space because the raw Euler row is square-summable off seam. But that is not the completed source topology used by the Green incidence.

On the source-normalized Green domain, \(U_\sigma\) is an exterior observer in the rigged dual. It cannot be inserted as a bounded Birman–Schwinger loading.

This explains the artificial eigenvalue-one crossing found for the identity metric: it came from placing the observer in the wrong carrier.

## Revised hierarchy

The correct architecture is

\[
\text{weighted label Green space}
\longrightarrow
\text{faithful finite-port boundary packet}
\longrightarrow
\text{rigged exterior observer}
\longrightarrow
\text{scalar Riemann section}.
\]

The five Green margins concern the first two levels. The scalar zero is a vanishing pairing with an exterior observer, not automatically a kernel of

\[
G-U^{*}U.
\]

To recover a Birman–Schwinger formulation, the source would need an additional bounded control or Poisson operator that regularizes the exterior observer into the Green space. That operator must be constructed, not inferred from scalar convergence.

## Exterior pairing

Let

\[
\mathcal E
\subset
\mathcal H_G
\subset
\mathcal E'
\]

be the declared rigging. The scalar observer should be continuous as

\[
\Lambda_s:\mathcal E\to\mathbb C
\]

and extend as a distributional boundary section. Its zero set is meaningful without \(\Lambda_s\) belonging to \(\mathcal H_G'\).

The missing theorem is then a control identity transporting

\[
\Lambda_s(x)=0
\]

to a mixed boundary condition on the faithful packet. Positivity of interior energy alone cannot do this.

## Hostiles

Absorbing Euler weights into the source norm and then treating the same weighted row as a Hilbert vector cancels the decay label by label and produces an infinite-norm observer.

Switching to the unweighted label norm makes the observer bounded off seam but changes the source Green topology and creates the false eigenvalue crossing.

A finite cutoff hides both failures because every row is bounded in finite dimension.

## Frontier

The scalar augmentation must be removed from the bounded Green loading problem. The next constructor is exactly the previously identified exterior-observer boundary morphism or a source Poisson/control lift that represents it boundedly.

Until that lift exists, spectral identification through a rank-one Birman–Schwinger collision is unauthorized.
