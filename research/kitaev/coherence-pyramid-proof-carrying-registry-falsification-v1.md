# Falsification attempt on the proof-carrying partial registry

## Question

Does requiring a stored certificate and passing checker for every non-unknown status make the partial transfer registry evidentially sound and reproducible?

## Claim boundary

This packet distinguishes mechanical replay from evidential grounding. It does not claim that the present registry has admitted a circular certificate.

## Bold conjecture under test

A fixed registry version may safely record `pass` or `fail` whenever a stored certificate is accepted by its checker; all remaining cases are `unknown` or inconclusive.

## Circular-certificate hostile

Let certificate `C_P` establish predicate `P` conditional on `Q`, and certificate `C_Q` establish `Q` conditional on `P`. A checker that validates schemas, references, and each conditional inference accepts both. Replaying the check is deterministic. Yet the pair supplies no derivation of either `P` or `Q` from source evidence.

In logical form the admitted edges are

\[
Q\longrightarrow P,
\qquad
P\longrightarrow Q.
\]

Their cycle proves only equivalence, not either endpoint. A predicate dependency DAG does not prevent this because certificate-evidence dependencies are a distinct graph. Thus `certificate present + checker passes` is insufficient unless the evidence graph is well-founded or each cycle contains an independently grounded invariant strong enough to discharge it.

## Environment hostile

A checker result is not reproducible from source text alone. It also depends on executable digest, interpreter and dependency versions, input digests, numeric modes, and acceptance thresholds. A stored certificate pointing only to a command can pass under one environment and fail under another while retaining the same registry record.

## Unsound-checker hostile

A deterministic checker can implement the wrong theorem, omit a branch, or import the target claim as an assumption. Replayability certifies execution, not semantic soundness. Proof-carrying status therefore needs a declared trusted base and hostile tests that fail for known counterfixtures.

## Strongest residual

The conjecture is falsified if `safely` means evidentially grounded. Proof carrying plus replay is necessary but not sufficient. Circular support is the smallest exact obstruction.

## Surviving conjecture

A non-unknown status is admissible only when:

1. its certificate dependency graph reaches source evidence without an ungrounded cycle;
2. the checker, executable, dependencies, inputs, and acceptance schema are digest-frozen;
3. the trusted base and imported assumptions are explicit;
4. deliberate-failure fixtures exhibit the predicted nonzero residual;
5. the checker proves exactly the registered predicate at the declared strength.

Mechanical replay and scientific admission remain separate statuses.

## Disposition

Revise. Add `evidence_dependencies`, `grounding_roots`, `trusted_base`, `execution_manifest`, `negative_controls`, and `semantic_review_status` to each certified predicate record. Reject ungrounded strongly connected components in the evidence graph. A passing checker may establish `mechanically_replayed`; only grounded review may establish `admitted_at_strength`.
