# Two-point background-drift robustness (WP373)

## Stronger nuisance model

WP372 assumed one differential background shared by both scan settings. Allow
independent differential offsets \(\delta_0(1,-1)^T\) and
\(\delta_1(1,-1)^T\) at the two masses \(L\) and \(L+d\).

The four observations now depend on four local parameters

\[
(L,\Omega,\delta_0,\delta_1).
\]

The exact four-by-four Jacobian determinant is

\[
\frac{4\Omega c^2d(L^2+Ld+\Omega^2)}
{(L^2+\Omega^2)^2((L+d)^2+\Omega^2)^2}.
\]

It is strictly positive for \(L,\Omega,c,d>0\). Two distinct contexts
therefore identify the pole packet even when the differential background
drifts independently between them.

## Context can replace channel complementarity

Apply the WP370 confusion matrix separately at both settings and add the
differential backgrounds after detector mixing. The determinant is unchanged
for every contrast, including zero. The nuisance columns occupy the two
difference-channel directions, while \((L,\Omega)\) are identified by the two
common-channel sums across distinct source settings.

Thus complete channel confusion need not destroy pole identification once a
second source-supported context is present. This does not contradict WP370:
WP370 concerned one context and recovery of both threshold-channel values.
WP373 identifies the two pole parameters from two common-channel values and
does not reconstruct each point's absorptive/dispersive split in the presence
of free differential drift.

## True drift obstruction

If each setting also receives an independent common-mode offset, there are six
local parameters for four records. The augmented Jacobian has rank four and a
two-dimensional kernel. Arbitrary two-component background drift can absorb
the source information. Distinct contexts repair only the nuisance family
they overdetermine.

## Disposition

WP373 strengthens the threshold instrument: shared differential background
is not required. The smallest exact scan falsifier remains \(d=0\); the
smallest drift falsifier is admitting independent common and differential
offsets at every setting. The result improves source identification only and
does not select a flavor value or restore full `physical16` faithfulness.

Run `uv run --with sympy python
research/flavor/checkers/wp373_two_point_background_drift_robustness.py` to
regenerate the exact result.
