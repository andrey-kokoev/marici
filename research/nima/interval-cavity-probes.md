# Three conditional optical probes identify the finite interval process

## Result

The three probes proposed in `interval-cavity-probe-protocol.md` distinguish all six interval processes at m=3, using the **existing** passive photon lift and ready/dead detector outcome maps. Every proper subset of this particular three-probe family fails to distinguish at least two intervals.

This constructs a conditional observation interface, not calibrated hardware. The physical preparation/routing binding is new and remains assumed. The theorem concerns repeated-trial probability distributions under a canonical six-process promise; it does not identify an interval exactly from one trial or certify arbitrary process operators.

## Actual instrument comparison

In a separate trial for each k, prepare one photon at u_k=1+3k, every other optical mode vacuum, and the detector ready. Apply E(i,j), then measure slot u_k. The checker applies both actual Kraus outcome maps to the evolved one-photon state and computes their unnormalized masses. Every C/N pair sums to one.

Define A=81/625 and B=9/25. The click vectors are:

| Interval | Probe 0 | Probe 1 | Probe 2 |
|---|---|---|---|
| [1,1] | A | B | B |
| [1,2] | A | A | B |
| [2,2] | B | A | B |
| [1,3] | A | A | A |
| [2,3] | B | A | A |
| [3,3] | B | B | A |

No-click probabilities are their complements. Independently, the passive process has incident-slot return amplitude -3/5 on selected rounds and 1 otherwise. Multiplying the resulting occupation probability by eta=9/25 gives exactly the actual instrument calculation.

The low coordinates recover the nonempty contiguous round mask. Reconstructing its endpoints recovers the complete actual n=8 compiler record, including diagonal boundary updates. The checker compares complete record objects, not only endpoint labels.

All three probes are needed **within this candidate family**. Examples:

- omit probe 0: [1,2] and [2,2] coincide;
- omit probe 1: [1,1] and [1,2] coincide;
- omit probe 2: [1,2] and [1,3] coincide.

All seven proper subsets have explicit collision witnesses in the receipt. No minimum over all possible physical observables is claimed.

## Calibration theorem and separation bound

An actual identity/bypass exposure with the same supplied ready detector gives reference click rate b_k=9/25 at every port.

Separately, suppose independently justified static multiplicative factors a_k>0 are shared by reference and interval exposures. Then

    c_k=a_k t_k,  b_k=a_k,  t_k in {9/25,1},

so c_k/b_k=t_k. The factors may differ between ports; they must not change between the matched reference and validation exposures. Unverified preparation, readiness or path-dependent loss need not satisfy this assumption. A measured reference must be independently justified, not fitted to the interval response.

If both rate estimates have absolute error at most epsilon, and a_k>=a_min>epsilon, write c_hat=a_k*t_k+delta_c and b_hat=a_k+delta_b. Then

    |c_hat/b_hat-t_k|
      = |delta_c-t_k delta_b|/|a_k+delta_b|
      <= epsilon(1+t_k)/(a_min-epsilon)
      <= 2 epsilon/(a_min-epsilon).

This is an analytic bound for all admitted errors, not a conclusion inferred from sampling corners. With a_min=1/5 and epsilon=1/100 the uniform bound is 2/19, strictly less than half the signature gap 8/25. Threshold 17/25 therefore separates the calibrated low and high coordinates. Twenty-four exact corner cases regress that argument.

These uncertainty bounds are illustrative assumptions. No shot count, confidence coverage or measured uncertainty has been supplied. At epsilon=4/145 the conservative bound reaches 8/25 and the checker refuses certification. Failure of this sufficient bound is not a proof that discrimination is impossible.

## Exact limits and counterexamples

1. **Unknown readiness:** with initially dead detectors, every first-trial click rate is zero. Nominal ready-state decoding cannot silently be reused.
2. **Discarded no-clicks:** conditioning on click makes the selected click frequency one for every interval. The complete-trial denominator matters.
3. **Unknown independent per-port efficiencies:** [1,2] with efficiencies (9/25,9/25,81/625) and [2,3] with (81/625,9/25,9/25) give the same vector (81/625,81/625,81/625). Thus uncalibrated counts need not identify the interval. This counterexample allows independent channel efficiencies; it is not a claim about a single unknown common factor.
4. **Phase alias:** multiply the output at slot 1 by -1. Every process matrix changes, but these three probe distributions do not. The family distinguishes the six canonical interval processes, not arbitrary processes with matching intensities. It cannot replace full process validation or certify an inverse implementation.
5. **Zero reference:** division by zero is rejected. Empty and noncontiguous exact response masks are also rejected as outside the declared interval family.

Detection identifies distributions while consuming the detected photon. It does not preserve a quantum system for subsequent inverse replay. Use independent preparations for observation and coherent-control studies.

## Reproduction and next gate

    python research/nima/checkers/check_interval_cavity_probes.py

Receipt: `results/interval-cavity-probes.json`. Exact checks passed: 18 normalized distributions, six full record recoveries, seven subset collisions, calibration identities and 24 uncertainty corners. Source hashes are checked before and after execution. Original sources/results were not rewritten.

The previously missing conditional probe map now exists. The remaining physical gate is a specified source/preparation/routing and reference-calibration package with stable readiness/efficiency, complete trials and finite-sample uncertainties. Inverse/replay control access and causal interpretation remain separate; neither is needed to establish this bounded distribution-level theorem, and neither follows from it.
