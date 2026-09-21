# Endpoint-radius observers close the paired two-seam comparison

## Result

The two-seam Green differential has an explicit complete observer domain. Polynomial endpoint moments suffice for that differential, but do not suffice for the mate of an artificial-cut normalization. Endpoint-exponential radii, together with the existing feature radii, control both.

On the new observer scale, Green mates, the dual connecting square, and each fixed finite normalization diagram are continuous. This is a strengthened observer topology on the existing carriers and pairings, not a perfect-duality equivalence or a change to the source Green form.

## 1. Polynomial moments give a complex, but not all paired sewing

Write n(c) for outer endpoint event length. On the fixed one- and two-seam targets, take all seminorms

`||(1+n)^p y||_(s,b)`, for integers p>=0 and s,b>=1.

The bound proved in `two-seam-green-mates-require-endpoint-incidence-control.md` implies

`||(1+n)^p d^sharp y||_(s,b)
 <= 8 lambda^2 s ||(1+n)^(p+1) y||_(s,b)`.

The ordinary differential preserves endpoints and retains its old graph bound. Finite normal forms are dense in the intersection. The finite mate identities therefore extend, including the signed cochain identity d_G^2=0. Thus this is already an explicit complete observer complex contained in the earlier representable-mate graph domain.

A forward normalization N preserves outer endpoints. Its old contractive estimate therefore holds at every endpoint-moment seminorm. The same is not automatically true of N^sharp.

## 2. A normalization-mate hostile

Consider a bottom two-seam vacuum record in an n-event interval. Its first edge is the first event, its last edge the last event, and the middle buffer is vacuum. Between these edges lies a Boolean interval of length n-2.

Before balancing, the middle buffer can be split at any intermediate vertex v. There are 2^(n-2) such vertices. Each fine record has two vacuum buffers, and N sends it to the same coarse record.

With the prescribed unit vacuum pairings, the Green mate of that coarse observer is the sum of all these fine records. Its fine cut-l1 norm is exactly 2^(n-2) times its coarse norm. Graph and feature radii do not change this ratio: both sides have two active seams and no features.

At distinct outer corners of lengths 2m, sum these coarse observers with coefficients 2^(-m). This lies in every polynomial endpoint-moment seminorm. Its normalization mate has contributions proportional to 2^(m-2), and is not even in the unweighted fine cut-l1 space.

Therefore an observer complex intended to support BOTH differential mates and these reverse normalization comparisons needs more than the polynomial-moment construction. This hostile concerns the actual external-to-balanced cut map, not an invented cross-degree pairing.

## 3. The explicit endpoint-radius scale

Keep seam count at most two and each specified external presentation with finitely many artificial cuts. Define

`||y||_(R,s,b)=sum_shapes R^(n(c)) b_s(k) b^d ||y_shape||_raw`,

where k is active seam count, d is total feature count, and R,s,b>=1. The raw norm retains all original memory/seam multipliers and typed labels. Take the intersection over integer R,s,b.

Call this complete locally convex space O_exp. Completeness and finite-normal-form density follow from the compatible weighted l1 coordinate description. Hilbert tensor coordinates may be approximated inside each fixed shape. No finite-dimensional approximation is treated as a spectral rank test.

The endpoint-radius factor leaves the forward differential bound unchanged. Since 1+n<=2^n,

`||d^sharp y||_(R,s,b) <= 8 lambda^2 s ||y||_(2R,s,b)`.

After cohomological reversal, insert the established sign (-1)^(degree+1) to obtain d_G. It is continuous on O_exp. The finite identities d_G^2=0 and beta d_G=d^vee beta extend by density. Thus every observer in this stronger intersection has a representable mate in the same intersection.

This does not say the mate is bounded on one unchanged Banach stage, or that O_exp equals the maximal graph domain.

## 4. Normalizations and their mates

A forward artificial-cut normalization has norm at most one at every (R,s,b): it preserves outer endpoints, active seam count and total feature count.

For its mate, consider one homogeneous coarse buffer of feature length m, between comparable vertices in an n-event outer interval. There are at most 2^n choices of intermediate vertex and m+1 ways to split the feature word. On each fixed choice the Green mate is the prescribed tensor reassociation, with norm one; the multiplicative memory weights and the signature involutions do not introduce a new factor.

This is an estimate on the full ambient normal-form carrier. It does not require the observer to be a source-generated tensor. In particular it applies to a general Hilbert tensor coordinate by the same fixed-split isometries, not by choosing a coefficient expansion with an uncontrolled norm.

The fine shape-l1 sum is consequently bounded by

`2^n (m+1) <= 2^(n+m)`.

The endpoint radius and feature radius pay those two factors:

`||N^sharp y||_(R,s,b) <= ||y||_(2R,s,2b)`.

Here m is no greater than the total feature count. The bound includes vacuum buffers, for which m=0. The finite-cap versions are restrictions; the argument uses the admitted untruncated homogeneous shapes.

For q successive artificial-cut removals, iterating yields radius losses at most 2^q in R and b. Thus every fixed finite normalization diagram is continuous on the intersection. No uniform assertion about summing over arbitrarily many artificial-cut presentations is made.

Associators of already balanced normal forms are ordered isometries and preserve these weights. Their mates are their inverse reassociations. For normalizations, mates compose in reverse order by the finite Green transpose identity, and the resulting equalities extend by density.

Use the nondegenerate fine and coarse ambient pairings for these mates. Do not invert the potentially degenerate corrected fine form q_external+T_N. The independently constructed relative identity remains

`q_external+T_N=N^* q_balanced`.

Neither its correction current nor any source metric is changed here.

## 5. Attachment and continuous dual square

Restrict the observer construction in `the-factorial-attachment-has-a-continuous-observer-dual-square.md` to O_exp. The inclusion into its graph domain is continuous by section 3. Its beta map into the strong continuous dual is therefore a continuous chain map, now on an explicit space with no implicit representability test.

For the joint source map j and the connecting projection pi, retain

`F2^vee beta = pi^vee j^vee beta`.

Every arrow is continuous. The identity follows on finite records from F2=j pi and extends with the preceding scale estimates. Reverse normalization comparisons can now be included using section 4, on each fixed finite presentation diagram.

Endpoint-radius weights can also be paid on the primal attachment map: multiplying a target bound by R^n simply enlarges the source path radius by R. Thus the existing factorial source attachment maps continuously into the strengthened primal target with the same underlying normal forms. On inherited actual-letter source quotients, the same conclusion follows from their Q-radius estimate; no Gamma-weighted factorization comparison is needed.

The four-event translated-family obstruction to full source-dual surjectivity persists. Its event length is fixed, so the extra factor R^4 cannot prevent its analytical images from tending to zero. The stronger observer domain does not turn the paired square into a completed perfect-duality equivalence.

## 6. Scope of currents and depth

These are analytical ambient observers. They are not automatically forcing-resolved preimages. Separate bulk/forcing current assertions still require the previously specified forcing-resolved domain; they do not follow solely from the total Green beta used here.

The differential estimate is for seam count at most two. Larger or unbounded seam counts require control of the number of inactive vertex separators as well as endpoint incidence. This note does not silently extend that bound to arbitrary depth.

Established: an explicit complete observer complex, controlled differential mates, controlled normalization mates, and the continuous paired first-attachment comparison on every fixed finite normalization diagram.

Not asserted: equality with the maximal graph domain, unchanged-stage boundedness, arbitrary-depth summability, or completed tensor-Hom equivalence.

## Verification

`uv run python research/nima/checkers/check_endpoint_radius_observers.py`

The checker counts actual intermediate vertices and homogeneous feature splits, checks the radius/moment inequalities, and verifies finite normalization/transpose pairing identities with independent coefficients. The continuous extensions and the infinite polynomial-moment hostile follow from the proofs above.
