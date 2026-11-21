# All three pairings—and ordered ports—return unchanged in the bounded search

ramsey_three_pairing_loop_search.py propagates all THREE pairings of the four off-square label neighbors simultaneously through exactly the graph moves of the earlier search. At each graph-center reencounter it compares the ordered triple of comparison permutations, rather than only the original seed comparison. This detects an S3 return action hidden by fixing one pairing.

Result at5000 expanded nodes:16000 states seen,35641 reencounters, no permutation of the three pairings. Same move counts as previous run:50000 four-edge changes,678 full-orbit transfers,962 rebases. Budget stops partway through depth6, with11000 states queued; depth9 ceiling not exhausted.

There is still a mathematical blind spot if only pairings are followed: S4 acting on four ports maps onto S3 acting on their three pairings, with Klein-four kernel. A double transposition of ordered ports preserves EVERY pairing. Therefore ramsey_ordered_port_loop_search.py additionally follows the individual ordered port labels.

The port correspondence at an admitted center change c->h is explicit: for an old port a, take the unique common neighbor of h and a other than c, i.e. the old duad {h,a}. This is an off-square label at the new center. Four-edge moves preserving the current chart leave port labels unchanged. The code verifies the four transported vertices equal the new off-square neighbor set at every step.

The ordered-port test has the same5000/16000/35641 counts and again finds no return discrepancy. Thus neither an S3 permutation of pairings nor a hidden Klein-four port permutation appears in the explored region. These are stronger bounded observations, NOT a proof of global flatness.

Initial fixed square is {0,1,3,11}, initial ordered ports[2,4,5,6] in catalogue coordinates. JSON artifacts retain scope and counters; a discovered discrepancy would preserve replayable route certificates. Next structural target: define or rule out a path-independent four-label assignment to the off-square ports over the entire reachable component. Such an assignment would explain both comparison and port return at once. Its existence is suggested by this search but has not been derived from an intrinsic graph invariant.
