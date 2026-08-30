# Fourier-equivariant constructor bounds automatically lift to the saturated pro-Gram

## Basic lifting theorem

Let \(Q_x\) be a source-authorized Gram on a typed object \(x\), with Fourier orbit

\[
F_x^j,
\qquad
j=0,1,2,3.
\]

Define

\[
Q_{x,\mathrm{sat}}
=
\sum_{j=0}^{3}
(F_x^j)^{*}Q_xF_x^j.
\]

Let \(S:x\to y\) be an admitted constructor. Suppose \(S\) is Fourier-natural:

\[
F_yS=SF_x,
\]

and bounded in the unsaturated source Grams:

\[
S^{*}Q_yS
\le
C_S^2Q_x.
\]

Then

\[
S^{*}Q_{y,\mathrm{sat}}S
=
\sum_{j=0}^{3}
(F_y^jS)^{*}Q_y(F_y^jS)
\]

becomes

\[
S^{*}Q_{y,\mathrm{sat}}S
=
\sum_{j=0}^{3}
(SF_x^j)^{*}Q_y(SF_x^j)
\le
C_S^2Q_{x,\mathrm{sat}}.
\]

Thus Fourier saturation introduces no new operator-norm loss.

## Twisted naturality

Typed Adams operations may not commute literally with Fourier transport. It is enough that they permute the finite Fourier orbit through authorized comparison cells:

\[
F_y^jS
=
U_{j,S}S_jF_x^{\pi_S(j)},
\]

where:

- \(\pi_S\) is a permutation of the four presentations;
- \(S_j\) is the correctly typed conjugate constructor;
- \(U_{j,S}\) is source-unitary, or uniformly bi-bounded.

If

\[
S_j^{*}Q_yS_j
\le
C^2Q_x
\]

uniformly in \(j\), then the saturated bound follows with the additional fixed comparison-cell bound. Since the orbit has only four elements, no depth growth arises from Fourier saturation itself.

## Cutoff bonding

For a bonding map \(B_{X\to Y}\), exact naturality

\[
F_YB_{X\to Y}
=
B_{X\to Y}F_X
\]

and unsaturated Gram compatibility imply saturated compatibility term by term.

Therefore cutoff preservation of the saturated pro-Gram is not an independent analytic estimate. It is a finite naturality audit of the four transported source Grams.

## Lower observability

Because the identity presentation is one summand,

\[
Q_{x,\mathrm{sat}}\ge Q_x.
\]

Any lower bound

\[
Q_x\ge c\,G_x
\]

passes directly to \(Q_{x,\mathrm{sat}}\). More generally, saturation can remove null directions by intersecting the four transported kernels.

Uniform lower observability still requires a source metric \(G_x\) compatible with the constructor family. Saturation cannot repair a lower bound that collapses simultaneously in all four presentations.

## Semigroup control

For constructor words, the saturated norm estimate composes exactly as the unsaturated estimates. Hence the previously identified composite-growth problem remains, but saturation does not worsen it.

Two sufficient regimes are:

- the conjugate constructor semigroup is uniformly bounded;
- Euler half-density contraction dominates its word growth.

The intensive-order theorem separately controls escape along infinite Adams rays.

## Concrete audit

The nine-operation domain now needs, for each generator:

1. its unsaturated source-Gram bound;
2. its Fourier naturality or four-cell permutation law;
3. bounds on the comparison cells;
4. cutoff compatibility;
5. word-level growth after Euler weights.

There is no need to estimate the saturated Gram from scratch.

## Hostiles

A constructor can be bounded in \(Q\) but send \(FQ\)-visible data into a \(Q\)-dark direction; without naturality, its saturated norm may blow up.

Generatorwise Fourier comparison cells can be bounded while their word composites amplify. The finite orbit prevents Fourier-index growth, not constructor-depth growth.

A cutoff map may commute with scalar Fourier shadows but fail on one typed boundary port, breaking the pro-Gram system.

## Frontier

The saturated completion problem has reduced to existing constructor data:

> Prove Fourier naturality and unsaturated bounds for each admitted generator, then audit the weighted word semigroup.

The earliest unresolved generator remains the Adams type edge only insofar as its full Fourier comparison cell has not been supplied. Local history boundedness itself is already closed.
