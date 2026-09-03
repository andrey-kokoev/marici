# Optical attachment transport as a correspondence

## Question

How can optical attachment transport retain deletion and branch ambiguity without fabricating a pullback choice?

## Claim boundary

This packet constructs a finite relation- and profunctor-valued extension of typed-port attachment transport. It treats occurrence-preserving lifts. Replication of one target detector onto several source ports is excluded unless supplied as an additional policy.

## Lift witnesses

For a typed optical-network map

\[
f:M\to N,
\]

let \(E\in\operatorname{Att}_{\rm opt}(M)\) and \(D\in\operatorname{Att}_{\rm opt}(N)\). Define

\[
P_f(E,D)
\]

to be the set, or groupoid, of compatible lift witnesses from \(D\) to \(E\). A witness contains:

1. an occurrence map preserving detector identity;
2. a placement lift over the boundary-port map of \(f\);
3. compatible mode and coupler transport;
4. transport of incidence and coherence data.

Thus \(P_f\) is a profunctor

\[
P_f:\operatorname{Att}_{\rm opt}(M)^{op}
\times\operatorname{Att}_{\rm opt}(N)	o\mathbf{Set},
\]

or to groupoids when lift witnesses have nontrivial equivalences.

## Three transport regimes

For fixed \(D\), the support of \(P_f(-,D)\) records all admissible source attachments:

- empty support means deletion or incompatibility;
- singleton support with a unique witness recovers ordinary pullback;
- multiple support objects retain unresolved branch choices.

No member of a multiple support is selected by the correspondence itself.

For finite discrete attachment categories this is equivalently a relation

\[
R_f\subseteq
\operatorname{Att}_{\rm opt}(M)	imes
\operatorname{Att}_{\rm opt}(N).
\]

It can also be written as a powerset-valued map

\[
\operatorname{Lift}_f:
\operatorname{Att}_{\rm opt}(N)	o
\mathcal P(\operatorname{Att}_{\rm opt}(M)).
\]

## Composition

For \(L\xrightarrow{g}M\xrightarrow{f}N\), compose lift witnesses through the coend

\[
P_{fg}(F,D)
\cong
\int^{E}
P_g(F,E)\times P_f(E,D).
\]

In finite discrete models this is relational composition:

\[
\operatorname{Lift}_{fg}(D)
=
\bigcup_{E\in\operatorname{Lift}_f(D)}
\operatorname{Lift}_g(E).
\]

Composition preserves all branches rather than choosing an intermediate attachment. Associativity follows from associativity of relational composition, or from the standard associator for profunctor composition.

## Recovery of ordinary reindexing

On the subcategory of port-cartesian typed maps, every target attachment has a unique supported source attachment and a unique lift witness. The profunctor is then representable by the ordinary pullback functor

\[
f^*:\operatorname{Att}_{\rm opt}(N)	o
\operatorname{Att}_{\rm opt}(M).
\]

Hence the earlier Cat-valued indexed category is the representable restriction of the correspondence semantics, not a competing construction.

## Replication boundary

If one target occurrence has two source-port preimages, the basic correspondence contains two one-occurrence lifts. A replicated two-occurrence attachment is a different object requiring:

- an occurrence-comultiplication or replication policy;
- resource and no-cloning constraints appropriate to the optical sector;
- new inter-occurrence coherence and readout data.

Branch multiplicity alone does not authorize replication.

## Finite diagnostic

A target detector at port \(p\) has two compatible source lifts at \(a\) and \(b\). A second network map gives unique predecessors \(x\) and \(y\). Direct transport returns \(\{x,y\}\), equal to the union of the two iterated lift sets. A deletion map returns the empty set, and a cartesian map returns a singleton. Selecting the lexicographically first branch is detected as information loss because its support is strictly smaller than the lawful correspondence.

## Disposition

Optical attachment transport extends across deletion and branching as a profunctor or relation. Ordinary pullback is recovered exactly on the representable, port-cartesian locus. Empty and multiple fibers remain typed obstruction data; neither is repaired by an implicit choice.
