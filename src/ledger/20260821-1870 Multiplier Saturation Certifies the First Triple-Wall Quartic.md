# 1870 — Multiplier Saturation Certifies the First Triple-Wall Quartic

## Remaining gate from Entry 1869

Entry 1869 derives the nonsoft quartic

\[
D_3(z)=7424-35728z+61041z^2-44032z^3+11264z^4
\]

for

\[
G_{\setminus e_{12}}\mid g_{1345}\mid g_{145},
\]

but leaves open whether one of the three wall multipliers vanishes
identically on that divisor.

## Normalization-free multiplier test

Let \(\alpha_1,\alpha_2,\alpha_3\) be the Kummer-equation multipliers for
the three solved square variables, normalized only by

\[
\alpha_1+\alpha_2+\alpha_3=1.
\]

The routing-column equations imply

\[
\alpha_2=(H^{-1}u)_1,
\qquad
\alpha_3=(H^{-1}u)_2.
\]

Using the source wall ordering, the three wall multipliers vanish precisely
with

\[
\alpha_2,
\qquad
\alpha_3,
\qquad
5-8\alpha_2-6\alpha_3.
\]

Instead of substituting the rational repeated root
\(v=-P_1/(2P_2)\), the checker clears its denominator first. This produces
three polynomial zero tests over \(\mathbb Q(\sqrt5)[z]\), independent of
the null-vector normalization.

## Exact result

The rational field norm of each multiplier-zero polynomial is coprime to
\(D_3\) at the good prime \(2147483647\). Together with Entry 1869's
square-free and soft-branch tests, this proves that on the generic quartic
locus:

- \(y_1,\ldots,y_5\ne0\);
- the routing Gram pivot remains a unit;
- all three source-ordered wall multipliers are nonzero.

Therefore

\[
\boxed{
D_3(z)=0
\text{ is a saturated triple-wall Landau divisor.}
}
\]

## Updated finite bound

Since \(D_3\) is coprime to Entry 1866's degree-83 polynomial, the certified
Landau denominator bound becomes

\[
\boxed{
\deg_z D_{\rm cand}=87.
}
\]

This does not yet prove that the selected scalar period has nontrivial local
monodromy at every root of \(D_3\); numerator cancellation or trivial cycle
pairing remains possible. It does prove that the source Landau geometry
permits the divisor without lower-support contamination.

## Next falsifier

Transport the pilot through every dihedral-equivalent occurrence and verify
the orientation/unit packet. Then run the same elimination on the next
geometric profile and compare its saturated factor with the degree-87 union.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_landau_pilot.rs`
- `research/benincasa/results/five-site-cyclic-triple-landau-pilot.json`
- Entries 1866 and 1869
- allocator claim: `seqclaim-a8f1bc5254d1fdf0845d5629`
