# The arrival reader is closed under every typed continuation

## Result

For the EXISTING arrival observer and path interpreter, two histories ending at the same vertex have the same current arrival exactly when every endpoint-compatible finite continuation gives the same arrival reading. The empty continuation is included.

This gives a precise, continuation-closed observational quotient of the free seed histories. It does not recover those histories, select a physical instrument, or identify the quotient with the intended rung4 state.

The result corrects a possible overreading of the previous repeat-history collision: repetition alone does not require a larger predictive state. Additional HISTORY-SENSITIVE questions do. Full provenance continues to be retained separately.

## Frozen task and operation

Use the original six-occurrence table, unchanged:

    AB, BC, CA, AD, DB, BA.

The carrier at a vertex v is the existing target fiber

    Arrival(v) = (e : Occurrence, target(e)=v).

The previously declared observation update is

    arrive(e, previous) = (e,refl).

A typed continuation is a free path k:v->w. Its operation is the existing `SeedArrivalEffects.Read.run k`. This is an observer of a supplied traversal, not an autonomous selection of which traversal occurs.

For a fixed initial arrival a at A, write

    obs(p)=Read.run p a.

The existing composition law gives

    obs(append(p,k))=Read.run k (obs(p)).

No face equation, inverse reference, numerical amplitude, metric or new transition policy is needed.

## Exact contextual theorem

For p,q:A->v define

    FutureEqual(p,q) :=
      for every w and k:v->w,
      obs(append(p,k))=obs(append(q,k)).

`SeedArrivalContinuationQuotient.agda` proves both implications:

    obs(p)=obs(q)  -> FutureEqual(p,q),
    FutureEqual(p,q) -> obs(p)=obs(q).

The forward implication uses the composition law and congruence of the actual continuation interpreter. The reverse implication uses the empty continuation. This is an unbounded theorem over all finite typed paths, not an enumeration up to a chosen depth.

Therefore current arrival equality is exactly the coarsest equivalence preserving this frozen current-and-future arrival task. Any other summary that reconstructs current arrival must refine that equivalence; the module supplies the corresponding factorization implication. No claim of physical minimal memory or least resource cost follows.

## Source-level port binding to the existing successor

All six arrival occurrence states are reachable from A, with explicitly proved representatives:

| Arrival | Representative retained path |
|---|---|
| AB | AB |
| BC | AB BC |
| CA | AB BC CA |
| AD | AD |
| DB | AD DB |
| BA | AB BA |

A primitive transition from current occurrence e to next occurrence f is available exactly when

    target(e)=source(f).

The resulting transition support has ten pairs. It matches EXACTLY the ten-word first successor already produced by `RetainedSuccessorLedger` in `check_actual_triangle_branch_composition.py`:

- LL: AB BC, BC CA, CA AB;
- LR: AB BA, CA AD;
- RL: BA AB, DB BC;
- RR: BA AD, AD DB, DB BA.

The companion checker extracts the formal endpoint declarations and compares them with that existing ledger's registry and actual generated words. It does not compare counts alone. The36 existing branch-composition checks are rerun.

This binds the two implementations at their typed transition SUPPORT. It does not identify the observer quotient with the whole retained ledger, its coefficients, sibling-detail decomposition or response law. In particular historical operand-role correlations may remain relevant to tasks outside arrival-only observation.

## What survives from the previous source-row result

On the original two-triangle joint relation, CA identifies ABC and BA identifies ADB, so the arrival observer recovers every question about that ONE selected row.

For larger domains, arrival no longer recovers the full path. Yet the new theorem shows exactly when that loss is operationally harmless:

- the four-corner paths AB BA and AD DB BA have the same arrival and remain arrival-indistinguishable under every typed continuation;
- one ABC and two concatenated ABC traversals have different retained histories but likewise remain arrival-indistinguishable under every future arrival reading.

The latter is proved directly in the new formal module. Their length difference remains proved by the earlier source module. Adding a question about length, earlier component roles, or history-sensitive response changes the task family; the arrival quotient need not preserve it.

A hidden distinction need not be discarded from provenance just because it is unnecessary for this predictive observer. Conversely, retaining it does not show that the observer consumes it.

## Consequence for the descent programme

There is now an existing source operation with an exact closed observation interface:

    retained typed paths --observe--> arrival fibers
          | append k                    | Read.run k
          v                             v
    retained typed paths --observe--> arrival fibers.

Unlike a generic memory analogy, both sides use the same original occurrences and the same actual interpreter. The transition support also matches the existing endpoint-compatible successor.

This is a structural synthesis result, not identification with the confirmed rung diagram. The intended T9 still must be bound to an actual constructor and its admitted task family. The present candidate is adequate for arrival-only continuation; it is inadequate for full-history recovery or an independently specified mixed response. Matrix J4, physical reference normalization and instrument selection are untouched.

The next productive test of a proposed rung binding is therefore concrete: does its authorized observation include anything beyond this arrival process? If yes, exhibit that question or feedback operation and test its descent. Do not demand all history merely because repetitions exist, and do not discard history-dependent response tasks merely because the arrival process closes.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedArrivalContinuationQuotient -Fresh
    python research/nima/checkers/check_seed_arrival_continuation_quotient.py

Fresh safe Cubical/guardedness closure passed with ignored interfaces and stable inputs.11 port-binding checks pass, alongside36 rerun existing successor checks. The Python audit verifies relevant formal-source hashes against the fresh receipt; running Python alone does not recompile Agda.

Artifacts:

- `agda/SeedArrivalContinuationQuotient.agda`
- `results/agda-SeedArrivalContinuationQuotient.json`
- `results/seed-arrival-continuation-quotient.json`

No existing source update or physical policy was modified. No new postulates or unresolved holes remain.
