# Actual source/evidence coupling needs retained records and delivery state

## Result

An explicit finite coupling is now constructed and checked on the actual six-event source, actual assembled rows and the existing hidden source relation.

The typed current observer alone does **not** determine evidence-dependent decision permissions. Two histories have an invisible ideal difference at their current corner but opposite earlier vacuum readings. Once those records have been acquired and delivered, the correct issuances differ.

Adding the source-authorized producer record, locally received record and one-shot issuance state makes the declared transition system descend through the source-relative observer equivalence. An independent replay checks all 638 reachable coupled states and 1,268 transitions.

This closes a small, explicitly declared coupling—not the previously unspecified general coupling of arbitrary source histories to the signed theta-task ledger.

## 1. Actual source collision and actual observation anchor

Start with either zero-mark prefix

    [0,1] or [1,0],

both in corner (0,3). The published base observer row 0 is the canonical vacuum functional

    corner (0,3), word [0,1], marks [0,0], coefficient 1.

Its values on these two prefixes are respectively one and zero. The acquisition below explicitly uses this owning raw-row representative; it is not inferred by extending an abstract quotient observer to all individual paths without an anchor.

Append forgotten event 3. The histories become

    h_one  = [0,1,3],
    h_zero = [1,0,3].

Their difference, up to sign, is the owning hidden ideal relation in corner (0,11). Both record the constant unit, so their difference is in the recorder kernel. Its assembled observer column is zero.

The checker freshly runs the actual opposite-observer action verifier and binds the collision to the matching presentation. It also checks all 79 common continuations using unused events 2,4,5, including every binary retained-mark assignment. Recorder equality and equality of assembled row expressions persist for every such continuation.

The comparison is source-relative: same corner, same recorder value, and zero observer value on the ideal difference. It is not an assertion that O3, whose declared domain is the source ideal, is already an unrestricted physical-history observer.

## 2. The newly declared coupling

The protocol begins at either of the two admitted prefixes above.

1. **Source extension:** at mask 3, append forgotten event 3. Subsequently append any unused event from 2,4,5, with either mark. The independent recorder validates each extension.
2. **Acquisition:** optionally, while still at corner (0,3), evaluate actual row 0 and construct a record binding the task, row, corner, generating prefix, marks and exact value.
3. **Delivery:** explicitly deliver that same source-authorized pending record to the recipient. Acquisition does not imply delivery.
4. **Issuance:** after event 3 has occurred, issue ONE or ZERO once, only after validating the matching local record.

The task concerns the earlier vacuum value, not the current terminal value. Source extension does not automatically acquire, deliver or certify anything.

The finite execution semantics is the admission authority: acquisition creates a record from the actual prefix, and delivery transports only that created record. Hashes bind the fields but do not authenticate a physical producer. The stipulated reliable delivery and exact ideal acquisition are model assumptions, not implementations of sensing or secure communication.

## 3. Two explicit failures of current-observer sufficiency

### Lost historical value

In one execution acquire and deliver the value one from [0,1], then append 3. In another acquire and deliver zero from [1,0], then append 3.

At corner (0,11), the current histories have zero observed ideal difference. Nevertheless the allowed issuances are different:

    first history:  issue ONE,
    second history: issue ZERO.

Both are admitted histories in this finite protocol. This is not the empty-fiber incompatibility of the earlier middle-threshold task.

### Missing local availability

Use the same history [0,1,3] and the same acquired producer record. If delivery occurred, ONE may be issued. If delivery has not occurred, issuance is forbidden.

Here even the source history is identical. The difference is the recipient's evidence state. A source clock tick or observer equality cannot replace the delivery event.

These are counterexamples to the sufficiency of the current source-relative observer for this declared evidence-dependent protocol, not counterexamples to its already-verified algebraic source-action descent.

## 4. Sufficient enriched operational state

Retain

    typed source-relative observer class
    + producer's acquired record
    + recipient's delivered record
    + issued-decision flag.

The producer buffer is part of the coupled operational state; it is not presumed remotely known by the recipient. The recipient's issuance guard uses its own received record and issuance state. The global buffer is needed to describe which deliveries can occur.

The finite graph has 160 source histories, 638 reachable coupled states and 461 enriched equivalence classes. Every pair of states in an enumerated enriched class has the same admitted event labels and equivalent successors. All reachable issued values equal the actual earlier vacuum reading.

The structural descent argument is also explicit:

- source-extension admission depends on the typed endpoint;
- equality after source extension follows from the verified observer action on ideal differences;
- acquisition is allowed only at the designated cut and reads actual observer row 0, hence equal observer values there give equal acquired values;
- delivery and issuance depend only on retained records and the declared flags.

The finite enumeration uses sufficient exact formal coefficient equalities, not an assertion that distinct coefficient expressions are analytically independent. The structural argument does not rely on ruling out additional equalities at the actual calibration.

The fields have separate necessity controls in this protocol: the producer buffer controls delivery, the received record controls issuance, its value controls which answer is sound, and the flag controls one-shot issuance. This is not a theorem of information-theoretic minimality over every representation or policy.

## 5. Rejection controls and provenance boundaries

Changed task binding, changed row binding, a relocated observation corner and an incorrect acquired value are rejected. Delivery without a producer record and issuance without a received record are absent from the reachable transition graph.

A syntactically valid record from the other possible history is not thereby a record produced in this execution. The authoritative acquisition/delivery semantics enforces that lineage. No claim is made that a bare hash lets a receiver discover forged physical provenance without trusted acquisition or authenticated delivery.

This protocol has no analytical calibration refinement, quantitative deadline, history reversal or common-commit requirement. Adding the signed task ledger would require an additional constructor relating its three-channel observations and calibration dependencies to actual source transitions. That broader gate remains separate.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_source_evidence_coupling.py
    python research/nima/checkers/verify_source_evidence_coupling.py

The first command freshly checks the owning actual source actions and exports the complete finite coupled-state graph. The independent verifier reconstructs the row evaluations, recorder values, all transition guards, graph reachability, and enriched transition congruence. Both pass.

Artifacts:

- `research/nima/results/source-evidence-coupling-contract.json`
- `research/nima/results/actual-source-evidence-coupling.json`
- `research/nima/results/source-evidence-coupling-verification.json`

The productive advance is an explicit source/acquisition/delivery/issuance constructor with a tested boundary: the source observer forgets information that a history-dependent task needs, while a declared evidence enrichment preserves exactly the permissions used by this finite protocol.
