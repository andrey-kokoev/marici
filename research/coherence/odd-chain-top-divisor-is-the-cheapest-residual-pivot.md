# The odd-chain top divisor is the cheapest residual pivot

## Maximal path matchings

Let an odd chain have \(2m+1\) vertices and prime-local gap costs

\[
c_i=v_p(x_i),
\qquad 0\le i<2m.
\]

A maximum matching has \(m\) edges and leaves one vertex unmatched. On a path with an odd number of vertices, the unmatched vertex must have even index

\[
2r,
\qquad 0\le r\le m.
\]

Once that pivot is chosen, the matching is forced:

- even-indexed edges strictly to its left;
- odd-indexed edges strictly to its right.

Its cost is

\[
C_r
=
\sum_{j=0}^{r-1}c_{2j}
+
\sum_{j=r}^{m-1}c_{2j+1}.
\]

## Closed top-divisor formula

The maximal Pfaffian-divisor valuation is therefore

\[
v_p(D_m)=\min_{0\le r\le m}C_r.
\]

Equivalently, the gcd of maximal Pfaffian cofactors is controlled by the cheapest even-position residual pivot.

Cofactors obtained by omitting odd-indexed vertices may contain path weights crossing the omitted point. Their valuations can be larger, but they are never needed to attain the gcd minimum.

## Efficient scan

The costs obey

\[
C_{r+1}-C_r=c_{2r}-c_{2r+1}.
\]

Hence every \(C_r\) can be computed in one linear scan from

\[
C_0=\sum_{j=0}^{m-1}c_{2j+1}.
\]

The top odd divisor requires \(O(n)\) operations per prime.

## Residual interpretation

Each even pivot corresponds to one orientation-compatible primitive residual presentation. The minimizing pivots are those with least prime divisibility. If several pivots tie, the integral residual has multiple equally primitive local presentations.

The primitive null vector is obtained by dividing all cofactors by \(D_m\). The formula identifies prime by prime where that normalization is witnessed combinatorially.

## Relation to reversal

Reversal sends pivot \(2r\) to \(2(m-r)\) and exchanges the two sums in \(C_r\). Therefore the multiset of pivot costs and their minimum are reversal invariant, while individual minimizing pivots are transported contravariantly.

## Verification

```text
python research/coherence/check_odd_chain_top_divisor_closed_form.py
```

The checker compares all cofactor valuations with the closed even-pivot formula for 280 odd chains through fifteen vertices.

Artifacts:

- `check_odd_chain_top_divisor_closed_form.py`
- `odd-chain-top-divisor-closed-form.v1.json`
