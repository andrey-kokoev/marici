# 1873 — Multiplier Saturation Certifies the Region-Only Quartic

## Remaining gate from Entry 1872

Entry 1872 derives the squarefree nonsoft quartic

\[
D_{3,\mathrm{reg}}(z)
=2016064-5586608z+5762041z^2-2628992z^3+446464z^4
\]

from

\[
g_{1234}\mid g_{234}\mid g_{2345},
\]

but leaves open whether a source wall multiplier vanishes on that component.

## Denominator-free multiplier solve

The three wall rows have zero (y_2)- and (y_3)-columns. Away from soft
support, the corresponding cover-gradient equations force

\[
\alpha_2=\alpha_3=0.
\]

Rather than divide by a quadratic-field coordinate, the checker solves the
remaining routing-gradient equations in the homogeneous scale

\[
\det(H)c_1.
\]

This gives polynomial representatives for

\[
\alpha_1,\alpha_4,\alpha_5
\]

and then solves the five labelled (y)-gradient equations for the three
source-ordered wall multipliers.

The unused routing-gradient component vanishes identically after restriction
to the repeated-root scheme. Thus the multiplier solve is compatible with
the critical-value elimination rather than an independently fitted null
vector.

## Exact result

Up to nonzero rational units, the three multiplier-zero norms are

\[
71-136z+64z^2,
\]

\[
261161-704896z+446464z^2,
\]

and again

\[
71-136z+64z^2.
\]

Each is coprime to (D_{3,\mathrm{reg}}) at the good prime
(2147483647). Together with Entry 1872's soft and lower-support exclusions,
this proves

\[
\boxed{
D_{3,\mathrm{reg}}=0
\text{ is a saturated region-only triple-wall Landau divisor.}
}
\]

## Updated finite bound

The new quartic is coprime to the degree-87 union, so the certified Landau
candidate denominator bound becomes

\[
\boxed{\deg_z D_{\mathrm{cand}}=91.}
\]

This remains a geometric denominator bound. It does not prove nontrivial
monodromy of the selected scalar period at every root, nor does it identify a
new carrier wall. The divisor is produced by compatible composition of three
already frozen walls.

## Next falsifier

Run the same saturated elimination on the remaining three nonsoft
region-only pure-(t) representatives. Determine whether they reproduce the
two known quartic orbits or enlarge the degree-91 union.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_pilot.rs`
- `research/benincasa/results/five-site-cyclic-triple-region-pilot.json`
- allocator claim: `seqclaim-88d9d8979de5aad837adb268`
- epistemic event: `ev-000000002227-e5992edb-46df-472b-9d4c-a543318e9526`
