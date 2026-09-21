# Source-generated derived composition detects the conormal relation layer

## The general identification

Let S be the finite free marked path algebra and let rho be the typed terminal record representation, retaining source and target blocks. Put

I=ker rho, B=S/I.

Use a common record capacity at least the maximum source event length. The record representation is multiplicative: each marked event acts by right multiplication by its emitted letter or the scalar unit, with its endpoint block retained. Consequently I is a two-sided ideal, not merely the kernel of one untyped scalar observation.

At fixed endpoints s,t, the source-generated prefix and suffix modules are

M=e_s B, N=B e_t.

There are canonical identifications

M tensor_S N = e_s B e_t,

Tor_1^S(M,N)=e_s (I/I^2) e_t.

Thus negative homology detects the conormal relation module I/I^2. It is not in general the entire terminal kernel I.

## Proof

Apply right-derived tensor with the left S-module B to

0 -> I -> S -> B -> 0.

The exact sequence identifies Tor_1^S(B,B) with the kernel of

I tensor_S B -> S tensor_S B.

The first term is I/I^2. The displayed map is zero because every element of I acts as zero in B. Hence Tor_1^S(B,B)=I/I^2. Ordinary tensor gives B tensor_S B=B.

Taking the source and target idempotent summands yields the two corner formulas above. These formulas hold for a general quotient algebra; for our free acyclic source S, heredity additionally implies Tor_j^S(-,-)=0 for j>=2.

The argument concerns source-generated quotient modules. It does not replace the larger arbitrary-memory modules in the earlier bar fixture by assertion; those were different inputs and had different homology.

## Why the two-prime result was the whole kernel

The local event observation sends the two marked arrows to vacuum and a nonzero feature in different record degrees. Thus there are no degree-zero or degree-one kernel relations. Every element of I has event length at least two.

A product of two relations therefore has event length at least four. In any corner admitting only two or three events, I^2 vanishes. In those corners,

Tor_1^S(e_s B,B e_t)=e_s I e_t.

For the faithful diamond this gives H^(-1) dimension 2 and H^0 dimension 6, as identified in the preceding packet.

For the three-prime source, the marked path space has dimension 48 and terminal rank 26. Therefore the source-generated derived composition has

H^(-1) dimension 22,

H^0 dimension 26.

The two-dimensional joint-single-cut ghost space is a different kernel: it concerns both cut marginals together, not terminal composition. It must not be substituted for these twenty-two terminal relations.

## Four events: the first nonzero product layer

In the four-prime root-to-terminal corner, an I^2 product can only split as two events followed by two events. There are six possible middle vertices, one for each two-element prime subset.

At each such vertex the prefix diamond has a two-dimensional relation space and the suffix diamond has a two-dimensional relation space. Their four tensor products multiply into the full source path space. This multiplication is injective on each tensor product because the free path source retains the full marked word and its unique length-two cut. Different middle vertices occupy disjoint source blocks.

Consequently

dim e_s I^2 e_t =6 times 2 times 2=24.

Every product is invisible to terminal recording, but these twenty-four composite relations are also zero in I/I^2. Hence

dim H^(-1)=dim e_s I e_t -24

in this four-event corner. The total four-event terminal rank is not computed in this packet; the formula and the product-layer dimension do not require it.

At this cutoff I^3=0 by event length. Nevertheless there is no new Tor_2 carrying the product layer: the source algebra is hereditary. The distinction between ideal depth and derived homological degree remains essential.

## Meaning for closure and reconstruction

Derived source-generated composition exposes the first relation layer, not automatically every lost joint record. For complete source-kernel reconstruction one must retain I^2 as well as I/I^2, including their extension and multiplication data. A choice of representatives of I/I^2 alone is not canonical reconstruction of I.

This does not imply that the full derived correspondence with all additional structure forgets every product relation. It says specifically that its negative homology group alone cannot be identified with the entire source observation kernel once four-event products occur.

Nima's attachment-parameter construction supplies a compatible interpretation: a nonzero source relation is still a nonzero typed projective map before terminal observation. Passing to B and then to its conormal module are two distinct quotient operations. Neither turns those coefficients into cofiber objects without the stated attachment construction.

No Green-radical or positivity identification follows from the conormal formula.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_source_relation_conormal_layer.py`

Exact checks passed:

- all twelve prefix/suffix diamond instances have terminal rank six;
- both local kernel generators vanish;
- the twenty-four four-event products vanish under terminal recording;
- their source vectors are linearly independent;
- the three-event terminal rank is 26.

The Tor formula is proved from the quotient exact sequence above. The checker certifies its source-specific dimensions, not a formal derived-category implementation.

Related notes:

- `prior-path-kernel-results-identify-the-three-and-forty-seven.md`;
- `research/nima/joint-records-type-as-attachment-parameters-not-cofiber-objects.md`;
- `research/nima/prime-cube-faithful-observers-paths-relations-and-nested-reconstruction.md`.
