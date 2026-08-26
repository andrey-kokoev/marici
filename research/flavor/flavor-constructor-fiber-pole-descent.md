# Constructor-fiber pole descent

Work package: WP558  
Owner: marici.Figueiredo

## Question

Can the missing WP557 map from `physical16` to an internal pole realization
be defined without restricting or labelling the UV constructor?

## Descent criterion

Let a source domain \(S\) carry maps

\[
L:S\longrightarrow\mathrm{physical16},
\qquad
Q:S\longrightarrow\mathcal P,
\]

where \(Q\) records pole or threshold structure. A map
\(\phi:\mathrm{physical16}\to\mathcal P\) satisfying \(Q=\phi\circ L\)
exists only if \(Q\) is constant on every fiber of \(L\). In the linear local
form this is

\[
\ker L\subseteq\ker Q.
\]

## Exact WP129 hostile

WP129 freezes three inequivalent constructors with the same low-energy packet:
two renormalizable adjoints, one auxiliary adjoint, and direct EFT contact.
Their common low-energy response has rank one and kernel dimension two. Their
formal threshold signatures have rank three. In exact normal form,

\[
L=(1,1,1),
\qquad
Q=I_3.
\]

The displacement \((1,-1,0)^T\) has zero low-energy response and nonzero pole
response. Therefore the pole record does not descend through the shared
low-energy record on this bounded rival family.

## Consequence for WP556 and WP557

WP556's six-state Gramian remains valid inside its chosen pole realization.
WP558 denies a constructor-independent promotion from generic `physical16` to
that internal state. The source class must first be restricted by independent
authority or a constructor label must be added.

Adding a constructor or threshold reference port changes the experiment. Its
objects are pairs of low-energy records and source references, and its
equivalences preserve that reference. It does not reveal a unique constructor
already encoded in the original `physical16` experiment.

Threshold signatures separate the frozen family algebraically, but WP129 has
no admitted physical threshold instrument. Even a faithful threshold
instrument would identify constructors rather than select a numerical
\(g_Ff/v\) without a separate source law.

The smallest exact falsifier is \((1,-1,0)^T\), which lies in the low-energy
kernel but not the pole kernel.

## Status

WP558 closes the generic reverse-map branch negative. A `physical16`-to-pole
map is constructor-relative, not a function on the unrestricted low-energy
quotient.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp558_constructor_fiber_pole_descent.py

The generated result is
research/flavor/results/wp558_constructor_fiber_pole_descent.json.
