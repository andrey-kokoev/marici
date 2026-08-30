# The cyclic observer seed must mix the wall and oriented-tail planes

## Two invariant planes

The four-dimensional boundary quotient splits over the real source frame as

\[
W=W_{\mathrm{wall}}\oplus W_{\mathrm{tail}},
\]

where

\[
W_{\mathrm{wall}}=\operatorname{span}\{1,\delta_0\},
\qquad
W_{\mathrm{tail}}=\operatorname{span}\{K,V\}.
\]

Fourier preserves both planes. On the first it exchanges \(1\) and \(\delta_0\); on the second it performs the quarter-turn \(K\mapsto V\mapsto-K\).

Consequently, no covector supported on only one source plane can be cyclic on all of \(W\). Its complete Fourier orbit remains trapped in a two-dimensional invariant subspace.

## Coordinate criterion

Write a real boundary covector as

\[
\ell=(a,b,c,d)
\]

in the dual frame to \((1,\delta_0,K,V)\). Its four character components are proportional to

\[
a+b,\qquad
a-b,\qquad
c+id,\qquad
c-id.
\]

Therefore the Fourier orbit of \(\ell\) is faithful exactly when

\[
a+b\ne0,
\qquad
a-b\ne0,
\qquad
(c,d)\ne(0,0).
\]

For a real covector, nonvanishing of one odd complex character automatically gives nonvanishing of its conjugate. The four-port cyclicity gate therefore reduces to three real conditions:

- the wall seed is neither symmetric nor antisymmetric;
- the oriented-tail seed is nonzero.

## Minimal source candidate

Let \(\ell_{\mathrm{wall}}\) be an authorized one-sided wall incidence and let \(\ell_{\mathrm{tail}}\) be the causal-history or Wronskian incidence on the oriented tail plane. Then

\[
\ell_{\mathrm{seed}}
=
\ell_{\mathrm{wall}}+\ell_{\mathrm{tail}}
\]

is the minimal algebraic cyclic candidate.

In the normalized model

\[
\ell_{\mathrm{wall}}=(1,0,0,0),
\qquad
\ell_{\mathrm{tail}}=(0,0,1,0),
\]

the seed is

\[
\ell_{\mathrm{seed}}=(1,0,1,0),
\]

whose character coordinates are all nonzero. Its Fourier orbit separates the full boundary quotient.

## Authority and cancellation gate

The sum is not authorized merely because the five-cell contains both summands. The source must supply a common terminal evaluator or a typed direct-sum comparison cell. Otherwise the candidate is a fitted mixture.

Even with an authorized sum, its completed frame bound depends separately on

\[
|a+b|,
\qquad
|a-b|,
\qquad
\sqrt{c^2+d^2}.
\]

This exposes two distinct failures:

- wall tangency, when \(a\to\pm b\);
- tail darkness, when \(c,d\to0\).

There is no cross-cancellation between these character planes after the full orbit packet is retained. Cross-cancellation reappears only after applying the final scalar matrix coefficient.

## Source theorem required

The next executable theorem is:

1. derive the one-sided wall incidence before reciprocal symmetrization;
2. derive the oriented-tail incidence from causal history;
3. prove both land in one declared observer target;
4. prove their sum is the image of an authorized assembly arrow;
5. establish uniform lower bounds for the two wall combinations and the tail magnitude;
6. transport the same decomposition to the polarized Green-current packet.

The smallest hostile uses a reciprocal-symmetrized wall observer with \(a=b\). It is perfectly nonzero but loses the \(-1\) character. Another uses a valid wall seed and a scalarized tail whose orientation magnitude tends to zero.

## Frontier

The abstract cyclicity problem has reduced to a mixed-incidence construction:

> Join one one-sided wall incidence and one oriented causal-tail incidence at a common typed evaluator without symmetrizing either away.

This is the finite source cell that can generate the complete exterior observer by Fourier transport.
