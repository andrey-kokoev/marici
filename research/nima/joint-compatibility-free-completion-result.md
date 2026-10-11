# Tested result: joint completion adds zero prediction constraints

## Disposition

The strict added-selection claim in
`contracts/joint-compatibility-free-completion.v1.json` is falsified.
Every admissible retained-unitary annotation receives the same canonical
state geometry and consistent fixed quantum readout. The completion preserves
the generator, preparations, effects and all record probabilities. Forgetting
it recovers the original annotation, so the prediction sets are equal.

The conjecture that sharing compatible structures by itself forces a new
observable restriction is withdrawn as a general sufficiency principle.
This construction uses quantum-state geometry and the existing two-factor
state model. Shared maps connecting the distinct spatial, flavor and gravity
sources remain unspecified; the ten-topic version has no complete test class.

## Evidence

The checker passes **878 exact checks**, including generic identities for all
16 real parameters of a Hermitian 4-by-4 generator and a second generic
Hermitian observer. The universal completion argument is in
`joint-compatibility-free-completion.md`.

The original k=0 and k=2 annotations both satisfy the new compatibility laws.
For preparation 00 at the dimensionless parameter pair (pi/3,0), their complete
ZZ records are (3/4,0,1/4,0) and (3/16,3/16,7/16,3/16). The probability of the
second factor's record 1 is respectively 0 and 3/8. Squared amplitude
determinants 0 and 3/16 retain the predecessor's obstruction to identifying the
rival with any baseline parameter pair or overall phase.

Sixteen model/schedule/preparation fixtures retain all four records in each of
nine Pauli settings. Full-state tomography reproduces each density matrix.

| Deliberate defect / extra requirement | Squared Frobenius residual |
|---|---:|
| Wrong Hamiltonian sign | 320 |
| Mismatched symplectic form | 20 |
| Wrong observer-transport sign | 64 |
| Intermediate tensor locality, tested on k=2 | 8 |
| Non-Hermitian generator | 16 |
| Odd coefficient violating a source corner | 4 |

Intermediate tensor locality is an additional selector that excludes k=2.
It is absent from the frozen annotation class. The original source constraints,
including its corner restrictions, remain intact throughout the attack.

## Verification

- SymPy 1.14.0 and current predecessor source hashes:
  `e_38524_1791468677093661000_203`.
- Manifest validation: `e_38524_1791469311452044600_205`.
- Prospective freeze:
  `scc-freezes/nima-joint-compatibility-free-completion.909e092e8f865e14.json`.
- Challenge with preregistered zero-exit meaning falsifies:
  `e_38524_1791469343751495900_207`.
- Fresh headless closure: `e_38524_1791469508998794100_208`.
- Failure lifecycle, transposed-completion hostile and current-source check:
  `e_38524_1791469600128012700_209`.
  AssertionError and RuntimeError remove temporary prior successes. Transposing
  the complex completion fails at `generic-state-effect-route`. All live
  receipts and bound inputs retain their original bytes.
- Receipt: `results/joint-compatibility-free-completion.json`.
- Opening graph notice: `ep_300cbf95-17f1-45ba-a532-70f39a02c0a8`.
- Tested report: `ep_b53d414d-fe3f-4570-acfc-05dc480a6a5c`.

The global SCC model inventory command returned exit 1; the scoped manifest
validation, freeze, challenge and closure above all pass. No shared registry
or foreign source was edited. The owner artifacts and this communication
interval remain uncommitted.
