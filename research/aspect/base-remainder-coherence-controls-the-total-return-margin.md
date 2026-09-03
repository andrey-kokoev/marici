# Base–remainder coherence controls the total return margin

## Question

Once the base-lift route norm and torsor-remainder width are bounded, can source orthogonality improve the conservative triangle gate?

## Coherence bound

Let \(b\) be the complete route image of a declared base lift, and let \(Rw\) be the route variation over admissible torsor displacements. Suppose

\[
\|b\|\le q_0,
\qquad
\|Rw\|\le\gamma,
\]

and the physical target inner product satisfies the uniform coherence estimate

\[
|\operatorname{Re}\langle b,Rw\rangle|
\le
\kappa q_0\gamma,
\qquad
0\le\kappa\le1.
\]

Then

\[
\|b+Rw\|^2
\le
q_0^2+2\kappa q_0\gamma+\gamma^2.
\]

Strict confinement follows when the right side is below one.

## Two limiting routes

For \(\kappa=1\), the bound is

\[
(q_0+\gamma)^2,
\]

which recovers the triangle certificate and is saturated by coherent alignment.

For \(\kappa=0\), base and remainder images are orthogonal, giving

\[
q_0^2+\gamma^2.
\]

This can certify confinement even when \(q_0+\gamma\ge1\).

With \(q_0=3/5\) and \(\gamma=2/5\), alignment reaches unit norm, while orthogonality leaves return margin \(12/25\). A partial coherence bound \(\kappa=1/2\) leaves margin \(6/25\).

## Source gate

The coherence parameter must be proved in the physical target inner product for every admissible torsor displacement. Sector names, opposite signs, oscillatory formulas, or orthogonality of source coordinates do not imply target-route orthogonality.

A basis-free source certificate is the functional inequality

\[
|\operatorname{Re}\langle b,Rw\rangle|^2
\le
\kappa^2q_0^2\,w^*Hw
\]

on the admissibility form. Exact orthogonality is the special case \(R^*b=0\) on the torsor support.

## Base-choice boundary

Changing the base lift changes both \(b\) and the displacement set. The resulting numerical coherence bound may improve, but choosing a base to minimize it is not a physical lift selection. Any certificate must cover the full source-admissible affine set or retain the chosen base solely as a coordinate origin.

## Verification

`research/aspect/checkers/check_base_remainder_coherence.py` verifies orthogonal, partially coherent, and aligned budgets with exact rational arithmetic.

## Disposition

The combined confinement target is no longer forced to use the triangle bound. A source-derived base–remainder coherence theorem can recover strict margin, but without such a theorem coherent alignment remains admissible and the conservative sum gate is sharp.
