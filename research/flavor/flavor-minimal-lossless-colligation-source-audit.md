# Minimal Lossless Colligation Source Audit

## Question

Can one minimal lossless source colligation jointly derive the asymmetric
portal ray, its basin, threshold survival, and its complementary readout?

## Claim boundary

Use the three-state source packet consisting of an absent state (e_0) and
two endpoint ports.  For (|z|=1), define the reciprocal bright and dark rays

\[
b_z=\frac{(1,\bar z)}{\sqrt2},
\qquad
d_z=\frac{(-z,1)}{\sqrt2}.
\]

For (0\leq q<1), the Kraus family

\[
A_0=P_{d_z}+\sqrt q P_{b_z},
\qquad
A_1=\sqrt{1-q}\,|d_z\rangle\langle b_z|,
\qquad
A_2=|d_z\rangle\langle e_0|
\]

is trace preserving and therefore has a lossless Stinespring dilation.  Its
channel has the unique stationary state (P_{d_z}).  Every normalized input
converges to that state; its nontrivial eigenvalues are

\[
\sqrt q,\quad \sqrt q,\quad q.
\]

The same reciprocal junction has orthonormal output rows

\[
r_b=\frac{(1,z)}{\sqrt2},
\qquad
r_d=\frac{(-\bar z,1)}{\sqrt2},
\]

so the selected ray is dark at the bright port and has unit amplitude at the
complementary port.  Thus a single unitary completion can contain selection,
a global basin, and a source-level readout.

This does not yet make the required portal unavoidable.  The family retains
two exact source moduli:

- (z) changes the selected relative phase while preserving reciprocity,
  losslessness, Kraus rank, and the channel spectrum;
- (q) changes the convergence rate while preserving the selected ray and
  every structural property above.

Minimal Stinespring dilation is unique only after the channel is fixed; it
does not select the channel from the family.  Consequently it cannot supply
the missing reverse arrow from general lossless architecture to the desired
portal.

Threshold survival is likewise conditional.  If the endpoint projector is a
superselection projector for the complete colligation, it is reducing and the
state and both readout rows transport isometrically.  A full unitary that
mixes one endpoint with a heavy state remains lossless but violates reduction
and attenuates the selected ray.  Losslessness alone therefore does not prove
WP860's threshold hypothesis.

Finally, unit complementary amplitude is a source normalization, not a
detector calibration.  No map from this port to an experimentally calibrated
`physical16` record follows from Stinespring dilation.

## Smallest exact falsifier

At fixed (z=i), the channels (q=0) and (q=1/4) have the same unique dark
ray and three-Kraus lossless realization but different basin spectra.  At
fixed (q=1/4), (z=1) and (z=i) have identical channel spectra and
reciprocal weights but select distinct rays.  These two pairs prove that
minimal lossless dilation fixes neither the relative sign nor the RG basin.

## Disposition

Negative as a source principle, positive as an interface architecture.  One
colligation can implement selector, basin, and complementary source readout,
but only after (z), (q), the reducing threshold projector, and detector
calibration have been supplied.  It packages the desired answer without
explaining those data.  A progressive successor must derive the channel—not
merely its unitary dilation—from a microscopic flavor symmetry, locality law,
or anomaly-protected boundary condition.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp865_minimal_lossless_colligation_source_audit.py
```
