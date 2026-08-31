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

## Start here

From the repository root, first inspect the installation and the live model
registry:

```text
python research/aspect/scc/scc.py doctor
python research/aspect/scc/scc.py models
python research/aspect/scc/scc.py dashboard --markdown
```

To add a model without editing Aspect's registry:

```text
python research/aspect/scc/scc.py init marici.YourName your-model-id
python research/aspect/scc/scc.py validate all
python research/aspect/scc/scc.py check your-model-id
python research/aspect/scc/scc.py explain your-model-id
```

`init` creates an owner-local manifest under
`research/<owner>/scc-models/`. Replace its unresolved fields, point it at
authoritative inputs and deterministic checkers, then validate before relying
on any result. Use `freeze` before a prospective hostile and `challenge`
afterward so the interpretation cannot be changed after observing the outcome.

## Capability map

| Question | SCC surface | Primary implementation |
| --- | --- | --- |
| What models are watched, stale, blocked, or downstream? | `models`, `status`, `dashboard`, `impact`, `plan`, `watch` | `scc.py` |
| What constructor could remove a typed obstruction? | `constructors`, `transfers` | `constructor_synthesizer.py` |
| Do routes and higher cells cohere? | `categorical`, `inverse` | `categorical_compiler.py` |
| Can source equations determine a bridge formula? | `formulas` | `formula_synthesizer.py` |
| Does a family of observers become jointly faithful? | `observer-set` | `observer_set_compiler.py` |
| Do observers of observers form a valid higher tower? | `globular-tower` | `globular_tower_compiler.py` |
| Do interaction-net reductions terminate, join, and preserve observables? | `net-algebra`, `universal-core` | `interaction_net_algebra.py`, `universal_net_certifier.py` |
| Does an analytic or RH realization carry the required rigging/state data? | `beurling-rigging`, `projective-rigging`, `rh-state` | the corresponding `*_compiler.py` modules |
| Is a physical apparatus claim source-authorized and uncertainty-complete? | watched-model apparatus certificate | `model-manifest.schema.json` |

Canonical contributor inputs are owner-local manifests and contracts. Generated
results belong under the owner's `results/` directory; preregistrations belong
under `scc-freezes/`. The reusable schemas and templates are
`model-manifest.schema.json`, `model-manifest.template.json`, and
`contract.v1.json`. Fast coordinator regression coverage is in
`test_scc.py`.

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
python research/aspect/scc/scc.py constructors <model-id>
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
python research/aspect/scc/scc.py categorical research/owner/contracts/diagram.json
python research/aspect/scc/scc.py formulas research/owner/contracts/formula-system.json
python research/aspect/scc/scc.py observer-set research/owner/contracts/observer-set.json
python research/aspect/scc/scc.py globular-tower research/owner/contracts/globular-tower.json
python research/aspect/scc/scc.py beurling-rigging research/owner/contracts/beurling-rigging.json
python research/aspect/scc/scc.py projective-rigging research/owner/contracts/projective-rigging.json
python research/aspect/scc/scc.py net-algebra research/owner/contracts/interaction-net-algebra.json
python research/aspect/scc/scc.py universal-core research/owner/contracts/universal-interaction-net-core.json
python research/aspect/scc/scc.py rh-state research/owner/contracts/rh-interaction-net-state.json
python research/aspect/scc/scc.py inverse research/owner/contracts/diagram.json <claim-id>
python research/aspect/scc/scc.py status all
python research/aspect/scc/scc.py watch
```

The registry is `registry.v1.json`. A registered checker must be deterministic, bounded, return zero only when its own declared checks pass, and write a machine-readable result packet.

Contributors declare watched models in their own `research/<owner>/scc-models/*.json` manifests. SCC discovers these automatically; nobody edits Aspect's central registry. Use `init` or copy `model-manifest.template.json`, declare workspace-relative inputs and inline checkers, then run `validate` and `check`. The bundled JSON Schema supplies editor completion and field validation.

SCC fingerprints authoritative inputs, the manifest, and checker sources. Per-model runtime checkpoints live under `.ai/tmp/scc-state`, avoiding one shared multi-agent state file. A changed or missing input makes the model stale or unavailable before any scientific conclusion is reused.

`watch` is one bounded reconciliation sweep, not a resident temporal process. It rechecks models whose fingerprints are stale or absent. An external scheduler may invoke the sweep repeatedly.

Normal runs capture checker output and print a concise structured summary. Add `--verbose` to include bounded stdout and stderr. `explain` reports the scientific classification and stratum separately from checker health.

`import` finds a checker and nearby result packets, then emits a draft manifest without writing by default. `--write` creates the draft in the contributor's own locus and never overwrites an existing manifest. Classification, stratum, capabilities, and the next falsifier remain explicitly unresolved for owner review.

`constructors` performs bounded backward synthesis from explicit obstruction vocabulary. It emits ranked candidate constructors, a discriminating hostile for each, and the forbidden observer-side substitute. Its output is always a candidate menu, never a truth certificate; vocabulary-free failures produce no guess.

Manifests may declare `depends_on`, `consumes`, `provides`, `missing_constructors`, and `next_falsifier`. `impact` computes the downstream recheck order. `transfers` proposes only multi-token or exact capability matches. Rechecks normalize JSON checker results into a common scientific envelope and report changes from the previous checkpoint as `scientific_delta`.

`freeze` writes a content-addressed preregistration into the model owner's `scc-freezes` directory and never overwrites it. `challenge` requires a freeze matching the current fingerprint and an explicit declaration of whether exit zero means `survives` or `falsifies`; this prevents SCC from guessing hostile semantics after seeing the result. `dashboard` keeps scientific classification, checker health, blockers, downstream impact, and freeze state in separate fields.

`doctor` reports the exact interpreter, platform, missing paths, manifest errors, and declared dependency versions. `capsule` emits a reproducibility fingerprint containing the model fingerprint and each checker hash. `dashboard --markdown` is suitable for human workboards. `graph-packet` emits a dry-run, dependency-closed proposal shape with no publication authority; an owner must review and submit it through the governed graph surface.

Discovery rejects owner/locus mismatches, unknown dependencies, and dependency cycles. `plan` computes topological execution layers: models within one layer may run in parallel, while downstream layers wait for their declared dependencies. Fast coordinator tests live in `test_scc.py`.

## Categorical diagram compiler

`categorical` compiles a finite typed diagram into executable route residuals,
realization-fiber comparisons, typed obstruction cones, generated deletion and
profile-collapse hostiles, proof-carrying promotions, higher-coherence states,
and structure-preserving cross-sector functors. SCC profiles are instrument-capability
profiles in the 405-element SCC Instrument Profile Lattice; they are not source
types or instrument identities. Equal SCC instrument profiles never imply
realization equivalence. Higher cells are explicitly verified, falsified, or
unsupported; unsupported cells are never promoted.

`inverse` starts from a declared claim, returns its missing witnesses, and ranks
preregistered experiments by how many missing branches they separate. The
compiler assigns no causal or temporal semantics to arrows and certifies only
the finite diagram supplied by its owner.

`formulas` solves declared affine bridge systems over exact rational numbers.
It emits formulas only when the source equations have sufficient rank, marks
assumption-relative formulas as non-source-derived, reports free unknowns, and
rejects observer-fitted systems. Deleting an equation must expose the affected
output as underdetermined. An empty source fiber produces no invented formula.

`observer-set` treats a graded or grouped observer family as one SCC object.
Members declare arity domains, exact matrices, transported realizations,
polarization fixtures, joint-faithfulness scope, A7 realization comparisons,
and higher-coherence states. The compiler induces one- and two-copy transport,
tests complete family laws, and never promotes unsupported higher cells.

`globular-tower` compiles recursively boxed observers of observers. Every
higher cell must have constructed parallel lower boundaries. The ordered gates
cover exact source-incidence rank monotonicity, distinct kernel, cokernel,
topological, and authority residuals, typed child seeds, source-authorized
promotion, termination, strictness, supported finite defect, acyclicity, local
critical-pair joins, and global coherence across completion, authority,
coefficient, and parent-child lenses. Filling schema slots does not substitute
for these runtime witnesses. Source-authorized precomposition may form a stacked
Level-0 family such as `J`, `J A`, and `J A^2`; its joint rank is computed
separately from higher-observer postcomposition, which remains rank-monotone.

## Contextual irreducibility gate

A model may freeze a `lower_theory` containing composition, tensoring,
authorized ancillas, discard, conditioning, tester identities, and explicit
completeness statuses for its context and hostile languages. Checker output may
then supply `contextual_irreducibility`. An irreducible result requires
lower-equivalent inputs with unequal records after the candidate interaction.
Reducibility requires a descent certificate. Ancillas must be authorized,
hostile-independent, and uniformly available. An inconclusive result is refused
when both frozen languages are declared complete.

## Physical apparatus certificates

A manifest may attach an `apparatus_certificate` for a separately
source-authorized physical instrument. SCC validates the supplied authority,
state types, one-use joint map, labelled composition law, reset, repeated-use
law, uncertainty bounds, quotient descent, calibration, domain, and support
assumptions. It never synthesizes an apparatus or treats a passing packet as
evidence that the apparatus exists.

Repeated-use packets must declare `fresh` or `shared` coupling semantics,
including joint signatures, covariance, and two-use variance. This distinguishes
WP970's fresh variance `1/2` from shared variance `1` even when their
one-use marginals agree. Triple composition and mixed coherence must close;
preparation-label side channels and observer-fitted couplings or covariance are
rejected. Validation returns `pass`, `fail`, or `inconclusive` with the
first failed gate. Candidate construction remains `candidate_requires_source_derivation`.

The certificate keeps three claims independent: observational rank, natural
transport between presentations, and accessibility through the stated physical
port. Equal observations define only an observer kernel pair, not source-state
identity. Equal chartwise ranks do not replace a closed naturality square. A
fixed-radius port claim additionally needs a uniform depth/range bound and a
non-correctable backward-support witness; otherwise the certificate must declare
growing support or decline the bounded-port claim.

An optional `conjugate_readout_certificate` describes the optical analogue of
a carrier readout and its generator-weighted mate on the same preparation. It
requires a source-authorized joint rank-two response. Its admitted conclusion
is deliberately exact: `transversality_only`. It cannot claim to locate the
zero or parameter whose transverse crossing it detects.

The conjugate packet also preregisters a controlled-successor experiment. A
source-derived joint first jet and uncertainty threshold must exist before the
response is observed. The hostile set includes independent detector channels
and common-mode drift. A reported pass is invalid unless both nulls are rejected;
an observer-fitted response law is rejected at the calibration gate.

The watched optical candidate freezes its decision rule in
`contracts/optical-conjugate-uncertainty-threshold.v1.json`. It whitens the
complete three-residual packet using independent calibration covariance and
uses a fixed maximum absolute score cutoff of `5.0`. Candidate survival also
requires both preregistered null models to exceed that cutoff. Calibration
failure, missing packets, or a surviving null produces `inconclusive`.