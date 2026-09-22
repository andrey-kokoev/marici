# Saturated observer transitions split first and retain later filtered extensions

## Result

For Nima's SPECIFIED source-action-saturated residual observer tower:

- The first transition O_2 -> O_1 SPLITS as a source bimodule map.
- The induced pushout of the first source extension into ker(O_2->O_1) is ZERO, although its witness has nonzero image. An explicit source-equivariant nullhomotopy is given below.
- Every later transition O_(m+1) -> O_m, m>=2, is NONSPLIT.
- More precisely, the corresponding full filtered source extension remains nonzero after pushout into the observer transition kernel for every m>=2.

Thus the tower does retain genuine extension information, but NOT by preserving the first adjacent attachment in its first transition. A nonzero observed witness and a nonzero observed extension class are different assertions.

Input: `../nima/source-action-saturation-builds-an-all-depth-residual-observer-tower.md`.

The Yoneda comparison in `adjacent-attachments-are-degree-one-transports-not-higher-yoneda-products.md` is unchanged. All transition classes considered here have degree one.

## 1. Conventions and the initial corner

Use the same source bimodule category, fixed marked-path generators, completed domains, and observer modules as the input. Put

    F_m=J_1/J_(m+1), G_r=J_r/J_(r+1),
    Obs_m:F_m -> O_m,
    pi_m:O_(m+1) -> O_m,
    K_m=ker(pi_m).

The letter F avoids confusing the full filtered object with an adjacent two-layer quotient.

Let c be the initial two-event corner, arithmetic endpoints 2 and 12, with event primes (2,3). Let a_0 be its forgotten diamond and a_1 its mixed diamond. Its source ideal corner is exactly

    I_c=span(a_0,a_1).

Indeed the corner has eight marked paths. The recorder has rank six: ranks one, three, and two in feature degrees zero, one, and two. Its two kernel vectors are precisely a_0 and a_1. This finite corner is unchanged by the declared completions.

The base scalar ell_1 sees a_0 with value one and kills a_1. Its source-action saturation on I has no nontrivial path contexts: a proper subcorner has fewer than two events and contains no relation. Thus O_1 is the one-dimensional corner bimodule supported at c, with every positive-length source path acting as zero.

At stage two, a contextual ell_2 also sees a_1. Append the actual forgotten (5,7) diamond b_0. Then

    ell_2(a_1 b_0)=d_2>0.

Together with ell_1 this detects both independent vectors in I_c. Since Obs_m is onto and respects vertex projections, for every m>=2 its initial corner is exactly two-dimensional, with Obs_m:I_c -> (O_m)_c an isomorphism.

Consequently

    (K_m)_c=0 for every m>=2.

This absence of a kernel at one small corner will force the later nonsplitting.

## 2. An explicit splitting of the first transition

Put u_m=Obs_m(a_0). The vectors u_m are compatible and u_1 is the unit basis of O_1.

For ANY later detector ell_r, r>=2, and ANY source contexts p,q,

    ell_r(p a_0 q)=0.

Here is the source-support reason, not a numerical cancellation. Every such detector requires its first retained seam in the initial (2,3) diamond. The two paths of a_0 are entirely forgotten. A right context begins after that diamond and cannot supply the missing retained seam inside it. A nonidentity left context cannot precede this fixed initial corner while still beginning at the detector's prescribed initial vertex. Incompatible contexts vanish by typing.

The old detector also vanishes on every positive-length context of a_0. Therefore u_m has the same one-dimensional corner action as u_1. The map

    s_m:O_1 -> O_m,  s_m(u_1)=u_m

is a source bimodule map. It is bounded because the spaces are finite-dimensional. At stage two,

    pi_1 s_2=id_(O_1).

This proves that the first observer transition splits. In fact these s_m split off one compatible constant vacuum summand at EVERY stage of the tower. This says nothing about splitting the remainder into ideal-annihilated pieces.

## 3. The first source extension becomes null in this transition kernel

The first source extension and first observer transition form the diagram

    0 -> G_2 -> F_2 -> G_1 -> 0
         |f_1    |Obs_2  |Obs_1
    0 -> K_1 -> O_2 -> O_1 -> 0.

The left arrow is restriction of Obs_2; it lands in K_1 because Obs_1 kills J_2. It is NONZERO: the actual witness a_1 b_0 has ell_2 value d_2>0.

Nevertheless the pushout of the top extension by f_1 is zero. Define

    H=(id_(O_2)-s_2 pi_1) Obs_2 : F_2 -> K_1.

This is a bounded source bimodule map and its restriction to G_2 is f_1. On the usual extension roof [G_2 -> F_2], H is an explicit homotopy from the degree-minus-one projection followed by f_1 to zero: the required equation is exactly H i=f_1.

Equivalently, if alpha_1 is the first source extension class and tau_1 is the first observer transition class, then

    (f_1)_* alpha_1 = Obs_1^* tau_1 = 0.

There is no contradiction with the old nonzero residual attachment. Its receiver has ideal-annihilated outer action, which obstructed such a homotopy. The saturated kernel K_1 instead retains nontrivial ideal action. Saturation has supplied enough target action to extend f_1 over F_2.

This is an explicit instance where a nonzero detector of the relation product does NOT preserve its source extension class under the natural target map.

## 4. Every subsequent transition is nonsplit

Fix m>=2. Use the next actual source witness

    v_(m+1)=a_1 a_2 ... a_(m+1),

where the first m diamonds are mixed and the last is forgotten. The first factor is the same a_1 in the initial corner c. Put b=a_2...a_(m+1), so b belongs to I^m.

Every element of O_m is annihilated on the right by I^m. This follows from surjectivity of Obs_m and

    F_m I^m=(J_1/J_(m+1)) I^m=0.

Suppose a source-bimodule section t:O_m->O_(m+1) of pi_m existed. Vertex equivariance forces it to respect c. By section 1, pi_m is an isomorphism on c, so the lift of Obs_m(a_1) is forced:

    t(Obs_m(a_1))=Obs_(m+1)(a_1).

Now act on the right by b. The left side must give

    t(Obs_m(a_1)b)=t(0)=0.

The right side gives

    Obs_(m+1)(a_1)b=Obs_(m+1)(v_(m+1)) !=0,

as detected by ell_(m+1) with its positive value d_(m+1). Contradiction.

Therefore tau_m is nonzero for ALL m>=2. The first case is O_3->O_2: the mixed initial diamond has a forced lift, and the subsequent mixed/forgotten two-diamond context annihilates O_2 but produces the nonzero cubic witness in O_3.

This proves nonsplitting by actual typed source action. It does not infer nonsplitting merely from nontrivial ideal action somewhere in O_(m+1).

## 5. Which later source extension is retained

For m>=2 consider the FULL filtered extension

    0 -> G_(m+1) -> F_(m+1) -> F_m -> 0,

with class alpha_m. Evaluation gives the commuting diagram

    0 -> G_(m+1) -> F_(m+1) -> F_m -> 0
         |f_m         |Obs_(m+1) |Obs_m
    0 -> K_m     -> O_(m+1) -> O_m -> 0.

Hence the natural comparison of degree-one classes is

    (f_m)_* alpha_m = Obs_m^* tau_m.

In this case the common class is NONZERO, not just tau_m itself. If the pullback on the right split, there would be a source-module map h:F_m->O_(m+1) lifting Obs_m. On the initial corner it would again have the forced value h([a_1])=Obs_(m+1)(a_1). Multiplication by the same b in I^m gives zero in F_m but the nonzero v_(m+1) observation in O_(m+1), a contradiction.

All obstructions lie in the finite 2(m+1)-event convex source packet. Thus finite restriction proves nonzero degree-one extension classes; no projectivity of completed ideals is asserted. The positive witness values, bounded finite observer maps, and strict filtered source sequences are exactly those already supplied by the input theorem.

The retained alpha_m is an extension of the ENTIRE F_m. It must not silently be identified with the adjacent extension whose quotient is G_m. Restricting a nonzero extension to a smaller submodule can kill its class. No preservation claim for those later adjacent restrictions follows merely from this nonsplitting proof.

## 6. Interpretation and verification

The concrete answer is not a uniform yes or no:

- First observer transition: split; natural observation of the first source class is null, despite its nonzero witness.
- Later observer transitions: nonsplit; their pullbacks detect nonzero full filtered source extensions.
- All of these are Ext1 statements. Neither all-depth nonstabilization nor the present result manufactures nonzero iterated Yoneda products or higher associators.

No depth-uniform norm or summability statement is needed. Each proof takes place at a finite stage, with the exact finite-support module action extended continuously to the declared sources.

Run:

    uv run --with sympy python research/voevodsky/checkers/check_saturated_observer_transitions.py

The checker verifies the actual eight-path initial recorder and its two-dimensional ideal kernel, all eight possible right contexts for the vacuum lift at the first transition, the two-dimensional observed initial corner, and the forced-lift obstruction using actual cubic and quartic source products. The general all-depth conclusion is the module argument above, not an extrapolation from enumeration.
