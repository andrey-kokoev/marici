# Rzk ergonomics and latency audit

## Question

Why is the current Rzk loop slow, and which changes can reduce latency without weakening pinned-source verification?

## Observed path

`research/nima/rzk/check-factn.ps1` creates a fresh temporary tree, downloads the same pinned sHoTT archive, verifies its digest, extracts it, copies every local Rzk module, edits `rzk.yaml`, and typechecks the complete staged project on every invocation. Process-launch code is duplicated in `diagnose-rzk.ps1`. This makes network, extraction, staging, and full-project checking part of every edit cycle.

## Bounded improvements

1. Cache the digest-verified sHoTT extraction in an ignored content-addressed directory keyed by commit and archive SHA-256. Reuse only after checking a completion manifest and source digest.
2. Separate `prepare` from `check`: preparation materializes the pinned dependency once; checking creates only a small disposable overlay or copied local source subtree.
3. Add a fast changed-module lane after verifying whether Rzk 0.11.3 exposes a sound file/module selector. Do not assume incremental checking without CLI evidence. Retain the full-suite lane as the closeout authority.
4. Generate one local aggregate module with dependency order, so diagnostics identify the first failing Marici module rather than forcing manual isolation.
5. Record per-phase durations—dependency validation, staging, parsing/typechecking—and source digests in a result JSON. Optimize the measured dominant phase.
6. Consolidate executable discovery and version checking into one helper used by diagnostics and verification.
7. Keep a warm editor/LSP process for interactive feedback if supported, while retaining fresh headless verification for durable claims.

## Acceptance tests

- Cached and cold runs check identical source digests and produce equivalent pass/fail results.
- Cache corruption forces reconstruction.
- Fast-lane success is never reported as full-suite verification.
- A deliberate error in each module is localized to that module.
- Median warm-loop latency is reported against the current cold baseline.

## Measured implementation

`check-factn.ps1` now uses a digest-keyed prepared sHoTT cache, serializes cache mutation, refreshes only local modules, bounds diagnostics, and reports phase timings. A cold verification passed with `prepare_ms=1492`, `stage_ms=30`, and `typecheck_ms=29977`; a warm verification passed with `prepare_ms=27`, `stage_ms=39`, and `typecheck_ms=37926`. The preparation optimization is real, but typechecking dominates and varied upward in the warm sample.

A one-module prefix still took `37825 ms`, showing that Rzk 0.11.3 checks the included sHoTT libraries rather than obtaining useful locality from fewer Marici files. A positional file-selector probe returned in 12 ms without a usable exit-status witness and is therefore not admitted as verification.

## Disposition

Content-addressed dependency caching and prepare/check separation are implemented and verified. The remaining latency is the full included-library typecheck. Further speedup requires either a verified incremental/LSP path or a source-derived minimal sHoTT include closure; neither may replace the full-suite closeout check until equivalence is tested.
