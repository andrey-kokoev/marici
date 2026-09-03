# Minimal SCC schema delta for probe semantics

## Question

Which fields are absent from the live SCC contract and registry but required by the tested probe-configuration semantics?

## Claim boundary

This packet proposes an opt-in schema delta. It does not mutate or admit changes to `research/aspect/scc/contract.v1.json` or `registry.v1.json`.

## Fresh comparison

The live contract declares stages from packet through admission, four authority invariants, and outputs including typed claims, hostile witnesses, generic residuals, admitted scope, missing constructors, and next falsifiers. It does not declare a configuration domain, restriction maps, matching maps, continuation-state interfaces, naturality squares, or typed residual kinds. The registry lists checker identifiers, stages, and paths but has no probe-specific check kinds.

A generic `residuals` output is insufficient: it cannot distinguish a matching-map failure, erased continuation state, kernel, cokernel, or additive cross-effect, and it does not type the map whose failure produced the residual.

## Proposed delta

`contracts/scc-probe-semantics-delta.v1.json` adds two opt-in stages:

1. `probe_configuration` after ports;
2. `probe_rewrite_certificate` after dynamic coherence.

It requires seven sections covering the complete admissibility domain, constraint presheaf, matching classification, optional additive valuation, continuation interface, rewrite certificate, and source authority. It also defines six registry check kinds for downward closure, functoriality, matching-map typing, continuation faithfulness, rewrite naturality, and source digests.

Legacy entries remain readable but are `untyped_for_probe_semantics`. Missing fields cannot be interpreted as zero defect or successful factorization.

## Admission gates

- Absence of a configuration and an empty constraint object remain distinct.
- A matching defect requires a typed matching map.
- A cross-effect requires additive target authority.
- Scalar readout cannot authorize state reconstruction without a faithful coordinate proof.
- Local rewrite naturality cannot certify global confluence.

## Verification

The checker binds the proposal to SHA-256 of the current SCC contract, confirms the required fields are genuinely absent from version 1, verifies all proposed sections and registry checks, and asserts that both live files remain outside the proposal's claimed mutation scope.

## Disposition

The minimal delta is specified and mechanically checked, but intentionally not admitted. The next implementation gate is a versioned SCC contract successor plus migration behavior for legacy entries; that requires a separate review because it changes the compiler's public schema.
