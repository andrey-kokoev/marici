# A concrete missing history and its cell

Fresh decomposition of the mixed component with flavor pairs(1,9),(2,8),(3,7),(4,6) finds exactly ONE nonzero term among the50 authored histories at BOTH common targets: outer(2,4), inner(6,8), right-nested, no boundary replacements. It is [9,1,2,3,4][9,5,6,7,8], with sourced coefficient+1. Exact missing coefficients are625/11743683969024 at e=1/2 and1369/19046322892800 at e=1. All four original zero2/zero3 cell tensors have zero coefficient here. A nonzero3x3 augmented minor is now recorded alongside the prior rank computation.

An explicit8-parameter cell representative for this term is

C = [[a1,a2,a3,a4,0,0,0,0,-1],
     [0,0,0,0,b5,b6,b7,b8,1]].

Every ordered2x2 minor is zero or a positive monomial when all eight parameters are positive. The gauge is fully fixed by the two row supports and column9. With ordered dlog coordinates(a1,a2,a3,a4,b5,b6,b7,b8), the localized bosonic Jacobian and full fermion wedge normalization agree exactly with the sourced R-product at both quotient inputs; no extra frame factor is needed.

IMPORTANT: the unique inverse coordinates at these particular common targets are NOT all positive (a3,b6,b8 are negative). Thus this is a positive cell whose rational canonical-form continuation supplies the missing tree history, NOT an additional positive source preimage at these targets. Do not insert it as an enabled positive barrier channel or infer a positive contour completion from this calculation. The distinction between algebraic rational-form sum and positive image coverage is now explicit.

Artifacts: results/nine-point-missing-support-histories.json and results/nine-point-missing-cell.json. Fresh checkers: check_nine_point_missing_support_histories.py and check_nine_point_missing_cell.py. Both pass, including the expected negative positivity result.

Next characterize the full sourced cell collection (including boundary-intersection cells), or first test whether the original four rational contributions plus this new history span additional tree components. The latter is a useful exclusion test, not a completeness proof. A physical contour interpretation must account for signed/algebraic continuation rather than demand every source history have a positive preimage at every target.
