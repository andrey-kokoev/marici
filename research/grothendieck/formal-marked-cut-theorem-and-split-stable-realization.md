# Formal marked-cut theorem and split stable realization

## Result

The typed marking and cut-index theorems are now checked in safe Cubical Agda. The finite rational source and marked path algebras also supply a split exact stable realization by derived extension of scalars. It lifts the decorated construction to complete cofiber diagrams without equating forgotten arithmetic arrows with identities.

The stable result is a categorical proof below, not an Agda formalization of derived module categories.

## 1. Formal theorem: arbitrary typed source graph

`agda/EndpointDecoratedHistory.agda` is parameterized by any vertex type V and edge family E:V->V->Type. It defines typed routes, Boolean markings, and cuts carrying their actual intermediate vertex.

Checked constructions and theorems:

- `erase-kept`: retaining every event and then forgetting marks recovers the source route;
- `kept-fiber-contractible`: among all markings there is exactly one all-retained marking, with its witness;
- `composition-mark-iso`: markings of a joined route are equivalent to a pair of markings of its two pieces;
- `rejoin`: the prefix and suffix at any typed cut rejoin to the original route;
- `cut-mark-iso`: restriction of markings at a cut is an isomorphism, with explicit inverse;
- `full-cut-iso`: the entire summand-index family for cutting a marked lift is isomorphic to the family for independently lifting the two cut pieces.

The last theorem is the objective indexing identity underlying

Delta_D L=(L tensor L) Delta_P.

The formal module does not implement rational vector spaces and their sums. Rather, it proves the actual index isomorphism which, on free linearization, gives that equality. Likewise the contractible retained fiber supplies the unique surviving summand in A L=id. These are not claims that the whole scalar module calculation has been formalized.

## 2. Fresh compiler verification

Command:

    agda --transliterate --safe --cubical --guardedness --no-libraries \
      -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
      -i research/grothendieck/agda \
      research/grothendieck/agda/EndpointDecoratedHistory.agda

Compilation succeeded with no holes or postulates. Cubical Agda reports `UnsupportedIndexedMatch` warnings on some indexed pattern matches: those functions are not guaranteed to compute when applied to transported inputs. The proofs themselves are accepted. This limitation is recorded, not suppressed or described as warning-free verification.

Log: `results/endpoint-decorated-history-agda.log`.

The existing exact Python checker separately verifies the concrete arithmetic fixture: 168 source routes, 1,040 marked histories, and 4,176 typed cuts.

## 3. Source and marked path algebras

Let R=Q[P] be the path algebra of the finite retained source category and S=Q[D] that of the marked graph. Their units are the sums of the sixteen vertex idempotents. Their dimensions are respectively 168 and 1,040.

The marked lift and all-retained extraction give unital algebra maps

l:R->S, l(e)=e^0+e^1,

a:S->R, a(e^0)=0, a(e^1)=e.

Both preserve the vertex idempotents. Noncomposable products remain zero, and composable paths are evaluated by multiplication. The generator identities imply

a l=id_R.

This is the algebra-level split identity proved by the preceding path construction and its unique retained summand. The map a does not send a forgotten arrow to an identity: it sends it to the zero morphism with the same typed endpoints.

## 4. Generated exact stable functors

Use perfect LEFT modules so the projective object R e_x has path morphisms in the chronological convention of the source algebra. Define

F:Perf(R)->Perf(S), F(M)=S tensor_R^L M,

G:Perf(S)->Perf(R), G(N)=R tensor_S^L N,

where the bimodule actions use l and a, respectively.

Derived extension of scalars is exact. It preserves perfect modules because it sends the free generator to the free generator, and preserves finite cofibers and retracts. No unproved flatness assumption is used; the tensor products are derived.

Associativity of derived tensor gives

G F(M) equivalent to (R tensor_S^L S) tensor_R^L M
             equivalent to R tensor_R^L M
             equivalent to M.

The right R-action on the intermediate R is induced by a l, which is exactly the identity. These equivalences are natural in M. Hence

G F equivalent to id_Perf(R).

On the vertex projectives, F sends R e_x to S e_x. A source edge map becomes the sum e^0+e^1. This is the actual marked lift, not an unrelated stable carrier chosen to have the same dimensions.

This makes F split faithful on mapping information. It is NOT generally fully faithful: a one-edge source Hom has its marked edge split into two independent target arrows, while F sees their sum. No equivalence Perf(R)=Perf(S) is asserted.

## 5. Lifting the main interval closure

For any complete interval diagram in S_n(Perf(R)), apply F pointwise. Exactness preserves zero objects and bicartesian squares, so the result lies in S_n(Perf(S)). Apply G pointwise for the reverse functor.

Naturality of G F equivalent to id yields

S_n(G) S_n(F) equivalent to id

for every n. The equivalences commute with restriction along the ordinal maps because the functors are applied pointwise. Thus the split realization is compatible with the entire interval-diagram construction, not merely with one selected cut.

Concretely, for a cofiber attachment u:A->B,

F(cofib u) equivalent to cofib(Fu),

and similarly for G. The comparison is generated by the universal property of the cofiber under an exact functor. It requires no independently fitted map between the quotient objects. Compatibility for nested cuts follows from the functorial cofiber construction in the stable category.

A source route can be realized by its vertex projectives and edge maps, prepending the zero object to obtain a filtration. Its interval cofibers give a complete closure diagram. Its marked realization is the pointwise image under F, and G recovers the original diagram up to the natural equivalence above.

This establishes a split stable realization in the canonical path-module model. Identifying it with another already prescribed stable or analytic source category still requires that category's realization functor.

## 6. What does not distribute

Although l(w) expands as a sum of marked route morphisms, a cofiber of that sum is not a direct sum of their cofibers. We never use such a distributivity claim.

For example in Perf(Q), cofib(0+id_Q) is zero, whereas cofib(0) direct_sum cofib(id_Q) has the nonzero summand Q direct_sum Q[1]. Exactness of a functor is not additivity of the cofiber operation in the arrow variable.

The stable lift therefore realizes the sum map as a single map with its actual attachment. It retains the distinction between the index-level path-cut theorem and the stable cofiber theorem.

## 7. Location of the coefficient projection

The coefficient observation P(e^0)=1, P(e^1)=v_e remains a further realization that drops the source object labels. Its ordinary deconcatenation does not strictly preserve the unlocalized source cuts. The forgotten-gap localization remains the required comparison there.

The stable construction above does not rely on P, invert forgotten source arrows, or select a Green metric. It provides a faithful attachment-bearing stage before coefficient projection.

## Status

Completed:

1. formal typed mask, composition, and cut-index isomorphisms;
2. a proof of split exact stable realization from the actual source and marked path algebras;
3. induced split realization on every complete interval-closure level.

Remaining:

- formal verification of the derived-category and S-construction layer;
- comparison to any externally prescribed source realization;
- elimination of the Agda indexed-transport computation warnings if stronger executable transport behavior is required.

No Clark receiver or arithmetic metric is claimed or modified.
