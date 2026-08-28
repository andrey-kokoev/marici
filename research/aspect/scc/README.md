# SCC — Stratified Coherence Compiler

SCC is the canonical name of the instrument formerly called Aspect's germ tester.

It compiles a proposed explanation into typed obligations and executable hostiles. Its output is not a truth certificate. It reports which claims are admitted on which stratum, which residuals remain, and which constructor or capability is missing.

The compilation order is:

1. **Packet** — freeze the claim, source maps, coefficients, and evidence locators.
2. **Stratum** — verify that compared fibers have constant relevant type and rank.
3. **Ports** — type preparations, adapters, observers, quotients, and capabilities.
4. **Static coherence** — test contravariant restriction, descent, and cocycles.
5. **Dynamic coherence** — test covariant connection, transport, and mixed cells without introducing a preferred time parameter.
6. **Hostiles** — search for the smallest typed counterexample that preserves the declared lower gates.
7. **Admission** — emit bounded scope, residuals, and the next constructor.

The historical germ tester is SCC's local-packet and hostile-testing core. Existing research records retain that name; new work should use SCC.

The namespace is `marici.scc`. This avoids confusing SCC with the standard graph-theoretic abbreviation for strongly connected component.

## Usage

```text
python research/aspect/scc/scc.py init marici.YourName your-model-id
python research/aspect/scc/scc.py import research/yourname/checkers/your_checker.py
python research/aspect/scc/scc.py import research/yourname/checkers/your_checker.py --write
python research/aspect/scc/scc.py models
python research/aspect/scc/scc.py run <check-id>
python research/aspect/scc/scc.py run core
python research/aspect/scc/scc.py validate all
python research/aspect/scc/scc.py check <model-id>
python research/aspect/scc/scc.py explain <model-id>
python research/aspect/scc/scc.py impact <model-id>
python research/aspect/scc/scc.py transfers <model-id>
python research/aspect/scc/scc.py freeze <model-id>
python research/aspect/scc/scc.py challenge <model-id> research/owner/checkers/hostile.py survives
python research/aspect/scc/scc.py dashboard
python research/aspect/scc/scc.py dashboard --markdown
python research/aspect/scc/scc.py doctor
python research/aspect/scc/scc.py plan
python research/aspect/scc/scc.py capsule <model-id>
python research/aspect/scc/scc.py graph-packet <model-id>
python research/aspect/scc/scc.py status all
python research/aspect/scc/scc.py watch
```

The registry is `registry.v1.json`. A registered checker must be deterministic, bounded, return zero only when its own declared checks pass, and write a machine-readable result packet.

Contributors declare watched models in their own `research/<owner>/scc-models/*.json` manifests. SCC discovers these automatically; nobody edits Aspect's central registry. Use `init` or copy `model-manifest.template.json`, declare workspace-relative inputs and inline checkers, then run `validate` and `check`. The bundled JSON Schema supplies editor completion and field validation.

SCC fingerprints authoritative inputs, the manifest, and checker sources. Per-model runtime checkpoints live under `.ai/tmp/scc-state`, avoiding one shared multi-agent state file. A changed or missing input makes the model stale or unavailable before any scientific conclusion is reused.

`watch` is one bounded reconciliation sweep, not a resident temporal process. It rechecks models whose fingerprints are stale or absent. An external scheduler may invoke the sweep repeatedly.

Normal runs capture checker output and print a concise structured summary. Add `--verbose` to include bounded stdout and stderr. `explain` reports the scientific classification and stratum separately from checker health.

`import` finds a checker and nearby result packets, then emits a draft manifest without writing by default. `--write` creates the draft in the contributor's own locus and never overwrites an existing manifest. Classification, stratum, capabilities, and the next falsifier remain explicitly unresolved for owner review.

Manifests may declare `depends_on`, `consumes`, `provides`, `missing_constructors`, and `next_falsifier`. `impact` computes the downstream recheck order. `transfers` proposes only multi-token or exact capability matches. Rechecks normalize JSON checker results into a common scientific envelope and report changes from the previous checkpoint as `scientific_delta`.

`freeze` writes a content-addressed preregistration into the model owner's `scc-freezes` directory and never overwrites it. `challenge` requires a freeze matching the current fingerprint and an explicit declaration of whether exit zero means `survives` or `falsifies`; this prevents SCC from guessing hostile semantics after seeing the result. `dashboard` keeps scientific classification, checker health, blockers, downstream impact, and freeze state in separate fields.

`doctor` reports the exact interpreter, platform, missing paths, manifest errors, and declared dependency versions. `capsule` emits a reproducibility fingerprint containing the model fingerprint and each checker hash. `dashboard --markdown` is suitable for human workboards. `graph-packet` emits a dry-run, dependency-closed proposal shape with no publication authority; an owner must review and submit it through the governed graph surface.

Discovery rejects owner/locus mismatches, unknown dependencies, and dependency cycles. `plan` computes topological execution layers: models within one layer may run in parallel, while downstream layers wait for their declared dependencies. Fast coordinator tests live in `test_scc.py`.
