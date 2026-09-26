# Common kinematics reveal a frame issue and a two-family obstruction

Freshly evaluated the50-term source P9 expression at the fork's actual quotient z=Z9[:,2:]-Z9[:,:2]B for e=1/2 and1. All source denominators are regular. No unrelated moment-curve evaluation is substituted. Exact target/tree/cell data are recorded in results/nine-point-common-frame.json.

## Frame audit

Let M=C h and F=C z, evaluated on a regular zero F=0. For source density rho and J=det(dF/dq), the localized delta-function supercoefficient for chi_i^4 chi_j^4 is rho*minor_ij(C)^4/J. Under constant C->G C, both J and the fourth-power minor scale by det(G)^4; the ratio is invariant. At constant G=2I the inherited extra det(C h)^4 multiplies by256, so the fork's current payload is not itself a representative-independent P9 coefficient unless an additional compensating density convention is specified.

Equivalently, the target chart Jacobian is J_B=J/det(M)^4 (up to the fixed flattening/orientation convention), while the normalized fermion row is M^-1 C. Its fourth-power minor contributes det(M)^-4. Those factors cancel. Combining J_B^-1 with the unnormalized minor instead retains the extra frame factor. This is a warning about interpreting the payload, not a claim that the existing fixed-chart barrier conservation tests failed. The source parameterization is fixed in those tests.

## Necessary fit against the physical tree

Using the explicitly unframed delta-function coefficients and the inherited per-cell orientations, form the3x2 matrix of zero2/zero3 EB+FB pair sums. Fit alpha,beta to the first two tree components (chi3^4chi5^4, chi2^4chi5^4). The remaining chi1^4chi5^4 component has a nonzero exact residual at BOTH e=1/2 and1. Thus even target-dependent choices of two family weights cannot match these three tree components in this convention. Missing contributions or a different geometric interpretation are required; simply selecting alpha/beta cannot finish the full amplitude.

Fresh commands: check_nine_point_common_frame.py and check_nine_point_two_family_fit.py under uv run --with sympy. Both diagnostic checks pass; three-component matching fails as expected and the exact residuals are retained. This does not identify the missing cells, validate inherited relative orientations independently, or prove an all-target identity.

Next derive/recheck the source-form-to-delta normalization on an ordinary five-bracket/known cell, and use the sourced50-history intersection representation as the full candidate rather than forcing the four-channel subset to be complete. A geometric derivation must explicitly map those histories to cells and orientations or supply a different complete contour.
