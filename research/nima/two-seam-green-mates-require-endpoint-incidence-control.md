# Two-seam Green mates require endpoint incidence control

## Result

The actual Green mate of the two-seam differential does not extend to the entire existing depth/feature scale intersection. No fixed enlargement of those radii bounds it. The obstruction already occurs on vacuum records, independently of Clark conditioning.

An endpoint-length moment is sufficient on this fixed two-seam complex. Thus the observer graph domain from `the-factorial-attachment-has-a-continuous-observer-dual-square.md` is a genuinely proper domain, not merely a cautious definition awaiting an automatic bounded extension.

## 1. A mixed observer with many incident preimages

Work on a Boolean endpoint interval of event length n>=2, with outer source the empty subset and target the full subset. Let z contain the first n-1 events and let e be the final edge z->y.

In the unshifted balanced two-seam complex choose y_n whose first separator is the vertex at the outer source and whose second separator is the forgotten edge e. All three coefficient buffers and the seam letter are vacuum. Its active-edge count is one and its feature count is zero.

For each of the n-1 initial edges a_i:empty-> {i} with i in z there is a bottom record x_i with separators (a_i,e) and all buffers vacuum. The first-seam boundary contributes minus y_n; its other endpoint contribution is at {i}, not at the outer source. The second-seam boundary lies in an edge/vertex sector, not the vertex/edge sector of y_n.

There are no incoming edges at the outer source. No feature-bearing preimage pairs with these vacuum buffers. These are therefore exactly the preimages contributing to the Green mate:

`d2^sharp(y_n)=-sum_(i=1)^(n-1) x_i`.

The records have distinct typed edges and unit vacuum pairing. The formula follows directly from the differential and the prescribed pairing, not from a fitted Gram matrix. Shifting the complex and using the cochain dual convention changes at most its overall sign.

## 2. No depth/feature-radius repair

Let b_s(k)=(2 lambda s)^k k!. Then

`||y_n||_(s',b')=b_(s')(1)`,

`||d2^sharp(y_n)||_(s,b)=(n-1)b_s(2)`.

For any fixed s,s',b,b', their ratio grows without bound. Neither feature-radius changes nor depth-radius changes supply the missing endpoint-valence factor: the feature count is zero and the active counts stay one and two.

This obstruction holds in the actual two-seam attachment target J_(R,2)[-1]. It does not require summing over an unbounded number of seam factors.

## 3. A receiver vector outside the representable-mate domain

Choose the y_n in distinct outer endpoint corners and put

`y=sum_(n>=2) y_n/n^2`.

It belongs to every existing depth/feature seminorm, since its norm is b_s(1) sum 1/n^2. If its transposed functional had a Green representative z in the cut-l1 receiver, testing against each x_i would force the coefficient -1/n^2 in that coordinate. Different outer corners cannot cancel.

Consequently any such representative would have norm at least

`b_s(2) sum_(n>=2) (n-1)/n^2=infinity`.

There is no representable mate in even one of these target spaces. The transpose still exists as a continuous functional, because the forward differential is bounded. What fails is its representation by a cut-l1 observer.

This proves strict containment of the observer graph domain in the receiver scale intersection. Each finite truncation has an ordinary finite Green mate; completion is the substantive issue.

## 4. A sufficient endpoint-length domain

Retain the existing shape norms and add the scalar observer weight 1+n(c), where c is the outer endpoint interval. At fixed seam count r=2 this gives a sufficient domain for the mate.

Here is the local count on the admitted untruncated normal forms. A vertex in an n-event Boolean interval has at most n incident elementary edges. Replacing a vertex separator by an incident edge has at most two channels: vacuum insertion reversed, or extraction of one feature from the adjacent memory buffer. At a fixed homogeneous memory shape that extraction has a uniquely specified end slot; it is not unrestricted word splitting.

The local insertion norm is at most lambda=max(1,tau/sqrt(w_seam)). Its Green mate has the same upper bound on the ambient signed Hilbert carrier: the fundamental symmetries have norm one. Total feature count is preserved, so the feature-radius multiplier cancels.

A term with k active edges has 2-k vertex separators. The graph ratio for the mate is

`b_s(k+1)/b_s(k)=2 lambda s(k+1)`.

Counting at most 2n channels per vertex and using (2-k)(k+1)<=2 for k=0,1 gives

`||d^sharp y||_(s,b) <= 8 lambda^2 s ||(1+n)y||_(s,b)`.

The mate is zero out of the all-edge sector in this reversed direction. Signs from the two tensor positions and the attachment shift do not alter the estimate. Triangle inequalities handle collisions between outputs.

Finite normal forms are dense in the strengthened norm. The estimate extends their mates continuously, and the Green transpose identity passes to the limit by boundedness of the pairing. Thus the all-radius endpoint-moment domain embeds continuously into the maximal graph domain.

This is a sufficient domain, not an equality: cancellations within a corner can reduce a mate norm, so necessity of an absolute endpoint moment for every observer is not asserted. Nor is this a uniform statement over arbitrary seam count r; additional inactive-vertex multiplicity must then be controlled.

## 5. Consequence for the paired attachment

The continuous graph-domain square already constructed remains valid. Its observer restriction is essential. A convenient explicit subdomain is now available by adding the endpoint-length moment, with the displayed scale bound.

No finite Green form, source attachment, or forward receiver differential is changed. This does not identify the graph observer complex with the full continuous dual, or repair the previously exhibited failure of joint-observer surjectivity onto the source dual.

## Verification

`uv run python research/nima/checkers/check_two_seam_green_mate_incidence.py`

The checker enumerates actual vacuum bottom boundaries in finite Boolean intervals, transposes their coefficients against the mixed observer, and checks the exact n-1 multiplicity and graph ratios. The infinite-domain exclusion and sufficient endpoint-moment estimate are the arguments above.
