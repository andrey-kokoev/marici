# Theta faithful seam Gram and oriented oscillator occupy decoupled blocks

## Bounded question

Does combining the prime-uniform seam Gram from packet 223 with the
seam-selective oscillator energy from packet 220 produce the required signed
Green identity?

## Two exact blocks

The labelled oscillator block obeys

\[
E_{pn}(p^{-s}R_p\psi)
=p^{1-2\Re s}E_n(\psi).
\]

It therefore carries the correct critical-seam orientation. But on every
labelled Gaussian source atom,

\[
E_n(\phi_n)=0.
\]

The full tail--seam block instead uses the moving-cut isometry

\[
U_qf=(g_q,h_q),
\qquad
\|g_q\|^2+\|h_q\|^2=\|f\|^2.
\]

It is faithful and, after prime resolution with von Mangoldt weight, has the
uniform lower frame reserve from packet 223.

## Transport mismatch

Raw dilation on the oscillator graph contributes the Jacobian factor that
produces \(p^{1-2\Re s}\). Translation in the logarithmic tail--seam coordinate
is an isometry. After multiplication by the Mellin amplitude, the full
tail--seam norm receives only the scalar factor \(p^{-2\Re s}\) in this frame,
not \(p^{1-2\Re s}\).

The static von Mangoldt weight \(\log p\) repairs the prime-uniform frame bound,
but it does not supply the missing dilation factor \(p\). Current normalization
and transport orientation are distinct operations.

## Commuting-square obstruction

The oscillator/Clark action and moving-cut action live on separate tensor
factors. Their established covariance is a commuting square. Consequently the
mixed commutator of the two independent operations vanishes.

Thus their direct-sum energy has the form

\[
Q_s=Q_s^{\rm osc}\oplus Q_s^{\rm seam},
\]

where the first summand has the right spectral multiplier and vanishes on the
source, while the second is faithful and has the wrong multiplier. Adding the
two does not produce

\[
(2\Re s-1)Q_s^{\rm seam}.
\]

No Schur complement can manufacture the missing mixed term when the declared
off-diagonal coupling is zero.

## Exact remaining constructor

The programme now requires a source-derived operator \(C_p\) coupling the
oscillator and seam-history factors such that its commutator with prime Mellin
transport has a faithful component proportional to the weighted seam Gram.
Schematically, the target is

\[
\langle\Psi,[K_s,C_p]\Psi\rangle
=(2\Re s-1)(\log p)\|H_p\Psi\|^2
+\partial J_p(\Psi),
\]

with every object defined before scalar aggregation.

This display is a target type, not an asserted identity. The coefficient,
domain, adjoint, and boundary term must be derived from the theta/Tate source.

## Candidate source of noncommutation

The only known operation touching both factors is moving-boundary incidence:
prime multiplication changes the cut by \(\log p\), while the Gaussian
oscillator changes real dilation. Their endpoint evaluation and normal
derivative may fail to commute even though the bulk tensor maps do.

Therefore the next calculation should be the boundary commutator, not another
bulk norm sum. It must retain the common trace

\[
g_q(0)=h_q(0)=\Phi(q)
\]

and the oriented normal jump

\[
g_q'(0)-h_q'(0)=2\Phi'(q).
\]

If this commutator is finite-rank or decays on prime Følner packets, it cannot
transfer the uniform seam reserve and the route closes. If it reproduces the
full seam Gram, it supplies the missing distributive law.

## Scope

This packet proves that the currently derived faithful seam energy and
seam-oriented oscillator energy occupy commuting, capability-complementary
blocks. Their direct sum has no RH force. It does not compute the moving-boundary
commutator, derive an off-diagonal coupling, close the Green identity, or prove
RH.
