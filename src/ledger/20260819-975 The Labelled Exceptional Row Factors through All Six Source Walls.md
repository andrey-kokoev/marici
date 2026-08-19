# 975 — The Labelled Exceptional Row Factors through All Six Source Walls

## Rational assembly gate

Entry 974 provides the unique labelled support permutation

\[
p=(4,1,0,5,3,2).
\]

Let \(r_j\) be the exact dense exceptional-row component in column \(j\).
For occurrence \(i\), let \(f_i\) be its source wall equation, with repeated
factors retained as separate labelled occurrences:

\[
\begin{aligned}
f_0&=(ZA_2)^2-1,\\
f_1=f_2&=(ZA_2B_{24})^2-1,\\
f_3&=(A_3/Z)^2-1,\\
f_4=f_5&=(A_3B_{34}/Z)^2-1.
\end{aligned}
\]

The exact Symbolica reduction computes

\[
u_i=\frac{r_{p(i)}}{f_i}
\]

and verifies, without sampling,

\[
\boxed{r_{p(i)}=f_i u_i\qquad(0\leq i<6).}
\]

## Generic local-unit test

Each \(u_i\) was restricted independently to both roots of its assigned
wall. All twelve restrictions are nonzero rational functions. Moreover,
the two signed roots give the same restriction for every occurrence.

For example,

\[
u_0\big|_{Z=\pm A_2^{-1}}
=
\frac{4A_2(A_3^2-1)}
{A_3(A_2^2-1)},
\]

and

\[
u_4\big|_{Z=\pm A_3B_{34}}
=
-\frac{4A_3B_{34}(A_2^2-1)}
{A_2((A_3B_{34})^2-1)}.
\]

Thus each quotient is a unit at the generic point of its assigned wall,
after removing the already declared intersections with the other wall and
normalization divisors. It is not asserted to be a unit on the entire
compactified wall.

## Narrow conclusion

\[
\boxed{
\text{The labelled exceptional row factors componentwise through all six
source walls with generically invertible coefficients.}
}
\]

The rational rank-one exceptional comparison therefore has neither a
missing component nor an extra generic divisor. Together with Entry 974,
this upgrades support matching to exact local factorization.

This remains a statement about one exceptional row. It does not construct
the complete six-by-six rational transition or prove its horizontality.

## Next falsifier

Collect the six \(u_i\) into the diagonal matrix \(U\) and test whether

\[
P_{\rm lab}U
\]

extends from the exceptional row to an intertwiner of the complete source and
dense comparison matrices. The extension must satisfy all rows over the
common conserved kinematic ring; fitting uncomputed entries is prohibited.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_exceptional_row_factorization.rs;
- packet:
  research/benincasa/string-six-point-exceptional-row-factorization.json;
- verified command:
  cargo run --quiet --bin string_six_point_exceptional_row_factorization;
- allocator claim:
  seqclaim-fbadb8598a8c3dce94e4bdbb.
- epistemic event:
  ev-000000000592-2597ee49-1cbb-417c-a15f-de012f86ad1e.
