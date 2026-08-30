# Theta silent endpoint shear does not silence reciprocal path energy

## Endpoint silence

For a source (f\in L^2(0,L)), the finite transfer shear is

\[
 S_L(s)=\begin{pmatrix}1&F_L(s)\\0&1\end{pmatrix},
 \qquad
 F_L(s)=\int_0^L f(v)e^{sv}\,dv.
\]

At a transmission zero,

\[
 F_L(s)=0,
 \qquad
 S_L(s)=I.
\]

Thus the completed endpoint comparison records no displacement.

## Internal reciprocal energy

Let

\[
 T(q)=\int_q^L|f(v)|^2\,dv,
 \qquad
 R(q)=\int_0^q|f(v)|^2\,dv.
\]

The two reciprocal Mellin orientations have combined energy

\[
 E_\delta(q)
 =2\cosh(2\delta q)\|f\|_{L^2(0,L)}^2.
\]

Therefore

\[
 E_\delta(L)-E_\delta(0)
 =2\bigl(\cosh(2\delta L)-1\bigr)
 \|f\|_{L^2(0,L)}^2.
\]

For nonzero (f), this is strictly positive whenever (\delta\ne0). The
formula does not depend on (F_L(s)). In particular, it remains strictly
positive at every off-seam transmission zero.

## Exact no-go

Silent endpoint transfer does not imply zero reciprocal boundary supply.
Hence no dynamic energy law whose supply depends only on the total shear, its
off-diagonal coefficient, or its endpoint displacement can couple scalar
zeros to the seam-selective positive energy.

Two source paths can have the same identity endpoint shear and different
internal energies. The transfer coefficient retains a first-order integral of
the source, while the reciprocal energy retains quadratic path information.
The latter cannot be reconstructed from the former.

## Gramian cocycle interpretation

Kitaev's path-observability theorem gives the correct compositional type. For
segment transport (S_{a,b}) and source-authorized observation Gramian
(W_{a,b}), concatenation obeys

\[
 W_{a,c}
 =W_{a,b}+S_{a,b}^*W_{b,c}S_{a,b}.
\]

This twisted additive cocycle remembers internal observation energy even when
the total endpoint shear is the identity. The theta reciprocal energy must be
realized as such a path-level Gramian, with observation rows derived from the
tail, seam, primitive, square, and archimedean channels.

The scalar shear is therefore a first-level quotient of the required object.
The missing RH information lives at the quadratic Gramian level or higher.

## Revised RH gate

A viable source identity must retain both:

1. the shear cocycle carrying the scalar transmission coefficient; and
2. the positive Gramian cocycle carrying faithful internal relationship
   energy.

It must then derive a boundary-current law coupling them without reducing the
Gramian to an endpoint function. Completion stability requires a uniform lower
bound on the source-authorized Gramian; finite positivity alone is
insufficient.

## Falsifier

Any endpoint-only coupling is falsified by a nonzero source with
(F_L(s)=0) and (\delta\ne0), because its shear is the identity while its
reciprocal energy change is positive. A proposed Gramian coupling fails if its
sensor rows are not source-derived or if its smallest normalized energy tends
to zero with the cutoff.

## Scope

This proves that scalar silence and reciprocal path-energy silence are
independent at finite cutoff and types the missing coupling as a positive
Gramian cocycle. It does not derive the full theta/Tate sensor family, prove a
uniform observability bound, or prove RH.
