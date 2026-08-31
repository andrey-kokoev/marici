# The uniform Cayley impedance gap overcoerces the seam and cannot carry the Xi divisor

> **Three-port scope correction.** The successor packet
> `the-strict-cayley-law-overcoerces-the-square-source-block-but-remains-valid-as-the-three-port-complement.md`
> shows that this no-go applies to the square arithmetic/history block treated
> as the whole pencil. In the minimal three-port system, the strict Cayley law
> controls only the arithmetic complement; the zero-diagonal theta coordinate
> can still carry a seam defect.

## Boundary value of the Schur margin

The prime-delay coefficient contains the fixed half-density factor

\[
|S_p(x)|=p^{-1/2}
\]

for real centered parameter \(x\).  Hence the direct sum retains

\[
\|S_{\rm ar}(x)\|
=
2^{-1/2}<1
\]

on the critical seam itself.

Its Cayley transform therefore satisfies the same strict boundary gap

\[
\operatorname{Im}\Theta_{\rm ar}(x)
\ge
(3-2\sqrt2)I.
\]

The gap does not collapse as the seam is approached.

## Addition with the same passive sign

If the history Weyl return has the same nonnegative imaginary-part convention,
then

\[
\operatorname{Im}
\bigl(
\Theta_{\rm ar}(x)+M_H(x)
\bigr)
\ge
(3-2\sqrt2)I
\]

wherever the boundary value is defined.

Thus the paired characteristic remains invertible on the seam as well as in
both open half-planes. It has no kernel states anywhere in the completed
strip.

## Divisor contradiction

The Xi section has nontrivial zeros. A pencil that is uniformly invertible on
the seam cannot satisfy a divisor-preserving identity

\[
\det_{\rm rel}M_U(z)=E(z)\xi(s)
\]

with \(E\) nowhere zero and with determinant zeros equivalent to pencil
kernels.

Assigning the analytically continued Euler scalar to the determinant line of
this invertible pencil would reproduce a scalar coordinate but not its kernel
divisor. It would repeat the line-section versus trivialization error.

## Source of overcoercivity

The half-density coefficient \(p^{-1/2}\) makes every local delay a strict
contraction even on the seam. The Cayley transform converts that strictness
into a uniformly positive impedance reservoir. Adding another passive
impedance with the same sign can only strengthen the gap.

This architecture is therefore a valid zero-free passive comparison system,
not a candidate Xi spectral pencil.

## Alternatives and their costs

A divisor-bearing characteristic requires at least one of the following:

1. **Lossless seam limit.** The arithmetic scattering network must acquire
   unit-modulus directions on the seam, so its Cayley gap can close.
2. **Opposite-sign history coupling.** Cancellation between arithmetic and
   history impedances may create seam kernels, but the uniform passivity proof
   is lost and must be replaced by a Krein-signature theorem.
3. **Rectangular defect channel.** Xi zeros may live in a cokernel or boundary
   defect space not seen by invertibility of the square impedance block.
4. **Singular boundary relation.** The seam may carry a relation rather than a
   bounded operator, with kernel states appearing in its multivalued part.

None may be selected after inspecting Xi zeros; its source origin must be
proved.

## Consequence for the finite factorization

The identity

\[
\det M_{U,X}
=
\zeta_X(s)\det N_X(s)
\]

remains correct at finite cutoff. The strict gap shows that the finite
numerator is a unit. It does not authorize continuation of
\(\zeta_X\det N_X\) as the determinant of the invertible completed pencil.
The Xi divisor enters only through the separate theta Mellin dual section.

## Corrected status

Closed:

- strict Schur arithmetic network;
- passive Cayley realization;
- quantitative off-seam and seam invertibility;
- finite inverse-Euler factorization.

Rejected as an RH pencil:

- the same-sign passive sum
  \(\Theta_{\rm ar}+M_H\), because it has no seam defect channel.

Open:

- a source-derived lossless, indefinite, rectangular, or relational boundary
  completion whose determinant section is Xi and whose off-seam Green form
  remains coercive.

## Disposition

The uniform Cayley gap is too strong for the spectral task. It proves that the
constructed passive characteristic is divisor-blind. G4 cannot close through
this same-sign strict passive network, and no RH conclusion is authorized.
