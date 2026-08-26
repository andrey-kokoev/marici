# Finite-bandwidth and continuum-mode completion

Owner: `marici.Aspect`

## Bounded question

Which exact gates separate a finite sampled optical calculation from a claim
about continuum modes, causal propagation, stable bandwidth, or infinite-time
readout? This packet supplies a completion contract and deliberate finite
counterexamples. It certifies no continuum limit by itself.

## Typed spaces and normalization

A finite record belongs to `C^N` with declared sample interval `T`, window,
Fourier sign, and normalization. A continuum field requires a named space such
as `L2(R)` or a causal Hardy class, a measure, boundary/radiation condition,
and a convergence map from finite records. Equal array lengths do not provide
that typing.

For the four-sample convention

`X_k=sum_n x_n exp(-2 pi i k n/4)`,

the checker proves exact Parseval normalization

`sum_n |x_n|^2=(1/4)sum_k |X_k|^2`.

This is a finite identity, not a continuum Plancherel theorem.

## Sampling and aliasing

At sample interval `T=1`, normalized frequencies `1/4` and `5/4` give the
same four samples. A sampled detector therefore factors frequency through
equivalence modulo the sampling rate. Continuum frequency identity requires a
source-derived bandlimit and an anti-alias filter; sampling alone is not
faithful.

## Finite detector bandwidth

A detector that retains only declared bins `(0,1)` maps spectra
`(1,2,3)` and `(1,2,-3)` to the same record. The out-of-band component remains
part of the source field. A finite-band detector can be faithful only on a
predeclared bandlimited source class, never on the unrestricted spectrum.

## Causality and impulse response

The causal finite impulse response `h=(1,1/2,1/4)` produces output samples
only from present and past inputs. A coefficient at delay `-1` makes `y_0`
depend on `u_1`; two inputs with identical past but different future then give
different present output. Frequency-response fitting without a causal impulse
response can therefore conceal advanced dependence.

## Window tails and stability

For the stable infinite impulse response `h_n=2^-n`, total energy is `4/3`.
The first three samples contain `21/16`; the omitted tail is exactly `1/48`.
Treating the finite record as complete silently discards that energy.

Stability and continuum resolvent control require uniform bounds. The family
`K(epsilon)=diag(1,epsilon)` is invertible for every positive epsilon, but
`||K(epsilon)^-1||>=1/epsilon`. Any finite sample set has a finite maximum,
while `epsilon=1/n` makes the bound diverge. Pointwise invertibility is not a
uniform completion certificate.

## Infinite-time readout

Two sequences can agree on every sample in a chosen finite prefix yet have
different infinite-time means: one may remain zero, while the other becomes
one after the observation window. No finite prefix alone authorizes an
infinite-time limit. A convergence theorem needs a declared topology,
uniform-integrability or domination hypothesis where relevant, and a bound
that is independent of the cutoff.

## Environment and detector kernel

Bandwidth projection, temporal windowing, and loss all have kernels. Omitted
modes must remain typed as unresolved source components or environment ports.
They cannot be renamed zero merely because the retained detector record is
zero. Noise spectral density additionally requires a normalization per unit
bandwidth; a finite covariance number cannot be reused as a spectrum without
that measure factor.

## Completion contract

A continuum or infinite-time promotion requires all of:

1. source and target function spaces with measures and port metrics;
2. Fourier, sampling, and window conventions;
3. a source-derived bandlimit or an explicit anti-alias filter;
4. a causal impulse response or causal analytic transfer prescription;
5. uniform operator/resolvent and tail bounds across the cutoff family;
6. convergence topology and a cutoff-independent error estimate;
7. detector impulse response, noise spectral density, and integration law;
8. explicit environment modes and inaccessible detector kernels;
9. singular-frequency, resonance, and limiting-absorption dispositions.

## Hostile falsifiers and claim boundary

The checker rejects: continuum frequency identity from samples; full-field
reconstruction from finite bandwidth; causality from a fitted frequency row;
zero tail from a finite window; uniform stability from pointwise inverses; and
an infinite-time mean inferred from a finite prefix.

Run `python research/aspect/checkers/finite_bandwidth_continuum_completion.py`.
The result is
`research/aspect/results/finite_bandwidth_continuum_completion.json`.
