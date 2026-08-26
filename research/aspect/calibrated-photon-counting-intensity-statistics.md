# Calibrated photon counting and intensity statistics

Owner: `marici.Aspect`

## Bounded question

Which source distinctions survive number-resolving counts, threshold clicks,
finite efficiency, dark counts, temporal integration, and intensity-only
readout? This packet fixes a finite photon-number class and exact probability
laws. It does not claim a microscopic detector or continuum point-process
completion.

## Source and POVM authority

The source class is the Fock basis on one declared temporal, spatial,
polarization, and frequency mode. An ideal number-resolving detector uses
effects `Pi_n=|n><n|`. These effects recover the diagonal photon-number
distribution but are blind to off-diagonal phase coherence. A finite outcome
alphabet must include an overflow effect; silently dropping `n>N` makes the
POVM incomplete on the declared source space.

Threshold detection instead has outcomes `no click` and `click`, with every
positive photon number mapped to the same ideal click. It cannot distinguish
one photon from two and is not number resolving.

## Efficiency and environment

Loss before an ideal counter is a beam-splitter channel with inaccessible
environment output. For input photon number `n` and intensity efficiency
`eta`, detected counts are binomial:

`P(k|n)=binomial(n,k) eta^k (1-eta)^(n-k)`.

The checker uses `n=2` and `eta=9/25`, corresponding to retained amplitude
`3/5`. The probabilities for `k=0,1,2` are `256/625`, `288/625`, and
`81/625`; they normalize exactly. Missing photons occupy the environment and
cannot be called absent from the source.

## Dark counts and covariance

An independently calibrated Bernoulli dark event with probability `d=1/10`
convolves with the optical count distribution. The observed mean is
`41/50`; the variance is `1377/2500`. Subtracting the mean dark rate does not
undo its variance or recover event identities. Afterpulsing, dead time, and
correlated backgrounds violate this independent convolution and require a
larger detector state.

## Intensity and higher moments

The certain one-photon state and an equal mixture of zero and two photons both
have mean count one before loss, but their variances are zero and one. Their
second normalized factorial correlations differ: `g2=0` and `g2=1`.
Therefore mean intensity does not determine photon statistics.

Intensity is also invariant under a global optical phase. The distinct field
amplitudes `(3/5,4/5)` and its quarter-turn `(-4/5,3/5)` both have intensity
one. A local oscillator or another coherent phase reference is required for
phase-sensitive recovery.

## Temporal gate and detector kernel

Integrated counts erase arrival order. Records `(1,0)` and `(0,1)` in two
time bins have the same total count but different temporal modes. Time-resolved
effects are required if arrival structure is part of the source class.

On diagonal states supported on photon numbers `0..N`, a number-resolving
family with all `N+1` outcomes is faithful. It remains invisible to number
coherences. On a larger space, an overflow outcome preserves normalization but
does not resolve the distribution within the overflow subspace.

## Hostile falsifiers

- threshold clicks are called number resolving;
- lost counts are called absent source photons;
- mean dark rate subtraction is called noise removal;
- equal mean intensities are used to identify photon statistics;
- intensity is used as absolute phase readout;
- integrated counts are used to reconstruct arrival order;
- a truncated counter omits its overflow effect.

## Completion boundary

A continuum counting model requires a detector instrument or quantum
trajectory, response kernel, recovery/dead-time state, afterpulse law,
time-tag resolution, spectral mode response, stationary or nonstationary dark
process, and convergence from finite bins to a point process. Exact finite
probabilities here do not supply that completion.

Run `python research/aspect/checkers/calibrated_photon_counting_intensity_statistics.py`.
The result is
`research/aspect/results/calibrated_photon_counting_intensity_statistics.json`.
