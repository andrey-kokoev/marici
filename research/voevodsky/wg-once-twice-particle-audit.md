# Witness Generator and the one-pass/two-pass particle conjecture

## Search and verification scope

Read the current WG paper, ledger glossary, Layer 1/2/3 notes, meta-generator and nested-specialization notes, retained tetrahedral package note and its actual Agda implementation. Also inspected the incidence-rung tower and the earlier inner-face electron hypothesis. This is a source-reading audit: no Agda compilation or mathematical checker was rerun.

## What WG actually is

For declared complete states S and a relation R:S->S->Type, a Witness Generator is

    G : (s:S) -> Sigma(t:S) R(s,t).

It selects a next state and returns an actual witness relating input to output. The definition is an interface, not an algorithm for discovering arbitrary witnesses. Admission conditions, geometric realizations and physical laws must be supplied. The output may equal the input.

The implementation `research/nima/agda/TypedGeneratorLayers.agda` has exactly State, Witness and generate fields. `next` and `edge` are their two projections. Layer 2 adds histories with intermediate states and relation witnesses; their checked length records the number of calls. A two-step history is not automatically a single witness of the original relation. The Boolean-flip control makes that distinction explicit.

Source: `papers/witness-generators/main.md`, `src/ledger/4296 Witness Generator Glossary and Scope.md`, `research/nima/typed-witness-generator-layer.md`, `research/nima/typed-generator-layer-2.md`.

## Three inequivalent readings of “twice”

1. Execute the same selected next-state map twice: s -> s1 -> s2. A retained history distinguishes the calls even if s2=s1 or s2=s. No increase of spatial dimension or coefficient capacity follows merely from the count.
2. Refine a WG twice: add admissions and evidence to a transition. The nested-specialization implementation can flatten two layers while preserving the original transition and proof payload. This is additional retained evidence, not necessarily a second material assembly.
3. Promote an output package to the input of another construction: the second pass may compare whole first-pass records rather than their original elements. This requires an explicit promotion/admission map and a typed operation on those records. It is the most productive possible reading of the user's growth conjecture, but is not automatic from the WG type.

A macro-WG can return the endpoint of two microsteps with their entire History-2 witness, so the raw number of invocations depends on the chosen primitive interface. A particle-relevant depth must therefore be attached to a frozen source operation or promotion grammar, not the spelling of a wrapper function.

Source: `research/nima/meta-witness-generator-pilot.md`, `research/nima/nested-witness-specialization.md`, and the current tutorial's refinement composition.

## How arrows, faces and volumes enter

For a general R, WG returns only the declared witness. If R is path equality, existing path composition and coherence can build edges, triangle comparisons and tetrahedral comparisons. The type theory already supplies that structure; the words “witness generator” do not generate arbitrary spatial dimensions.

The generated-path construction starts with three successive transitions A->B->C->D, constructs composite edges, and compares their parenthesizations. This is not a theorem that one WG call means a plane or that two calls mean a volume.

There is also a concrete request/answer tetrahedral WG. Its admitted request already contains four vertices, six edges and three compatible face witnesses. It supplies the missing face together with a coherence filler and retains the original horn. The filler is a path-coherence witness, not automatically an occupied Euclidean volume.

## Decisive current-code control: the same completion WG twice does not grow

In `research/nima/agda/RetainedTetrahedralPackage.agda` the current definitions are:

    WGState = Request + Full
    generate (request q) = (answer (build q), completed q)
    generate (answer p) = (answer p, retained p).

Thus the first call completes the admitted horn; the second retains the same package. Two calls can have different history length but identical resulting geometry. This directly blocks identifying the *existing* completion WG's first and second calls with two geometrically different particles without an intervening new operation.

The older `inner-face-electron-candidate.md` discusses the same lack of an automatic particle-birth rule. Its description of an identity-retention WG must be read alongside the current request/answer implementation, which does perform completion on requests but is stationary on completed answers.

## Prior examples of genuine growth

`research/nima/incidence-rung-tower.md` explicitly separates source/target grouping, which preserves the graph, from a promotion, which takes its line graph. For a tetrahedral graph the first promotion produces the octahedral graph. A second promotion gives a different graph again. This is an existing example of a repeated constructive rule with nontrivial growth, but it does not select electron/proton states and is not the same operation as tetrahedral horn completion.

`research/nima/typed-generator-layer-3.md` also separates repeated execution from transport: one turn in a supplied circle double cover flips a fiber value, two restore it with nonempty history. Those nontrivial loops are supplied route inputs, not iterations of its identity generator. It cannot be cited as a particle-specific pass counter without the missing source bridge.

## What the conjecture must specify

A testable one-pass/two-pass claim needs:

- the complete common input, including whether AA is only a vertex mark or carries a typed value;
- the actual generator term, its admission and witness relation;
- what one complete pass means at the chosen primitive level;
- any promotion that makes the first output a new input rather than a retained final answer;
- explicit comparisons of the first output with the stored electron and the second with the stored proton, preserving source labels, local selectors and transports;
- accounting for retained or discarded components when coherent rank changes.

The last condition is important because the stored electron uses spinor coefficients and the original proton uses vector coefficients. If a fixed linear operator were equivariant for the same binary rotation action, applying it twice could not change central character from -1 to +1. A nonlinear spinor-square operation can change that character, but it would be a specific supplied WG transition, not a consequence of calling an arbitrary WG twice.

## Current conclusion

The conjecture remains a useful *construction-depth hypothesis*. The located research gives both formal tools to state it and counterexamples to inferring it from pass count alone. No inspected source already identifies the electron with one WG pass and the proton with two.

The next useful experiment is to trace the actual geometric/coefficient constructors into explicit request/answer records and identify a candidate nontrivial promotion between passes. First test the source-level records; do not use later field Hamiltonians, transfer counts or viewer animations as a substitute for this missing operation.
