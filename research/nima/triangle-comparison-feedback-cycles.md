# Triangle comparison feedback through three cycles

## Explicit feedback law

The seed is the checked three-record triangle in
`ThreeRecordTriangleRegression.agda`: AB and BC flip a Boolean payload, AC
preserves it. Its first compilation retains the direct one-step route and the
two-step route through B in a joint comparison record R1.

The new rule acts on those retained comparisons:

1. Use the entire previous comparison R as the next input.
2. Exchange its first and second routes, their compiled histories, and their
   canonical-boundary certificates. Reverse its effect-equality witness.
3. Exchange them again, recovering the original full R.
4. Compare this two-step route with the direct identity on R.
5. Promote the resulting new comparison record for the next iteration.

This is a supplied feedback law implemented with the existing native compiler.
It is not selected or inferred by that compiler, and is not identified with the
physical tower's full rung12-to-rung4 dynamics.

The intermediate exchange is nontrivial: the first route's length changes from
one to two. The twice-exchanged record is exactly recovered, including both
histories and the comparison witness. At each new level the competing routes
are distinct syntax with the same complete effect.

## Checked cycles

`TriangleComparisonFeedbackRegression.agda` uses the existing
`compare-compilations` and `next-comparison-Q` constructors. The promoted payload
is actually passed to the next relationship constructor. This replaces the
normalization-only second cycle of the earlier triangle experiment.

| Cycle | Data acted on | Direct route | Two-step route | New retained output |
|---:|---|---|---|---|
| 1 | Seed payload at A,B,C | AC preserves | AB flips, BC flips | R1: comparison of the original routes |
| 2 | Full R1 | Preserve R1 | Exchange its routes twice | R2: comparison of transformations of R1 |
| 3 | Full R2 | Preserve R2 | Exchange its routes twice | R3: comparison of transformations of R2 |

Each row uses three presentation roles, two competing routes, and three new
route comparison slots (one plus two). Two payload inputs, false and true, are
checked. They remain distinct throughout all three cycles.

| Completed cycles | Retained comparison layers per input lineage | Route comparison slots along that ancestry | Checked input lineages |
|---:|---:|---:|---:|
| 1 | 1 | 3 | 2 |
| 2 | 2 | 6 | 2 |
| 3 | 3 | 9 | 2 |

Ancestral counts visit the preceding input chain once. They exclude duplicated
references and the internal syntax of normalization/boundary certificates; they
are not full proof-tree sizes or physical arrow/mass counts. The full compiler
record types permit many other inputs and routes, so two is only the size of
this explicitly generated family.

## Preservation and adverse checks

The generic Feedback module proves:

- exchange twice returns the complete previous comparison;
- the direct and via routes have lengths one and two and are unequal;
- the effects of those routes agree;
- both routes have native canonical-boundary certificates;
- decoding a run recovers the exact previous comparison;
- the feedback map is injective.

The concrete three-cycle instantiation proves:

- the first exchange genuinely changes the order of the seed histories;
- the previous comparison is recoverable after each feedback step;
- the complete seed comparison and its original payload are recoverable after
  cycle3;
- distinct input payloads give distinct cycle3 outputs;
- resetting the true input to the false lineage fails ancestry preservation.

The seed module's conflicting-link check is retained in the dependency closure:
changing AC to flip disagrees with the AB-BC composition and cannot be admitted
with the same coherent coordinates.

## Outcome and limits

Relationships now act on the preceding comparison's retained route fields. This
constructs progressively higher-order comparison records instead of repeatedly
normalizing the same seed value. The chosen exchange is an involution, so its
orbit consists of the original and exchanged ordering. Population growth or new
independent payload information is not produced by this rule. The measured
growth is nested comparison provenance.

The seed triangle's coordinate laws and the feedback exchange are explicit
inputs. Native canonical boundary seeds are inherited from the existing
compiler. No quark, electric charge, spin or proton mass identification is made.

## Verification and implementation

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module TriangleComparisonFeedbackRegression -Fresh
```

Fresh safe Cubical Agda verification passed with `--ignore-interfaces`.

Compilation and its generic preservation proofs are enclosed in an Agda
`abstract` block. The definitions are checked; subsequent cycles use their
proved interfaces rather than repeatedly unfolding complete nested proof trees.
This resolves the expensive definitional expansion encountered in initial
concrete multi-cycle proofs. The final receipt covers the three-cycle version.

- Source: `agda/TriangleComparisonFeedbackRegression.agda`
- Receipt: `results/agda-TriangleComparisonFeedbackRegression.json`
- Log: `results/agda-TriangleComparisonFeedbackRegression.log`
