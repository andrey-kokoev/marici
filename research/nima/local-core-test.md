# Standalone local-core existence test

## Claim and logical scope

`A = exists f L(f)`: a source-derived, factor-local continuous lift of the native Bool square exists, without a whole-Tick return interpretation obligation.

This is independent of the parent assumption, unlike the conditional schema `P -> A`. Here `P = exists f (L(f) and R(f))`, with the same candidate class and the same L. The parent's prose now states its return obligation explicitly; that obligation was already in its proof protocol.

## Outcome routing

- A proof of A supplies a particular witness f and a certificate L(f). The next test is R(f). A proof of that very R(f) closes P.
- A rejection of A refutes P by projection: any full lift would provide a forbidden local lift.
- Failed proof/rejection attempts imply neither truth nor falsity of P.
- Failure of R(f) for a single witness does not refute P, because another local lift might extend.
- A proof of P proves A; rejection of P does not refute A.

`TickLiftOutcomeSplit.agda` checks the projection, contrapositive and same-witness extension rules parametrically. These are inference rules, not a construction or exclusion of a local lift.

## Historical readiness audit

The reduction genuinely removes the return obligation. It does not remove the unresolved meaning of source derivation. The previous source-contract audit found only reconstruction/coherence criteria, which admit arbitrary schedule semantics. The relative profile contract fixes a particular interpretation by rule; that is not automatically a witness for this same L.

Before a scientific test is admitted, fix:

1. Candidate carrier and permitted analytic premises, shared with P.
2. The actual source-derivation predicate.
3. Continuous preservation of the factor algebras, not just the already-proved algebraic slice laws.

For a proof, produce a named f and check these requirements only; do not burden it with R(f). For a rejection, exclude every candidate in that exact class. Existing local matrices and relative-component proofs are useful supporting material, not sufficient evidence for A.

## Meaning resolved and test performed

The agreed meaning is uniform construction within explicitly declared analytic mathematics, **not unique selection by the source**. It applies to L in both A and P. The test contract is `contracts/uniform-local-core-test.v1.json`.

The spectral rule constructs the carrier, encoding, operators and generators from the native factor maps. It does not accept an arbitrary per-source phase profile. Standard exponential laws prove continuity, unitarity and generator compatibility for all real parameters. Tensor factorization proves preservation of factor operator algebras, not merely slice locality. The written all-time proof is `uniform-local-core-proof.md`; exact supporting checks are in `results/uniform-local-core.json`.

`source-derived-local-core-exists` now has outcome **++ in standard complex-matrix semantics**, with a named spectral witness. The kernel-verified Cauchy-completion implementation is not claimed complete. This is a declared backend boundary, not a use of the still-open ScheduledNormBound.

The follow-up test now proves the whole-Tick return interpretation for this same witness and meaning of source derivation; see `spectral-whole-return-proof.md`. Combining L(f) and R_ext(f) proves the clarified parent in standard-C4 external-path semantics. The operational completion refinement remains open. The old numerical portfolio is historical; no numerical optimum is asserted.
