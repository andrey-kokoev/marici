# Pi/Rzk persistent LSP integration

## Question

Can Pi retain an Rzk language-server process and obtain useful incremental
diagnostics without replacing fresh headless closure verification?

## Interface

The project extension is `.pi/extensions/rzk-lsp.ts`. Reload Pi after changing
it. It exposes:

- `rzk_lsp_diagnostics`, an agent tool accepting a repository-relative `path`;
- `/rzk-lsp-check <path>`, a direct interactive check;
- `/rzk-lsp-status` and `/rzk-lsp-restart`.

The extension discovers the newest staged pinned-sHoTT project under
`research/grothendieck/rzk/.check-tmp-*`. Set `MARICI_RZK_PROJECT_ROOT` to
override discovery. Run `typecheck-target-closure.ps1` first to refresh
`src/marici-target`. The staged project is disposable and remains distinct from
the authoritative Rzk sources.

The LSP writes each requested live document to its staged shadow before sending
`didOpen` or `didChange`. Repeated checks of unchanged text return the last
published diagnostic set because Rzk does not republish diagnostics for an
unchanged `didChange`.

## Verification

Run:

```powershell
node research/grothendieck/rzk/checkers/pi-rzk-lsp-smoke.mjs
```

The smoke checker launches a separate Pi RPC process, loads the extension,
checks the repaired translated-cancellation file twice, and checks
`fixtures/lsp-deliberate-failure.rzk.md`. The deliberate failure must report
`MissingRzkType`; both valid checks must report no diagnostics.

Observed on Rzk 0.11.3 with the 27-core/119-Marici focused closure:

- cold valid check: 60,003 ms;
- unchanged warm check from the diagnostic cache: 3 ms;
- changed deliberate-failure check: 595 ms.

These are measurements of one run, not latency bounds. The persistent server
materially improves repeated feedback, while the cold load remains expensive.

## Claim boundary and disposition

LSP diagnostics provide rapid local feedback. They do not certify a dependency
closure, process freshness, or reproducibility. The pinned headless closure
checker remains the verification authority. The integration is retained as a
feedback layer because the smoke test detected both absence and presence of
expected diagnostics and demonstrated persistent reuse.
