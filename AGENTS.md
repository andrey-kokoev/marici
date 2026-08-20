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
`research/strominger/`). Conventions:

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
