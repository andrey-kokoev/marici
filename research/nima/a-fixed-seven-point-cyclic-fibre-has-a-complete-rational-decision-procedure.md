# A fixed seven-point cyclic fibre has a complete rational decision procedure

The seven-cyclic-minor conjecture now has a **complete exact decision procedure at each fixed rational target**—not a theorem asserting that every positive target passes.

For a source representative `C` with strictly positive cyclic minors, express the seven cyclic and fourteen noncyclic minors of `C+[a,b]^T k` as affine rational forms. The universal telescoping theorem proves the seven cyclic halfspaces make a nonempty compact two-dimensional polygon. Enumerate intersections of its 21 pairs of supporting lines, retain feasible vertices, and evaluate each noncyclic affine form at every vertex.

For a given noncyclic minor, the procedure returns exactly one of two proof types:

- if its minimum is negative, an exact feasible cyclic-polygon vertex where that noncyclic minor is negative;
- if its minimum is nonnegative, an exact identity `L=alpha*L_p+beta*L_q+gamma`, with two cyclic edges `p,q` and `alpha,beta,gamma>=0`, certifying that minor on the ENTIRE cyclic polygon.

The sparse positive identity exists whenever the minimum is nonnegative: the primal LP has a finite optimum on a compact full-dimensional rational polygon; strong LP duality gives a nonnegative representation of its normal, and a basic dual solution in two fibre dimensions uses at most two cyclic normals. An optimal dual certificate can have constant equal to the nonnegative primal minimum; the executable procedure may return a different valid pair with a smaller nonnegative constant. It enumerates all 21 edge pairs, independently verifies every produced affine identity, and fails closed if the dual search disagrees with the exact vertex minimum.

On seven frozen admitted targets, it returns all 98 whole-fibre certificates. Changing each source representative by a small exact multiple of the moment-curve left-kernel vector leaves its observed `CZ` invariant; independently recomputed noncyclic minima and verdicts remain identical. On the explicit UNADMITTED negative control, it instead returns eight violated noncyclic inequalities, beginning with minor 15 equal to `-16/15` at the cyclic-feasible vertex `(0,-1/15)`.

This distinguishes a **general verifier/construction algorithm for one target** from the missing universal positive-image theorem. The unresolved quantified statement is: every strictly positive seven-column source target is accepted by this decision procedure. Over 14,000 adversarial admitted targets it has not failed, but a finite run is not proof. The algorithm does not identify any source form with a generalized-R history or establish the `n^-2` completion law.

Run `python research/nima/checkers/check_seven_point_cyclic_decision.py`; artifact `research/nima/results/seven-point-cyclic-decision.json`. Independently replayable Farkas identities for the seven admitted targets are in `seven-point-cyclic-farkas-packets.json` with `verify_seven_point_cyclic_farkas_packets.py`.
