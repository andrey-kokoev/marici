# Path–marker mate-interferometer preregistration

## Question

What frozen laboratory contract distinguishes late record conditioning from
coherent pre-detection reverse incidence without allowing detector loss,
calibration drift, or post hoc fiber selection to decide the result?

## Frozen design

Each heralded photon is assigned by a predeclared pseudorandom schedule to a
route, phase, and environment-overlap setting. The three routes are untouched,
late conditioning, and coherent marker uncomputation. A fourth timing control
applies the same nominal uncomputation only after the signal record is formed.

The phase grid is zero, one quarter turn, one half turn, and three quarter
turns. The environment-overlap settings are one, three fifths, and zero.

Every trial retains:

- its immutable herald key;
- route, phase, and environment setting;
- click-plus, click-minus, or no-click signal record;
- marker record and marker-reset probe;
- calibration epoch.

Analysis labels remain sealed until both raw records and the calibration
manifest are immutable.

## Primary laws

For environment overlap `gamma` and phase cosine `c`, the preregistered
probabilities are:

\[
p_{\rm untouched}=\frac12,
\]

\[
p_{\rm conditioned,+}=\frac{1+\gamma c}{2},
\qquad
p_{\rm conditioned,-}=\frac{1-\gamma c}{2},
\]

and

\[
p_{\rm coherent}=\frac{1+\gamma c}{2}.
\]

The two conditioned fibers must totalize to one half. The post-record timing
control must produce zero change. The coherent route must reset the accessible
marker. At zero environment overlap, coherent recovery must remain flat.

## Statistical contract

There are forty-eight primary proportions: three environment settings, four
phases, and four estimands per cell. Each proportion requires at least 500,000
effective trials after its declared conditioning, with absolute tolerance one
twentieth.

For any Bernoulli proportion, the variance of its empirical mean is at most
`1/(4N)`. Chebyshev’s inequality followed by the union bound gives familywise
error at most

\[
\frac{48}{4(500000)(1/20)^2}
=
\frac{6}{625},
\]

which is below one percent. This is the frozen conservative error budget; it
cannot be replaced after seeing the curves.

## Calibration interlock

Both signal-port efficiencies must be at least one half, so efficiency
inversion is bounded by two. Every route must share the same phase reference
and calibration epoch. Routes are randomized within an epoch rather than
collected in separate drifting blocks.

A missing no-click stream, stale epoch, singular efficiency, or route-specific
acquisition window rejects the run before physical interpretation.

## Acceptance

The experiment passes only if all ten gates in the contract pass together:

1. every required record field is present;
2. the full outcome law is retained;
3. calibration epochs match;
4. efficiency inversion is bounded;
5. minimum effective counts are met;
6. all primary laws meet the frozen tolerance;
7. conditioned fibers totalize;
8. the post-record control is invariant;
9. the coherent route resets the marker;
10. orthogonal environment leakage blocks recovery.

No single fringe is a pass.

## Deliberate failures

The conformance checker rejects three fixtures:

- click-only normalization with the exact fake visibility-one-third fringe;
- a mathematically correct dataset bound to a stale calibration epoch;
- conditioned fringes reported as coherent actuation while the unconditional
  coherent route remains flat.

## Disposition

This contract converts the finite mate theorem into a falsifiable acquisition
and analysis object. Passing establishes the operational difference between
conditioning and coherent uncomputation on the declared single-photon probe
family.

## Claim boundary

Dark counts, multipair emission, dead time, afterpulsing, jitter, and continuum
photodetection require successor contracts.

## Verification

Run:

```text
python research/aspect/checkers/check_path_marker_mate_interferometer_preregistration.py
```
