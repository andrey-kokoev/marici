# Review of the protected-sector transfer microprogramme v1

## Question

Can Kitaev's transfer proposal be integrated into the coherence-pyramid programme without collapsing typing, evidence, and authority statuses?

## Claim boundary

This review evaluates the interface design. It does not adopt Kitaev-owned registry entries or supply the absent transfer map.

## Accepted structure

The tuple

\[
(S,T,f,I,C,E)
\]

captures the minimum transfer data: typed endpoints, source-derived map, preserved invariant, descent/coherence certificate, and evidence. The strength separation and prohibited promotions agree with the coherence-pyramid gates. In particular, equal dimensions, commuting boundaries, and presentation-level checks do not construct a transfer.

## Required correction: two independent status axes

`authority_blocked` is not a member of the same semantic failure coproduct as

- `undefined`;
- `representative_dependent`;
- `underdetermined`;
- `inconsistent`;
- `unstable`;
- `counterexample`.

Those six classify the mathematical state of a proposed map after the relevant objects are available. `authority_blocked` classifies whether an available object may be used or mutated. Combining them loses cases such as:

- mathematically `undefined` and independently authority-blocked;
- mathematically untested because authority is absent;
- a proved counterexample whose publication or cross-locus mutation remains unauthorized.

Canonical integration should therefore use a product status

\[
\mathsf{TransferStatus}
=
\mathsf{SemanticDisposition}
\times
\mathsf{AuthorityState},
\]

where the authority coordinate is one of `authorized`, `self_claim_only`, `authority_blocked`, or `not_required`, as admitted by the governing surface. `untested` must be available on the semantic coordinate when authority prevents the first test; it must not be reported as `undefined` unless absence of the typed map is independently established.

## Required correction: split the certificate field

The field `C` should be replaced by separately typed fields:

- `descent_certificate`, proving representative independence;
- `coherence_certificate`, proving the required route equality or higher cell;
- `completion_certificate`, present only for completed strength.

A single certificate union permits a descent proof to be mistaken for associativity, interchange, or completion stability. Optional fields may be absent only when the target strength does not require them.

## Registry instance

The proposed `R_zeta` to `U_G4` branch is correctly non-admitted because no owner-authorized carrier or independently derived map exists. Its current semantic status should be `untested`, with authority state `authority_blocked`; radical stability and quotient coercivity remain separately `unverified`. No issue-tree waiting leaf should be created.

## Disposition

Integrate the admission tuple, strength gates, prohibited promotions, and hostile-test workflow after the two-axis status correction and certificate-field split. Do not canonically import the current registry status encoding unchanged.
