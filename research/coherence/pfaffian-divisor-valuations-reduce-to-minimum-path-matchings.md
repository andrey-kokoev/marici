# Pfaffian-divisor valuations reduce to minimum path matchings

## Reduction theorem

The tropical principal-Pfaffian formula initially minimizes over arbitrary ordered path pairs. When gap valuations are nonnegative, every selected interval can be shortened to one adjacent edge without increasing cost. Disjoint ordered intervals yield vertex-disjoint adjacent edges after shortening.

Conversely, every matching of \(k\) adjacent path edges is a valid \(2k\)-vertex principal subset.

Therefore

\[
v_p(D_k)
=
\min_{M\in\operatorname{Match}_k(P_{n-1})}
\sum_{i\in M}v_p(x_i),
\]

where \(\operatorname{Match}_k(P_{n-1})\) is the set of size-\(k\) matchings in the path of adjacent gaps.

## Dynamic recurrence

Let \(F(i,k)\) be the minimum cost of a size-\(k\) matching using gap edges at or after \(i\). Then

\[
F(i,k)
=
\min\bigl(
F(i+1,k),
\ c_i+F(i+2,k-1)
\bigr).
\]

The first branch skips edge \(i\); the second selects it and skips its adjacent edge.

This computes each prime-local divisor spectrum in \(O(nk)\) operations.

## Terminal cases

For \(n=2m\), a size-\(m\) path matching is forced:

\[
M=\{0,2,\ldots,2m-2\}.
\]

Hence

\[
v_p(D_m)
=
\sum_{r=0}^{m-1}v_p(x_{2r}),
\]

recovering the adjacent full Pfaffian.

For odd \(n=2m+1\), size-\(m\) matchings leave one vertex unmatched. Their minimum cost gives the gcd valuation of maximal Pfaffian cofactors and therefore the divisibility scale of the odd residual.

## Structural consequence

Integral rank reset has a purely local combinatorial algorithm:

```text
gap prime valuations
-> weighted path
-> minimum k-matchings
-> Pfaffian divisors D_k
-> alternating Smith factors d_k
```

The integral torsion module can be computed primewise without assembling the dense skew matrix.

## Verification

```text
python research/coherence/check_pfaffian_divisor_path_matching_reduction.py
```

The checker compares arbitrary-interval principal-subset optimization with adjacent-edge matching for 300 chains through thirteen vertices.

Artifacts:

- `check_pfaffian_divisor_path_matching_reduction.py`
- `pfaffian-divisor-path-matching-reduction.v1.json`
