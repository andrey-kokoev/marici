# Theta hostile quartic forces a derivative-delta source

## Mellin source type

Use the Mellin convention

\[
 \mathcal M\mu(s)=\langle\mu,x^{-s}\rangle.
\]

Let `E=x partial_x` act on test functions. Since

\[
 E(x^{-s})=-s x^{-s},
\]

the distributional transpose satisfies

\[
 \mathcal M(E^*\mu)(s)=-s\mathcal M\mu(s).
\]

Consequently, for every polynomial `P`,

\[
 P(s)\mathcal M\mu(s)
 =\mathcal M\left(P(-E^*)\mu\right)(s).
\]

## Effect on the arithmetic comb

The positive-Fock Euler source is an order-zero positive atomic distribution,
schematically

\[
 \mu=\sum_{n\ge1}a_n\delta_n,
 \qquad a_n\ge0.
\]

If `P` has degree `d>0`, then `P(-E^*)delta_n` contains a nonzero derivative
of `delta_n` of order `d`. Distinct atoms have disjoint local supports, so
their highest derivative terms cannot cancel across labels. Therefore
(P(-E^*)\mu) is a distribution of positive order, not a positive atomic
measure.

This conclusion is local at each integer label and requires no inspection of
the zeros of `P`.

## Hostile divisor multiplier

For

\[
 H_{a,b}(s)=
 \left((s-\tfrac12-a)^2+b^2\right)
 \left((s-\tfrac12+a)^2+b^2\right),
\]

the degree is four. Thus realizing

\[
 H_{a,b}(s)\mathcal M\mu(s)
\]

requires fourth-order derivative-delta components at every occupied source
label. It cannot arise from the original positive occupation-number grammar,
which permits weighted atoms and Fock convolution but not derivatives of the
label evaluation functional.

The hostile multiplier is therefore rejected by the distributional order of
the labelled arithmetic source.

This rejection occurs before reciprocal symmetry, completion, or divisor
analysis.

## What this proves and does not prove

This supplies the first concrete success of the Deutsch constructor test:
the standard quartic off-line-zero insertion is not a presentation change of
the positive atomic Fock source.

It does not prove that the genuine completed section is zero-free off the
seam. Nor does it reject every imaginable hostile source. A stronger hostile
test is an order-zero positive atomic source, obeying the full labelled
constructor grammar, whose completed readout has off-seam zeros.

## Falsifier

The theorem is falsified as a constructor discriminator if the authorized
theta/Tate source category independently contains derivative-delta label
currents of order four, or if the hostile quartic admits an alternative
order-zero positive atomic lift with the same complete boundary incidence.
