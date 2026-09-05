# Native completion-preservation contract

## Question

Can a cubical adapter be required to preserve the declared completion cone rather than merely map between completed carriers?

## Claim boundary

The module defines and composes completion-preserving maps for a typed base and two completion cones. It does not identify the RH source-global completion or establish that the existing JSON adapter realizes this contract.

## Construction

A completion cone contains a completed type and an injection from its base. A completion map contains a map of completed types and a path

\[
f(\iota_S(x))=\iota_T(x)
\]

for every base element. Identity and composition are proved to preserve this equation, so completion-preserving adapters form a composition-closed class.

## Strongest falsification attempt

`negative/BadCompletionMap.agda` uses the natural numbers with identity completion injection and proposes successor as an adapter. Agda rejects its preservation face with `n != suc n`.

## Disposition

Completion preservation is now a native proof obligation rather than an unchecked `cubical_adapter` descriptor. Instantiating the contract with the RH source-global completion remains a separate source-typing task.

## Verification

- `research/voevodsky/agda/CompletionPreservation.agda`
- `research/voevodsky/agda/negative/BadCompletionMap.agda`
- `research/voevodsky/results/cubical_agda_completion_preservation.json`
