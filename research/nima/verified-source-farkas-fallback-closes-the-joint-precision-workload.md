# Verified source Farkas fallback closes the joint precision workload

## Result

All 92 objective requests in the 46-case precision bridge now have independently verified answers:

- 88 native joint finite-dictionary certificates;
- four explicit source-space Farkas fallbacks;
- zero unanswered requests in this workload.

The four primary proposal failures remain recorded. The joint optimizer was not repaired or proved total. The fallback instead uses the already available, independently verified planar emptiness certificate for each of the two inconsistent states.

## Admission gate

`recover_inconsistency(request, specialized, sign)` first verifies the specialized certificate against the expected precision state and threshold query. It proceeds only if the verified result is INCONSISTENT.

Neither a solver exception nor an unverified status tag establishes emptiness. The producer explicitly rejects recovery from a feasible state's certificate and from an empty-tagged certificate whose Farkas weights have been removed.

The fallback currently requires the specialized certificate as input. It is not a new general-purpose Farkas solver and does not promise recovery for arbitrary joint-schema problems.

## Proof transformation

The existing source-space bridge translates the planar ray:

1. Preserve weights on corresponding free-cap and retained evidence rows.
2. Compute the resulting coefficients on pinned atoms.
3. Cancel each such coefficient with a nonnegative multiple of the appropriate exact-pin equality orientation.

The resulting full source-space normal is zero. Pin-bound contributions reproduce the constants subtracted during residualization, so the combined upper bound remains strictly negative.

The fallback has the ordinary general-reference Farkas certificate format. It is not disguised as a joint cut trace. Its full source state and signed audit objective are checked against an independently reconstructed translation of the original expected precision state.

The fallback envelope also retains the primary error type and message. Those fields are diagnostics, not independently certified explanations of library behavior.

## Independent acceptance

The bridge verifier checks native joint proofs as before. For SOURCE_FARKAS_FALLBACK it independently reconstructs the full source-space statement, checks the translated certificate with the existing general arithmetic verifier, and requires EMPTY. It also independently verifies the specialized emptiness certificate.

Both objective signs can share the same mathematical emptiness proof, but each certificate remains bound to its requested objective. All 46 four-valued query comparisons now complete, including the two inconsistent states.

The verifier rejects 17 mutations/replays: the previous eleven controls plus negative and zero fallback rays, omitted pin evidence, a changed fallback objective, a foreign source binding, and replay of an empty-state fallback into a feasible state.

## Reproduction and limits

    uv run --with sympy python research/nima/checkers/check_precision_joint_bridge.py
    python research/nima/checkers/verify_precision_joint_bridge.py

Updated artifacts: `research/nima/results/precision-joint-bridge*`.

Native joint row, cut, dimension and rational-size measurements remain scoped to native packets; they do not measure the source-space fallback representation. Fallbacks retain full source constraints and pin information through their translated states and checked row indices.

This closes the concrete precision workload, not third-party solver totality, general audit elimination, noisy-pin semantics, observation authentication or storage compression. The original mathematical inconsistency answers come from checked proofs, never from operational failure.
