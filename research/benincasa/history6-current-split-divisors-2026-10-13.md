# Pivot/normal covariance and physical contour — iteration 4

Freshly read pins v43, the normal-link receipt/current checker, and the owning source `invariant_top_form_section` (lines1058–1073). This turn classifies the split poles and derives the precise missing local contour-lift datum.

## Canonical versus weighted Plucker divisors

On the active labels (1,2,3,5,6,8), the canonical G(2,6) cyclic minors are p12,p23,p35,p56,p68,p81. With p81=-p18 recorded and the frozen positive orientation, their product and the actual eight-coordinate source Jacobian give exactly d8b/product(bi). This is an active-cell local calculation, not a new ambient n8 top-form residue certificate.

The split weights are the invariant cross-ratios

    g=p56*p38/(p36*p58), 1-g=p35*p68/(p36*p58),
    p36*p58=p35*p68+p38*p56.

Here p36=b5*b7*(b2+b3), p58=b6*b8*(b3+b4). Both are nonconsecutive minors in the active order. The canonical source has no pole on their generic zero loci; the split weights have opposite nonzero simple residues. Two explicit fixtures have all canonical cyclic minors nonzero, and only the relevant extra minor zero. Adjacent minors have opposite signs there, so these fixtures are not positive. In the nonnegative source closure, b2+b3=0 forces b2=b3=0 and b3+b4=0 forces b3=b4=0, each codim2 on the specified nonzero base localization. Thus the extra divisor is not a new positive codim1 boundary.

This matches the owning source's explicit statement in `cyclic_minor_top_form`: adding nonconsecutive-minor denominator factors introduces unwanted poles not in the canonical positroid boundary stratification. The localized weighted/current extension is therefore meromorphic decoration, not a sourced canonical-boundary theorem.

## Actual source chart covariance

For each extra-divisor fixture, all14 regular source pivots are tested; the singular pivot at the vanishing extra minor is excluded. In all28 tests the actual eight-dimensional free-entry Jacobian scales by det(H)^6, as does the product of six cyclic minors. The canonical source density agrees. Both split cross-ratios agree as exact rational functions, not as newly selected pole locations in each chart. A singular pivot cannot remove the genuine split pole that is visible in the regular C12 chart.

## Extra contour datum and descent obstruction

Forgetting the added central puncture induces the exact sequence

    0 -> Z[Cminus1] -> H1(P1 minus {0,-1,infinity})
      -> H1(P1 minus {0,infinity}) -> 0.

For the fixed undecorated source class represented by C0, all decorated lifts are C0+n*Cminus1, n integer. With the source normal orientation already checked, their split source periods are (1-n,n), total1. The two product-torus chambers are n0 and n1; canonical source periods and pivot covariance cannot choose between them. More generally the lift is a Z-torsor, not only a two-option radius choice.

Neither split period descends to undecorated source contour homology: each is nonzero on the central-loop kernel. Their sum does descend. This is a local contour-data obstruction, not a failed coordinate covariance law. It does not say that a physical contour must annihilate both splits; it says that split integration requires an additional oriented lift avoiding the decoration divisor, and physical admission needs owning-source compatibility for that lift plus the external constraint prescription. No physical n has been selected or fitted.

## Next executable continuation

Compare this explicit lift datum with the owning history boundary/residue word and normal orders. Construct conditional ordered-residue lifts and test exchange of deletion order and the second extra divisor p58; determine what local compatibility data must accompany any source-admitted physical choice. Source orientation alone must not be silently promoted into a selected radius hierarchy or winding.

Evidence: `checkers/check_history6_current_split_divisors.py`, `results/history6_current_split_divisors.json`. Fresh runs pass; scientific verdicts unchanged. Successor pins v44 and net/SCC checks are structural only. Global current gluing, ordinary blowdown seven-form and physical cycle admission remain open.
