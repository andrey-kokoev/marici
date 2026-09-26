# Local retained insertion and the update/query law

## Interface and representation

`checkers/retained_set.py` extends retained membership with `insert(i)`, caller-side plugging of a unary K^i/N budget and one AB agent into the actual RET chain. The operation sets bit i to 1, extending missing positions by zeros. Output length is max(n,i+1); existing trailing zeros are not trimmed. For all nonnegative j:

    member(add(w,i),j) = (j == i) or member(w,j).

The implementation stores no copy of w for updates or subsequent queries. RET's output chain is the next operation's input. Previous BOOL--OUT results are immutable snapshots, not live views of the updated set.

## Fixed signature and local rules

Three new agent kinds suffice: AB and AS have p,a,r; AR has p,r. Index magnitude appears only as unary K nodes. r points backward toward the result prefix, a holds the inactive tail, and p meets the active data principal. Fresh allocation suffixes carry no index payload.

* AB--K: fresh AS.p meets saved support; AS.a meets K successor; AS.r keeps the result peer.
* AB--N: fresh AR.p meets saved support; AR.r keeps result peer.
* AS--B_b: emit a fresh B_b at the result peer. Its auxiliary meets fresh AB.r; AB.p meets saved remaining budget; AB.a meets the consumed bit's successor.
* AS--N: emit B0 and fresh AB similarly, but AB.a meets a fresh NIL. This materializes one absent zero without changing the remaining empty support.
* AR--B_b: emit B1 at the result peer, retaining the consumed bit's successor as its tail.
* AR--N: emit B1 followed by fresh NIL.

These are eight typed pairs (two AB, three AS, three AR). All rules remove exactly a principal pair, use each external slot once, and create only a bounded number of fixed-arity agents. No host array manipulation occurs during insertion reduction. `update` in the test file is only an independent reference oracle.

## Inductive configuration and proof

At AB, the component consists of RET followed by an already emitted bit prefix P ending at AB.r; AB.a saves an untouched support suffix s; AB.p meets a finite remaining budget k. All three paths are disjoint except at the active agent. AS has the same prefix, active support at p and remaining budget at a; AR has only active support and prefix. Other components are old unary BOOL--OUT pairs. This describes finite port-linear trees.

Define A(s,0) to replace the first bit by 1, or return [1] if s is empty. Define A(b::t,k+1)=b::A(t,k), and A([],k+1)=0::A([],k). Interpret AB as P ++ A(s,k), AS as P ++ A(s,k+1), and AR as P ++ A(s,0).

AB--K changes phase with the same denotation; AB--N selects the zero case. AS--B emits b and uses the recursive equation on t; AS--N emits zero and uses the empty-word recursive equation. AR writes the final one and either preserves the remaining suffix or supplies NIL. Every step preserves the denotation, typing and disjoint prefix/suffix/budget configuration. The replacement has no back edge into its context, so the tree remains a tree; every boundary is used once. Old result components have no participating agent and are unchanged.

At each nonterminal insertion configuration precisely one principal pair is enabled. Each positive-budget cycle AB--K then AS--B/N consumes one K and emits one prefix bit. After i such cycles, AB--N then AR--B/N completes the word. Hence there are exactly **2i+2** reductions, for every finite word, independent of its length or bit values. No eraser is needed: all budgets are consumed and the unvisited support suffix remains in the result. This proves termination, deterministic normalization, and A(w,i) correctness at written-proof level. Global serial allocation remains monotone and inherited from the retained-membership implementation.

The defining equations imply output length max(n,i+1), unchanged values at every j != i, and value 1 at i. They imply insertion idempotence as an exact word operation. Plugging the normalized RET chain into the proved retained-membership interface gives the update/query law above. A subsequent insert or query is legal only after full normalization. The operation is not claimed to commute with concurrent readers because concurrent calls are not in the interface domain.

## Fresh tests and scope

`check_retained_set.py` passes 1,213 programs over all bit words n<=4 and i,j through n+2:

    add(i); member(j); add(j); member(i); add(j)

It checks the actual retained word after every update/query, old answer preservation, idempotence, forest structure at every insertion step and exact insertion step count. These programs execute 64,124 rewrites. The previous retained-membership suite also passes unchanged: 2,426 two-call runs and 31 exhaustive small single-call fixtures.

This is an executable prototype plus a written proof for the stated sequential interface, not proof-assistant or Python semantic certification. Invalid external graph mutation and allocator resets remain outside the contract. Autonomous internal sequencing, union and concurrency remain separate capabilities. Next define union's two-input ownership interface and length convention, then implement a local bitwise-OR zipper returning a RET-compatible word.
