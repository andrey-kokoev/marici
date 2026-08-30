# 1840 — Correction: A True Polar Landau Point Is Double-Morse and Square-Root

## Error corrected

Entry 1837 correctly identifies the owner-wall focal segment and its
Morse--Bott transverse quadratic form.  Its proposed transverse cut by the
second wall is **not**, however, a physical Landau point.

On the owner focal segment,

\[
\nabla q_1=0.
\]

The positive Landau equation is

\[
\alpha\nabla q_1+\beta\nabla q_2=0,
\qquad
\alpha,\beta>0.
\]

It therefore forces

\[
\boxed{\nabla q_2=0.}
\]

Thus the loop point must lie on the second focal segment as well.  Entry
1837's transverse-second-wall grade-zero logarithmic model is withdrawn.

## Correct local geometry

At a generic true polar collision, two nonparallel focal segments intersect.
The two Hessians are positive semidefinite with kernels equal to their segment
directions:

\[
\ker H_1=T\ell_1,
\qquad
\ker H_2=T\ell_2.
\]

For nonparallel lines, every positive combination

\[
\alpha H_1+\beta H_2
\]

is positive definite.  The local physical integral is therefore of
double-quadratic Morse type:

\[
\int
\frac{d^3x}
{(\delta_1+Q_1(x))(\delta_2+Q_2(x))}.
\]

On a generic diagonal normal \(\delta_1\sim\delta_2\sim\delta\), scaling
\(x=\sqrt\delta\,\xi\) gives

\[
\delta^{3/2-2}=\delta^{-1/2}.
\]

Hence the local coefficient is a rank-one square-root Kummer/Morse line with
monodromy \(-1\), not a logarithmic line.

## Corrected classification

Entry 1839's support typing survives:

- carrier: existing Gram/Cayley--Menger segment-intersection divisor;
- coefficient condition: equality of labelled focal lengths;
- physical chamber: both labelled segment parameters in \([0,1]\).

Only the coefficient type changes:

\[
\boxed{
\text{polar coefficient}=	ext{square-root Kummer line}.
}
\]

No new carrier datum is required.

## Remaining exceptional case

Parallel or coincident focal segments make the positive Hessian combination
degenerate.  That deeper Gram stratum requires a separate excess calculation
and is not covered here.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_polar_double_morse_correction.py`
- `research/benincasa/results/five-site-region-pair-polar-double-morse-correction.json`
- Entries 1836--1839
- allocator claim: `seqclaim-2d786ab9c6b9c397a2f6c58b`
