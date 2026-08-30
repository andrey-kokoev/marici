# Spin(5) coupling minimality correction (WP905)

## Defect

WP903 treated width-dependent random-draw desynchronization as a falsifier of
WP902's coupling. That was too strong. WP902 only needs a joint distribution
of the two completed outputs with the correct arm marginals. It does not need
coordinate-by-coordinate identity of latent physical draws.

If (X) and (Y) are defined on any common probability space, then for every
output event (A),

\[
|\Pr(X\in A)-\Pr(Y\in A)|
\leq \Pr(X\ne Y).
\]

Taking the supremum over (A) gives

\[
d_{\rm TV}(P_X,P_Y)\leq\Pr(X\ne Y).
\]

No semantic alignment assumption appears. Different control flow can consume
the common random stream differently and still define a coupling.

## Exact hostile enumeration

The checker enumerates every pair of binary-output maps from a four-atom
uniform seed space: (16^2=256) joint constructions. It verifies the coupling
inequality exactly in every case, including maps with deliberately permuted
seed semantics. It separately verifies that incorrect marginal generation is
a genuine failure.

This separates three gates:

1. **Validity:** both arm outputs have their declared marginals.
2. **Reproducibility:** the seed/configuration manifest recreates the same
   joint experiment.
3. **Efficiency:** the chosen coupling makes disagreement rare enough for the
   zero-discordance WP902 budget to be plausible.

WP904's semantic random field strengthens gate 3 and makes the coupling easier
to audit, but it is not necessary for gate 1.

## Revised instrument boundary

A shared CMSSW seed or restored state can instantiate a legitimate coupling
even when a width-dependent branch changes later draw meaning, provided both
arms are reproducible and independently validated against their target
marginals. What remains absent is an executed two-arm sample and those
marginal-validation records. Zero observed discordance may also be extremely
unlikely under a poor coupling; that is a power or cost failure, not a
validity failure.

The smallest exact validity falsifier is one arm with the wrong marginal. The
smallest reproducibility falsifier is one manifest replay mismatch. The
smallest efficiency falsifier for WP902's planned zero-discordance run is one
observed discordance, which prevents use of its zero-count formula but does
not invalidate the coupling.

This correction changes no selector conclusion. The experiment remains a
detector-response stability test, neither selector nor rigidifier.

Run:

~~~text
uv run python research/flavor/checkers/wp905_spin5_coupling_minimality_correction.py
~~~
