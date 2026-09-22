# The background-two vacuum increment has seven states and a nonintrinsic filtration

## Result

The remaining rank audit is resolved for the full declared old detector union, including its matched-optimal scalar test:

    D=ker(E^+->E), dim D=7,
    dim(F^1 D,F^2 D,F^3 D,F^4 D)=(7,5,1,0).

The acquisition extension remains nonsplit, as proved in `the-background-two-vacuum-acquisition-is-a-nonsplit-observer-enlargement.md`.

The inherited filtration is NOT the intrinsic ideal-power filtration of D. In fact

    dim(I D)=1, dim(D I)=2,
    I^2 D=0=D I^2,

whereas F^2 D has dimension five and F^3 D has dimension one.

This distinction comes from an actual lower-filtration source lift, not from choosing an arbitrary flag on a vector space.

## 1. Freeze which measurements are retained

The old union contains the 270 private scalar rows, the original four-sector test, the declared two-/sixteen-private tests, and the matched-optimal scalar test. The background-two vacuum generator itself is omitted before acquisition. The old first two stages remain fixed.

Crucially, the matched test is the declared signed common-waveform combination on 448 analytical blocks plus its reserved positive block. It is NOT a protocol retaining every analytical block as an independent observer coordinate.

The owning construction is `../grothendieck/matched-private-corrections-attain-the-full-cubic-observer-norm.md`. Its common test is positive on the actual windows, and its crossed gain is nonzero. These facts justify the nonzero scalar factors below. The checker does not replace them by numerical midpoints or arbitrary rational weights.

Independently retaining all implementation readings is a different observer. The subsequent audit `retaining-the-raw-matched-readings-reduces-the-vacuum-increment-to-six-states.md` matches the actual 449-row receiver manifest and obtains dimension six with filtration (6,5,1,0) for that protocol. The receiver requires the inputs but its return value alone does not specify whether callers archive them.

## 2. Interval notation

The canonical forgotten chain is

    a_0,...,a_6 = 2,4,12,60,420,4620,60060.

The full vacuum module V has the fifteen basis states z_(i,j), j-i>=2, dual to canonical contiguous-subword coefficients at corner (a_i,a_j).

Let W=Omega intersect Sat(chi_2). The previous audit established seven shared interval functionals:

    (0,2), (1,3), (1,4), (2,4), (3,5), (3,6), (4,6).

The new audit proves that exactly ONE further interval functional is shared:

    (2,5), at the actual corner 12->4620.

Therefore dim W=8 and D, identified with its annihilator inside V, has the seven interval basis states

    (0,3), (0,4), (0,5), (0,6), (1,5), (1,6), (2,6).

## 3. Why the matched test sees the extra shared corner

Prepend the path (2_retained,3_retained) to an entirely forgotten input in the corner (2,5), and append the forgotten event 13. The two retained windows are the fixed adjacent windows [2,4] and [4,12].

The exact signed matched-block sum on ALL six input path orders is

    2 * coefficient(5,7,11),

times the common nonzero window-pair response and the nonzero crossed gain. The reserved block and the other detector families contribute zero in this context.

Consequently this contextual old detector is a nonzero multiple of the new vacuum interval functional. It lies in W.

The equality is on the full source corner: an input with any retained mark has total degree greater than two after the fixed context and is killed by the homogeneous old test. It is not merely an equality on one source witness.

## 4. Seven actual old-invisible source lifts prove the complementary bound

For six of the remaining seven intervals, the canonical forgotten word minus the word with its first two events exchanged is an I-source with vacuum value one and zero old evaluation in every contributing context.

The checker tests the complete possible prefix/suffix contexts, retaining their marks and endpoints. At shorter corners it separately checks the original first and second stages. An old cubic context must supply exactly two retained marks; longer contexts do not fit.

The exceptional corner is (2,6), namely 12->60060. The naïve two-term source there is not old-invisible. The matched test on its 24 forgotten path orders is

    2 * [coefficient(5,7,11,13)-coefficient(5,7,13,11)],

again times the same nonzero common factor.

Instead use the actual three-term forgotten source

    h=(5,7,11,13)+(5,7,13,11)-2(5,11,7,13).

All paths have the same outer endpoints. Their coefficients sum to zero, so h lies in the forgotten terminal-record ideal I. Its new canonical vacuum coefficient is one. The signed matched test cancels exactly, and all other old contextual functionals vanish.

This cancellation is between the declared equal-window terms of ONE detector. Requiring every analytical block separately to vanish would incorrectly reject h and silently enlarge the old observer.

These seven old-invisible lifts have different source corners and new evaluation equal to the corresponding z_(i,j). Hence dim D>=7. Combined with the eight independent shared functionals, dim D<=7, proving equality.

## 5. Compute the inherited second and third levels

For the five intervals

    (0,4), (0,5), (0,6), (1,5), (1,6),

the checker constructs actual I^2 sources: two consecutive forgotten diamonds followed, where needed, by the remaining forgotten path. Their canonical coefficients are one and every old contextual detector vanishes. Thus these five states lie in F^2 D=D intersect I E^+.

The length-three interval (0,3) cannot receive an I^2 input, since every contributing ideal factor has at least two events.

The remaining state (2,6) also does NOT lie in F^2 D, for a different reason. On the complete minimal forgotten I^2 basis in this four-event corner,

    coefficient(5,7,13,11)=-coefficient(5,7,11,13).

The old matched contextual detector is therefore four times the canonical vacuum coefficient, up to its nonzero common factor. An old-invisible I^2 source must have zero new vacuum coefficient. Positive-feature source components cannot cancel this obstruction because the particular contextual old functional has retained degree zero on its input.

In particular h above cannot lie in I^2: its two displayed coefficients are both one. The state z_(2,6) has an I-valued lift but no old-invisible I^2-valued lift.

This proves dim F^2 D=5. Only the full six-event corner can contribute to F^3 D; the all-forgotten cubic product k_2 supplies its nonzero value. Hence F^3 D=span(z_(0,6)) and dim F^3 D=1.

## 6. Source actions and intrinsic powers

The module D is the indicated invariant submodule of the fifteen-state vacuum module. Its nonzero prime-edge actions are inherited from

    left(a_k->a_(k+1)): z_(k+1,j) -> z_(k,j),
    right(a_k->a_(k+1)): z_(i,k) -> z_(i,k+1),

whenever the displayed state belongs to D. All retained edges and off-chain edges act by zero. The artifact records the sparse maps.

Consecutive forgotten diamonds give

    I D=span(z_(0,6)),
    D I=span(z_(0,5),z_(0,6)).

Another ideal factor kills both images. Therefore the inherited depth-two and depth-three submodules cannot be reconstructed by taking intrinsic powers of I on D.

There is no contradiction with equal left/right ideal images for the WHOLE vacuum module V: passing to a submodule can break that equality. Nor is this a change in the previously declared inherited-filtration convention.

## 7. What this completes

The background-two acquisition is now specified by:

- its seven-dimensional restriction kernel with explicit source actions;
- the inherited flag (7,5,1,0);
- a source-action proof that E^+->E does not split;
- the continuing distinction between the nonzero acquisition extension and the adjacent class that remains filtered-nonzero but unfiltered-zero.

The exact count applies to the stated signed common-test protocol. The split background-three/four blocks may be present on both sides without changing this calculation because their supported source corners are disjoint.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_background_two_vacuum_increment_exact.py

The checker reconstructs the owning 270-column analytical-shape audit and matched-block signs; checks all relevant contexts and source path orders; solves and verifies the three-term annihilator; checks the complete minimal I^2 relation basis at the exceptional corner; and records the module actions and ideal images.

Artifact: `results/background-two-vacuum-increment-exact.json`.

No new norming coefficient is numerically fitted. Exact equal-window cancellation is used where blockwise vanishing is unavailable, and the owning positive common-window response supplies the required nonzero factor.
