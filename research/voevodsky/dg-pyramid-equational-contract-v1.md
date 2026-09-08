# DG pyramid equational contract — iteration 9

The public mathematical interface now has checked definitional equalities.

- `namedDiscrepancyEquation` proves `pyramidDiscrepancy P` is literally the bounded Hom expression `H_C - e ∘ h_M` using the exported mathematical accessors.
- `namedPyramidDiscrepancyClosed` states directly that its Hom differential is zero and is discharged by the internally derived closure theorem.
- `admissibleFillerShape` proves `AdmissibleFiller P Frame` definitionally expands to the requested Sigma fibre over `Hom⁰JF`, followed by the boundary equation and `PreservesFrame`.

No new assumptions were added. In particular, closure remains derived rather than a boundary-record field, and the filler remains outside `DGPyramidBoundary`.

Fresh mutable state was checked; `relative_morse_fibre_comparison_proof.md` remains newest and still does not instantiate physical Q/support fields.

A clean positive build removed six relevant interfaces and rebuilt `DGPyramidArchitecture.agda`. Agda 2.8.0.1/Cubical 0.9 returned exit0 with no warnings. The two expected-failure controls were rerun: degree mismatch and even-Leibniz-sign mismatch each returned exit42 and contained the asserted projection mismatch. No holes, postulates, Git operations, or analytic changes.

Iteration 10 should produce the final requirement-to-symbol matrix, perform one last clean aggregate/negative check, and stop unless fresh physical data creates a new executable instantiation task.
