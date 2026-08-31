# Shifted Chern–Simons coset gate: WP1070

## Question

What exact shifted Chern–Simons lattice coset is required by WP1069's
conditional seven-channel one-quartet vector?

## Residue vector

A shifted lattice with one coset has the form

\[
s+\mathbb Z^7.
\]

In the WP1069 channel order, the one-quartet vector is

\[
\left(\frac12,\frac14,0,2,2,-\frac14,0\right).
\]

Its residue modulo the integral Chern–Simons lattice is therefore

\[
s_{\rm quartet}
=
\left(\frac12,\frac14,0,0,0,\frac34,0\right)
\pmod{\mathbb Z^7}.
\]

The common denominator is \(4\).

## Exact hostiles

The reflected orientation has a different coset:

\[
s_{\rm reflected}
=
\left(\frac12,\frac34,0,0,0,\frac14,0\right)
\pmod{\mathbb Z^7}.
\]

The port-destroying \(C=23\) doublet-pair cell has

\[
s_{\rm pair}
=
(0,0,0,0,0,0,\tfrac12)
\pmod{\mathbb Z^7}.
\]

The alternate WP1069 Green–Schwarz split changes the quartet coset to

\[
s_{\rm alt}
=
\left(\frac12,\frac14,0,0,0,\frac14,\frac12\right)
\pmod{\mathbb Z^7}.
\]

Thus a generic statement that “half-integer levels are allowed” is
insufficient. The UV theory must produce the complete residue vector and the
endpoint orientation.

## Boundary

This packet computes the required coset only. It does not prove that the UV
compactification realizes it.

## Classification

Shifted-coset gate. It converts shifted quantization into an exact
multicomponent lattice test.

Checker: `research/flavor/checkers/wp1070_shifted_chern_simons_coset_gate.py`

Result: `results/wp1070_shifted_chern_simons_coset_gate.json`
