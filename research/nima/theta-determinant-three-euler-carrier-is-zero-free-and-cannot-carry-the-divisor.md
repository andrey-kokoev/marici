# The determinant-three Euler carrier is zero-free and cannot carry the Riemann divisor

## Native chart domains

On the labelled prime Hilbert space, define the reciprocal diagonal operators

\[
L_+(s)e_p=p^{-s}e_p
\]

and

\[
L_-(s)e_p=p^{s-1}e_p.
\]

The Schatten-three condition for \(L_+\) is

\[
\sum_p |p^{-s}|^3
=
\sum_p p^{-3\operatorname{Re}s}
<\infty,
\]

which holds exactly when

\[
\operatorname{Re}s>\frac13.
\]

For \(L_-\), the condition is

\[
\sum_p |p^{s-1}|^3
=
\sum_p p^{-3(1-\operatorname{Re}s)}
<\infty,
\]

which holds exactly when

\[
\operatorname{Re}s<\frac23.
\]

Thus the two determinant-three charts overlap on

\[
\frac13<\operatorname{Re}s<\frac23,
\]

an open strip containing the critical seam.

## Each chart determinant is zero-free

An eigenvalue \(1\) of \(L_+(s)\) would require

\[
p^{-s}=1
\]

for some prime \(p\). Taking absolute values forces

\[
\operatorname{Re}s=0.
\]

This lies outside the \(L_+\) Schatten-three chart. Therefore

\[
\det_3(I-L_+(s))\ne0
\]

throughout its native domain.

Similarly, an eigenvalue \(1\) of \(L_-(s)\) would require

\[
p^{s-1}=1,
\]

which forces

\[
\operatorname{Re}s=1.
\]

This lies outside the \(L_-\) chart. Hence

\[
\det_3(I-L_-(s))\ne0
\]

throughout its native domain.

## Transition is a unit

On the overlap strip, the ratio of the two nonvanishing determinant-three trivializations is a holomorphic unit.

Therefore the reciprocal Euler construction supplies a coherent determinant-line carrier across the critical seam. Neither local chart determinant nor their transition carries the Riemann divisor.

This proves a clean separation:

- the determinant-three line is the carrier;
- the completed theta/Tate object supplies a distinguished section;
- the zeros belong to that section, not to failure of the carrier transition.

## Consequences for earlier geometric proposals

The following mechanisms are now excluded as explanations of RH:

- a puncture in the determinant-three transition;
- noninvertibility of a local Euler chart;
- nontrivial line-bundle holonomy caused by Riemann zeros;
- failure of reciprocal chart sewing;
- positivity of the carrier metric alone.

All of these structures remain regular where the distinguished section may vanish.

The correct geometric picture is a regular two-chart carrier with a divisor-bearing section.

## Primitive and square obstruction

The determinant-three regularization removes the first two cyclic traces from the convergent determinant expression. They must be restored as separately typed relative boundary data.

Attempting to reconstruct the distinguished section through scalar continuation of

\[
\operatorname{Tr}L
\]

imports the zeta divisor through the continuation being explained.

The second trace

\[
\operatorname{Tr}L^2
\]

reaches its singular boundary at the critical seam. It cannot be treated as an ordinary holomorphic correction across the overlap.

Thus the carrier is source-derived and regular, while the section requires the full theta–Poisson boundary construction.

## Existing section route

The additive doubled-tail Schur realization already supplies a source-derived bilateral theta section. The global Tate–Poisson comparison is the only admissible route for placing that section on the Euler determinant line.

The remaining audit is binary:

1. If the comparison transports the distinguished section, not merely the underlying line, then section construction is complete and only orientation/conservation remains.
2. If it compares only carrier lines, the missing datum is a source-derived section comparison cell. It cannot be filled by continuing the primitive trace or fitting \(\Xi\).

No third reconstruction through the determinant-three transition is available.

## Finite falsifier

For any proposed chart-based zero mechanism, choose a point in the overlap and inspect the diagonal eigenvalues. Since neither \(p^{-s}\) nor \(p^{s-1}\) can equal \(1\) there, both regularized determinants are nonzero.

A claimed Riemann zero produced by either chart determinant or their ratio is therefore immediately mistyped.

## Disposition

The determinant-three Euler construction solves the reciprocal carrier problem and proves that the carrier is regular across the critical seam.

It cannot carry the Riemann divisor. The divisor belongs to the distinguished boundary-bearing theta section. Once the section comparison is audited, the sole unresolved RH content is the source-derived conservation or orientation law for that section.
