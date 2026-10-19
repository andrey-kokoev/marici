# Period genericity is not an automatic cycle-spreading certificate

## Fresh task and the exact fixed-source certificate

Execute period-genericity-cycle-spread-audit. The original fixed source uses eighteen algebraically independent real coordinates in the positive-plane chart. Its complex structure J is a rational function of those coordinates with rational coefficients and nonzero denominators.

For a FIXED rational exterior form v, its Hodge condition is therefore a rational-function equation in the chart parameters. Vanishing at the independent tuple forces the cleared numerator polynomials to vanish identically. This licenses the finite common-kernel proof of the stated rational Hodge/Picard space. It does not quantify over cycle equations with arbitrary coefficients or identify their parameter images with those rational Hodge equations.

The Picard certificate and the ensuing simplicity proof remain valid. The audit does not retract them; it prevents an extra conclusion not supplied by their hypotheses.

## Three spaces and two different meanings of generic

Use the following distinct objects:

1. The analytic positive-plane period domain D with the given real coordinates and native K structure.
2. An algebraic moduli component S for the polarized O_K abelian varieties, after adding sufficient level structure to work with a universal abelian family. Its analytic uniformization by the period domain is a separate map u:D->S(C).
3. Relative Hilbert/Chow parameter spaces over S for actual algebraic cycles on the fibers. For rational signed cycles, allow pairs of effective cycles and positive integer denominators.

Existence of such algebraic moduli and relative cycle parameter spaces is standard imported background; their equations and the moduli coordinates of the fixed point have not been constructed in this project. In particular the pullback under u of an algebraic equation on S need not be a polynomial or rational function of the selected period coordinates. The map is an analytic uniformization, not an established algebraic chart map of the kind needed by the fixed-point argument.

Thus independence of period coordinates does not by itself show that u(P_fixed) avoids every proper closed subvariety of S defined over an algebraic number field. This audit does not prove that the fixed moduli point fails that stronger genericity condition either. It is simply unproved by the retained certificate.

## An explicit hostile to the coordinate-change inference

Let z0=log(2)/2^20 and u0(z)=exp(2^20 z), on a small complex neighborhood of z0. Then 0<z0<2^-20. The number z0 is transcendental: if nonzero log(2) were algebraic, Lindemann's theorem would make its exponential transcendental, contradicting exp(log(2))=2. Hence z0 is algebraically generic over Qbar in the one-variable affine coordinate.

But u0(z0)=2 lies on the proper algebraic locus w-2=0. Moreover u0'(z0)=2^21 is nonzero, so even a local analytic coordinate isomorphism does not preserve this algebraic genericity. Its pulled-back equation is a nonpolynomial analytic equation. This is a counterexample to the general inference, NOT a claim that u0 is the actual Weil moduli map or that the chosen eighteen-coordinate point has an algebraic moduli value.

The checker verifies the exact local Taylor coefficients and the nonzero derivative; transcendence uses the stated imported theorem, not numerical testing.

## What a valid cycle-spreading argument would require

Let pi:mathcal X->S be a smooth projective family on an irreducible algebraic base. Work with a specified flat rational degree-six class alpha_S. In the Weil setup, its determinant monodromy can be trivialized after a finite cover: the integral O_K-linear monodromy has determinant in Z[i]^times={1,-1,i,-i}. A finite-index kernel fixes the determinant components. Alternatively all class comparisons may be stated on a simply connected local chart, with monodromy bookkeeping retained before any global conclusion.

For fixed Hilbert polynomials P_plus,P_minus and an integer n>0, a pair of relative Hilbert points supplies a signed cycle whose class can be tested against n alpha_S. Parameter spaces are projective over S; their irreducible components form a countable collection as the polynomials and n vary. Compatibility of cycle classes with flat families makes the equality locally constant on connected parameter pieces after the chosen class marking.

For one such component T carrying the desired class, the decisive extra input is

    T -> S is dominant.

Projectivity then makes its image all of S. With appropriate base changes and the universal cycles, this can supply realizations in fibers; after restricting to a dense open, a finite multisection and normalized trace are standard ways to obtain a relative rational cycle class. None of these operations is supplied merely by knowing that T has a point over a special fiber.

A conditional genericity argument is valid if a point of S is algebraically generic over a field over which these components and their closed images are defined: a component containing a cycle above that point cannot have a proper closed image defined over that field. The fixed period independence result has not established this premise for S. Conversely finding a cycle at a special point only produces a nonempty component, not dominance.

No claim that flat Hodge type is sufficient to deform an arbitrary algebraic cycle is made. That additional geometric step is precisely the type of issue addressed by semiregularity or other actual cycle-deformation arguments, with their own hypotheses.

## Apply the boundary to the retained controls

The composed correspondences prove pointwise algebraicity on a four-complex-dimensional product locus S0 inside a nine-dimensional Weil moduli component (after choosing compatible marking/level). They do not establish a cycle-parameter component dominating the full S. The fixed X is simple, so it is not on any product-isogeny locus; its relationship to other cycle-parameter images remains unknown.

Even a countable union of proper parameter images or rationally re-marked product loci need not be contained in one proper closed subset. Thus no claim that their union is nondense is inferred from dimensions alone. What fails is the asserted dominance of a PARTICULAR cycle family on the full base, which has not been shown.

## Disposition and next executable construction

Rejected: using polynomial independence in the analytic period chart as an automatic certificate of algebraic-moduli genericity or cycle-family dominance. Retained: the original Hodge/Picard calculation and all pointwise algebraic control results. No Hodge verdict follows in either direction.

The next bounded construction is positive but confined to S0: use the established pointwise algebraicity there, countability of signed relative cycle parameters, and the uncountability/Baire argument to obtain a dominating parameter component over S0. Then perform the finite-multisection and trace construction explicitly at the level of relative Chow classes, keeping degree, denominator and monodromy conditions. This would supply a relative control witness on a dense open of S0 without pretending it dominates the full nine-dimensional base or reaches the fixed X.

Verification separates exact rational/Taylor and dominance-hostile fixtures from the written algebraic-geometry implications. No actual coordinates of the fixed moduli point, universal parameter enumeration or proof-assistant certification are claimed.
