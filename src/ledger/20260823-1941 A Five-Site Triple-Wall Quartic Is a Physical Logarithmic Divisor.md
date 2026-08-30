# 1941 — A Five-Site Triple-Wall Quartic Is a Physical Logarithmic Divisor

## Question

Do any of Entry 1940's four genuine nonsoft pure-(t) three-wall
representatives survive exact elimination, lower-support saturation, and the
physical-cycle gates?

## Exact four-representative elimination

For each representative, eliminate the two remaining squared loop-energy
coordinates from the frozen five-Kummer-cover ideal and the three labelled
wall equations.  Saturate by:

- the routing Gram determinant;
- all five loop-energy coordinates;
- vanishing wall multipliers;
- coincident focal gradients;
- the certified one-/two-wall discriminant union.

All four rational field norms are quartic in (z=t^2).  They are square-free,
pairwise coprime, coprime to both free-coordinate soft tests, and coprime to
the lower discriminant union.  The exact Symbolica packets reproduce
byte-for-byte.

## Physical root census

Three representatives fail before physical activation:

- two have positive norm roots only on the wrong quadratic branch;
- (g_{123}\mid g_4\mid g_5) has one root with common multiplier sign but no
  positive linear loop sheet.

For

\[
g_{12}\mid g_{34}\mid g_5,
\]

the primitive field norm is

\[
\boxed{
D_4(z)=
1024z^4-16576z^3+95289z^2-231696z+202304.
}
\]

It has four positive simple real roots.  Exactly one certified root interval
simultaneously has:

- the correct (\mathbb Q(\sqrt5)) branch;
- positive free squared loop energies;
- a positive linear loop sheet, with (t<0);
- three common-sign, nonzero projective Landau multipliers.

## Source and Betti activation

Exactly eight frozen OFPT terms contain the active labelled walls.  Their
uncut denominator products all have residue sign (-1), so termwise
cancellation is impossible.

Under the independent source prescription

\[
X_i\longmapsto X_i-i\epsilon_i,
\qquad \epsilon_i>0,
\]

the active normal pairing is strictly negative throughout the full positive
regulator cone.  The local ordinary-(A_1) Picard--Lefschetz intersection has
absolute value one.  Cyclic transport gives one free orbit of five labelled
physical singularities.

Therefore

\[
\boxed{
D_4=0\text{ supports a source-derived five-site physical logarithmic
coefficient singularity.}
}
\]

## Architectural classification

The divisor arises from three existing occurrence-resolved region walls and
the frozen loop routing/Kummer geometry.  It is new coefficient support over
the existing carrier, not a new carrier incidence generator.

This is a progressive Q-1 belt result: higher external complexity produces a
genuine successor polynomial with nontrivial physical activation.  No
relationship between (D_4) and the homogeneous three-site quartic
(\mathcal Q) is asserted yet.

## Next falsifier

Derive a source-defined degeneration from the five-site family to the
homogeneous three-site family.  Pull back (D_4) along that map and classify
the limit before comparing factors with (\mathcal Q).  If no such
degeneration exists, (D_4) is an independent higher-site successor rather
than a parent of (\mathcal Q).

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_pilot.rs`
- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_real_roots.rs`
- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_d4_source_residue.rs`
- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_d4_iepsilon_pairing.rs`
- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_d4_activation_orbit.rs`
- corresponding JSON packets under `research/benincasa/results/`
- allocator claim: `seqclaim-403afccb1e8981223f14bc8b`

