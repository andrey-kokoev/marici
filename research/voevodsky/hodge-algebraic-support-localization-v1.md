# Algebraic support localization in degree six

## Fresh task and scope

The workbench asks for the source-specific map H_Z^6(X,Q)->H^6(X,Q), including singular and reducible supports, on the fixed smooth projective sixfold. Throughout Z is a closed reduced algebraic subset of complex dimension at most three. Nilpotent scheme structure does not change this topological support group; cycle multiplicities are rational coefficients of fundamental classes.

SCC obligations: the support category, every lower-dimensional stratum, the localization map and its kernel. A smooth real six-dimensional support is not automatically an algebraic threefold.

## Duality computes the entire source, not merely its smooth part

The complex orientation of the real twelve-dimensional manifold X gives support duality

    H_Z^6(X,Q) = H_6^BM(Z,Q).

Let Z_1,...,Z_r be its irreducible components of complex dimension three. Remove their singular loci, pairwise intersections and all smaller-dimensional components. The removed closed algebraic subset B has complex dimension at most two; the remainder is a disjoint union of connected smooth complex threefolds U_i.

Both H_6^BM(B,Q) and H_5^BM(B,Q) vanish by real dimension at most four. The Borel-Moore localization sequence therefore identifies

    H_6^BM(Z,Q) = direct_sum_i H_6^BM(U_i,Q)
                = direct_sum_i Q[Z_i].

In particular singularities and intersections create no extra generators in this TOP homology degree. This does not assert that their lower-degree homology is trivial. If dim_C Z<3 the source is zero.

The support-forgetting map sends each generator to the ordinary cycle class cl(Z_i). Consequently

    im(H_Z^6(X,Q)->H^6(X,Q)) = span_Q{cl(Z_i)}.

This uses oriented support duality, top Borel-Moore fundamental classes and localization as imported standard theorems. It does not assume a moving lemma or smoothness of Z.

## Restriction criterion and its exact quantifier

Put V=X minus Z. Localization gives

    H^5(V,Q) --delta_loc--> H_Z^6(X,Q) -> H^6(X,Q) -> H^6(V,Q).

Thus beta restricts to zero on V exactly when beta lies in the span of the classes of the dimension-three components of THIS support. The support map need not be injective; delta_loc retains relations among fundamental classes.

Taking all such algebraic supports, including finite unions, gives

    N^3 H^6(X,Q)
      := sum_(codim Z >=3) im H_Z^6(X,Q)
       = im(cl:CH^3(X)_Q -> H^6(X,Q)).

Indeed one direction follows from the computed basis. Conversely every finite rational algebraic cycle sum is supported on the finite union of its components. The sum over supports is also a union of their images because finite unions of supports are allowed.

Hence alpha is algebraic iff there exists such an algebraic Z with alpha|_(X minus Z)=0. A refutation would require nonzero restriction for EVERY such Z. Renaming the cycle image as coniveau is a valid geometric characterization, not a new proof that alpha is outside it.

## Actual reducible-support and localization-kernel control

Choose m with L of Chern class mE very ample. Let W be a general complete intersection of two sections of L; choose two additional general sections s,t, yielding distinct smooth threefolds Z_s,Z_t inside W. Their intersection has dimension two. Both have cohomology class m^3 E^3. Set Z=Z_s union Z_t.

The top-support group is Q^2, even though this union is singular along its intersection. Its support map is

    (u,v) -> m^3(u+v) E^3.

Its image is the polarization line, and its kernel is Q(1,-1). By exactness, (1,-1) is in the image of delta_loc from H^5(X minus Z,Q). It is a real, nonzero support-group relation, not a nonrealizable-cycle obstruction. The previously constructed rational function s/t on W supplies the parallel algebraic rational-equivalence relation Z_s-Z_t. We do not identify delta_loc itself with the cubical graph boundary; these are distinct typed maps explaining the same class cancellation.

The actual class alpha=R is not in this support image: its period on the marked all-x six-torus is one, whereas E^3 has period zero. Equivalently the two exact exterior forms are independent. Hence alpha restricts nontrivially to X minus THIS Z. Each effective component still has intersection degree 2160 m^3 against E^3. The kernel relation is compatible with positive effective degree because it is signed.

The argument holds for every support made from these complete-intersection components; it does not assert that every algebraic support is so generated. The choice of a sufficiently large m is existential via very ampleness/Bertini; no numerical very-ampleness bound or equations for the exceptional fixed class are computed.

## Topological support is insufficient

Support duality also exists for suitable nonalgebraic closed sets, but the conclusion that generators are algebraic cycle classes used complex algebraicity of Z. Merely producing a rational topological cycle Poincare dual to alpha does not meet this requirement. Conversely the marked period torus used above is a test cycle, not a proposed algebraic support for alpha.

## Disposition and executable continuation

The algebraic support interface is constructed, including all singular and lower-dimensional strata in the relevant top degree. Its universal criterion is exactly the still-unknown cycle image; the explicit reducible support excludes alpha only for that support family. No Hodge verdict follows.

Next bounded test: compute the support image for a smooth ample DIVISOR D of class mE using weak Lefschetz and Gysin, then test the primitive alpha. Determine whether an arbitrary codimension-three algebraic support may be placed inside such a smooth D, rather than assuming a Bertini statement with a prescribed base locus. This genuinely different envelope test can constrain the geometry of potential supports and expose the role of singular ample divisors. It remains executable without asking the operator to supply a cycle representing alpha.

Verification separates the written general duality argument from exact exterior-form and matrix controls on the supplied polarization supports. No proof-assistant certification, universal support enumeration or independent all-cycle annihilation theorem is claimed.
