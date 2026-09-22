# One extra retained raw row suffices for the six-state vacuum increment

## Result

Retaining the combined matched scalar AND unscaled manifest row 76 is sufficient to reproduce the background-two vacuum-acquisition kernel obtained by retaining all 449 raw readings:

    dim D=6, inherited filtration dimensions (6,5,1,0).

One additional raw reading is minimal for this specified comparison: with no extra reading, the increment has seven states. This is not a claim that row 76 reconstructs the full raw observer or all 449 inputs, nor that it is the best-conditioned choice.

A portable retention policy and standalone standard-library verifier now certify this finite structural assertion against the actual receiver manifest.

## 1. Fix the retention product

Keep all previously declared detector families fixed. For the matched receiver, retain:

1. its combined scalar, together with the existing error fields;
2. the original UNWEIGHTED, UNSCALED joint-filter input at zero-based index 76;
3. the receiver-manifest digest and selected analytical shape;
4. the input's total joint l1 error budget as a valid conservative error bound for this component.

Row 76 is copied before applying its sign or final crossed gain. It is not divided by a response amplitude or by the gain of the combined scalar.

The policy is `results/minimal-matched-retention-policy.json`. It binds the actual `../grothendieck/results/finite-cubic-observer.json` by SHA-256 and also records the row's semantic shape. A changed manifest requires rebinding and re-verification; an index alone is not a stable identifier.

No production receiver behavior or archival policy was changed by this work. This is an explicit proposed data product with a verified structural guarantee.

## 2. The exact comparison being certified

Let Omega_s retain the signed scalar, Omega_m retain that scalar plus row 76, and Omega_r retain all raw inputs. Then

    Omega_s subset Omega_m subset Omega_r.

Let W_v=Omega_v intersect Sat(chi_2). The vacuum module Sat(chi_2)^* has fifteen interval coordinates. Previous source audits give

    dim W_s=8, dim W_r=9.

The new row supplies exactly the additional interval functional at corner 12->60060. Hence

    W_m=W_r,

and the three corresponding restriction kernels satisfy

    D_r -> D_m -> D_s,
    D_m=D_r

under their canonical faithful representations inside the full vacuum module.

The equality is as source bimodules, not merely as dimensions. Their inherited filtrations also agree: the five second-level and one third-level states have explicit old-invisible I^2 and I^3 source lifts, while the remaining length-three state cannot be lifted from I^2.

The background-two acquisition remains nonsplit by the already established forced-initial-lift obstruction. Agreement of the increment modules does not assert equality of the complete acquisition extension diagrams, whose old observer modules differ.

## 3. Why one row suffices, and zero does not

The selected row has seams

    2->4 retained, 60->420 forgotten, 420->4620 forgotten,

with one retained feature in the buffer after the first seam. Prepending the retained path (2,3) to a forgotten input in the corner 12->60060 makes this row equal to

    coefficient(5,7,11,13)

times a fixed nonzero common-filter response on [2,4] and [4,12]. This supplies the missing vacuum interval functional.

For minimality use the actual source

    h=(5,7,11,13)+(5,7,13,11)-2(5,11,7,13).

Its coefficients sum to zero, so it lies in the forgotten terminal-record ideal. Every old scalar contextual detector kills h, including the signed matched sum, but the selected raw contextual reading has normalized coefficient one.

The six remaining interval states have explicit sources invisible even to ALL independently retained raw rows. Thus adding this one reading achieves the maximal relevant gain available from all 449 readings for this vacuum-increment comparison.

The row need not be unique. The result minimizes the number of additional retained raw readings while preserving the existing combined output; it does not optimize precision, storage encoding or receiver cost over arbitrary alternative products.

## 4. Structural sufficiency does not manufacture precision

If the admitted input budget is

    sum_j |error_j| <= eta,

then |error_76|<=eta. The existing combined-output error remains bounded by its own maximal-gain factor times eta, with its separately reported arithmetic errors.

The two retained outputs come from the SAME input vector. Their errors need not be independent. Keeping both does not create two independent measurements or justify reducing either bound.

The policy never divides eta by the final gain to claim a sharper raw reading. Structural nonvanishing of the row's physical response is not a quantitative reconstruction/noise guarantee. Acquisition and calibration assumptions remain external.

## 5. Independent portable verification

`certificates/verify_minimal_matched_retention.py` imports no producer, discovery checker, source recorder or numerical integration package. It implements its own ordered-cut evaluation on exact marked paths using the Python standard library.

It checks:

- the manifest digest, row index and semantic shape;
- the 449 typed two-feature input shapes, signs and nonzero gain labels;
- the seven original shared private-coordinate intervals;
- the eighth shared interval from the signed matched test;
- the selected row's exact coefficient identity on every four-event forgotten path order;
- the scalar-invisible but raw-visible minimality witness;
- all contributing source contexts of the six remaining invisible source directions;
- explicit I^2 lifts for the five second-level states and the cubic vacuum witness.

The nonzero physical response factors and the interpretation of actual measurements are stated as external hypotheses, rather than inferred from rational coefficients.

The tests reject eight invalid policies, including an overclaim of complete raw-observer reconstruction and an invalid gain-divided error rule. A changed manifest is rejected until rebound. Isolated execution succeeds outside the repository with only the verifier, manifest and policy files.

## Reproduction

Generate the policy and run adversarial/portability tests:

    python research/voevodsky/checkers/check_minimal_matched_retention.py

Verify independently:

    python research/voevodsky/certificates/verify_minimal_matched_retention.py research/grothendieck/results/finite-cubic-observer.json research/voevodsky/results/minimal-matched-retention-policy.json

All pass. Test report: `results/minimal-matched-retention-tests.json`.
