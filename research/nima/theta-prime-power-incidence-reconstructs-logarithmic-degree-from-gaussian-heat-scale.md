# Theta prime-power incidence reconstructs logarithmic degree from Gaussian heat scale

## Status

Exact arithmetic–archimedean coupling theorem. Evaluating the Gaussian scale
orbit at a prime-power jump sends an additive lattice label (n\) to the product
label (np^k\). The complete typed family of prime-power divisibility
incidences reconstructs the logarithmic label generator through the classical
von Mangoldt divisor identity.

Equivalently, logarithmic arithmetic degree is half the operator logarithm of
the Gaussian heat-scale operator. This gives a source-derived bridge between
the jump measure and heat flow that is absent for hostile arbitrary sources.

It supplies a positive arithmetic degree operator, but not yet a scalar
zero-orientation theorem.

## Gaussian scale sampling at a jump

For the basic Gaussian atom, write

\[
g_n(v)=e^{-\pi n^2e^{2v}}.
\]

At a prime-power jump

\[
v=k\log p,
\]

we have

\[
g_n(k\log p)
=e^{-\pi n^2p^{2k}}
=e^{-\pi(np^k)^2}.
\]

Thus the jump evaluation implements the labelled multiplication

\[
n\longmapsto np^k
\]

inside the Gaussian heat orbit. The continuous scale coordinate and the
multiplicative valuation label meet at the same source atom.

## Divisibility incidence projections

On the positive-integer label module define

\[
P_{p,k}e_m
=\mathbf1_{p^k\mid m}e_m.
\]

Each (P_{p,k}\) records whether the label (m\) contains the declared
prime-power incidence. The full logarithmic incidence operator is

\[
L_{\mathrm{inc}}
=\sum_p\sum_{k\geq1}(\log p)P_{p,k}.
\]

The sum is finite on every basis state because only finitely many prime powers
divide one integer.

## Von Mangoldt divisor identity

Let

\[
m=\prod_pp^{a_p}.
\]

Then

\[
\begin{aligned}
L_{\mathrm{inc}}e_m
&=\sum_p\sum_{k=1}^{a_p}(\log p)e_m\\
&=\sum_pa_p\log p\,e_m\\
&=(\log m)e_m.
\end{aligned}
\]

Therefore

\[
L_{\mathrm{inc}}=L,
\qquad
Le_m=(\log m)e_m.
\]

This is the operator form of

\[
\sum_{d\mid m}\Lambda(d)=\log m.
\]

Typing is essential: the sum ranges over prime-power divisors, with each
incidence weighted by its primitive logarithm.

## Relation to Gaussian heat scale

Define the positive Gaussian scale operator

\[
Qe_m=m^2e_m.
\]

Functional calculus gives

\[
\frac12\log Q\,e_m
=\log m\,e_m.
\]

Hence

\[
L_{\mathrm{inc}}
=\frac12\log Q.
\]

The multiplicative prime-power incidence and the archimedean Gaussian heat
scale determine the same logarithmic degree operator from opposite sides.

This is a genuine coherence relation, not an analogy.

## Prime transport commutator recovered

For multiplication transport

\[
T_pe_m=e_{pm},
\]

the reconstructed degree satisfies

\[
[L_{\mathrm{inc}},T_p]
=(\log p)T_p.
\]

Thus the earlier logarithmic transport current is now sourced twice:

- combinatorially by the complete prime-power divisibility family;
- analytically by the logarithm of Gaussian heat scale.

The equality of these constructions is the arithmetic–archimedean coupling.

## Why the square channel alone failed

The prime-square incidence (P_{p,2}\) contributes one copy of \(\log p\) when
(p^2\mid m\). It does not supply the full eigenvalue \(\log m\), nor does it
act as the Clark jet-number operator.

Only the complete typed tower

\[
P_{p,1},P_{p,2},\ldots,P_{p,a_p}
\]

reconstructs (a_p\log p\). This confirms the earlier rejection of a direct
identification between the bare square current and a number operator while
exhibiting the correct completed arithmetic degree.

## Positive energy

Since (m\geq1\),

\[
L_{\mathrm{inc}}\geq0
\]

on the integer label Hilbert module, with kernel equal to the vacuum label

\[
\ker L_{\mathrm{inc}}=\operatorname{span}\{e_1\}.
\]

The corresponding quadratic form is

\[
\langle c,L_{\mathrm{inc}}c\rangle
=\sum_m(\log m)|c_m|^2.
\]

This is an independently source-derived positive label-regularity energy. It
is distinct from the Clark spectral-jet number energy and from the scalar Weil
kernel.

## Coupling to the staircase derivative

The jump measure

\[
dW=\sum_{p,k}w_{p,k}\delta_{k\log p}
\]

samples the Gaussian scale orbit precisely at the incidences implementing
(n\mapsto np^k\). With unrenormalized von Mangoldt incidence, aggregation over
all divisors of a final label produces (L_{\mathrm{inc}}\).

Half-density or Euler-log weights modify the boundary amplitude of each jump
but do not change the underlying divisibility constructor. These weights must
remain separate from the incidence count when comparing the boundary current
with the positive degree operator.

## Hostile-source discrimination

An arbitrary positive Fourier-fixed source may satisfy Poisson symmetry and may
be sampled at the same jump locations. It need not obey the Gaussian scale law

\[
g_n(k\log p)=g_{np^k}(0).
\]

Therefore it need not identify the jump incidence with one global positive
operator (Q\), nor satisfy

\[
L_{\mathrm{inc}}=\frac12\log Q.
\]

This coherence rejects the prior hostile class for a source-visible reason.

## Orientation boundary

The positive operator (L_{\mathrm{inc}}\) controls arithmetic label
regularity. It does not make the distinguished scalar readout faithful. A
nonzero state can have positive logarithmic energy while its scalar aggregation
vanishes.

The RH-bearing theorem must connect this positive degree to the transverse
staircase Green current or to star compatibility of the zero-state boundary
domain. Merely adjoining the energy repeats the observability-versus-orientation
failure.

## Finite falsifiers

Any proposed arithmetic–heat coupling fails if:

- it uses only (k=2\) incidence to reconstruct \(\log m\);
- it counts composites that are not prime powers;
- it erases multiplicity (a_p\);
- it identifies half-density boundary weights with divisibility weights;
- it violates (L_{\mathrm{inc}}=(1/2)\log Q\) on a basis label;
- it infers scalar nonvanishing from positivity of (L_{\mathrm{inc}}\) alone.

The smallest multiplicity witness is (m=p^2\): both (p\) and (p^2\)
incidences are required to obtain (2\log p\).

## Consequence

The programme now has the theta-specific heat/jump relation requested by the
staircase hostile audit. The full prime-power grammar reconstructs a canonical
positive logarithmic degree from the Gaussian scale operator.

The next decisive calculation is whether the completed staircase Green
identity can be strengthened to an energy balance in which the transverse
current is controlled by \(L_{\mathrm{inc}}\) and the control is star-compatible
only on the seam. If no such balance exists, the new coherence remains a deep
source-provenance theorem rather than an RH orientation mechanism.
