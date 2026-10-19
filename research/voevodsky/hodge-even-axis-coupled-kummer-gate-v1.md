# Global iteration 40 (fourth series 9/10): coupled Kummer equations for the even-axis model

## Result: a concrete common-cover search, not a matched Prym

Fresh iteration39 supplies the actual principal auxiliary Y3, with its saturated physical elliptic product of theta degrees4,6. For a hypothetical **smooth etale cyclic-quartic** principal Prym presentation of this Y3, this turn derives the following necessary data on the genus-five quotient B:

    deg(f8)=8, deg(f12)=12,
    H(z)=z(z-1)^2,
    H(f8) H(f12)=r^4 in C(B),
    ord_P f_j over0,infinity divisible by4,
    multiplicities over1 divisible by2,
    [D(f8)] of EXACT order4 in Pic^0(B),
    D(f)=(F0+2F1-3Finfinity)/4,
    [D(f12)]=-[D(f8)].

Conversely, on a smooth connected genus-five B, these data reconstruct an actual smooth etale cyclic-quartic tower of genera17/9/5 and opposite-character elliptic maps of degrees8,12. This is a conditional reconstruction theorem: **no B, functions, Picard class or matched Y3 has been supplied**.

The functions must be coupled. Two independently acceptable divisibility patterns do not specify a common cover; even their product equation does not prove order4. The search becomes a curve/function problem on the fixed quotient surface

    S=(E_i x E_i)/<(i,-i)>,
    function-field equation r^4=H(s)H(t).

This replaces an unspecified period-source request by explicit algebraic input requirements. It does not replace the remaining target polarization/period test. No classification of S as a K3 or dimension-based exclusion of the fixed X is invoked.

## 1. Why the axis actions are opposite, even for an unmarked ppav presentation

Every elliptic subvariety of Y3 lies in its actual saturated surface E_i^2 with physical polarization diag(4,6). A polarized automorphism preserves this isotypic surface. Its shortest primitive Gaussian column of squared length4 must be a unit on the first axis; orthogonality then preserves the other axis. Thus both axes are individually invariant. The exact unitary control has16 elements, all diagonal.

Suppose a cyclic-four curve generator rho induces the given principal Prym action. On the Prym rho^2=-Id. On the unique simple sixfold isogeny factor, End^0(X)=Q(i) forces rho to act by i or -i. Either has holomorphic multiplicities(3,3). For an etale cyclic-four cover of a genus-five curve, the two primitive character spaces each have dimension4: Riemann-Roch for the nontrivial degree-zero torsion line bundles gives g(B)-1=4. Hence the two remaining elliptic holomorphic characters must be opposite.

After replacing rho by its inverse if necessary, label the degree-four theta axis with character i and the degree-six axis with character -i. This is not the unsupported assumption that every ppav isomorphism respects a preselected K-marking.

## 2. Actual elliptic maps and affine constants

Let C17->D9->B5 be the hypothetical tower. If e_j:E_j->P is one of the actual elliptic inclusions of theta degree d_j, use polarization adjunction on the Abel-Prym map to obtain phi_j:C->E_j. With the canonical etale normalization I*Theta_C=2Xi on P,

    deg(phi_j)=2d_j=8 or12.

More explicitly phi_j^*=I e_j and phi_j,* phi_j^*=[2d_j]. These equalities use the actual elliptic inclusion and standard Jacobian norm/pullback functoriality, not just an inverse cohomology matrix.

The rho-actions on these maps may initially have translation constants. Translate each elliptic target to a fixed point of its affine order-four automorphism; multiplication by1-i and1+i is surjective, so such a point exists. Then

    phi_+ rho=i phi_+, phi_- rho=-i phi_-.

Such translations change no map degree or induced homomorphism. In particular h=rho^2 acts by negation on both maps. Both elliptic targets are the square-lattice curve E_i; we may put

    E_i: y^2=x^3-x,
    i:(x,y)->(-x,i y).

## 3. The elliptic cyclic quotient and the product equation

On E_i set z=x^2. Then y^4=z(z-1)^2=H(z), and E_i->P1_z is the degree-four quotient by i. Its inertia orders at0,1,infinity are4,2,4, with Kummer exponents1,2,-3 (the last is1 mod4).

Pull back along phi_+,phi_- on C, writing their y-functions v_+,v_-. Their x-squares descend to functions f8,f12 on B=C/<rho>. Comparing total degrees gives deg(f_j)=deg(phi_j)=8,12. Moreover

    v_+^4=H(f8), rho(v_+)=i v_+,
    v_-^4=H(f12), rho(v_-)=-i v_-.

Each v_j has a full four-element Galois orbit, so C(B)(v_j)=C(C); the two maps encode the **same connected cyclic-four extension**, with inverse characters. The product r=v_+v_- belongs to C(B), yielding

    H(f8)H(f12)=r^4.

The ratio v_+/v_- has character -1 and in general descends only to D9, not B5. Substituting a ratio equation for the product would therefore be wrong.

At the generic point of E_i^2 the two Kummer extensions over C(s,t) are independent (use valuations at s=0 and t=0). Its degree is16. The subgroup(i,-i) fixes v_+v_-; the latter has fourth power H(s)H(t), of exact order4 generically. Degree comparison identifies the invariant field as C(s,t,r), r^4=H(s)H(t). This describes the function field of the normal projective quotient S; no claim that the displayed affine hypersurface is already smooth or normal is needed. The hypothetical B maps to S. No curve on S has been constructed here.

## 4. Etaleness, global torsion and reconstruction

For a Kummer equation v^4=a over C(B), a valuation k has local normalization ramification index4/gcd(4,k). Applying this to H(f) gives precisely

| fibre of f | valuation of H(f) | required multiplicity |
|---|---|---|
| 0 | e | 4 divides e |
| 1 | 2e | 2 divides e |
| infinity | -3e | 4 divides e |

There are no other zero/pole valuations. Thus these conditions make D(f)=div(H(f))/4 an integral degree-zero divisor. They prove local etaleness of normalization, not connectedness. Over C the order of H(f) in C(B)^*/C(B)^{*4} equals the order of [D(f)] in Pic^0(B)[4]. Order1 gives a split cover; order2 gives a disconnected quartic normalization with quadratic components; exact order4 is necessary and sufficient for a connected cyclic-four field extension.

The product equation is equivalent to D(f8)+D(f12)=div(r), or inverse Picard classes. Conversely, inverse classes supply r after absorbing a nonzero constant into a fourth root over C. Neither statement by itself proves that the classes have order4.

For an explicit false-positive mechanism take z=x^2 on the elliptic base E_i itself: its special fibres have exactly the required divisibilities, but H(z)=y^4, so the base change splits. Pullback along any map to this elliptic base leaves H a fourth power: changing the base genus does not repair this error. For example, a smooth double cover B5->E_i branched at eight points has genus5 and supplies such a degree-eight function with split Kummer pullback. Abstract labels of orders1,2,4 in a marked (Z/4)^10 are only order-test controls, not a calculation of any actual genus-five Picard class.

Now assume actual smooth connected genus-five B, nonconstant functions of the stated degrees, the local conditions, exact order4 and the product identity have been supplied. Normalize B in

    C(B)(v), v^4=H(f8).

It is connected, cyclic-four and unramified. Hence C is smooth projective of genus17, its intermediate quadratic quotient D has genus9, and B has genus5. Set v_+=v and v_-=r/v. Recover elliptic coordinates by

    y_j=v_j, x_j=v_j^2/(f_j-1).

Then x_j^2=f_j and y_j^2=x_j^3-x_j. This gives the two genuine maps to E_i, of degrees8,12 and opposite characters. Rational maps to the projective elliptic curve extend across omitted points. Thus the common-cover reconstruction is geometric, not only formal local bookkeeping. The ordinary etale principal Prym and the retained conditional Schoen route apply to this reconstructed tower, once such data exist.

## 5. What reconstruction does NOT prove about Y3

The induced elliptic homomorphisms phi_j^*:E_i->J(C) land in the anti-h Prym. Their cross pairing is zero: equivariance gives i*a=a*(-i) for a in End(E_i)=Z[i], so a=0. But separate maps can have finite kernel, and separate embedded axes can still meet in torsion. Neither is excluded by the Kummer equations.

To recover the particular actual surface of Y3, the **joint map E_i^2->P must be an embedding with trivial kernel**. Only with this input do the induced theta degrees equal4,6 with no mixed gluing. Even then one still needs the full principal Gaussian period isomorphism with Y3, or an explicitly licensed correspondence/isogeny route and the four-channel tests. A similarly shaped elliptic surface alone identifies neither the complementary sixfold nor the whole principal lattice. Record which action occurs on the sixfold as well as the axes: the initial unmarked ppav comparison did not identify rho with the preselected native K-marking.

Consequently a reconstructed source is only a candidate source. There is no fixed-Y3 Prym-membership theorem here, no computed target period, and no target exceptional cycle. The degree256 Y2->Y3 and phase768i/denominator768 maps remain unchanged. Exact-polarization exclusions for Y2 have not been transported across that isogeny.

## 6. Exhausted LOCAL partition controls, not covers

For each f of degree n, enumerate all full partitions of its special fibres satisfying the inertia divisibilities. Riemann-Hurwitz on B5 gives total ramification2n+8. The special fibres use3n minus their total support size. Their excess over2n is exactly one quarter of the ramification of C->E over those special values; the remaining budget gives the rest, totaling32 as required by g(C)=17.

For n=8 there are2 choices at each order-four fibre and5 at the order-two fibre: all20 satisfy RH. For n=12 there are3,3,11 choices:99 initially, but the triple consisting of one multiplicity12 point in each fibre uses33, exceeding the total32. Thus **98** survive. The20*98=1960 paired profiles are local controls only: they do not enumerate functions, torsion classes, curves, covers or target matches. In particular the coupled product equation and order4 requirement remain wholly unverified for any actual B5.

## 7. Executable continuation and trust

Search for genus-five curves on S, or functions f8,f12 and an exact order-four line bundle satisfying the divisor conditions and product equation. Certify smoothness, torsion order and the common connected cover; then compute the joint elliptic kernel and the remaining principal Gaussian period/correspondence match before using the four exceptional channels. Direct cycles and other generalized/isogenous/ramified sources remain open; this reduction concerns only the stated smooth etale cyclic-four presentation.

Contract: `research/conjecture_net/contracts/hodge-even-axis-coupled-kummer-gate.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_even_axis_coupled_kummer_gate.py`.
Receipt: `research/voevodsky/results/hodge-even-axis-coupled-kummer-gate-v1.json`.

Trust: the written adjunction, Riemann-Roch, Kummer/normalization and finite-group invariant-field arguments, with fresh Y3/literature receipts and exact polynomial, character, partition, RH and abstract torsion controls. The checker does not compute an actual function field, Picard class, period or cover from absent inputs. This is not proof-assistant certification or independent review. Iteration39 and pins v1-v42 are preserved; the fixed X, alpha and all open target witness obligations remain unchanged.
