# Residual three-vertex shortcuts: a boundary-symmetry obstruction

## Status

An executed follow-up to the [derived completion test](trivalent-derived-completion-results.md).
This works in the **reversible experimental extension** with associativity and
Frobenius comparisons. No new independent generator, primitive vertex or higher
filler is admitted.

```text
python research/nima/checkers/check_trivalent_residual_completion.py
```

Evidence: `results/trivalent-residual-completion.json`. The checker verifies
the prior report's source hashes before using its canonical graph IDs. It
stores signed derivations, internal relabelling witnesses, actual contextual
primitive expansions, boundary-symmetry witnesses and all completion tests.
All assertions pass.

## 1. Extracting the four forks

Use the first best acyclic orientation from the earlier test:

    α forward; reversed α backward; K→F_L; F_R→K.

Its four unjoined ordered-boundary instances have these terminal pairs:

| Source IDs | Terminal IDs | Boundary |
|---|---|---|
| 190, 191 | 272, 273 | (2,1) |
| 612, 613 | 626, 627 | (1,2) |

Each pair consists of the same internal port graph with a different order of
the two external input or output legs. These IDs refer to the hash-bound saved
census, not invariant mathematical names.

Each fork has a one-step route to one terminal and a two-step route to the
other. Inverting the first route and following the second gives an explicit
**three-step composite comparison** between terminals. The checker replays
all four composites, accounting for canonical vertex relabelling. It also
expands every actual macro placement back into primitive steps.

Thus the terminal comparison is derived, provided the experimental comparison
cells are reversible. No appeal to a new primitive relation is necessary.
This does not derive a higher cell equating the two routes.

## 2. Symmetry classification

Simultaneously permuting the external boundary of the fork source and both
terminals gives two fork orbits: the pair at (2,1) and the pair at (1,2).
Allowing the chosen global reversal still leaves two orbits of these
**source-plus-unordered-terminal triples**.

In particular, reversal does not simply exchange the two residual forks of
this directed presentation. It can exchange a source diagram with a terminal
diagram: the chosen normalization directions are not reversal-equivariant.
Do not confuse orbit equivalence of diagrams, terminal equations and whole
forks.

## 3. Testing the derived local schemas

For each terminal equation, try either rewrite direction and instantiate it
as an honest local three-vertex schema. There are four choices of the two
nominal directions. **All four give the same result:**

- all 124 tested forks join;
- four placement edges lie on directed cycles;
- these edges form two two-cycles, one per terminal pair;
- the total directed placement count is 760, compared with 756 before adding
  the macros.

Why does choosing a direction not remove the reverse?

At (2,1), exchanging the two external inputs maps diagram 272 to 273 and 273
to 272. At (1,2), exchanging the two outputs does the same for 626 and 627.
The schema applies in both boundary-permuted placements. Therefore one displayed
orientation already generates both directed edges.

This is not an implementation accident: the checker records the explicit
input permutation (1,0) or output permutation (1,0), and verifies its action
on both endpoints. Local slot numbers remain fixed throughout.

### The general obstruction exposed here

If a symmetry p exchanges A and B, an equivariant relation containing A→B
also contains p(A)→p(B), namely B→A. Hence that direct orientation cannot be
terminating on distinct A,B.

The experiment realizes this elementary obstruction twice. It does **not**
prove that every possible normalization strategy for the theory is impossible.
It rules out these directly oriented terminal-swap schemas as an equivariant
terminating completion on the present ordered syntax.

## 4. A deliberately misleading control, made explicit

For comparison, orient only the numbered graph pairs, without adding their
boundary-permuted placements. All four such controls have:

- zero unjoined forks;
- zero directed cycles;
- 758 placements.

So one can manufacture a convergent finite lookup table here. But this is not
a local equivariant rewriting system: its apparent success depends on treating
one representative differently from its symmetry mate. The checker labels
these results `non_equivariant_anchored_controls` rather than claiming a
completion of the calculus.

A future canonical-order algorithm could intentionally break symmetry, but
would need to specify that choice and prove context compatibility or an
appropriate equivariance-up-to-witness property. Graph ID order supplies none
of those properties.

## 5. Checks

- Freshness of the prior report against all its recorded checker dependencies.
- Replay of every signed residual derivation through valid primitive matches.
- Explicit internal renaming when undoing canonicalized primitive steps.
- Replay of each local macro placement, including boundary-permuted instances,
  as a three-step primitive path with the same target.
- Syntax substitution reversal, convexity, valid incidence and census closure.
- Exact integer tensor agreement in the scaled copy/merge model.
- Explicit symmetry exchanging both endpoints of each terminal equation.
- Fork joinability and directed-cycle checks for every nominal macro direction
  and every numbered-graph control.

The scope remains the closed one-through-three-vertex DAG census. No
four-vertex disjoint-support analysis, arbitrary-arity completion theorem or
higher coherence filler is claimed.

## 6. What this means and what to test next

The residual diagrams can be compared using existing experimental cells.
The obstruction is in **directed normalization respecting symmetry**, not a
lack of a comparison path and not evidence for a new primitive operation.

Three distinct continuations should not be conflated:

1. **Rewriting modulo a declared symmetry:** choose exactly which boundary
   actions may be quotiented. This changes the representation of the ordered
   calculus; retain permutation witnesses if boundary information is needed.
2. **Normalization with explicit choices:** add an order or marked port and
   test a deterministic strategy, while proving how its outputs transform under
   symmetry. Do not call the orientation choice intrinsic.
3. **Retained higher comparisons:** keep the two directions and their paths
   rather than forcing termination. Then specify and test candidate coherence
   cells between paths; endpoint joinability alone does not supply them.

The [boundary-modulo normalization test](trivalent-modulo-boundary-results.md)
now checks the full external-boundary quotient: 95 orbits, 72 directed edges
and 33 terminal normal forms, with exact recovery of all 874 ordered canonical
inputs from retained ledgers. A noncommutative Frobenius model shows that the
quotient alone loses semantic boundary information. Next test composition with
transported gluing. This does not select seven grades or close the general
trivalent-generation conjecture.
