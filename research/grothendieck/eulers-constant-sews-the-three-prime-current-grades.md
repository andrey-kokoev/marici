# Euler's constant sews the three prime-current grades

## Exact decomposition

Let `B_1` be the Meissel--Mertens prime constant:

\[
B_1
=
\lim_{X\to\infty}
\left(
\sum_{p\le X}\frac1p-log\log X
\right).
\]

Expanding each finite Euler logarithm gives

\[
\sum_{p\le X}-\log(1-p^{-1})
=
\sum_{p\le X}\frac1p
+
\frac12\sum_{p\le X}\frac1{p^2}
+
\sum_{p\le X}\sum_{k\ge3}\frac1{k p^k}.
\]

The last two terms converge absolutely. Comparing with Mertens' product
theorem yields

\[
\gamma
=
B_1
+
\frac12\sum_p\frac1{p^2}
+
\sum_p\sum_{k\ge3}\frac1{k p^k}.
\]

## Typed interpretation

The three summands are exactly the previously derived current filtration:

| Grade | Scalar finite contribution | Analytic type |
|---|---:|---|
| `k=1` | `B_1` | primitive logarithmic current |
| `k=2` | one half of the prime-zeta value at `2` | square, Hilbert-level current |
| `k>=3` | the remaining absolutely convergent double sum | trace-class connected tail |

Euler's constant is therefore not an unrelated endpoint number appended to
the Euler product. At the scalar Mertens readout, it is the exact sewing
constant of all three prime-current grades.

## Consequence for relative determinants

A third-order relative determinant naturally retains the `k>=3` tail while
placing its first two logarithmic traces outside the ordinary determinant.
The identity above fixes what those two boundary traces must reconstruct at
the Cauchy/Mertens anchor.

Any proposed operator packet `K_X` must satisfy the scalar audit

\[
\operatorname{Tr}K_X
-
\frac12\operatorname{Tr}(K_X^2)
+
\log\det_3(1+K_X)
\longrightarrow
\gamma
\]

after applying the declared sign convention and source evaluation. The
formula is an acceptance shape, not an asserted construction of `K_X`.
The primitive trace must reproduce `B_1`, the square trace must reproduce the
prime-square constant, and the relative determinant must reproduce the
connected tail without cross-grade leakage.

## Hostile deletion test

Deleting the primitive channel changes both cutoff covariance and the finite
constant. Deleting the square channel leaves an explicit positive deficit

\[
\frac12\sum_p p^{-2}.
\]

Deleting only the connected tail leaves another explicit positive deficit.
No deleted grade can be recovered by renaming the remaining scalar
counterterm without destroying source provenance.

## What remains RH-bearing

This closes the scalar normalization of the finite Euler side. It does not
show that theta--Tate completion preserves the three-grade packet. The BSY
anomaly remains the failure of that full typed packet to descend to the same
critical-boundary finite part.

The next non-scalar gate is therefore the one Nima isolated earlier: derive a
source operator whose first trace, second trace, and third-order determinant
realize these three terms before compression.

## Scope

This packet proves an exact classical constant decomposition and identifies
its role in the current filtration. It does not construct the required
operator, prove completion compatibility, or prove RH.
