# 1442 — Only the Positive Deck Sheet Has an Ordinary Exceptional Period

## Question

Entry 1440 proves that the coefficient and Betti lattices transform with
opposite valuation shifts under all 32 five-site deck changes. That strict
pairing theorem does not determine whether every continued chamber also
defines an ordinary scalar integral on the frozen positive radial ray
\(\rho\in[0,\infty)\).

## Complete-source audit

For sheet \(S\subseteq\{1,\ldots,5\}\), every source denominator has the
exact coalesced form

\[
q_I^{(S)}(\rho)
=
|I|+\rho\sum_{e\in\partial I}(-1)^{\mathbf 1_{e\in S}}.
\]

The checker assembled all 180 source terms, included the fixed
\(G,g_1,\ldots,g_5\) prefactor, combined the complete rational function, and
cancelled numerator and denominator over \(\mathbb Q(\rho)\) before locating
poles.

Exactly one sheet is regular on the positive ray:

\[
\boxed{
\{S:\text{the complete integrand has no pole on }(0,\infty)\}
=
\{\varnothing\}.
}
\]

Every nontrivial sheet change leaves at least one uncancelled pole. The full
positive pole set is

\[
\boxed{
\rho\in
\left\{\frac12,1,\frac32,2\right\},
}
\]

with pole orders ranging from one through six.

## Consequence

The strict fractional-lattice groupoid is not a family of 32 ordinary
positive-ray periods. It transports the typed coefficient--Betti pairing, but
the scalar evaluation additionally requires a contour:

\[
\boxed{
\text{deck transport of the pairing}
\not\Rightarrow
\text{deck transport of the frozen positive integral}.
}
\]

Thus the source-positive chamber is singled out operationally, not merely by
the order-nine associated grade. Assigning a scalar period to any of the other
31 sheets requires an independently specified contour deformation or
\(i\epsilon\) prescription around the crossed poles.

## Scope

This is an exact characteristic-zero theorem about the complete coalesced
five-site source integrand and the literal positive radial ray. It does not
choose continuations around the poles, compute their discontinuities, or claim
that no physically authorized complex contour exists.

## Durable verification

- Checker: research/nima/check_five_site_deck_continued_period_poles.py
- Result: research/nima/results/five-site-deck-continued-period-poles.json
- Input: research/benincasa/results/five-cycle-ofpt-packet.json
- Result SHA-256:
  0838e3c195195db1c74bba4d0686d3fd6ab895fdd2825731ff2b554b91ed864f
- Sequence claim: seqclaim-ed22b102710dd4de36d25560
- Epistemic graph event:
  ev-000000001522-2fd130e5-4b5a-46b3-8bb0-27e69688c746
