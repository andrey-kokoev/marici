# Theta Gaussian vacuum selection produces a lattice Ward current, not yet RH orientation

## Status

Exact source-selection theorem and exact transport commutator. Positivity and
Fourier self-duality leave hostile archimedean carriers with off-critical
Mellin zeros. The oscillator ground-state equation removes those perturbations
and uniquely selects the Gaussian vacuum line.

This is a genuine source-derived restriction. Its first nontrivial consequence
is a coherent-state Ward current under lattice translation. It still does not,
by itself, prove that the completed scalar readout avoids zero off the seam.

## Vacuum annihilation law

Take the self-dual Gaussian

\[
g(x)=e^{-\pi x^2}
\]

and define the annihilation operator

\[
a=\partial_x+2\pi x.
\]

Then

\[
ag=0.
\]

Conversely, every differentiable solution of (af=0) has the form

\[
f(x)=Cg(x).
\]

Thus the annihilation law selects a one-dimensional vacuum line. Normalization
and positivity select the standard Gaussian on that line.

This is stronger than Fourier self-duality. A Fourier-fixed Hermite
perturbation need not lie in \(\ker a\).

## Exact rejection of the hostile direction

Let

\[
f_\delta(x)
=g(x)[1+\delta P(\pi x^2)]
\]

with nonconstant polynomial (P). Since (ag=0\), direct differentiation
gives

\[
af_\delta(x)
=2\pi\delta xP'(\pi x^2)g(x).
\]

This is nonzero for every nonzero \(\delta\). Hence Grothendieck's positive,
even, Fourier-fixed hostile family fails the oscillator-vacuum law even when it
passes positivity and full primal-dual Poisson sewing.

The law therefore distinguishes the actual archimedean vacuum from that
hostile orbit by a source-visible local operator.

## Lattice-translation commutator

Let translation act by

\[
(T_nf)(x)=f(x-n).
\]

Then

\[
[a,T_n]=2\pi nT_n.
\]

Indeed,

\[
aT_nf
=T_n(af)+2\pi nT_nf.
\]

Applied to the vacuum,

\[
aT_ng=2\pi nT_ng.
\]

Each translated Gaussian is therefore a coherent state whose annihilation
eigenvalue is its lattice label. This is an exact coupling between oscillator
degree and labelled source transport.

It is qualitatively different from the multiplicative prime commutator

\[
[L,T_p]=(\log p)T_p.
\]

The two laws live on different source coordinates and must not be identified
without the adelic Poisson constructor that joins additive lattice labels to
multiplicative Mellin scale.

## Number-energy identity

Let (a^*=-\partial_x+2\pi x\) on the Schwartz core. The oscillator number
form is

\[
\langle f,a^*af\rangle=\lVert af\rVert^2\geq0.
\]

It vanishes exactly on the Gaussian vacuum line. For a translated vacuum,

\[
\lVert aT_ng\rVert^2
=4\pi^2n^2\lVert g\rVert^2.
\]

Thus the source supplies a positive label-sensitive energy before Mellin
projection. This is a legitimate candidate ancestor of a number current, but
it grades additive lattice displacement by (n^2), not Clark jet degree by
(m) and not prime-power depth by (k).

## Ward identity against the comb

Let the rational or integral boundary be represented schematically by a comb

\[
\Delta=\sum_{n\in\mathbb Z}\delta_n.
\]

Pairing the translated-vacuum commutator with this boundary produces a labelled
Ward current weighted by (n). Formally,

\[
\sum_n aT_ng
=2\pi\sum_n nT_ng.
\]

For a symmetric full lattice, the odd current cancels globally. Its one-sided,
boundary, differentiated, or two-copy forms need not vanish. Those are the
only forms that can carry orientation after reciprocal sewing.

All such identities require distributional typing before completion. Moving
(a) across the comb introduces derivative distributions and boundary terms;
they cannot be discarded by scalar Poisson summation.

## Why source uniqueness is not RH

The annihilation equation proves that the standard local vacuum is selected.
Together with the labelled comb and Poisson summation, it reconstructs the
actual theta source. That is stronger provenance than positivity plus
self-duality.

But selecting one source object does not establish a zero-exclusion law for a
particular scalar matrix coefficient of that object. No implication from
\(af=0\) to off-seam scalar nonvanishing has been proved. Declaring one would
merely attach the desired property to the unique source after selection.

The explanatory gain must come from a transported Ward identity, energy, or
boundary relation derived from (af=0\) before the Mellin readout.

## Finite falsifiers

Any proposed vacuum-orientation mechanism fails if:

- it admits a nonconstant Fourier-fixed Hermite perturbation in \(\ker a\);
- it identifies the additive label (n), multiplicative degree \(\log p\), and
  spectral jet grade (m) without a typed constructor;
- it drops the derivative-comb boundary term when moving (a) through Poisson
  sewing;
- it derives only source uniqueness and then asserts scalar nonvanishing;
- its pushed-forward law also holds for the hostile (f_\delta\).

## Decisive next calculation

Push the annihilation relation and the positive form (a^*a) through the full
labelled primal-dual Poisson construction before Mellin aggregation. Keep the
following channels distinct:

1. the vacuum equation (ag=0);
2. the coherent lattice current (aT_ng=2\pi nT_ng);
3. derivative-comb boundary terms;
4. the even number energy (a^*a);
5. the final Mellin readout.

If their completed Green identity yields a signed mismatch current that fails
for the hostile Fourier-fixed perturbation, the vacuum law adds genuine
orientation information. If it only reconstructs the known theta functional
equation, then oscillator selection supplies provenance but no RH mechanism.
