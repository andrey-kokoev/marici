# Persistent NN core repaired at origin4 — net iteration8

The final core `[13,18]` has a certified extension at **D4**. Combined with the D2/D3 source contradictions, this establishes minimum completion origin4 for that marked core.

The source-guided search found a witness in49 search nodes. After removal of individually dispensable records, it has8P/6N/8E,42 retained records and41 representative construction operations. Every prefix was replayed from the root; the final selected set passes all source contact/root/exit checks. Record reduction is single-deletion minimal, not global optimization.

## The interface did not need a new face

| Budget | Native operations across core face | Compatible with core and incoming support | Completion outcome |
|---|---:|---:|---|
|D3|4|2|impossible|
|D4|7|2|certified extension|

The two useful operations are the same in both universes:

- packet13 (origin2) → packet27 (origin3), NN-phase-advance;
- packet18 (origin2) → packet28 (origin3), NN-phase-advance.

They cross the occupied face between neutron cells8 and12. The additional D4 face candidates do not explain the repair: the compatible pair count stays2.

## What changed: continuation of the face witnesses

At D3, with the forced incoming support retained:

1. The optimistic source analysis removes packets27 and28 because neither can reach an E exit.
2. In the next elimination round, the mandatory NN face has no remaining witness.

Thus the earlier statement that the face had no possible witness refers to the viability-filtered graph, not immediate endpoint incompatibility.

At D4, the saved construction supplies:

```text
N packet27 @3 → P packet55 @3 → P packet59 @4 → E packet152 @4
N packet28 @3 → P packet60 @3 → P packet64 @4 → E packet157 @4
```

The steps are **inverse-PN**, **reader-phase-advance**, then **experimental-terminal-PE**. Both exit paths are retained in the receipt and checked on the final selected configuration. Each necessarily reaches origin4.

The incoming support requirements themselves are unchanged: forbidding the mapped packet1, or forbidding packet4 after selecting packet1, still yields a source contradiction. What changes is that the required face-witness readers now have viable continuations.

## Structural conclusion

Face geometry and factor validity alone do not decide whether an interface is usable in a completed assembly. The endpoint readers must fit into the whole entry-to-exit network. Here an origin increment in a downstream proton reader makes an already available NN face connection usable.

The nine original cores are now fully classified by minimum completion depth: **eight at3, this one at4**. That concerns each retained marked core with other support freely synthesized, not arbitrary full configurations containing it.

## Next frontier

Prove the general prefix-completeness property of the current conditional-interface grammar: every finite compatible rooted selected set should have a construction from the seed, because compatibility is hereditary and active native/PE edges remain active in subsets containing their endpoints.

The proof must name those hypotheses. A rule requiring extra positive support can break the property. An exhaustive generic small-graph test and such a counterexample will accompany the proof. This turns the observed complete-family agreement into an explicit structural reason that interface-driven generation is complete for this grammar.

## Reproduction

```sh
node research/nima/checkers/check_persistent_nn_depth4.mjs
```

[Checker](checkers/check_persistent_nn_depth4.mjs) · [D3/D4 comparison, witness, exit paths and hashes](results/persistent-nn-depth4/verification.json)
