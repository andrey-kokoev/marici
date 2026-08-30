# An Inverse Mellin Channel Is Still a Logarithmic-Origin Torsor

## The proposed orientation repair

The Mellin corona cannot orient a phase on its own. The smallest apparent
repair is a second source channel carrying the inverse character. A prime
amplitude of Mellin weight \(\log p\) would pair with a reference amplitude of
weight \(-\log p\), producing an invariant scalar.

Covariance determines the weight of the reference channel. It does not
determine the phase of the intertwiner joining the two one-dimensional weight
spaces.

## The surviving character freedom

Let \(z_n\) denote the relative phase assigned to a multiplicative label
\(n\). The natural coherence laws require

\[
z_{mn}=z_mz_n,
\qquad
z_1=1,
\qquad
z_{1/n}=z_n^{-1},
\qquad
z_n^* = z_n^{-1}.
\]

For every real \(a\), the family

\[
z_n^{(a)}=n^{ia}
\]

satisfies all four laws. Distinct values of \(a\) give distinct relative
phase frames.

Thus an inverse Mellin channel changes the problem from an unpaired character
to a torsor of pairings. Composition, unit, reciprocal reflection, and dagger
do not select its origin.

## Geometric meaning

The parameter \(a\) translates the logarithmic coordinate. Indeed,

\[
n^{-it}n^{ia}=n^{-i(t-a)}.
\]

Selecting \(a\) is selecting where the Mellin phase is declared to be zero.
It is a choice of logarithmic origin, not a consequence of representation
weight.

This explains why endpoint incidence is structurally relevant. A genuinely
source-derived endpoint at \(q=0\) may point the translation torsor. But the
claim must be proved by an incidence map that evaluates or transports the
reference channel at that endpoint. Merely mentioning the endpoint does not
fix \(a\).

## Exact no-go statement

The following data are insufficient to orient the inverse-channel pairing:

1. opposite Mellin weights;
2. multiplicative coherence;
3. preservation of the unit;
4. reciprocal reflection;
5. dagger compatibility;
6. positivity after pairing.

All remain invariant under the twist \(z_n\mapsto n^{ia}z_n\).

Write \(E_0\) for the endpoint-source carrier and \(F_{\mathrm{rel}}\) for the
relative Mellin-frame carrier. The missing constructor is a pointed incidence

\[
\iota_0:
\ E_0
\longrightarrow
\ F_{\mathrm{rel}}
\]

whose covariance law forces one value of \(a\). Without \(\iota_0\), a fitted
phase can be hidden as a harmless-looking translation.

## Finite falsifier

On a finite cyclic label model, every character parameter defines a distinct
phase frame while satisfying the same unit, product, inverse, and dagger
laws. Two different character parameters are therefore the minimum
falsifier for any claim that covariance alone uniquely selects the
intertwiner.

The next source audit should derive the endpoint incidence from the actual
theta tail or Tate boundary map and test whether it is invariant under any
nontrivial character twist. If one twist survives, the orientation remains
unpointed.
