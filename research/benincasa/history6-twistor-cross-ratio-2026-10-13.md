# History6 endpoint/boundary iteration 4 — intrinsic projective coefficient

Freshly read the incidence/projection checker, owning twistor constructors and work-net (pins v30). The successor now derives, rather than guesses from projection tests,

    c6 = 1 - <6812><5123>/(<5812><6123>).

Let W=(56) intersect (812), with the owning representative

    W = Z5 <6812> - Z6 <5812>.

Write b=-<5812> for its Z6 coefficient. The transported upper endpoint k(ut) is projectively the spinor projection of W. On the line (56), the evaluator's endpoint sandwich S has the same ratio as the plane covector V -> <V123>. Therefore

    A0/At * St/S0 = <W123>/(b <6123>)
                  = 1 - <6812><5123>/(<5812><6123>).

## Symbolic proof and localization

On the <12> != 0 spinor patch, translate x2 to zero and choose the spinor basis lambda1=e1,lambda2=e2. Translation leaves all dual x differences fixed; a spinor basis change multiplies endpoint A/S evaluations by common canceling factors. Z3,Z5,Z6,Z8 are otherwise unrestricted four-vectors (sixteen independent symbolic components). Incidence reconstructs x3 from (23) and x6 from (56); <8|x8=-mu8^T eliminates x8 and Z7. The checker proves exactly:

- det[k(ut),P(W)]=0;
- S(lambda5)<6123> - S(lambda6)<5123>=0;
- source endpoint ratio minus the bracket expression is the zero rational function.

The formula reproduces all three prior exact fixture ratios. Each bracket acquires det(G), while each individual twistor label has balanced weights in the cross-ratio term. Thus the explicit rational coefficient is GL4/projectively invariant on its domain; this is not merely the preceding bounded projection screen. Original incidence and generalized-R localization remains required. This formula does not repair the earlier singular rho1 incidence frame or admit an ordinary untransported canonical seed.

## Candidate target-dependent boundary coefficient

For the four-dimensional quotient by a bosonized target two-plane Y, the intrinsic expression specifies

    c6(Y,Z) = 1 - <Y6812><Y5123>/(<Y5812><Y6123>).

This is now an explicit rational function of Y and external six-vectors, invariant under the Y row frame and external projective rescaling. It is **not externally fixed in Y**. The previous independent-spinor/Z coefficient-module squares remain scoped predecessors, not residue evaluations for this new function.

Next executable step: pull this quotient coefficient back to the actual positive F6 source chart, inspect its reduced and original localization at b2=b4=0, and compute its iterated Laurent residues and any cross terms. A defined quotient function alone is not a boundary-supercomponent extraction theorem; compatibility with the physical selector and complete weighted map remains open.

Evidence: `checkers/check_history6_twistor_cross_ratio.py`, `results/history6_twistor_cross_ratio.json`. Scientific verdicts unchanged; successor pins v31 and structural net/SCC validation are separate. The physical boundary extraction objective still has a nonredundant continuation.
