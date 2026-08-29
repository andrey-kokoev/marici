# A two-port seed avoids unauthorized wall-tail scalar mixing

## Correction

The previous cyclic-seed reduction chose a scalar sum

\[
\ell_{\mathrm{wall}}+\ell_{\mathrm{tail}}.
\]

That is sufficient when a source-authorized common scalar evaluator exists, but it is stronger than necessary. The representation-valued exterior observer should retain the two incidences as separate ports before any scalar mixing.

## Pair-valued seed

Define

\[
J:W\longrightarrow \mathbb C^2,
\qquad
J(w)=
\bigl(
\ell_{\mathrm{wall}}(w),
\ell_{\mathrm{tail}}(w)
\bigr).
\]

Its Fourier orbit packet is

\[
\mathcal O_J(w)
=
\bigl(
J(w),J(Fw),J(F^2w),J(F^3w)
\bigr).
\]

Because \(W_{\mathrm{wall}}\) and \(W_{\mathrm{tail}}\) are invariant and the two components are typed separately, faithfulness reduces blockwise:

\[
\mathcal O_J\ \text{injective}
\]

if and only if the wall orbit separates \(\operatorname{span}\{1,\delta_0\}\) and the tail orbit separates \(\operatorname{span}\{K,V\}\).

For wall coordinates \((a,b)\), separation requires

\[
a+b\ne0,
\qquad
a-b\ne0.
\]

For a real tail coordinate \((c,d)\), separation requires

\[
c^2+d^2>0.
\]

No wall-tail cancellation is possible in this packet because the outputs have different types.

## Quantitative bound

Let \(\delta_{\mathrm{wall}}\) be the lower frame bound of the wall orbit and \(\delta_{\mathrm{tail}}\) the lower frame bound of the tail orbit. With the direct-sum target norm,

\[
\sigma_{\min}(\mathcal O_J)
=
\min\{
\delta_{\mathrm{wall}},
\delta_{\mathrm{tail}}
\}
\]

up to the frozen normalization of the Fourier orbit.

Thus completion requires two independent bounds, not a mixed scalar-angle bound:

\[
\inf\delta_{\mathrm{wall}}>0,
\qquad
\inf\delta_{\mathrm{tail}}>0.
\]

The mixed-cancellation margin enters only downstream, when a scalar matrix coefficient combines the two ports.

## Categorical advantage

The five-cell already authorizes a direct-sum boundary packet more naturally than it authorizes addition into one scalar. The pair-valued seed therefore respects the packet-first hierarchy:

\[
\text{wall incidence}\oplus\text{tail incidence}
\longrightarrow
\text{Fourier orbit packet}
\longrightarrow
\text{faithful boundary observer}
\longrightarrow
\text{source scalar matrix coefficient}.
\]

This removes the need to find a common terminal evaluator at the observer-construction stage. What remains is only a common target object carrying the typed direct sum and Fourier transport.

## Source gates

The finite theorem now asks for:

1. one-sided wall incidence with both wall characters nonzero;
2. causal or Wronskian tail incidence with nonzero odd magnitude;
3. a typed direct-sum constructor;
4. Fourier–Tate action on that direct sum;
5. the same block decomposition for polarized Green currents;
6. uniform lower frame bounds at completion.

Only after these pass should the Riemann scalar readout be introduced. Its map

\[
r_s:\mathbb C^8\to\mathbb C
\]

must then be audited against the global mixed-cancellation margin.

## Hostiles

A scalar sum may vanish through wall-tail cancellation even when both source ports are healthy. The pair packet remains faithful and exposes the cancellation as a downstream readout defect.

A direct-sum packet with a reciprocal-symmetrized wall row still loses one wall character. Keeping ports separate does not repair a dark component within either invariant plane.

## Frontier

The earliest missing constructor is weakened and clarified:

> Construct the typed direct sum of the one-sided wall observer and the oriented causal-tail observer, then prove their separate Fourier-orbit frame bounds.

A common scalar evaluator is not needed until the final Riemann matrix coefficient.
