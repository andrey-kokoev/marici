# The Small Theta Tail Carries the Entire Seam-Derivative Repair

## Primitive derivative

The primitive positive-chamber profile is

\[
\phi_1(u)
=
2\pi e^{5u/2}
\left(2\pi e^{2u}-3\right)e^{-\pi e^{2u}}.
\]

Its logarithmic derivative at the seam is

\[
\frac{\phi_1'(0)}{\phi_1(0)}
=
\frac52
+
\frac{4\pi}{2\pi-3}
-
2\pi.
\]

Equivalently,

\[
2(2\pi-3)
\frac{\phi_1'(0)}{\phi_1(0)}
=
30\pi-15-8\pi^2.
\]

This quantity is nonzero and positive. Thus

\[
\phi_1'(0)>0.
\]

## Completed seam cancellation

Write

\[
\Phi=\phi_1+\tau,
\qquad
\tau=\sum_{n\ge2}\phi_n.
\]

The completed theta source is even, so

\[
\Phi'(0)=0.
\]

Consequently

\[
\tau'(0)=-\phi_1'(0).
\]

Although

\[
0<\tau(u)<0.006001\,\phi_1(u)
\]

in value on the entire positive chamber, the tail carries one hundred
percent of the derivative needed to repair the primitive seam mismatch.

## High-frequency consequence

For a smooth profile \(f\) on \([0,L]\), repeated integration by parts gives

\[
\int_0^Lf(u)\cos(xu)\,du
=
\frac{f(L)\sin(xL)}x
+
\frac{f'(L)\cos(xL)-f'(0)}{x^2}
+
O(x^{-3}).
\]

The primitive and completed sources therefore have different
high-frequency boundary structure:

- the primitive transform contains the seam term
  \(-\phi_1'(0)/x^2\);
- the completed transform has no seam-derivative term because
  \(\Phi'(0)=0\).

The small tail cancels that entire leading channel. Pointwise value
dominance cannot control this cancellation.

## Correction to the perturbative programme

The primitive near-collision localization remains valid at finite
frequencies because it uses absolute integral bounds. But a global
primitive-plus-small-tail proof cannot obtain its high-frequency regime from
value dominance alone.

The reference object must be seam-matched before perturbation. At minimum it
must retain enough higher-label boundary data to reproduce

\[
\Phi'(0)=0.
\]

More generally, an order-\(r\) high-frequency argument needs the completed
boundary jet through the corresponding order. A component small in function
value can be leading in a cancelled boundary derivative.

This is the exact mechanism behind the programme's repeated warning that
completion must precede compression.

## Next target

Construct the smallest seam-matched reference packet consisting of:

1. the primitive profile;
2. one typed boundary-jet repair coordinate carrying
   \(-\phi_1'(0)\);
3. the remaining value-small and jet-small tail.

Then redo the collision reserve with a norm controlling both bulk mass and
the repaired endpoint jet.

## Falsifier

Any primitive-dominance proof fails if it estimates only
\(\tau/\phi_1\) while using high-frequency integration by parts. It must also
account for the exact derivative identity
\(\tau'(0)=-\phi_1'(0)\).
