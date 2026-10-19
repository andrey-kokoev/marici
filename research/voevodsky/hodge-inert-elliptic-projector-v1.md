# Global iteration49, fifth series8/10: an inert-prime polarization obstruction

## Result

The former two-prime survivor a=-24 is now excluded EVEN UP TO UNPOLARIZED complex Y3 isogeny. More generally, algebraic scalar parameters integral at a place over13 with residues(lambda,a,b)=(2,2,2) or(2,2,11) are excluded. This is not an inference from a missing CM factor: the relevant reduction HAS exactly one extra opposite-type E_i.

Its Frobenius eigenspace instead has a3-integral self-adjoint projector. Any primitive complex opposite-type axis, if it exists, must therefore have theta degree prime to3. The known first axis has theta degree4. Their determinant parities, together with the principal source and the fixed target End/norm-class data, give a contradiction to any target isogeny. No complex axis is lifted, and the isogeny is not assumed K-linear or polarization-preserving.

The CRT exclusion count on the fixed lambda2,b2 integral a-line rises from197 to201 classes mod221. Joint survivor197 is removed;214 remains. Three formerly uncertified classes are also removed using the new13-certificate, leaving19 uncertified classes NOT excluded. The actual a=-7 source remains unresolved.

## 1. Fresh polynomial input and exact projector

Rerun the iteration48 checker, including all finite-field kernels, the complete CM and native-type certificates and independent small counts. In its(a,p)=(2,13) case the sevenfold i-character polynomial f7 has precisely one CM root

    gamma=-2-3i=-i*conjugate(beta), beta=3+2i.

This is the only opposite-type geometric elliptic factor in the complement. The first known axis contributes beta. Hence the principal eightfold's Gaussian characteristic polynomial is

    f8(T)=(T-beta)*f7(T)=(T-gamma)*r(T).

The source principally polarized P8 is isogenous to the ramified Prym used in counting; this preserves its rational Gaussian characteristic polynomial. At the lattice prime3, the two-primary ramified-to-principal comparison is harmless.

Exact Gaussian polynomial arithmetic gives

    d=r(gamma)=f8'(gamma)=-14400-73600i,
    Norm(d)=5624320000,
    d mod3=2i, a unit of F9.

Therefore e(T)=r(T)/d is integral over Z_3[i]. In Q(i)[T]/f8 the checker verifies

    e^2=e,  T*e=gamma*e,  trace_K(e)=1,
    e^dagger=e, where T^dagger=13/T and i^dagger=-i.

The last identity is computed EXACTLY, not deduced merely from a small modular remainder: invert T using f8's nonzero constant coefficient, substitute13/T and conjugate all Gaussian coefficients, and reduce modulo f8. The receipt retains r, d, all rational projector coefficients, their F9 reductions and exact identity flags. Trace is computed from the regular representation of multiplication by e, proving Gaussian rank1. The conjugate orientation above13 is checked as well; derivative integrality does not depend on the chosen square root of-1.

For comparison, residue a6, relevant to the remaining a=-7 source, gives

    gamma=3-2i,
    f8'(gamma)=-22080+4320i,
    Norm=506188800, v3(Norm)=2.

Its rational projector is idempotent and self-adjoint but NOT3-integral. That test is INCONCLUSIVE about its primitive theta degree: a nonunit derivative does not prove a nonunit degree. The new obstruction is not applied to that source.

## 2. Local self-duality forces a unit elliptic degree, conditionally

Let O=Z_3[i];3 is inert and disc(Z[i])=-4 is a3-adic unit. The principal source's Tate module L=T_3(P8) is free of rank8 over O. Its polarization gives a perfect Hermitian lattice, equivalently the perfect alternating Weil pairing with the native unitary Gaussian action. Frobenius has Rosati adjoint13/Frobenius.

The integral self-adjoint idempotent e splits this lattice orthogonally:

    L=eL orthogonal-sum (1-e)L.

Each summand is perfect: for a perfect pairing and an integral orthogonal direct sum, both restricted Gram determinants are units. The summand eL has O-rank1.

Now suppose a primitive opposite-action complex elliptic subvariety E_- exists in the algebraic source. It and its embedding descend after a finite number-field extension. All subquotients of a good-reduction abelian variety have good reduction after this extension. The prime-to13 Tate lattice of a primitive abelian subvariety is saturated and specializes with the restricted polarization. Equivariant Hom specialization and the COMPLETE native-type certificate force the reduced E_- into the UNIQUE opposite-type elliptic summand. Its Frobenius after a finite extension is gamma^m; no other root can differ from it by a root of unity. The known beta-axis is not opposite type, and beta/conjugate(beta) is not a root of unity. Consequently

    T_3(E_-)=eL.

The restriction of the principal polarization to this primitive elliptic subvariety is therefore3-unimodular. Its theta degree d_- satisfies v3(d_-)=0. The degree is unchanged under good specialization. This is a CONDITIONAL implication, not construction or lifting of E_-.

The argument uses the special fibre's integral Frobenius action only on the SOURCE; no reduction or field of definition for the fixed transcendental-period X6 is assumed. It is stronger than using only the rational characteristic polynomial to count factors, but the extra input is still only an exact polynomial projector acting integrally on a principally polarized Tate lattice.

## 3. Why the unit degree excludes even an arbitrary unpolarized target isogeny

Retain the fixed data already used in the principal-model rigidity arguments:

* Y3 is unpolarized-isogenous to X6 x E_i^2;
* X6 is simple, End^0(X6)=K=Q(i), with signature(3,3);
* its raw Hermitian determinant class is-3 modulo Gaussian norms;
* the scalar source is principal, of native K signature(4,4), with primitive first axis of degree4.

Assume, for contradiction, that this source is unpolarized-isogenous to Y3. Its intrinsic sixfold isotypic factor is then isogenous to X6. Transport the SOURCE's native K action through the isogeny; this does NOT assume agreement with the target's preselected K action. On the simple sixfold the transported field embedding is identity or conjugation, because End^0(X6)=K. Both have signature(3,3). The elliptic-isotypic surface must therefore have signature(1,1). This forces an actual opposite-type elliptic subvariety in the source, in addition to the known first positive-type axis, exactly as in iteration48.

The two elliptic axes are orthogonal for the K-invariant polarization. Indeed an off-diagonal homomorphism between the same physical CM elliptic curve with native actions+i and-i changes sign under polarization invariance, so it is zero. Their raw Hermitian degrees are4 and-d_-. Both have even valuation parity at3 (in fact valuation0).

The full source's principal Hermitian determinant has3-valuation0. In a rational K-basis adapted to the sixfold and two axes, determinant multiplication holds up to a Gaussian norm of a basis determinant. At an inert prime every Gaussian norm has EVEN valuation: if z=3^v*u with u a unit in Q_3(i), then v3(Norm(z))=2v. The checker verifies anisotropy of a^2+b^2 over F3, the residue-field fact behind this formula. Thus

    v3(det H_source_sixfold)
       = v3(det H_source)-v3(4)-v3(d_-) = 0 mod2.

Finite joint-axis gluing need not be computed: rational changes of K-basis alter this parity only by a norm. No separate-axis saturation assumption is substituted for a computed joint kernel.

But a sixfold isogenous to the fixed X6 has determinant valuation ODD at3, for ANY polarization and either K embedding. To see why the polarization cannot be adjusted to evade this: End^0(X6)=K and Rosati is conjugation, so its symmetric endomorphism space, hence NS_Q, is one-dimensional. Any two polarizations differ by a positive rational scalar. Rescaling a sixfold Hermitian form changes its determinant by the SIXTH power of that scalar, which has even3-valuation. A K-isogeny changes it by a Gaussian norm, also even; conjugating K replaces H by-bar(H), preserving determinant in dimension6. The retained class-3 therefore always has odd valuation. Contradiction.

This is not an illegal transfer of a ppav obstruction along an unpolarized isogeny. We explicitly allow arbitrary polarizations on the simple factor and prove that none changes the required parity. It critically uses the EXACT fixed End field, its even dimension and its determinant class. Without these hypotheses only the conditional axis-degree statement is proved. It does not exclude an arbitrary sixfold target or an arbitrary unpolarized K-abelian eightfold.

In particular the expected opposite theta-six axis, whose degree has odd3-valuation, cannot occur here. The stronger sixfold-norm argument excludes target isogeny even without requiring that exact theta-six polarization.

## 4. Algebraic boxes, control and updated frontier

For algebraic integral(lambda,a,b) reducing to(2,2,2) or(2,2,11) at a place over13, the known branch conditions are units, so the relative scalar source, its principal cyclic Prym and native action have good reduction. For the sign pair, the actual V isomorphism(p,w)->(-p,i*w) commutes with native action, preserving the projector certificate. If the orientation of i is conjugated, conjugate the entire Gaussian certificate; integrality and determinant parities are unchanged. The first primitive axis remains degree4. Apply the conditional-then-contradiction argument to obtain the exclusion. Arbitrary transcendental coefficients are not covered by this descent/specialization assertion.

Literal(2,-24,2) has residue a2 at13 and is consequently excluded. Its actual source construction and first theta-four axis are NOT invalidated; this is a target mismatch, not a failure to construct the auxiliary variety.

On the fixed lambda2,b2 integral a-line, union this veto with iteration48's CRT sets. The newly excluded residues mod221 are

    54,80,158,197.

Three came from the previous uncertified set;197 was a joint CM/type survivor. The updated disjoint classification is

    201 excluded; joint necessary survivor214;19 uncertified.

The certificate retains all arrays and checks their complete disjoint union. Other parameters and the19 uncertified classes remain open; the one joint survivor is NOT a complete classification of complex sources.

The actual remaining control is(2,-7,2), in residue214. Its13/a6 projector is nonintegral, so this gate leaves it unresolved. The attempted next split prime29 fails the DISPLAYED model certificate: D and F0 have a common factor. This alone is not a complex exclusion. Prime37 passes all extended branch conditions and is an executable next Frobenius test. No third-prime Frobenius polynomial has been computed in this turn. An alternative continuation is to construct an actual opposite-action elliptic map and determine the primitive degree, joint kernel, sixfold End/simplicity and fixed-X6 periods/correspondences. Target denominator768/four-channel transfer, other scalar parameters, compactified/uncertified charts, birational genus-five-image and direct-cycle routes remain open.

Contract: `research/conjecture_net/contracts/hodge-inert-elliptic-projector.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_inert_elliptic_projector.py`.

Trust: fresh inherited complete finite-field data; exact Gaussian projector/Rosati algebra; written self-dual Tate-lattice, saturated specialization and conditional isogeny/norm arguments; retained actual-source primitivity and fixed-target End/norm rigidity. These are not proof-assistant-certified or independently reviewed. Iteration48 and pins v1-v51 remain immutable. No positive Hom lift, source End calculation, global family exclusion, target cycle or Hodge verdict is supplied.
