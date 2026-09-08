# DG pyramid aggregate check — iteration 6

`agda/DGPyramidArchitecture.agda` publicly imports the boundary, filler, negative controls, adapter, and nonphysical fixture as one checked surface.

The adapter was strengthened: every source, generic, and supported comparison record now has a required action on its declared concrete object. Rich map records may still retain roofs and homotopies, while a bare uninterpreted token no longer counts as a comparison map. The fixture was updated with these actions.

Fresh mutable input `research/chatgpt/relative_morse_fibre_comparison_proof.md` was reviewed. It supplies explicit endpoint-derived relative maps and two labelled endpoint coefficient lines, but explicitly does not construct the physical Q/support comparison and proves the scalar unit-Q normalization incompatible with its source equation. It is therefore partial future adapter input, not a `DGPyramidAdapter` inhabitant. The aggregate module records this scope and does not import it as physical evidence.

A fresh check deleted the aggregate/adapter/fixture interfaces before rebuilding. Agda 2.8.0.1/Cubical 0.9 accepted all three under `--safe --cubical --guardedness`, exit0 without warnings, holes, or postulates.

```
pwsh -NoProfile -Command "Remove-Item -ErrorAction SilentlyContinue research/voevodsky/agda/DGPyramidArchitecture.agdai,research/voevodsky/agda/DGPyramidAdapter.agdai,research/voevodsky/agda/DGPyramidFixture.agdai; & 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/DGPyramidArchitecture.agda"
```

Remaining nonredundant work: add compile-fail degree/sign regression modules and verify they fail for the intended type reason; then perform final requirements audit. No Git operations or analytic changes.
