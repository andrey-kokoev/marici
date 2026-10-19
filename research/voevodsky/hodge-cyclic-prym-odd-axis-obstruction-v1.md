# Global iteration 37 (fourth series 6/10): the odd elliptic axis excludes every exact principal etale cyclic-quartic realization of Y2

## Result and boundaries

The fixed naturally polarized Y2 cannot be the principal Prym of a smooth etale cyclic-quartic tower C17->D9->B5. Unlike iteration36, this obstruction does not require a tetragonal pencil on the top curve or the special ramified-trigonal auxiliary family. We derive preservation of **both** actual elliptic axes by every polarized automorphism of Y2, rather than assume it for a prospective deck generator.

The preserved degree-three axis would give a degree-six map from C17 to an elliptic curve, equivariant up to translation for an order-four elliptic automorphism. A fibre over a fixed elliptic point is an invariant effective divisor under the free cyclic-four curve action. Its degree must be divisible by4, contradicting6.

This does not exclude every smooth etale double-cover Prym, ramified presentations, arbitrary unpolarized K-isogenies, or polarized isogenies with a nonunit polarization multiplier. The auxiliary family and Schoen's auxiliary algebraicity result remain valid. No target cycle or Hodge verdict is supplied.

## 1. Compute the actual elliptic surface, including the joint lattice

The maximal connected elliptic isotypic subvariety B in Y2 has dimension2. It is intrinsic: Y2 is unpolarized-isogenous to the fixed simple X6 times E^2, and there are no nonzero homomorphisms between X and E. Thus every group automorphism of Y2 preserves B.

Read the existing actual composite Gaussian marking Tf, not just the two separate axis degrees. Its plus-axis column has support {1,7} and coefficients(1,-1). Its minus-axis column has support {6,8} and coefficients(2,1+i). (These are one-based coordinate labels.) The support sets are disjoint. In the respective vector planes, integrality of the plus column forces its parameter into Z[i]; integrality of the minus column forces its parameter into (1/(1+i))Z[i]. No mixed cancellation is possible across disjoint supports.

Hence the entire joint lattice, not merely its axis intersections, has Gaussian basis

    b_plus = Tf e7,
    b_minus = Tf e8/(1+i).

Each column is Gaussian integral and contains a unit in a disjoint coordinate. These facts prove saturation in the full lattice. Thus B is the **actual product** of its two connected elliptic axes, with no additional finite gluing between them. The minus axis is still a square-lattice elliptic curve; its parameter lattice was just rotated and rescaled.

The native Gaussian Hermitian restriction is diag(2,-3), with cross term zero. In holomorphic coordinates on the two physical elliptic curves the complex structure is standard on both, so the corresponding positive CM polarization matrix is

    H_B=diag(2,3).

The second sign changes because the native Gaussian action has opposite CM type on the minus axis. These are product elliptic line-bundle degrees2 and3, not a Smith-normal-form polarization type labelled(2,3).

It would be incorrect to enumerate all holomorphic polarized automorphisms using the indefinite native form diag(2,-3) while forgetting its non-scalar physical complex structure. As a complex abelian variety B is E_i x E_i with End(B)=M2(Z[i]); in those physical CM coordinates the form to preserve is positive diag(2,3).

## 2. Both axes are intrinsically preserved

A polarized automorphism of Y2 restricts to an element M of GL2(Z[i]) with

    M* diag(2,3) M = diag(2,3).

For its first column(a,b), the norm equation is 2 Norm(a)+3 Norm(b)=2. Thus b=0 and a is a Gaussian unit. Orthogonality then forces the first entry of the second column to be zero, and its second entry is another unit. Every such restriction is diagonal; **both actual axes are preserved**.

There are16 surface unitary automorphisms, and four with square minus identity. These are upper bounds on restrictions of Y2 automorphisms, not claims that all extend through its gluing to X or come from curves. The checker enumerates the entire bounded column set: positive weights at least2 and column norms at most3 bound real and imaginary integer entries by1. The written inequality is what makes this finite enumeration exhaustive. As a hostile control equal weights(2,2) give32 unitary matrices, including axis exchange; diagonal preservation is not inferred for arbitrary product polarizations.

Now suppose a smooth curve C has an order-four automorphism rho, with h=rho^2 acting freely, and its natural principal Prym P(C/C/h) is the fixed Y2. The induced polarized group automorphism rho_P on P satisfies rho_P^2=-Id. No K-equivariance of the hypothetical ppav identification is needed. After any such identification it preserves both axes by the intrinsic argument above, and on either elliptic axis it acts by i or-i. In particular it preserves the actual theta-degree-three axis E_minus.

This resolves, for this target and this comparison, the previously explicit missing axis-preservation gate. We have proved it, not silently added it as a hypothesis about a selected curve map.

## 3. Norm-adjoint degree and affine equivariance

For a smooth etale double cover C->D and its natural principal Prym(P,Xi), the inclusion I:P->J(C) has I^*Theta_J=2Xi. Let e:E->P be an elliptic inclusion of theta degree d and let e^dagger be its polarization adjoint. The Abel-Prym map alpha:C->P induces I^dagger on Jacobians. For

    phi=e^dagger alpha:C->E

we obtain

    phi_* phi^* = e^dagger I^dagger I e = 2 e^dagger e = [2d].

Thus phi is nonconstant and deg(phi)=2d. This is the same norm-adjoint calculation retained in the earlier axis gate, now applied to d=3 as well as d=2. It gives degree6, not the degree of the polarization homomorphism of E or the old axis-source isogeny.

Since rho_P preserves e(E), write rho_P e=e u with u=+/-i. Polarized adjoint compatibility gives e^dagger rho_P=u e^dagger. The choice of basepoint in alpha contributes a constant, so

    phi(rho x)=u phi(x)+c.

We do not discard c or assume a rigidified theta line bundle. The affine elliptic automorphism A(z)=u z+c has fixed points because 1-u is a surjective degree-two isogeny. It has order4. Take any fixed point z0.

## 4. An invariant fibre contradicts the odd axis

The effective fibre divisor phi^*(z0) has degree6. Equivariance makes it invariant under rho. Since h has no fixed points, neither rho nor rho^3 has a fixed point, so the full cyclic-four action on C is free. Every support orbit of the divisor has length4. Multiplicities are constant along an orbit, even at ramification points of phi. Therefore

    4 divides deg(phi)=6,

a contradiction.

This proves exclusion of **all exact natural principal smooth etale cyclic-quartic Prym presentations of the fixed Y2**. It does not merely eliminate the iteration35 family. No top or intermediate gonality, theta-singularity dimension, moduli dimension or assumed deck preservation of an arbitrary axis was used.

A mere etale double-cover presentation need not lift Y2's order-four automorphism to a curve automorphism squaring to the deck involution; it is not excluded. For ramified cyclic towers the curve action is not free and the orbit-divisibility step is unavailable. We do not transfer this contradiction to those problems.

## 5. Quantitative gate for the still-open unpolarized K-isogeny route

Suppose instead a natural etale cyclic-four Prym P admits an **actual K-equivariant isogeny** to Y2. The connected inverse images of the two target axes are elliptic curves invariant under the source deck action, with its restrictions i and-i. Let their degrees for the **source natural Prym polarization** be d_plus,d_minus. The same fixed-fibre argument gives

    4 divides 2d_plus and 2d_minus,
    hence both d_plus,d_minus are even.

They need not equal the target degrees2,3: neither an unpolarized isogeny nor one with f*theta2=nXi for n>1 preserves those degrees. No actual source axes or matching isogeny are produced here.

For the specific auxiliary family of iteration35 we can sharpen this conditional gate to d_plus,d_minus>=4. If either degree were2, its degree-four elliptic map together with the existing degree-four orientation pencil would trigger iteration36's unique-low-genus-quotient proof. That proof after supplying the two maps uses only the unpolarized isogeny decomposition X6 x E^2, freeness and the simple sixfold rigidity; it does not otherwise require principal equality with Y2. It would again force X to be a forbidden primitive cyclic-quartic sixfold. Thus degree2 is unavailable for any invariant elliptic curve under this hypothetical isogeny, leaving even degrees at least4 and curve-map degrees at least8.

This is a necessary condition, not an existence theorem, a census of axes, or exclusion of every K-isogeny. Direct period/isogeny/factor data would still be needed to exploit Schoen's auxiliary cycles. Other principal models, genuinely ramified sources without this free-action obstruction, different objects, restricted deformation theorems and direct cycles remain executable.

## Verification and trust

Contract: `research/conjecture_net/contracts/hodge-cyclic-prym-odd-axis-obstruction.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_cyclic_prym_odd_axis_obstruction.py`.
Receipt: `research/voevodsky/results/hodge-cyclic-prym-odd-axis-obstruction-v1.json`.

Fresh inputs: actual Y2 marking/axis/polarization receipt; norm-adjoint/tetragonal gate; and the previous auxiliary principal-match/quotient proof for the conditional degree>=4 refinement. The checker computes joint-column saturation controls, native and physical restrictions, all possible surface unitary matrices, square-minus-one restrictions, equal-weight countercontrols and exact orbit-degree parity. The universal arguments also import standard isotypic decomposition, elliptic CM endomorphisms, adjoints and equivariant fibre divisors; finite arithmetic alone does not certify them. No proof-assistant verification or independent review is asserted.

Iteration36 and immutable pins v1-v38 are retained. Fixed X, alpha, Y2 and all cycle transfers and prior target censuses are unchanged. The natural principal etale cyclic-quartic presentation route is now closed for Y2, not the unrestricted cycle/isogeny research problem. No theta dimension, target exceptional cycle, all-cycle theorem, nonalgebraicity conclusion or Hodge verdict follows.
