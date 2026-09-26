# Recursive signature-relative bridge and its exact limitation

## Checked construction

`agda/ObserverRRCRecursiveBridge.agda` defines an indexed `Term S q` with variable leaves and explicit generator calls. Every child is recursively another Term, not an opaque Resolve subtree. The retained generator signature is exactly the imported RRC Rule/Arity/input/output interface, including its supplied equivalences and higher witnesses.

Encode and decode recursively traverse every child. Both roundtrips are checked, giving `Resolve S q ≃ Term S q` for each endpoint and seed family. No histories or comparison witnesses are quotiented away. The result supports all declared RRC Rule tags, and in particular the previous native E/Pi fragment.

Separate recursively defined renaming and substitution satisfy:

- encode(mapSeeds f d) = rename f (encode d);
- encode(flatten d) = bind encode (encode d), where outer seed payloads are explicitly translated;
- encode(flatten(mapSeeds f d)) = bind (encode after f) (encode d).

The last two equations translate replacement histories recursively: no opaque Resolve child remains in the final Term unless a caller independently chooses Resolve itself as the external seed type. Substitution unit and associativity are also checked.

An explicit dependent boundary (rule, recursively typed children) assembles a call through the actual DSC `execute` interface. Child arities may be infinite: these are well-founded indexed trees with dependent-function branching, not necessarily finite serialized programs.

## What the theorem means

This is an isomorphic signature-relative presentation of retained RRC histories, with a checked substitution algebra and a DSC semantic interface. The parallel grammar is deliberate. It proves recursive retention and substitution compatibility, NOT a reduction of RRC's primitive signature to bare DSC composition.

The added `call` constructor and imported Rule values are assumptions of this syntax extension. Their evidence can include source functions/equivalences; representation does not construct those witnesses. The primitive inventory has not shrunk. No autonomous object-level evaluator, search procedure, finite runtime or operational complexity equivalence has been obtained.

Thus the programme must distinguish three layers:

1. DSC's existing semantic context/substitution interface;
2. this explicit signature-relative syntax extension;
3. the retained RRC generator signature it assumes.

A claim that layer1 alone derives layers2–3 still lacks evidence. The next existing source-signature branch should record the precise generator admission boundary and separate derivable structural substitution from externally supplied construction/comparison capabilities. No duplicate operational branch is needed.

## Fresh verification

The new module passes fresh safe Cubical Agda with --ignore-interfaces -Werror; see results/agda-rrc-recursive-bridge.log.

The canonical aggregate was freshly rerun after adding both bridge modules:48 entries,189 source/checker files unchanged,110.445 seconds, with both false-theorem controls rejected. See results/operational-checkpoint.json. No Nima-owned source was edited. Admission to the coordination graph does not certify the foundational interpretation.
