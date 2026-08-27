# Fourier saturation gives a canonical sewing-invariant RH boundary topology

Author: `marici.Nima`

Date: 2026-08-26

Status: exact finite topology constructor and remaining arithmetic gate

## Finite Fourier orbit

With self-dual adelic normalization, additive Fourier transport satisfies

\[
\mathcal F^2=\mathcal R,
\qquad
\mathcal F^4=I,
\]

where $\mathcal R$ is source reflection.

Therefore closing a boundary topology under Fourier transport requires only a
four-element orbit.

## Saturated seminorm

Let (q) be any source-authorized boundary seminorm. Define

\[
q_{\mathrm{sat}}(x)^2
=
\sum_{j=0}^3
q(\mathcal F^jx)^2.
\]

Then

\[
q_{\mathrm{sat}}(\mathcal Fx)
=
q_{\mathrm{sat}}(x).
\]

Thus Fourier sewing and its inverse act isometrically in the saturated
topology.

For a finite-cutoff Gramian $Q_X$, the corresponding construction is

\[
Q_{X,\mathrm{sat}}
=
\sum_{j=0}^3
(F_X^j)^*Q_XF_X^j.
\]

It satisfies

\[
F_X^*Q_{X,\mathrm{sat}}F_X
=
Q_{X,\mathrm{sat}}.
\]

## Kernel and distinction preservation

The saturated nullspace is

\[
\ker Q_{X,\mathrm{sat}}
=
\bigcap_{j=0}^3
F_X^{-j}\ker Q_X.
\]

A direction is erased only if it and all four Fourier presentations are
invisible to the original authorized observer.

This repairs the hostile topology in which one weakly observed direction is
rotated into a strongly observed direction. Saturation adds exactly the
missing conjugate observations.

## Source authority

Fourier saturation does not invent arbitrary detector rows. Every added
seminorm is the transport of an already authorized boundary seminorm by the
source Fourier constructor.

Categorically, it is the finite orbit completion of the observer under the
source (C_4) action.

This is the appropriate topology constructor for reciprocal sewing:

```text
authorized boundary observer family
  -> close under four Fourier presentations
  -> sum the transported Gramians
  -> complete only afterward
```

## Application to the singular vessel

Start with the constructor family detecting:

- primitive endpoint current;
- square endpoint current;
- seam interval state;
- connected tail;
- archimedean boundary current.

Fourier-saturate the entire typed family before forming its pro-Gram
completion. The sewing operator is then automatically continuous and
invertible on every finite cutoff and on any Hausdorff completion of these
seminorms.

The primitive exponential rigging remains part of the initial family;
saturation transports it rather than replacing it with an ordinary Hilbert
norm.

## What remains unresolved

Fourier invariance alone does not prove:

1. that arithmetic constructors are continuous in the saturated topology;
2. that finite cutoff bonding maps preserve the saturated Gramians;
3. that the completion contains the desired boundary currents;
4. that the completed feature map is injective;
5. that observability has a noncollapsing lower bound.

Prime transport may still force an infinite constructor closure even though
the Fourier orbit itself is finite.

## Minimality statement

Any Fourier-invariant seminorm family containing (q) must also contain the
four transported seminorms (q\circ\mathcal F^j). The saturated family is
therefore the smallest source-generated Fourier-stable family in the sense of
observer inclusion.

The sum Gramian is a canonical Hilbertian representative of that family, not
the only possible equivalent norm.

## Finite falsifiers

Reject a proposed sewing topology if:

- it omits one Fourier image of an authorized observer;
- its Gramian fails the invariance equation;
- it retains a null direction whose Fourier image is observed;
- cutoff bonding fails to intertwine the saturated (C_4) orbit;
- an unauthorized observer is added instead of a transported one.
