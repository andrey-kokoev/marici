# Corrective and preventive action plan

Status: deferred by the operator until the current application work is finished. Retain for the next work item; no actions are executed or closed by this plan.
Scope: reliable edit/reload/serve/handoff of isotope-wiring, plus adherence to operator-specified UI placement. No graph/routing redesign, dependency expansion, new dashboard or general process-management framework.

## 1. Incident and evidence boundary

Observed:

- The operator-facing server returned HTTP 200 while the application failed to render.
- Its transformed `src/examples/neon20.ts` response contained only a source-map comment, although the source file was populated.
- Fresh temporary-server browser checks passed while the long-running operator server was broken.
- Reloading the server cleared the empty transformed module. A fresh browser subsequently rendered the actual `http://127.0.0.1:5173/` application and found its controls in the appbar.
- Command-runner server executions terminated with `timed_out`, including an execution requested with a 24-hour lifetime.
- Earlier UI placement decisions were made without an operator requirement and required repeated corrections.

Not yet established:

- A controlled reproduction proving the precise partial-write/watcher/cache sequence. The empty response is confirmed; the proposed causal sequence remains a hypothesis until reproduced.
- Why the command runner did not provide the requested lifetime.
- That the current watcher setting prevents recurrence across the actual edit tools, formatter, retained browser session and long-running server.

Containment already applied, **not closure**:

- Vite now waits for file-write stability (200 ms threshold, 25 ms polling).
- A standalone Windows Vite process replaced the timed-out launch method, with local PID and log files.
- The actual operator URL was checked in a fresh browser after recovery.

## 2. Actions, in execution order

Owner labels below identify implementation boundaries, not task assignments or grants of authority.

### C1 — Establish actual-service acceptance (priority 0)

Owner boundary: application verification.

- Promote the temporary live-browser check into a checked repository script, reusing the existing browser infrastructure rather than adding another automation dependency.
- Accept an explicit target URL and **do not create or silently substitute another server** in this mode.
- Capture browser exceptions, failed module requests and unhandled rejections from before navigation.
- Check that Vue mounts, the expected current model renders with nonzero SVG dimensions, and all action controls are in the appbar.
- Exercise selection and Start/Pause/Clear against that URL. Verify the drawing fills its viewport.
- Record URL, time, source/configuration identity, browser version, result and bounded diagnostic references. Do not record secrets or the operator's personal browser profile.

Acceptance:

- The check fails for HTTP-200/empty-root, empty imported module, failed mount, stale model and misplaced controls.
- It passes against the operator-facing service after recovery, not merely an isolated test server.
- A refused connection or timeout is a failure, never a skip reported as success.

### C2 — Reproduce and eliminate the write/reload failure (priority 0)

Owner boundary: application development tooling; editor/tool writer where applicable.

- Use an isolated fixture on the same filesystem with the same Vite/plugin versions. Never truncate an operator source file to reproduce the incident.
- Keep both the server and browser session running across edits.
- Reproduce truncate-then-write, formatter rewrites, rapid successive changes and atomic replacement. Include writes shorter and longer than the current stability threshold.
- Record file-write completion, watcher events, transformed responses, module requests and browser errors. Establish which sequence actually produces the empty cached module.
- Prefer atomic publication where the responsible writer supports it. Do not claim the app controls writes made by external editing tools.
- Retain write-stability waiting only with demonstrated coverage. A fixed delay is not an atomicity guarantee. If the actual writer cannot be made safe, establish an explicit post-write reload/invalidation boundary rather than repeatedly increasing delays.
- Require a later valid edit to recover correctly even after an interrupted or invalid edit.

Acceptance:

- A regression reproduces the original failure before the correction, or the inability to reproduce is explicitly retained as an open issue.
- With the correction, repeated supported edit sequences yield the latest nonempty module and a working application in the retained browser session.
- Failure injection is detected; it cannot produce a passing handoff.
- Fixture files and browser/server processes are cleaned up even on failure.

### C3 — Make service ownership and lifetime explicit (priority 0)

Owner boundaries: app-local launch tooling; command-runner owner for its contract discrepancy.

- Retain one documented app-local start/status/stop/restart path with repository path, host, port, PID, process start time and log locations.
- Distinguish a running listener from a browser-ready application. Start/restart finishes successfully only after C1 passes.
- Check process identity and port ownership before stopping anything; reject an unrelated listener or stale PID. Do not kill every Node process or blindly free a port.
- Record requested versus observed lifetime of the timed-out runner executions and send a bounded reproducer to the owning surface. Do not modify the harness or claim its lifetime contract is fixed without owner-authorized work.
- Verify the supported launch path survives completion of its launching command and remains healthy beyond the previously observed failure interval.

Acceptance:

- Start, duplicate start, status, restart, stop, occupied port and stale PID cases have explicit tested outcomes.
- A bounded longevity check records its actual observation interval. No statement such as “will run for 24 hours” is inferred from an accepted argument.
- Failed startup leaves actionable logs, not a success message and abandoned process.

### P1 — Cover the missing integration boundary (priority 1)

Owner boundary: application verification.

Keep these as separate checks with separate claims:

1. Static/type/schema checks and production build.
2. Fresh-server browser startup and interaction.
3. Persistent-server, retained-browser edit/reload regression from C2.
4. Actual-service acceptance at the handoff URL from C1.

Acceptance:

- The suite intentionally demonstrates that check 2 can pass while check 3 or 4 fails; reporting must not collapse those results into “the app works.”
- After a relevant edit, evidence from before that edit is not presented as verification of the new state.
- A bounded sequence of at least ten representative edits passes warm reload and actual-service acceptance; this is regression evidence, not a universal reliability claim.

### P2 — Preserve the requested interface, not an assumed design (priority 1)

Owner boundary: application implementation.

- Keep a short authoritative placement contract in `REQUIREMENTS.md`: all action controls in the appbar; only title and route readouts over the drawing; SVG fills the diagram viewport.
- Check actual DOM ancestry and bounds at the existing wide and narrow test sizes, including playback, unavailable diagrams and navigation.
- Before changing arrangement or behaviour, identify the requirement it implements. Ask only when a material choice is genuinely unspecified; do not impose a dashboard convention and rationalize it afterward.
- Do not convert this incident into an unsolicited UI redesign.

Acceptance:

- Tests fail if any button, selector or checkbox returns to the diagram viewport, or if overlay readouts reserve layout rows and shrink the SVG.
- Operator-directed placement is preserved through subsequent changes.

### P3 — Make handoff claims evidence-specific (effective immediately)

Owner boundary: coding agent / implementing maintainer.

- Report “listener responds,” “build passes,” “isolated browser passes,” and “actual service renders” as different facts.
- For a user-visible change, require actual-service browser acceptance before claiming it is available at the operator URL.
- State any untested path or residual failure directly. For example, a deliberately blocked route is not a completed traversal.
- On recurrence, reopen the causal investigation and retained regression. Do not treat another restart as closure.

Acceptance:

- Every completion claim names the relevant verified boundary; HTTP 200 alone never supports a rendering claim.

## 3. Closure gate

The incident remains open until:

- [ ] C1 is retained and demonstrates its negative cases.
- [ ] C2 has a reproduced cause and a passing regression, or an explicitly documented unresolved cause with no claim of permanent correction.
- [ ] C3 has verified ownership/lifecycle behaviour and a separately recorded runner-contract issue.
- [ ] Cold startup, warm reload and actual-service checks pass independently on the corrected state.
- [ ] UI-placement regressions pass at both test sizes.
- [ ] The final evidence identifies the tested source/configuration and the actual URL.

A restart, a watcher delay, a successful build, or one successful browser load does not alone close this plan. Closure is an evidence-backed review, not an automatic status inferred from the amount of work performed.

## 4. Scope controls

- Implement C1 first so subsequent work has a trustworthy acceptance check; then C2 and C3; then complete P1/P2 regression coverage.
- No commits, dependency additions, cross-repository runtime changes or publication are authorized by this plan alone.
- Prefer small retained scripts and existing checks over new infrastructure. Remove superseded temporary diagnostics only after their useful checks are retained and their owned processes are accounted for.
