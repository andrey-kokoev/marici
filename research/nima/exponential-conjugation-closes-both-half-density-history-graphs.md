# Exponential conjugation closes both half-density history graphs

## Untwisted relative graph

Let \(\mathcal H_{\mathrm{rel}}\) be the weighted relative Sobolev history space for the ordinary Volterra primitive, with continuous endpoint traces.

Define multiplication conjugators

\[
(U_-f)(u)=e^{-u/2}f(u),
\qquad
(U_+f)(u)=e^{u/2}f(u).
\]

## Twisted output spaces

Define

\[
\mathcal H_-
=
U_-^{-1}\mathcal H_{\mathrm{rel}},
\qquad
\|f\|_{\mathcal H_-}
=
\|U_-f\|_{\mathrm{rel}},
\]

and

\[
\mathcal H_+
=
U_+^{-1}\mathcal H_{\mathrm{rel}},
\qquad
\|f\|_{\mathcal H_+}
=
\|U_+f\|_{\mathrm{rel}}.
\]

These are complete because they are pullbacks of a complete graph space by invertible multiplication maps.

Their renormalized traces are ordinary endpoint traces after conjugation:

\[
\operatorname{Tr}^{-}_{\pm}f
=
\operatorname{Tr}_{\pm}(U_-f),
\]

\[
\operatorname{Tr}^{+}_{\pm}f
=
\operatorname{Tr}_{\pm}(U_+f).
\]

## Twisted input spaces and closed histories

Define source spaces

\[
\mathcal E_-
=
\{g:U_-g\in\mathcal E_w\},
\qquad
\mathcal E_+
=
\{g:U_+g\in\mathcal E_w\}.
\]

The twisted histories factor exactly as

\[
H_-
=
U_-^{-1}H_0U_-,
\]

and

\[
H_+
=
U_+^{-1}H_0U_+,
\]

where \(H_0\) is ordinary causal Volterra history. Therefore

\[
H_-:\mathcal E_-\to\mathcal H_-,
\qquad
H_+:\mathcal E_+\to\mathcal H_+
\]

are continuous closed graph maps with the same norm as \(H_0\).

Their outgoing traces are

\[
\operatorname{Tr}^{-}_{+}H_-g
=
\int e^{-u/2}g(u)\,du,
\]

and

\[
\operatorname{Tr}^{+}_{+}H_+g
=
\int e^{u/2}g(u)\,du.
\]

Thus closure preserves the exact Wronskian normalization.

## Reciprocal reflection

Reflection satisfies

\[
RU_-=U_+R.
\]

Consequently it gives an isometric exchange

\[
R:\mathcal H_-\longrightarrow\mathcal H_+,
\]

after reflecting the polynomial weight, and similarly exchanges \(\mathcal E_-\) and \(\mathcal E_+\). Causal orientation changes to the corresponding anti-causal orientation, supplying the expected reciprocal sign.

## Labelled assembly

At label \((p,k)\), translate both the polynomial weight and the exponential conjugator by \(L_{p,k}=k\log p\). The resulting history pair is an isometric copy of the seam pair before multiplication by the Euler coefficient.

Taking the valuation-labelled direct sum preserves:

- closedness;
- prime diagonality;
- reciprocal exchange;
- the exact endpoint columns \((1/2,1/2)\) and \((1/4,-1/4)\);
- cutoff naturality.

Euler coefficients affect source amplitudes but not the normalized two-channel frame.

## Consequence

The analytic closure defect introduced by the correction is resolved by conjugation. The first Adams edge now has a closed, prime-labelled, reciprocal two-history carrier with exact Wronskian traces.

The next unresolved gate returns to the auxiliary energy: derive a positive even form on \(\mathcal H_-\oplus\mathcal H_+\) and prove the causal odd coupling is relatively contractive before Schur elimination.
