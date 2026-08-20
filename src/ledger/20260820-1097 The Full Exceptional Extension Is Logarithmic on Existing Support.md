# 1097 — The Full Exceptional Extension Is Logarithmic on Existing Support

## Record

Entry 1095 derived a two-pole source frame for the absolute quotient line.
The complete rank-four connection is now reconstructed in the quotient basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_4)
\]

and transported to the (e_5) frame.

Sequence claim: `seqclaim-168ab3b1b72c01d0c62fc51c`.

## Quotient connection shape

The induced connection is upper triangular in the stated ordering.  Thus the
absolute line is a quotient connection, while the three marked classes extend
it through one wall-to-line column.  No line-to-wall entries occur.

Use the source transition

\[
e_5=-\frac{24}{(s+3)(s^2+3)}e_4.
\]

In the transformed ordering

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_5),
\]

the extension column is

\[
\boxed{
A_{03}'
=
-\frac{(s+1)(s^3-5s^2-9s-3)}
{8s(s-1)(s^2+6s+1)},
}
\]

\[
\boxed{
A_{13}'
=
\frac{(s+1)^3}{(s-1)(s^2+6s+1)},
}
\]

and

\[
\boxed{
A_{23}'
=
\frac{s+1}{4(s-1)}.
}
\]

The scalar line entry remains

\[
A_{33}'=-\frac{2(s-2)}{(s-1)(s+1)}.
\]

## Support audit

Every extension pole belongs to

\[
s=0,
\qquad
s=1,
\qquad
s^2+6s+1=0.
\]

These are respectively:

- the existing top-collision direction (q=0);
- the existing (L_2) endpoint collision;
- the exact (L_1) square-root collision of Entry 1094.

The candidate factors

\[
s+3,
\qquad
s^2+3
\]

cancel from the entire extension column, not merely from the scalar diagonal.

## Deutsch--Popperian verdict

The conjecture that the scalar frame correction might leave a hidden
wall-to-line pole on undeclared support is falsified in both tested finite
fields.  The complete rank-four exceptional connection is logarithmic on
existing branch/marked support after the source-derived frame change.

Therefore the first exceptional center closes, at this associated-grade and
modular-connection level, as

\[
\boxed{
\text{existing joint carrier}
+
\text{sector-specific rank-four coefficient extension}.
}
\]

No new carrier incidence is indicated.

## Epistemic status

- matrix shape and rational entries: identical reconstruction over two
  independent 61-bit primes;
- each entry verified at nine unused directions per prime;
- frame cancellation and support factorization: exact rational algebra;
- characteristic-zero primitive witness for the complete matrix: pending;
- new carrier datum: none.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`;
- `research/benincasa/rank12-u0-v2-exceptional-line.json`.

Epistemic graph admission:
`ev-000000000796-c6e81e53-4618-480f-ac2e-f6377206efbe`.

## Next falsifier

Construct the overlapping (q\neq0) chart independently and compare its
rank-four quotient connection with this (p\neq0) chart.  Derive the chart
transition from the joint Rees coordinates and test cocycle, deck-character,
and connection compatibility.  A failure to glue would localize the remaining
obstruction to coefficient descent on the existing carrier.
