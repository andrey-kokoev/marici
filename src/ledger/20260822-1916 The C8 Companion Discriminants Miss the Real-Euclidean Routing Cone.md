# 1916 — The C8 Companion Discriminants Miss the Real-Euclidean Routing Cone

## Claim

After quotienting by the source base relations, the 36 cyclic orbit representatives of rank-four C8 walls split into four reduced patterns with multiplicities

\[
21+7+6+2=36.
\]

For every pattern, the four cover equations and the companion Jacobian factor have no simultaneous solution with strictly positive retained edge squares and positive-semidefinite full C8 routing Gram matrix.

The edge-8 and edge-6 patterns are directly `unsat` after passing to edge-square variables. The two harder patterns reduce to equations quadratic in one edge square \(B\). Their discriminants are strictly negative throughout the exact C8 PSD polygon. Their linear-solve denominators occur squared in those discriminants, whose zero loci also miss the PSD polygon, so no exceptional branch remains.

Therefore

\[
\boxed{
\text{all 36 C8 companion coefficient-wall orbits miss the real-Euclidean routing cone.}
}
\]

Every orbit has size eight and trivial stabilizer, so this excludes all \(288\) labelled occurrences.

Combined with Entry 1913, both the universal linear factors and all companion factors are excluded on this real-Euclidean continuation class.

## Interpretation

This closes real-Euclidean activation, not complex Leray activation. The coefficient walls remain legitimate algebraic support of the C8 coefficient system. The result supplies no new carrier stratum and makes no claim about a source-selected complex relative cycle.

## Provenance

Allocator claim: `seqclaim-1e48bd2f4356f932e9f08fab`.

Detailed derivation and durable artifacts are in `research/benincasa/eight-site-companion-real-euclidean-exclusion.md` and its linked machine-readable packets.
