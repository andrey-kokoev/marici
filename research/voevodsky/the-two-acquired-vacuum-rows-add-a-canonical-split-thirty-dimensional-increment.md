# The two acquired vacuum rows add a canonical split thirty-dimensional increment

## Result

For the specified background-three and background-four unit-vacuum acquisitions, the restriction from the enlarged saturated observer SPLITS canonically as a source-bimodule map:

    E^+ ~= E direct_sum V_3 direct_sum V_4.

Each V_A has dimension 15. The restriction kernel is therefore

    D=V_3 direct_sum V_4, dim D=30,
    dim(F^1 D,F^2 D,F^3 D,F^4 D)=(30,12,2,0).

The splitting preserves the inherited ideal-depth filtration. There is no new coupling to the old observer in this enlargement. Under this splitting the adjacent filtered class is

    tau^+=(tau,0,0).

The old nonzero filtered attachment is retained; the two new adjacent components are filtered-nullhomotopic. This does not mean the new module actions are trivial or that the acquisitions reveal no new information.

Input: `acquiring-the-background-three-and-four-vacuum-rows-preserves-the-filtered-attachment.md`.

## 1. A vacuum seed is one actual path coefficient

Let p=(2,3,5,7,11,13), and define the ordered chain

    a_0=A, a_i=A product_(r<i) p_r, i=1,...,6.

The selected vacuum row chi_A has seams

    A->2A, 6A->30A, 210A->2310A,

with all remaining buffers vacuum and outer endpoint 30030 A.

It vanishes on every source word with a retained mark. On entirely forgotten paths its seam labels force the UNIQUE word

    (2,3,5,7,11,13).

Its coefficient on that word is one. The checker independently enumerates all 720 forgotten path orders and their cut triples to verify this assertion. Retained words are excluded by homogeneous feature degree, not by numerical smallness.

## 2. Compute the entire saturation, not only its cubic layer

A nonzero left/right context of this coefficient functional must be an exact prefix and suffix of that ordered word. The contextual functional on the remaining source is the coefficient of a contiguous subword

    (p_i,...,p_(j-1)), with outer corner (a_i,a_j).

Restrict to the actual source ideal I. For subword lengths zero and one, the all-forgotten corner has only one path and its terminal recorder is injective; positive-feature ideal elements are invisible to the vacuum functional. These contextual restrictions are zero on I.

For every length j-i>=2, the restriction is nonzero. An explicit I-source representative is the canonical forgotten subword minus the same word with its first two events exchanged. This is a forgotten diamond times the remaining path and is evaluated to one.

Thus Sat(chi_A)|_I has precisely the basis indexed by

    0<=i<j<=6, j-i>=2.

There are 5+4+3+2+1=15 such intervals. Their outer corners are distinct, so the functionals are independent. Every contextual functional has already been included. This proves completeness of the saturated basis.

Let V_A be its dual evaluation module, with basis z_(i,j) dual to those coefficient functionals. The representatives above evaluate to this basis, so the description includes actual source realizations rather than only an abstract dimension count.

## 3. Full source action and ideal-depth filtration

A forgotten chain edge a_i->a_(i+1) acts on the left by

    z_(i+1,j) |-> z_(i,j),

and on the right by

    z_(h,i) |-> z_(h,i+1),

whenever the source basis interval exists. Every other prime edge acts by zero, including all retained edges. Vertex idempotents project onto the stated initial or terminal labels.

These formulas determine all path actions. The checker compares them with actual multiplication of the I-source representatives for all 192 prime edges in each packet. Off-chain paths cannot match the selected canonical coefficient.

A consecutive two-event forgotten diamond acts through its canonical term; its reversed term passes through an off-chain vertex and is zero. Therefore

    I V_A=V_A I=span{z_(i,j):j-i>=4},
    I^2 V_A=span{z_(0,6)}, I^3 V_A=0.

The inclusions in the other direction follow because every contributing ideal factor requires at least two events. Hence the dimensions are

    dim V_A=15, dim I V_A=6, dim I^2 V_A=1.

These are powers of the actual source ideal, not the joint-action ideal of the earlier abstract gain fixture. The left and right images here really coincide.

The blocks have nonzero internal source actions. They are not fifteen independent trivial scalar modules.

## 4. Why neither new block can couple to the old observer

Every original detector is supported inside the background-two packet, whose maximal terminal vertex is 60060. A contextual functional from any of these detectors can only be supported at a source corner whose terminal vertex divides 60060.

For A=3 the chain is

    3,6,18,90,630,6930,90090.

Every nonzero interval functional has terminal index j>=2. Its terminal therefore contains 3^2, whereas 60060 contains only one factor of 3.

For A=4 the chain is

    4,8,24,120,840,9240,120120.

Every nonzero interval functional has a terminal divisible by 2^3, whereas 60060 contains only 2^2.

Thus every nonzero corner of each new block is outside the support of the old observer. The two new blocks also have disjoint corner supports; their possible terminal lists do not intersect.

Each saturated detector space is a source submodule. Disjoint corner supports consequently give the direct sum

    Omega^+=Omega direct_sum Sat(chi_3) direct_sum Sat(chi_4).

Dualizing these finite-dimensional spaces gives the asserted decomposition of E^+. It is not merely a decomposition of vector spaces or of top graded pieces.

Moreover Hom_(S-S)(E,V_3 direct_sum V_4)=0: any equivariant map preserves vertex corners, and there are no common supported corners. Therefore the section of E^+->E is unique. This is the precise sense in which the splitting is canonical for the declared source labels and detector families.

The section is NOT compatible with the enlarged evaluation of every same source: a source invisible in E can have nonzero new vacuum evaluations. There is no evaluation-compatible isomorphism identifying the enlargement with the old observer.

## 5. The restriction kernel with its inherited filtration

The old lower observer is unchanged and the new blocks map to zero there. Consequently

    K^+=K direct_sum V_3 direct_sum V_4,
    N^+=N direct_sum I V_3 direct_sum I V_4,
    L^+=L direct_sum I^2 V_3 direct_sum I^2 V_4.

For D=ker(E^+->E), the inherited flag is therefore

    D superset I V_3 direct_sum I V_4
      superset I^2 V_3 direct_sum I^2 V_4 superset 0.

Its dimensions are (30,12,2,0), and its successive graded dimensions are (18,10,2). The artifact provides every basis corner and the sparse left/right edge-action matrices.

This resolves the earlier unknown total increment. Exactly two of the thirty additional structural directions lie in the deepest retained ideal layer.

## 6. The new adjacent filtered components are zero

Keep the common source extension B=G_3 -> A=J_2/J_4 -> G_2. Under the splitting, its observed map decomposes as

    f^+=(f,f_3,f_4).

For each new block, source evaluation itself restricts to

    H_A:A->I V_A, H_A i=f_A.

This is a filtered extension of f_A: A has levels (A,A,B,0), and V_A has levels (V_A,I V_A,I^2 V_A,0). Evaluation sends I^2 sources to I V_A and I^3 sources to I^2 V_A.

Hence the pushout along f_A is zero even in the levelwise exact filtered category. Additivity of the finite direct sum gives

    tau^+=(tau,0,0).

The older lower-filtration homotopy is still needed for the old component's UNFILTERED vanishing. The new components require no such filtration escape.

This does not identify relative-boundary classes on I V_A/I^2 V_A with the adjacent source pushout. Nor does it assert that all extensions involving a new block split.

## 7. Acquisition and support boundaries

The thirty-dimensional increment describes formal source-action saturation. The two measured scalar readings alone do not determine all thirty coordinates. Contextual observation states and acquired numerical constraints remain distinct.

No row is installed for the unacquired tail, and no endpoint aggregation is made equivariant. The conclusion is specific to the canonical selected vacuum rows at backgrounds 3 and 4 and the old background-two detector support.

Different selected seam words can have different contextual supports. Additional old detectors at other backgrounds could also destroy the disjoint-support argument. Neither case is covered automatically.

## Verification

    python research/voevodsky/checkers/check_vacuum_acquisition_increment.py

The standard-library checker reconstructs the vacuum coefficient, its complete contextual interval basis and actual I-source representatives; checks all prime-edge actions; computes both ideal images; and verifies every support exclusion used in the splitting proof.

Artifact: `results/vacuum-acquisition-increment.json`.

The completeness of saturation, the splitting and the filtered extension decomposition use the explicit source arguments above, not just the reported ranks. No new theta integration or numerical calibration assumption is required.
