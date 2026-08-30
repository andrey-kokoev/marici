# The transverse magnetic response has a hypergeometric character

Companion to `checkers/magnetic_transverse_recurrence_checks.py` (7/7, exit
0) and `results/magnetic_transverse_recurrence.json`.

Let (	au_g) be the lower-right entry of the endpoint Schur block for the
row-(3) alternate chart at

\[
q=2g+8,qquad k=g/2+4.
\]

Exact values through even grade (40) determine the low-degree factored
ratio

\[
\boxed{
\frac{\tau_g}{\tau_{g-2}}
=
\frac{
4g(g+3)(g+4)(2g+1)(2g+3)(g^2-g-26)
}{
(g-2)(g+6)(g+7)(g^2-5g-20)
}.
}
\]

The checker then computes grades (42,44,46) independently.  All three
held-out ratios agree exactly.  The base value is

\[
\tau_2=\frac{320}{3}.
\]

The two exceptional quadratic factors have the same discriminant,

\[
\operatorname{disc}(g^2-g-26)
=\operatorname{disc}(g^2-5g-20)=105.
\]

Since (105) is not a square, neither quadratic vanishes at an integral
grade.  Every remaining factor is plainly nonzero for even (g\ge4).
Therefore, conditional only on the recurrence identity,

\[
\boxed{\tau_g\ne0\quad\text{for every even }g\ge2.}
\]

The sign law is also explained.  The multiplier is positive at (g=4),
negative at (g=6), and positive for every even (g\ge8).  Hence
(	au_2,	au_4>0) and (	au_g<0) thereafter.

This is stronger than an empirical nonzero census: it isolates a rational
transport character whose arithmetic divisor misses the admissible integral
lattice.

## Scope

The ratio is verified exactly at nineteen discovery grades and three held-out
grades through (g=46).  Its factorization gives a rigorous all-grade
nonvanishing consequence if the recurrence holds.  A symbolic derivation of
the recurrence from consecutive Schur eliminations remains required before
calling the all-grade transverse theorem proved.
