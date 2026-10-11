# Pentagon and triangle for the actual refinement operation

`agda/CoherentWitnessSpecialization.agda` uses `compose`, `Composite.rebase`, `Associativity.associator`, and `Units` from `ComposableWitnessSpecialization`, not the older presentation-only pentagon.

`Tail.rebase-next` extends the canonical rebase through a further proof-dependent refinement. `rebase-compose` checks its compatibility with binary composition. `Pentagon.P0` through `P4` are the five actual four-operand compositions, all in `Refinement L`. Three edges use the existing associator directly; two are whiskerings whose restrictions are proved equal to the existing associator's state and witness maps. `state-pentagon`, `step-pentagon`, and `source-pentagon` equate both routes as functions, including all step witnesses and retained source records. `generated-pentagon` checks the selected generated step.

`Triangle` inserts the actual identity refinement between two operands. Its short route is a whiskered right unitor; its long route is the existing associator followed by a whiskered left unitor. Explicit full-step restriction equations identify both whiskerings with `Units` rather than unrelated deletion maps. The triangle commutes on states, full steps, source records and generated steps.

The Boolean fixture adds a fourth proof-dependent layer to the existing nonidentity example. Admissions change at each step; the final layer reads the earlier proof payload. The fixture tests both diagrams and the changed output.

Fresh checks through `check_cubical_agda.ps1 -Module CoherentWitnessSpecialization -Fresh` pass with the pre-existing imported warning. Receipt and log: `results/agda-CoherentWitnessSpecialization.json` and `.log`. The SCC receipt checker also requires the base composition and displayed-history bridge receipts to match the current source inventories.

Scope: coherence of the canonical indexed compose/rebase/unit actions on states, full steps and sources. This does not supply a general category/bicategory of arbitrary WG comparison cells, naturality under arbitrary equivalences, or a uniqueness theorem for all possible coherence structures. The graph/category distinction and conditional library bridge are developed in `displayed-witness-specialization.md`.
