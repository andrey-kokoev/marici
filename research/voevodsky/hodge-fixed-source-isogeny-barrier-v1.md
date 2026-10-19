# The fixed Picard-rank-one source is simple, not cycle-free

## Fresh task and unchanged source

Execute fixed-source-isogeny-decomposition-barrier. Return to the ORIGINAL selected sixfold X, not one of the decomposable controls. The retained explicit-period proof and exact rank65 certificate in the 66-dimensional two-form space give

    NS(X)_Q=Q E, rho(X)=1.

This is a rational cohomological/divisor conclusion, using the imported Lefschetz(1,1) theorem and the written period-independence argument. It does not assume anything about alpha's algebraicity.

## Isogeny invariance of the rational divisor rank

Let phi:T->X be an isogeny of complex abelian varieties. There is a quasi-inverse isogeny psi:X->T and an integer n>0 with

    phi psi=[n]_X, psi phi=[n]_T.

On Neron-Severi groups, [n]* is multiplication by n^2. Thus the two pullback compositions are n^2 times the identity. Over Q, phi* is an isomorphism with inverse (1/n^2)psi*. In particular

    rho(T)=rho(X).

The scalar n^2 here comes from divisor degree and is not the topological degree of [n], which is n^(2 dim X). No corresponding assertion about equality of integral Neron-Severi lattices is made.

## A genuine product has at least two independent polarizations

If T=T1 times T2 with both factors positive-dimensional, choose ample divisor classes L1,L2 on them. The classes

    pr1*L1, pr2*L2 in NS(T)_Q

are independent. Restriction to T1 times {0} kills the second and detects the first; restriction to {0} times T2 does the reverse. Nonzero rational multiples of an ample class cannot vanish, for example by its positive top self-intersection.

Therefore rho(T)>=2. Since rho(X)=1, X cannot be isogenous to ANY nontrivial product of positive-dimensional abelian varieties. The exclusion is not limited to a threefold-times-threefold product or to K-compatible decompositions.

By Poincare complete reducibility, any nonzero proper abelian subvariety of X would have a complementary abelian subvariety whose product maps isogenously onto X. Hence X is simple. This imports Poincare reducibility, not a classification of its full endomorphism algebra; in particular we do not infer End(X)_Q=Q(i) from this argument.

## Rational re-marking cannot evade the conclusion

A decomposition of the rational H^1 or rational homology into appropriate polarized rational weight-one sub-Hodge structures corresponds, up to isogeny, to an abelian product decomposition. Equivalently a rational J-invariant tangent subspace gives a complex subtorus with its induced lattice, and projectivity makes that subtorus algebraic. Such a decomposition is excluded by simplicity.

Thus changing the rational marking cannot turn the fixed X into one of the decomposable correspondence controls. This is stronger than observing nonzero off-block entries in one period matrix. An arbitrary real change of basis need not preserve rational structures and provides no isogeny or algebraic factor.

## Exactly which transport maps are excluded

Any homomorphism from a lower-dimensional abelian variety into X has an abelian-subvariety image, and is therefore zero. Likewise X has no nontrivial lower-dimensional abelian quotient. A homomorphism from a product of two threefolds to X is zero on each factor and thus zero. An arbitrary morphism between these abelian varieties is a translate of a homomorphism, so it cannot provide a generically finite transfer to X either.

These facts exclude direct product identification, isogeny transfer and such abelian morphisms as ways to move the previously constructed R/I controls to the fixed X. They do NOT exclude higher-codimension algebraic correspondences, graph constructions on nonabelian auxiliary varieties, or maps from nonabelian smooth threefolds.

## Concrete nonlinear-cycle boundary on the same X

Choose k sufficiently large and three general divisors in |H^k|. Their intersection Y is a smooth connected algebraic threefold in X with class k^3 E^3 and positive intersection degree 2160 k^3 against E^3. It cannot be a translate of a positive-dimensional abelian subvariety, but it certainly exists.

Moreover weak Lefschetz gives H^1(X,Q) isomorphic to H^1(Y,Q). Hence q(Y)=6, and the induced map Alb(Y)->X is an isogeny. This is compatible with dim Y=3: the Albanese variety of a threefold can have dimension greater than three. Therefore the exclusion of maps from three-dimensional ABELIAN varieties does not exclude this inclusion of a nonlinear threefold. The supplied control keeps the distinction concrete.

No conclusion that every nonlinear threefold has polarization class is made. An exceptional codimension-three cycle representing alpha, if it exists, is not ruled out by simplicity.

## Disposition and next bounded audit

The decomposable algebraic controls cannot reach the fixed X by changing rational coordinates or applying an isogeny. This route boundary is proved intrinsically. The controls still refute family-uniform nonalgebraicity shortcuts; they neither prove nor refute algebraicity of the fixed alpha.

Next audit the other tempting transport claim: does algebraic independence of the chosen PERIOD coordinates license a generic algebraic-moduli or cycle-spreading conclusion? Separate the rational-in-period Hodge equations used for the Picard certificate from relative Chow/Hilbert parameter images under the analytic period map. Determine exactly what dominance or deformation input would be needed to move the supplied special-fiber cycles. Do not assume that a point generic for polynomial period equations is automatically generic for algebraic cycle parameter spaces.

Verification combines the written isogeny/restriction/reducibility proof with exact degree/rank controls and the retained Picard certificate. Standard abelian-variety rigidity and weak Lefschetz are imported. No all-cycle exclusion, proof-assistant certification or Hodge verdict is claimed.
