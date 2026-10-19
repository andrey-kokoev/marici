# Pivot/normal covariance and physical contour — iteration 1

Freshly read the local boundary-current checker/receipt and active work-net (pins v40). This turn establishes local covariance, without treating that as contour admission.

## Kernel frame and source-pivot covariance

For Cprime=H(b) C, every sector fermionic two-form scales by det(H); hence the full degree-eight numerator scales by det(H)^4. The ordered eight bosonic constraints transform by H tensor I4, whose determinant is also det(H)^4. At incidence support C z=0, the derivative term dH*(C z) vanishes, so the actual constraint Jacobian has the same transformation even when H depends on source coordinates. Consequently Nprime/Jprime=N/J for every fermionic component, not only a chosen scalar.

The checker proves the generic row-frame law symbolically and tests every unordered active source pivot on two actual incidence opens:

- regular b3 boundary: 14 regular pivots, 1 singular pivot excluded;
- exceptional b2=b3 center: 12 regular pivots, 3 singular pivots excluded.

Three actual varying-pivot derivatives per open agree independently with the support transformation law. Reversed pivot order and a frame with determinant -2 preserve the full kernel ratio. Omitting the fermionic determinant factor gives retained nonzero hostile defects. Singular gauge patches are not assigned zero currents or implicitly included in overlap coverage.

## External normal and direction covariance

These local currents are density-valued in their normal frame. For regular w=a*nu+O(nu²), delta(w)=delta(nu)/a on support, so the coefficient must transform by a. Positive, negative and tangentially varying nonzero scale controls pass; omission produces nonzero defects.

For exceptional normal vector nu=(nu2,nu3), w=A nu, det(A)!=0, the normal-induced blowup direction changes by

    rho_prime=(a*rho+b)/(c*rho+d).

The new one-form coefficient is

    det(A) * f(rho(rho_prime)) * d rho/d rho_prime,

and the ordered constraint current transforms as delta(w)=delta(nu)/det(A). Their pullback is exactly the original current. Three frame controls include an orientation-reversing normal swap, an anisotropic signed scaling, and a mixing frame. Each K0/B22 current agrees rationally after both factors are included. Omitting the normal determinant gives nonzero defects.

A reciprocal direction change with fixed normal order is different from swapping the two normal coordinates: the latter also has a delta-frame minus sign. These signs are explicitly retained rather than fitted from residue cancellation. Coordinate changes do not admit a new positive direction or physical contour.

## Physical contour gate and next action

The local pivot/normal tests do not choose a global integration cycle. A physical contour still needs sourced winding/orientation data around rho=0,-1,infinity and compatibility with the external constraint/normal prescription. The extra rho=-1 pole remains nonpositive; adding it merely to force split closure is not allowed. The ordinary blowdown seven-form remains unavailable.

Next executable turn: construct the punctured-direction contour/winding lattice, compute its K0/B22 residue pairings with the retained meromorphic table, and distinguish algebraic closure from source admission. Compare the owning contour prescription without choosing a physical cycle from a desired zero.

Evidence: `checkers/check_history6_current_covariance.py`, `results/history6_current_covariance.json`. Scientific node verdicts unchanged; successor pins v41 and structural net/SCC checks are separate from these covariance computations. Completion/no-continuation is not reached.
