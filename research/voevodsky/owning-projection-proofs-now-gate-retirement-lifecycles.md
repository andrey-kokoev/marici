# Owning projection proofs now gate retirement lifecycles

## Integration delivered

The research wrapper `checked_retirement_interface.py` consumes real owning elimination packets. Its migration factory calls Grothendieck's independent `verify_case` against the separately supplied expected fine plan before constructing the retired state. Inputs are copied into canonical serialized context, so later caller mutation does not alter the retained snapshot.

The runtime stores the checked coarse descriptor, a migration binding, later public frames and explicitly selected capabilities. Query answers carry the expected retired descriptor and objective; arithmetic is checked by the existing independent source/LP verifier, without relying on the proposer for validity.

## Lifecycle controls

The forced-zero and coupled-surviving-audit owning cases both pass:

1. Verify projection and construct an answer-only retired state.
2. Optimize publicly, then append a public frame.
3. Independently check a new answer against the updated expected state.
4. Reject the earlier packet against that updated state, even where its mathematical optimum still agrees.
5. With lift capability, extend the public optimum through the exact retired-coordinate interval and construct a fine source witness satisfying the original evidence.
6. With archive capability, restore the fine evidence and append translated later public frames, inserting zero coefficients on the retired coordinate.
7. Reject missing capabilities, malformed/nonpublic frame dimensions, lifting after an impossible public refinement, and a projection packet with a missing runtime frame.

Fourteen lifecycle violations are rejected. Importing the owning research verifier also freshly replays its existing five migration cases and quadratic controls before these wrapper tests.

## Capability versus retained information

The answer-only state does not retain the fine plan or projection packet; its migration digest binds a transition, but cannot by itself independently replay it. A verifier of the transition still needs the expected fine context and proof archive. Query verification after migration presumes this descriptor has been admitted through that transition; it does not re-prove projection on every query.

The prototype lift capability stores the fine plan and full source/evidence row context. That data is sufficient in principle for re-exposure, although the method refuses it unless archive capability is declared. This is an explicit application policy, not an information-theoretic separation or confidentiality claim. More economical lift programs could reduce that context in specialized cases but are not implemented here.

Archive-only states can restore the fine relation without exposing the wrapper's lift method. The two feature flags name promised operations, not a universal ordering of necessary storage. The result records live descriptor, optional lift context, optional archive and full migration packet byte sizes separately.

## Limits

This is integration of existing proof contracts, not another projection theorem. It leaves the owning Nima and Grothendieck APIs unchanged. It assumes well-formed research inputs outside its targeted checks, relies on assertion-enabled verifiers and has a directly constructible dataclass; it is not a hardened unforgeable capability system. A separate lifecycle packet verifier now reconstructs the expected migration binding, coarse schema, appended frame, capability declaration and objective independently from the owning context. It imports neither the wrapper nor an optimizer. Both lifecycle records and their old-compatible fine lifts pass. Six mutations of migration binding, history, capabilities, query, fine lift and schema are rejected. This verifies the emitted semantic packets, not every runtime refusal path; lifecycle method policy remains directly tested by the producer.

Solver failures still remain operational failures, never proofs of inconsistency. The lifecycle workload succeeded on two owning migrations; it does not establish totality of the third-party solver or support for every future schema extension. Source binding is not observation authentication.

## Reproduction

    uv run --with sympy python research/voevodsky/checkers/check_checked_retirement_lifecycle.py
    python research/voevodsky/checkers/verify_checked_retirement_lifecycle.py

Artifacts:

- `results/checked-retirement-lifecycle.json`
- `results/checked-retirement-lifecycle-verification.json`

The integration closes the earlier fixture-only gap: real source-relative projection certificates now gate a retirement lifecycle with independently expected statements and explicit continuation capabilities.
