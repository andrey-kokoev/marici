# 1809 — Exactly Twenty-Two Transverse Region Pairs Are Source-Active

## Claim

Among Entry 1808's 34 transverse pairs of supported five-site region walls,
exactly 22 have nonzero source double-residue coefficients at the frozen
physical threshold.

## Frozen calculation

For each source-supported pair, keep

\[
G^-_{e_{12}}=g_5=g_A=g_B=0
\]

and preserve total energy while solving the two labelled wall equations with
three source-energy coordinates. The adjustment triple is chosen only to
isolate the intersection from all remaining marked walls; it does not alter
the source sum.

For each of the two physical loop sheets, exact rational interval arithmetic
then evaluates the complete double-residue coefficient after removing the
four frozen denominators. Every remaining denominator is certified away from
zero.

## Result

After excluding the ten source-absent pairs and Entry 1808's two exact source
cancellations, all remaining coefficients obey

\[
0\notin \operatorname{Res}_{A,B}
\]

on both physical sheets. The certificate count is

\[
22\times2=44.
\]

Thus the exact partition is

\[
\boxed{
34
=10\ \text{source absent}
+2\ \text{source cancelled}
+22\ \text{source active}.
}
\]

This certifies activation only. It does not yet identify the integrated local
coefficient object with a tensor product of the two one-wall Kummer systems.

## Architectural consequence

The carrier incidence, source term incidence, and source residue differential
are three distinct gates:

\[
\text{transverse carrier pair}
\not\Rightarrow
\text{source co-occurrence}
\not\Rightarrow
\text{nonzero source coefficient}.
\]

All three gates are now explicitly resolved for this finite pair census.

## Next falsifier

Compute the labelled \(C_5\)-orbit decomposition of the 22 active pair types.
For one representative of each orbit, derive the two-normal local integral
and test whether its coefficient system splits as a Kummer tensor product or
contains a nontrivial extension.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_pair_exact_coefficients.py
- research/benincasa/results/five-site-g5-transverse-pair-exact-coefficients.json
- allocator claim: seqclaim-74050128f126d049f53c1a30
