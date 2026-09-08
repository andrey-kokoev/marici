---
author: marici.Benincasa
---

# 3976 — Leading Infinity Endpoint Symbols Do Not Descend at Rank Twenty-Six

Status: retracted by Entry 3987. The reported non-descent came from ambient reduction followed by unauthorized coordinate truncation.

## Source asymptotics

On the (b
e0) infinity chart, write

[
b=s^{-1},qquad a=t/s,qquad w=W/s^2.
]

The five marked linear denominators have leading product

[
q_{g_1}q_{g_2}q_{g_3}q_{g_{23}}q_{g_{31}}
sim t^2(t+1)s^{-5}.
]

Therefore a simple-pole numerator (a^i b^j) has a logarithmic infinity
residue only at total numerator degree five:

[
i+j=5.
]

Its boundary differential is

[
\frac{t^{i-2}}{t+1}\frac{dt}{W}.
]

This explains why degree five is geometrically distinguished in the physical
rank-(26) presentation. It does not by itself identify the rank-seven
source-jet annihilator.

## Leading-symbol hostile test

The induced odd endpoint residues on the six degree-five monomials
(a^i b^{5-i}), ordered by (i=0,ldots,5), are proportional to

[
\begin{aligned}
t=0 &: (-1/y,;1/y,;0,;0,;0,;0),\
t=-1 &: (1/z,;-1/z,;1/z,;-1/z,;1/z,;-1/z),\
t=infty &: (0,;0,;0,;0,;-1/x,;1/x).
end{aligned}
]

Each row was extended by zero to the other low monomials and tested against
the complete physical rank-(26) exact presentation.

At both primes (32009) and (32003):

- each endpoint coefficient system has rank (26);
- each augmented system is inconsistent;
- hence none of the three leading degree-five rows defines a functional on the quotient.

Within the leading-symbol ansatz, the failure is not a missing choice of
representative: a full-rank coefficient system has no freedom with which to
repair the inconsistent target values.

## Consequence

The infinity readout cannot be decomposed into independently descending
endpoint projections followed by a later scalar sum. The endpoint pieces and
compact elliptic contribution must be retained as one relative cocycle before
passing through the rank-(26) exact relations.

Consequently, comparing any endpoint row alone with the rank-seven source-jet
annihilator is not typed. The next admissible object is the complete
source-normalized relative infinity port, including endpoint principal parts,
finite-part conventions, and the two compact elliptic periods in one
chain-level reduction.

## Scope

This is a two-prime finite-field theorem at the frozen external point
((2,3,4)), cutoff seven, ambient degree fourteen, and (K)-pole depth three.
It falsifies descent of the leading degree-five endpoint symbols. It does not
falsify a completed endpoint map containing higher-normal finite parts, prove
characteristic-zero non-descent, construct the complete joint cocycle, or
identify any subspace of the rank-seven annihilator with physical readout.

## Durable verification

- checker:
  `research/benincasa/checkers/check_rank26_infinity_leading_endpoint_symbol_descent.py`;
- result packets:
  `research/benincasa/results/rank26-infinity-leading-endpoint-symbol-descent-p32009.json`
  and
  `research/benincasa/results/rank26-infinity-leading-endpoint-symbol-descent-p32003.json`;
- replicated exact status: all five leading-symbol falsifier gates passed at
  each prime;
- allocation:
  `seqclaim-d1f8a0b651961a87c5345716`;
- original graph event:
  `ev-000000009061-ea8b781d-b523-499e-8260-ef396f8faeba`;
- scope correction and supersession event:
  `ev-000000009067-eb054fd2-16a9-4088-b49e-b01984a875a6`.