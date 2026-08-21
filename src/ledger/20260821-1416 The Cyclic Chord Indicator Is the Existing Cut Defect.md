# 1416 — The Cyclic Chord Indicator Is the Existing Cut Defect

## Status

Exact combinatorial identification applied to Entry 1415’s replicated modular residual.

> **CORRECTION (Entry 1423).** The Cut defect identifies which sheets occur in the growth-four boundary grade. It is a support valuation, not a compatibility valuation across all six orbits.

## Question

Entry 1415 factors the boundary residual into a direction-dependent scalar and a binary selector on the six nontrivial (C_5)-sheet orbits.

Is that selector a new string-sector primitive?

## Cut valuation

For a nontrivial proper subset (S) of the labelled five-cycle, let

\[
|\partial S|
\]

be the number of cycle edges crossing from (S) to its complement.

The six cyclic orbit representatives have cut sizes

\[
\begin{array}{c|cccccc}
S&1&3&5&7&11&15\\
\hline
|\partial S|&2&2&4&2&4&2.
\end{array}
\]

Therefore Entry 1415’s selector is exactly

\[
\boxed{
\chi_{\rm obs}(S)
=
\frac{4-|\partial S|}{2}.
}
\]

The diagonal-pair orbit (5) and its complement (11) are precisely the maximum-cut orbits and have zero defect. Every other nontrivial orbit has cut size two and defect one.

## Boundary residual

For each sampled kinematic direction (d), the modular residual becomes

\[
\boxed{
\operatorname{res}_d(S)
=
\rho_d\frac{4-|\partial S|}{2}.
}
\]

The occurrence dependence is thus entirely compiled from existing labelled Cut incidence.

## Narrow consequence

No new string-specific carrier generator is supported by this obstruction. The tested model instead exhibits

\[
\boxed{
\text{existing Cut carrier valuation}
\otimes
\text{string-sector scalar boundary functional}.
}
\]

This supports the shared-carrier, sector-specific-coefficient architecture at this finite five-site test.

## Limits

The scalar functional (ho) remains modular and sample-defined. The declared radial boundary model has not yet been identified with a physical string compactification boundary.

## Next finite falsifier

Derive (ho) from the source denominator form and test whether it is a canonical residue/normal valuation. If no source-defined functional produces the sampled values, the factorization remains computational pattern evidence only.

Artifacts:

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_kummer_ibp_pilot.rs`
- `research/benincasa/results/five-site-cyclic-level-zero-obstruction.json`

Allocator claim: `seqclaim-c63c61e030304fb23a5127cd`.
