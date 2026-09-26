# Boundary-updated history now has a checked positive cell

Freshly validated the candidate for outer(2,4), inner(4,6), right-nested with lower boundary replacement:

C1=(a1,a2,a3,a4,0,0,0,0,-1),
C2=(0,0,a3*b3,a4*b3+b4,b5,b6,0,0,1).

Every ordered2x2 minor is symbolically zero or a polynomial with positive coefficients. In particular minor23=a2*a3*b3, so the new cell supplies the support absent from the earlier five cells. The ordered8-variable dlog measure is calibrated without an inferred sign: its localized Jacobian coefficient agrees with the sourced R-product, with normalization ratio exactly1 at four rational inputs. All36 fermionic wedges agree up to the compensated fourth-power scale.

Inputs comprise both existing common targets, a4D moment curve, and an independently constructed positive image: use6D moment-curve external data and source parameters(1,2,3,4,2,3,4,5). The inverse reconstruction recovers exactly these positive parameters, with nonzero Jacobian2282486169600/841. This demonstrates a regular positive-image example rather than only positivity of formal parameters.

At the original two common targets, inverse parameters are still not all positive, and this remains recorded rather than suppressed. Rational-form comparison and positive-image membership are distinct. No barrier channels were modified.

Reproduce: uv run --with sympy python research/voevodsky/checkers/check_nine_point_boundary_cell.py. Result: results/nine-point-boundary-cell.json.

Next generalize the construction to the15 right-nested authored histories, distinguishing unshifted and lower-boundary cases. The disjoint support rule gives the unshifted cells; at inner lower endpoint equal to the outer upper endpoint, replace the boundary column by the transported combination of the final two outer columns. Check overlapping-support gauge choices carefully: repeated explicit endpoints need combined entries, not overwrites. Left-nested histories and upper boundary replacements remain a separate35-history obligation. Two calibrated cells do not establish a complete contour.
