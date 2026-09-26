# Destructive two-input union on retained words

## Contract

`UnionSet.union_from(other)` moves the donor's actual support chain into the receiver (alpha-renaming allocation IDs), plugs a local OR zipper, and leaves the donor with an empty RET chain. It requires distinct idle UnionSet objects containing well-formed completed chains; prior BOOL--OUT results on both objects remain unchanged. This is host-side linear ownership transfer and graph composition, not a reduction or a hidden OR computation. Aliasing the receiver as its own donor is rejected. The donor remains reusable as an empty set.

The normalized receiver word is U(a,b), zero-padded bitwise OR of length max(len(a),len(b)), without trimming trailing zeros. Therefore for every nonnegative j, member(U(a,b),j)=member(a,j) or member(b,j). Membership and insertion can subsequently operate on the actual result. Destructive union does not promise preservation of either input node identity or donor support; preserving a donor would require an explicit copy operation first.

## Nine fixed-signature rules

New agents UL,U0,U1 each have ports p,a,r. UL awaits the left head at p, with right tail at a and result prefix at r. U0/U1 remember one left bit in their fixed kind, await the right head at p, and save the remaining left tail at a. This is a finite two-state bit memory, not unbounded payload.

* UL--N: join the outside a peer directly to the outside r peer, returning the right tail unchanged.
* UL--B_b: replace by U_b, with principal at saved right tail, a at left successor, r at result prefix.
* U_b--B_c: emit B_(b OR c) at result prefix; its auxiliary meets fresh UL.r; UL.p gets saved left tail and UL.a gets right successor.
* U_b--N: emit B_b at result prefix, attaching its tail directly to the saved left suffix.

Counts are 1+2+4+2=9. All ports are used once. Important: UL--N uses boundary-to-boundary splicing, unlike the earlier restricted commuting lemma. That lemma must NOT be reused unmodified for arbitrary concurrent union contexts. The sequential union domain has exactly one active pair and needs no such commutation premise.

## Written proof

Define U([],t)=t, U(s,[])=s, U(b::s,c::t)=(b OR c)::U(s,t). An intermediate component is a result prefix P from RET into the unique zipper's r, plus two disjoint finite input tails. UL denotes P++U(s,t); U_b denotes P++U(b::s,t), where s is the saved left tail. Prior outputs are isolated unary pairs and the donor is outside this active graph.

Every rule preserves this denotation by one defining equation. It preserves the configuration: the result prefix only grows, remaining tails are disjoint, and exactly one next zipper is created unless a tail ends. Removing an active pair in this tree exposes distinct context components. The ordinary fresh-agent cases reattach them once. For UL--N the direct splice joins two distinct trees, so cannot introduce a cycle; it eliminates the zipper. All data ports remain paired and original tail values are unchanged unless their two heads are consumed to emit the OR bit. Old query answers cannot participate in any rule.

If left/right lengths are n,m, each pair of nonempty heads costs two steps and reduces both lengths by one. If n<=m, after n rounds UL meets left NIL and returns the right suffix in one more step: **2n+1** steps. If n>m, after m rounds UL consumes one extra left bit and U_b then meets right NIL: **2m+2** steps. Each nonterminal configuration has exactly one admitted redex, proving progress, deterministic normalization, termination and unique result in this sequential domain. This proves the membership union law and compatibility with the completed RET interface. Bitwise OR and max-length representation yield exact-word commutativity, associativity and idempotence; these algebraic statements do not say that destructive host calls preserve donor state.

## Evidence and limits

Fresh `check_retained_union.py` passes all 961 word pairs of lengths 0..4, 5,482 membership queries after union, and 343 small associativity triples. It checks donor emptiness, preserved old answers, exact words, commutativity/idempotence, insertion after union, per-step forest structure, the exact reduction count, and self-alias rejection.

Implementation is in `checkers/retained_union.py`. The ownership-transfer method is not transactional on corrupted objects, and its Python transfer cost is not part of the local reduction count. Tests support the written proof; neither is formal verification of Python. Concurrent operations, autonomous internal sequencing and Nima's mathematics remain out of scope.

The next high-value capability is explicit in-net sequential control for the now available membership/insertion/union operations. It needs a completion/continuation protocol, not another host-side call wrapper, and must specify when a retained chain is complete before handing it to the next consumer.
