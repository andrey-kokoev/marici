# Controller covariance requires reflected contexts and event labels

**New batch, iteration 3 of 10.**

**Strength:** exact mask, labelled-transition and predictive-quotient symmetry tests for the supplied controller. Not derived control or parity preparation.

[Previous orbit adapter](SYMMETRY-ORBIT-ADAPTER.md) · [Checker](check_controller_reflection.py) · [Receipt](results/controller-reflection.v1.json)

## 1. Fresh test: primitive masks versus retained contexts

The current continuation asks whether the conditional controller preserves the parity assumed by the rank-two construction. We recompute its eighteen contexts, allowed primitive choices and labelled transitions, rather than assuming symmetry from the bare graph.

Let R be primitive reflection and J be the induced controller reflection. J permutes the twelve boundary states and the six internal composite-progress states; the latter map is derived from the reflected length-two macro IDs. Each context's expected primitive and available outgoing set map to those of its reflected context.

A single primitive mask M_p on the full ten-primitive registry does not commute with R. All eighteen context masks have commutator rank two and odd-to-even leakage rank one. A concrete odd input e_p-e_Rp becomes e_p after the fixed selector, losing its odd parity.

This test is on the full registry. Four contexts are endpoint-forced, where a mask is already identity on the local available set; they do not impose an extra local choice. Reflection maps their local domains to different reflected contexts. The full-registry leakage claim must not be confused with extra local control cost in those four cases.

## 2. Keeping contexts restores the correct joint covariance

Use the carrier whose slots are (context,available primitive), rather than applying one fixed mask globally. It has **32** slots. Joint reflection sends

    (c,p) -> (Jc,Rp).

The selected diagonal mask accepts the expected primitive in each context. Its complement retains every rejected available primitive. Both commute with joint reflection, are complementary idempotents, and have ranks:

| Record | Total rank | Even rank | Odd rank |
|---|---:|---:|---:|
| Accepted | 18 | 9 | 9 |
| Rejected | 14 | 7 | 7 |

Adding accepted and rejected records recovers all eligible coefficients. This is the retained direct-sum representation of the existing conditional masks, not a newly derived actuator. It shows that pairing contexts resolves a symmetry objection, while leaving the policy itself supplied.

The bare primitive selector and the context-conditioned family are different maps on different carriers. Their parity results are therefore not contradictory.

## 3. Labelled events versus aggregate dynamics

For each primitive p, form the actual eighteen-state transition matrix T_p from the supplied segmented automaton. Exact checks give

    J T_p J = T_Rp,
    J P = P J,    P=sum_p T_p.

Every nonzero primitive-labelled branch has nonzero odd-to-even leakage. Summing a reflected pair T_p+T_Rp removes the mixed-parity blocks; summing all events yields the parity-preserving aggregate P.

Thus the machine is **covariant across reflected labels**, not parity-preserving within each fixed label. Conditioning on a primitive label differs from aggregate propagation. The full event observation also records pair and completion flag; reflection maps

    (pair,p,completed) -> (1-pair,Rp,completed).

The checker verifies this mapping directly on the transition arcs. Aggregating a reflected orbit is a coefficient sum that no longer distinguishes its primitive label. It is not an authorized physical erasure or a proof that a record-bearing instrument prepares an odd system state.

This distinction is the next frontier: the previously used aggregate micro/macro operators should not be treated as conditional labelled dynamics without retaining the label register.

## 4. The predictive quotient respects reflection without deleting its residuals

The independently checked sixteen-class predictive quotient also admits reflection. If Q sums equivalent contexts and J_q reflects classes, then

    Q J = J_q Q.

Its even and odd subspaces each have dimension eight. The two difference records needed for exact eighteen-coordinate reconstruction are exchanged by reflection. They are not discarded or reclassified as prepared outputs.

This confirms that the prior minimal-memory construction is compatible with covariance. It does not change its observational scope from predictive event counts to lossless source history or physical memory.

## 5. Result and continuation

The supplied controller can be made mathematically reflection-covariant without changing its policy by keeping reflected contexts and all rejected records. However, selecting a primitive event branch does not preserve the controller's odd parity. Aggregate covariance alone therefore does not solve odd preparation.

Next, lift the labelled transition family to an explicit system/event-register output. Test joint reflection parity against parity of each conditional system record. Identify the signed recombination or label-erasure operation required before reading aggregate transport as prepared odd dynamics. Preserve original path history throughout.

No source-authorized policy, parity preparation, physical measurement or photon output is admitted. The scientific root remains null and existing formal contracts remain unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_controller_reflection.py
python research/scattering/seed-composition/check_controller_reflection.py --check
python research/scattering/seed-composition/check_symmetry_orbit_adapter.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

All matrix identities and ranks use exact rational arithmetic; prerequisites are recomputed. Only this checker's receipt is written; `--check` is read-only.
