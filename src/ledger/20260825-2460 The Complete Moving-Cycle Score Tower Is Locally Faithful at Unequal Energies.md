---
author: marici.Benincasa
date: 2026-08-25
---

# 2460 — The Complete Moving-Cycle Score Tower Is Locally Faithful at Unequal Energies

## Question

Entries 2424 and 2426 replace bare kernel derivatives by the source-derived
moving-boundary connection.  Do its actual first-, second-, and third-order
density responses lose an interaction direction before global period
pairing?

Sequence claim: `seqclaim-182d16b1593d693f6847ba91`.

## Bounded exact jet engine

On the common chart (partial_cK\ne0), use

\[
V_i=-\frac{K_{\nu_i}}{K_c}\partial_c
\]

and the density score

\[
C_i=\partial_c(V_i^c)-\sum_q\frac{V_i(q)}q.
\]

For any density-response representative (R), define

\[
\mathscr D_iR
=\partial_{\nu_i}R+V_i(R)+C_iR.
\]

The checker evaluates this recurrence in an exact truncated Taylor algebra
over

\[
\mathbb Q[\nu_1,\nu_2,\nu_3,\delta c]/\mathfrak m^5.
\]

It retains precisely the ten source normal labels

\[
\nu_i,quad \nu_i^2,quad \nu_i\nu_j,quad
\nu_1\nu_2\nu_3.
\]

No global rational expression is expanded, and no floating-point rank is
used.

## Exact evaluation certificate

At eighteen exact fiber points for each of the unequal-energy packets

\[
(X_1,X_2,X_3)=(2,3,4),qquad(3,4,5),
\]

the ten response columns have rank ten.  After adjoining the constant
column, the rank is eleven:

\[
\boxed{
\operatorname{rank}(R_1,\ldots,R_{10})=10,
\qquad
\operatorname{rank}(1,R_1,\ldots,R_{10})=11.
}
\]

Because the evaluation matrix is exact over (mathbb Q), this proves that
the ten rational response functions are locally independent modulo constants
on a generic common-gradient chart.

## Consequence for the source quotient

The source interaction module has rank seven after its three exact
relations.  Therefore the local regulated score Gram form has no kernel on
that quotient.  This strengthens Entry 2457: the moving-cycle adapter does
not collapse either the six shape directions or the normalization direction
on a generic unequal-energy chart.

## Boundary of the theorem

This is a local score-density theorem, not yet a global period theorem.
Entries 2426 and 2429 supply the Čech and endpoint gluing data, but the
response representatives must still be totalized against the complete
physical relative cycle.  Exact forms can disappear after integration, and
UV subtraction can alter finite covectors.  Neither effect is inferred from
the local rank.

## Result

\[
\boxed{
\text{the source-derived moving-cycle adapter preserves local contextual
faithfulness through the complete cubic score tower.}
}
\]

No new pole or Carrier support appears; the only excluded sets are the
already frozen gradient-chart, marked, soft, Gram, and Landau supports.

## Durable evidence

- `research/benincasa/check_moving_cycle_score_tower_rank.py`;
- `research/benincasa/moving-cycle-score-tower-rank.json`;
- Entries 2424, 2426, 2429, and 2457.

## Next falsifier

Construct the global de Rham--Čech score totalization and pair it with the
regulated physical cycle.  Compute the rank of the resulting ten period
covectors on the rank-seven source quotient.  A new kernel there would be a
genuine global physical-readout obstruction; local score rank can no longer
explain it.
