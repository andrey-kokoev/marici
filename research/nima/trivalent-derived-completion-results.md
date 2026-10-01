# Derived slide shortcuts: bounded completion test

## Scope

Continuation of the [contextual overlap experiment](trivalent-contextual-overlap-results.md).
All checks use the same 874 ordered-boundary connected DAGs with one through
three vertices. Local slots remain distinguishable. Only convex induced
two-vertex subdiagrams are rewritten.

```text
python research/nima/checkers/check_trivalent_derived_completion.py
```

Machine evidence: `results/trivalent-derived-completion.json`, with diagrams,
placements, replayable shortcut expansions, fork witnesses, normal forms,
orientation controls, example directed cycles and source hashes. All assertions
pass. These are finite Python checks, not a global convergence proof.

## What is derived, and under which assumption?

Let β_L: K→F_L and β_R: K→F_R denote the **experimental** Frobenius comparisons.
If these comparisons are reversible, the following path is available:

    F_R --β_R⁻¹--> K --β_L--> F_L.

The reverse path gives F_L→F_R. The experiment tests each path as a shortcut
rewrite. Each contextual instance stores its expansion and intermediate graph;
replaying the two underlying steps must reproduce the shortcut exactly.

This is a derived **composite rewrite in the reversible experimental extension**.
It is not derived from primitive vertex reversal or from the outward directed
system alone. Invertibility of comparison cells and orientation reversal of
vertices are distinct assumptions. No independent higher filler is introduced.

## Main results

| Directed system | Joined same-support forks | Joined shared-vertex forks | Unjoined shared-vertex forks | Placement edges on directed cycles |
|---|---:|---:|---:|---:|
| Outward plus F_R→F_L | 156 | 168 | 16 | 4 |
| Outward plus F_L→F_R | 156 | 168 | 16 | 4 |
| Outward plus both shortcuts | 156 | 296 | 0 | 388 |

The outward baseline has 156 unjoined same-support forks and 96 joined
shared-vertex forks, with no directed cycles. Either shortcut fixes the
same-support fork but creates new contextual problems. In each single-shortcut
system, an explicit four-step directed loop is stored in the report. With both
shortcuts, there is already a two-step loop between the slide targets.

The last column counts **placement edges participating in cycles**, not the
number of distinct cycles. All-forks-join is not enough for terminating
normalization. Introducing both shortcuts does not establish a convergent
presentation.

## Orientation control: all sixteen choices

The checker also tests both directions for each of the four elementary
comparisons: α, reversed α, β_L and β_R. These sixteen tests use no shortcut.
None has both zero unjoined forks and zero directed cycles in the census.

The two best acyclic orientations each leave only four unjoined forks. One is:

    α forward;
    reversed α backward;
    K → F_L;
    F_R → K.

The other reverses all four choices. Their remaining forks have boundaries

    (2,1), (2,1), (1,2), (1,2).

Each source has three vertices and three external legs, so its underlying
undirected cycle rank is one, by B=V+2−2b₁. These graphs are still directed
acyclic: an undirected cycle is not directed feedback.

Thus these orientations remove all unjoined forks in the underlying-tree
sector through three vertices, while leaving a sharply localized mixed
cycle-rank-one obstruction. The four counts are ordered-boundary instances,
not a claim of four irreducible relation types.

These preferred orientations need not preserve the chosen reversal action
as a **directed** rewrite symmetry. They orient the same reversible equations;
that is weaker than a reversal-equivariant normalization procedure.

## Checks and boundaries

- Every admitted replacement has valid incidence and remains in the DAG census.
- Every replacement can be undone as a syntax substitution.
- Derived steps expand into the claimed two elementary steps with a valid
  intermediate graph; a deliberately wrong first direction is rejected.
- All elementary and derived replacements preserve their exact integer tensor
  maps in the scaled copy/merge model.
- The report retains explicit joining paths or terminal descendant sets.
- No higher cell equating two paths is assumed just because their endpoints join.
- Nonconvex matches are excluded; unrestricted feedback composition is not part
  of this experiment.

The 1,824 placement entries in the report include all elementary directions and
both shortcuts. They are not all enabled simultaneously in any of the sixteen
orientation controls. Thirty-two candidate placements are excluded by the
convex/DAG constraints.

## Meaning and next executable step

The first shortcut is justified by existing **experimental reversible cells**,
but it is not a successful directed completion. The finite test narrows where
to look next without demanding another primitive vertex or declaring seven
grades.

The [residual shortcut test](trivalent-residual-completion-results.md) now
extracts and replays those three-step derived comparisons. Honest local schemas
close every tested fork but create two two-cycles: an external-port swap
exchanges each pair of terminals, so either nominal orientation supplies both
directions under the boundary action. Numbered-graph-only controls converge in
the finite census but are not equivariant local schemas.

Next compare rewriting modulo an explicitly declared symmetry, normalization
with recorded choices, and retaining higher comparison paths. A higher
coherence cell remains separate from the composite path.

No result here proves global termination, finite completion in all arities,
or an interpretation into the native grammar or conditional DG model.
