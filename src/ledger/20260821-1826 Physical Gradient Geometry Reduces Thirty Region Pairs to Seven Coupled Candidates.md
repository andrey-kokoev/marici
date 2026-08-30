# 1826 — Physical Gradient Geometry Reduces Thirty Region Pairs to Seven Coupled Candidates

## Census

After Entries 1824--1825, the source-compatible pair frontier consists of
thirty region--region orbits.  Their two-edge cut supports divide as

\[
2\text{ same-cut}
\;\sqcup\;
21\text{ one-edge overlaps}
\;\sqcup\;
7\text{ disjoint cuts}.
\]

## One-edge overlap

Write the two physical gradients as

\[
v_1=u_a+u_b,
\qquad
v_2=u_b+u_c,
\]

where all \(u\)'s are unit vectors.  Positive Landau multipliers require
\(v_1=-\lambda v_2\) for some \(\lambda>0\), hence

\[
u_a+(1+\lambda)u_b+\lambda u_c=0.
\]

The coefficient \(1+\lambda\) equals the sum of the other two coefficients.
The unit-vector triangle inequality must therefore be saturated.  This forces

\[
u_a=u_c=-u_b,
\]

and consequently

\[
v_1=v_2=0.
\]

Thus no one-edge-overlap orbit supports a genuinely coupled cancellation of
two nonzero physical gradients.  Any survivor belongs to the simultaneous
stationary loci of the individual region walls and must be treated as an
iterated one-wall endpoint problem.

## Same-cut profiles

The two same-cut profiles already force \(t=0\).  Their identical gradients
cannot cancel with positive multipliers unless stationary, and their wall
equations then lie on existing soft support.

## Result

\[
\boxed{
30\text{ region-pair orbits}
\longrightarrow
7\text{ genuinely coupled disjoint-cut candidates}.
}
\]

This is a typing reduction, not a claim that the simultaneous stationary
loci vanish.  It separates those iterated endpoint objects from ordinary
two-wall physical pinches.

## Next falsifier

For the seven disjoint-cut representatives, solve the two wall equations
together with antiparallel, nonzero physical gradients and positive
multipliers.  Apply the open physical-domain gate before constructing any
ambient resultant or period system.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_physical_gradient_reduction.py`
- `research/benincasa/results/five-site-region-pair-physical-gradient-reduction.json`
- allocator claim: `seqclaim-1043cc2a10fb87bc8593ed91`
