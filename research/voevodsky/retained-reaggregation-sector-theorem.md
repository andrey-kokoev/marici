# Shared sector-decomposition and exact-dynamics conjecture

Contract: `contracts/retained-reaggregation-sector-theorem.v1.json`.
Admission/routing: `checkers/sector_theorem.py`, integrated into
`checkers/reaggregation_harness.py`.

## Position in the net

```text
common interface ++   primary rule ++   rival rule ++
                  \         |         /
           shared sector theorem ++
                  /         |         \
       accounting ++  classification ++  discriminator ++
                  \         |         /
               conditional comparison ++
                         |
                physical admission ?
```

The arrows from the umbrella are **scoped proof-reuse routes**, not automatic
outcome propagation. The discriminator still requires admitted accounting and
classification. The final comparison still requires its own target-scoped proof.

The extension adds one named umbrella conjecture to the combined net view:
eight canonical lifecycle nodes, four rule refinements, and one umbrella (13
obligations). It does not change frozen source contracts or invalidate their
existing receipts. Its digest is pinned by a history-preserving ledger migration.

## What must be proved

Identify the actual frozen source K and establish self-adjointness and
[K,c]=[K,Pi]=0; **do not assume these relations** or silently replace K by zero.
Derive both complete generators from signed controls, with one common empty
reference, retaining all complementary records:

    H_P = K + N - g P tensor X,
    P = Pi (primary) or c-Pi (rival).

Then derive exact sector propagators, conserved carrier-number/charge sectors,
and a distinguishing readout at the frozen time with exact or certified bounds.
Account for joint energy, measurement effect and the retained post-readout state.
Classification must also state the variable-phase contract. Neutral dressing is
not automatically carrier annihilation, physical photon production or selection.

The contract lists five assumptions to establish and thirteen conclusion checks
partitioned among the three existing consumer claims. A failed commutation or
readout check is a blocker, not by itself an admitted refutation of any claim.
Scoped counterexamples continue through existing rejection actions; no fan-out
of refutation or failed-attempt outcomes is implemented.

## Operational route

All three conclusion actions and the final comparison are complete. No further
conditional action is recommended. There is no new
independent prior, start action, duplicate charge or bundled cost estimate.
The three existing conclusion actions retain their own effort costs and nonces;
this route shares proof evidence, not free lifecycle admissions.

The theorem is **++**, through the discriminator's fresh shared bundle. The
selected cycle-defect K, zero vacuum extension, phase contract, complete generator,
readout and retained-sector identities are proved in all four native cases. The
bundle records local assistant mathematical/code review, not independent human
review, kernel certification or physical admission. See
[the complete conditional proof](retained-comparison-closure.v1.md).

The theorem-specific verifier and local review produced a shared JSON bundle with:

- `schema`: `marici.voevodsky.sector-theorem-proof.v1`
- `theorem_id`: `shared-sector-decomposition-and-exact-dynamics`
- `status`: `admitted`; `fresh_execution`: true
- `physical_admission`: false; `kernel_verified_analytic_theorem`: false
- nonempty `reviewer` and `proof_kind`
- `assumptions`: every contract assumption mapped to literal true
- `conclusions`: each consumer ID mapped to its exact named checks, all true
- `verifier`: path and SHA-256 of the reviewed theorem-specific verifier
- `source_hashes`: verifier and all proof dependencies, including the frozen
  contract, sector-theorem contract, selected-K contract and `checkers/sector_theorem.py`.

A bundle is a reviewed proof record, not a replacement for doing the mathematics.
The admission validator checks its declared scope, completeness and pinned
provenance; it does not synthesize a proof or independently audit arbitrary code.

A consumer's normal `marici.voevodsky.scoped-review-receipt.v1` (or the dedicated
`marici.voevodsky.retained-comparison-receipt.v1` discriminator gate) additionally
carries `sector_theorem_evidence: {"path": "...", "sha256": "..."}`, pins the
bundle, sector contract and selected-K contract in `source_hashes`, and copies exactly its own
conclusion check group into `checks`/`required_checks`. Its node, intent, outcome
and nonce must still match the active attempt. Existing `finish` admission handles
this optional evidence link; unrelated, partial, stale or scope-upgraded bundles
are rejected. Ordinary independently reviewed proofs remain available.

The umbrella becomes `++` when a valid complete bundle is referenced by an admitted
consumer receipt. Other consumers remain unresolved until individually admitted.
The planning result reports umbrella readiness, assumptions, conclusion mapping,
consumer outcomes and shared evidence identities under `sector_theorem`.
