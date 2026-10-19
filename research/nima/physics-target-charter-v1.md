# Bounded physical target charter — iteration 3

## Frozen decision

Select two primary physical targets:

1. **`reciprocal-lossy-cavity-ordered-response`** — one-mode, phase-locked, finite ordered cavity responses with retained returning field and loss ports.
2. **`finite-dead-time-detector-records`** — zero/one-photon preparations, ready/dead detector memory and complete click/no-click histories.

Both are bounded to sequences of at most three steps. The [charter](contracts/physics-target-charter.v1.json) fixes regimes, source IDs, ingredient roles, recovery laws, exact controls, empirical acceptance requirements and candidate dispositions. [Catalog v3](../conjecture_net/contracts/physics-target-catalog.v3.json) preserves every v2 entry and adds the two precise instances of its cavity/detector candidate.

This completes `source-target-charter` as a reviewed target specification. The common source, physical realization records, empirical dataset and root assembly remain open.

## Why this pair

Both targets have explicit finite source models and inexpensive exact composed-operation tests. The cavity requires phase, ordered ports, stored field, energy normalization and environment. The detector requires outcome-conditioned memory, preparation order and complete records. Their shared-source comparison therefore tests retained operations and history, rather than a common scalar summary.

Compton remains a reserve complete-record target. High-energy scattering remains a deferred primary expansion with numerical, source-law, scale/species and readout gates. The retained coefficient Hamiltonian awaits physical preparation/clock/actuator/reader maps. Sontag's coherent-Gamma optical controller remains a reviewed conditional contribution; its preparation and ideal Poisson instrument require comparison before use with the finite-memory detector.

These dispositions concern the primary central target set. Source-owner research continues under its own contracts.

## Cavity recovery contract

Registered source: `instrument.reciprocal-lossy-cavity.v1`.

Retain the ordered input mirror, end mirror and loss dilation. At the nominal phase-locked setting,

```
y_r = -r1*u + t1*x       f = t1*u + r1*x
y_t = t2*f - r2*v2       b = r2*f + t2*v2
x_next = a*b + ell*w     y_e = -ell*b + a*w
```

The complete input is `(u,x,v2,w)` and output `(y_r,y_t,x_next,y_e)`. Each component uses its declared common energy metric. The next returning state becomes available after the physical round-trip delay. The source map must preserve this order, state and environment, and commute with composed operations and output maps.

The exact reference fixture is

`(r1,t1,r2,t2,a,ell)=(3/5,4/5,4/5,3/5,3/5,4/5)`.

For input `(4/5,3/5,0,0)`, the output is

`(0,3/5,12/25,-16/25)`.

The reflected port is dark while returning field `12/25` survives. A subsequent zero-drive round trip has reflected amplitude `48/125`. Deleting the state after the dark output fails this continuation test. The complete dilation preserves energy; the projected detector ports alone form an open system.

The fixture values are theoretical regression parameters. Physical predictions must use independently frozen parameter, phase, delay, preparation and readout calibration. The source-law task must identify which optical ingredients are imported and what additional constraint the proposed carrier actually derives.

## Detector recovery contract

Registered source: `instrument.dead-time-detector.v1`.

The preparation domain is a sharp zero/one optical input and a classical ready/dead memory distribution. The source instrument has a full CP completion with separate Kraus environment labels. Each photon is destroyed; the next preparation changes the optical input without resetting memory.

Let eta be ready-state detection probability and gamma dead-state recovery probability. A click moves ready to dead. A dead detector cannot click in that bin; it recovers with gamma after producing no-click. Every outcome-conditioned memory state, including no-click branches, participates in the next step.

At the reference `eta=gamma=9/25`:

| Complete-record prediction | Probability |
|---|---:|
| `CC` for inputs `11` | 0 |
| `NC` for inputs `11` | 144/625 |
| `CNC` for inputs `101` | 729/15625 |
| Next click after one empty gap, conditional on the previous click | 81/625 |
| Incorrect iid-reset prediction for `CC` on `11` | 81/625 |

The joint triple-word probability and conditional recovery probability are kept distinct. Independent trials require physically certified initial readiness. Bins within a trial are history dependent.

Multiphoton pileup, afterpulsing, graded recovery, continuous-time claims and unbounded dark-count effects lie outside this charter. Any instrument discrepancy used in an experiment must have an independently justified contribution to the frozen error budget.

## Frozen target-level empirical decision

The required discrepancy tolerance is **1/100** in normalized mean cavity amplitudes or detector word probabilities. It is a design requirement, not a measured accuracy. Cavity amplitude units require an independently fixed nonzero reference.

For each target, let P be the complete prediction set from independent calibration and C the simultaneous held-out confidence set for the frozen finite observable vector.

- **Reject** if every pair of points from C and P differs by more than the tolerance in the infinity norm.
- **Accept at the tested target scope** only if every such pair differs by at most the tolerance and the source, preparation, record and protocol gates pass.
- **Inconclusive** otherwise.

Both sets must be nonempty and have certified bounds. The overall error allowance is 1/100: 1/400 for calibration coverage and 1/400 for held-out coverage for each of two targets, by the union bound. Coverage within a target must be simultaneous across its observable vector.

The next empirical-protocol task must freeze the observable vector, sample/stopping rule, preparation/reset checks, nuisance bounds and preprocessing before validation data. Calibration and validation observations and dependencies must be disjoint. All complete records remain available; model fixtures supply no confidence set or empirical evidence.

## Common-source and overlap task

The charter binds each target to its own registered source ID. It supplies no cross-source identity.

A concrete proposed overlap domain is a **separately constructed single-excitation lift of the full passive cavity dilation, with ready/dead detector memory**. The two comparison routes are:

1. common carrier -> cavity history -> specified quantum/preparation lift -> detector records;
2. common carrier -> joint optical-memory instrument -> the same records.

Construct preparation, output-port/time-bin routing, clock, environment and memory maps before asserting that these routes agree. The current classical/coherent amplitude model and the at-most-one-photon detector are different source descriptions. Their quantum preparation relation and any Born pairing are explicit ingredients, not consequences of equal amplitude dimensions.

The phase-sensitive hostile from iteration 1 and memory-reset hostile above constrain the permissible state quotient. Gamma/Poisson count feedback cannot replace the finite detector's instrument without a versioned comparison.

## Independent verification

The new checker reads owner sources without running their result-writing programs. It verifies:

- 16 complete cavity orthogonality entries and 27 two-step state/resource cases;
- the dark/refeed prediction and component-order/loss-compression controls;
- 2295 full-joint versus two-state detector history squares through three bins, across nine rational eta/gamma pairs and three initial memory distributions;
- 405 complete-record normalizations and 36 Kraus completeness entries;
- exact nominal detector predictions and iid/postselection controls;
- accept/reject/inconclusive interval decisions;
- eleven corrupted charter variants rejected.

```sh
python research/nima/checkers/check_physics_target_charter.py
python research/aspect/scc/scc.py check physics-programme-v18
```

The [result](results/physics-target-charter-v1.json) exports the reviewed target-scope interface, catalog/charter hashes and target-set digest. The central checker verifies these bindings and dynamically activates the instrument-common-source requirement for both selected targets. Per-target realization records and a shared source witness are still required at assembly.

## Next executable frontier

- Sontag: instantiate the selected preparation/observation/resource interfaces.
- Benincasa: choose an explicit common-source candidate and construct the optical-port and memory geometry maps.
- Strominger: test an independently justified source operation law against both target histories.
- Nima: specify overlap routes and rivals, and bind the accepted structural pilot at its existing scope.

These are suggested research leads, not task claims. Physical and empirical admission remains governed by the existing downstream gates.
