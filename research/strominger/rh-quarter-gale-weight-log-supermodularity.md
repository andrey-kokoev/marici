# Fixed-eight source weights are log-supermodular on nonzero Gale diamonds

## Question

Do the absolute complementary-minor source weights satisfy the local multiplicative inequality required by a lattice-positivity transport mechanism?

## Claim boundary

Yes on every fixed-eight Gale cover diamond whose four weights are nonzero. Across all 3,584 terminal cases, the exact checker tested 109,556 diamonds and found no violation of

\[
w(K)w(K_{ab})\geq w(K_a)w(K_b),
\]

where \(K_a\) and \(K_b\) are commuting Gale cover moves and \(K_{ab}\) is their join. Arithmetic is exact. This is a finite positive certificate; it neither proves the inequality for arbitrary order nor handles diamonds containing zero source terms.

## Disposition

Unlike the failed local cancellation and greedy-flow routes, lattice multiplicative positivity survives a complete nonzero fixed-eight audit. The immediate falsifier is support compatibility: extend weights by zero and test every Gale diamond, including boundary diamonds. A nonzero middle pair with zero meet or join would destroy full log-supermodularity; survival would identify an MTP2-type finite structure worth requesting from the all-order source constructor.
