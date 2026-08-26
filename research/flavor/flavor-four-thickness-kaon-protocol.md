# Four-thickness kaon no-refit protocol (WP408)

## Intervention schedule

Fix carbon composition, kaon momentum, beam preparation, geometry, decay
selection, and detector calibration. Manufacture four certified column
thicknesses $0,t,2t,3t$ from the same homogeneous stock. Randomize runs across
the four settings, but seal every $3t$ event identifier before fitting.

At each open setting measure the two-component complex regeneration shift. Fit
the declared completion

\[
s(x)=b_0+b_1x+b_2x^2
\]

to $x=0,1,2$. The exact design determinant is nonzero. The second divided
difference $s(0)-2s(1)+s(2)$ tests the quadratic coefficient before the withheld
sample is opened.

## Frozen displacement

Polynomial interpolation fixes the complex $3t$ displacement without refitting:

\[
s(3)=s(0)-3s(1)+3s(2).
\]

The same weights propagate the full two-component covariance. After adding the
independently calibrated covariance of the sealed $3t$ record, compare the
complex residual with a predeclared Mahalanobis threshold. Unseal once. A failed
record rejects the frozen transfer packet; it cannot add a cubic term, change
the material mixture, or refit the open contexts.

## Completion typing

- Quadratic density corrections are included and tested by the three open
  settings.
- Finite widths and exact coherent multiple interaction are carried by WP406's
  transfer matrix at every thickness.
- Extra material species are excluded by assay or included as separately
  calibrated noncollinear forward-amplitude directions.
- Nonlinear detector response is calibrated with randomized settings and
  source-off controls; it is not absorbed into $b_2$ without a named interface.
- Cubic source response or additional species define a predeclared successor,
  not an after-unblinding rescue.

## Current evidence boundary

CPLEAR provides the real carrier, physical carbon operation, and rank-two
complex calibration, but only at absorber absent/present. KTeV's compound
regenerator and CPLEAR momentum bins do not supply three carbon thicknesses at
fixed momentum and composition. WP408 is therefore executable and statistically
typed, but not executed.

Run `uv run --with sympy python
research/flavor/checkers/wp408_four_thickness_kaon_protocol.py` to regenerate
the JSON result.
