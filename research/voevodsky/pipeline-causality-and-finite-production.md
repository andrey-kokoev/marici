# Critical-path reassessment: pipeline causality before more capabilities

Fresh source: `checkers/sequenced_set.py`. The compiler tags each instruction's initial nodes by stage; each rule gives its new nodes the active consumer's stage. Tags are proof/debug annotations and do not enable reductions. The current highest-leverage obligation is a directed production invariant, not additional tests of completed answers or implementing control flow.

## Candidate causal invariant

For every active consumer x at stage s, a principal/principal data peer has allocation stage <=s. A principal/auxiliary wait points to a producer at stage <=s. Strictly earlier stages represent upstream instruction dependencies. Same-stage waits require a separate structural restriction: for membership, Q/E waits can target that stage's COPY auxiliary, while COPY input must come from strictly earlier stages. Insertion and union have only one control agent per stage at a time, so cannot wait on another control agent of their own stage. (Saved query/insertion auxiliary inputs need analogous conditions; the principal condition alone is insufficient.)

Initial source data have stage -1. COPY's output data have its own stage, allowing same-stage Q/E consumption and later-stage consumption. Insertion emits its prefix at its stage; when extending beyond NIL it also creates same-stage NIL for its own next step. Union may return an untouched earlier-stage suffix by splicing, so provenance is not uniformly equal to current stage. The necessary inequality is <=, not equality.

## Finite-production termination route

Assume this invariant and its linear resource/phase clauses are established. Prove by induction on instruction stage that each stage performs finitely many reductions, even under interleaving:

* Initial input and each literal budget/union operand contain finitely many nodes.
* Insertion's AB consumes one of its finitely many budget K nodes per AS visit. Each AS performs at most one step before returning to AB; after budget NIL there is one AR step. Thus its rewrite count is bounded by 2i+2 independently of upstream production timing.
* Union consumes a left head in UL and at most one right head in U0/U1, then returns to UL or finishes. Its literal right chain is finite, so there are at most 2m+2 steps regardless of an upstream stream's size. Splicing emits no extra control loop.
* A membership COPY consumes only earlier-stage nodes and creates no new input on its own principal side. By the stage induction hypothesis only finitely many such nodes are ever produced, so COPY fires finitely often. Its Q/E subsystem consumes its finite budget and the finite copied query branch; no Q/E creates B/N/K. Thus it also fires finitely often.

With finitely many stages, finitely many total reductions follow. This does NOT prove progress: a finite maximal run could still be stuck if a dependency or phase clause is missing. Progress needs a minimal-stage blocked-consumer argument, including same-stage Q/E-to-COPY waits and auxiliary saved tails. Nor does finite production prove outputs have sequential semantics; that needs virtual stream denotations.

## Next critical-path proof

Make causality and same-stage dependency shape explicit for all principal and saved-tail interfaces, prove it under all rules (including UL--N splicing), and use minimal blocked stage to establish no stuck unfinished pipeline. Termination then follows by the finite-production argument above. Semantic preservation and generalized boundary-splice diamonds can be integrated afterward. Do not claim that stage numbers alone prove acyclicity: same-stage constraints are indispensable.
