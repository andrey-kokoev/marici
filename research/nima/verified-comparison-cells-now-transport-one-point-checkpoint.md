# Verified comparison cells now transport one point checkpoint

## Delivered transport gate

A process-local service now transports one checked point-admission result between direct, staged and permuted fine-continuation presentations.

Four bootstrap checks cover both original histories at two distinguishing public points. Eight transports reuse the checked point result while performing sixteen fresh path checks and eight fresh authority checks. Forty-two invalid calls are refused without changing the checkpoint or counters. Fresh arithmetic replay and the owning continuation-coherence regression pass.

This is point-result transport, not whole-section transport or a higher-coherence construction.

## Bootstrap establishes the reusable result

The owner supplies an event-bound archive reference, expected continuation batches, candidate path and requested point. Bootstrap:

1. Obtains the archive through the trusted vault for that event/context and request.
2. Checks the immutable archive root and every expected path edge.
3. Checks point admission against the complete terminal fine relation.
4. For a positive answer, checks original atom caps, exact public moments, t1=51 and every terminal fine row.
5. Retains an immutable point result and issues an opaque live handle.

The mathematical reuse key includes the complete terminal semantic presentation, point, fixed exact-point-only policy and verification source-file epoch. The semantic presentation includes the public polygon, source chart and canonical fine rows. Root authority is checked separately and is never inferred from key equality.

## Transport checks both paths, not just their advertised tips

A transfer requires the current handle, independently expected predecessor descriptor, destination batches and destination path. It reauthorizes the archive reference against the same event/context and requires the resulting archive root to equal the retained root.

The comparison checker replays BOTH paths against their expected operation batches. Their terminal canonical row systems must agree, including the public polygon and source chart. Only then may the cached point result be rebound to the destination path tip.

No candidate replacement answer is accepted. The answer comes from the session's own previously verified encoding. Its destination receipt carries the new path binding and a fresh head. Stale handles and authorization records are not transported.

The vault lock spans authorization through publication. A revoked reference therefore cannot exploit a mathematically valid comparison to gain authority. Semantic equality and authority remain separate gates.

## Direct, staged and permuted controls

For each authorized history, use

    F: h<=1/2,
    G: h>=1/4.

Bootstrap on the direct [F,G] batch, transfer to [F] then [G], and transfer again to [G] then [F]. The proof tips differ while the canonical terminal relations agree.

At (1,1), only B admits the point. At the first public vertex, only A admits it. Both positive witnesses and negative admission results survive transport without collapsing the actual-history distinction.

The workload replaces the point-verification function with a trap during successful transfers. The transfers still succeed, demonstrating that the point arithmetic is genuinely reused. Afterwards, full path and point replay checks every transported result.

## Fail-closed boundaries

Controls reject missing refined rows, omission of an earlier operation, broken parent bindings, changed source-chart claims, an archive for the opposite history under the same event/context, self-asserted authority, a changed point, a changed policy, a changed verifier epoch, stale heads and revoked authority.

Changed points require fresh point verification. Source or policy changes are outside this transport rule and require fresh admission rather than a cache hit. The fixed policy grants neither general fine updates nor archival re-exposure.

A failed transfer leaves the whole receipt unchanged. Returned answer encodings cannot mutate the trusted cached result.

## Meaning of the comparison

The service changes the certified presentation to which a result is attached. It does not claim that two physical executions occurred, rewrite an observed authorization history, or identify distinct proof traces. The retained archive root stays fixed, while the path tip and request binding change.

Canonical row identity remains a sufficient semantic equality test, not a general polyhedral-equivalence procedure. A comparison cannot cross an actual-history authority boundary merely because a particular point has the same answer.

This is one checked consequence of the owning two-refinement comparison cell. It is not a minimal retained-defect theorem, a residue-jet identification, whole-domain section transport or a construction of higher proof-path homotopies.

## Separate work and retention accounts

Successful workload totals:

- four fresh bootstrap point checks;
- eight transported point results with zero fresh point arithmetic;
- sixteen fresh transport path checks;
- eight fresh transport authority checks.

Source/archive reconstruction, canonicalization, dependency hashing and proof-path replay remain fresh work. The service retains complete paths and terminal rows; it does not claim bounded path storage or an overall runtime improvement.

Receipts report the current checkpoint encoding, and the workload reports the vault encoding separately. These are serialized lengths, not a complete heap ledger. Rejected attempts, reference replays, source code and exported logs remain additional costs.

The separate replay script imports no transport session. It verifies path comparisons and point arithmetic, conditional on the exported fixture's authorized root. It cannot authenticate a vault label from JSON; live authority and cache-reuse behavior are tested in process.

## Reproduction

    python research/nima/checkers/check_comparison_checkpoint_transport.py
    python research/nima/checkers/verify_comparison_checkpoint_transport.py

Implementation: `research/nima/checkers/comparison_checkpoint_transport.py`.

Artifacts: `research/nima/results/comparison-checkpoint-transport*.json`.

Owning comparison: `research/voevodsky/retained-defect-transport-makes-two-refinement-retirement-coherent.md`.
