# Visibility-reference calibration gate: WP1045

## Question

What extra reference row closes WP1044's visibility-gain confounder?

## Four-coordinate rank

WP1044 uses background, absolute signal, and phase-flipped coherent difference:

\[
B,
\qquad
S=B+\mathcal Lg^2,
\qquad
D=S_+-S_-=4\nu\mathcal Lg.
\]

When visibility \(\nu\) is unknown, the local coordinates are
\((B,\mathcal L,g,\nu)\). The three rows have rank three and cannot identify
all four coordinates. Add one independent reference-only visibility row:

\[
V=\nu.
\]

The row set has rank four. This is the minimal local calibration repair for
the one-amplitude model.

## Exact collision without the reference

The packets

\[
(B,\,\mathcal L,g,\nu)=(0,4,1,1/2)
\]

and

\[
(B,\,\mathcal L,g,\nu)=(0,1,2,1)
\]

share

\[
B=0,
\qquad
S=4,
\qquad
D=8.
\]

Thus the coherent difference does not separate gain from visibility unless
\(\nu\) is independently measured.

## Exact reconstruction with the reference

For \(D\ne0\), \(S>B\), and calibrated \(\nu\),

\[
g=\frac{4\nu(S-B)}{D},
\qquad
\mathcal L=\frac{D^2}{16\nu^2(S-B)}.
\]

The two collision packets reconstruct to \((\mathcal L,g)=(4,1)\) and
\((1,2)\) once their distinct visibility records are retained.

## Bad-reference falsifier

Repeating the same flavor interference contrast is not a visibility
calibration. It leaves rank three because it repeats the row
\((0,4,4,4)\). The reference must be a separate channel whose visibility is
independent of the flavor portal while sharing the same interferometer frame.

## Disposition

Productive. WP1044's visibility caveat is now a finite row requirement: add an
independent reference-only visibility row with its own background and stability
calibration. This remains an instrument target, not a physical16 source
instantiation.

Checker: `research/flavor/checkers/wp1045_visibility_reference_calibration_gate.py`

Result: `results/wp1045_visibility_reference_calibration_gate.json`
