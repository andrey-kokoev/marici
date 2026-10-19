# First untransported simple-root candidate — 2026-10-13

## Active net obligation

`untransported-simple-forms` in the weighted-A3 work net, starting with history 3 / root [1,1]. The canonical-form admission gate remains open.

## Construction retained before component extraction

The actual source history has outer pair (2,5), inner pair (3,5), prefix (5,2), inner covector path (8,5,2), lower endpoint (2), and updated upper endpoint (8,2,5).

Construct F_t using that transported upper endpoint and F_0 using external upper endpoint (5), with every other datum unchanged. The receipt retains both generalized-R sparse eta coefficient rows, bosonic prefactors and denominator factors. The full degree-eight superfunction is encoded as

    F = prefactor_outer * prefactor_inner
          * product_{A=1..4}(q_outer^A q_inner^A),

with the algebraic Grassmann factor order outer then inner. It is not merely a retained K0 scalar. The receipt also stores all 70 momentum-conservation-quotiented one-SU(4) numerator coefficients.

Source constructors: `nnmhv_coherence_paths.py`, `dual_r_invariant.py`, `dual_spinor_kinematics.py`, and the external-upper branch in `check_nnmhv_kernel_wall_tail_boundary.py`. No owner producer or missing BCFW artifact was executed/reconstructed.

## Exact endpoint identity

Inspection of generalized_r gives a useful simplification: the boundary-spinor switch does not change the eta coefficient row. It changes only an angle numerator and one denominator sandwich.

Write

    u_t = <8| x_82 tilde(x_25),  u_0 = <5|,
    k(u) = epsilon u^T,
    xi = <8| x_85 tilde(x_52),
    L = xi x_23 tilde(x_35).

Then, on the declared nonsingular localization,

    c = det[k(u_0),lambda_4]/det[k(u_t),lambda_4]
          * (L k(u_t))/(L k(u_0)),
    F_0 = c F_t,
    F_t-F_0 = (1-c) F_t.

For the existing eta2/eta3 selector divided by <23>^4 this gives K0_11=c K_11 and B_11=(1-c)K_11.

All outer and both inner denominator factors must be nonzero. The ratio expression also requires the transported angle numerator nonzero; the normalized component requires <23> nonzero. These are rational-function localizations, not proof of a positive common chart.

## Exact controls

Three rational momentum-conserving fixtures, with the original constructor family shifted by 0,1,2, give respectively

    c = 3195/9943, 4807/14596, 4122/12337.

For each fixture the checker verifies all sparse inner polynomial coefficients scale by c, identical eta coefficient rows, the endpoint ratio formula, the selected-component relations and nonsingularity. Cyclic momentum conservation is checked independently.

The varying nonunit ratios reject the shortcut of taking the transported representative unchanged as the untransported object with the same unit canonical normalization. They do not rule out a different source-authorized cell, chain, pushforward or coefficient-valued form realization.

## What this advances, and what it does not

Completed precursor: an explicit source-defined untransported rational superfunction candidate for one simple root, with full factorized fermionic data, exact component extraction and localization.

Not completed: canonical-cell admission, positive-coordinate chart, dlog orientation, source-normalized differential-form realization, or common-chart transition to the transported form. A kinematic prefactor is not automatically a logarithmic transition Jacobian. The auxiliary operation of omitting the source-mandated update does not by itself produce a term in the sourced BCFW chain.

The next meaningful test is canonical admission of this explicit F0, preserving its nonconstant coefficient c. If admission requires a broader coefficient-valued form class, that is a successor specification, not a silent reuse of the transported cell. We should not extend the candidate to the other two roots as though this gate had passed.

## Reproduction and evidence

    python research/benincasa/checkers/check_untransported_simple_root_candidate.py

Result: `research/benincasa/results/untransported_simple_root_candidate.json`.

Verification level: fresh exact rational fixture algebra plus the written endpoint identity from the existing evaluator. Not a fresh Rzk/Agda kernel proof, symbolic classification of all cells, or positive-atlas replay. Weighted descent remains open.
