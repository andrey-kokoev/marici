# Two-instrument integrating witness

## Question

Can one finite model exercise attachment reindexing, inter-instrument coherence, continuation, readout ambiguity, and predicted malformed-attachment rejection without promoting the fixture to a general theorem?

## Claim boundary

This is a finite integrating diagnostic for the abstract constructions in the preceding packets. It demonstrates compatibility of those constructions in one model. It does not prove their existence for arbitrary systems, provide a physical apparatus, or assign physical-time meaning to composition order.

## Base and attachment fibers

Let the base category be the poset

\[
S_0\longrightarrow S_1.
\]

Each system has a discrete fiber containing a bare attachment and a joint attachment. The joint attachment has two occurrence-labelled instruments \(L\) and \(R\). Pullback along \(S_0\to S_1\) sends the joint attachment over \(S_1\) to the joint attachment over \(S_0\), preserving both occurrence labels and their interface.

This gives a finite indexed attachment category and a corresponding total category. The cross-system morphism between joint attachments exists because the source attachment equals the pulled-back target attachment. Relabeling the target as bare destroys that compatibility and rejects the purported total morphism.

## Local states and continuation

Each occurrence carries a bit. The local product is

\[
X_{\rm local}=\{0,1\}_L\times\{0,1\}_R.
\]

The shared continuation object is \(Q=\{0,1\}\). The output boundary of \(L\) and input boundary of \(R\) are the corresponding bit projections. Coherence requires equality in \(Q\), so the matching object is

\[
M=\{(0,0),(1,1)\}.
\]

The family \((0,1)\) is locally admissible but fails the continuation equation. This is the predicted malformed-state fixture.

A structurally malformed attachment whose continuation edge names an undeclared occurrence fails earlier, at incidence validation. These are distinct failures: one has invalid structure; the other has valid structure but an incoherent state.

## Readout

Define the coarse detector record by parity,

\[
r(l,r)=l\mathbin{\mathrm{xor}}r.
\]

Both coherent states map to record \(0\). Thus the readout kernel pair contains an off-diagonal pair and readout is nonmonic on \(M\). Adding the left-bit probe gives the combined coordinate

\[
(r,l):M\to\{0,1\}^2,
\]

which is injective on this finite matching object.

This does not select one coherent state. It only shows that the enlarged probe family separates the two states if both coordinates are available through admitted record maps.

## Integrated gates

The checker evaluates the following sequence of typed gates:

1. attachment occurrences and interface endpoints are declared;
2. reindexing preserves the joint attachment and its incidence;
3. local states are enumerated independently of coherence;
4. continuation equality constructs the matching subset;
5. malformed structure and incoherent local state fail at distinct gates;
6. coarse readout retains a two-state fiber;
7. the additional probe makes the coordinate jointly monic.

No gate supplies physical realization or physical time. The arrow in the base and the ordering of the continuation interface remain categorical data only.

## Disposition

The finite witness integrates the indexed-category, matching-limit, continuation, and readout-fiber semantics without contradiction. Its hostile fixtures fail at their predicted structural and coherence gates. The witness remains finite diagnostic evidence rather than a general existence theorem.
