# A versioned source-task ledger prevents stale-proof downgrade

## Result

A receiver now has an exact local ledger for the existing calibration lineage

    projection272 -> theta-Taylor -> signed-pairing.

For the unchanged frozen `private/middle_threshold` task, the first two versions are `UNRESOLVED`; the signed-pairing version is `CERTIFIED_INFEASIBLE`. Every ledger envelope binds the canonical task input, calibration hash, parent calibration hash, portable-chain hash, terminal problem hash, status and exact necessary cost.

The receiver does not trust rank labels or an asserted status. Admission is closed over a fixed declared lineage: it verifies the envelope digest, task binding, calibration identity, source-task replay, and portable chain before applying a transition.

## Safe ordering behavior

- An in-order projection, theta, signed sequence reaches `CERTIFIED_INFEASIBLE`.
- A late theta certificate after signed pairing is `STALE_IGNORED`; it cannot replace the resolved state with `UNRESOLVED`.
- A duplicate signed envelope is ignored.
- A receiver may catch up directly to signed pairing because the admitted signed portable chain itself contains and verifies all skipped identity-refinement edges.
- A malformed task binding, status, rank, or parent relation causes `ABSTAIN`, not an inferred conclusion.

The direct catch-up rule is important: serial delivery of every historical certificate is not a causal requirement when the terminal artifact carries a verified ancestry. Conversely, an unproved claimed jump is not made safe merely by attaching a larger version number.

## Scope

This is a finite local artifact ledger, not a cryptographic protocol. SHA-256 bindings detect accidental or adversarial byte changes only conditional on trustworthy acquisition of the referenced artifacts; there are no signatures, keys, authenticated channels, equivocation consensus rule, or recovery protocol.

The order is also intentionally task-specific. It covers this declared calibration ancestry and frozen source task, rather than asserting that arbitrary numerical refinements form a global total order or preserve every type of decision.

## Verification

    uv run --with python-flint python research/voevodsky/checkers/check_versioned_signed_certificate_ledger.py

Artifact:

- `research/voevodsky/results/versioned-signed-certificate-ledger.json`

The checker replays all three source-task versions, verifies their portable chains, validates parent/edge identities, exercises in-order and delayed replay, permits only the terminal chain's embedded verified catch-up lineage, and rejects forged task, status, rank and parent fields.
