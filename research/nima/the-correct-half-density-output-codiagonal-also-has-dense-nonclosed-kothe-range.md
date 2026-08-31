# The correct half-density output codiagonal also has dense nonclosed Köthe range

## Corrected low-grade coefficient

The plain Stokes ratio is not the Wronskian comparison.  On the strict
primitive-square packet, the correct half-density coefficient is

\[
\lambda_{p,\le2}^{(1/2)}
=
\frac{-\kappa_p^{(\le2)}}{2s_p^{(1/2)}}>0,
\]

where

\[
s_p^{(1/2)}
=2\sqrt2e^{1/(16\pi)}
\left(\sinh(\log p)-\sinh\frac{\log p}{2}\right).
\]

This packet tests the output-only diagonal map

\[
T_{1/2}e_p
=\lambda_{p,\le2}^{(1/2)}e_p
\]

on the declared prime Köthe source

\[
\mathcal A_{\exp}
=\bigcap_{\delta>0}\ell^1(\mathbb P,p^\delta).
\]

## Asymptotic separation

The denominator grows at most polynomially and is asymptotic to a positive
multiple of \(p\).  The numerator samples \(\Phi'\) at \(\log p\) and
\(2\log p\).  Completed theta decay gives, for every \(N>0\),

\[
|\kappa_p^{(\le2)}|=O(p^{-N}).
\]

Therefore

\[
\lambda_{p,\le2}^{(1/2)}=O(p^{-N})
\]

for every \(N>0\).  Every coefficient is positive, but the inverse grows
faster than every power of \(p\).

## Forward continuity and failure of inverse continuity

The sequence \((\lambda_{p,\le2}^{(1/2)})_p\) is bounded, so

\[
q_\delta(T_{1/2}x)
\le
\sup_p\lambda_{p,\le2}^{(1/2)}q_\delta(x).
\]

Thus \(T_{1/2}\) is continuous and injective.  It is not a Köthe
automorphism: a continuous inverse on its range would require a finite loss of
polynomial order, contradicting the superpolynomial growth of
\((\lambda_{p,\le2}^{(1/2)})^{-1}\).

## Explicit nonclosed-range witness

Let

\[
y_p=\lambda_{p,\le2}^{(1/2)}.
\]

Superpolynomial decay implies \(y\in\mathcal A_{\exp}\).  For every finite
prime cutoff \(P_X\),

\[
P_Xy=T_{1/2}(P_X\mathbf1)
\]

lies in the range and converges to \(y\) in every Köthe seminorm.  But the only
coordinatewise preimage of \(y\) is the constant sequence \(\mathbf1\), which
does not belong to \(\mathcal A_{\exp}\).  Hence

\[
\operatorname{ran}T_{1/2}
\]

is dense and nonclosed in the declared Köthe source.

## Connected tail does not repair the low-grade witness

Adding the nuclear \(k\ge3\) Wronskian return changes the output coefficient by
an even smaller theta-sampled term.  The full coefficient remains positive and
superpolynomially decaying.  The same cutoff witness applies to the full scalar
codiagonal.

More importantly, the connected return is a separate grade-labelled source
summand.  Summing it into one scalar output cannot restore the forgotten source
coordinate or reconstruct the individual grades.

## Constructor consequence

The corrected half-density comparison confirms the earlier structural
obstruction without relying on the invalid plain-Stokes identification:

- the retained graph has closed range because it keeps the source coordinate;
- the output-only scalar codiagonal has dense nonclosed range in the declared
  Köthe topology;
- a pullback range topology would change the source object;
- adding the nuclear connected tail does not restore closed range.

Therefore the output-only codiagonal cannot be the completed G1 constructor if
G1.2 requires closed range in the declared source topology.  The only currently
proved architecture satisfying the ledger's closure clauses is the retained
saturated graph.  No RH conclusion is authorized.
