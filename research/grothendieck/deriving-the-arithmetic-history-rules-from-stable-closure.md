# Deriving the arithmetic history rules from stable closure

## Result

Ordered composition, rational linearity in the selected Perf(Q) realization, and the finite prime-path length supply substantial parts of the history construction. They do not force a unique nilpotent record algebra from the polymorphic closure operator alone.

The exact derivation has three levels:

1. the closure operation and its coherent cuts;
2. the admitted arithmetic event diagram, retaining routes;
3. the chosen linear record of that diagram.

Keeping these levels explicit exposes the part already forced and the remaining choice. The requirement that everything be internally constructed becomes a precise demand to specify the record functor, rather than quietly treat it as an output of the cut equivalences.

## 1. Composition is inherited from the closure diagram

A complete interval diagram contains its maps and all their compositional comparisons. Restriction at a cut and rejoining with the same attachment data provide compatible descriptions of the same composite. Evaluating such a diagram by a functor preserves composition and units.

For the admitted prime-event source, a route is an ordered sequence of typed arrows n->np. Evaluation therefore satisfies

H(w followed by v)=H(w) H(v)

in chronological multiplication convention. Associativity follows from composition of the complete diagram. The empty route has the identity value.

This establishes the compositional law. The target in which H takes values still has to be constructed. Equality of terminal integer labels does not equate the route arrows: the arithmetic adapter explicitly retains those routes and its two-order witness distinguishes them.

## 2. Where linearity comes from

Nima's explicit stable model is Perf(Q). Its degree-zero mapping groups are rational vector spaces and composition is bilinear. An exact realization in this model has additive structure; finite freely labelled source objects have their usual rational coefficient spaces. For the fifteen chambers, this gives V=Q^15.

Complex coefficients are obtained by extension of scalars. General stable categories supply additive mapping groups, not a distinguished complex scalar field. Thus Q-linearity belongs to the specified Perf(Q) model, while C-linearity belongs to its chosen complex realization.

A record of a single event expressed as a morphism from the chamber object is linear in that object. This is the relevant categorical requirement for the event increment; arbitrary nonlinear functions of its coefficients need not be morphisms of the chosen linear category.

## 3. Natural linear event recording forces 1+v

Suppose the history receiver is tensor-graded and its single-event record has the form

U_V(v)=1+j_V(v), j_V(v)=sum_(r>=1) j_(r,V)(v).

Assume j is a natural linear map of chamber objects, preserves augmentation, and its first-degree component is the declared chamber incidence. Naturality under scalar dilation 2 id_V gives

j_(r,V)(2v)=2^r j_(r,V)(v).

Linearity gives j_(r,V)(2v)=2 j_(r,V)(v). Over Q, 2^r-2 is invertible for r>1, so every higher-degree component vanishes. The degree-one component is v. Consequently

U_V(v)=1+v.

This derives the one-event rule from the natural linear record specification. It also explains why same-event powers are absent. The natural linear record specification itself is part of choosing a morphism of the linear realization; the bare cofiber theorem does not mention this record map.

Combining this with section 1 yields

H(w)=product_(events in w)(1+v_event).

Its degree-r term is the sum over all ordered choices of r distinct event positions. The source signature formula follows by induction from the two derived rules.

## 4. Source-length nilpotence is genuinely forced

The retained squarefree four-prime source has sixteen objects and 168 typed paths, including identities. A nonidentity arrow adds a previously unused prime. Every composable string of five nonidentity arrows is impossible.

In the rational category algebra of the free retained path category, let J be the ideal spanned by positive-length paths. Its powers are spanned by paths of length at least k. Therefore

J^5=0, J^4 != 0.

Exact dimensions of J^k, k=0,...,5, are

168,152,120,72,24,0.

This is a consequence of the admitted event source. It is independent of a chosen observation or energy form. The nilpotence concerns positive-length paths; an identity map in a four-step closure diagram remains an identity under every power.

## 5. The tensor truncation is a finite record quotient

All actual source routes have at most four events. Under the one-event rule, their forward records have degree at most four. Projection to T_<=4(V) therefore preserves every coefficient of those records.

There is nevertheless an important distinction:

- the typed path algebra kills products of noncomposable arrows;
- the tensor record algebra permits arbitrary products of chamber letters, then kills degrees above four.

These are different algebras. Source-length nilpotence does not by itself identify their multiplication laws. The tensor receiver is a realization of the typed paths, with endpoints retained as structural indices.

The finite tensor quotient is sufficient for this protocol. The full degree-completed tensor algebra is another receiver: the same forward records have no degrees above four, while comparison inverses contain higher-degree terms. Both support coherent comparisons. The closure laws alone do not select the finite quotient over the completion.

Thus the statement that the main operator *forces* I^5=0 on every history receiver would be false. What is forced is the four-step length bound on the source, and what follows is the adequacy of the four-jet quotient for its forward observations.

## 6. Universal receiver after fixing the record specification

For a natural linear chamber increment into an associative receiver with ideal I^5=0, T_<=4(V) has the universal property proved in the previous packet. Hence its use is canonical relative to that finite-record specification.

The construction is internal to the selected linear model: form the freely chamber-labelled object, its tensor words, and the quotient by degrees at least five. Tensor multiplication realizes rejoining; the finite degree filtration records the number of retained event positions.

This is a construction from specified source data and a universal property. The bare iterated S-construction, applicable to arbitrary stable categories, neither supplies a distinguished tensor product on every target nor selects a unique record quotient. Those features must be part of the intended full operator's definition if they are to be mandatory.

## 7. Concrete nonuniqueness test

Take a five-by-five nilpotent Jordan shift N, N^5=0. Both

U(v)=I+v N

and

V(v)=exp(v N)=I+v N+v^2 N^2/2+v^3 N^3/6+v^4 N^4/24

produce invertible event maps, associative route composition, and coherent common-reference comparisons. They have the same first-order increment and different higher event records.

The second fails linearity of U(v)-I. Thus coherence alone permits both; the linear-morphism requirement selects the first. This exhibits exactly which ingredient does the selection, rather than attributing it to associativity or cut independence.

## 8. Answer to the derivation request

Within the declared arithmetic source and Perf(Q) model:

- ordered route multiplication follows from composition;
- linear source dependence follows when the record is a morphism in the linear realization;
- naturality and the fixed first-degree incidence force the single-event rule 1+v;
- the squarefree source forces a four-event bound and positive-path ideal nilpotence;
- the degree-four tensor quotient preserves every forward route record;
- the universal property then constructs the finite adapter and its generated comparisons.

The remaining definitional question is whether the intended main operator includes this natural linear record functor and its finite degree quotient. The inspected cut-and-rejoin implementation is more general and does not select them uniquely. The counterexample identifies the exact additional specification required to make the derivation unconditional.

This keeps the central programme testable: a claimed single-operator derivation must expose that selection in its definition or prove its uniqueness from stronger internal laws. The existing cofiber and normalization laws alone do not provide that uniqueness theorem.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_closure_history_requirements.py`

Exact checks passed for all 168 paths, the six ideal-power dimensions, a nonnilpotent identity on a four-step flag, the two coherent event rules, and their different linearity behavior. The naturality/scaling argument is the proof in section 3.

Source definitions inspected: Nima's nested-closure sketch, the finite gluing and common-reference implementations, and Voevodsky's prime-window history adapter. No positivity or arithmetic Green-form uniqueness is inferred from these record-generation results.
