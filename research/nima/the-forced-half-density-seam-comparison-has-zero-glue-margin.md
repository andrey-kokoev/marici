# The forced half-density seam comparison has zero glue margin

## Seam comparison

On the strict primitive-square prime fibres, the source traces force the
half-density Stokes-to-Wronskian coefficient

\[
\lambda_p
=
\lambda_{p,\le2}^{(1/2)}
=
\frac{-\kappa_p^{(\le2)}}{2s_p^{(1/2)}}>0.
\]

Consider the diagonal seam comparison

\[
Te_p=\lambda_pe_p.
\]

The coefficients tend to zero faster than every inverse power of \(p\).

## Hilbert margin

On the unweighted prime Hilbert carrier,

\[
\inf_{\|x\|=1}\|Tx\|
\le\|Te_p\|
=\lambda_p
\longrightarrow0.
\]

Therefore the minimum modulus is zero:

\[
m(T)=0.
\]

Equivalently, the range is not closed and the Moore--Penrose inverse is
unbounded on the range closure.  No positive singular-value or Friedrichs-angle
margin can be extracted from this diagonal comparison.

## Köthe margin

On the declared projective exponential Köthe source, \(T\) is continuous and
injective but has dense nonclosed range.  The explicit witness is

\[
y=(\lambda_p)_p.
\]

Every finite cutoff \(P_Xy\) lies in the range and converges to \(y\) in every
Köthe seminorm, while the only coordinatewise preimage of \(y\) is the constant
sequence, which is not in the source.

Thus changing from the Hilbert realization to the declared source topology
does not create a completed inverse or a positive glue margin.

## Connected grades

The connected return adds

\[
\kappa_p^{(\ge3)}j_p
\]

inside the same prime fibre.  Its coefficient is theta-sampled and decays at
least as fast as the low-grade term.  The full scalar coefficient still tends
to zero superpolynomially.  Hence adding the nuclear connected tail does not
repair the singular sequence \((e_p)_p\).

## Difference-map formulation

Suppose the seam pullback is represented after normalization by

\[
D(x_P,x_A)=Tx_P-x_A.
\]

The graph of \(T\) is closed only when the source coordinate is retained in the
domain topology.  After measuring mismatch in the output seam norm, the
correction from \(x_A=Te_p\) back to \(x_P=e_p\) has norm ratio

\[
\frac{\|e_p\|}{\|Te_p\|}
=\lambda_p^{-1}\to\infty.
\]

Therefore the uniform inf-sup constant for output correction is zero.
Adjoining an identity provenance coordinate would bound this ratio, but that
would test constructor faithfulness rather than output seam transversality.

## G3 consequence

For the forced scalar half-density seam comparison,

\[
\delta_{\rm glue}=0.
\]

This is a negative theorem, not an unresolved estimate.  Consequently the
current output-only seam cannot satisfy G3.

A valid repair requires an independently source-authorized noncompact seam
observer, a larger jointly faithful output family, or a revised G3 seam object
whose topology is physically and arithmetically justified.  Merely using the
retained source identity, changing to the pullback range norm, or adding the
nuclear connected tail does not prove the required output margin.

G3 therefore remains blocked even though \(\delta_P\) and the doubled-history
\(\delta_A\) are positive.  No RH conclusion is authorized.
