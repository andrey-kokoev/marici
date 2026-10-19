# Prior WG operations and composition: correction of the rung discussion

## Correction

The operator clarified that the software presentation operations ARE WG operations. My earlier opposition between reindexing and WG application was incorrect. A presentation change can return a constructed successor and a recovery/coherence witness, and so instantiate a WG. Preserving underlying data does not disqualify it as generation.

The actual question is which typed operation, selector, witness and retained state each step uses. It is not necessary to replace the existing software operation with a new Hamiltonian or physical process before calling it WG.

## Direct prior source

`research/nima/label-from-to-fibration-tower.md`, under "Operator rule", states: each rung takes the previous record type and fibers it over the next field, label -> from-label -> to-label -> repeat.

For selected map p_k:E->X_k, its retained-total successor is

    T_k(E)=Sigma(x:X_k) Sigma(e:E) (p_k(e)=x).

It retains outer key, entire preceding row and membership path. Field maps for the next operation are pulled back through the preceding row projection. Each successor reconstructs its input; construction history still grows.

A uniform software WG can carry the selector phase as part of its state:

    WG(E,k,history)=(T_k(E),next(k),extended_history; recovery witness).

This formula is a synthesis of the inspected interface, not a newly compiled dependent-type implementation. With that state convention, if r12=WG(s), then r11=WG(r12)=WG^2(s) is coherent. One must include the phase and full output, rather than iterate a bare fixed-column dictionary operation and expect its meaning to change automatically.

The prior note starts r12 as an initial table and then applies label/from/to successively. The later `indexed-path-structural-synthesis.md` and clarified `rung-transport-diagram-and-fixed-reference.md` describe the base triple as disaggregated/source-indexed/target-indexed presentations. These phase conventions must not be silently equated: the historical first note reaches r11 by label; the later triple calls r11 source-indexed. The common underlying fibration/recovery construction does not alone settle the phase assignment.

Neither note identifies six successive applications with12->4. The first explicitly counts eight transitions among nine presentations. The later9/8/7 transport-role diagram is a different scheduling description; its composites need an explicit identification with any proposed iteration schedule.

## Composition results already present

1. `research/nima/whole-package-generators.md`: E-whole and Pi-whole take COMPLETE prior packages as values, preserving expression, value, maps and witnesses. `reify-history` makes an endpoint-and-derivation pair a new input package. The12 resolution schemas include comparison composition, higher comparison and E/Pi action on comparisons. Retained closure flattening has units and associativity. Reification raises universe level where required.
2. `research/nima/native-table-equivalence.md`: independently implemented typed recursive tables cover all8 constructor forms and12 native rule schemas, with an equivalence of complete packages and retained derivations for supplied source policies. This is stronger than bare regrouping of three scalar columns.
3. `research/nima/typed-generator-layer-2.md`: `Histories.generated` iterates the actual supplied generator; `join` composes matching histories with units/associativity. Compressing that history to one witness in the ORIGINAL relation needs separately supplied `Composition`; Boolean flips prove it is not universal.
4. `research/nima/typed-generator-layer-3.md`: dependent payload execution preserves joined-history composition. Stepwise execution agrees with composite-path transport in the path specialization.
5. `research/nima/typed-generator-layer-4.md`: certified presentation reductions have source/boundary recovery, observation preservation, composition and associativity. Presentation change is explicitly inside the generator stack.
6. `research/nima/composable-witness-specialization.md`: indexed refinement composition constructs the composite, preserves actual proof payloads and sources, supports rebase, units and an actual-operation associator. `Composer.WG` packages composition itself as a WG.
7. `research/nima/coherent-witness-specialization.md`: actual-operation pentagon and triangle preserve states, full steps, generated steps and sources. This is not inferred merely from equal scalar outputs.
8. `research/nima/retained-path-family-composition-synthesis.md`: concrete software composition concatenates endpoint-compatible weighted paths, retains parent operands and assembly trees, and verifies associativity of weighted outputs without erasing different bracketings.

## Boundaries that still matter

Being a WG operation does not make every operation the same WG specialization. Reindexing, total-family construction, dependent sections, path concatenation, witnessed comparison and refinement composition have different typed inputs/outputs.

Pi-sections must not be identified with Sigma-total rows or opposite-endpoint grouping. The native recursive constructor implementation explicitly supplies more structure than bare reindexing. Likewise concatenating paths changes length; reindexing alone does not.

The fibration route note itself already warns not to mistake flat row readouts for absence of retained comparison/history structure. This supports the operator's correction and should have prevented the earlier oversimplification.

## Fresh checks and search scope

Executed successfully:

    python research/nima/checkers/check_label_from_to_fibration_tower.py
    python research/nima/checkers/check_indexed_path_synthesis.py

First:147 tables,1176 retained fibration transitions, complete reconstruction and total-versus-section hostile. Second: endpoint-indexing recovery, retained path composition and association checks at lengths1,2,4.

The generic proofs and higher composition modules were read through their source notes; no fresh Agda compilation is claimed here. The search is bounded, not an absence theorem. No source-owner files, native operations, physical claims or selected software T9 contract were changed.

## Consequence

Resume the rung investigation from WG operation composition, carrying phase, complete previous package and witnesses. Do not make a fresh physical-control theory a prerequisite. The pending identification is the exact operation schedule for the user's diagram, not whether software WG can operate on its own prior output.
