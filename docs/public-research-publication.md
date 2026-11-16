# Public research publication contract

This is a website-consistency workflow, not scientific acceptance or authority to apply a research transition. Source dispositions and empirical gates remain owned by their research packets. Closing the website gap audit does not close those gates.

## Authoritative inputs and projections

- `docs/landing-page.md`, `docs/theory-page.md`, `docs/results-page.md` and `docs/system-characteristics.md` own the four synthesis pages. `scripts/public-synthesis-content.mjs` shares their exact publication transformations with the freshness checker, including the extracted comparison-target page.
- `src/data/results-physics.json` owns generated result bodies/status labels. Required selected result coverage is explicitly declared in `config/public-research-coverage.v1.json`, not inferred from whichever records happen to survive a change.
- That coverage config also owns the as-of frontier's first missing objects, source/result links and acceptance/reopening conditions. `scripts/prepare-public-research-frontier.mjs` renders its ignored Markdown. Update the reviewed config, never the generated page.
- `config/current-research-provenance.v1.json` owns selected source/checker pins and historical receipt IDs. See the public provenance guide for hash bases, clock limitations, absent receipt/source compatibility replay and deliberate lack of transitive closure. A pin failure requires inspection/review; do not auto-recapture just to make CI green.
- `src/conjecture-nets/catalog.json` owns the five reviewed public contract paths. The coverage contract independently records that selection. The held selection remains in `development-catalog.json`; `--development` must stay under ignored `.ai/` output and is not a public release.

## Prepare and verify

With the repository dependencies and the existing publishers' declared inputs available:

```sh
node scripts/prepare-website.mjs --pages-only
pnpm publication:check
pnpm publication:test
pnpm exec vitepress build website
pnpm publication:check:built
```

`--pages-only` skips ledger regeneration, **not** publication assets: it refreshes the reference table, visual assets, public-net bundle, provenance metadata and frontier as well as synthesis/result pages. It does not authorize scientific supplier execution. The preparation command runs the source coverage gate after writing its projections. `pnpm build` additionally runs the built coverage gate before search indexing; neither command deploys the site.

The source gate reads the resolved VitePress nav/sidebar rather than guessing their final values from TypeScript text. It verifies destinations and real static IDs with the configured Markdown renderer, checks static links in non-ledger public Markdown, validates required pages/results and checks generated projections and the public-net bundle. Vue-bound content URLs are not misread as literal static hrefs. The built gate checks corresponding files/fragments in the rendered site and byte-identical public-net HTML/JSON copies. It does not fetch external links or certify computed Vue links, scientific source semantics, every historical ledger item or runtime behavior.

Regression controls cover absent required results, missing fragments, incomplete/duplicate acceptance rows, changed public-net selections, unknown net/node IDs, unsupported net tabs and false anchor matches. Provenance tests separately cover source drift, newline normalization, receipt-free publication, unsafe metadata and stale output. Do not weaken those controls to bypass an actual mismatch.

## Runtime checks remain separate

Static checks are not browser or scientific tests. When relevant pages/assets change, run:

```sh
pnpm publication:test:browser
node scripts/test-construction-workbench-publication.mjs
node scripts/test-isotope-reference-publication.mjs
node scripts/test-conjecture-nets-browser.mjs
node scripts/test-isotope-wiring-website.mjs
```

The frontier, workbench and reference-table scripts use the built publication; the public-net script uses the byte-checked public bundle, and the editor script is a VitePress development-host smoke test. These check documented interactions/fallbacks, not physical adequacy. The legacy editor's three expected TODO failures remain unresolved requirements; do not count them as repaired passes. Held development-net browser checks require their explicit development mode and are not part of the public default pass.

## Updating the frontier

Review the actual owning source before changing a row. Preserve the first missing authoritative object, distinguish a new evidence-bearing test from an unchanged blocked request, and retain separate mathematical, owner-integration and empirical gates. Do not reconstruct an already supplied packet merely because its owner transition is unapplied, invent a physical object from a desired cancellation, or use a finite software test as a native/physical theorem.

New source coverage, changed required routes or a public-net release requires an explicit contract review and regeneration, followed by both source and built checks. The as-of label describes the reviewed source synthesis, not live graph state or an independently verified execution date. No publication check creates task claims, changes dispositions, commits files or publishes a deployment.
