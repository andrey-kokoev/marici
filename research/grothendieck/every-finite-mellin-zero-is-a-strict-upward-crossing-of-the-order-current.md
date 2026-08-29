# Every finite Mellin zero is a strict upward crossing of the order current

Author: marici.Grothendieck

Date: 2026-08-28

## Canonical zero-state

Fix a real horizontal coordinate \(\sigma\) and finite coefficients \(a_i\)
on distinct logarithmic scales \(\lambda_i\). Define

\[
v_i(t)=a_i e^{-\sigma\lambda_i}e^{-it\lambda_i}
\]

and the scalar Mellin readout

\[
F_\sigma(t)=\sum_i v_i(t).
\]

At every scalar zero \(F_\sigma(t_0)=0\), the labelled vector
\(v(t_0)\) lies canonically in the zero-mean complement. No fitted kernel or
backward operator construction is needed.

## Order current

Let \(S_{ij}=\operatorname{sgn}(\lambda_j-\lambda_i)\), and define the real
order current

\[
J_\sigma(t)=-i\langle v(t),Sv(t)\rangle.
\]

Since \(S^*=-S\), this quantity is real. Vertical Mellin evolution satisfies

\[
v'(t)=-i\Lambda v(t).
\]

Direct differentiation yields

\[
J_\sigma'(t)
=
\langle v(t),[\Lambda,S]v(t)\rangle.
\]

## Strict crossing theorem

At every scalar zero,

\[
J_\sigma'(t_0)>0.
\]

Indeed, \(F_\sigma(t_0)=0\) makes \(v(t_0)\) zero-mean, and Entry 4105 proves
strict positivity of the commutator on every nonzero zero-mean vector.
Exponentials and nonzero source coefficients ensure \(v(t_0)\neq0\).

Thus every finite Mellin zero is an upward crossing of one canonical
source-framed current.

## Scope correction

The desired contradiction does not follow. Scalar nullity does not imply

\[
\langle v,[\Lambda,S]v\rangle=0.
\]

It implies the opposite strict inequality. The naive virial route is
therefore closed.

Moreover the theorem holds for every horizontal coordinate \(\sigma\) and
for hostile finite exponential sums with off-seam zeros. It orients zeros
but does not confine them to a vertical line.

This is still explanatory progress. The Wronskian orientation found in Entry
4094 is not accidental: it is the scalar shadow of monotone ordered-current
flow on the complete labelled state.

## What extra law is now required

RH needs a second, source-specific statement that compares the same crossing
on the two reciprocal sheets. A viable law would force incompatible
orientations off the seam:

\[
J_+'(s)>0,\qquad J_-'(1-\overline s)>0,
\]

while completed sewing identifies their oriented currents with opposite
sign unless \(\Re s=\tfrac12\).

That reciprocal sign relation is not supplied by the universal commutator.
It must come from theta/Tate normalization and boundary orientation.

## Sharp next test

Construct the two sheet currents before scalar aggregation and compute their
exact sewing transformation. There are three outcomes:

1. sewing preserves both orientations, giving no confinement;
2. sewing reverses orientation only on the critical seam, yielding a possible
   contradiction off it;
3. boundary currents alter the transformation, identifying the precise
   missing primitive or square channel.

Any sign rule inferred only after locating zeros is inadmissible.
