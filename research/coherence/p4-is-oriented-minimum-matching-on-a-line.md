# P4 is the oriented minimum perfect matching of four boundary lengths

## General chamber law

Let \(a_0,a_1,a_2,a_3\) be four distinct positive shift lengths, and write their order statistics as

\[
a_{(0)}<a_{(1)}<a_{(2)}<a_{(3)}.
\]

Exhaustive exact-rational tests support the law

\[
\rho_0(\mathcal Q_4)
=
\operatorname{or}(a_0,a_1,a_2,a_3)\,
\operatorname{ev}_{L_4},
\]

where

\[
L_4=(a_{(1)}-a_{(0)})+(a_{(3)}-a_{(2)})
\]

and \(\operatorname{or}\) is the sign of the permutation carrying the supplied frame to increasing order.

The checker tested 22 distinct rational length sets and all 24 permutations of each, for 528 frames. Every raw endpoint expression reduced to exactly one term and every frame obeyed the displayed law.

This is computational evidence for the general chamber theorem; a symbolic inequality proof remains separate.

## Minimum-matching interpretation

There are three perfect matchings of four points:

\[
(01)(23),\qquad(02)(13),\qquad(03)(12).
\]

For four ordered points on a line, pairing adjacent points uniquely minimizes total distance:

\[
L_4
=
\min_{M}
\sum_{\{i,j\}\in M}|a_i-a_j|.
\]

Indeed the other costs exceed it by twice one of the positive interior gaps. Therefore the endpoint four-cup computes the oriented minimum perfect-matching length.

The half-line support conditions perform the chamber selection; the alternating cup provides orientation. No external sorting or matching operator was inserted.

## Relation to the prime frame

For \(a_p=\log p\),

\[
L_4
=
\log\frac{p_{(1)}}{p_{(0)}}
+
\log\frac{p_{(3)}}{p_{(2)}}
=
\log\frac{p_{(1)}p_{(3)}}{p_{(0)}p_{(2)}}.
\]

For \((2,3,5,7)\), this gives

\[
L_4=\log\frac{21}{10}.
\]

Thus the multiplicative ratio is the exponential of an additive optimal-matching cost in logarithmic valuation geometry.

## Higher-level consequence

The four-cell does more than compare two arbitrary observers. It selects a compatible decomposition of four primitive boundary positions into two nearest-neighbor observer pairs:

\[
\boxed{
P^4
=
\text{orientation}
\otimes
\text{minimum pairing of four boundary positions}.
}
\]

This is an atemporal optimization law. “Computation” here means that support, incidence, and antisymmetry jointly determine the surviving matching. There is no algorithmic sequence or external chooser.

The pattern points toward a higher even-rank conjecture. For \(2m\) ordered boundary lengths, a Pfaffian cup of the two-cochain may select the adjacent perfect matching

\[
(a_{(0)},a_{(1)}),\ldots,(a_{(2m-2)},a_{(2m-1)}),
\]

whose cost is

\[
L_{2m}=\sum_{j=0}^{m-1}(a_{(2j+1)}-a_{(2j)}).
\]

The next discriminator is rank six: construct the Pfaffian three-cup and test whether its endpoint readout is the oriented evaluation at \(L_6\), or whether new cyclic interference appears.

## Verification

Run:

```text
python research/coherence/check_p4_arbitrary_length_chambers.py
```

Artifacts:

- `check_p4_arbitrary_length_chambers.py`
- `p4-arbitrary-length-chambers.v1.json`
