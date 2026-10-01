# Effective-dimension tests of the promoted graph

## Operators and scope

Keep the paw seed and shared-endpoint promotion fixed. Measure graph geometry
at cycles0..7 using unit edge length. These are observables of the growing graph,
not the alternative rung4 ancestry-coordinate readout or a physical clock.

Volume slopes use the existing exact all-source BFS ball volumes B(r):

    d_volume(r,2r)=log[B(2r)/B(r)]/log2.

Balls include the centre and are averaged over all centres. The source artifact
is hashed in the report. For diffusion, use the lazy simple random walk with
symmetric representative

    Q=(I+D^(-1/2) A D^(-1/2))/2,
    P(t)=trace(Q^t)/N,
    d_s(t,2t)=-2 log[P(2t)/P(t)]/log2.

The clock is walk steps at fixed total stepping rate per vertex. The formula
is motivated by P(t) proportional to t^(-d/2); a finite-scale slope is not by
itself a continuum dimension. Laziness removes bipartite oscillations.

Full numerical spectra are used through cycle6 (396 vertices). Cycle7 uses64
Rademacher trace probes, removes the known stationary eigenvector, and adds
its exact1/N contribution. Seed and probe count are recorded. Correlated-time
bootstrap intervals use1000 resamples. They describe trace-estimation uncertainty,
not physical or finite-size uncertainty. The stochastic method is cross-checked
against the cycle6 full spectrum.

## Results

| Cycle | N | Volume slope r=1..2 | Diffusion slope t=4..8 |
|---:|---:|---:|---:|
|0|4|0.415|0.337|
|1|4|0.193|0.199|
|2|5|0.252|0.350|
|3|8|0.541|0.873|
|4|18|1.150|1.803|
|5|64|1.931|2.930|
|6|396|2.783|4.127|
|7|4552|3.696|5.275|

These fixed short-scale columns drift strongly across cycles. They should not
be interpreted as assigning a unique dimension to each graph.

### Finite-size and microscopic effects

The report flags diffusion intervals with t>=4 and P(2t)>=5/N. These are explicit
screening conventions, not sufficient conditions for a continuum limit. Cycle6
has only the4..8 interval meeting them. Cycle7 has4..8 and8..16, with estimates:

- 4..8:5.275, bootstrap95% interval[5.241,5.309];
- 8..16:5.059, bootstrap95% interval[4.983,5.128].

Longer walks approach the finite graph's stationary return floor and their
uncorrected dimension slopes fall toward zero. The cycle5 value2.930 occurs
where the floor already accounts for41% of the return probability at t=8.
It is not evidence of a stable three-dimensional diffusion regime.

For volume, radius2 at cycle7 covers about12.9% of the graph, but the1..2 interval
is microscopic. The2..4 slope is2.948; its outer ball covers99.7% of the graph.
Thus that near-three value is also affected by graph-wide saturation. No volume
interval simultaneously avoids the microscopic radius and the stated
quarter-graph saturation threshold in this sample.

### Calibration

A periodic64^3 cubic-lattice control has an analytically known lazy-walk
spectrum. The same diffusion diagnostic gives3.023 on32..64 steps and3.010
on64..128 steps, with ample separation from the stationary floor. The method
can therefore exhibit a three-dimensional plateau on a known3D example.

## Interpretation

The measured promoted graphs have not exhibited a stable three-dimensional
regime across cycles and observation scales. Short-scale slopes increase with
promotion; available longer scales encounter finite-size saturation. A pair
of cycle7 slopes near5 also does not establish a limiting dimension of five.

This is a constraint on this supplied graph-growth/walk/readout combination,
not a disproof of all relational models or a Planck-scale prediction. A claim
of emergent dimension needs larger well-resolved scale windows, stability under
coarse-graining, and justification of the dynamics and physical readout.

## Reproduction

```
uv run research/nima/checkers/check_growth_effective_dimension.py
```

Dependencies are declared in the script. Numerical assertions and controls
passed. All intermediate return probabilities, slopes, saturation fractions,
and stochastic uncertainty estimates are retained in
`results/growth-effective-dimension.json`.
