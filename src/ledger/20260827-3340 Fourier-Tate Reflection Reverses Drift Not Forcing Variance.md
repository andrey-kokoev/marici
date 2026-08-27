# Fourier--Tate Reflection Reverses Drift, Not Forcing Variance

The actual centered theta equations use the same real forward forcing on both
reciprocal sheets:

\[
\psi_+'=-z\psi_+-F,
\qquad
\psi_-'=\overline z\psi_--F.
\]

Fourier--Tate reflection reverses spectral drift but transports the
upper-right source-to-tail arrow to another upper-right arrow. It does not
produce the lower-left adjoint incidence `B*`.

Therefore the same-forcing pointwise common-path no-go applies to the native
theta double, closing the reflected-forward Green shortcut. With a
role-preserving pairing, cross-adjointness of two nontrivial upper-triangular
forward blocks is impossible: it forces the source incidence to vanish.

The unique surviving local constructor is variance-reversing adjoint
completion. At finite cutoff it must supply a typed lower incidence
`B_{-,X}:H_X -> U_X` and pass

\[
B_{-,X}=B_{+,X}^*
\]

with domains, metrics, and boundary grades retained. Scalar agreement after
aggregation is insufficient.

Research packet:
`research/grothendieck/fourier-tate-reflection-reverses-drift-not-forcing-variance.md`

Exact checker:
`research/grothendieck/checkers/check_reflection_does_not_reverse_forcing_variance.py`

The checker passes 6/6 exact tests.
