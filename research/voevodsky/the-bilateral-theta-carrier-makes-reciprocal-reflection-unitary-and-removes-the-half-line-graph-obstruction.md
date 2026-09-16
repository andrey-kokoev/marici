# The bilateral theta carrier makes reciprocal reflection unitary and removes the half-line graph obstruction

## Bilateral state space

Let

\[
W(u)=
\Phi(|u|)
\]

and define

\[
\widehat{\mathcal H}_\Phi
=
L^2(\mathbb R,W(u)du).
\]

The reflection operator

\[
(Rf)(u)=f(-u)
\]

is a unitary involution because \(W\) is even:

\[
R^*=R,
\qquad
R^2=I.
\]

For every spectral parameter \(s\),

\[
R(e^{-su})=e^{su}.
\]

Thus reciprocal analytic reflection, which is unbounded when represented as a map between two copies of the positive half-line carrier, becomes a fixed unitary on the bilateral carrier.

## Bilateral transport

Take

\[
Af=-f'.
\]

There is no endpoint boundary term on the full line. Its weighted adjoint is

\[
A^*f
=
f'
+
\frac{W'}{W}f,
\]

so

\[
A^*+A
=
M_q,
\qquad
q(u)=
\frac{W'(u)}{W(u)}.
\]

Since \(W\) is even, \(q\) is odd and

\[
RqR=-q.
\]

Equivalently,

\[
R(A^*+A)R
=-
(A^*+A).
\]

The two opposite distributed signatures are now the two reflection polarities of one bilateral transport system, rather than unrelated half-line sheets.

## Clark observations

For

\[
e_s(u)=e^{-su},
\]

the completed even transform is

\[
X(z)
=
\frac12
\int_{\mathbb R}
W(u)e^{-su}
\,du,
\qquad
s=-iz.
\]

The Clark functions are the bilateral moment observations

\[
E(z)
=
\frac12
\int_{\mathbb R}
(1-u)W(u)e^{-su}
\,du,
\]

\[
E^*(z)
=
\frac12
\int_{\mathbb R}
(1+u)W(u)e^{-su}
\,du.
\]

Reflection exchanges the observation vectors:

\[
R(1-u)=1+u.
\]

Hence

\[
E^*(z)
\]

is the reflected output of the same bilateral state, not the output of an independently growing half-line state.

## Control interpretation

The correct reciprocal controller is dynamic only in the half-line chart. On the bilateral dilation it is the unitary symmetry \(R\).

This removes the norm obstruction

\[
e^{-su}\mapsto e^{su}
\]

because both sections have exactly equal bilateral norm:

\[
\|e^{-su}\|_{
\widehat{\mathcal H}_\Phi}
=
\|e^{su}\|_{
\widehat{\mathcal H}_\Phi}
\]

for real \(s\), by reflection.

## Remaining positivity problem

The bilateral Green form is still indefinite:

\[
2\operatorname{Re}
\langle Af,f\rangle
=
\int_{\mathbb R}
q(u)|f(u)|^2W(u)du.
\]

Reflection reverses this form. Therefore unitary reciprocal implementation does not itself select a positive orientation.

The required positive quotient must choose a maximal graph or Hardy polarization compatible with:

1. the unitary reflection \(R\);
2. the transport generator \(A\);
3. the Clark observation pair \(1-u,1+u\);
4. the physical exponential sections.

This is a better-typed problem than bounded reflection on the half-line because all physical sections and symmetries now inhabit one Hilbert carrier.

## Candidate next constructor

Let

\[
P_\pm
=
\frac12(I\pm R)
\]

be the even and odd reflection projections. The transport interchanges parity because

\[
RA=-AR.
\]

The next operator calculation is the block form of \(A\) and \(M_q\) relative to

\[
\widehat{\mathcal H}_\Phi
=
P_+\widehat{\mathcal H}_\Phi
\oplus
P_-\widehat{\mathcal H}_\Phi.
\]

A positive realization would require a contractive graph from one parity sector to the other whose boundary observation is the Clark ratio.

## Disposition

The half-line unbounded-reflection obstruction is a chart artifact. Bilateral theta dilation supplies an exact unitary reciprocal constructor. The unresolved issue is no longer implementation of reflection, but positive Hardy/parity polarization of the bilateral Green form.
