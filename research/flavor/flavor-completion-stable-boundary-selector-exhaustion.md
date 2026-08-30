# Completion-stable boundary-selector exhaustion: WP942

## Question

After WP935--WP941, does any declared operation select the exchange-even
boundary coefficient while preserving the complete flavor source domain,
nonzero physical coupling, and calibrated experiment?

## Frozen domain and acceptance gates

The admitted state domain is the five-dimensional interval realization used
by the `SU(4)` gauge-Higgs branch, together with its complete residual
boundary operator ring and admitted matter completions.  A progressive
operation must satisfy all of:

1. act within the same source domain;
2. select or eliminate the common boundary coefficient;
3. retain a nonzero physical coupling;
4. remain stable under the complete matter realization;
5. preserve or independently rederive a calibrated instrument;
6. supply a descent into a proper family of `physical16`.

## Exhausted declared operations

| Operation | Exact outcome | First failed gate |
|---|---|---|
| `SU(4)` gauge-Higgs parent | selects link realization and pure-vector half twist | complete matter stability |
| sign, parity, endpoint exchange | leaves the even `(1,1)` coefficient line | boundary selection |
| additive or finite homogeneous RG | preserves the initial coefficient fiber | boundary selection |
| affine attractive RG | conditionally selects `-b/a`, but no complete beta system is declared | source authority |
| `S1/Z2` bulk hypermultiplets at one loop | lie in the boundary-beta kernel | boundary selection |
| generic bulk-loop counterterms | affine transport `tau_R=tau_B+L` | boundary selection |
| volume or NDA suppression | contracts sensitivity but remains injective | boundary selection |
| boundaryless circle | removes coefficient and endpoint ports together | same-domain/instrument preservation |

No row passes all six gates.  This is a relative exhaustion of the declared
branch, not a theorem against unknown UV completions.

## Cross-check against the strongest non-boundary selector

WP861 supplies a genuine conditional `physical16` selector: a complete
dark-word Yukawa grammar has a proper rank-three invariant image.  WP862 then
proves that every matrix in this family violates an exact mass-shape bound and
that none of the 1,210 fitted sheets belongs to it.  Therefore existence of a
descending selector architecture does not imply compatibility with the
physical flavor point.

The boundaryless Wilson-line branch is weaker at present: WP789 selects a
dimensionless angle conditionally but retains a radius fiber, while no
declared natural transformation maps that selected holonomy into a proper
`physical16` family with calibrated readout.  Importing WP861's map would mix
distinct source objects without an interface constructor.

## Contextual partition

On the interval branch, the largest source-authorized probe family consists
of the parent realization/parity data, the perturbative affine boundary
transport, and conditional two-momentum response tomography.  It separates
renormalized boundary packets when the loop and calibration data are fixed,
but it does not reduce the admissible source family.  The source-selection
partition therefore retains at least the one-dimensional bare `tau` fiber.

On the unmarked circle, that fiber is absent because the state domain and
instrument are different.  Two marked reference ports define a new
relational experiment over the stabilizer groupoid; they do not repair the
interval quotient.

These are categorical comparisons, not temporal or causal assertions.

## Result

The completion-stable interval boundary-selector branch closes negative
relative to all declared operations through WP941.  The smallest exact
falsifier remains the symmetry-compatible pair `tau=0,1`; perturbative
transport preserves it, volume suppression only shrinks its readout, and
boundaryless geometry deletes its instrument.

The next progressive constructor must be one of exactly two types:

1. a UV boundary law that computes the finite even coefficient and survives
   the full matter completion; or
2. a new boundaryless source whose holonomy-to-Yukawa map, `physical16`
   descent, ensemble compatibility, and calibrated instrument are derived in
   one source frame.

Reproduce with:

    uv run python research/flavor/checkers/wp942_completion_stable_boundary_selector_exhaustion.py

Generated result:
`research/flavor/results/wp942_completion_stable_boundary_selector_exhaustion.json`.
