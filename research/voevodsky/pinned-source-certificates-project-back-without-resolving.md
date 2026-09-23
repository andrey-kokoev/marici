# Pinned source certificates project back without re-solving

## Supported domain

The reverse bridge accepts exact general-reference primal/dual or Farkas packets for states that are exactly the canonical translation of a supplied two-free precision state. The caller supplies the expected original state and threshold query independently. The general objective must be the signed first-free-atom objective. All source rows, pin equalities and evidence order must match the expected translation.

This is not a translator for arbitrary full-schema states, native joint cut-trace packets or arbitrary proof syntaxes. It uses the source-space format already handled by the independent reference checker.

## Proof transformation

First validate the entire input certificate. Substitute the exact pins into each weighted row:

- free-coordinate caps become the corresponding planar cap rows;
- retained evidence becomes its original residual row;
- pin equalities become 0<=0;
- pinned-coordinate caps become 0<=slack, with nonnegative slack.

Retain the free-cap/evidence multipliers, aggregating matching indices. Discard the constant rows. Their normal contribution is zero and their weighted bound contribution is nonnegative. The residual normal is therefore unchanged while its bound can only decrease.

For a Farkas ray, a negative old bound stays negative, giving a planar contradiction. For an optimality proof, the projected feasible witness attains the original bound. A strictly smaller residual upper bound would contradict this feasible witness. Hence the discarded weighted slack is necessarily zero, and the projected proof retains the exact optimum. The implementation explicitly checks this identity.

Project the primal vector to its two free coordinates. Combine the two signed objective proofs into the specialized threshold certificate, respecting equality at the threshold and independently bound original history. This is algebraic proof transport, with no optimization call.

## Exact replay

The existing 46-case source-schema bridge supplies two input routes:

1. all forward-translated general certificates;
2. independently proposed simplex certificates where verified, using the existing transported proof only for the recorded failed proposal.

Both routes reconstruct 46 specialized answer packets: 92 packets total. Independent replay checks the expected source/state/query, both input proofs, both output extrema or contradiction, and the four-valued answer. All pass. Four output mutations altering source binding, threshold, dual or witness are rejected.

The second route is important: reversal is not limited to syntactically undoing the forward translator's chosen multipliers. It accepts the same supported statement with another valid general-reference proof. Empty branches use one projected Farkas proof for the combined query after validating both signed requests; proof multiplicity is not preserved.

## Cost statement

Reverse transport performs one pass over supplied nonzero multipliers plus input validation, source-row reconstruction and primal projection. It introduces no new nonzero multipliers. This is an arithmetic-structure observation, not a polynomial bit-complexity benchmark; independent checking and statement reconstruction have their own costs.

Across both tested routes, serialized input pairs occupy 140244 bytes and returned specialized packets occupy 81308 bytes. The comparison includes full statements: an input pair repeats its general state twice, while the output combines the two objectives into one threshold packet. It is not a pure dual-compression ratio or evidence-storage saving. Pin values and retained history remain necessary in the specialized state. Upstream admission is not freshly replayed here.

Together with Nima's forward bridge, this establishes bidirectional answer/proof transport on the translated pinned subfamily without re-solving. It does not make the packet transformations mutual inverses on syntax, guarantee identical selected witnesses, or establish equal runtime/verification budgets across representations.

## Reproduction

    python research/voevodsky/checkers/check_reverse_precision_bridge.py
    python research/voevodsky/checkers/verify_reverse_precision_bridge.py

Neither command invokes an optimizer. The verifier imports the existing independent arithmetic verifiers, not the reverse translator.

Artifacts:

- `results/reverse-precision-bridge.json`
- `results/reverse-precision-bridge-verification.json`
