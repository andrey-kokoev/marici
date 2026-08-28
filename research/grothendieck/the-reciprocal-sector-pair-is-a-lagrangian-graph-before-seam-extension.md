# The Reciprocal Sector Pair Is a Lagrangian Graph Before Seam Extension

## Product versus correspondence

Let \((V,\omega)\) be the one-mode theta phase space and let

\[
R:V\longrightarrow V
\]

be the Fourier–Tate symplectic transport. The two reciprocal presentations
are not initially two freely chosen points of \(V\times V\). Their compatible
pairs lie on the graph

\[
\Gamma_R=\{(x,Rx):x\in V\}.
\]

The correct doubled correspondence space carries the difference form

\[
\omega\oplus(-\omega).
\]

Because \(R\) is symplectic, its pullback to the graph vanishes:

\[
\omega(x,y)-\omega(Rx,Ry)=0.
\]

The graph has half the dimension of \(V\oplus V\), so it is Lagrangian.

Thus the two sectors are two typed presentations of one canonical state
before seam extension. Treating them as independent oscillator modes at this
stage overcounts the source.

## Collapse of the ambient quadratic controls

The ambient doubled phase space has ten quadratic symbols, whose Hamiltonian
algebra is \(\mathfrak{sp}_4\). Restriction to \(\Gamma_R\) substitutes the
second-sector coordinates by linear functions of the first. Every restricted
quadratic therefore belongs to

\[
\operatorname{Sym}^2(V^*),
\]

which has dimension three. Exact rank computation gives

\[
10\longrightarrow3.
\]

Neither the second local triple nor the four mixed quadratics remain
independent on the graph. The bulk compatible-pair object therefore retains
only the original one-mode `sp2`, equivalently `sl2`, quadratic control.

## Where sp4 can re-enter

The seam has already been shown not to be reconstructible from the retained
tail. This means the completed object need not remain the bare graph. An
independent seam state can supply transverse information, geometrically a
normal or conormal direction to \(\Gamma_R\).

The corrected architecture is:

```text
Fourier-related bulk sectors -> Lagrangian graph -> one sl2
independent seam extension   -> transverse directions -> possible sp4 closure.
```

Hence the four mixed controls are not bulk seam observables waiting to be
noticed. They are operators that require a genuine transverse seam extension
before they become independent.

## Explanation

This realizes the recurring phrase “one thing that looks like two things.”
The plus and minus half-planes are distinct typed charts, but Fourier–Tate
coherence places their compatible states on one Lagrangian graph. The loss of
meaning occurs when scalar projection forgets whether a state lies on the
graph or has acquired a transverse seam component.

## Falsifier and next gate

The graph theorem fails if the completed sector values can vary independently
while holding their common source fixed, or if Fourier–Tate transport is not
symplectic in the declared boundary form.

The next gate is to construct the seam extension as a source-derived normal
bundle or relative complex and determine its rank. Only then can one decide
whether the endpoint `sp4` module is the correct completed theta target.
