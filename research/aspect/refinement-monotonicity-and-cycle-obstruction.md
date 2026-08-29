# Refinement monotonicity and the compatibility-cycle obstruction

## Level one: the forgetful-map theorem

Let a completion rung add local labels to an inclusive Bell packet, and let the forgetful map erase only those labels. If the refined packet has a local hidden-variable factorization, applying the local forgetful maps to that factorization produces a local factorization of the coarse packet.

Contrapositively, a nonlocal coarse packet has no local honest refinement.

This closes an ambiguity in the completion ladder. Merely recording more local facts cannot explain away an already inclusive Bell obstruction. If a later rung loses the obstruction, the square did not commute: events were selected, settings or measurement maps changed, cross-wing information entered a local label, or the apparatus was physically perturbed.

## Level two: the quantitative statement

The CHSH functional has coefficient vector `(1, 1, 1, -1)`. Its excess above the local ceiling is `S - 2`. Altering each of the four correlations by at most `epsilon` changes the witness by at most `4 epsilon`. Therefore the packet cannot reach the local CHSH half-space unless at least one correlation coordinate moves by `(S - 2)/4` or more.

For the ideal fixture this lower bound is approximately `0.207107`. This is not the full distance to the local polytope; it is a certified witness lower bound.

## Level three: the cycle rather than the scalar

CHSH is the holonomy around the four-context compatibility cycle. The scalar witness is a readout of a sign inconsistency: three context products are requested with one orientation and the fourth with the opposite orientation. Every deterministic local assignment cancels to magnitude 2. The quantum packet carries a cycle obstruction of magnitude `2 sqrt(2)`.

Completion may split vertices and edges into finer local labels, but an honest forgetful map returns the same oriented cycle. The obstruction is consequently natural under refinement. The informative object is not only the number `S`; it is the cycle plus its projection maps.

## Level four: passive refinement versus active intervention

The theorem applies only when a rung is passive:

- every refined event maps to exactly one previous event;
- pushforward recovers the preceding inclusive counts within preregistered uncertainty;
- settings, measurement maps, and outcome conventions are unchanged;
- no cross-wing variable enters a nominally local label.

An active intervention may be scientifically valuable, but it starts a new ladder. Conditioning and coincidence selection are not forgetful maps on normalized packets; they can create or erase a witness and must be reported as such.

## New experimental target

At each physical rung, test the commuting square before recomputing CHSH. If pushforward fails, localize the failure by setting pair, outcome, no-click class, frame, and reset identifier. The first failed square identifies how the apparatus changed the empirical model. If every square commutes and the obstruction persists, missing-local-route explanations are excluded for all registered routes at once.
