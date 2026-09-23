# State-relative query certificates require an independent expected history

## Result

The owning symbolic tail interface now exposes state-relative membership and state-bound optimization certificates. Independent replay verifies 200 certificates through m=1024, rejects ten binding/proof attacks, and rejects eight malformed expected contexts.

The gate is not another geometry fixture: the caller must supply the expected immutable state and query independently of the returned certificate. A mathematically valid answer for a forgotten history is not an answer for the current state.

## State and statement binding

`RetainedInterface` retains m, the entire ordered tuple of rational observable frames, and a source-binding string. Construction copies and normalizes nested caller containers. Refinement returns a new snapshot and propagates its source binding.

`descriptor()` exposes a canonical description containing the source rule, binding, m and every retained frame. Rational numbers have canonical exact encodings. Booleans, floating-point inputs and extra observable coordinates are rejected at the query boundary.

The certificate envelope binds that descriptor and the exact request. Its digests cover the state and the state/request pair. The independent verifier also compares their complete contents with the expected statement; it does not merely trust a packet-provided digest.

Binding is to the syntactic snapshot, not to an equivalence class of histories. Reordered or redundant histories may describe the same possibility set while having different bindings. This conservative interface does not silently certify semantic history equivalence.

The source-binding string is caller-supplied context, not authentication. The tests use the owning source-report hash plus a control-run label. The default names the mathematical source rule; it does not identify a real observation session.

## Membership

`RetainedInterface.member(point)` has three proof branches:

1. **Retained-frame exclusion:** an indexed expected frame is violated by the requested point.
2. **Source exclusion:** all retained frames pass, but an independently checked source support separates the point.
3. **Membership:** all retained frames pass and an independently checked greedy lift realizes the point inside the source box.

A negative point answer is not a certificate that the entire state is empty. A positive lift is not identification of the unknown actual source.

## Optimization

`certify_maximum(objective)` wraps the existing exact optimization or Farkas certificate in the same state/request envelope. Independent verification passes the externally expected frames to the existing arithmetic checker.

The older `maximize` method remains available with its existing raw-result format. It does not acquire envelope binding merely because the new method exists.

## Correct caller pattern

With the checker directory on the import path:

```python
from check_symbolic_tail_interface import RetainedInterface
from verify_state_bound_tail_query import verify_certificate

state = RetainedInterface(3, source_binding="caller-owned-context")
state = state.refine((1, 0), 50)
expected_state = state.descriptor()  # retained independently of the response
expected_query = {"kind": "point-membership", "point": ["75", "75"]}

packet = state.member((75, 75))
checked = verify_certificate(expected_state, expected_query, packet)
assert checked["verified"] and not checked["admitted"]
```

Do not replace `expected_state` with `packet["state"]`. That would discard the expected-history trust boundary. Likewise, the requested point or objective must come from the caller, not from the response.

`verified=True` means the answer's proof checked; it does not mean membership is positive. The membership result explicitly returns `admitted` separately.

The verifier rejects unrecognized expected-state fields and frame fields instead of silently dropping hidden restrictions or audit declarations. This two-observable interface remains separate from the conditional atom-audit section prototype.

## Controls and cost

The workload has five history prefixes, eight membership points and two objectives for each of m=2,3,16,1024: 160 membership certificates and 40 optimization certificates. It includes an inconsistent final history.

The ten rejected attacks cover stale history, wrong source size, foreign source binding, changed query, resealed query with a reused lift, resealed omitted history, false frame exclusion, corrupted source separation, corrupted lift, and omitted optimization frames. Recomputing hashes does not repair the independent statement or arithmetic mismatch.

Separate producer controls check six invalid inputs and mutation of caller-owned nested frame containers. The independent verifier additionally checks eight malformed expected contexts, including undeclared audits.

The envelope carries the full history. It is not a constant-size proof or a compressed substitute for evidence. Hashes neither authenticate observations nor establish that the caller's expected state really contains its entire earlier history. That remains an external initialization and retention obligation.

No witness interchange, audit-preserving transport, physical action or publication authority follows from these certificates.

## Reproduction

    python research/nima/checkers/check_state_bound_tail_query.py
    python research/nima/checkers/verify_state_bound_tail_query.py

Artifacts are under `research/nima/results/state-bound-tail-query*`.

A fresh original-interface producer run and independent replay also pass: 118 support queries, 310 base membership queries, 48 persistent queries, 16 reset controls and four rejected corruptions. The coherence and audited-section checks were regenerated and independently verified against the updated engine binding. These are interface/geometry checks, not a fresh upstream all-m analytical-admission proof.

The research verifier requires Python assertions enabled and refuses optimized execution. It is not a hardened network service.
