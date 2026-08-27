# Relational fringe versus Bell nonlocality

## Question

Does the local-zero, joint-nonzero signature of the `2(3+2+1)+1` instrument
already establish nonclassicality?

## Answer

No. Relational coherence and Bell nonlocality are distinct thresholds.
Correlated classical phase noise can preserve a joint parity fringe while both
local phase averages vanish. The outer sewing fringe establishes relational
coherence, not by itself the impossibility of a local hidden-variable model.

## Four-setting extension

Give each wing two late, independently randomized analyzer settings. For the
standard optimal geometry, the four correlators obey

\[
E_{00}=E_{01}=E_{10}=\frac{\gamma}{\sqrt 2},
\qquad
E_{11}=-\frac{\gamma}{\sqrt 2}.
\]

Hence the CHSH value satisfies the exact rational comparison

\[
S^2=8\gamma^2.
\]

Bell violation occurs exactly when

\[
\gamma^2>\frac12.
\]

This avoids numerical treatment of the square root.

## Two regimes in the existing apparatus

At `gamma = 3/5`, the relational fringe has visibility `3/5`, but

\[
S^2=\frac{72}{25}<4.
\]

At `gamma = 4/5`,

\[
S^2=\frac{128}{25}>4.
\]

The first regime demonstrates coherence stored in the relation while remaining
Bell-local at this noise level. The second rejects the local hidden-variable
bound under the Bell causal contract.

## Combined experiment

Use the same paired source and full herald-normalized record for two sealed
modules:

1. the sewing module scans the joint phase and estimates relational
   visibility;
2. the Bell module randomly chooses two settings per wing and estimates all
   four unconditional correlators.

Setting bits must be generated after pair emission, recorded independently,
and kept outside the source and opposite-wing light cones until detection.
Every herald, single click, double click, and no-click remains in the outcome
alphabet. The correlated-phase census runs in the same epoch.

The ideal coherence threshold is not sufficient when detectors miss heralded
photons. The companion no-click checker derives the additional efficiency
gate for the declared deterministic assignment of missing outcomes.

The combined checker asks two different questions:

- Is there a coherent relational port?
- Can any Bell-local source explain its four-setting behavior?

## Deutschian result

The architecture produces an explanatory hierarchy rather than treating every
correlation as the same phenomenon. A possible sewing transformation explains
the relational fringe. A family of incompatible local measurement constructors
and the CHSH obstruction tests whether that relation admits a Bell-local
replacement.

## Falsification

The quantum prediction fails if the four correlators do not follow the signed
optimal pattern after independently measured visibility and analyzer errors
are applied. The nonlocal conclusion fails if the complete unconditional data
do not exceed the preregistered Bell bound. A sewing fringe below the threshold
remains relational coherence; it is not promoted to Bell nonlocality.

## Disposition

The `2(3+2+1)+1` apparatus supports two nested claims with separate gates.
This prevents classical correlated phase noise from being mistaken for a Bell
result while preserving it as a genuine relational-channel diagnostic.

## Verification

Run:

```text
python research/aspect/checkers/check_relational_fringe_bell_boundary.py
```
