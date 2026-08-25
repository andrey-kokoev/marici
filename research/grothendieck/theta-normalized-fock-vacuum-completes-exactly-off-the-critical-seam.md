# Theta normalized Fock vacuum completes exactly off the critical seam

## Local normalized occupation state

For a prime `p` and `s=sigma+it` with `sigma>0`, put

\[
 r_p=p^{-s}.
\]

In the local bosonic occupation space with orthonormal basis `e_(p,k)`, the
unramified geometric state is

\[
 \Omega_{p,s}^{\rm raw}
 =\sum_{k\ge0}r_p^ke_{p,k}.
\]

Its squared norm is

\[
 \|\Omega_{p,s}^{\rm raw}\|^2
 ={1\over1-|r_p|^2}
 ={1\over1-p^{-2\sigma}}.
\]

Therefore the normalized local state is

\[
 \boxed{
 \omega_{p,s}
 =\sqrt{1-p^{-2\sigma}}
 \sum_{k\ge0}p^{-ks}e_{p,k}.}
\]

Take the empty-occupation vector `e_(p,0)` as the source reference ray. Then

\[
 \langle e_{p,0},\omega_{p,s}\rangle
 =\sqrt{1-p^{-2\sigma}}>0.
\]

The overlap is independent of spectral height `t`.

## Infinite tensor criterion

The normalized restricted tensor product

\[
 \Omega_s=\bigotimes_p\omega_{p,s}
\]

exists in the incomplete tensor product based at the vacuum rays precisely
when

\[
 \sum_p
 \left(1-\langle e_{p,0},\omega_{p,s}\rangle\right)<\infty.
\]

Since

\[
 1-\sqrt{1-x}\sim{x\over2}
 \qquad(x\to0),
\]

this is equivalent to

\[
 \sum_pp^{-2\sigma}<\infty.
\]

The prime sum converges exactly for `2 sigma>1`. Hence

\[
 \boxed{
 \Omega_s\text{ exists canonically in the direct Fock sector}
 \iff\Re s>{1\over2}.}
\]

On every compact sub-half-plane `Re(s)>=1/2+epsilon`, convergence is uniform
and independent of `Im(s)`.

## The reciprocal sector

Fourier--Tate reflection sends `s` to `1-conj(s)`. Applying the same theorem
to the dual occupation parameter gives

\[
 \boxed{
 \Omega_{1-\bar s}^{\vee}	ext{ exists canonically in the dual Fock sector}
 \iff\Re s<{1\over2}.}
\]

Thus the two open half-planes are not merely regions where different Euler
formulas converge. They are exactly the two domains in which the corresponding
normalized infinite Fock state belongs to its vacuum representation.

At the critical seam,

\[
 \sum_pp^{-1}=\infty,
\]

so neither direct vacuum representation contains the completed state. The seam
requires the relative anomaly-line/rigged construction developed in packets
172--176.

## State completion gate closes

Packet 184 left open whether the finite Fock-state net itself survives
completion. The normalized tensor criterion answers this positively and
locally uniformly in each appropriate open sector.

There is no state escape there:

\[
 \|\Omega_s\|=1.
\]

Moreover the finite-cutoff tensors converge in the source Hilbert topology,
not merely projectively or through a scalar Euler coordinate.

This is a source-derived completion theorem independent of the zero set.

## What remains

The completed Fock state can exist and still be orthogonal to the
distinguished Poisson detector.  Therefore the theorem closes the first of the
two gates isolated after Kitaev's objection:

1. completion-stable existence of the distinguished source state — closed in
   each open sector;
2. transversality of the distinguished Poisson detector — open.

The scalar Euler product is not the normalized-state overlap. In particular,
nonzero vacuum overlap does not imply nonzero completed Tate readout.

The remaining RH-bearing question is now singular again, but for a justified
reason:

\[
 \boxed{
 \langle\ell_s,\Omega_s\rangle\stackrel{?}{\ne}0
 \quad\text{throughout the direct open sector},}
\]

with the reciprocal statement in the dual sector and with `ell_s` derived
from the four-channel Poisson incidence.

## Scope

This packet proves the exact infinite-tensor implementability threshold for
the normalized unramified Fock vacuum. It does not identify its Poisson
detector overlap with `Xi` in the completed rigging or prove that overlap is
nonzero. At the seam it asserts failure of the chosen vacuum representation,
not nonexistence of the relative completed state.
