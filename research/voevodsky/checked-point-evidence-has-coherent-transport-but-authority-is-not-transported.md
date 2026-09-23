# Checked point evidence has coherent transport, but authority is not transported

## From comparison cells to their action on evidence

Nima's point transport service now passes a composition-and-loop workload. The owning fine histories are A and B; the fixed continuations are F: h<=1/2 and G: h>=1/4. Three presentations describe the same terminal fine relation:

    P: [F,G] in one batch,
    Q: [F] followed by [G],
    R: [G] followed by [F].

The paths have distinct proof tips but equal canonical terminal rows. For one checked point result r, compare

    T_(P->R)(r)
        with
    T_(Q->R)(T_(P->Q)(r)).

Two independently bootstrapped live sessions under the same event-bound archive root realize the two routes. Their destination descriptors and checked answers agree exactly. Handles and work counters differ, as they should: equality of evidence transport is not equality of operational histories.

## Closed boundary and identity action

The staged session then travels R->P, closing P->Q->R->P. Its final descriptor and cached result equal those of its original P checkpoint. A further P->P transport leaves that same semantic descriptor and answer unchanged, while issuing a new handle and freshly checking authority/path obligations.

Thus the tested semantic action obeys composition and identity/loop laws. The loop does not restore a stale handle, erase authorization events or assert that the same physical execution occurred.

## Both positive and negative evidence

The workload uses both original histories at the public endpoint (1,1) and the first public vertex. These give four bootstrap cases, including admitted witnesses and empty-fiber results. Each route preserves its original history root, even where a single point's answer could coincide with another history.

Each case has two fresh bootstrap point checks and six successful transports. Across the workload:

- eight bootstrap point checks;
- twenty-four transported results;
- zero point arithmetic during those transports;
- forty-eight fresh transport path checks;
- twenty-four fresh successful transport authority checks.

A trap replaces the point-verification function during all successful transports. It would fail the workload if the service silently replayed the cached arithmetic. Bootstrap checks, independent replays and refused attempts are additional work.

## Revocation breaks execution, not mathematical coherence

After a direct route has arrived, the staged session begins another P->Q->R route. The owner revokes the archive reference after P->Q. Q->R is refused and the entire checkpoint receipt remains unchanged. The already-arrived direct session also cannot use the revoked reference for a further transport.

Nevertheless the mathematical Q/R comparison still verifies: the fine relations did not change when the authority record was revoked. The eight refusal controls across four cases therefore distinguish

    a valid semantic comparison

from

    an authorized executable transport right now.

Retained evidence remains evidence after revocation; revocation does not falsify arithmetic already checked. It removes the authority to perform the next protected operation. Every transition must reacquire its own authority. The vault lock in Nima's implementation spans authorization through publication; this workload uses deterministic revocation between edges, not a concurrency stress test.

## Structural interpretation

Certified presentations form the base diagram. Checked results are retained above those presentations. Verified comparisons act on those results, preserving the point, complete terminal relation, policy and verifier epoch. The actual-history root is fixed but separately reauthorized.

This is a concrete coherent action on checked POINT evidence. It is a candidate fragment of a fibered account of proof-carrying interfaces, not a proof that all evidence types form a fibration or that every semantic equivalence has a canonical operational lift. The service's transport is restricted to canonical row equality and one fixed point/policy.

In particular, this action does not yet transport a domain-wide section, its cell geometry or coverage proof. Those need a separate dependency and coherence theorem. Neither the checked loop nor the existing presentation cone identifies an analytic residue jet.

## Independent replay

`verify_evidence_transport_coherence.py` imports no transport-session implementation. It reconstructs the fine archive from the declared family, verifies all presentation paths, directly checks original atom coordinates and exact public moments, and replays 32 checkpoint answers. It confirms the direct/staged and closed-loop semantic identities.

This offline replay is conditional on the exported authorized root; a JSON event label cannot authenticate the live vault. Authority and cache-reuse behavior are tested separately by the live workload. The distinction is intentionally not compressed into one claimed proof.

## Reproduction

    python research/voevodsky/checkers/check_evidence_transport_coherence.py
    python research/voevodsky/checkers/verify_evidence_transport_coherence.py

Artifacts:

- `results/evidence-transport-coherence.json`
- `results/evidence-transport-coherence-verification.json`

The tests use the existing Nima transport service unchanged. Complete paths, canonical rows, archive records and result logs remain retained costs; no bounded total memory or wall-clock improvement is claimed.
