# 1871 — Twenty-Eight Triple-Wall Orbits Admit the Pilot Elimination

## Question

Entry 1870 certifies one new saturated quartic from the triple

\[
G_{\setminus e_{12}}\mid g_{1345}\mid g_{145}.
\]

Before repeating that elimination, ask which of Entry 1868's 96 surviving
dihedral representatives have the same source-derived simplification: three
wall equations solve three labelled (y_i) as rational multiples of (t),
without involving the two remaining (y)-variables.

## Exact criterion

For each (3\times5) wall matrix (A), enumerate every three-column pivot
(A_P). A representative enters the pure-(t) stratum exactly when

\[
\det A_P\ne0
\]

and both nonpivot columns vanish in all three rows. Cramer's rule then gives

\[
y_P=-A_P^{-1}m\,t.
\]

The checker verifies every recovered wall equation exactly over
\(\mathbb Q\). Because the Landau ideal is saturated by
\(y_1y_2y_3y_4y_5\), it separately rejects solutions in which a solved
coordinate vanishes for generic (t\ne0).

## Result

All 96 representatives have wall rank three. Of these:

\[
32
\]

admit a pure-(t) wall solution algebraically, but four region-only triples
force one solved (y_i) to zero. The generically nonsoft fast lane therefore
contains

\[
\boxed{28}
\]

dihedral representatives, split as

\[
\boxed{24\,(G_{\setminus e}+g+g)+4\,(g+g+g).}
\]

The remaining 68 representatives require genuinely mixed elimination in
which the solved wall variables depend on one or both free (y)-coordinates.

## Interpretation and scope

This is a finite algorithmic stratification of the frozen source search
space. It does not assert that all 28 representatives produce new divisors,
that their discriminants are distinct, or that any resulting divisor has
nontrivial monodromy in the selected physical period.

It does show that Entry 1870 is not an isolated computational accident: its
elimination architecture applies to a source-defined 28-member stratum. No
new carrier cell or fitted support factor was introduced.

## Next falsifier

Run the pilot elimination on a nonsoft region-only representative from the
four-member (g+g+g) stratum. Then test its saturated discriminant against
the degree-87 candidate union from Entry 1870.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_landau_ideal_compiler.rs`
- `research/benincasa/results/five-site-cyclic-triple-landau-ideal-compiler.json`
- allocator claim: `seqclaim-6c941fe3441b7e22ffb48c08`
- epistemic event: `ev-000000002224-202734da-cbd7-4bd6-a1f2-77fa49879928`
