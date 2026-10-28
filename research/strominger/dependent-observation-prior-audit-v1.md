# Dependent-observation conjecture: contract and prior-construction audit

## Finding

A substantial part of the proposed construction already exists. `research/nima/agda/SeedGeometricResponseState.agda` defines the source-derived based-path state, reversible edge equivalences, seam distinctions and retained native execution. The original recommendation should have consulted this work before treating existence of dependent transport as a fresh open problem.

Fresh verification:

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedGeometricResponseState -Fresh

Exit 0. Inherited warning: TypedGeneratorLayers imports the unexported isPropIsContr. No existing proof source was edited.

## Frozen candidate

See `contracts/dependent-observation-realization.v1.json`.

Use the existing free six-edge realization X, choose base A explicitly, and take O(x)=(node A = x). At vertices this is definitionally the existing State(v). Edge action is path concatenation; inverse transport recovers the preceding state. No independently chosen edge-action matrix is supplied.

The declared observable distinctions are the existing two seam tests: AB versus AD;DB, and AB;BA versus AB;BC;CA. Literal words remain separate retained provenance and are not claimed recoverable from the geometric state alone. This is not just an appended history log: the current path state itself distinguishes the seam alternatives, as the existing proofs show.

The family is source-generated relative to the explicitly chosen free realization and base. Neither choice is claimed uniquely forced by the original source.

## Why the discrete-reader obstruction does not apply

No global Vertex-valued retraction is constructed. The endpoint is the index of a fiber. In particular, a map sending (x,p) in Sigma x:X, O(x) to x is X-valued, not a decoder to the original discrete Vertex type. External constructor labels are not promoted to a global section of a discrete reader.

A further subtlety: the total based-path space Sigma x:X, (node A = x) is contractible. That does not make every fixed fiber contractible or its loop transport trivial. The proposed observations are fiberwise, so total-space contractibility is not a license to discard the base/fiber interface.

## Scope distinction that must survive

The existing module supplies native pointed fillers using BoundaryGeneratedQuestions. Its arbitrary-word retained execution uses RetainedTransportResolution.Extension, explicitly an extension, not a derivation in the unchanged original Resolve calculus. A conjecture requiring execution under only the original rules is not closed by this evidence.

`SeedGeometricResponseInterpretation` already provides a general dependent-family interpretation from supplied edge equivalences and proves route/native response squares. That generic theorem alone does not select its equivalences. The based-path candidate avoids that free choice, but its global-family transport still needs an explicit binding to the already constructed edge actions.

## Remaining work

Do not rebuild based-path state, seam separators or retained execution. Assemble the global family interface, prove its transport/concatenation binding and nontrivial based-loop action, then report the exact native execution scope. This is the narrowed next proof task; the conjecture remains open at that assembled scope.
