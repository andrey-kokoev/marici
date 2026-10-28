# Conjecture: is the 126 response forced by routing symmetries?

## C1 — strong conjecture (falsified)

> For the edge-7 octahedral P/E occupancy, a nontrivial local N port rule that preserves reversible one-to-one routing, threefold symmetry about the distinguished face, geometric P/E duality, and no branching necessarily produces 126 open-channel dual response pairs.

All tests use the same object, native lattice, ambient-reference subtraction and exact full-trajectory geometric pairing. The main counterexamples also keep the same imbalance trigger and **the same 248 switched N cells**. They change only the matching of the companion three strands.

## C2 — restricted conjecture (not falsified by these tests)

> If coupling is confined to the distinguished-face port triplet and its opposite triplet, the other three strands are fixed straight, and both one-occupied-face and seven-occupied-face cases undergo a nontrivial cyclic switch, then the edge-7 response has 126 open dual pairs regardless of the handedness choices for those two cases.

This is a narrower conditional claim, not a repair of C1 by pretending the extra hypothesis had already been proved. All four handedness choices were tested. Nothing here derives the face-only interaction restriction from physics.

## Local matching enumeration

The twelve edge ports form four three-element orbits under the distinguished face's C3 rotation. Exhaustive enumeration gives:

- 10,395 fixed-point-free involutive matchings of twelve ports;
- **27** commuting with C3;
- **3** when the companion three strands are additionally fixed straight;
- **2** nontrivial choices under that extra restriction.

The count 27 also follows combinatorially: each odd three-element orbit must be matched to a different orbit; there are three ways to pair four orbits, and three cyclic offsets for each pair, giving `3 × 3 × 3`.

Thus “only straight or the two cyclic shifts” describes a restricted six-port interaction, **not all symmetric twelve-port rules**.

## Attempts and outcomes at edge 7

| Policy | Switched N cells | Rerouted open channels | Open dual pairs | Closed loops |
|---|---:|---:|---:|---:|
| Reference cyclic | 248 | 252 | 126 | 0 |
| Reverse both handedness choices | 248 | 252 | 126 | 0 |
| Reverse vacancy-case handedness only | 248 | 252 | 126 | 0 |
| Reverse occupied-case handedness only | 248 | 252 | 126 | 0 |
| Occupied-face trigger only | 168 | 252 | 126 | 0 |
| Vacant-face trigger only | 80 | 120 | **60** | 0 |
| Cycle both port triplets | 248 | 396 | **198** | **128** |
| Reverse the companion-triplet cycle | 248 | 396 | **198** | **144** |

The last two are the decisive counterexamples: the same triggers and switched cells yield a different response while preserving all the symmetries stated in C1. Their extra cycles act on the other six edge ports, forming the companion three strands. The companion cycle is drive-even in the local oriented frame; the distinguished-face cycle remains drive-odd. The full matching commutes with **geometric P/E inversion**, as checked on every port.

A drive-odd version of the companion cycle was also tried. It **failed geometric P/E duality** and was rejected; it is not counted as a valid counterexample. Reversibility and C3 symmetry alone would not have exposed this failure.

A possible additional requirement of fixed-geometry charge conjugation is distinct from the geometric P/E inversion implemented here. Such an extra law, or a restriction to face-supported interactions only, might exclude these counterexamples. Neither has been independently established.

## Robustness and exclusions

For both companion-strand counterexamples:

- all local ports remain paired by a fixed-point-free involution;
- the distinguished-face C3 rotation commutes with the local routing;
- geometric P/E duality commutes with the entire routing;
- every local pass is retained exactly once across open paths and closed loops;
- the number of open boundary channels remains fixed; they are rerouted, not merged;
- enlarging the ambient lattice preserves 198 open dual pairs and the respective 128/144 closed loops;
- removing P/E occupancy restores the identity response and removes all loops.

Closed loops are routing cycles, not demonstrated bound neutron states. The 198 counts refer to pairs of **open** response paths and do not fold loops into a fitted total. `localizedNeutronCount` remains null for every policy.

## Conclusion

**C1 is falsified.** The 126 result depends on keeping the companion strands straight (or on an additional law implying that restriction), not on the stated symmetries alone. **C2 survives the finite tests performed**, but is not a physical identification of 126 neutrons.

The viewer keeps the original cyclic rule as reference and now warns that equally symmetric counterrules give different counts. No counterrule is silently substituted into the displayed geometry.

## Reproduction

```
node scripts/falsify-n-routing-conjecture.mjs
node --test tests/routing-symmetry-falsification.test.mjs
```

Sources: `research/strominger/routing-symmetry-falsification.mjs` and the policy variants in `research/strominger/pe-coupled-n-routing.mjs`.
