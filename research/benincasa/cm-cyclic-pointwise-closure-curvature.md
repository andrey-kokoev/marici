# Cyclic quadratic pointwise closure has curvature

## Reconstructed scalar

The modular pointwise closure coefficients from Entry 2593 admit a unique
degree-certified reconstruction

\[
\omega_i=\frac{N_i(s_1,s_2,s_3)}{s_1s_2s_3\Lambda_P},
\]

where every \(N_i\) is homogeneous of degree four. Fifteen training points
determine the fifteen coefficients, and five unused points validate every
component over both primes 32003 and 65521.

The denominator agrees with the minimal univariate slice denominator on two
independent slices and both primes. Thus the observed rational presentation
uses only existing soft and triangle support.

## Curvature obstruction

Exact differentiation of the reconstructed one-form gives, at
\((s_1,s_2,s_3)=(5,7,11)\),

\[
F_{12}=\frac{8}{40425},\qquad
F_{13}=-\frac{8}{63525},\qquad
F_{23}=\frac{8}{88935}.
\]

At \((7,11,13)\), all three components are again nonzero with the same sign
pattern.

A scalar connection induced from a flat connection on a genuine quotient
line would be flat. Therefore this reconstructed scalar cannot be such an
induced connection.

## Typing correction

Entry 2593 established

\[
\nabla\mathsf A_{\rm cyc}^{(2)}
\subset
\langle\nu_1,\nu_2,\nu_3,\mathsf A_{\rm cyc}^{(2)}\rangle
\]

at the tested fibers. It did not establish

\[
\nabla\langle\nu_1,\nu_2,\nu_3\rangle
\subset
\langle\nu_1,\nu_2,\nu_3\rangle.
\]

Without the second inclusion, quotient transport is undefined. The phrase
“horizontal quotient line” is therefore retracted and replaced by “pointwise
derivative closure modulo an unverified denominator.”

The next finite gate is preservation of the labelled first-normal span. If it
fails, export the smallest off-span component. If it passes under a corrected
connection convention, the scalar transport must be recomputed and its
curvature must vanish before any support interpretation.

## Artifacts

- `research/benincasa/checkers/probe_cm_cyclic_connection_slice_degrees.py`
- `research/benincasa/checkers/check_cm_cyclic_connection_reconstruction.py`
- `research/benincasa/results/cm-cyclic-connection-slice-degrees.json`
- `research/benincasa/results/cm-cyclic-connection-reconstruction.json`
- `research/benincasa/checkers/check_cm_cyclic_connection_curvature.py`
- `research/benincasa/results/cm-cyclic-connection-curvature.json`

