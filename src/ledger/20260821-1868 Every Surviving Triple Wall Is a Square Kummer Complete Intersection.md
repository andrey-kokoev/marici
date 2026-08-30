# 1868 — Every Surviving Triple Wall Is a Square Kummer Complete Intersection

## Source-normalized compiler

Entry 1867 leaves 96 nonzero dihedral triple-wall representatives on the
cyclic physical slice. Each representative is now compiled on the frozen
rank-three multi-Kummer cover with fiber variables

\[
(u_1,u_2,u_3,y_1,y_2,y_3,y_4,y_5).
\]

The coefficient field is \(\mathbb Q(\sqrt5)\). The routing Gram matrix,
its determinant, the coordinates of the fifth routing center, the five
Kummer equations, and every labelled wall equation are derived from the
source conventions rather than selected per example.

## Rank theorem

For each triple, form the \(3\times5\) matrix of coefficients of
\((y_1,\ldots,y_5)\) in its three wall equations. Exact integer elimination
gives

\[
\boxed{
\operatorname{rank}=3
\quad\text{for all }96\text{ representatives}.
}
\]

Thus no surviving case has a rank-deficient wall pullback. The five Kummer
cover equations plus the three wall equations form a square system of eight
constraints in eight fiber variables at fixed \(t\).

## Canonical critical ideal

For every representative the unsaturated critical ideal is therefore

\[
I_{\rm crit}
=
\left(
K_1,\ldots,K_5,
q_{a},q_b,q_c,
\det J_{\rm fib}
\right),
\]

where \(J_{\rm fib}\) is the \(8\times8\) Jacobian of the five Kummer and
three wall equations with respect to the eight fiber variables.

The determinant is canonical in the frozen ordering up to a nonzero
orientation sign. A genuine triple-wall eliminant must still saturate away:

- edge-soft factors \(y_1\cdots y_5\);
- lower-wall solutions where a Landau multiplier vanishes;
- coincident-focus or vanishing-gradient components;
- the already inverted routing Gram determinant.

## Narrow result

The 96-case problem now has one uniform exact ideal template. No exceptional
rank-deficient complex or fitted critical equation is required. This is
computational infrastructure, not evidence that all 96 ideals have nonempty
saturated support.

## Next falsifier

Run saturation and elimination for one representative in each source wall
type/profile, beginning with the profiles of smallest support overlap. Verify
that representatives sharing a proposed template have identical eliminants
under their exact dihedral transition before transporting the result.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_landau_ideal_compiler.rs`
- `research/benincasa/results/five-site-cyclic-triple-landau-ideal-compiler.json`
- `research/benincasa/results/five-site-compatible-landau-subsets.json`
- Entries 1215--1217 and 1867
- allocator claim: `seqclaim-28a78800ad392e8130ec88ce`
