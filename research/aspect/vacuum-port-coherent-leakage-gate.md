# Vacuum-port coherent-leakage gate

## Question

Does a small ancillary photon-number bound certify the vacuum port used by the
partial sewing constructor?

## Exact hostile

No. With visible amplitude `3/5`, complementary amplitude `4/5`, and ancillary
occupation at most `1/100`, a coherent ancillary displacement may have
amplitude `1/10`. Its interference term is bounded by

\[
2\frac35\frac45\frac1{10}=\frac{12}{125}.
\]

The population contribution is only

\[
\frac{16}{25}\frac1{100}=\frac4{625}.
\]

Thus number-only calibration sees the smaller quadratic term while leaving a
linear coherent contamination. Their combined bound is `64/625`.

The intended visibility at source coherence `3/5` and round-trip factor `9/25`
is `27/125`. Without first-moment control, its certified floor falls to
`71/625`.

## Repair

Randomize the ancillary phase independently on every heralded trial and retain
the phase key until the raw records are immutable. Interleave blocked-source
balanced-homodyne samples to test both ancillary quadrature means. Under the
phase-randomized null, the coherent cross term averages to zero and the
remaining contamination is bounded by `4/625`. The target visibility floor is
then `131/625`.

For a finite drift-resistant implementation, use the companion ABBA phase
twirl. Independent random signs cancel only in expectation; the four-shot ABBA
word cancels constant and linear leakage exactly within each completed block.

The vacuum admission gate therefore requires both:

- a number or click bound on ancillary occupation;
- a first-moment null established by quadrature monitoring or declared phase
  randomization.

Neither substitutes for retaining the complementary output record.

## Falsification

The vacuum-port model fails if either quadrature mean exceeds its frozen null
bound, phase keys correlate with source or analyzer settings, complementary
occupation exceeds `1/100`, or observed visibility lies outside the resulting
contamination interval.

## Disposition

The physical ancillary carrier is now distinguished from an arbitrary weak
input. A low-intensity coherent field is not admitted as vacuum.

## Verification

Run:

```text
python research/aspect/checkers/check_vacuum_port_coherent_leakage_gate.py
```
