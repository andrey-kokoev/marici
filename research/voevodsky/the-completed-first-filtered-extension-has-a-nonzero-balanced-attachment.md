# The completed first filtered extension has a nonzero balanced attachment

## Result and category

The first strictly exact filtered sequence has a bounded source-equivariant analytical attachment comparison. Its product component is the ordered two-seam derivative, not an independently appended graded coordinate. It is nonzero already on the finite four-event source restriction.

Work with bounded complexes of Banach modules over the completed typed path algebra, continuous source-linear maps, and quasi-isomorphisms whose cones are strictly exact. The construction below gives an explicit roof in that localization. It does not assert topological projectivity of completed ideals or compute a completed derived tensor product.

Inputs:
- `the-first-filtered-extension-is-strictly-exact-and-source-nonsplit.md`
- `../nima/the-relation-attachment-has-a-nonzero-source-equivariant-seam-realization.md`
- `../nima/nonminimal-relation-factorizations-descend-through-balanced-seam-complexes.md`
- `bulk-and-forcing-currents-converge-separately-on-the-forcing-resolved-completion.md`

## 1. The actual extension complex

Use the common path-norm closure J_k of I^k. Set

    P=J_2/J_3, E=J_1/J_3, C=J_1/J_2.

The previous strict exactness theorem gives the bounded complex

    K=[P --inclusion--> E], in degrees -1,0,

and its canonical quasi-isomorphism q:K->C. The projection pi:K->P[1], identity in degree -1 and zero in degree zero, represents the extension connecting map through the roof

    C <-q- K --pi--> P[1].

This is an extension model, not a claim that K is a projective resolution after completion.

## 2. Ordered two-seam derivative

For an individual path, sum over ordered distinct event positions i<j. Keep the two actual marked seam edges and the terminal records in the prefix, middle, and suffix buffers. Call this D2. It is the balanced normal-form version of the iterated marked derivative.

For source relations a,b the product expansion gives

    D2(ab)=D(a) tensor_balanced D(b),

because the terms with both seams inside one factor contain rho of the other factor, which is zero. For a product of three relations every term leaves at least one factor unmarked, so

    D2(I^3)=0.

The same expansion proves source equivariance on I^2: terms differentiating an outer multiplier also contain D(I^2)=0 or rho(I^2)=0. Thus D2 induces an S-bimodule map from I^2/I^3 to the balanced two-seam bottom cycles.

It is the finite balanced layer injection already supplied by the source theorem, expressed without choosing a product factorization. Nonminimal balancing follows literally from the buffer normal form.

## 3. Continuity in the common path topology

Choose the common path weight (1+n)^2 A^n, with A at least both the forcing-letter and analytical-letter bounds. This is allowed in the previous common path-norm construction; equivalently enlarge its fixed radius. The derivative D has at most n terms, and D2 has binomial(n,2) terms. Every term is bounded by A^n in the forcing-resolved projective/cut-l1 norm. Hence both maps are bounded on this common source domain.

D2 annihilates the closure J_3 and extends to P. D annihilates J_2 and extends to E through C. The completed maps land in cycles, since the target differential is bounded and the finite cycle identity extends by density.

Fixed endpoint projections reduce the D2 map to the faithful finite associated-layer injection. Hence its completed map on P is injective in this common path-quotient completion too. No uniform inverse is asserted.

At a desired stronger feature/current radius, enlarge the source radius by the explicit letter/feature factor as in the forcing bridge. This yields a compatible scale of these extension complexes and maps; a single finite source radius is not asserted to dominate every spectral compact and every feature radius at once.

## 4. The bounded attachment chain map

Let T1 be the typed analytical single-seam complex and J2=T1 tensor_R T1 the balanced two-seam complex. Their outer source actions factor through the terminal recorder. Define

    Z=T1[-1] direct_sum J2[-1],
    F^(-1)(p)=(0,D2(p)),
    F^0(e)=(D(e),0).

This is a continuous source-equivariant chain map K->Z. The chain equations are precisely D(I^2)=0, dD=0, and dD2=0. The joint component is

    K -> P[1] -> J2[-1],

so it is explicitly the balanced product observation after the connecting projection. The shift places the two-seam cycles in degree -1. No metric is fitted and no middle term is replaced by a graded direct sum.

The construction first makes the same map in the forcing-resolved seam complex, then applies the normalized Clark feature map. The resulting square commutes on finite paths and hence on the completed domains.

## 5. Nonzero source-equivariant attachment

Restrict to a finite four-event packet. There I^3=0, and the source model becomes the existing projective complex [I^2->I] over the finite hereditary source. Let a,c be consecutive forgotten diamond relations. Their product has nonzero D2(ac).

A source-linear nullhomotopy of the joint component would require

    D2(ac)=H(ac)=a H(c)=0,

since the target's outer I-action vanishes. There is no lower target term to supply an alternative homotopy component. This is the established finite source-equivariant obstruction.

It also excludes zero for the completed roof in the stated localization: restriction by the finite packet idempotents is a bounded exact projection, preserves strict exact cones, and followed by forgetting topology gives the finite algebraic module-derived comparison. The restricted source resolution is projective on either the left or the right, where the preceding non-nullhomotopy test detects a nonzero morphism. A zero completed morphism could not restrict to that nonzero morphism.

This reasoning uses the finite projective restriction, NOT the false implication that a non-nullhomotopic map from an arbitrary completed K must be nonzero after derived localization. No enveloping-algebra projectivity is assumed.

## 6. Pairings and exact boundaries

The forcing-resolved map retains the source data needed for separately convergent bulk, forcing, and incidence currents. At each fixed compact spectral set the earlier bounds apply after the indicated radius enlargement. The relative collision corrections compare unbalanced and balanced observations; they do not change F or its connecting projection.

Injectivity of the joint component is not nondegeneracy of its restricted Green form. Ambient paired observation and source self-pairing remain distinct. A completed perfect-module tensor-Hom beta equivalence is not proved by this construction.

## Verification

`uv run python research/voevodsky/checkers/check_completed_filtered_attachment_map.py`

Passed four actual product derivative identities, eight I^3 vanishings, eight nonminimal balanced comparisons, closure of the two-seam images, and the nonzero four-event witness. The norm extension and roof interpretation are the arguments above, not a numerical derived-category calculation.

## Closed target

The first filtered extension now has strict completed exactness, a nonzero source extension class, and its bounded forcing/Clark balanced attachment realization in the specified common path topology. Recovering all filtered levels, identifying their completed tensor-Hom duality, and comparing other completion topologies remain separate tasks.
