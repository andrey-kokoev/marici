# Two exact local pushforward values for the nine-point four-pair cell

The normalized source eight-form of the minimum-eight-support cell now has TWO independently checked exact LOCAL pushforwards through the SAME nine-point moment-curve `CZ`. This is a differential-form computation, not only a source image-rank test.

Use target chart

    B = (CZ)[:,0:2]^-1 (CZ)[:,2:6]

with the eight entries of `B` ordered row-major. Use source coordinates `(w2,w4,w5,w6,w7,w8,t,u)` and the oriented source form

    - d^8(source) / [w2*w4*w5*w6*w7*w8*u*(t-u)].

For weights ALL one, `t=3,u=2`, the exact target Jacobian and local pushed coefficient are

    det(dB/dsource) = 21039669/5120000,
    pushed coefficient = -2560000/21039669.

For `(w2,w4,w5,w6,w7,w8)=(2,3,1,4,2,5)`, `t=7/2,u=3/2`, they are

    det(dB/dsource) = 3415346249728000/25632972850442049,
    pushed coefficient = -2848108094493561/273227699978240000.

All entries are exact rationals; a separate verifier recomputes the Jacobians via Plücker-ratio derivatives rather than the original inverse-matrix differential and refuses four mutations. At EACH sampled target the four paired conditions intersect its four-parameter source fibre in TWO graph-realizable roots. Exactly one is in the positive paired cell; the other has respectively 12 and 6 negative retained minors. Thus there is no omitted SECOND POSITIVE sheet at either sampled target. This is a local branch census, not a global univalence theorem.

This step opens a concrete next comparison but does NOT identify a physical generalized-R term: no sourced nine-point history-form coefficient has been evaluated on the same external data. A SUBSEQUENT exact rational-interval computation now also evaluates the local pushforward at the earlier algebraic minimum-eight-support target and excludes its second fibre root from the positive paired cell; see `the-nine-point-minimum-eight-target-has-a-certified-local-pushforward.md`. Neither those rational samples nor that one algebraic point prove equality of differential forms or global image coverage.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_paired_pushforward_samples.py
    uv run --with sympy python research/nima/checkers/verify_nine_point_paired_pushforward_samples.py

Artifacts: `research/nima/results/nine-point-paired-pushforward-samples.json` and `nine-point-paired-pushforward-samples-verification.json`.
