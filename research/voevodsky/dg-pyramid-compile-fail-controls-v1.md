# DG pyramid compile-fail controls — iteration 7

Two intentionally rejected modules now guard the degree and sign conventions.

- `agda/negative/BadDGPyramidDegree.agda` attempts to use `hM : JQminus1` where `JQzero` is required. Agda rejects it with `MismatchedProjectionsError`: `JQminus1` and `JQzero` do not match.
- `agda/negative/BadDGPyramidLeibnizSign.agda` replaces the positive `e ∘ δ(hM)` term required by even degree `e = 2` with its negative. Agda rejects the claimed use of `compositionBoundary`, reporting the mismatch between `compose20` and `negJFtwo`.

A harness ran each module with the negative directory on the include path, required nonzero exit, and checked an error-specific substring. Both exited 42 for the intended type reason. The first preliminary invocation omitted the negative include root and only detected a module-path mismatch; a second preliminary run exposed a missing Prelude import in the degree control. Those harness/setup defects were repaired before the successful expected-failure run.

These modules are intentionally excluded from `DGPyramidArchitecture.agda`; importing them would make the positive aggregate fail. They contain no holes or postulates.

Fresh mutable state was checked. The newest offline result remains `relative_morse_fibre_comparison_proof.md`; no later physical Q/support comparison is available.

Remaining nonredundant work: audit exact requested names/shape, especially J/Q/F naming and the fibre presentation, then add any compatibility aliases without changing proved content. No Git operations or analytic changes.
