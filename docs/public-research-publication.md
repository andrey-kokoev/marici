# Public research publication contract

This is a website-consistency workflow, not scientific acceptance or authority to apply a research transition. Source dispositions and empirical gates remain owned by their research packets. Closing the website gap audit does not close those gates.

## Authoritative inputs and projections

- `docs/landing-page.md`, `docs/theory-page.md`, `docs/results-page.md` and `docs/system-characteristics.md` own the four synthesis pages. `scripts/public-synthesis-content.mjs` shares their exact publication transformations with the freshness checker, including the extracted comparison-target page.
- `src/data/results-physics.json` owns generated result bodies/status labels. Required selected result coverage is declared by the versioned config selected through `config/public-research-coverage.current.json`, not inferred from whichever records happen to survive a change.
- The selected coverage config owns the as-of frontier's first missing objects, source/result links and acceptance/reopening conditions. The current selector now chooses `config/public-research-coverage.v2.json`; v1 remains a hash-pinned historical checkpoint. `scripts/prepare-public-research-frontier.mjs` renders the ignored Markdown and public JSON snapshots/current pointer. Update the reviewed selected config, never generated copies; older snapshots retain their original wording and are not current obligations. Snapshot identity hashes use canonical UTF-8 JSON with two-space indentation and final LF, not the scientific receipt hashing policy.
- Frozen `config/current-research-provenance.v1.json` retains its ten-family selection and all valid original pins. Additive `config/current-research-provenance.v2.json`, bound to `config/research-provenance-selection.v2.json`, adds two result families and three authored explanations with immediate source/checker pins, historical receipt IDs and explicit missing/compatibility limits. `scripts/prepare-research-provenance-successor.mjs` validates both snapshots; builds never recapture metadata or run scientific suppliers. Its `--capture` writes an ignored candidate; inspect it before the digest-bound, exclusive `--accept-reviewed-candidate SHA256` operation. Further drift needs a reviewed successor, not overwriting v1 or calling metadata a replay. See the public provenance guide for hash bases and absent transitive/receipt-source compatibility guarantees.
- `config/research-change-dispositions.v1.json` accounts for all 160 research Markdown changes in the eighteen thematic commits: public context, archived editions, development-only docs, exact duplicates or explicit pending source review. The frozen machine observation index also detects later Markdown additions/edits/deletions outside that selection. See [queue scope and review procedure](research-change-dispositions.md); a green change-accountability check is not scientific review of all legacy sources. Both normal source and built gates enforce the queue selection and live source-content comparison. They also require all twelve selected provenance-backed results and the five reviewed normalized net IDs; completed assemblies remain completed annotations, not new open frontier rows.
- `src/conjecture-nets/catalog.json` owns the five reviewed public contract paths. The coverage contract independently records that selection. The held selection remains in `development-catalog.json`; `--development` must stay under ignored `.ai/` output and is not a public release.

- `config/typed-editor-publication.v1.json` explicitly holds `apps/isotope-wiring/` development-only. The public explanation is `website/experiments/typed-wiring-development.md`, not an application route. Source/built coverage invokes `scripts/check-typed-editor-publication.mjs` to reject a declared public app route, output under its protected app paths, silent iframe replacement or standalone bytes differing from `examples/isotope-wiring/index.html`. This bounded path/identity guard is not a classifier for arbitrarily renamed code or a typed-app/Morse acceptance check. Promotion requires a separately reviewed selection and publisher/runtime integration; an app commit or local `dist/` is insufficient.

## Prepare and verify

With the repository dependencies and the existing publishers' declared inputs available:

```sh
pnpm build
node scripts/research-currency.mjs
pnpm publication:check
pnpm publication:test
pnpm publication:check:built
```

Build before the complete publication test suite: recorded browser-byte evidence and the integrated source/built negative-control fixture require the actual production output, not an absent or old `dist/`. Do not run source-reading tests concurrently with regeneration. For a source-only preparation pass, `node scripts/prepare-website.mjs --pages-only` skips ledger regeneration, **not** publication assets: it refreshes the reference table, visual assets, public-net bundle, provenance metadata and frontier as well as synthesis/result pages. It does not authorize scientific supplier execution. The preparation command runs the source coverage gate after writing its projections. `pnpm build` additionally runs the built coverage gate before search indexing; neither command deploys the site.

The source gate reads the resolved VitePress nav/sidebar rather than guessing their final values from TypeScript text. It verifies destinations and real static IDs with the configured Markdown renderer, checks static links in non-ledger public Markdown, validates required pages/results and checks generated projections and the public-net bundle. Vue-bound content URLs are not misread as literal static hrefs. The built gate checks corresponding files/fragments in the rendered site and byte-identical public-net HTML/JSON copies. It does not fetch external links or certify computed Vue links, scientific source semantics, every historical ledger item or runtime behavior.

Regression controls cover absent required results, missing fragments, incomplete/duplicate acceptance rows, changed public-net selections, unknown net/node IDs, unsupported net tabs and false anchor matches. Provenance tests separately cover source drift, newline normalization, receipt-free publication, unsafe metadata and stale output. Do not weaken those controls to bypass an actual mismatch.

## Runtime checks remain separate

Static checks are not browser or scientific tests. When relevant pages/assets change, run:

```sh
pnpm publication:test:browser
node scripts/test-construction-workbench-publication.mjs
node scripts/test-isotope-reference-publication.mjs
node scripts/test-conjecture-nets-browser.mjs
node scripts/test-isotope-wiring-browsers.mjs
node scripts/check-isotope-wiring-browser-evidence.mjs
```

The frontier, workbench and reference-table scripts use the built publication; the public-net script uses the byte-checked public bundle, and the current editor matrix checks local direct-file behavior plus the actual production host/download. These target documented interactions/fallbacks, not physical adequacy. Held development-net browser checks require their explicit development mode and are not part of the public default pass.

## Verification checkpoint: 3ace86e33

The legacy core's fourteen-case suite passes with no TODOs: identity-delta replay, base-only metadata deletion and coordinate-ID uniqueness were repaired at their tested scope. This does not establish whole-definition persistence or immutable revision-engine integration. The separate combined software baseline at that checkpoint was **343/371 passing, with 28 failures and zero TODOs**, in `isotope-wiring-alternating-route`, `isotope-wiring-li6-line-colors` and `isotope-wiring-research` tests. Those were genuine failing tests, not the three repaired cases.

At currency correction iteration 2 the reviewed suite is **371/371 passing, with no skips or TODOs**. The [regression contract review](isotope-wiring-regression-contract.md) maps each former failure category to the already documented current contract and its replacement coverage. It also records the visible keyboard-target fallback fix. This preserves source-defined drawings and model controls; it does not restore SVG routing, EP rendering or canvas difference overlays that were explicitly removed. The separate typed application's routing checker is not evidence that its policy equals the retired legacy algorithm.

Reproduce the broader baseline with:

```sh
node --test tests/isotope-wiring-*.test.mjs tests/isotope-reference-fts.test.mjs tests/simplex-step-span.test.mjs tests/two-attractor-field.test.mjs
```

The historical 33-run Chromium/Firefox/WebKit report first appears in commit `c1025e302`; its exact source-under-test and engine versions were not recorded with that claim. It is not current browser acceptance.

**Current browser checkpoint, currency iteration 3:** the replacement ten-case matrix passed **30/30 runs** with zero failures/unrun cases on Chromium 151.0.7922.34, Firefox 153.0 and WebKit 26.5. Its base is `3ace86e33` with dirty working-tree changes; exact tested bytes and per-case versions are recorded in `config/isotope-wiring-browser-evidence.v1.json`, not inferred from that base commit. See [coverage, supersession and limits](isotope-wiring-browser-verification.md). This includes stored-record replay, fresh-context persistence and placement/survey data APIs, not the retired EP/placement-dialog UI or the separate typed application. Partial engine/case selections never count as a full matrix pass; the evidence checker checks recorded source-byte freshness and does not replay browsers. Real-device, screen-reader and live-deployment acceptance remain separate.

## Release authorization and acceptance

A passing local build is not a deployment. Keep an explicit source-file proposal and byte fingerprints; exclude `.agdai`, ignored evidence, generated website/public/dist assets and unrelated work. Review the actual staged diff after authorization rather than treating an unstaged proposal as an approved commit. Preserve the historical coverage/provenance configs and the held app/net selections.

The configured destination is Cloudflare Worker `marici` (`wrangler.jsonc`), serving `website/.vitepress/dist` at `https://marici.andrei-kokoev.workers.dev`. `pnpm ship` rebuilds and invokes `wrangler deploy`; it is a publication action, not a diagnostic command. Separate authorization is required for commit, pushing `origin/main` and deployment in this currency workflow; any staging must remain explicitly scoped. Read-only preflight requests do not grant that authority. Once authorized, use `pnpm exec wrangler deploy` only after confirming the already-tested build's byte manifest. Any rebuild invalidates that artifact record and requires renewed checks/fingerprinting before deployment; do not use the combined `pnpm ship` command to silently rebuild-and-deploy after artifact approval.

After an authorized release, check the live frontier/current pointer, both provenance manifests, selected source/result/status-guide routes, five actual net IDs and viewer routes/assets against the reviewed build. Run `node scripts/test-curated-viewers.mjs --live --output .ai/website-currency-release` for exact deployed viewer bytes and runtime cases. The verifier allows only the configured same-origin `index.html` → viewer-directory canonical redirect, requires a final 200 with matching bytes, and rejects redirected assets, other destinations and redirect chains. Old v1 metadata or an unchanged five-net JSON can match while new pages still return 404; neither alone proves currency. T08 and T14 remain open until deployed acceptance succeeds. Record unavailable scientific inputs and unrun supplier checks separately.

## Updating the frontier

Review the actual owning source before changing a row. Preserve the first missing authoritative object, distinguish a new evidence-bearing test from an unchanged blocked request, and retain separate mathematical, owner-integration and empirical gates. Do not reconstruct an already supplied packet merely because its owner transition is unapplied, invent a physical object from a desired cancellation, or use a finite software test as a native/physical theorem.

New source coverage, changed required routes or a public-net release requires an explicit contract review and regeneration, followed by both source and built checks. The as-of label describes the reviewed source synthesis, not live graph state or an independently verified execution date. No publication check creates task claims, changes dispositions, commits files or publishes a deployment.
