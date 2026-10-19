# The complete-intersection semiregularity map: trace, rank15, kernel120

## Fresh input and conventions

Execute complete-intersection-semiregularity-map. Retain the smooth complete intersection Z of three sections of an ample L=H^k on an abelian sixfold X. Put l=c1(L), let W be the three-dimensional space indexing its defining sections, and set E=L tensor W*. Thus the section s of E cuts out Z and N=E|Z. All groups below are complex Dolbeault/coherent cohomology groups. Cycle-class and connecting-map signs are chosen compatibly with sigma(ob(kappa))=kappa contracted with [Z]. Changing the common convention does not change any ranks or kernels.

This is a calculation for the actual ample complete-intersection control, not a claim about a smooth representative of the Weil class R.

## Canonical Koszul identification of the obstruction space

Tensor the ideal Koszul resolution by E:

    0 -> E tensor Lambda^3 E* -> E tensor Lambda^2 E*
      -> End(E) -> I_Z tensor E -> 0.

The first two terms are sums of L^(-2) and L^(-1); their cohomology below degree6 vanishes. Together with H^1(E)=H^2(E)=0 and

    0 -> I_Z tensor E -> E -> i_*N -> 0,

the connecting maps give a canonical identification

    delta:H^1(Z,N) ~= H^2(X,End(E))
                         = End(W*) tensor H^2(X,O_X).

Its dimension is 9*15=135, as in the previous calculation. Keeping End(W*) rather than replacing it by nine unrelated copies is essential.

## Compute the map, not just its dimensions

Under delta the semiregularity map is

    sigma(beta) = l^2 cup tr(beta).

Here trace lands in H^2(O_X), and multiplication by l^2 lands in H^4(Omega_X^2).

The geometric ingredient is the Koszul/Atiyah transgression of the dual conormal map used in the previous note. Its Euler-class expression in rank3 is the coefficient of t^2 in

    tr(adj(1+t At(E)) beta),

with the Atiyah class normalized to represent Chern classes. This is the standard Koszul semiregularity compatibility for a regular zero locus. To see the specialization here: transgressing the two differentiated defining equations in the dual conormal map contributes two line-bundle transition classes. At(E)=l Id, so adj(1+t At(E))=(1+t l)^2 Id. Only the matching endomorphism indices survive contraction with the Koszul exterior factors; the result is l^2 times the ordinary trace. This computes the map via the regular-sequence presentation, not via a dimension guess.

Equivalently, in the dual description H^2(Omega_X^4) maps into H^4(O_X) tensor End(W*)* by the dual of multiplication by l^2 followed by the scalar identity tensor. This is the same conormal/Koszul transgression under Serre duality.

Changing a basis of W conjugates beta and preserves its trace. Basis covariance is a consistency check, NOT by itself a proof of the trace formula: dependence on the chosen sections would need to be excluded by the transgression calculation. The latter identity is imported standard Koszul/Atiyah geometry; the checker verifies its specialized exterior-algebra consequences, not that geometric theorem.

## Rank and kernel

Multiplication by l^2 is injective on H^2(X,O_X). Indeed hard Lefschetz says l^4:H^2(X,C)->H^10(X,C) is an isomorphism, so l^2 on H^2 is injective. Its restriction sends type(0,2) to type(2,4).

Since trace:End(W*)->C is surjective,

    rank(sigma)=dim H^2(O_X)=15,
    ker(sigma)=sl(W*) tensor H^2(O_X),
    dim ker(sigma)=8*15=120.

The target dimension remains225. In particular this smooth ample complete intersection is NOT semiregular in the sense of injectivity of sigma, despite its genuine polarized-family lifting established previously.

## Actual ambient obstruction values occupy a smaller space

Let a(kappa)=kappa contracted with l in H^2(O_X). Compatibility of the ideal connecting map with the Atiyah obstruction gives

    delta(ob_Z(kappa)) = Id_(W*) tensor a(kappa).

One can read this directly from transition functions: E has the same line-bundle transition in each of its three summands; the failure to lift these transitions is the line-bundle obstruction a(kappa) on each diagonal and zero off the diagonal. Applying End(E)->I_Z E evaluates this failure on the defining section, giving the normal-lift connecting cocycle.

Consequently

    sigma(ob_Z(kappa)) = 3 l^2 a(kappa)
                       = kappa contracted with l^3,

which also fixes the normalization of the trace formula.

For an abelian sixfold, H^1(T_X) has dimension36. Nondegeneracy of l identifies contraction with the alternating quotient of a 6 by 6 matrix: a is surjective onto Lambda^2 H^1(O_X), of dimension15. Its kernel has dimension21, the polarized tangent space. Therefore

    image(delta ob_Z) = C Id tensor H^2(O_X),
    image(delta ob_Z) intersect ker(sigma) = 0.

The last assertion uses tr(Id)=3 in characteristic zero. Sigma has a large kernel, but it loses NO actual first-order ambient obstruction value for this particular Z. The polarized directions, including the nine-dimensional Weil subfamily, have a(kappa)=0 and genuinely lift. Unpolarized directions with a(kappa) nonzero do not lift this embedding at first order.

Thus the full obstruction space, the attainable ambient obstruction values, and the Hodge image are three distinct objects. The rank120 invisible space is not a collection of demonstrated nonzero obstructions to the polarized lifting control.

## Scope and next constructive test

This calculation cannot be assigned to the unspecified signed Weil-cycle representatives. No semiregularity kernel, smooth representative or actual obstruction for alpha has been computed. Its original algebraicity question is unchanged.

A nonredundant next test concerns HIGHER-order values on the supplied control: deformations of E=L tensor C^3 have matrix-valued tangent classes in End(C^3) tensor H^1(O_X). Their primary quadratic obstruction is built from commutators in End(C^3) tensor H^2(O_X), whose trace vanishes. Construct a concrete noncommuting example with nonzero obstruction, then audit whether and under what comparison theorem it transfers to an embedded deformation of Z. Do not identify a bundle obstruction with a cycle obstruction merely because delta identifies their vector spaces.

Verification consists of an exact exterior-algebra model of l^2, trace rank/kernel and the alternating ambient map, with the geometric factorization kept explicit as imported theory. No Hodge verdict or proof-assistant certification is claimed.
