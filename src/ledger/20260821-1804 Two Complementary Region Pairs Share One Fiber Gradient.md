# 1804 — Two Complementary Region Pairs Share One Fiber Gradient

## Question

Among Entry 1803's nine source-supported region walls, which pairs can create
a higher collision on the physical threshold Morse plane?

## Exact gradient census

There are

\[
\binom92=36
\]

unordered relative-label pairs. For both reflected physical sheets, restrict
their gradients to the \(q_e\)-residue sphere and compute the \(2\times2\)
Gram determinant.

Exact interval arithmetic proves that thirty-four pairs have nonzero
determinant.

Exactly two pairs are collinear:

\[
\boxed{
(g_{145},g_{23}),
\qquad
(g_{15},g_{234}).
}
\]

In each pair the regions are complementary and have the same labelled cut
boundary. Their loop-distance parts, and hence their fiber gradients, are
identical by source incidence—not merely proportional at the sampled point.

Each exceptional pair occurs together with \(G^-_{e_{12}}\) in three source
terms.

## Important qualification

For complementary regions \(A,A^c\),

\[
q_A+q_{A^c}
=
E_T+2\sum_{e\in\partial A}y_e.
\]

Therefore simultaneous vanishing of the two labelled occurrences requires
the additional complement condition

\[
E_T+2\sum_{e\in\partial A}y_e=0.
\]

That condition is not satisfied at the generic active point and cannot be
imposed there by redistributing site energies while holding the threshold
geometry fixed.

## Result

\[
\boxed{
36\text{ supported pairs}
=
34\text{ fiber-independent pairs}
+
2\text{ complementary occurrence pairs}.
}
\]

This entry identifies the only higher-collision candidates. It does not claim
that their deeper complement locus meets the physical threshold divisor.

## Next falsifier

Adjoin each complement condition to the \(g_5\) Landau system, saturate by
the existing walls and soft factors, and test whether a real physical
critical point survives. Only then compute the doubled-occurrence coefficient
complex.

## Evidence

- research/benincasa/checkers/five_site_g5_region_pair_gradient_census.py
- research/benincasa/results/five-site-g5-region-pair-gradient-census.json
- allocator claim: seqclaim-85cdf54ce142c7f165eb922f
