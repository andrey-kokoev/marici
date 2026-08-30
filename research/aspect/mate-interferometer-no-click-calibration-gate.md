# Mate-interferometer no-click calibration gate

## Question

Can phase- and route-dependent detector loss make late conditioning look like
coherent reverse incidence in the path–marker mate interferometer?

Yes. Click-only postselection admits an exact false positive.

## Smallest hostile

Take a genuinely flat unconditional signal:

\[
p_+(\phi)=p_-(\phi)=\frac12.
\]

At the four phase samples, let the two detector efficiencies be

```text
eta_plus  = 1,   3/4, 1/2, 3/4
eta_minus = 1/2, 3/4, 1,   3/4.
```

If no-click heralds are discarded and the remaining clicks are normalized,
the apparent plus-port curve is

\[
\frac23,\quad\frac12,\quad\frac13,\quad\frac12.
\]

This is exactly

\[
\frac{1+(1/3)\cos\phi}{2}.
\]

A flat state plus structured loss is therefore behaviorally identical, on the
click-conditioned projection, to a coherently uncomputed state with visibility
one third.

## Full output law

For a heralded trial with underlying plus probability `p`, the typed outcomes
are

\[
p(C_+)=\eta_+p,
\qquad
p(C_-)=\eta_-(1-p),
\]

and

\[
p(N)=1-p(C_+)-p(C_-).
\]

The no-click outcome `N` is part of the detector instrument. Dropping it is a
nonfaithful output projection, not an innocent normalization.

With a live efficiency manifest, the source probabilities are recovered by

\[
p=\frac{p(C_+)}{\eta_+},
\qquad
1-p=\frac{p(C_-)}{\eta_-}.
\]

The hostile then reconstructs the exact flat curve and zero visibility.

## True coherent control

For a genuinely coherently uncomputed state with environment overlap
`gamma=3/5`, the true curve is

```text
4/5, 1/2, 1/5, 1/2.
```

The same detector hostile distorts the click-conditioned curve to

```text
8/9, 1/2, 1/9, 1/2,
```

inflating visibility from `3/5` to `7/9`. Full efficiency inversion recovers
the original curve and exact visibility `3/5`.

## Placement in `3+2+1`

The robustness gate expands, rather than changes, the architecture:

- **Input:** heralded path–marker trials and the declared environment-overlap
  family.
- **Output:** click-plus, click-minus, no-click, marker record, and immutable
  herald key.
- **Control:** phase, randomized route, detector efficiencies, acquisition
  window, and calibration epoch.
- **Forward witness:** the source and detector instruments construct the full
  outcome law.
- **Backward witness:** conditioning selects marker and detector record fibers.
- **Mate:** calibrated totalization over every output recovers the invariant
  unconditional signal law.

Click-only normalization attempts to form the mate after quotienting away the
no-click fiber. The resulting square does not commute.

## Laboratory requirements

1. Count every herald, including trials with no signal click.
2. Calibrate both detector efficiencies at every phase sample and route.
3. Bind the calibration manifest to the acquisition epoch.
4. Randomize routes within that epoch rather than measuring them in separate
   drifting blocks.
5. Report raw herald-normalized outcomes before efficiency inversion.
6. Reconstruct the unconditional law using both detector ports.
7. Treat singular or unbounded efficiency inversion as a failed completion
   gate, not as missing data to discard.

## Result

The original causal discriminator remains valid only on the full calibrated
instrument. An apparent unconditional fringe in click-postselected data does
not establish coherent reverse incidence.

## Claim boundary

This is an exact finite single-photon loss hostile. Dark counts, multipair
emission, dead time, afterpulsing, timing-window bias, and continuum
photodetection remain additional completion gates.

## Verification

Run:

```text
python research/aspect/checkers/check_mate_interferometer_no_click_calibration_gate.py
```
