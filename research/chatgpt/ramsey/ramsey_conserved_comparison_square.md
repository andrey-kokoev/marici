# A conserved embedded square, but not yet a complete comparison invariant

The initial row comparison fixes six vertices. Exactly four of them form a red four-cycle. In catalogue191 coordinates this square is Q={0,1,3,11}; in the affine seed output coordinates it is {0,3,4,16}: root, hub label14, stationary label23, and their duad.

The expanded search now explicitly verifies that every visited center lies in Q, every comparison fixes Q pointwise, and the four square edges remain unchanged. At5000 expanded states (16000 discovered), centers were0:409,1:1926,3:2089,11:576. It examined50000 four-edge moves,678 full-orbit transfers,962 rebases and35641 repeated graph-center encounters, with no comparison collision. Budget exhausted partway through depth6; depth9 ceiling was not exhausted.

Why Q is conserved under the admitted operations:
- At a current center c, the two other adjacent Q vertices are its fixed label neighbors a,b; the opposite vertex is their duad {a,b}. Four-edge matching changes do not modify root-label or label-duad incidences, so cannot alter Q.
- A permitted alternative center or full-transfer hub must be fixed by the comparison. Among the center's six label neighbors only the two Q neighbors are fixed. Thus the new center stays in Q.
- The hub-pair star correspondence preserves all four square edges and re-lifts the other three square vertices as fixed points. In particular the opposite old label becomes a pair of fixed new labels. This preserves pointwise comparison fixedness through rebasing/full transfer.

Thus the search is moving around one physically fixed square, not freely choosing any of22 centers. This explains a substantial restriction on the explored state space and connects the moving-center calculus back to the original fixed-label square.

However Q is NOT sufficient to determine the comparison. At any chosen corner/center, it specifies two fixed neighbors among six labels. The remaining FOUR neighbors can be paired into transpositions in THREE different ways. Each choice has a unique canonical extension to the fifteen duads. Hence the remaining comparison information is a three-valued pairing of four off-square label ports.

Next discriminating test: transport ALL THREE such pairings, not merely the original seed pairing, around the same graph-center loops. The observed absence of drift for one pairing could still hide a loop permuting the other two. In group language, the residual return action lies in S3 and the current test might only show that it stabilizes one of three elements. A complete invariant would fix all three, or identify the subgroup actually realized.

Do not claim the conserved square proves flatness. It reduces the unresolved question from arbitrary22-vertex permutations to a three-state pairing transport problem. The new search metadata is in ramsey_frame_loop_search.json and the executable contains square checks at every expanded state.
