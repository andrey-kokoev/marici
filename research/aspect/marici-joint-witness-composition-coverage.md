# Marici joint-witness composition coverage

## Result

The existing Marici capability family is sufficient to represent and govern the optical joint-witness invariant without introducing a new primitive. The composition is:

1. immutable payload for the complete witness packet;
2. exact domain checker for common-run and coherent-frame realizability;
3. lifecycle acceptance criterion requiring that checker;
4. task revision guard against stale lifecycle mutation;
5. evidence admission binding report, verification, and criteria;
6. scoped report retaining the measurement boundary.

The lifecycle surface does not natively understand optical epochs or frame transport. Domain semantics remain in the checker. Representation coverage is established; an end-to-end admitted lifecycle execution was not performed.

## Source and capability frame

The audit uses the frozen optical splice packet and live Site inventory observation `mcp_payload:site-tools-178776574805930@v1`. The observed task-lifecycle contract exposes immutable payloads, acceptance tests, evidence admission, scoped reporting, and expected-revision guards. Delegated tasks expose workflow correlation and source-task references. Artifacts register presentable files.

The inventory also reports contract drift for task lifecycle and delegated task, and the work-lifecycle probe failed because its store is not prepared. Those defects bound the audit; they do not erase the observed narrower capabilities.

## Constructor order

Payload integrity occurs first but grants no semantic authority. The exact optical checker then evaluates the two-sided signature:

- reject cross-run splicing;
- accept same-run source-certified coherent frame transport.

Lifecycle acceptance can require that result, bind it to the current task revision, admit the verification evidence, and emit a scoped claim. The order matters: evidence admission cannot turn an unchecked payload into a physical witness.

## Conserved information and detector

The payload preserves witness bytes. The domain checker preserves run, source, port, epoch, decoder-version, and transport incidence. Lifecycle preserves task-state provenance and acceptance history. The scoped report preserves the claim boundary.

No one layer performs all jobs. Their typed composition does.

## Smallest hostile

Substitute any one of the following for the complete composition:

- an immutable payload hash;
- a current task revision;
- an artifact registration;
- a delegated correlation key;
- an authorized claimant.

Each preserves a real marginal property but fails to establish the physical common-run/coherent-transport witness.

## Classification

The capability family is representationally sufficient. Therefore the optical hostile supplies no evidence for a missing primitive. A reusable native domain validator could reduce repetition, but convenience and semantic centralization are different claims from necessity.

The unperformed next test is an authorized lifecycle task whose acceptance criteria execute the exact checker on both the spliced and transported packets and whose admitted evidence is read back at the resulting revision.

## Completion boundary

This point-in-time audit does not claim native optical semantics, prepared work-lifecycle coverage, or a completed end-to-end execution. Surface contract drift must also be resolved or explicitly tolerated before a production claim.

## Reproduction

Run:

    python research/aspect/checkers/marici_joint_witness_composition_coverage.py
