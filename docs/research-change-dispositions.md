# Research-change disposition queue

This is **website editorial accountability, not a scientific verdict or source-owner transition**. A citation's absence is a review signal, not proof of semantic absence, invalidity or an obligation to create a page for every file.

## Reviewed checkpoint

`config/research-change-dispositions.v1.json` inventories **all 160 added/changed research Markdown paths** in the eighteen thematic commits after `518280545d386097ed9bc71588cd084c444fd3dc` through `3ace86e3340491c07fdf1c186d99d9ce77140d6b`. Every row records its source path/title, thematic commit identity, reviewed revision, source hash, review group, disposition and rationale. Public coverage names its guide/result route; historical records name their successor; duplicates name the exact matching source.

| Disposition | Files | Meaning |
|---|---:|---|
| Public coverage | 11 | Selected bounded result, programme or explanatory context; not complete semantic exhaustion or independent scientific verification. P/E coverage is its **held-status explanation**, not net release. |
| Historical/superseded | 26 | Owner-labelled WG snapshots 1–26; revision 27 is the current handoff. Earlier frontiers/verdicts remain historical, not false or reopened. |
| Development-only | 7 | RDF/SHACL prototype documentation. Source-reported tests/replay are not rerun here; no public native-spatial engine is selected. |
| Duplicate | 6 | Exact LF-normalized source-byte identity with the named canonical imported note, not independent corroboration. A `(1)` filename alone is insufficient: the nonmatching open-continuation note remains pending. |
| Pending source review | 110 | Explicitly unselected additional claims needing source/scope/environment review. They are neither scientifically rejected nor assumed absent from indirect public coverage. |

The fifteen review groups separate reference data, RDF, WG historical/current, held P/E, Ramsey assembly, Pauli, heptagon, extension repair, selected programme notes, reflected-simplex stages, matrix/Golay proposals, port/incidence reductions, native/neutron notes and remaining finite audits. Group responsibility is the website editorial queue; scientific decisions remain with their owning surfaces. Several of the eighteen commits have **zero** research Markdown paths (their code, application docs or other artifacts are outside this particular inventory).

### Inventory evidence and limits

The executed thematic commit journal and NUL path manifests were preserved under `.ai/thematic-commit-plan/`. Their eighteen commit identities/endpoints were cross-checked through Site-local Git; per-manifest byte hashes and counts are retained in the versioned queue. The earlier currency audit independently reported the **same count**, not an independent per-path comparison by this iteration. The inventory is reconstructed from those execution manifests; no new complete Git diff replay is claimed. Normal checks need neither these ignored journals nor historical scientific receipts.

`config/research-currency-baseline.v1.json` is a **machine index**, not a claim-review packet: it observes 15,260 regular research Markdown files, including legacy sources outside the audited 160. This larger index only detects later source changes. It does not disposition or certify every legacy claim. The frozen canonical baseline SHA-256 is `3b4d1abae2900b378c5a0476b39c00a1c2d020d730553495a6a7f4dc86787b15`. Inventory identities and thematic evidence have separate frozen digests in `scripts/research-currency.mjs`.

Hashes preserve source bytes after CRLF/CR → LF normalization, including BOM and legacy non-UTF-8 bytes. Do not decode malformed bytes with replacement: distinct legacy bytes must not collapse to the same hash. Initial local validation exposed twelve such legacy files outside the 160-file set; only their new, unreleased index identities were explicitly corrected before final validation. No research file or scientific provenance snapshot was changed.

## Subsequent editorial review — revision 2

The 2026-11-25 review accounts for 138 later research Markdown changes: **53 development-only** protocol/inventory records and **85 pending-source-review** claims, arguments and context notes. No additional public-coverage routes were selected. These counts describe the subsequent rows, not replacements for the original 160-file audit above.

Each subsequent row binds its observed bytes and change kind to checkout context `97bf26a21c7dae891e8ea9acfbd0c14bb071cbda`. The review includes dirty working-tree content; that revision is not a claim that all reviewed bytes are committed. Pending review does not assert invalidity or absence of indirect coverage. The frozen baseline, initial inventory, thematic evidence, scientific verdicts and owner sources are unchanged. Further source edits still invalidate their matching review rows.

## Detect changes without automatic promotion

After source preparation, run:

```sh
node scripts/research-currency.mjs
node scripts/research-currency.mjs --observe
node --test tests/public-research-currency.test.mjs
```

The first command fails for an undispositioned addition, edit or deletion. `--observe` writes the full diagnostic to ignored `.ai/research-currency-observation.json` and reports changes without assigning coverage or a scientific verdict. Both normal source and built publication gates invoke this check, so preparation/build also fails on unreviewed source changes. The coverage contract explicitly selects the queue. An isolated real-filesystem fixture first passes both gates, then adds a synthetic research note and confirms that both reject it without altering selections, verdicts or owner files.

The scanner compares current content, so research Markdown changes introduced by **later commits or dirty worktrees** cannot evade it just by retaining the same selected citation list. It does not poll Git HEAD, audit every intermediate/reverted commit, or cover non-Markdown research changes. Obtain current Git context through the owning Site-local Git surface; do not infer commit containment from an observed worktree hash.

The scope is regular `research/**/*.md`, excluding the explicitly declared generated/runtime/dependency directories and scratch prefixes in `source_scope`. Symlinks are refused, not followed outside that scope. Read/permission errors fail rather than silently omitting sources. This is not a scientific compiler, transitive dependency checker or exhaustive semantic citation analyzer.

## Record an accountable subsequent disposition

1. Obtain fresh Git context and run `--observe`; inspect the affected source and its claimed scope. A pending-source-review disposition is valid when scientific review is not complete.
2. Add or update **one** `subsequent_dispositions` row per changed path in the queue. Record `change` (`added`, `modified`, `deleted`), the observed `text_sha256` (`null` for deletion), a review group, full `reviewed_revision`, explicit disposition, rationale and `coverage` routes (possibly empty). For dirty bytes, explain the worktree context: the revision is the checkout context, not a claim the commit contains those bytes.
3. Public coverage requires a real guide/result route. Historical/superseded records need `superseded_by`; duplicates need `duplicate_of` with matching content. Neither field licenses owner-file changes or public promotion. New public claims also need the usual coverage, provenance and selection review.
4. Increase queue revision and record the review checkpoint. Rerun the check/tests. The latest subsequent row overrides that path's checkpoint disposition; changed-again, disappeared or reverted source states invalidate stale subsequent reviews.

**Never automatically refresh the baseline to make drift pass.** Its digest, the original 160 identities and the thematic evidence are frozen. A deliberate later baseline needs a reviewed successor design, not overwriting v1. The one-time `scripts/capture-research-currency.mjs` reconstructs ignored initial candidates only; it does not review them. Its digest-bound `--accept-reviewed-candidate SHA256` operation exclusively creates configs, refuses overwrite, requires explicit reviewed state and re-observes sources before adoption. The digest covers canonical JSON `{baseline, queue}`. Ordinary checks/builds never invoke capture, scientific suppliers, graph actions, commits or deployments.
