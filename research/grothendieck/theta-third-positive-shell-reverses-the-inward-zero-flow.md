# Theta third positive shell reverses the inward zero flow

## Bounded question

Does the monotone seam-attracting motion of the two-shell model survive the
next positive source shell?

## Base hostile zero

Let

\[
F_c(z)=\cosh z+c\cosh 2z,
\qquad
0<c<1.
\]

Its right-half-plane hostile zero has the form

\[
z_0=a+i\pi,
\qquad
a>0.
\]

The zero equation gives

\[
c=\frac{\cosh a}{\cosh 2a}.
\]

At this zero,

\[
F_c'(z_0)
=
-\sinh a+2c\sinh 2a
=
\sinh a
\frac{2\cosh^2a+1}{\cosh 2a}
>0.
\]

## Add the third positive shell

Consider the positive deformation

\[
F_{c,\varepsilon}(z)
=
F_c(z)+\varepsilon\cosh 3z,
\qquad
\varepsilon\ge0.
\]

For the simple zero branch (z(\varepsilon)) through (z_0), implicit
differentiation yields

\[
z'(0)
=
-\frac{\cosh 3z_0}{F_c'(z_0)}.
\]

Since

\[
\cosh(3a+3i\pi)=-\cosh 3a<0,
\]

one obtains

\[
z'(0)>0.
\]

The velocity is real and points away from the seam. The third positive shell
therefore falsifies atomwise monotone inward transport at first order.

## Parity law at the hostile branch

More generally, adding a positive shell \(\varepsilon\cosh kz\) gives

\[
z_k'(0)
=
-\frac{(-1)^k\cosh ka}{F_c'(z_0)}.
\]

Thus even shell indices move this branch inward, while odd shell indices move
it outward. Positivity alone leaves an alternating orientation after spectral
transport.

## Meaning

The inward motion found in the two-shell family was real but not stable under
independent positive completion. It depended on the parity of the added shell
at the relevant phase.

Any surviving theta divisor-flow law must therefore act on canonical source
blocks whose alternating spectral phases have already been coherently paired.
The likely primitive is not one positive shell but a modularly sewn block with
an oriented net velocity.

For a block deformation (H_B), the exact velocity gate is

\[
\operatorname{Re}z_0
\operatorname{Re}
\left(
-\frac{H_B(z_0)}{F'(z_0)}
\right)
\le0.
\]

The block and its order must be derived from theta labels before evaluating
this ratio.

## Result

The atomwise seam-attraction conjecture is false at the third positive shell.
The failure exposes the missing structure more precisely: source positivity
must be transported together with a coherent parity or modular orientation.

The next target is a canonical paired-shell or Poisson-sewn completion block
whose combined zero velocity is inward even though its individual summands
alternate.

## Sharp falsifier

The deformation by (cosh 3z) at any hostile two-shell zero
(a+i\pi) has positive horizontal velocity. Any atomwise positive-completion
law accepts this deformation and is false.
