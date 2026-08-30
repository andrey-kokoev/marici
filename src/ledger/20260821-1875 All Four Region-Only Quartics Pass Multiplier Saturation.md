# 1875 — All Four Region-Only Quartics Pass Multiplier Saturation

## Common source-derived solve

Entry 1874 finds four pairwise-coprime nonsoft quartics from the four
region-only pure-(t) representatives. To avoid four fitted null vectors, the
checker now derives every multiplier from the same labelled construction.

For each representative:

1. the two free (y_i)-columns force their cover multipliers to zero away
   from soft support;
2. the remaining three cover multipliers are solved homogeneously from three
   independent rows of the routing-gradient system;
3. the unused routing row is retained as a consistency equation;
4. the transpose of the source wall-incidence matrix solves the three wall
   multipliers;
5. all expressions are restricted through the same (G=0) elimination and
   repeated-root map used to derive the quartic.

No quadratic-field division or choice of primitive null-vector normalization
is used.

## Exact result

For all four representatives:

- the cover-multiplier pivot is nonzero;
- the labelled wall-incidence pivot is (pm2);
- the unused routing-gradient equation restricts identically to zero;
- each of the three wall-multiplier zero norms is coprime to its quartic at
  the good prime (2147483647).

Therefore

\[
\boxed{
D_1D_2D_3D_4=0
\text{ is a union of four saturated region-only triple-wall divisors.}
}
\]

## Updated bound

The four quartics are pairwise coprime and are each coprime to Entry 1870's
degree-87 union. The certified five-site cyclic Landau candidate bound is now

\[
\boxed{\deg_zD_{\mathrm{cand}}=103.}
\]

This is a geometric bound, not yet the singular divisor of the selected
period. Numerator cancellation and trivial Betti pairing remain possible.

## Architectural meaning

The four new divisors arise from compatible triples of existing region walls.
They enlarge the coefficient singular locus without adding a carrier
incidence generator. This is positive evidence for

\[
\text{shared carrier and calculus}
+
\text{sector-specific coefficient objects}.
\]

## Next falsifier

Move from Landau permission to the selected cyclic period. Compute local
Picard--Lefschetz or differential-equation monodromy at one generic root from
each quartic orbit. A trivial pairing removes that factor from the physical
period even though the geometric Landau component is saturated.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_pilot.rs`
- `research/benincasa/results/five-site-cyclic-triple-region-census.json`
- allocator claim: `seqclaim-96585d030de3db46c290f14d`
- epistemic event: `ev-000000002231-9ff8e634-6353-44fd-927b-7bf08549ef96`
