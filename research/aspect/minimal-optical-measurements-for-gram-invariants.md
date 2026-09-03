# Minimal optical measurements for Gram invariants

## Question

Which intensity and interference measurements reconstruct the trace and determinant of a two-route Gram return while retaining the two routes until readout?

## Four-intensity reconstruction

Let the route amplitudes be \(b_1,b_2\), with

\[
u=\|b_1\|^2,
\qquad v=\|b_2\|^2,
\qquad c=\langle b_1,b_2\rangle.
\]

Measure the two route-resolved intensities and two coherent combinations:

\[
I_0=\|b_1+b_2\|^2,
\qquad
I_{\pi/2}=\|b_1+i b_2\|^2.
\]

With the declared inner-product convention,

\[
\operatorname{Re}c=\frac{I_0-u-v}{2},
\qquad
\operatorname{Im}c=\frac{u+v-I_{\pi/2}}{2}.
\]

Therefore

\[
\operatorname{tr}G=u+v,
\qquad
\det G=uv-|c|^2.
\]

This reconstructs the two invariant inputs to the strict-return test without identifying the routes before the phase-controlled combining stage.

## Phase hostile

The data \((u,v,I_0)\) determine only \(\operatorname{Re}c\). Two route pairs can share these three measurements while having different \(|\operatorname{Im}c|\), hence different determinants. A single interference phase is not faithful for the invariant readout.

If reciprocity independently proves \(c\) real in the same target pairing, \(I_{\pi/2}\) is redundant and three measurements suffice. The reduction is conditional on that physical symmetry, not on presentation choice.

## Minimality boundary

For unrestricted complex overlap and ordinary scalar intensity detectors, four phase-resolved values are generically required to recover \(u,v,\operatorname{Re}c,\operatorname{Im}c\). A detector that directly measures exterior area \(\|b_1\wedge b_2\|^2\) could instead provide the determinant as one specialized readout, but that is a different apparatus contract.

## Verification

`research/aspect/checkers/check_optical_gram_measurements.py` reconstructs exact rational invariants and exhibits a same-\((u,v,I_0)\), different-determinant hostile.

## Disposition

The ordinary-intensity measurement problem is resolved. The required physical interface is two route-resolved intensities, a phase-stable combiner at two quadratures, and a declared target pairing. Arithmetic source data supplies none of these apparatus objects.
