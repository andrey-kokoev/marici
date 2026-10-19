# Global iteration 20 (new series 10/10): Picard-norm strata and the lifting gap

## Scoped result

Stay in the **conditional bielliptic-intermediate branch** of the previous audit. Fix a smooth degree-two map k:C5->Eprime with eight branch points, nonzero zeta in Pic0(Eprime)[2], eta=k^*zeta, and L in Pic0(C5)[4] with L^2=eta. It defines C17->C9->C5, where C9 is the elliptic two-isogeny pullback. Let b0 be the deck involution of k, and b the unique bielliptic involution on C9.

Of the 1024 marked root labels per fixed (C5,k,zeta):

| Nm_k(L) | Root labels | Lift behavior | Consequence for the fixed A isogeny class |
|---|---:|---|---|
| trivial | 256 | inverts the cyclic-four generator | excluded: primitive Prym is a square of fourfolds |
| zeta | 256 | commutes with the cyclic-four generator | not excluded here; the equal-factor square argument does not apply |
| either of the other two nonzero elliptic two-torsion classes | 512 total | b does not lift to C17 | not excluded here; there is no such dihedral decomposition |

Thus Nm_k(L) must be **nontrivial** for a realization in the fixed A isogeny class. The remaining 768 labels, or 384 inverse pairs, satisfy a necessary condition only. They are not actual target realizations or an unmarked cover-moduli count. The assertion that uniqueness of b forces it to lift is false in this family.

No biellipticity or theta-singularity dimension has been established for an actual Y2 realization. This table refines a conditional route; it does not exclude all Pryms or supply a cycle.

## 1. Norm kernel and why the four strata really have equal size

Use additive notation for Picard groups. Let J=Pic0(C5), K=k^*:Pic0(Eprime)->J, and N=Nm_k. The identities are

    NK=[2], KN=Id+b0^*.

K is injective. If K(T)=0, then 2T=0. A nontrivial such T defines an elliptic two-isogeny through which k would lift; since deg k=2, this would force a degree-one map C5->an elliptic curve, impossible at genus five. This also proves the earlier eta is nonzero.

Duality for abelian varieties makes N surjective with connected kernel P0 of dimension four. Consequently

    0 -> P0[2] -> J[2] --N--> Pic0(Eprime)[2] -> 0

is exact on complex points. For surjectivity on two-torsion explicitly: choose a preimage x of a two-torsion point; 2x lies in P0, so divide 2x by two in the connected abelian variety P0 and subtract that half from x. The resulting preimage is two-torsion.

The roots of 2L=eta form a J[2]-torsor of size 2^10=1024. As 2NL=NK(zeta)=2zeta=0, their norms lie in the four-element elliptic two-torsion group. Translation by J[2] maps onto that group with fibres P0[2] of size 2^8=256. Each norm stratum therefore contains exactly 256 roots, independently of a choice of coordinates or a particular lattice control.

All roots have exact order four. Inversion has no fixed root and preserves norm, since every norm is two-torsion. Each stratum has 128 inverse pairs.

## 2. Exact criterion for lifting the bottom involution

From KN=Id+b0^* one gets

    b0^*L=K(NL)-L.

An automorphism of C5 lifts to the connected cyclic-quartic cover defined by L exactly when it preserves its cyclic character subgroup: b0^*L=L or -L, since these are the two generators of <L>. This is the usual classification of connected cyclic etale covers by exact-order torsion line bundles; a scalar change of trivialization of L^4 makes no difference over C.

Since K is injective and 2L=K(zeta),

    b0^*L=-L iff NL=0;
    b0^*L= L iff NL=zeta.

The first lift conjugates rho to rho^-1. The second conjugates rho to rho. For the other two norm classes b0 has no lift normalizing the cyclic-four cover.

Here a lift can be chosen to fix a point over a branch point of k, because b0 has fixed points and C17->C5 is etale. Its square is a deck transformation fixing that point, hence identity. This rules out an unverified order-four lift with square rho^2. It does not extend this pointed argument to ramified top covers.

## 3. The unique intermediate bielliptic involution is not automatically liftable

Write p:C9->C5 for the etale double cover with class eta. The curve C9 has unique bielliptic involution b; it descends to b0. Its other lift of b0 is eta_deck b, which is free because it acts by nonzero two-torsion translation on the elliptic quotient. Thus the pointed lift in section 2 descends to b, not to that free involution.

Conversely, suppose b lifts to sigma on C17. Since b commutes with eta_deck, sigma rho sigma^-1 is a lift of eta_deck to C17. The only two such lifts are rho and rho^3, differing by the deck involution of C17/C9. Therefore sigma normalizes <rho> and descends to b0. The criterion in section 2 is necessary as well as sufficient for b to lift.

Equivalently, the line bundle of C17/C9 is p^*L. Its transform by b differs by p^*K(NL). The kernel of p^* on Pic0(C5) is precisely {0,eta}, giving the same criterion NL in {0,zeta}.

Hence b lifts on 512 roots and does not lift on 512 roots. Uniqueness of an involution on an intermediate curve concerns automorphisms of that curve; it does not imply invariance of an arbitrary double-cover class above it. The nonlifting half is a genuine obstruction to a universal lifting argument, not a rejection of those covers as potential Y2 realizations.

## 4. Norm-zero quarter is incompatible with X

For NL=0, the pointed involutive lift satisfies sigma rho sigma=rho^-1. On the primitive Prym P=Prym(C17/C9), rho^2=-Id, so

    sigma rho=-rho sigma.

The previous audit's actual abelian-image argument applies unchanged: P_+=im(1+sigma), P_-=im(1-sigma) sum isogenously to P, intersect in two-torsion, and rho identifies them. Both have dimension four. Thus P is isogenous to Q4 x Q4.

The fixed A=X6 x B2 contains simple X6, whereas Hom(X6,Q4)=0 by simplicity and dimension. Therefore these 256 roots cannot yield any P isogenous to A. No principal polarization or Gaussian-marking adjustment repairs that obstruction.

For NL=zeta the lift instead COMMUTES with rho. Rho need not exchange the two sigma-eigenspaces; the equal-fourfold decomposition is not licensed. For the other norm classes there is no lifted b to use at all. We do not carry the norm-zero contradiction into either remaining branch.

## 5. What the finite lattice computation does and does not establish

The checker uses one explicit primitive degree-two elliptic embedding in a symplectic rank-ten lattice, reduced modulo four. With coordinates (e1,f1,e2,f2,...), set

    K(a,b)=(a,2b,b,0,...),
    N(x)=(2x_e1-x_f2,x_f1).

Then NK=2, K is injective modulo four, K and N are symplectic adjoints, and B=KN-Id squares to identity. K(zeta)=(2,0,...,0) for zeta=(2,0). All 1024 formal root labels are enumerated and partitioned by norm; B(L)=+L, -L or neither has exactly the geometric case census above.

This is a control of the norm identities, embedding index and finite root accounting. The uniform geometric counts were proved in section 1 from connectedness of the norm kernel. We do not infer a general geometric theorem from one lattice example, claim a canonical marking, or identify these coordinates with actual algebraic torsion points of a supplied C5.

## 6. Remaining executable work

For a target realization in this conditional family, require NL nontrivial. Separate the commuting norm-zeta stratum from the two nonlifting strata. In the commuting case compute quotient genera and the polarization types of the resulting ramified-double-cover Pryms before using the retained sixfold determinant invariant; a generic principal-product or equal-factor assumption is not valid. The nonlifting half needs different geometry rather than that involution shortcut.

Actual theta singularities, actual curve/period matching and non-divisor cycles remain uncomputed. All four f-pullback exceptional channels remain required for any cycle proposal. Direct smooth-threefold/reflexive geometry on X and other Prym families remain available. The three unrestricted research obligations and independent review are still open; there is no Hodge verdict.

Contract: `research/conjecture_net/contracts/hodge-bielliptic-lift-audit.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_bielliptic_lift_audit.py`.
Receipt: `research/voevodsky/results/hodge-bielliptic-lift-audit-v1.json`.

    python research/voevodsky/checkers/check_hodge_bielliptic_lift_audit.py

Trust boundary: original written Picard-norm and complex covering argument importing standard norm-pullback identities, abelian duality, cyclic-cover classification and pointed lifting. Finite controls are not formal verification of those imports, actual target geometry or independent review. No new exhaustive literature claim is made. The iteration-19 predecessor and immutable pins v1-v20 are retained unchanged.
