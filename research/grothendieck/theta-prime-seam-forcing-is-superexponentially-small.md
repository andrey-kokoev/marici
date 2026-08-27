# Theta prime-seam forcing is superexponentially small

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact asymptotic aggregation obstruction

## Sampled moving-seam forcing

The continuous moving-seam density is

\[
F(L,z)=\Phi(L)D(L,z),
\qquad
D(L,z)=H_+(L,z)-H_-(L,z).
\]

Ledger 3068 gives, with (x=\pi e^{2L}),

\[
D(L,z)\sim\frac{z\Phi(L)}{2x^2}.
\]

The leading theta label satisfies

\[
\Phi(L)\sim4x^{9/4}e^{-x}.
\]

Consequently,

\[
F(L,z)\sim8z x^{5/2}e^{-2x}.
\]

At a prime seam (L=\log p), this becomes

\[
F(\log p,z)
\sim8\pi^{5/2}z p^5e^{-2\pi p^2}.
\]

## Aggregation consequence

For every fixed real exponent (A),

\[
\sum_{p\in\mathbb P}p^A|F(\log p,z)|
\]

converges absolutely. The same remains true after multiplication by any fixed
power of (log p). Thus every weight supplied by ordinary Euler valuation,
primitive, square, or connected-tail bookkeeping leaves a
superexponentially vanishing prime-infinity tail.

This is the opposite of the earlier primitive-current completion problem.
The sampled moving-seam forcing is not too large to aggregate. It is far too
small to reconstruct the unsampled continuous current through its tail.

## Meaning

Large prime seams faithfully detect whether the odd tail is nonzero, but they
carry asymptotically negligible magnitude. Faithfulness and reconstruction
are therefore distinct:

- every sufficiently large sample is nonzero when (z\ne0);
- the entire large-prime tail contributes vanishing total mass under
  source-authorized polynomial Euler weights.

Any identity equating the continuous seam integral to an arithmetic sample
sum must consequently derive its content from finitely many small seams plus
an archimedean or Poisson interpolation term. It cannot arise from a limiting
prime boundary flux.

Exponentially increasing interpolation weights could defeat this argument,
but no such weights occur in the Euler constructors. Introducing them solely
to restore the integral would be unauthorized fitting.

## Revised frontier

The moving-seam route now faces a hard dichotomy:

1. Poisson completion supplies an explicit archimedean interpolation operator
   carrying the unsampled continuum; or
2. arithmetic seam sampling is merely a diagnostic readout and cannot close
   the Green conservation law.

The next calculation should search for that interpolation operator directly
in the full lattice Poisson formula. More prime summation cannot provide it.

## Verification

The checker derives the leading prime scale and verifies by the ratio test
that every polynomially weighted integer majorant converges.
