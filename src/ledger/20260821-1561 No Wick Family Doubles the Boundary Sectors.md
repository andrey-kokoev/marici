# 1561 — No Wick Family Doubles the Boundary Sectors

## Hard-to-vary claim

The complete labelled Wick census for two external fields and two
\(\zeta(\partial\zeta)^2\) vertices contains exactly

\[
\boxed{36}
\]

connected fish contractions at generic nonzero external momentum. The count
is identical for bulk--bulk, bulk--surface, and surface--surface placement.

There is no omitted connected contraction family that selectively doubles
the boundary-containing sectors of Eq. (19).

## Complete census

There are \(8\) labelled fields: two external fields and three slots at each
cubic vertex. Their \(105\) perfect pairings split as

\[
\begin{array}{c|c}
\text{class}&\text{count}\\
\hline
\text{connected fish}&36\\
\text{zero-momentum tadpole topology}&36\\
\text{disconnected}&18\\
\text{external pair}&15
\end{array}
\]

The tadpole topology forces the line connecting the vertices to carry zero
momentum when the two external momenta are \(p,-p\). It is not a second
generic fish contribution and cannot produce the printed \(J_0,J_2\)
structures.

For the fish class, summing the three choices of undifferentiated slot and
the exchange of the differentiated slots gives the same vertex factor at
every location:

\[
2(p\!\cdot q+p\!\cdot k+q\!\cdot k)
=-(p^2+q^2+k^2).
\]

Two vertices therefore give the source's
\((p^2+q^2+k^2)^2\).

## Artifacts

- `research/benincasa/checkers/labelled_cubic_wick_census.rs`
- `research/benincasa/results/labelled-cubic-wick-census.json`

## Narrow conclusion

The conventional repair space is exhausted:

- Eq. (17) and Eq. (18) have identical expansion coefficients (Entry 1560);
- a separated endpoint regulator is multiplicative (Entry 1559);
- a scalar endpoint weight cannot match both sectors (Entry 1558);
- bulk counterterms cannot supply the zero-mode discrepancy (Entry 1557);
- and no missing Wick family doubles the boundary sectors (this entry).

Within the frozen one-operator toy model and the printed formulas, the factor
two multiplying both boundary-containing contributions in Eq. (19) is not
derived. The narrow surviving diagnosis is

\[
\boxed{
\text{Eq. (19) has an unsupported boundary-sector normalization.}
}
\]

This is a primary-source normalization defect, not evidence for a new
cosmological carrier or coefficient object.

## Next falsifier

Independently reproduce the three sector coefficients from the published
three-point boundary kernel by sewing two source-normalized three-point
vertices. If sewing yields the direct-exponent coefficients again, mark the
Eq. (19) boundary factor as a probable typo and continue the omitted
\(\eta_0^1,\eta_0^0\) reconstruction using the corrected normalization. If
sewing produces the extra factor two, its occurrence-level provenance will
identify the missing comparison map.
