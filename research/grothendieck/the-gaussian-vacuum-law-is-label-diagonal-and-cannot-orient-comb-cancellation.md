# The Gaussian vacuum law is label-diagonal and cannot orient comb cancellation

## Bounded question

After positive Fourier-fixed Poisson sewing failed as an orbit restriction,
can the oscillator ground-state law distinguish the Gaussian strongly enough
to prevent off-seam scalar cancellation?

## Source vacuum law

Let

\[
f(x)=e^{-\pi x^2}.
\]

It is the positive solution, up to normalization, of

\[
a f=0,
\qquad
a=\partial_x+2\pi x.
\]

For the half-density dilation

\[
f_u(x)=e^{u/2}f(e^u x),
\]

the transported annihilator is

\[
a_u=\partial_x+2\pi e^{2u}x,
\qquad
a_uf_u=0.
\]

This law excludes the positive Hermite excitation in the preceding hostile
packet. It therefore supplies genuine source provenance.

## Sampling exposes its limitation

Let the labelled comb readout be

\[
\mathcal A_c(u)
=
\sum_{n}c_n f_u(n),
\]

initially for finite coefficient packets. The vacuum equation holds at every
label independently:

\[
(a_uf_u)(n)=0.
\]

Consequently

\[
\sum_n c_n(a_uf_u)(n)=0
\]

for every coefficient packet (c). This scalar Ward identity is termwise
zero. It contains no relation between two distinct labels.

A scalar zero, by contrast, is exactly an inter-label cancellation:

\[
\sum_n c_n f_u(n)=0.
\]

Whenever two sampled values are nonzero, coefficients supported on those two
labels can be chosen so that the readout vanishes, while the vacuum Ward
identity remains valid label by label. Thus the annihilator identifies the
carrier but does not keep the sampled orbit away from the augmentation kernel.

## The induced hierarchy does not close

Differentiating the scaled samples gives

\[
\partial_u f_u(n)
=
\left(\frac12-2\pi n^2e^{2u}\right)f_u(n).
\]

Repeated derivatives generate the labelled moments

\[
\sum_n c_n n^{2k}f_u(n).
\]

Because the rates (n^2) are distinct, no finite collection of these moments
closes under (u)-evolution on arbitrary finite supports. The vacuum law
therefore produces the already familiar complete observer tower, not a scalar
conservation law.

## Result

Gaussian-vacuum selection and scalar orientation are different achievements:

1. the annihilator rejects non-vacuum Fourier-fixed carriers;
2. it acts diagonally on arithmetic labels;
3. its sampled Ward identity is termwise tautological;
4. its dilation evolution generates an infinite moment tower;
5. none of these statements constrains cancellation between distinct labels.

The conjunction of the exact Gaussian and the exact integer comb determines
the theta readout, but merely identifying that unique pair is not an
explanation of its zero set. The missing theorem must be a mixed source law:
it must couple the oscillator ladder to arithmetic label transport before
augmentation and produce a conserved cross-label current.

## Next target

Compute the commutator square between the transported annihilator and the
Poisson label correspondence. Its residual is the first possible mixed
Gaussian--arithmetic current. If that residual remains label-diagonal, factors
through the moment tower, or vanishes termwise, vacuum selection contributes
no RH force beyond provenance.
