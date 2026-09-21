# Fox lifts transfer the compatible filtered tower to presentation scales

## Result

The controlled Fox lifts remove the topology mismatch between the common-path filtered attachment models and the independently completed ideal-power presentations, on their compatible all-radius intersections. The first two attachment comparisons therefore belong to the same source-scale architecture as the completed associated algebra.

The same construction gives compatible attachment roofs at every FINITE filtration level. This does not compute completed derived tensor products or identify an unrestricted filtration inverse limit.

Input:
`../nima/universal-form-fox-lifts-control-the-completed-ideal-power-topologies.md`.

## 1. Quantitative comparison, not a feature inverse

For a fixed endpoint interval of length n, the supplied source-only factorization lift satisfies

    w_r(n)||z||_path <= nu_r(z) <= 32^n w_r(n)||z||_path.

It is a lift in actual relation-factor presentations; no analytical Gram or inverse Clark transform enters. With depth graph weights, the next ideal-power comparison is

    ||z||_(r+1,s,b) <= 2 lambda s ||z||_(r,2s,64b).

The forward merging map and this reverse estimate identify the compatible scale intersections. On each fixed finite depth, changing the polynomial path weight costs a fixed additional radius enlargement. Taking quotient infima transfers these estimates to I^r/I^m for every specified m>r.

These are topological identifications of the scale intersections, not isometries and not equivalences of individual Banach stages. The finite identity maps preserve endpoints and source actions, so their continuous extensions do too.

## 2. Exactness on an intersection needs an additional argument

One cannot conclude that a sequence of intersections is surjective just because every Banach stage is. Here the common-path corner structure supplies simultaneous lifts.

Fix a finite quotient of ideal powers and a common polynomial weight. In each stabilized endpoint corner the source space and its quotient are finite dimensional. Choose, for each quotient vector, a lift minimizing the UNWEIGHTED path norm. Such a lift exists in finite dimension. The weights for every radius, and any fixed polynomial exponent, are scalar multiples of that same corner norm, since all paths in the corner have the same event length.

Thus this ONE choice of corner lifts attains the quotient norm simultaneously at every radius. If a family of quotient coordinates belongs to all radius-weighted l1 spaces, the family of chosen lifts also belongs to all of them. This proves surjectivity on the common-path scale intersection. No linear, multiplicative, or source-equivariant section is asserted.

The kernel is the intersection of the prescribed closed corner kernels. The spaces are Frechet, so the continuous surjection is open. Hence the sequence is strictly exact. Transport by the Fox comparison gives strict exactness for the corresponding presentation-scale sequence.

This is the missing justification beyond stagewise Banach exactness.

## 3. Consequence for the existing two stages

The sequences

    0 -> I^2/I^3 -> I/I^3 -> I/I^2 -> 0,
    0 -> I^3/I^4 -> I/I^4 -> I/I^3 -> 0

now have their strict completed versions on the compatible presentation intersections as well as the common-path intersections. Their continuous attachment maps transfer unchanged. The four- and six-event nonsplitting witnesses persist, since every comparison restricts to the identity on those finite source coordinates.

The kernel [I^3/I^4 --id--> I^3/I^4] in the common refinement remains contractible. The Fox lift is used for norm control and surjectivity, not as a source-module splitting of either extension. The known nonsplitting is therefore respected.

## 4. Every finite filtration level

For m>=2 put

    E_m=J_1/J_(m+1),    G_m=J_m/J_(m+1).

All quotients here carry the compatible all-radius topology just identified. The sequence

    0 -> G_m -> E_m -> E_(m-1) -> 0

is strictly exact by section 2. Its extension model is H_m=[G_m->E_m] in degrees -1,0, with its projection to G_m[1].

The ordered m-seam derivative D_m on paths has at most binomial(n,m) terms. It kills I^(m+1), and on I^m it is the balanced product of the local relation derivatives. The product rule makes it source-equivariant there. A fixed polynomial path weight (1+n)^m and a sufficiently enlarged letter radius bound it. The Fox estimates transfer this continuity to the presentation intersection.

Thus the connecting projection has the bounded forcing/Clark observation

    H_m -> G_m[1] -> J_(R,m)[1-m].

At every fixed endpoint the finite balanced layer map is injective; retained endpoint projections preserve that injection on the summable domain. The prescribed tensor-of-shifts comparisons, rather than new phases, handle alternate presentations.

## 5. Refinement preserves earlier attachment roofs

For 2<=k<=m consider

    L_(m,k)=[J_k/J_(m+1) -> J_1/J_(m+1)].

It resolves E_(k-1)=J_1/J_k. For m>k, truncation to L_(m-1,k) has kernel

    [G_m --id--> G_m],

so is a strict quasi-isomorphism with a bounded kernel contraction. Quotient maps compose literally under further truncations.

The k-seam observation on the degree-minus-one term is D_k, factoring through G_k because it kills J_(k+1). It is therefore unchanged by every such refinement. This proves compatibility of earlier attachment roofs at all finite levels, not merely equality of their graded dimensions.

A new D_m observation is attached to H_m, where its domain is G_m. It is not declared to be an equivariant cycle map on an arbitrary larger quotient J_k/J_(m+1).

## 6. Remaining completion boundary

The finite-level family is now coherent in the presentation-scale topology. Passing to an inverse limit still needs its realization topology and a boundedness/summability condition on compatible families. A projective limit can contain families not arising from the summable source. Nothing here identifies them by fiat.

Completed projectivity, flatness, and tensor-Hom beta equivalences also remain separate. The roof construction avoids those assumptions. The compact analytical map remains without a continuous inverse; Fox lifting is purely on the source side and does not repair that instability.

## Verification

Fresh `uv run python research/nima/checkers/check_controlled_ideal_factorization_lift.py` passed: 442 marked-path identities, 184 normalized-form sections, and 42 exact factorization lifts.

The first- and two-stage attachment checkers supply the concrete derivative and comparison regressions. The all-finite-level assertion follows from the ordered derivative product rule, the explicit identity-kernel complexes, and the Fox bounds. It is not reported as a numerical all-level test.
