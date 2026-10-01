# What composition itself distinguishes at the seam

## Existing machinery reused

`check_seed_seam_continuations.py` uses the existing endpoint-matched path composition and the actual four-word seed rectangle. The interpretation follows Voevodsky's `history-and-possibility-swap-under-coherent-cut-reversal.md`: a source language retains JOINT history/continuation pairs; allowed continuations cannot be inferred by freely combining their marginals.

No edge response matrices, phase updates, comparison fillers or physical admission law are added.

## Free paths: same possibilities, different retained prefixes

The two forward paths x0=AB and x1=AD DB both end at B. In the free endpoint path category, their compatible continuation type is therefore exactly the same: all paths starting at B. This is true at every length, not just a finite approximation.

Appending the same suffix keeps the complete words distinct. A reader retaining the original prefix or full history can distinguish them. But terminal-vertex reading and the set of endpoint-compatible future possibilities cannot. Composition alone gives faithful syntactic history, not an additional dynamical effect.

For the mixed four-word chain Delta, appending any common continuation from A preserves its nonzero word support. The terminal reading and every additive primitive-edge readout still annihilate it: each appended suffix contributes equally to all four terms, whose coefficients sum to zero. Exact regressions test all suffixes of lengths zero through six, while the general statement follows by right cancellation of words and linearity of additive costs.

## Restricted continuations: a real distinction with an explicit assumption

Use the already declared finite objective 'execute each supplied edge once in an A-based closed word'. The permitted suffixes after AB and after AD DB differ because they have consumed different primitive edges. The checker enumerates this language and its two continuation fibers.

The joint relation reconstructs only admitted words. Combining the two history choices with the union of their suffix sets admits forbidden words. Thus retaining a source-defined admission relation can make history operationally relevant to what may happen next.

But the edge-once objective is a scheduling/admission assumption, not a consequence of free path composition or the physical architecture. The resulting distinction cannot be promoted to physical response without justifying that constraint. This is a control comparing two semantics, not a chosen dynamics.

## Synthesis

There are three different levels:

1. **Retained history:** the direct/indirect paths and mixed rectangle are already distinguishable as records.
2. **Free endpoint behavior:** the parallel paths have the same possible continuations and terminal effects; the mixed rectangle has no new signal for those readers.
3. **History-dependent admissibility or response:** can distinguish the paths operationally, but needs a supplied rule. The prior edge-once language is one explicit example, not the derived rule.

The path category is therefore a faithful intrinsic representation, not by itself a physical interaction model. We should not call a path-word indicator a physical measurement or turn a chosen admission restriction into a source theorem.

## Next decision

The missing hypothesis can now be phrased operationally rather than as arbitrary matrices: does traversing a primitive relation change the permissions/state for subsequent comparisons, and by what source rule? If it changes neither and the reader sees only endpoints/additive resources, the mixed seam signal remains zero. If it does, that state/admission update must be specified and tested; it cannot be recovered by further regrouping alone.

## Verification

    python research/nima/checkers/check_seed_seam_continuations.py

Fresh pass includes existing seed/shared-leg checks, finite free-continuation controls, persistence of the retained-word distinction, and the joint-admission/marginal counterexample. No new formal Agda theorem or physical readout is claimed.
