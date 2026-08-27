# The linear Fourier tail cell has five components

## Correction being tested

The Gaussian-tail calculation exposed Gaussian bulk, one-sided tail, delta,
and principal-value ports. Can those four roles form a linear object closed
under Fourier transform and reflection?

They cannot. The relation

\[
H(q)+H(-q)=1
\]

forces the constant carrier into every reflection-stable linear span
containing \(H\). Fourier transform then exchanges that constant with the
delta atom. The constant is therefore not merely a scalar equation among the
other ports; it is an independent linear coordinate required for closure.

## Centered tail basis

Set

\[
K=H-\frac12
\]

and let

\[
V=\mathcal F K
=\frac{i}{2\pi}
\operatorname{pv}\left(\frac{e^{-\pi\xi^2}}{\xi}\right).
\]

Use the five typed components

\[
(\phi,1,\delta_0,K,V).
\]

Their Fourier action is

\[
\mathcal F\phi=\phi,
\qquad
\mathcal F1=\delta_0,
\qquad
\mathcal F\delta_0=1,
\qquad
\mathcal FK=V,
\qquad
\mathcal FV=-K.
\]

Thus Fourier transport splits into three exact blocks:

1. a fixed Gaussian bulk line;
2. a constant–delta exchange plane;
3. an odd tail–principal-value quarter-turn plane.

The square of Fourier transform is reflection: it fixes the first three
components and negates the last two. Its fourth power is the identity.

## Why the fifth component is unavoidable

Omitting the constant fails because Fourier sends \(\delta_0\) to it.
Omitting the delta fails because Fourier sends the constant to it. Omitting
either member of the odd plane fails because Fourier quarter-turns between
them. Omitting the Gaussian bulk discards the source vacuum whose tail
created the cell.

The earlier four-role description was therefore affine: it allowed the
constant to be reconstructed by adding opposite tail orientations. A
category of linear source objects cannot leave that reconstruction outside
the object. Linearization creates the fifth wall.

## Geometric-algebra interpretation

The odd plane carries a genuine complex structure because Fourier squares to
minus one there. The constant–delta plane is an involutive exchange pair.
The Gaussian line is fixed. These are three different representation types,
so one scalar norm or one undifferentiated boundary label would erase the
transport law.

This is the source-native meaning of the additional comparison channel: it
is not another measurement of the same state. It is the unit carrier needed
to linearize the affine relation between the two tail orientations.

## Remaining obstruction

This five-component span is closed under Fourier and reflection, but not yet
under arbitrary differentiation. Differentiating \(\delta_0\) creates delta
jets, while differentiating the principal-value port creates higher boundary
distributions. Therefore Clark or spectral differentiation must be typed as
a morphism into a jet-prolonged object, not assumed to be an endomorphism of
the five-component cell.

The next falsifier is exact: if the required doubled Green construction uses
only first tail differentiation, the five-cell may suffice; if its authorized
constructor algebra differentiates the Fourier boundary repeatedly, an
infinite jet tower is forced.

## Result

The minimal linear Fourier/reflection closure of the Gaussian tail has five
components. The fifth is the constant carrier paired with the delta boundary.
The next gate is whether the actual theta/Tate constructor repertoire stops
at this finite cell or forces its infinite jet prolongation.
