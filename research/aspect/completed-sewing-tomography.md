# Completed sewing tomography compiler

## Minimal instrument size

The missing completed sewing cannot remain an unnamed scalar. Its presently
required channels are primitive, prime-square, seam, endpoint, connected-tail,
and archimedean. Assigning only one scalar coordinate to each already gives a
six-dimensional port space in each reciprocal sector.

Both directions must be measured independently. Calling one measured map's
matrix inverse the reverse constructor would assume the coherence law being
tested.

With a common phase reference, the minimal finite design is simple:

- inject each of the six typed basis ports into `J_forward`;
- read both quadratures at all six outputs;
- repeat for `J_reverse`.

This uses twelve input settings and yields 144 real quadrature observations.
The realified design has rank 144. Omitting any one typed input loses twelve
real ranks, so no remaining channel can infer it.

## Why coherent tomography matters

Intensity-only phase retrieval requires the six basis probes plus two probes
for every unordered pair: a pair sum and a quarter-turn pair. That is 36
preparations per direction, or 72 total. Even then each output row retains an
independent phase unless the detector supplies a common coherent reference.
Those phases matter when outputs are sewn into the opposite node.

Thus coherent heterodyne tomography reduces the preparation count by a factor
of six and closes precisely the phase blindness shared by optical and theta
determinant projections.

## Acceptance tests

After reconstruction, test separately:

- full matrix unitarity in the frozen source metric;
- `J_reverse J_forward=I`;
- preservation of every typed subspace and declared incidence direction;
- environment-port closure;
- cutoff transport without post-hoc whitening.

The six-dimensional count is a lower bound, not a claim that every typed
channel is one-dimensional. Source-derived multiplicities may enlarge the
apparatus. The tomography measures a supplied sewing; it does not manufacture
source authority for one.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_completed_sewing_tomography.py
```
