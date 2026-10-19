# Construction-obstruction atlas: fixed support and terminal repair

## Question and claim boundary

The operator selected structural synthesis over simply adding heavier isotope targets. The bounded goal is to explain retained-construction success/failure through marked interface incidence, directed reader support and actual contact obligations. Active coherence obligation: forward realization for the classifier, then fixed-selection route compatibility for the materialization square. Neither is field sewing or physical reaction dynamics.

The implemented terminal PE constructor, Nima's obligation atlas and his execution planner are reused, not redeveloped or treated as an occupancy derivation. The initial protocol is `inputs/isotope-obstruction-protocol-v1.json`. N-15 single deletions are the development family. Ne-22 single deletions are retrospective cross-family validation, since their outcomes were already known. All 66 Ne-22 double deletions are the additional test family generated in this execution. Classification does not read saved pass/fail flags.

## Exact criterion

Fix a compatible selected reader set S containing its root. Let G be its selected native directed graph, E its selected electron readers, and J the eligible PE edges under the explicit experimental policy. Every electron reader is a native sink, and every edge in J ends at one. Native factors, marked edge, complete permutation, common origin, reference-body vacancy and source-reader terminality are checked independently of the constructor implementation.

Let R be the native root-reachable set, T the native ancestors of E, and Anc_G the native ancestor closure. Then

\[
R'=R\cup\{e:(p,e)\in J,\ p\in R\},
\qquad
T'=T\cup\operatorname{Anc}_G(\operatorname{sources}(J)).
\]

The full selected assembly passes the experimental policy exactly when R'=S, T'=S, and every occupied triangular face has a selected native witness. Particle-count and geometric compatibility gates remain in force.

**Derivation:** a path can traverse an added edge only as its final edge, because its electron target is a sink. Hence added edges cannot change reachability of nuclear readers; their effect on exit ancestry is exactly the native predecessors of their P sources. PE edges do not witness occupied triangular faces. Eligible final-set guards are negative selection conditions: vacancy and absence of selected native successors. They remain valid in subsets containing the endpoints. Compatibility is hereditary under selection removal. Thus a rooted traversal of the final graph supplies a prefix-valid construction under these source-rule hypotheses. The existing full constructor separately replays those prefixes in every tested case.

This restates and applies the previously known sink-only support constraint; the new deliverables are a reusable obstruction signature, cross-family comparisons, the double-deletion family and its isotope-level materialization routes. It is not a new gluing theorem or a source-independent occupancy law.

## Falsification and finite results

Rivals were particle-count sufficiency, scalar port-budget sufficiency, reference-geometry-only contraction and undirected connectivity. The strongest test compares independently computed root/exit sets and eligible schemas against the existing full constructor, including prefix replay. All 87 configurations agree exactly:

| Family | Cases | Already native | Experimental terminal repairs | Nuclear-root-cut category | Remaining unserved-terminal category |
|---|---:|---:|---:|---:|---:|
| N-15 minus one N: N-14 counts | 8 | 0 | 2 | 5 | 1 |
| Ne-22 minus one N: Ne-21 counts | 12 | 0 | 2 | 7 | 3 |
| Ne-22 minus two N: Ne-20 counts | 66 | 0 | 1 | 56 | 9 |
| Independent saved Ne-20 | 1 | 1 | 0 | 0 | 0 |

Categories have a declared priority. Raw failure flags are nonexclusive and retained in the receipt: root failure can coexist with missing exits or unserved E records. All deletion cases retain native witnesses for their remaining occupied faces, so this family does not empirically exercise the missing-face obstruction. The criterion retains that gate rather than inferring its dispensability.

### Scalar port budgets fail

The proxy `2*P - occupied PN faces` counts unoccupied proton MCM-face slots. It is not a count of geometrically/role-admissible additions.

- N-15 deletion 16 passes; deletion 8 fails. Both have 7P/7N/7e and one unoccupied MCM slot.
- Ne-22 deletion 16 passes; deletion 1 fails. Both have 10P/11N/10e and two such slots.
- Double deletion 16/29 passes; double deletion 1/6 fails. Both have 10P/10N/10e and three such slots.

The failing examples contain native nuclear root cuts. A terminal PE operation cannot cross those cuts. Thus neither isotope counts nor counts plus a total unused-face budget determine construction success. Full directed marked incidence is necessary for this diagnostic.

## A connected neon construction family

Exactly one of the 66 double deletions passes: source-local neutron bodies **16 and 29**. The resulting 10P/10N/10e configuration uses retained references at those vacant sites. It is a new fixed-footprint experimental Ne-20 certificate, not discovery of Ne-20 (an independent native witness was already saved at origin five).

Using Nima's current planner read-only at source origin four, all five tested target-interval plans replay successfully:

| Retained start → target | Replay | Singleton-only planner |
|---|---|---|
| Ne-20 → Ne-21 missing body16: restore29 | One singleton | Pass |
| Ne-21 missing16 → native Ne-22: restore16 | One whole-body batch | Unreachable in this interval |
| Ne-20 → Ne-21 missing29: restore16 | One whole-body batch | Unreachable in this interval |
| Ne-21 missing29 → native Ne-22: restore29 | One singleton | Pass |
| Ne-20 → native Ne-22 | Two steps, one batch | Unreachable in this interval |

The batch adds the two original readers of the same neutron body16, not two neutron particles. Occupying that body disables its reference shortcuts, so both needed native replacements must be restored together in these configurations. Body29 has one reader and admits a singleton addition. No arbitrary multi-body batch was introduced.

Both routes terminate at exactly the original saved Ne-22 selection with its unchanged complete packet maps. Intermediate route histories are retained, not identified. This is an endpoint-agreeing construction square with explicit schedules, not a higher-homotopy proof, reversible nuclear reaction, or energy/stability claim. The planner's singleton impossibilities are exhaustive only within each fixed start/target interval and the declared transition family.

## Relation to retained carbon/boron branches

Existing results provide two different obstruction types outside this new family:

- Selected C-12 → C-13 exhausts every proton's two PN faces under the stricter occupied-proton-reader ansatz. That is a local port obstruction in that ansatz, not a prohibition in the broader reference grammar.
- Selected Be-9 → B-10 fails completion of five admissible electron placements in its retained bounded extension search; a separate B-10 whole-assembly construction succeeds.

These are read context from `carbon-phase-references-v1.md`, `boron-phase-references-v1.md` and the current `assembly-contact-coverage-repair-v1.md`, not newly rerun searches here. Do not combine their stricter search hypotheses with the reference-only grammar silently. The present atlas supplies a reusable route/support layer; it does not yet replace geometric completion search for arbitrary new placements.

## Disposition and reproduction

The explanation surviving the tests is typed, not scalar: record native root cuts, terminal targets, exit ancestry, occupied face witnesses and guarded reference support separately. It correctly separates the saved single-deletion families and the new double-deletion cases, and produces a connected Ne-20/21/22 construction family with explicit schedules. No criterion for physical stability, unique/minimal geometry, occupancy permission, universal depth or global field sewing is promoted.

```sh
node research/strominger/checkers/check_isotope_obstruction_atlas.mjs
node research/strominger/checkers/check_isotope_materialization_square.mjs
```

- `results/isotope-obstruction-atlas/verification.json`: source hashes, protocol, all 87 cases, nonexclusive deficits, exact shortcut maps and full construction prefixes for passing cases.
- `results/isotope-obstruction-atlas/materialization-square.json`: all five source-bound plans, independent replay and singleton-only comparisons.
- Owner-local SCC manifest: `scc-models/isotope-obstruction-atlas.json`.

Other-owner source and result files, production rules and viewer admission remain unchanged.
