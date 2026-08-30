# Path–marker mate interferometer

## Objective

Build one exact optical instrument that distinguishes three operations often
compressed into the word “erasure”:

1. formation of a path–marker joint state;
2. late classical conditioning on a marker record;
3. coherent marker-to-path reverse incidence before signal detection.

The first two already explain the delayed-choice quantum eraser. The third
turns the architectural distinction into an intervention.

## Source and ports

Prepare the path–marker state

\[
\lvert\Psi\rangle
=
\frac{\lvert00\rangle+\lvert11\rangle}{\sqrt2}.
\]

The first qubit is the interferometer path. The second is a polarization,
frequency, or spatial marker. A phase-controlled balanced path analyzer
records the signal output. The marker can be measured in its complementary
basis and joined to the signal record by immutable trial identifiers.

## Three routes

### Untouched joint evolution

Forgetting the marker gives a maximally mixed path state. Each signal output
has probability one half at every phase. The phase is absent from the local
behavioral quotient but remains in the joint path–marker correlations.

### Late record conditioning

Conditioning on complementary marker records produces a fringe and
antifringe. At phase `phi`, their signal-plus probabilities are

\[
p_{\pm}(+\mid\phi)
=
\frac{1\pm\cos\phi}{2}.
\]

Their equally weighted total is one half. Conditioning changes the selected
fiber of the existing record object; it does not change the earlier marginal.

### Coherent reverse incidence

Before signal detection, apply a path-controlled marker flip:

```text
|00> -> |00>
|11> -> |10>.
```

It transforms the entangled state into

\[
\frac{\lvert0\rangle+\lvert1\rangle}{\sqrt2}
\otimes\lvert0\rangle.
\]

The path state now has full local coherence. Unconditional signal counts show
the fringe directly. This is a physical constructor: moving it after the
signal record is formed preserves the stored record probability by trace
invariance and cannot rewrite it.

## The mate distinction

Late conditioning and coherent uncomputation produce the same ideal fringe
shape in one selected channel, but they have different totalization laws:

```text
conditioned fringe + conditioned antifringe -> flat marginal
coherent uncompute -> unconditional fringe
```

That difference is the operational signature separating a backward record
map from reverse physical incidence.

In the `3+2+1` architecture:

- input, output, and control type the source, records, and phase/timing frame;
- the forward witness constructs the joint path–marker record;
- the backward witness conditions that record into complementary fibers;
- the mate totalizes those fibers to the invariant marginal;
- coherent uncomputation is an additional executable control constructor, not
  the backward witness itself.

## Environment hostile

Let inaccessible environment states correlated with the two paths have overlap
`gamma`. After tracing the environment, the off-diagonal path–marker terms are
scaled by `gamma`. Exact probabilities become

\[
p_{\pm}(+\mid\phi)
=
\frac{1\pm\gamma\cos\phi}{2}
\]

for conditioned fibers, while coherent uncomputation gives unconditional

\[
p_{\rm coh}(+\mid\phi)
=
\frac{1+\gamma\cos\phi}{2}.
\]

Thus accessible marker manipulation cannot recover coherence deposited in an
orthogonal environment. At `gamma=0`, both conditioned and coherently
uncomputed patterns are flat. At `gamma=3/5`, both have visibility `3/5`, but
only the coherent route changes the unconditional counts.

## Laboratory design

Use a heralded single-photon path qubit and polarization marker. Randomly route
each heralded trial into one of three predeclared branches:

1. direct signal analysis;
2. signal analysis plus delayed complementary marker measurement and classical
   time-tag join;
3. path-controlled marker flip followed by unconditional signal analysis.

Use the same phase reference, detector pair, trial-key format, and acquisition
window for all branches. Reconstruct both conditioned fibers in branch two,
not only the visually favorable fringe. In branch three, verify marker reset
tomographically and scan controlled environment leakage or mode mismatch.

The decisive report contains four curves on one phase grid:

- untouched unconditional signal;
- conditioned fringe;
- conditioned antifringe;
- coherently uncomputed unconditional signal.

## Falsifiers

- Conditioning changes the unconditional stored signal marginal.
- The two conditioned fibers fail to totalize to that marginal.
- A nominally coherent pre-detection route changes only postselected records.
- A post-detection unitary changes an already registered signal probability.
- Orthogonal inaccessible leakage permits full local-coherence recovery.
- Route-dependent phase, loss, or time-window calibration can account for the
  claimed distinction.

## Claim boundary

This is an exact finite instrument contract and a feasible optical design. It
does not supply a loophole-free spacelike experiment, a detector-memory model,
or a continuum photodetection theorem. It explains the causal difference
between conditioning and coherent uncomputation within standard quantum
mechanics; it does not select an interpretation of measurement.

## Verification

Run:

```text
python research/aspect/checkers/check_path_marker_mate_interferometer.py
```
