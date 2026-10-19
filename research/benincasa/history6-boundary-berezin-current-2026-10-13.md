# History6 — lower-degree direction-retaining boundary Berezin current

At the operator's request, construct a lower-degree map rather than reapply the degree-eight top extractor to a seven-form. Freshly read the source Grassmannian integral and dimension rule in `1212.5605/positive_grassmannian_update.tex`, equations `general_on_shell_function_momentum_twistors` and the following degree discussion. Its k=2 kernel imposes eight bosonic and eight fermionic constraints. A seven-dimensional source boundary therefore has graded bosonic degree7-8=-1, not an ordinary generic superfunction.

## Local normalization and actual incidence Jacobian

In the existing F6 C12 gauge write C=(I2|X(b)), active labels (1,2,3,5,6,8). The exact ordinary source Jacobian is

    det(dX/db)=b5*b6*b7*b8.

Fix an invertible four-column external bosonic block M at active labels (3,5,6,8). The other two columns encode Xstar(z), and the constraints read

    C z^T = (X-Xstar)*M^T.

Their ordered eight-constraint Jacobian is

    J = det(M)^2*b5*b6*b7*b8.

Two independently constructed incidence fixtures (M=I4 and diag(2,3,5,7)) verify this actual Jacobian at the regular b3 boundary. No bosonized positive six-vector fixture is substituted for these four-dimensional external incidence data.

Use algebraic **holomorphic constraint currents**, normalized by delta(A nu)=det(A)^(-1)delta(nu), with fixed ordered normal symbols. These are not real Dirac measures: there is no absolute-value Jacobian and no unspecified real integration contour.

Let

    N(Cstar,chi)=product_A((Cstar chi)_1^A wedge (Cstar chi)_2^A)
               =[phi_top]det_2(phi*Cstar*chi)^4/2880.

The universal normalized identity from the generic top bridge applies to all fermionic components. The checker additionally executes the actual exterior-algebra operator for the chi1/chi8 component (giving b8^4), rather than declaring a scalar selector to be a boundary map.

## Regular degree-seven boundary

Let nu3=b3(Cstar(z)) be the external kernel inverse normal. On b3=0 with b2,b4 and other parameters nonzero, the localized boundary current is

    E7(K0)=0,
    E7(B22)=delta(nu3) * N/(product_{i!=3} bi * J)|nu3=0.

This agrees with taking the coefficient residue of the normalized top incidence expression after supplying dnu3. The codomain is a fermionic-degree-eight external **codimension-one constraint current**, not an ordinary function. Its graded degree0-1 equals7-8. Source deletion parity for b3 is +1 and the normal convention is explicit.

## Exceptional direction-retaining map

At nu2=nu3=0 retain rho from b2=rho*T,b3=T. Integrate only the six base variables, not rho. The codomain is an external codimension-two current valued in meromorphic one-forms of the retained direction. With normal order delta(nu2)delta(nu3), define

    A = N/(b1*b4*b5*b6*b7*b8*J)|center,
    E7(K0) = -A delta(nu2)delta(nu3) drho/[rho(1+rho)],
    E7(B22)= -A delta(nu2)delta(nu3) drho/(1+rho).

The minus sign comes from moving rho ahead of b1 in the frozen source exceptional order (b1,rho,b4,b5,b6,b7,b8). No fitted residue or fiber average is used. Its graded degree is1-2=-1, equal to7-8, while fermionic degree remains eight and the Berezin factor remains2880. Thus source dimension, constraint codimension and surviving fiber degree are accounted for separately.

Actual normalized fermionic/current coefficient checks pass at both incidence fixtures. Directional residues at rho0,rho-1,rho-infinity reproduce the prior signed table (-A,0),(+A,-A),(0,+A). The extra rho=-1 pole remains meromorphic, not a positive physical boundary. The full three-direction sums vanish; positive endpoints alone still leave opposite nonzero split sums. The ordinary blowdown exceptional seven-form is still unavailable, not zero.

## Scope and continuation

This constructs a **localized holomorphic incidence-current extension** of the sourced Grassmannian delta integral, with a defined direction-retaining codomain and normalization. It is not a claim that the source paper already supplies an ordinary negative-degree on-shell function, nor a globally glued contour/current cycle, ordinary bosonized seven-form, superamplitude theorem or weighted-sector map. The target/codomain change is explicit rather than hidden behind top Berezin extraction.

Next: verify source/kernel pivot and external normal-coordinate covariance, including all determinant and orientation factors, before gluing the local current maps or identifying a physical boundary contour. Scientific net verdicts remain open outside this scoped construction.

Evidence: `checkers/check_history6_boundary_berezin_current.py`, `results/history6_boundary_berezin_current.json`. The initial implementation used a four-by-six external matrix without transposing it in C*z; fixing the dimensional convention to C*z^T yielded a passing fresh rerun without changing the map or coefficients. Successor pins v40 and structural net/SCC checks are distinct from the actual Grassmann/Jacobian/current calculation.
