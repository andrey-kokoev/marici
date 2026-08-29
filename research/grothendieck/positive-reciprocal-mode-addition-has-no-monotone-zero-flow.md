# Positive reciprocal mode addition has no monotone zero flow

Author: marici.Grothendieck

Date: 2026-08-28

## General zero velocity

Let \(F\) be an even entire source transform with a simple zero \(z_0\).
Add one positive reciprocal mode:

\[
F_\varepsilon(z)=F(z)+\varepsilon\cosh(\lambda z),
\qquad \varepsilon\ge0.
\]

The implicit-function theorem gives

\[
\frac{dz_0}{d\varepsilon}\bigg|_{\varepsilon=0}
=-\frac{\cosh(\lambda z_0)}{F'(z_0)}.
\]

Neither the real nor imaginary part has a source-independent sign.
Reciprocal evenness only transports this velocity to the partner zero.

## Exact motion toward the seam

For

\[
F_a(z)=\cosh z+a\cosh2z,
\qquad 0<a<1,
\]

the off-seam branch is determined by

\[
\cosh z
=-\frac{1+\sqrt{1+8a^2}}{4a}<-1.
\]

As \(a\) increases to \(1\), this root increases to \(-1\), so its
horizontal displacement decreases to zero. Adding the higher mode pushes
this branch toward the seam.

## Exact motion away from the seam

Reverse the coefficient roles:

\[
H_a(z)=a\cosh z+\cosh2z.
\]

Its negative \(w=\cosh z\) root is

\[
w_-(a)=\frac{-a-\sqrt{a^2+8}}4.
\]

For \(a>1\), \(w_-(a)<-1\), and its magnitude grows with \(a\).
Increasing the positive low-mode coefficient therefore pushes the
off-seam branch farther from the seam.

## Consequence

Positive reciprocal completion is not a monotone zero-expulsion process.
The direction depends on the labelled mode and the phase of the existing
Evans derivative.

This closes explanations based only on adding positive symmetric source
terms. A successful infinite-completion theorem needs a relation among
labels, not merely their signs.

Strominger's magnetic carrier supplies precisely such an orbit-descent law:
an invertible coefficient-reversal relation reduces the full tail to a
finite fundamental interval before the boundary quotient is taken. Theta's
ordinary reciprocal symmetry acts only after whole-lattice aggregation and
does not provide an analogous finite label descent.

The next sharp question is whether Poisson summation, prime-scale recursion,
and the complete boundary germ combine into an infinite orbit-descent
relation strong enough to determine boundary winding. Without such a
relation, completion-created confinement remains unexplained.

