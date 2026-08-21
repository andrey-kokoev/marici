# 1541 — The Four-Branch Bulk Loop Reduces to the Ordered Source Triangle

## Hard-to-vary claim

With the Hermitian Wightman convention of Entry 1533, the complete rectangular
Schwinger--Keldysh sum over the four branch pairs reduces to twice the ordered
bulk--bulk triangle printed in the source.  The common perturbative factor
\(-1/2\) therefore reproduces the source's minus ordered integral.

## Frozen comparison

For branches \(a,b\in\{+,-\}\), the rectangular integrand is

\[
\sum_{a,b}ab\,
G_p^{+a}(\eta,t_1)G_p^{+b}(\eta,t_2)
G_q^{ab}(t_1,t_2)G_k^{ab}(t_1,t_2),
\]

including the two de Sitter measure factors.  The source triangle is

\[
[G_p^>(\eta,t_1)-G_p^<(\eta,t_1)]
\left[
G_p^>(\eta,t_2)G_q^>(t_1,t_2)G_k^>(t_1,t_2)
-
G_p^<(\eta,t_2)G_q^<(t_1,t_2)G_k^<(t_1,t_2)
\right]
\]

on \(t_0\le t_2\le t_1\le t\).

## Verification

The standalone Rust checker evaluates both forms independently on an
\(800\times800\) midpoint grid at generic unequal momenta.  The diagonal cells
of the ordered triangle receive their geometric half weight.  It finds

\[
\text{rectangular sum}=-23.23898625116762,
\]

\[
2\times\text{ordered triangle}=-23.23898625116324,
\]

with relative defect

\[
1.89\times10^{-13}.
\]

Artifacts:

- `research/benincasa/checkers/finite_time_sk_bulk_bulk.rs`
- `research/benincasa/results/finite-time-sk-bulk-bulk.json`

## Narrow conclusion

The contour labels, greater/lesser assignments, ordering signs, and factor of
two in the bulk--bulk sector are now fixed independently of Eq. (19).  This is
the first validated component of the omitted-grade contraction engine.

It does not yet include bulk--boundary, boundary--bulk,
boundary--boundary, or counterterm sectors.

## Next falsifier

Add the exponent-normalized integrated boundary vertex from Entry 1539 and
verify the mixed and boundary--boundary sectors against a direct expansion of
Eq. (17).  Only then extract the \(\eta_0\)-graded asymptotics.

