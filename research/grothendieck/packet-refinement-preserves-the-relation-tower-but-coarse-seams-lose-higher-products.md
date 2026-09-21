# Packet refinement preserves the relation tower, but coarse seams lose higher products

## Result

The finite source relation towers are compatible under prime-packet enlargement, not just dimensionally similar. With the forcing and coefficient realization held fixed:

1. chamber refinements compose exactly and preserve every admitted event window;
2. the old marked source is a convex corner of the larger source;
3. every ideal power, associated layer, and source connecting map restricts exactly to the old packet;
4. one-sided derived quotient has a uniform two-term model at every filtration stage.

The first new stage is explicit: six primes give a 720-dimensional I^3, detected by three labelled seams. Its raw degree is -3, and its derived attachment realization requires shifting the joint complex by [-2].

There is also a genuine obstruction to arbitrary cut refinement AFTER compression. Two coarse first-derivative seam records can be zero while their three-seam refinement is nonzero. Thus the closure construction must retain the derived relation tower before replacing each block by its conormal seam image.

## 1. Packet and coefficient maps

Let A be a finite set of primes and A' a larger finite set. Vertices are subsets of the packet, with elementary arrows adding one prime. Let S_A be the free two-mark path algebra, with actual source and target idempotents retained.

The endpoint coordinate of a vertex U is 2 times the product of its primes, or its logarithm in the analytical model. The smaller endpoint set is contained in the larger one. Thus every old chamber is partitioned into new chambers.

Define alpha_(A,A') by sending an old chamber indicator to the sum of its new subchamber indicators. These sums have disjoint nonempty supports, so alpha is injective. Nested refinements satisfy

alpha_(A',A'') alpha_(A,A') = alpha_(A,A'').

An old event window is the sum of all chambers between its unchanged endpoints. Hence alpha carries it to precisely the same window in the refined coordinates.

For a fixed forcing and fixed analytical feature map, integration over those windows is additive. Therefore L_(A') alpha_(A,A')=L_A. This uses the same analytical data, not a separately calibrated receiver at each packet size. If feature envelopes are W_A=W0_A+J W0_A for a fixed J in a common Hilbert carrier, their inclusions are compatible as well.

This is coefficient breakpoint refinement. It does not insert a new arithmetic generator inside an old elementary event.

## 2. The strict corner identity for all relation powers

Let e be the sum of the larger source's vertex idempotents belonging to the old packet face. A monotone source path with both endpoints in that face cannot leave it: an added new prime could never be removed. Therefore

S_A = e S_(A') e.

The algebra inclusion is a CORNER inclusion; it does not send the old identity to the entire new identity. Ignoring this distinction would incorrectly merge source types.

Define the record kernel I_A using the full tensor algebra of the coefficient space, with endpoint labels. Since the coefficient refinement is injective and commutes with recording,

I_A = e I_(A') e.

For every k, convexity gives the stronger identity

I_A^k = e I_(A')^k e.

Indeed, insert the vertex idempotents between factors in a product. A surviving product with old outer endpoints can have only old intermediate vertices. Each factor then belongs to the old typed kernel. The reverse inclusion follows from multiplication compatibility.

Consequently, writing G_A^k=I_A^k/I_A^(k+1),

G_A^k = e G_(A')^k e.

Restriction M -> e M e is exact on the relevant bimodule categories. It sends the larger short exact sequence

0 -> I^(k+1) -> I^k -> G^k -> 0

to the corresponding old sequence. Thus it sends the larger connecting map to the old connecting map in the derived category. These restriction identifications compose exactly for nested packet faces.

This proves compatibility of the source filtration and attachments, without claiming that one fixed finite corner exhausts the enlarged source.

## 3. A uniform derived quotient model

For any finite packet, S is hereditary. Every I^k is a left submodule of S and therefore projective; use I^0=S. Thus

[I^(k+1) -> I^k]

is a projective model of G^k, in degrees -1 and 0.

With B=S/I, ordinary tensor on these terms computes derived base change:

B tensor_S I^k = G^k,

B tensor_S I^(k+1) = G^(k+1).

The induced differential is zero. Hence

B tensor_S^L G^k = G^k direct_sum G^(k+1)[1].

Both displayed layers are projective as left B-modules, since extension of scalars preserves projectives. The image of the connecting map is projection onto G^(k+1)[1]. For any right B-module receiver X,

X tensor_S^L G^k =
 (X tensor_B G^k) direct_sum (X tensor_B G^(k+1))[1].

No flatness assumption on X is needed.

These explicit models also restrict under the corners in section 2: term by term they become the old models, including the connecting projection. This is a base-change compatibility statement for this particular tower, not an unrestricted assertion that corner restriction commutes with every derived tensor product.

Higher relation powers therefore enter successive Tor_1 calculations with different second arguments. They do not require a nonzero Tor_2 over the hereditary source.

## 4. Receiver capacities: an important qualification

Computing I_A with a finite memory cap at least the maximum path length gives the same source kernel as the full tensor recorder. This justifies the source comparison above.

It does NOT make the inclusion of cap-N memory into cap-(N+1) memory a module intertwiner on arbitrary states. Creation kills a top-degree state at the smaller cap but may preserve it at the larger cap. Similarly, inclusion of truncated tensor algebras is not generally multiplicative across the truncation boundary.

For an all-state comparison between two finite packets, use ONE common capacity at least the larger packet's path length and compatible prepared source frames. Inclusion of the old feature envelope into the new one then intertwines every old generator at that common capacity, including the zero action at the common top degree.

At that capacity the receiver module map X_A -> X_(A') e is B_A-linear. Since the layers G_A^k are left B_A-projective, tensoring this inclusion with a layer preserves injectivity. Cutting the larger right endpoint back to the old face leaves precisely the old source tower, now with the larger coefficient receiver restricted to that face.

For an unbounded directed system, the algebraic full tensor recorder or a graded capacity system is available. A completed bounded analytical closure operator, with uniform estimates, is not proved here.

## 5. The first higher product: six primes

There are no relations of event length zero or one. Thus a product of r ideal factors requires at least 2r events. This concerns source event length, not retained-record degree.

In a packet of exactly 2r primes, every nonzero element of I^r has full root-to-terminal support. Each factor in a minimal product must be a two-event diamond relation. Each such local relation space has dimension two, independently of chamber refinement: the three interval pieces are independent, and the two marked routes have the established six-dimensional image.

An ordered partition of the 2r primes into pairs specifies every intermediate vertex. There are (2r)!/(2!)^r such partitions. The corresponding tensor product of local relation spaces has dimension 2^r.

Multiplication is injective on their labelled direct sum. Every full path determines its ordered two-event blocks uniquely, so different partitions have disjoint path support. Within a partition, free path concatenation is the tensor product of the local path spaces and preserves the relation-space injection. All products are exhausted this way.

Therefore

dim I^r = (2r)!, for a packet of exactly 2r primes.

This gives dimensions 2, 24, and 720 for r=1,2,3. In particular, six primes require a nonzero I^3 stage; I^4 is zero there.

The checker certifies the 720 products with a selected-coordinate left inverse: a fixed route order in each pair and the two local marking patterns select an identity minor. No full terminal-rank extrapolation is used.

## 6. The higher joint-seam shift

At the critical packet size 2r, form J_r as the direct sum over the labelled ordered pair partitions of the external tensor of their r local seam complexes. Its bottom degree is -r.

Tensoring the actual local derivative cycles yields an injective chain map

I^r[r] -> J_r.

The local cycles are literal closed vectors; no representatives modulo boundaries are selected. There are no boundaries entering the bottom degree. Coherent reassociation of the tensor factors uses the standard cochain tensor differential and does not erase intermediate vertices.

Apply section 3 to G^(r-1). Since I^(r+1)=0 at this packet size, its next layer is I^r. Root support identifies the shifted receiver term with

(X_s tensor_C I^r)[1].

The shift-correct seam comparison is consequently

E_X(G^(r-1)) -> (X_s tensor_C I^r)[1]
                  -> X_s tensor_C J_r[1-r].

The first map is the derived connecting projection; the second is the tensor of the actual local seam maps, shifted as displayed. On the canonical source-product image it realizes that projection exactly, with no ambient projection or fitted inverse metric.

For six primes, r=3: use three seams and shift J_3 by [-2]. Raw degree -3 then becomes degree -1. The shifted product term has dimension 720 times the root-carrier dimension.

For old endpoint configurations embedded into a larger packet, these cycle maps commute with coefficient refinement, since the event windows and their derivatives commute with it. This does not prove a faithful joint-seam presentation of every nonminimal associated layer in the larger packet; those layers can involve additional factorization relations.

## 7. A strict cut-refinement obstruction

Let a,b,c be nonzero local diamond relations on three successive two-event blocks. At six events their product a b c is nonzero.

If the first four events are compressed into one first-derivative seam before refining the cuts, then

D(a b) tensor D(c) = 0,

because D kills I^2. Likewise D(a) tensor D(b c)=0.

But keeping all three cuts gives

D(a) tensor D(b) tensor D(c) != 0.

Therefore there is no linear refinement map from those already compressed two-seam records that recovers the three-seam record of every source relation product: it would have to send zero to a nonzero vector.

This obstruction is distinct from coefficient breakpoint refinement or reassociating an already retained tensor product. Those operations are compatible. Changing the number of relation blocks after discarding their internal product layers is not.

The needed refinement domain must retain the internal derived relation layers of each block before applying the conormal seam observation. The uniform tower in section 3 provides the source data for such a construction; the present note does not yet build every general cut-refinement map between those enriched block complexes.

## 8. What is established and what remains

Established:

- a strict packet-compatible source relation filtration and its connecting maps;
- coherent coefficient refinements and the precise common-capacity receiver condition;
- the uniform derived quotient formula for every associated layer;
- the 720-dimensional first triple-product stage and its shift-correct three-seam realization;
- an explicit no-go for refining cuts after first-derivative compression.

Next gate: construct the enriched block complexes and their refinement maps BEFORE that compression, retaining the internal shifted layers. In larger packets, their joint maps must descend through the relations between different product factorizations. Merely tensoring more local conormal spaces does not establish that descent.

The resulting finite compatibility is necessary for a single closure construction, but is not yet a proof of a uniformly bounded completed analytical operator.

## Verification

`python research/grothendieck/checkers/check_packet_refinement_relation_tower.py`

Exact checks cover 160 event-window refinement squares, 441 convex old endpoint intervals, nested refinement composition, the product identity minors in dimensions 2,24,720, the shift formula, and a three-block cut-refinement hostile.

The ideal-power corner identity and general derived quotient formula are proved above. No formal implementation of their derived module categories is claimed.

References:

- `research/nima/derived-terminal-quotient-retains-the-product-attachment-as-a-shift.md`;
- `the-derived-connecting-projection-has-a-shifted-joint-seam-realization.md`;
- `the-four-prime-relation-layer-has-a-forced-nonsplit-attachment.md`.
