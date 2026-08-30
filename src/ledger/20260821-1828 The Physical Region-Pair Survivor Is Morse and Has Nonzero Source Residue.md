# 1828 — The Physical Region-Pair Survivor Is Morse and Has Nonzero Source Residue

## Transverse Hessian

For a nonzero distance vector with unit direction \(u\),

\[
\operatorname{Hess}|\ell-C|
=
\frac{I-uu^T}{|\ell-C|}
\]

is positive semidefinite with kernel \(\mathbb Ru\).  Entry 1827's exact
focal-line Gram certificate proves that the two rays entering
\(g_{123}\) are nonparallel.  Their Hessian sum is therefore already positive
definite.  Consequently the positive-multiplier Landau Hessian

\[
\operatorname{Hess}(g_{123}+g_{125})
\]

is positive definite as well.

Thus the physical critical point is Morse; it is not a flat or higher-order
stationary artifact.

## Remaining-wall separation

The exact rational-interval evaluation uses Entry 1827's isolating interval

\[
0.7067<q_*<0.7068.
\]

Every remaining denominator appearing in the ten frozen source terms that
contain both active walls is certified away from zero.  The candidate is
therefore isolated from all other source supports in this chart.

## Summed source coefficient

Removing \(g_{123}\) and \(g_{125}\) from those ten terms and summing the
remaining reciprocal products gives the certified interval

\[
-0.00689243
<
R_{m src}
<
-0.00686629.
\]

Hence

\[
\boxed{R_{m src}\ne0.}
\]

This is the source coefficient before the conventional nonzero geometric
double-residue Jacobian and orientation sign.  Those factors cannot turn a
nonzero coefficient into zero.

## Result

The pair \((g_{123},g_{125})\) now passes, in order:

1. frozen source co-occurrence;
2. exact physical pullback and positive multipliers;
3. open internal-distance support;
4. Morse nondegeneracy;
5. remaining-wall separation;
6. nonzero summed source residue.

It is therefore a genuine local physical pinch of the frozen five-site source
form.  What remains is to derive its vanishing-cycle coefficient object and
test whether cyclic assembly stays on the existing Cut/energy carrier.

## Next falsifier

Construct the local Picard--Lefschetz variation in the source-normalized
orientation, transport it through the five labelled cyclic occurrences, and
classify the resulting coefficient system.  No new carrier cell may be added;
failure to realize the variation as coefficient data over the existing pair
incidence would be the relevant H2 falsifier.

## Evidence

- `research/benincasa/checkers/five_site_disjoint_region_pair_source_residue.py`
- `research/benincasa/results/five-site-disjoint-region-pair-source-residue.json`
- Entry 1827
- allocator claim: `seqclaim-59381417962e2a5a60e4fd55`
