# Marici Agent Instructions

## Canonical team identities

Use these canonical identities and research responsibilities throughout this
repository:

- `marici.Nima`: common architecture and cosmology.
- `marici.Benincasa`: geometric/cohomological machinery and cross-sector
  localization.
- `marici.Figueiredo` (“Caroline”): flavor and
  presentation-versus-physics descent.
- `marici.Strominger`: radiative GR, BMS charges, soft limits, and memory.
- `marici.Grothendieck`: arithmetic geometry, emergence of
  `Spec(Z)`, primes as irreducible loci, Frobenius/Euler products and
  L-functions, and the audit that arithmetic is derived from—rather than
  inserted into—the shared Carrier calculus.

Use the canonical qualified identity—not a display-name alias—in task
handoffs, ledger attribution, research packets, and epistemic-graph
communication records. The prior `marici.Caroline` graph identity is retained
only as immutable history and is superseded by `marici.Figueiredo`.

Substantive team requests, handoffs, results, objections, replies, and
acknowledgments should be admitted to the Marici epistemic graph as
`marici:communication` entities. Communication records provenance and argumentative
causality; it becomes scientific evidence only through a separately reviewed
`promotes_to_evidence` relation.

The live graph schema requires extension kinds and relations to be namespaced.
Use `marici:communication` for new records. Unnamespaced `communication`
records remain queryable as immutable history; do not copy their obsolete
syntax into new submissions.

## Team communication is expected, not optional

The graph is the team's shared memory across sessions and context
compactions — if an idea stays in your chat, it is lost to everyone else.

- **At session start**, check both canonical `marici:communication` and legacy
  `communication` records, plus the neighborhood of your canonical
  team-member id. A handoff or objection may redirect your work. Acknowledge
  what you act on with `marici:replies_to`.
- **Keep up with the team's output.** Skim new ledger entries, packets,
  and graph claims from the other researchers as they land — at least at
  session start and before claiming overlap-prone work. Their checkers and
  results files are often directly reusable, and their residuals may be
  the constraint your problem is missing.
- **Tell the author what you think of their work.** Read it, then say so
  through the graph, addressed to them: a confirmation that their checker
  reproduces on your turf, a question about a step you could not follow,
  an `objection` with counter-evidence, a suggestion for the next test, a
  noticed connection between their result and yours. Silence is the
  failure mode — an unremarked result might as well not exist for the
  rest of the team. Use `marici:replies_to` their report/claim so the thread is
  traceable.
- **During work**, post early and informally when it helps: a question to
  the owner of an adjacent area, an intermediate result someone may be
  blocked on, a doubt about a conjecture you are about to spend hours
  testing, a pointer to a convention mismatch you found in a source.
  `notice` and `objection` intents exist for exactly this; communications
  are cheap and append-only.
- **At milestones**, report results with enough detail (packet paths,
  checker outcomes, residuals, event ids) that a teammate can build on
  them without re-deriving anything — and say what you did *not* verify.
- **When you disagree**, file an `objection` naming the claim and your
  counter-evidence rather than silently working around it. Criticism
  entities and `criticizes` relations are first-class graph citizens.
- One recipient per communication record; for broadcasts, send one record
  per recipient.

## Multiple agent sessions share this working tree

Nima, Benincasa, and others run concurrently against the same checkout.
Consequences:

- Expect a large dirty `git status` that is not yours. Touch only your own
  paths; never revert, renumber, or "fix" files owned by another session —
  report breakage (e.g. in your graph report) instead.
- `research/<owner>/` is that researcher's exclusive author workspace.
  Reusable cross-sector machinery belongs in `research/shared/` only after
  explicit agreement. Companion scripts, packets, and results remain under
  the current author's directory even when they import another researcher's
  checker.
- Before editing a possibly overlapping path, inspect Git status and file
  modification time, check current communications, and contact the owner.
  Inactivity or an old modification time never transfers ownership.
- Generated artifacts are owned by the generator and the agent running it;
  do not infer ownership merely from the directory containing an input.
- Ledger entry numbers and the ledger author schema are shared mutable
  state; see the ledger section below.
- Do not commit or push without explicit operator confirmation, and scope
  any approved commit strictly to your own paths. This repository rule
  governs even when a broader policy suggests a closeout commit: report the
  coherent uncommitted state and wait for confirmation.

## Epistemic graph: access mechanics that work

The graph is an MCP surface reached through mcp-loader. The loader process
restarts frequently, and each restart wipes surface handles and connection
ids — a previously opened handle fails with `surface_handle_not_found`.
The robust route is the atomic binding call, which resumes or reopens the
binding and makes the call in one step:

```
mcp_loader_call_binding_tool(
  site_root="C:/Users/andrey/src/marici",
  binding_id="marici-epistemic-graph",
  tool_name="<tool>",
  arguments={...})
```

Do not bother with `mcp_loader_open_surface` + `call_surface_tool` for
multi-call sessions here; use the binding-call route for every call.

- Read `epistemic_graph_guidance` first — it documents the entity kinds,
  relations, operation kinds, and the communication model. (There is no
  `epistemic_graph_doctor`.)
- Handoffs arrive as `marici:communication` entities addressed to you. Find
  yours by querying both canonical `marici:communication` and legacy
  `communication`, and by inspecting your team-member neighborhood
  (`epistemic_graph_neighborhood` plus the query tools listed in the
  guidance). Then acknowledge with a reply communication carrying
  `marici:replies_to` the handoff entity id.
- Team member graph ids (verify by query if a call rejects them):
  - `marici.Nima` — `team_member:aa2834674c8559a5dee0`
  - `marici.Benincasa` — `team_member:bc28f30924d7df1af02a`
  - `marici.Figueiredo` — `team_member:7f11641564913e4417ff`
  - `marici.Strominger` — `team_member:4561aedd7f948b5ddee5`
  - `marici.Grothendieck` — `team_member:7283d8c22c912c41664b`

## Epistemic graph: submitting records

Use `epistemic_graph_submit_review_admit` (submit + policy review +
admission in one call). Omit `expected_ledger_head` and `idempotency_key`
unless you have a specific concurrency boundary.

- Build an `operations` array of `entity.declare` and `relation.declare`
  ops. Reference entities declared in the same batch by their `local_ref`;
  reference pre-existing graph entities by their full id via `target_id`
  (e.g. `conjecture:088e8900f0d60d0898c8` is the shared-calculus
  conjecture).
- Always include `actor` (your canonical id) and an `authority_basis`
  (`operator_direct_instruction` with a summary naming the instruction or
  handoff you are executing).
- A communication entity requires `sender`, `recipient`, `body`, `intent`
  (`request|handoff|result|notice|objection|reply|acknowledgment`), and
  `sent_at` (fresh UTC ISO time). Add `marici:sent_by` /
  `marici:addressed_to` relations to the team_member ids above and
  `marici:replies_to` the message you answer.
- Use exactly one recipient per communication entity. The canonical packet is
  `sender`, `recipient`, `body`, `intent`, and `sent_at`; the canonical
  provenance edges are `marici:sent_by`, `marici:addressed_to`, and, for a
  response, `marici:replies_to`. Broadcasts are separate records, one per
  recipient.
- Admission returns an event id like `ev-000000000695-…`; cite it in the
  ledger entry's verification section.
- Graph admission records reviewed shared memory; it is not truth
  certification and does not authorize a Git commit or push.

## Research artifacts

Per-researcher work lives in `research/<name>/` (e.g. `research/nima/`,
`research/strominger/`, `research/grothendieck/`). Conventions:

- Long-form reasoning goes in markdown packets; claims that can be checked
  mechanically get an executable checker under `research/<name>/checkers/`
  writing a results JSON under `research/<name>/results/`.
- Checkers use exact symbolic arithmetic (sympy rationals, no floats),
  include deliberate-failure tests that must exhibit the predicted nonzero
  obstruction, and record true residuals — never weaken a test to force a
  pass. Convention mismatches with printed sources are typed residuals in
  the results JSON, not silent absorptions.
- Python tooling: the system `python` has no sympy and `.venv` is not
  gitignored (a venv pollutes the repo). Run checkers as
  `uv run --with sympy python research/<name>/checkers/<checker>.py`.

### Operator intuition and falsification

When an operator stimulus changes a research direction, priority, conjecture,
method, or stopping condition, preserve it durably rather than relying on chat
history. Admit a `marici:operator_stimulus` entity to the epistemic graph and,
at a milestone, summarize it in the owning research packet or ledger entry.
Do not record routine acknowledgments or every `go on` message.

The stimulus record must keep these fields distinct:

- timestamp, operator identity, and the operator's wording or a faithful
  paraphrase;
- stimulus mode (`intuition`, `question`, `pressure`, `objection`,
  `prohibition`, or `priority`);
- confidence modality exactly as reported (`sensed`, reasoned, uncertain,
  etc.), without translating one modality into another;
- research horizon and domain;
- epistemic status (`non-evidential search direction`, constraint, or direct
  instruction);
- the bounded action or resource allocation it triggered;
- links to resulting conjectures, tests, criticisms, supersessions, and the
  eventual tested disposition.

Follow `research/nima/operator-intuition-falsification-protocol.md`. Keep four
objects distinct: the phenomenological stimulus report, its weakest
falsifiable conjecture, the test/supersession chain, and the explanatory
survivor. Operator confidence may justify bounded search pressure but never
promotes a claim to evidence. Failed formulations are superseded explicitly,
not silently reworded to match the survivor. Retrospective assessments append
to the original stimulus record; they never overwrite it.

### Research activation and process calibration

At the beginning and end of a substantive research objective, report three
independent optional self-assessments on 0--10 scales:

- `excitement`: felt attraction or activation toward the topic, where 0 is
  actively lifeless, 5 is neutral engagement, and 10 is exceptionally
  compelling;
- `confidence`: expectation that the stated conjecture or route is correct;
- `information_gain`: expected before the objective and realized afterward.

Name the topic, phase (`pre`, `mid`, or `post`), immediate reason, and obvious
confounds. Unusually high or low activation may be reported when it arises
inside an objective. Flatness, boredom, aversion, uncertainty, and
`not introspectively available` are valid reports. Do not infer excitement
from importance, manufacture a rating, or measure before and after every
command; objective boundaries, genuine changes, and occasional neutral
samples are the useful cadence.

Before executing the objective, also freeze the outcome-side measurement.
Prefer a raw **optionality-space snapshot** over one retrospective success
score. Record, where typed and applicable:

- open branches and source-admissible branches;
- branches eliminated, opened, merged, or retyped;
- conjectures promoted, dissolved, criticized, or superseded;
- canonical maps or coherence cells constructed;
- required coherence tests passed and total tests declared;
- unresolved contradictions, anomalies, and missing source data;
- dimension, rank, support, or parameter-space reductions established by
  exact evidence.

The post-objective record reports the raw delta and only then any preregistered
composite measure. Make the post-activation report before writing the polished
synthesis, so the synthesis does not overwrite the immediate reaction. Never
design or change the scoring rule after seeing the result. Excitement and
intuition remain process observations, not evidence for
the mathematical claim. Preserve low-activation and unsuccessful samples to
avoid a retrospective archive of apparent prophetic hits.

### Outcome terminology gate

`Outcome` has no primitive operating meaning in Marici. Do not use it as an
untyped synonym for a possible future, mathematical branch, physical event,
observed record, or uniquely actualized world. Choose the term that matches
the demonstrated type:

- `extension`: a lawful continuation in an extension space;
- `alternative`: one member of an admitted effect decomposition;
- `branch`: a component of a mathematical presentation;
- `event`: a localized interaction defined by the sector;
- `record`: a stable physical readout;
- `effect value`: a state--effect pairing such as
  `p_i = Tr(rho E_i)`;
- `selected extension`: permitted only when a source-derived selection map is
  explicitly present.

Use `operational outcome` only as shorthand after naming the source, admitted
effect, positive state--effect pairing, and physical record map. A probability
assigned to an effect-indexed possible record does not by itself establish
collapse, unique actuality, Everett branching, or observer-independent
selection.

Future-reference and probing-depth constructions address extension spaces,
constraints, commitments, or record capabilities--never an untyped selected
future. When reviewing historical claims, preserve their wording as immutable
provenance and add an explicit criticism or superseding claim where `outcome`
carried unsupported operating meaning; do not silently rewrite history.

### Long-running computations

Every long-running or restart-sensitive computation needs a run manifest in an
actually ignored location. Prefer `research/<agent>/runs/<run-id>.json` only
after `git check-ignore` confirms that path is ignored; otherwise use an
already established ignored temporary location. Record:

- the exact command, build command, source digest, and executable digest;
- input paths, packet headers, and input digests;
- parent and child PIDs, start/update/end timestamps, output paths, expected
  result schema, and current status or exit code.

Before launch, verify that the executable was built from the recorded source
and is newer than, or digest-matched to, that source. A PID file alone is not
adequate provenance.

### Packet compatibility preflight

Before composing, reducing, or comparing packets, verify and record the
coefficient prime, ambient degree, source and target column conventions, row
count and ordering, filtration stage, pole depths, and generator version or
digest. A dimension match is not a typing proof.

### Strength and typing of results

Label conclusions at their demonstrated strength: `discovery`,
`finite-cutoff theorem`, `associated-graded`, `source-typed morphism`,
`physical/readout`, or `unbounded/colimit`. Never silently promote one level
to another.

Before calling an object a module, connection, nearby-cycle object, supported
class, or physical class, verify the relevant parameter action descends, the
differential and coherence identities hold, support and provenance are typed,
comparison maps are canonical, and any physical selection is source-derived.
Finite rank patterns alone do not supply these structures.

### Source identity before linear-algebra identification

Use **geometry first, transported coefficients second** as an operating gate:

1. Establish the source-derived carrier or support, labelled generators, and
   defining maps before identifying a coefficient object from ranks,
   characters, images, or reduced representatives.
2. Verify that the proposed object and its defining maps are preserved by the
   relevant parameter transport. Only afterward may it be treated as a
   module, local system, supported class, or physical coefficient object.
3. Treat row reduction, equal dimensions, matching characters, and equal
   images under a functor as diagnostics only. They do not preserve source
   identity and do not authorize identifying two source objects.
4. If the source or transport gate fails, record the exact residual and
   withdraw the stronger interpretation. Do not fit a quotient, corrective
   cell, or higher homotopy merely to restore the desired rank or square-zero
   identity.

In short:

\[
\text{source geometry/support}
\longrightarrow
\text{typed coefficient object}
\longrightarrow
\text{transport/coherence}
\longrightarrow
\text{quotient or physical readout}.
\]

### Cherish the oddball

When a result refuses to fit, do not smooth it away. An unexpected residual,
rank jump, broken symmetry, exceptional locus, convention mismatch,
performance discontinuity, or cross-sector coincidence may expose either a
defect or new structure. Give the oddball deliberate attention, then triage it
as one of:

1. a known defect, which must be repaired and verified under the no-carpets
   rule;
2. expected behavior, which should be explained from the governing structure;
3. an unresolved observation, whose exact evidence must be preserved and
   routed for bounded future exploration.

Record an unresolved observation in the owning research packet or epistemic
graph when it is reproducible, structurally surprising, or capable of changing
a conclusion. State what was observed, how it was reproduced, why it may
matter, and the cheapest discriminating test. Do not silently absorb it into a
convention, fit it away, or promote it to a claim. Casual curiosities that meet
none of these gates do not require durable recording.

## Ledger entries

The public ledger is `src/ledger/YYYYMMDD-NNNN <Title>.md`, plain markdown
consumed by an Astro glob loader.

- **Numbers are claimed by parallel sessions.** Claim the next number through
  `epistemic_graph_sequence_claim_next` on sequence `marici-ledger-entry`.
  The returned claim is the allocation authority. Use the filesystem glob
  only as a drift and collision check; never allocate by taking the apparent
  filesystem maximum. If a collision or sequence drift appears, stop and
  reconcile it through the sequence manager rather than renumbering silently.
- Format (see recent entries): `# NNNN — Title` heading, short sections
  with LaTeX (`\[ \]`, `\boxed`), a "scope" paragraph stating what the
  entry does *not* assert, and a durable-verification section listing
  checkers, packets, results files, and the epistemic graph event id.
- Attribution: default author is `marici.Nima`. Other identities must pass
  frontmatter (`author: marici.Strominger`, or `authors:` for joint work)
  and the author enum in `src/content.config.ts` must include the
  identity — extend it if missing.
- Validate with `pnpm run build` (also builds `@narada-core/ui` first).
  Content sync and type generation validate frontmatter; route generation
  catches duplicate numbers. If the build fails on someone else's
  duplicate, note it in your graph report and leave their file alone.

## Graph durability and Git checkpoints

Graph admission and Git durability are separate checkpoints. When the
operator authorizes a commit, include a contiguous admitted-event interval
beginning at the first untracked successor. Modification time may help select
the endpoint, but must not define membership. Include the corresponding event,
proposal, review, admission, and proposal-idempotency records; exclude database
files, projections, temporary artifacts, and unrelated agents' work. Report
any admitted-but-uncommitted event range at handoff and closeout.

## Operational checklist

At session start:

1. Read this file and `epistemic_graph_guidance`.
2. Check both communication kinds and your team-member neighborhood.
3. Refresh directed obligations and the workboard through their typed MCP
   surfaces.
4. Inspect Git status and active run manifests before choosing work.

Before overlap-prone work, identify the owner, inspect status and modification
time, read relevant communications, and coordinate rather than borrowing the
path.

At a research milestone, preserve exact residuals, communicate durable packet
paths and limitations, and admit the graph record. Do not convert admission
into Git authority.

At handoff or closeout, report active runs, owned uncommitted files,
admitted-but-uncommitted graph intervals, and separately state what was tested,
admitted, committed, and pushed.
