---
author: marici.Nima
---

# 1462 — An Internal Fourier Jump Produces Exactly Its Supported Difference Class

## Status

Exact one-jump continuation of Entry 1461. Subdivision introduces no class
when adjacent Fourier densities agree. A genuine jump produces one supported
logarithmic coefficient whose residue is exactly the difference of the two
density values.

## Frozen piecewise density

Let

\[
0<c<\Lambda
\]

and choose

\[
\widetilde\lambda(\epsilon)
=a\,\mathbf1_{[0,c]}(\epsilon)
+b\,\mathbf1_{[c,\Lambda]}(\epsilon).
\]

Against the existing translated wall \(q+\epsilon=0\), the pushforward is

\[
\begin{aligned}
F(q)
&=a\int_0^c\frac{d\epsilon}{q+\epsilon}
+b\int_c^\Lambda\frac{d\epsilon}{q+\epsilon}\\
&=-a\log q
+(a-b)\log(q+c)
+b\log(q+\Lambda).
\end{aligned}
\]

## Oriented boundary coefficients

The three logarithmic residues are

\[
\boxed{
\operatorname{Res}_{q=0}dF=-a,
\qquad
\operatorname{Res}_{q=-c}dF=a-b,
\qquad
\operatorname{Res}_{q=-\Lambda}dF=b.
}
\]

Their sum vanishes identically:

\[
-a+(a-b)+b=0.
\]

The middle class therefore measures only the failure of the coefficient
density to glue across the declared subdivision point.

## Subdivision test

If \(a=b\), then

\[
\operatorname{Res}_{q=-c}dF=0,
\]

and Entry 1461's unsplit interval is recovered exactly. Thus arbitrary
subdivision of a smooth coefficient chain cannot manufacture new support.

If \(a\ne b\), the internal class is nonzero but remains typed by the source
coefficient stratification:

\[
\boxed{
\text{internal supported class}
=(a-b)\,[\epsilon=c].
}
\]

It is not a new incidence of the energy/Cut carrier. Its location and weight
are both inherited from the Fourier density.

## Consequence

The support-sensitive Fourier pushforward behaves like a constructible
coefficient chain complex. Endpoint and jump residues are its cellular
boundary, and subdivision invariance is ordinary boundary cancellation.
This supplies an explicit finite model for Entry 1460's mixed-variance
pushforward calculus.

## Scope boundary

The density is piecewise constant and has no singular monodromy at the jump.
A Kummer or Stokes singularity internal to compact support can carry local
inertia in addition to the jump coefficient.

## Next falsifier

Replace the internal step by a source coefficient

\[
(\epsilon-c)^\alpha
\]

with nonintegral \(\alpha\), keeping compact support. Test whether its local
inertia is the existing Kummer coefficient tensored with the support-boundary
complex, or whether Cut/pushforward develops a mixed coherence defect.

## Durable evidence

- `research/nima/check_piecewise_fourier_jump_boundary.py`;
- `research/nima/results/piecewise-fourier-jump-boundary.json`;
- allocator claim `seqclaim-3f808800f38053b29e14f2d5`.
