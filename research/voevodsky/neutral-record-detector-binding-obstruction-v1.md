# Neutral record is not the empty-bin detector memory

Target: physical source-map preparation, not physical admission.
Checker: `research/voevodsky/checkers/check_neutral_record_detector_binding.py`.
Receipt: `research/voevodsky/results/neutral-record-detector-binding-obstruction-v1.json`.

## Frozen candidate and independently specified routes

Reuse the completed conditional reaggregation model: common normalized scalar pair, neutral record initially |0>, record gap 1, coupling 1/2 and model-time unit 1. In that matter sector the primary record Hamiltonian after common reference subtraction is [[0,-1/2],[-1/2,1]], apart from a scalar matter energy. Its coherent occupation law is

    p(t)=(1-cos(sqrt(2)t))/4.

Compare to the central detector's classical empty-bin memory update: ready stays ready; dead recovers to ready with probability gamma in [0,1]. Both no-click records are retained, no photon supplied, and one model-time interval corresponds to one empty bin. Freeze gamma across bins. This is a candidate map, not an independently calibrated physical time identification.

The candidate identifies the two neutral basis states with the two classical readiness labels, preserving their occupation queries. We test BOTH bijective assignments. No intermediate projective measurement of the neutral record is inserted in the two-step evolution: inserting it changes the declared coherent source operation.

## Both assignments fail

If |0> maps to ready, the detector remains ready under every empty bin, while the primary record has positive occupation of |1> after one interval. The one-step observation square fails.

If |0> maps to dead and |1> to ready, matching the first interval forces gamma=p(1). The classical two-step ready probability is

    q(2)=2 gamma-gamma² <= 2 gamma.

But coherent evolution gives, writing c=cos(sqrt(2)),

    p(1)=(1-c)/4,
    p(2)=(1-c²)/2,
    p(2)-2p(1)=c(1-c)/2 > 0.

An exact alternating-series enclosure certifies 3/20<c<4/25. Hence p(2)-2p(1)>3/50. In particular p(2)-q(2)>3/50 when the one-step laws match. This is not a fit residual or uncertainty claim: it is a structural obstruction at declared model parameters.

Even allowing discrepancies bounded by epsilon at both intervals, q(2)<=2q(1) implies p(2)-2p(1)<=3 epsilon. Thus epsilon=1/100 cannot repair this candidate. This tolerance comparison uses the central charter's numerical scale only as a mathematical benchmark, not as an admitted experimental test.

## Disposition and scope

Rejected: identifying the primary coherent neutral record with classical two-state detector readiness under the unchanged empty-bin operation, either label assignment and fixed recovery law. The rival, dark on the prepared scalar state, does not rescue a common map for BOTH rules by matching a trivial stable state alone.

Not rejected: a driven quantum-memory apparatus, different operation/time maps, nonclassical readiness instruments or a larger retained memory. Those are different source candidates requiring explicit preparation, control, observation and physical-system evidence. This counterexample does not assert that the completed detector CP family is exhausted by classical readiness laws; the comparison intentionally tests its classical empty-bin restriction.

Next useful source proposal must identify an actual coherent two-level record analogue and its generator/control map, or explicitly supply a changed measurement/reset protocol. Calling both systems 'two-level memory' is insufficient. No physical data, calibration, particle identity or annihilation is supplied; the physical-admission gate stays open.
