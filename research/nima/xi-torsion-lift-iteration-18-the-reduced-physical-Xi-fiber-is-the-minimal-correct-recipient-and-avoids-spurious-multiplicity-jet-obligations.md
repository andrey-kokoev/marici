# Xi-torsion lift iteration 18: the reduced physical Xi fiber is the minimal correct recipient and avoids spurious multiplicity-jet obligations

## Problem with the full divisor ideal

At a zero of multiplicity `m`, write locally

\[
\tau(z)=u^m v(u),
\qquad v(0)\ne0.
\]

The full scheme-theoretic fiber retains

\[
O/(u^m,\bar u^m).
\]

Even if `Re(z_0)=0`, the factor

\[
1-p^{-(z+w)}
\]

has a generally nonzero first normal jet. Hence the energy defect need not
vanish in this nonreduced quotient when `m>1`.

Demanding full scheme-theoretic vanishing therefore adds mixed multiplicity-jet
conditions not required by RH.

## Reduced physical fiber

The minimal recipient for zero location is the reduced local ideal

\[
I_{\rm red}=(u,\bar u)
=\sqrt{(\tau(z),\tau^\#(w))}
\]

at the physical pair `(z_0,bar z_0)`. In its residue fiber,

\[
[\delta_p]_{\rm red}
=
(1-p^{-2\operatorname{Re}z_0})E_p(b_{z_0}).
\]

Since the retained energy is positive,

\[
[\delta_p]_{\rm red}=0
\quad\Longleftrightarrow\quad
\operatorname{Re}z_0=0,
\]

independently of the multiplicity of the Xi zero.

## Torsion versus fiber value

Two distinct notions must not be conflated:

1. **Divisor torsion:** an ambient cokernel class `q` satisfies
   `tau^N q=0`.
2. **Fiber obstruction:** a section has nonzero image after reduction modulo
   the local divisor ideal.

The Haar residual is of the second type. It is an explicit value in the reduced
physical fiber. Proving that an unrelated holomorphic cokernel is torsion-free
does not force this value to vanish.

Conversely, vanishing of the reduced energy class at one Xi zero does not prove
all multiplicity jets required for divisibility by `tau`.

## Correct role of strictness

Strict horizontal topology is still useful for ensuring that:

- reduction commutes with cutoff completion;
- the Xi state does not collapse in the fiber;
- the positive energy evaluation remains continuous;
- no nonclosed-range artifact creates or erases the reduced class.

It makes the residual trustworthy. It does not determine its value.

## Revised three-part theorem

The strongest accurate formulation supported by the current source is:

1. the translated-history and labelled-bordered synthesis maps have strict,
   horizontal realizations in their respective graph categories;
2. `H_border` has a source-derived recoverable labelled lift;
3. the physical reduced Xi fiber of the prime energy cycle is the scalar
   `(1-p^(-2 Re z_0))E_p(b_(z_0))`.

The third item vanishes exactly on the critical line, but its vanishing is an
additional metric conservation theorem, not an equivalent reformulation of
1--2.

## Consequence for the remaining iterations

Any proposed proof should now be tested directly against the reduced-fiber
class. If it only proves holomorphic torsion-freeness, multiplicity
preservation, or labelled Evans divisibility, it does not touch the RH-bearing
scalar.