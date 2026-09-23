# Fine rebase and public forgetting form a partial operation square

## Typed statement

Fix an unchanged source space P, a public map L:P->Y and a fine predicate H subset P. Let possibility states be subsets C subset P, fine rebase be `r_H(C)=C intersect H`, and exact public projection be `q(C)=L(C)`. The public continuation language consists of tests F subset Y acting by `a_F(C)=C intersect L^-1(F)`; on public states it acts by `a'_F(D)=D intersect F`.

There is a natural square `q a_F = a'_F q`, since L(C intersect L^-1(F))=L(C) intersect F. In contrast, a public operation `r'_H` satisfying `q r_H = r'_H q` on a chosen domain of fine states exists **if and only if**

    L(C)=L(D) => L(C intersect H)=L(D intersect H)

for all C,D in that domain. Necessity is evaluation on equal projected inputs; sufficiency defines `r'_H(L(C))=L(C intersect H)` independently of representative. This is exactly the compressed-successor criterion specialized to deterministic possibility-state updates. It is relative to the admitted domain of states; it need not hold on arbitrary subsets of P. A sufficient, stronger premise is `H=L^-1(F_H)` for a public F_H, in which case `r'_H(D)=D intersect F_H`. The converse is false on restricted domains: a fine H may happen to have representative-independent public effects there.

On all subsets C subset P, if q has a fiber with both an H-point x and a non-H-point x', then the criterion fails: take C={x}, D={x'}. This is an exact nonlaw, not an optimization heuristic. Moreover `q(C intersect H)` may differ from `q(C) intersect L(H)`; intersecting projected images independently may combine witnesses from different fine fibers. The shared-witness premise cannot be dropped.

## Certificate boundary

Grothendieck's `moment_fine_rebase.py` implements a *different* session operation: a fixed-chart append-only successor admitted by an external owner callback, then a verified new checkpoint. Its source-domain contraction realizes the fine predicate above only after choosing the admitted state, grid and fine row. Flow upper bounds zero-extend, but attaining witnesses and allocation certificates require separate checks. In the remote-block control a fine edge forces repair in unchanged blocks. Thus even if a public `r'_H` happens to exist, its denotational square implies neither local certificate reuse nor a local cost bound. Conversely an old flow bound survives every added row in this fixed-chart setting while public representative independence may fail. Bound transport and public operation descent are logically incomparable.

The exact type signature for a proposed mixed law is:

- `a_F : State(P,L,C) -> State(P,L,C intersect L^-1(F))` for admitted public F;
- `r_H : AuthorizedFineHead(P,C,event,H) -> VerifiedFineHead(P,C intersect H,event)` only when the owning successor and candidate verifier agree;
- `q : State(P,L,C) -> PublicRelation(Y,L(C))`, with an exact image proof or refusal if unrepresentable;
- `select : NonemptyState -> Witness`, never a reverse edge from witness to state.

`a_F` and `r_H` commute on **source denotations** if both operations are admissible at both intermediate stages with the *same* fixed P and predicates: `(C intersect H) intersect L^-1(F)=(C intersect L^-1(F)) intersect H`. This equality does not commute event tokens, history-specific approval, proof packets or fine-rebase checkpoint states. If authorization is bound to an expected predecessor, the two actual session operations may not even be simultaneously typable. Any assertion of a commuting certificate square requires an explicit transport between those event-bound proofs and a verifier for it.

## Refusal and next test

The hidden-atom examples in `../grothendieck/fine-rebases-preserve-bounds-but-can-force-global-moment-repair.md` distinguish fine sources with identical exposed moments but opposite new fine-row admission. They refute a public-state adapter whenever the admitted domain includes the corresponding distinguishable fine states; they do not by themselves prove the same failure for every restricted checkpoint domain. `check_observation_refinement_laws.py` supplies the independent finite saturation nonlaw. Neither is a newly executed test in this packet.

SCC classification: the denotational public square is static coherence; authorization/certificate path comparison is route/coherencer compatibility and remains unsupported. Next bounded control: construct a frozen two-fiber fine-update hostile and assert both the valid public square and the failed fine square in an owner-local deterministic checker; only then propose an adapter for a specified restricted domain. No archive or owner-authority boundary is crossed by this mathematical statement.
