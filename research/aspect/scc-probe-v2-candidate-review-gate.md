# SCC probe-semantics v2 candidate review gate

## Question

Does the tested probe interface warrant a versioned SCC successor, and can legacy registry entries migrate without acquiring false interaction claims?

## Claim boundary

This packet creates a review candidate outside the live SCC directory and simulates migration. It does not replace or mutate the live contract or registry.

## Decision

The shadow compiler supports two semantically distinct entries and the schema delta has explicit checks. This warrants a versioned review candidate, but not live admission. The unresolved implementation premise is compatibility with the live compiler and all existing registry checks.

`contracts/scc-contract-probe-semantics.v2.candidate.json` binds the exact version-1 digest, preserves all existing stages, and inserts `probe_configuration` and `probe_rewrite_certificate`. It records seven semantic sections, six registry checks, typed migration defaults, invariants, outputs, and admission requirements.

## Migration rule

Every version-1 registry entry is preserved byte-for-structure inside a migration envelope and receives:

- `probe_semantics_status: untyped_for_probe_semantics`;
- `interaction_defect: null`, meaning not constructed;
- `probe_fields_constructed: false`.

The migration does not interpret missing probe fields as successful factorization or zero interaction. Existing scientific status is unchanged.

## Admission blockers

A live successor still requires:

1. explicit review of the candidate;
2. a versioned registry successor;
3. migration checker success;
4. shadow Schur and polarizer entries;
5. compatibility tests against the live compiler.

Only the first four are represented or tested here; live compiler compatibility remains open.

## Disposition

The candidate is ready for explicit review but not admission. The migration simulation is lossless for legacy entries and introduces no probe claims. Live SCC version 1 remains authoritative.
