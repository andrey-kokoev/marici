# An all-depth seam scale has bounded differential and continuous balanced tensoring

## Result and scope

The fixed-depth cut-l1 complexes admit an explicit all-depth scale of stronger norms. Their differential is uniformly bounded across depth, and balanced tensor concatenation is continuous with a controlled loss of scale. The intersection of the scale is a complete locally convex receiver for these operations.

These are norms on the existing coefficient seam complexes, not a new signed metric. All finite carrier pairings, memory/seam weights, source maps, and relative currents stay unchanged. This does not turn the source image into a closed subspace of its original target norm or identify arbitrary inverse-limit families with summable states.

Inputs:
- `endpointwise-separation-and-bounded-differentials-close-the-fixed-depth-l1-receiver.md`
- `the-relative-normalization-pentagon-extends-to-the-cut-l1-completion.md`
- `../nima/the-balanced-relative-seam-construction-satisfies-the-finite-pentagon.md`

## 1. Graph weights

In a term of the r-fold unshifted seam complex, let k be the number of active seam-edge factors; the remaining factors are vertex terms. Thus its degree is -k, with 0<=k<=r. Set

    lambda=max(1,tau/sqrt(w_seam)),
    b_s(k)=(2 lambda s)^k k!,    s>=1.

For each r retain the cut-l1 shape norm. Sum it over all r and all degrees with multiplier b_s(k), obtaining a Banach space Y_s. The depth label r remains retained. If external parenthesizations are also retained, use their declared labelled sums rather than identifying them implicitly.

A differential from k active seams to k-1 has unweighted norm at most 2k lambda. Therefore

    2k lambda b_s(k-1)/b_s(k)=1/s,
    ||d||_(Y_s -> Y_s)<=1/s.

The algebraic identity d^2=0 extends by density. This is a bounded all-depth complex. One can individually shift depth r by [1-r] when displaying its attachment in degree -1; tensor grading assertions below use the unshifted complexes.

## 2. Normalization and relative currents remain uniform

Permitted normalization merges coefficient buffers without changing r or k. Hence the multiplier b_s(k) cancels between input and output. Its norm remains at most one. Associators of balanced normal forms are likewise isometric ordered reassociations. The finite chain and pentagon identities extend on each Y_s.

The prescribed degreewise signed forms have norm at most one because b_s(k)>=1. Their source-generated collision forms retain the cut-l1 bound. Integrated relative identities therefore extend throughout the scale. This means the existing degreewise tensor forms and their direct-sum observations; no new cross-degree Green metric is inferred.

## 3. Tensor concatenation needs scale loss

For composable coefficient seam records, balanced tensor concatenation joins the adjacent outer memory buffers. On fixed-degree shapes it is tensor reassociation followed by the admitted normalization, with norm at most one before graph weights.

For k and l active seams,

    b_s(k+l)/(b_s(k)b_s(l))=binomial(k+l,k).

This is unbounded, so it would be incorrect to call Y_s a Banach algebra under unrestricted cross-depth tensor concatenation. However binomial(k+l,k)<=2^(k+l), giving

    ||x tensor_balanced y||_s <= ||x||_(2s) ||y||_(2s).

Endpoint-incompatible pairs contribute zero; summing compatible pairs is bounded by the product of the l1 sums. The usual graded differential Leibniz identity extends from finite tensors using these bounds.

This operation concerns typed coefficient seam complexes. It is not a prescription to duplicate or multiply independently chosen root states of the full receiver.

## 4. A complete scale intersection

Take

    Y_infty = intersection_(integer s>=1) Y_s

with its countable family of norms. The natural inclusions for larger s are continuous. The compatible intersection is complete, and finite-depth, finite-shape tensors with approximated finite tensor coordinates are dense in each specified finite collection of seminorms.

The estimates imply continuous differential and jointly continuous balanced tensor concatenation on Y_infty. Associativity and the balanced pentagon hold by density; no extra collision or triangle parameter is added. Relative currents remain the independently constructed currents of the source sewing theorem.

Thus an all-depth receiver with continuous typed tensor operations is available, but as a scale intersection rather than as the unchanged single Hilbert or single Banach norm.

## 5. A compatible source domain and faithful map

For a relation-depth r source presentation, use the prior path-length weight multiplied by b_s(r):

    b_s(r) (1+n)^r a^n.

Take its endpointwise associated-layer quotient norms, then the l1 sum over r and endpoints. Denote that Banach source domain X_s. The finite-depth estimates give a contraction X_s -> Y_s in bottom degree. Restriction to the compatible scale intersection X_infty gives a continuous map into Y_infty.

Each endpoint interval has finite event length, hence only finitely many nonzero relation layers. Finite corner projections remain continuous. The same endpointwise injectivity proof therefore separates every source vector at every depth; it does not require uniform finite inverse bounds.

For theta truncation estimates replace (1+n)^r by (1+n)^(r+1). The factor b_s(r) occurs on both sides, so the prior operator error delta_K/a is uniform over r on this stronger source domain. This assertion is about the linear layer maps. No continuous multiplication theorem for these particular source quotient norms is being inferred from the target tensor estimate.

## 6. Relation to the closed-range obstruction

At fixed depth, b_s(r) is a constant. The forgotten-suffix family still prevents a bounded inverse in the original target topology. The scale construction controls increasing seam depth; it does not remove the increasing path-length mismatch.

Finite-endpoint paired observers still separate the source. Full strong-dual surjectivity, stable inversion, and a preferred physical topology remain different questions.

## Verification

`uv run python research/voevodsky/checkers/check_all_depth_seam_graph_norm.py`

Passed 2460 exact differential-weight identities and tensor-weight ratio checks. The functional-analytic construction and extensions are proved above; the checker does not claim an infinite spectral computation.
