# Dot 422: source-role compatibility, not a recoloring rule

## Obligation and result

SCC obligation: **route/coherencer compatibility before readout descent**.
Stratum: finite geometric source programs; particle roles remain unassigned.
Status: **blocked**. Both competing translated red-tetrahedron programs violate
retained boundary roles. Contextual labels alone do not repair this.

## What the source actually says

The implemented Steps 2–7 specify:

- A is the white starting vertex.
- The primary red arrow ends at C, proposed and eventually filled white.
- The two white return paths pass through B and D, proposed and filled red.
- Continuation starts from the witnessed **white** destination, not any solid dot.

Sources: `examples/normal-ray/README.md`, Steps 2–7;
`research/realization-tower/cellulation-steps.mjs`, Steps 2–6; and
`cellulation-witness.mjs` / `cellulation-completion.mjs` in that directory.
Step 8 also specifies four colored ring sources and a white opposite vertex.
Blue copies transform the red family color; they do not introduce permission
to exchange white endpoints with colored turns.

These are construction/display assignments, not derived electric charges.
Nevertheless, a claim to copy that *decorated* source program must preserve
its roles, or explicitly provide a different transport of those roles.
The shell's geometric template fit checks only the point set. Its legacy
admission checks solidness, not source color. Proposal reuse returns the old
dot before checking a new requested assignment. Thus geometry can match
while the decorated program does not.

## Concrete obstruction

All coordinates below are FCC integer labels.

| Candidate program | Requested reading at 422 | Retained-boundary obstruction |
| --- | --- | --- |
| `shell:t:3,1,2` | D, red | A = 312 is already red; the source requires white |
| `shell:t:3,2,1` | C, white | A = 321 is white, but B = 332 is already white; the source requires red |

The second program passes its source-vertex check but **not** its complete
boundary-role check. Therefore the evidence does not authorize choosing white
at 422 either. Both failures occur against retained Step 22 data, independently
of which of the two cells is attempted first.

The normals `(1,1,-1)/sqrt(3)` and `(1,-1,1)/sqrt(3)` are computed relative to
cell centers `(3.5,1.5,2.5)` and `(3.5,2.5,1.5)` respectively. They remain
cell-relative geometric data. No intrinsic vertex normal or common camera-lock
reading follows from retaining both.

## Implemented rule

For the **role-preserving interpretation** of source copies:

1. Preserve all proposals and source requirements before deduplication.
2. Keep coincident geometry identified; do not use `(cell, role)` keys to hide
   different requested colors at that shared vertex.
3. Check A/C white and B/D family-colored against every existing vertex.
4. For octahedra, check the white shared/opposite vertices and family-colored ring.
5. If an existing assignment disagrees or its color is unknown, reject that
   candidate program before emitting any of its events. Do not recolor it.

`buildShellWitnessPlan(..., {requireSourceRoles:true})` implements this strict
color-role gate. In the tested Step 23 input it admits **0 of 30** target cells;
422 is not constructed. This is a blocked construction, not a successful repair.
The gate does not establish normal descent or introduce an arrow-exclusion law.
It runs in the planner's whole-cell schedule; it is not a new exhaustive
event-level certificate.

The default viewer still replays the legacy sequence for inspection. Its planner
now records all claims, including suppressed proposals. The panel marks 422
**unresolved**, displays the competing roles, and reports source-role violations.
Its displayed material and click normal remain explicitly legacy selections.
Replay removes future claims; later shell steps retain earlier claims.

## Correction to earlier verification scope

The previous counterexamples and exhaustive state counts concern the frozen
**weaker implemented program**, which admits any solid source. They are not
proof that both routes are admissible under every original source-role condition.
Those counts still expose first-writer order dependence, but cannot establish
compatibility of decorated source copies. Do not promote a geometry-complete
trace into a role-compatible assembly.

## Checks and residual

Run:

```sh
node research/strominger/checkers/check_cellulation_dot_compatibility.mjs
python research/aspect/scc/scc.py check cellulation-dot-422-compatibility
```

Evidence: `research/strominger/results/cellulation-dot-422-compatibility.json`.
The checker reproduces both legacy orders, validates claim retention and UI-state
replay, and checks rejection of both incompatible programs. Its zero exit code
means the negative findings reproduced, not that gluing succeeded. SCC checks
the artifact's source hashes and retains classification `blocked`.

The next construction must match **all** retained boundary roles and directed
witness obligations. Existing white-cell protocols are candidates to examine,
not automatically interchangeable replacements: their arrows, face colors and
admission gates must also match. Alternatively, a role-changing transport needs
an independent source rule and composition checks. Neither has been derived
here. Recoloring 422, averaging normals, or ordering one cell first supplies none
of that missing evidence.
