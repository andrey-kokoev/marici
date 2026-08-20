# 1091 — The First Joint-Rees Chart Has Only Perfect-Square Marked Restrictions

## Record

Entry 1090 derived the joint Rees ideal

\[
J=(p,q,A,B)
\]

at the rank-twelve exceptional center ((u,v)=(0,2)).  The first affine
chart of this blowup has (p\neq0) and coordinate

\[
s=\frac qp.
\]

Sequence claim: `seqclaim-5c85ee85b9200a552edf4204`.

## Exceptional family and retained walls

Let

\[
K_E(s,A,B)=\operatorname{in}_J(K)(1,s,A,B).
\]

The two labelled marked walls retain the equations

\[
L_{1,E}=B-1,
\qquad
L_{2,E}=A+\frac{s-1}{2}.
\]

No wall is reconstructed from a factorization; both are strict transforms of
the frozen source denominators.

## Exact restriction identities

Exact symbolic reduction gives

\[
\boxed{
K_E|_{L_{1,E}=0}
=
\frac1{16}
\left(1+6s+s^2-4A^2\right)^2,
}
\]

and

\[
\boxed{
K_E|_{L_{2,E}=0}
=
\left(-1+B+Bs+s\right)^2.
}
\]

At the labelled top intersection,

\[
\boxed{
K_E|_{L_{1,E}=L_{2,E}=0}=4s^2.
}
\]

Thus both single-wall restrictions and the same-sheet top restriction are
perfect squares.  The only top collision in this chart is

\[
s=0,
\]

which is precisely the strict-transform direction (q=0).

## Deutsch--Popperian verdict

The conjecture that the joint blowup creates a new exceptional marked
incidence is falsified on the (p)-chart.  Its marked restrictions contain no
new branch polynomial.  They rationalize into the two existing deck sheets,
and their top collision is carried by the already labelled normal (q=0).

The surviving structure is coefficient-theoretic: the nonuniform Rees shifts
of Entry 1090 and the choice of deck character on these perfect-square
restrictions.  Neither licenses a new carrier wall.

## Classification

- exceptional carrier: existing joint marked-wall resolution;
- single-wall coefficient geometry: rationalized two-sheet restriction;
- top support: existing (q=0) normal;
- new branch divisor: none;
- new carrier stratum: none.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u0v2_newton.rs`;
- `research/benincasa/rank12-u0-v2-joint-rees.json`;
- exact characteristic-zero Symbolica factorization.

Epistemic graph admission:
`ev-000000000786-91925b33-b79c-4818-8fa1-20420cbb4a9a`.

## Next falsifier

Construct the normalized twelve-class reduction on this (p)-chart and test
whether the two perfect-square wall restrictions glue with the required deck
characters at (s=0).  A failure of deck-compatible gluing would be a
coefficient obstruction on the existing carrier; only a source-derived new
incidence equation could reopen the carrier question.
