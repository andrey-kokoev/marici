# The three-prime Clark cut diagram needs joint attachments

## Result

The exact three-prime extension has six routes and 48 marked paths. Its ranks are:

| Observation | Rank | Kernel dimension |
|---|---:|---:|
| Terminal record | 26 | 22 |
| First internal cut only | 36 | 12 |
| Second internal cut only | 36 | 12 |
| Both single-cut observations, recorded separately | 46 | 2 |
| Both internal cuts retained jointly | 48 | 0 |

Thus even collecting **both one-cut observations** does not recover the complete linear history. Two explicit alternating braid combinations vanish in both marginals but survive the joint two-cut record.

All cut-forgetting maps compose correctly, including both orders of rejoining. Opposite reflection commutes with those maps. The finite graded signed record forms admit explicit rejoin mates, with correctly oriented polarity and contravariant mate composition.

This extends the marked diamond as an exact linear cut diagram. It does not identify a nondegenerate metric, physical memory interaction, reciprocal spatial source transformation, or derived Clark functor.

## 1. Source and fixed analytical inputs

Use the source adding 2,3,5 from 2 to 60. In the checker, routes have this order:

1. 2 -> 4 -> 12 -> 60;
2. 2 -> 4 -> 20 -> 60;
3. 2 -> 6 -> 12 -> 60;
4. 2 -> 6 -> 30 -> 60;
5. 2 -> 10 -> 20 -> 60;
6. 2 -> 10 -> 30 -> 60.

The minimal common shell refinement has exponential endpoints

`2,4,6,10,12,20,30,60`.

Let V be its seven-dimensional chamber space. Each event has the independently determined interval-incidence vector v_e. At each route use the eight markings 000 through 111 in lexicographic order.

The analytical inputs are those of `the-two-prime-marked-clark-diamond-is-faithful-before-rejoining-its-cut.md`: fixed prepared forcing, the bounded injective Clark feature map L on V, weighted tensor records, and unitary source seam transport. Here records are retained through degree three.

Replacing chamber letters by L(v) transfers finite linear independence because tensor powers of the finite-dimensional injective map remain injective. This uses the previously established analytical theorem, not a numerical rank test on sampled theta values.

## 2. Four observation levels and their actual maps

For S a subset of the internal positions {1,2}, cut the three-event word at S. Keep:

- the tuple of intermediate arithmetic vertices at those cuts;
- a separate ordered retained tensor word for each resulting segment.

The target is a direct sum over the admitted vertex tuples, with tensor products of the segment record spaces. Segment degree caps are the numbers of events in those segments:

- S empty: (3);
- S={1}: (1,2);
- S={2}: (2,1);
- S={1,2}: (1,1,1).

A forgotten event emits the scalar unit in its segment; it does not erase the intermediate vertex labels retained by S.

For T subset S, J_(T<-S) concatenates adjacent record factors across the deleted cuts and forgets just their vertex labels. It sums coefficients when coordinates collide. The checker verifies

`J_(T<-S) O_S = O_T`

for all inclusions, and, basiswise on the occupied coordinate spaces,

`J_(empty<-{1}) J_({1}<-{1,2})
 = J_(empty<-{1,2})
 = J_(empty<-{2}) J_({2}<-{1,2})`.

These are maps between retained history observations. They do not reconstruct the joint cut record from terminal memory, nor clone an arbitrary physical source state into multiple cut fibers. Source-fiber transport and the record factors remain separately typed.

## 3. Faithfulness and the two marginal ghosts

Write [r;m] for route r with marking m. Set

`epsilon=(-1,+1,+1,-1,-1,+1)`

in the displayed route order. Define

`g_0=sum_r epsilon_r [r;000]`,

`g_1=sum_r epsilon_r ([r;001]+[r;010]+[r;100])`.

Both vanish under O_{1} and O_{2}. They are independent, and the exact joint marginal kernel has dimension two, so they span it. Neither vanishes under O_{1,2}.

### Why these combinations disappear

The six pairs of intermediate vertices form the six-edge cycle in the bipartite graph

`{4,6,10} -- {12,20,30}`.

The alternating coefficients sum to zero at each vertex. This kills g_0 after retaining either vertex alone.

For g_1, at the first cut the three single-retained markings sum to

`v_first tensor 1 + 1 tensor (v_second+v_third)`.

Both v_first and the sum v_second+v_third depend only on the first cut vertex, not on the later prime order. The same statement holds at the second cut, with the first two event vectors summed. The cycle again cancels.

At the full cut level each route has its own pair of intermediate vertices. Within that summand, the eight markings occupy distinct degree triples, and each column is nonzero. Hence the 48 full-cut columns are independent. This gives a direct proof of the full-cut rank in addition to exact elimination.

A single retained cut groups routes into three two-route diamonds. Each group has a fixed nonzero outer event with two marking degrees and the rank-six marked diamond on the other side, explaining rank 3 times 2 times 6 = 36.

The terminal unmarked lift, which sums all eight markings for each route, has rank six. It distinguishes the unmarked routes, but that does not imply faithfulness on their full marked linear span.

## 4. Opposite reflection

Reverse the route and its mask in the opposite source graph. Keep the original real chamber label on each reversed edge, as prescribed by Grothendieck's `../grothendieck/opposite-history-reversal-commutes-with-marked-closure.md`.

The reflected cut set is

`S^rev={3-j : j in S}`.

On record coordinates, reverse the vertex tuple, reverse the order of segment factors, and reverse the letters in each factor. Extend conjugate-linearly over complex coefficients. Then

`Rev O_S = O_(S^rev)^op Rev_source`,

`Rev J_(T<-S) = J_(T^rev<-S^rev)^op Rev`.

The checker tests these identities on every marked path and on the occupied coordinate bases for rejoining. Its coefficient matrices are real, so these basis identities extend to conjugate-linear scalar reversal. Reversal squared is the identity.

This is opposite-category label transport, not an identification of the reversed route with a forward prime route or a spatial reciprocal forcing.

## 5. Signed Green mates for rejoining

Use the declared graded record form, with degree r weighted by tau^(2r) and signed operator C_Clark^(tensor r). For a segment capacity vector c, use the tensor product of its graded forms.

Rejoining preserves total degree. On pure tensors its Green mate splits the output word at every degree allocation allowed by the original segment capacities, restoring those tensor slots. If vertex labels have also been forgotten, the mate copies to every admitted label preimage. These are finite direct sums and bounded maps at depth three.

In the coordinate bases of four-port words, write J for rejoining and Q_source,Q_target for the weighted signed Gram matrices. The exact identity is

`J* Q_target = Q_source J^sharp`, with `J^sharp=J^T`.

The transpose is the explicit sum over permitted splittings; it is not an inverse. Tensor reassociation proves the same identity for the Hilbert feature factors, because the signed operators and weights agree on each fixed total-degree allocation. No inverse of the degenerate C_Clark is needed.

The checker tests all strict inclusions among the four capacity levels, of dimensions 85,105,105,125 in the four-port fixture. It also checks

`(J_2 J_1)^sharp = J_1^sharp J_2^sharp`

along both rejoining paths. The finite vertex-label copy/sum factors carry ordinary direct-sum pairings and obey the same transpose rule; no extra source-dependent scalar is fitted.

The independent complex-feature creation test verifies, now through depth three,

`c_R(g)* Q = Q [tau^2 a_R(C_Clark g)]`.

Its mate is not asserted invertible. These identities concern the specified graded signed extension, not a proof that it is the independently prescribed full arithmetic Green form.

## 6. Oriented feature polarity

Apply the actual port swap P, spectral conjugation, and reversal of tensor slots. The lower carrier uses -C_Clark, not C_Clark. Thus on total degree r its signed form differs by (-1)^r before conjugating the port coordinates.

The checker verifies the resulting form identity at every cut level and verifies that polarity commutes with rejoining and its signed mate. It includes a hostile test showing that retaining C_Clark instead of -C_Clark on the lower carrier fails.

The analytic antiunitary is the previously constructed tail polarity from `clark-tail-polarity-gives-an-exact-dagger-between-history-receivers.md`; these finite tests verify its tensor and cut bookkeeping. No Hilbert-adjoint or inverse-event identification is introduced.

## 7. Verification and next theorem

Command:

`uv run --with sympy python research/voevodsky/checkers/check_marked_clark_three_prime_cuts.py`

Passed all exact tests. Certificate:

`results/marked-clark-three-prime-cuts.json`.

The certificate includes sparse bases for every single-level kernel, the two explicit joint-marginal ghosts, route/mark ordering, ranks, rejoining, polarity, and signed-mate checks. Rational coordinate Gram matrices are used only to compute ranks and nullspaces; they are not claimed to be physical or Clark metrics. Every reported single-level null vector is also checked directly against its observation columns.

The decisive new result is that **separate cut observations are insufficient for linear faithfulness even when both are available**. The joint attachment data is essential.

The most useful next formal theorem is a typed multi-cut receiver with deletion/coarsening and opposite reflection laws, using this three-prime ghost pair as a negative control against replacing joint cut data by its marginals. This is now a concrete target for the boundary-sensitive semantics. A full stable analytical realization and a nondegenerate Green form remain separate obligations.
