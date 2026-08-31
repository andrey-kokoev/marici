# Degenerate pole clock fiber: WP1040

## Question

Does exact degeneracy of the \(C=23\) pole packet select the threshold clock?

## Degenerate hostile

Grant the strongest repair of WP1039 at the pole-typing level:

- \(k=2\);
- \(C=23\);
- exchange symmetry among the twenty-three operator copies;
- one exactly degenerate pole within each packet;
- residues scaled so the zero-momentum coefficient stays fixed.

The fixed zero-momentum data are

\[
h=\frac{138\pi^2}{1367},
\qquad
R(0)=23.
\]

For a degenerate pole with mass square \(M^2\), the normalized finite response
at \(q^2=1\) is

\[
\frac{R(1)}{R(0)}=\frac{M^2}{M^2+1}.
\]

Two packets satisfying all granted structure give

\[
M^2=1:\quad \frac{R(1)}{R(0)}=\frac12,
\qquad
M^2=2:\quad \frac{R(1)}{R(0)}=\frac23.
\]

Their difference is \(1/6\). Degeneracy removes the WP1039 split-spectrum
fiber but leaves the mass clock.

## Classification

The first nonfaithful arrow is

\[
\{\text{degenerate integer pole packet}\}
\longrightarrow
\{\text{physical threshold clock }M^2/q^2\}.
\]

Exchange symmetry can type one pole and equal residues, but it does not select
the pole mass in physical units or lock the detector momentum to it.

## Disposition

Negative for the degeneracy-only repair of WP1039. Reopening requires the same
source that selects \((k,C)=(2,23)\) and the pole operator to derive the common
mass clock, or a source-locked ratio \(q^2/M^2\), before `physical16`
threshold instrumentation is invoked.

Checker: `research/flavor/checkers/wp1040_degenerate_pole_clock_fiber.py`

Result: `results/wp1040_degenerate_pole_clock_fiber.json`
