# Global iteration 24 (third series 4/10): full automorphisms of the asymmetric control

## Result

The preceding explicit asymmetric genus-seventeen curve C17 has

    Aut(C17 over C) = C4 x C2,

with the known cyclic-four elliptic-isogeny translations and the double-cover sheet involution. In particular there is no dihedral order-eight curve action. This strengthens the previous **fixed-origin** nonlift to all translated elliptic inversions and determines the entire auxiliary curve automorphism group.

This is NOT an endomorphism-algebra computation for the primitive Prym. It does not prove its simplicity, exclude an abstract fourfold-square isogeny/correspondence, identify it with Y2 or compute theta singularities. No conditional root count or Hodge verdict changes.

## 1. A finite bound on every possible center

On Eprime: y2^2=x2(x2-1)(x2-25), let B be the eight distinct zeros of s=x2^4+y2-2. The preceding exact norm certificate proves smoothness and disjointness from elliptic infinity. Since

    div(s)=B-8O,

its elliptic group sum is zero. If a translated inversion j_A(Q)=A-Q preserves B, its image divisor has sum 8A-sum(B). Thus 8A=0. Likewise any translation t_A(Q)=Q+A preserving B has sum sum(B)+8A, so again 8A=0.

Consequently every possible inversion or translation center belongs to the finite 64-element group Eprime[8], even if the initial automorphism is considered over C rather than over Q. This necessary condition, not an arbitrary search cutoff, makes the following finite test exhaustive.

## 2. Good reduction and why one prime suffices here

Use p=409. The elliptic curve has good reduction (p is not 2,3,5). The branch polynomial

    B0(t)=t^8-4t^4-t^3+26t^2-25t+4

is squarefree modulo p and coprime to t(t-1)(t-25). Therefore the eight-point branch scheme remains finite etale and disjoint from elliptic infinity and two-torsion.

Exact enumeration gives #Eprime(F409)=384. Exactly 64 of these rational points are killed by eight, using the elliptic doubling formulas. In characteristic prime to eight there are exactly 8^2 geometric eight-torsion points, so **all** geometric Eprime[8] points are among these rational points. This is not merely an enumeration of the rational subset of a potentially larger torsion group.

At good reduction, prime-to-p torsion is finite etale and its specialization identifies the geometric eight-torsion groups. Any characteristic-zero preserving center is algebraic torsion, extends over a suitable good-reduction local ring, and specializes to one of these 64 points. Equality of the finite branch divisors under its translation/inversion persists on the good special fibre (equivalently take their closures in the smooth proper elliptic model). Thus nonexistence for all 64 special-fibre centers rules out every characteristic-zero center.

This proof uses the group-sum bound, good branch reduction and prime-to-p torsion specialization. It is not the invalid claim that finitely many point samples or a single arbitrary reduction settle an unrestricted complex automorphism search.

## 3. Exact residue certificates without choosing branch roots

Work in the reduced degree-eight branch algebra

    R=F409[t]/B0(t),  Q=(t,-p4(t)), p4=t^4-2.

At all nonidentity torsion centers A=(a,b), t-a is a unit: B0(a) is nonzero, checked for each center. For inversion use -Q=(t,p4) and set

    m=(p4-b)/(t-a),
    xnew=m^2+26-a-t,
    ynew=-b+m*(a-xnew).

These are the elliptic coordinates of A-Q. Reduce xnew^4+ynew-2 in R. Every one of the 64 inversion residues is nonzero, including the identity-center residue 2p4. Since the branch algebra is reduced, a nonzero residue means at least one geometric branch point is not sent into B. No inversion preserves the divisor.

For translation replace p4 in the slope numerator by -p4, representing Q rather than -Q. Exactly the identity-center translation residue is zero; the other 63 are nonzero. Hence the translation stabilizer of B is trivial.

The receipt retains every center and both polynomial residues. Euclidean inversion of every denominator is checked by multiplication in R. Coordinates and residues can be recomputed with only integer modular arithmetic; no factorization field or approximate branch roots are used.

## 4. Push the stabilizer restriction through the isogeny

The preceding cyclic-four isogeny psi:E->Eprime comes from

    E: y^2=x^3+7x^2+x,  ker psi=<P>, P=(1,3).

The branch support of the top double cover C17->E is psi^-1(B). If an elliptic translation or inversion with center C on E preserves that support, applying psi shows that the corresponding map on Eprime, with center psi(C), preserves B.

No inversion on Eprime preserves B, so **no translated elliptic inversion on E lifts to C17**. A preserving source translation must have psi(C)=O, hence C in ker psi. All four such translations do lift: they fix the z-coordinate and are the known cyclic-four deck group. This treats all source centers, not just those chosen rational in advance.

## 5. Why this determines the full curve automorphism group

The curve C17 has genus seventeen and a double map to E with deck involution sigma:z->-z. A curve of genus greater than five has at most one bielliptic involution. The retained proof applies: two distinct degree-two elliptic quotient maps have birational joint image in a product of elliptic curves; Hodge index bounds its self-intersection by eight, and adjunction bounds normalization genus by five. If their joint degree were two instead, the quotient subfields and involutions would coincide.

Therefore every automorphism of C17 commutes with sigma and descends to an automorphism of E. The kernel is exactly {Id,sigma}. For the specified E, c4=736 and c6=-19936 are nonzero, and discriminant=720. Thus j is neither 0 nor 1728. Every complex elliptic automorphism is a translation or a translated inversion; there are no additional origin-preserving CM automorphisms on this E.

Section 4 leaves at most four possible descended automorphisms, the kernel translations of psi. With at most two lifts each, |Aut(C17)|<=8. The four known deck translations and sigma provide eight commuting automorphisms with group C4 x C2, attaining the bound. This proves the full geometric group and excludes a dihedral order-eight subgroup of curve automorphisms.

The scope is essential: an endomorphism or correspondence of Jac(C17) or its primitive Prym need not arise from a curve automorphism. An isogeny-square decomposition could therefore exist without a dihedral curve lift. We make no contrary claim.

## 6. Frontier

Continue full Frobenius polynomial/geometric-factor calculations or periods for the auxiliary example. Test actual Y2 membership and theta geometry separately, or pursue the nonlifting 512-root family and direct non-divisor geometry on X. The original asymmetric control's fixed-origin-only receipt is retained unchanged; this successor supplies the stronger theorem.

The conditional 516-label census is unchanged and is not an unmarked moduli count. No exceptional cycle, all-cycle theorem or independent review is supplied. All four f-pullback channels remain required, and all three unrestricted research obligations remain open.

Contract: `research/conjecture_net/contracts/hodge-asymmetric-reflections.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_asymmetric_reflections.py`.
Receipt: `research/voevodsky/results/hodge-asymmetric-reflections-v1.json`.

    python research/voevodsky/checkers/check_hodge_asymmetric_reflections.py

Trust boundary: written good-reduction and divisor argument, exhaustive exact torsion/residue certificates, standard prime-to-p torsion specialization and elliptic automorphism facts, and the retained genus-bound proof of bielliptic uniqueness. Not formal verification, independent mathematical review, End computation or target matching. The iteration-23 predecessor and pins v1-v24 are retained unchanged.
