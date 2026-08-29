# The independent boundary factors are incidence lifts, not rank-one decompositions

## Source-derived primitive and square maps

The arithmetic source already fixes the two incidence maps before any mixed operator is known:

\[
I_1:(p,1)\longmapsto p^{-1/2}\delta_{\log p},
\]

and

\[
I_2:(p,2)\longmapsto \frac12p^{-1}\delta_{2\log p}.
\]

They have different target topologies:

- \(I_1\) lands in the exponentially weighted primitive current rigging;
- \(I_2\) lands in the tempered, non-finite square measure rigging.

Therefore the two boundary factors cannot be chosen as arbitrary vectors in one Hilbert space.

## Two-chart lifts

Let \(\iota_{p,1}\) and \(\iota_{p,2}\) denote the source comoving lifts from observed atoms to the two-front, two-sheet correspondence. The independently typed candidate factors are

\[
L_{P,p}=\iota_{p,1}I_{1,p},
\qquad
L_{Q,p}=\iota_{p,2}I_{2,p}.
\]

At the labelled level their coefficients are fixed:

\[
L_{P,p}\sim p^{-1/2},
\qquad
L_{Q,p}\sim \frac12p^{-1}.
\]

Their chart support and sheet orientation are fixed by

\[
u=q-\varepsilon k\log p
\]

and by the oriented zero-section sign \(\varepsilon\).

No normalization may be moved freely between \(L_P\) and \(L_Q\): doing so changes the primitive and square source currents even when their product remains unchanged.

## The missing Green/Stokes identity

Let

\[
\partial\mathscr C_p
=
e_{\mathrm{out}}-e_{\mathrm{in}}.
\]

The required theorem is the source identity

\[
b_{\alpha,p}(x,y)
=
\left\langle
L_{Q,p}^*y,\,
\partial\mathscr C_p\,L_{P,p}^*x
\right\rangle_{\mathrm{rel}}.
\]

The relative pairing must retain the wall coordinate and use the source test-dual pairing before any Hilbert realization.

This identity would simultaneously prove:

- wall-antisymmetric character;
- primitive-to-square orientation;
- rank at most one on one adjacent cell;
- the exact coefficient normalization;
- compatibility with the independently derived current maps.

## Why ordinary rank factorization is insufficient

Suppose a finite mixed matrix has rank one:

\[
B=uv^*.
\]

For every nonzero scalar \(c\),

\[
B=(cu)(c^{-1}v)^*.
\]

Thus rank-one support does not identify either factor. A fitted decomposition can satisfy

\[
P_sB=0
\]

while disagreeing with both \(L_{P,p}\) and \(L_{Q,p}\).

The source theorem must compare the fitted factors with the incidence lifts individually, not only compare their product.

## Factor normalization audit

At one prime, write a candidate decomposition as

\[
B_{\alpha,p}
=
\widetilde L_{Q,p}\,
\partial\mathscr C_p\,
\widetilde L_{P,p}^*.
\]

Require source intertwiners

\[
\widetilde L_{P,p}=U_{P,p}L_{P,p},
\qquad
\widetilde L_{Q,p}=U_{Q,p}L_{Q,p},
\]

where \(U_{P,p},U_{Q,p}\) are authorized chart changes preserving the source current norms and orientations.

An arbitrary reciprocal rescaling

\[
\widetilde L_{P,p}=c_pL_{P,p},
\qquad
\widetilde L_{Q,p}=c_p^{-1}L_{Q,p}
\]

is forbidden unless \(c_p\) is an authorized gauge acting isometrically on both typed riggings.

## Cancellation hostile

Choose

\[
\|\widetilde L_{P,X}\|\to\infty,
\qquad
\|\widetilde L_{Q,X}\|\to0,
\]

while

\[
\widetilde L_{Q,X}\partial\widetilde L_{P,X}^*
\]

remains bounded. The mixed product passes every operator-norm test, but the primitive factor loses completion continuity and the square factor loses a lower frame bound.

Therefore completion requires separate estimates:

\[
\sup_X\|L_{P,X}\|<\infty,
\qquad
\sup_X\|L_{Q,X}\|<\infty,
\]

and the corresponding inverse or lower-bound controls on their source supports. Product boundedness is insufficient.

## Finite audit order

For one adjacent prime cell:

1. construct \(I_{1,p}\) and \(I_{2,p}\);
2. lift them to \(L_{P,p}\) and \(L_{Q,p}\) on the comoving charts;
3. verify cutoff and reciprocal naturality of each lift;
4. derive the relative Green/Stokes identity;
5. test radical annihilation;
6. derive antisymmetric rank-one support;
7. prove closability on the original rigged spaces;
8. bound both factors separately through completion.

## Current frontier

The independent factors are no longer abstract unknowns: their arithmetic coefficients, current grades, chart locations, and sheet signs are source-fixed by the primitive and square incidence maps.

What is still absent is the relative Green/Stokes identity coupling those exact lifts through the oriented boundary cell. That identity—not existence of some rank-one factorization—is the next irreducible source theorem.
