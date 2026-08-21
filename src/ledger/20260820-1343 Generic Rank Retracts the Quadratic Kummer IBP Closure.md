# 1343 — Generic Rank Retracts the Quadratic Kummer IBP Closure

## Retraction

Entries 1329 and 1335 are retracted.

Their degree-two Kummer-resolved consistency occurred at modular rank-drop fibers and does not define a characteristic-zero affine solution module.

## Generic-rank gate

The declared degree-two system has

\[
961
\]

unknown coefficients:

\[
1+3\cdot32\cdot10.
\]

The original two fibers gave deficient coefficient ranks:

\[
\operatorname{rank}_{(1009,7)}=800,
\qquad
\operatorname{rank}_{(1013,11)}=768,
\]

and happened to be consistent.

A cross-fiber and fresh-prime scan gives

\[
\begin{array}{c|c|c|c}
p&z&\operatorname{rank}M&\text{consistent?}\\
\hline
1019&5&961&\text{no}\\
1019&7&961&\text{no}\\
1019&11&961&\text{no}\\
1021&5&961&\text{no}\\
1021&7&961&\text{no}\\
1021&11&928&\text{yes}.
\end{array}
\]

Thus consistency is confined to modular resonance loci where the coefficient rank drops.

A characteristic-zero identity would remain consistent at every good reduction outside finitely many denominator primes. Independent full-rank inconsistency over \(\mathbf F_{1019}\) and \(\mathbf F_{1021}\) falsifies the proposed degree-two identity.

## Corrected conclusion

\[
\boxed{
\text{The full Kummer-character first-order polynomial IBP ansatz does not close generically through degree two.}
}
\]

Consequently there is no declared affine solution module

\[
\operatorname{Sol}^{(2)}_{\rm Kum}
\]

on which to construct the boundary image claimed in Entry 1335.

The infinity valuation result itself survives:

\[
10\times R^{-2},
\qquad
20\times R^{-4},
\qquad
2\times R^{-9},
\]

with no observed leading canonical-sum cancellation. What is retracted is its interpretation as the nonzero boundary of a degree-two affine primitive.

## New acceptance rule

For modular discovery of an exact form, consistency is admissible only after a generic-rank gate:

1. scan multiple primes and fibers;
2. determine the maximal stable coefficient rank;
3. reject consistency confined to lower-rank fibers;
4. reconstruct only from consistency on the maximal-rank locus;
5. certify by exact substitution.

This rule applies before any kernel, cokernel, boundary, or monodromy interpretation.

## Updated frontier

The bounded no-go now includes:

- scalar-base first-order polynomial primitives through degree five;
- scalar-base second-order polynomial primitives through degree five;
- all single-wall logarithmic first-order primitives through numerator degree two;
- full Kummer-character first-order polynomial primitives through degree two.

The next search must either raise the Kummer-resolved polynomial degree under the generic-rank gate or construct the finite logarithmic de Rham module directly. No boundary module may be formed until a generic affine cocycle exists.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`
- `research/benincasa/results/five-site-asymmetric-kummer-resolved-ibp-pilot.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_infinity_deck_valuation.rs`
- `research/benincasa/results/five-site-asymmetric-infinity-deck-valuation.json`

Allocator claim: `seqclaim-3e88dd25bd23dd886e6d0725`.
