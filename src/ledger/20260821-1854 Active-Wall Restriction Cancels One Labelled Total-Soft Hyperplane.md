# 1854 — Active-Wall Restriction Cancels One Labelled Total-Soft Hyperplane

## Correction to Entries 1852--1853

The angular coefficient is not an ambient function on all six homogeneous
energy variables.  The ordered double residue lives on

\[
g_{123}=g_{125}=0.
\]

In the representative conventions these equations are

\[
3t+y_3+y_5=0,
\qquad
3t+y_2+y_4=0.
\]

Entries 1852--1853 counted poles before imposing this restriction.  Their
ambient support statements remain algebraically correct, but their physical
pole count is withdrawn.

## Exact restricted coefficient

After eliminating

\[
y_5=-3t-y_3,
\qquad
y_4=-3t-y_2,
\]

the exact ten-term coefficient reduces to

\[
-\frac{2}{5}
\frac{
11t^2+5ty_2+7ty_3+y_2^2+2y_2y_3+y_3^2
}{
\begin{aligned}
&t(t+2y_2)(5t+2y_3)(t+y_1+y_2)(t+y_2+y_3)\\
&\quad\cdot(2t+y_2+y_3)(2t+y_2-y_3)(2t-y_1+y_3)\\
&\quad\cdot(4t+y_2+y_3)(5t+y_2+y_3)
\end{aligned}
}.
\]

The restriction identifies two labelled source facets:

\[
\boxed{
g_{1235}|_{\rm active}
=
-g_{12}|_{\rm active}.
}
\]

Their apparent common pole cancels completely.  Neither a simple nor a double
pole remains on that restricted hyperplane.

## Physical pole census

The representative physical coefficient has ten genuine simple pole classes:

\[
G,\ G_{-e_{34}},\ G_{-e_{45}},\
g_1,g_2,g_3,g_4,g_5,g_{1234},g_{1245}.
\]

Thus

\[
\boxed{
12\ \text{ambient labels}
\longrightarrow
11\ \text{restricted hyperplanes}
\longrightarrow
10\ \text{physical poles}.
}
\]

## Architectural meaning

This is an occurrence-sensitive deletion--restriction phenomenon.  Two
distinct carrier labels become the same restricted hyperplane, while the
source numerator removes that hyperplane from the coefficient divisor.  The
carrier labels must remain distinct even though the physical coefficient is
regular on their common restriction.

No new carrier datum appears.

## Next falsifier

Transport the restricted ten-pole packet around the five occurrence charts.
Track which labelled pair/four-site coincidence cancels in each chart and
compute the resulting occurrence-resolved support complex before taking any
unlabelled global union.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_region_pair_total_soft_angular_residues.rs`
- `research/benincasa/checkers/five_site_region_pair_total_soft_active_restriction.py`
- `research/benincasa/results/five-site-region-pair-total-soft-active-restriction.json`
- Entries 1851--1853
- allocator claim: `seqclaim-0c695145cf007bbdbc448565`
