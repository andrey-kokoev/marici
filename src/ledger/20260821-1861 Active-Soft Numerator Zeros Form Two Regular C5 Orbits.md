# 1861 — Active-Soft Numerator Zeros Form Two Regular (C_5) Orbits

## Four endpoint types

Apply Entry 1860's exact numerator to all four active-soft occurrences of the
ordered representative ((g_{123},g_{125})).  After extracting the common
positive scale and writing the remaining radial ratio as (xin(0,3)), the
four numerator polynomials are

\[
\begin{array}{c|c|c}
\text{soft occurrence}&N(x)&\operatorname{disc}N\\
\hline
y_2=0&x^2-7x+11&5\\
y_3=0&x^2-5x+11&-19\\
y_4=0&x^2-x+5&-19\\
y_5=0&x^2+x-1&5.
\end{array}
\]

Thus the two middle endpoint types have no real numerator zero.

## Physical zero rays

The two physical roots are

\[
y_2=0:qquad
x=\frac{7-\sqrt5}{2},
\]

and

\[
y_5=0:qquad
x=\frac{\sqrt5-1}{2}.
\]

The other root of each quadratic lies outside (0<x<3).

This asymmetry is legitimate occurrence data: the ordered region pair and its
source residue orientation distinguish the four endpoint positions.  It must
not be erased by declaring all soft endpoints equivalent before calculation.

## Cyclic assembly

Each endpoint type has a free five-element cyclic orbit.  Therefore the two
zero-bearing types assemble as

\[
\boxed{
2\mathbb Q[C_5],
}

with character

\[
\boxed{
(10,0,0,0,0).
}

Among the twenty active-soft endpoint occurrences, exactly ten carry one
physical numerator-zero ray and ten carry none.

## Classification

These rays are zeros of the sector-specific source coefficient.  They are not
singular support, carrier walls, or new incidence generators.  Their cyclic
covariance confirms that the cancellation is source-defined rather than a
coordinate accident.

## Next falsifier

At one zero-bearing endpoint, expand the exact source coefficient transversely
to the numerator-zero ray.  Determine whether the vanishing is simple and
whether it raises the first nonzero active-soft normal term from second to
third Rees order only on that coefficient locus.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_active_soft_zero_orbits.py`
- `research/benincasa/results/five-site-region-pair-active-soft-zero-orbits.json`
- Entries 1859--1860
- allocator claim: `seqclaim-5817757a37db3aeb841220d7`
