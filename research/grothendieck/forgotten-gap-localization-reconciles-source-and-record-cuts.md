# Forgotten-gap localization reconciles source and record cuts

## Result

For each retained-event mask, the source cuts mapping to one recorded cut form an interval. Treating movement across a forgotten event as an equivalence contracts this interval to one cut. The construction extends to simultaneous cuts, commutes with deleting and repeating cuts, and composes under further forgetting.

This supplies an explicit coherent comparison for the record construction. It also proves that the unmodified source cut sum is not preserved: localization is a substantive operation, not an equality of the original arithmetic endpoint diagrams.

## 1. Source positions and the rank projection

Let a route have n events, with cut positions 0,...,n. Retain the event positions

M={i_1<...<i_k} subset {1,...,n}.

The recorded word has k letters and cut positions 0,...,k. Define

p_M(j)=number of retained positions at most j.

The fiber over r is the nonempty interval

[L_M(r),R_M(r)],

where L_M(0)=0, L_M(r)=i_r for r>0, R_M(k)=n, and R_M(r)=i_(r+1)-1 for r<k.

For example, retain positions 1 and 3 of a three-event route. Source cuts 1 and 2 both give the recorded cut between the two letters. They differ only by passage across the forgotten second event.

## 2. The actual universal comparison: localization

Regard [n] as the ordinal category. Mark each elementary arrow j-1->j for which event j is forgotten. The rank projection p_M:[n]->[k] sends precisely these elementary arrows to identities.

It realizes the localization at the marked arrows. To prove this, the monotone lower section L_M:[k]->[n] satisfies p_M L_M=id. The pointwise arrows

L_M p_M(j)->j

are composites of forgotten arrows. They become equivalences after localization. Thus L_M and p_M are inverse equivalences after those arrows have been inverted. Equivalently, precomposition with p_M identifies diagrams on [k] with diagrams on [n] that take forgotten arrows to equivalences, with their full natural-transformation data.

There is also an upper section R_M and a pointwise comparison id->[R_M p_M], again using forgotten arrows. The two extremal contractions make the fiber comparison explicit rather than selecting arbitrary representatives.

The original discrete set of cuts is not equivalent to the recorded set. The equivalence is obtained after the declared marked-arrow localization.

## 3. All simultaneous cuts

Take q weakly ordered source cuts j_1<=...<=j_q, allowing repeated cuts and empty pieces. Apply p_M coordinatewise. For any recorded tuple r_1<=...<=r_q, its fiber is ordered pointwise and has

initial object (L_M(r_1),...,L_M(r_q)),

terminal object (R_M(r_1),...,R_M(r_q)).

Every such fiber therefore has a contractible nerve. Deleting a cut or repeating a cut commutes strictly with p_M and both sections: these operations simply delete or repeat a coordinate. This supplies compatibility across the multi-cut diagrams, not only a binary-cut calculation.

Suppose a second mask retains some of the positions already retained by M. Let K denote their indices within M, and let M_K be the resulting original positions. Then

p_(M_K)=p_K p_M,

L_(M_K)=L_M L_K,

R_(M_K)=R_M R_K.

The formulas follow directly from the indexed retained positions. Hence contraction is compatible with successive forgetting, with no new choices at the second stage.

These statements concern marked route ordinals and their cuts. They do not constitute a comparison theorem for every stable S-construction diagram without its realization data.

## 4. Why the naive scalar cut formula fails

Write S(w)=product_j(1+v_j). Expanding chooses a mask M, with recorded tensor word v_M. In

sum_(j=0)^n S(prefix_j) tensor S(suffix_j),

the summand v_(M,left) tensor v_(M,right) at recorded cut r appears

R_M(r)-L_M(r)+1

times. By contrast, deconcatenation Delta S(w) counts this mask and recorded cut once.

Even one event already detects the failure:

naive source cut sum =2(1 tensor 1)+1 tensor v+v tensor 1,

Delta(1+v)=1 tensor 1+1 tensor v+v tensor 1.

Thus the signature map is not a coalgebra map for the unmodified path cut coproduct. In particular, its augmentation sends a nonempty path to 1, unlike the usual path-coalgebra counit.

## 5. Corrected cut sum

Retain the mask during cutting and form the comparison category of source cuts related by movement across forgotten events. Each fiber has contractible groupoid completion and contributes one equivalence class rather than its number of original cut positions.

After this localization, summing over masks and recorded cuts gives exactly

Delta S(w)=sum_M sum_(r=0)^|M| v_(M,<=r) tensor v_(M,>r).

No reciprocal gap-length weights are fitted. At the Euler-characteristic level the fiber contribution is one because its nerve is contractible. For a single gap with m source cuts, this is the finite cancellation

sum_(a=1)^m (-1)^(a-1) binomial(m,a)=1.

For multiple cuts the pointwise-order fibers again have initial and terminal objects, hence Euler characteristic one. This yields iterated deconcatenation, compatibly with all cut deletion/repetition operations from section 3.

This is a homotopical correction of the counting object. It is not an identity between the original raw positive cut counts and their corrected values.

## 6. Atomic uniqueness after the cut comparison is specified

A single event has two marked cases:

- forgotten: its arrow is localized to the identity, recording 1;
- retained: it has no interior event cut, recording an increment a with Delta(a)=1 tensor a+a tensor 1.

In the completed tensor record, the primitive subspace for deconcatenation is precisely V. For any degree r>=2 the (1,r-1) cut component is an injective identification of V^(tensor r), so it vanishes only if that degree is zero. The degree-zero primitive component is also zero.

Fixing the degree-one chamber incidence therefore forces a=v. Additivity over the two marked cases forces 1+v, and composition forces the complete product signature. Thus a record functor preserving these localized marked cuts has no freedom to replace an atomic increment by exp(v)-1.

This removes the event-rule ambiguity within the declared marked-cut realization. The marking operation, additive summation over masks, and permission to invert forgotten arrows remain explicit parts of that realization; the bare cut-and-rejoin operator does not silently impose them.

## 7. Arithmetic endpoint boundary

For an arithmetic route, source cut j also carries an integer n_j. Moving across a forgotten prime event changes n_j to n_j p. These are distinct objects in the ordinary divisibility category, and the multiplication arrow is not invertible there.

Consequently a functor retaining those arithmetic endpoints does not factor through the above localization unless its target supplies the required equivalences. This is an exact factorization criterion, not merely a concern about lost information.

The comparison is valid on record coefficients, where a forgotten event acts as the unit. To claim that it preserves the full original arithmetic closure, one must either:

1. retain the endpoint-and-gap attachment diagram as additional source data alongside the coefficient record; or
2. exhibit a source-admitted target in which the forgotten arrows really become equivalences.

The first preserves the data without pretending that the plain coefficient coalgebra is the entire source. The second is a stronger realization theorem still to be established. Neither permits declaring the arithmetic integers equal just because their record coefficients agree.

## 8. Status and next closure task

Constructed: the marked-cut localization, its explicit lower and upper contractions, multi-cut compatibility, compatibility under nested masks, and the corrected coefficient-level cut formula. This also supplies a cut-based uniqueness theorem for the single-event rule.

Not established: an equivalence between unmodified arithmetic closure diagrams and their coefficient-only histories. The one-event cut count and the distinct endpoint labels show why that assertion would be false as stated.

The next faithful construction is an endpoint-decorated marked history object retaining the forgotten gaps as attachment data. Its coefficient projection should be the localization proved here. No Clark receiver or Green metric is constructed in this packet.

## Verification

`python research/grothendieck/checkers/check_forgotten_gap_cut_comparison.py`

Exact tests cover source lengths zero through six and zero through three simultaneous cuts: 11,648 cut tuples, 4,047 contractible fibers, and 1,093 nested masks. Tests verify both fiber extrema, cut deletion/repetition, section composition under nested forgetting, corrected cut multiplicities, and the nonidentity of raw source and record cut counts.

The all-length proofs are sections 1–6. Tests are finite regressions, not a formal verification of the general categorical localization theorem.
