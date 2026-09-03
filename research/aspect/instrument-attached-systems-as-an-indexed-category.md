# Instrument-attached systems as an indexed category

## Question

What are the categories of original systems and instrument-attached systems, and what exactly does the forgetful functor forget?

## Claim boundary

This packet defines a decoration semantics in which attachment does not change the underlying system. It separates that construction from physical assembly or carrier extension, which would require additional objects and maps. It does not assert that every system has a canonical attachment or that attachment order is physical time.

## Base systems

Let \(\mathcal S\) be a category of systems and system-preserving maps. The abstract construction does not prescribe whether its objects are state spaces, interaction nets, optical assemblies, or another sector-specific type.

For each \(S\in\mathcal S\), let \(\operatorname{Att}(S)\) be the category of admissible attachment data over \(S\). An object \(D\in\operatorname{Att}(S)\) contains:

1. an occurrence-indexed placement category \(I_D\);
2. a typed instrument object for every occurrence;
3. a typed interface from each occurrence to its declared locus in \(S\);
4. continuation-state interfaces needed for lawful transformer composition;
5. inter-occurrence coherence data, including matching and incidence certificates;
6. an authority boundary distinguishing mathematical attachment, record maps, physical realization, and any admitted quotient.

A morphism in \(\operatorname{Att}(S)\) preserves the underlying \(S\) and maps occurrence, instrument, interface, continuation, and coherence data compatibly.

## Reindexing

Assume attachment data can be pulled back along system maps. This gives a contravariant indexed category

\[
\operatorname{Att}:\mathcal S^{op}\to\mathbf{Cat}.
\]

For \(f:S\to T\), the functor

\[
f^*:\operatorname{Att}(T)\to\operatorname{Att}(S)
\]

restricts a target attachment to the source system. It must preserve identities and composition, either strictly or through declared pseudofunctor coherence.

This pullback is a substantive assumption. A system map that does not transport loci or interfaces does not automatically admit \(f^*\).

## Total category

Define the category of instrument-attached systems as the Grothendieck construction

\[
\mathcal S_{\rm inst}=\int_{S\in\mathcal S}\operatorname{Att}(S).
\]

Its objects are pairs \((S,D)\). A morphism

\[
(S,D)\longrightarrow(T,E)
\]

consists of a base map \(f:S\to T\) and a vertical attachment map

\[
\delta:D\to f^*E
\]

in \(\operatorname{Att}(S)\). Composition uses reindexing functoriality.

The forgetful functor is the projection

\[
U:\mathcal S_{\rm inst}\to\mathcal S,
\qquad
U(S,D)=S,
\qquad
U(f,\delta)=f.
\]

Functoriality is immediate from the total-category composition law.

## What is preserved

In this decoration semantics,

\[
U(S,D)=S
\]

exactly. The attached object is not a later physical state and does not replace \(S\). It is \(S\) equipped with additional typed structure.

There is therefore no mandatory map

\[
S\to U(S,D):
\]

both sides are already the same base object. If a sector builds a genuinely enlarged carrier \(R(S,D)\), that is a separate realization or assembly functor

\[
R:\mathcal S_{\rm inst}\to\mathcal S_{\rm physical}
\]

with a separately supplied interface from the source system. Decoration must not be silently identified with realization.

## Finite diagnostic

Take a two-object base poset \(S_0\to S_1\). Give each base object two discrete attachments and define pullback by sending the distinguished attachment over \(S_1\) to the distinguished attachment over \(S_0\). The total category has four objects. Exhaustive enumeration verifies identities, composition, the projection functor, and equality of each strict projection fiber with its attachment category.

A hostile pair claiming a total morphism over \(S_0\to S_1\) is rejected when its source attachment has no map to the pulled-back target attachment. A base map alone does not transport instruments.

## Disposition

Instrument-attached systems are modeled by the total category of an indexed attachment category. The forgetful functor is projection and preserves the underlying system exactly. Physical assembly, free attachment, readout, and canonical instrument choice are separate constructions rather than hidden parts of \(U\).
