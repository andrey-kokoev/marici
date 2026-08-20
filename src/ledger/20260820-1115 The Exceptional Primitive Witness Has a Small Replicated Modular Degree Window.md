# 1115 — The Exceptional Primitive Witness Has a Small Replicated Modular Degree Window

## Question

Entry 1114 left one coefficient-level gap at the exceptional center

\[
(u,v)=(0,2):
\]

the glued rank-four quotient connection is known modularly, but its common
source primitive has no characteristic-zero certificate.

The present test asks a narrower computational question.  Does a bounded
univariate polynomial-module ansatz already contain a primitive witness in
each weighted chart?

## Frozen module gate

For one quotient generator, write the 124 coefficient identities as

\[
M(s)N(s)=D(s)r(s)
\]

in the \(p\)-chart, and analogously in \(r=p/q\) in the \(q\)-chart.  All
372 primitive coefficients share the numerator bound; the target shares one
denominator.  No primitive section is selected.

The test used the 27 chart-coordinate values \(2,\ldots,28\) and two
independent large primes.

## Replicated threshold

For the pilot quotient generator the first tested feasible windows are

\[
\boxed{
\begin{array}{c|c|c}
\text{chart}&(\deg N,\deg D)&\dim\ker_D\\
\hline
p\ne0, s=q/p&(6,4)&1\\
q\ne0, r=p/q&(6,5)&1
\end{array}}
\]

Both rows reproduce at

\[
2305843009213693951,qquad2305843009213693921.
\]

The adjacent failures are informative:

\[
(5,6),(6,3)\quad\text{fail in the }p\text{-chart},
\]

and

\[
(6,4)\quad\text{fails in the }q\text{-chart}.
\]

Thus numerator degree six is forced in the tested \(p\)-chart window, while
the inversion chart requires one additional denominator degree.

At the first prime, the other three quotient-basis generators also lie in the
\((6,4)\) \(p\)-chart gate.  Their denominator-kernel excesses are respectively
\(1,2,5\); this is feasibility data, not uniqueness.

## Narrow conclusion

\[
\boxed{
\text{The missing exceptional primitive is computationally bounded at small
univariate degree in both charts.}
}
\]

This removes the earlier concern that characteristic-zero descent necessarily
requires an unbounded rational search.  It does not itself perform descent.

## Prohibited inference

Finite-field module membership, even at two primes and unused sample points,
does not prove a characteristic-zero identity.  In particular this entry does
not establish:

- exact primitive coefficients over \(\mathbb Q\);
- one common normalization for all four quotient generators;
- exact compatibility of those primitives on the chart overlap;
- a rational height bound.

## Evidence

Packet:

`research/benincasa/rank12-u0-v2-exceptional-module-degree-gate.json`.

Checker mode:

`MARICI_EXCEPTIONAL_MODULE_MODE` in
`research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`.

Ledger claim: `seqclaim-95487e912b37cc566ba83710`.

Epistemic event:

`ev-000000000814-615cd7be-09bf-428d-92d3-83451ab427cf`.

## Next falsifier

Reconstruct one complete pilot primitive at the certified chartwise bounds,
lift its coefficients to \(\mathbb Q\), and verify every cleared polynomial
identity exactly.  Only after that pilot passes should the remaining quotient
generators be reconstructed and the exact overlap cocycle tested.
