# Global iteration 21 (third series 1/10): non-scalar commuting factors fail

## Scoped result

In the **conditional bielliptic-intermediate** family, restrict to Nm_k(L)=zeta. The previous audit left 256 roots with a commuting involutive lift sigma. This turn excludes every case in which sigma acts non-scalarly on the primitive eightfold Prym P, even up to unpolarized isogeny to the fixed A=X6 x B2.

There are exactly four remaining commuting roots: L=k^*M with M^2=zeta on the elliptic curve Eprime. They describe cyclic-four elliptic-isogeny base changes, not actual target realizations. Together with the untouched 512 nonlifting roots, the conditional necessary-condition census becomes **516 labels / 258 inverse pairs**. These are not unmarked moduli counts. No theta dimension or actual Y2 realization has been supplied.

## 1. The commuting action and its branch data

Use the prior notation C17->C9->C5, with rho generating the etale cyclic-four cover C17->C5, h=rho^2, and k:C5->Eprime the bielliptic double cover branched at eight points. In the norm-zeta stratum the pointed lift sigma of the bottom involution has sigma^2=1 and commutes with rho. It descends to the unique bielliptic involution b on C9. After proving its square is one, we may use either sigma or h sigma below; both are involutive lifts of b, although only a lift fixing a point is called pointed. This accounts for both scalar signs without counting covers twice. Therefore

    G=<rho,sigma> = C4 x C2,
    C17/G=Eprime,
    E=C17/<h,sigma> = C9/<b>

is elliptic. Sigma is independent of rho, since it acts nontrivially on C5 whereas rho is a deck transformation over C5.

The only branch points of C17->Eprime are the eight branch points of k. Their inertia has order two, since C17->C5 is etale. It lies outside <rho>, so is either <sigma> or <h sigma>. Let a be the number with inertia <sigma>.

**A is even.** In the abelian group G, the product of local inertia monodromies equals identity (the handle commutators vanish). That product is sigma^a(h sigma)^(8-a)=h^(8-a). Hence a is even. Without this step, odd splits such as 7+1 could not simply be omitted.

Above a branch point of the first type, sigma fixes all four points in the C17->C5 fibre; above a point of the other type it fixes none. This also follows from commuting with the transitive rho action on that fibre. Thus sigma has 4a fixed points, and h sigma has 4(8-a).

## 2. Quotients and actual Prym factors

Put D=C17/<sigma>, Dprime=C17/<h sigma>. Riemann--Hurwitz gives

    genus D=9-a, genus Dprime=1+a.

Both have degree-two maps to the elliptic curve E. Pullback on Jacobians identifies, up to isogeny, the sigma-even and sigma-odd parts of P with

    Prym(D/E), Prym(Dprime/E),

of dimensions 8-a and a. These are actual quotient-curve factors of a hypothetical cover, not an assumed principal product decomposition. Rho descends to both quotients and preserves their Jacobian polarizations. On each primitive Prym its square is -Id, giving an integral Z[i] action.

The even values a=0,2,4,6,8 give precisely:

- 0+8 (scalar action of sigma on P);
- 2+6;
- 4+4;
- 6+2;
- 8+0 (the other scalar sign).

The 4+4 case cannot contain simple X6. In a 6+2 case, any isogeny P~X6 x B2 forces the six-dimensional quotient Prym to be isogenous to X: a nonzero map from simple X to either fourfold or a twofold is impossible, and a nonzero map into a sixfold is an isogeny. No particular identification with the actual elliptic reflection of Y2 is made.

## 3. The sixfold factor is ramified, not principally normalized

In the 6+2 cases the sixfold is Psi=Prym(D7/E1), a double cover of an elliptic curve by a genus-seven curve. It has twelve branch points, by Riemann--Hurwitz.

Freshly inspected retained primary source: David Mumford, *Prym Varieties I*, section 3, **Corollary 1, printed p332 (PDF p8)**. For a ramified double cover its natural polarization p (restriction of the Jacobian theta polarization) has kernel symplectically isomorphic to the base Jacobian two-torsion. Here the base is elliptic, so

    ker p ~= (Z/2)^2,
    polarization type = (1,1,1,1,1,2).

Corollary 2 on printed p333 allows principal halving in the unramified or two-branch-point cases. It is **not** applicable to twelve branch points. We do not call p principal or divide it by two as an integral polarization.

The source PDF, newly extracted and rendered pages 331-333, and manifest are hashed under `inputs/hodge-commuting-prym-audit-v1/`. The rendered Corollary 1, its polarization kernel and the Corollary 2 boundary were visually inspected. `pnpm pdf:search ramified -Book '*prym*'` found no indexed book alias, not absence of literature; direct inspection of the retained primary PDF supplied the needed statement. No fresh download or exhaustive search is claimed.

## 4. Inert-three parity excludes the sixfold factor

The lattice H1(Psi,Z) is free of rank six over Z[i], since Z[i] is a PID. Rho preserves the restricted Jacobian polarization and rho^2=-Id on Psi. In a Gaussian basis write its alternating form as E=Im H for a Hermitian form H. The absolute Hermitian determinant equals the Pfaffian magnitude of E. The type above gives

    |det H|=2, so v3(det H) is even (zero).

This can also be read as a statement about the square of the determinant of E; the standard trace convention changes only powers of two, not its inert-three parity. The finite diagonal/Pfaffian control checks the magnitude, but does not identify a curve period lattice.

The fixed X has Hermitian determinant -3, rational NS rank one, and End^0(X)=Q(i). If Psi were isogenous to X, transporting its Gaussian action to X gives either i or -i, since these are the only roots of t^2+1 in End^0(X). The transported polarization is a positive rational multiple q of the fixed polarization, by NS rank one.

A rational Gaussian basis change multiplies det H by a norm from Q(i). At inert prime three, such norms have even valuation. The scalar q multiplies a rank-six determinant by q^6, again an even valuation change. Replacing i by -i replaces H by minus its conjugate; in even rank six the determinant is unchanged. Therefore v3(det H) modulo two is preserved under the putative unpolarized isogeny and either K-identification.

But the fixed X has v3(-3)=1, while Psi has v3(det H)=0. Equivalently 3/2 has odd three-valuation and is not a Gaussian norm. Contradiction. This rules out the 6+2 cases; it is not an unqualified determinant invariant for all abelian varieties or all NS ranks.

## 5. Scalar cases are exactly four pulled elliptic roots

It remains to understand a=0 or 8, not to reject them. Replacing sigma by h sigma interchanges a and 8-a, so assume a=8. Then D=C17/<sigma> has genus one and D->Eprime is an **etale cyclic-four isogeny**: all inertia of C17->Eprime is killed in this quotient.

The two quotient maps to C5 and D identify C17 with C5 x_Eprime D, since the corresponding subgroups <rho> and <sigma> intersect trivially. Both covers are smooth; the fibre product over C5 is etale. Thus the order-four class L comes from an elliptic class M in Pic0(Eprime)[4]. Injectivity of k^* and L^2=k^*zeta imply M^2=zeta.

Conversely each such M gives the elliptic four-isogeny base change and a scalar lift on P. Multiplication by two on an elliptic curve has four preimages of a given nonzero two-torsion point, all of exact order four. Pullback k^* is injective, so these are four distinct L, paired into two inverse pairs.

Every other commuting root has a non-scalar split and was excluded in sections 2-4. Therefore **252 of 256 commuting labels are removed**, leaving four. Together with the 512 nonlifting roots from the previous audit, 516 labels / 258 inverse pairs remain. We do not assign separate root multiplicities to the 4+4 and 6+2 cases from branch-subset counts alone.

## 6. What remains open

These are universal restrictions within the conditional bielliptic-intermediate family, not an actual computation of dim Sing theta2 or a chosen branch. The four pulled roots may still fail target matching; the 512 nonlifting roots have not been tested by this argument. Other nonbielliptic intermediates, noncyclic/ramified/singular Prym constructions and direct geometry on X remain available.

Next investigate the actual period/endomorphism data of elliptic four-isogeny base changes and the nonlifting half, or obtain theta/cycle geometry. All four f-pullback exceptional channels remain required for any proposed eightfold cycle. No exceptional algebraic cycle, all-cycle theorem, independent review or Hodge verdict is supplied. The three unrestricted research obligations remain open.

Contract: `research/conjecture_net/contracts/hodge-commuting-prym-audit.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_commuting_prym_audit.py`.
Receipt: `research/voevodsky/results/hodge-commuting-prym-audit-v1.json`.

    python research/voevodsky/checkers/check_hodge_commuting_prym_audit.py

Trust boundary: written abelian-cover monodromy and quotient argument; primary Mumford ramified-kernel theorem; elementary-divisor theory and Gaussian PID lattices; retained simplicity, End and NS/determinant proofs. Exact finite controls and source freshness are not formal verification or independent mathematical review. The iteration-20 predecessor and pins v1-v21 are preserved unchanged.
