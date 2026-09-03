# Readout kernel pairs and jointly monic probes

## Question

What does an instrument readout preserve, and which conditions justify distinguishing or reconstructing attached states?

## Claim boundary

This packet treats mathematical state-to-record maps. It does not infer a physical record, unique actualization, collapse, branch selection, or source realization from a probability or a set-valued readout.

## State and record maps

For an attachment \(D\), let \(X_D\) be its object of coherent attached states and let \(Y_D\) be a declared record object. A readout is a typed map

\[
r_D:X_D\to Y_D.
\]

The unresolved multiplicity of a record \(y\) is its fiber

\[
r_D^{-1}(y).
\]

Categorically, indistinguishability is the kernel pair

\[
K_D=X_D\times_{Y_D}X_D.
\]

The diagonal \(X_D\to K_D\) is an isomorphism exactly when \(r_D\) is monic. Until that condition is proved on the intended quotient, equal records certify compatibility only; they do not identify attached states.

## Families of probes

For probes

\[
r_j:X_D\to Y_j,
\]

the combined map is

\[
r=(r_j)_j:X_D\to\prod_jY_j.
\]

The family is jointly monic when this combined map is monic. Individual probes may have nontrivial fibers even when the family is jointly monic. Reconstruction is then relative to the declared state object or quotient represented by \(X_D\); it does not establish physical completeness of that object.

## Functor faithfulness is different

A readout may extend to a functor

\[
R:\mathcal X_{\rm att}\to\mathcal R.
\]

Faithfulness of \(R\) means that every hom-set map is injective. It does not mean that \(R\) is injective on objects, nor that a state-to-record map is monic. A faithful functor from a discrete four-object state category can identify pairs of objects in a discrete two-object record category: each hom-set map remains injective, while object reconstruction fails.

Accordingly, use:

- faithful for injectivity on morphisms;
- monic for a single state-to-record coordinate;
- jointly monic for a probe family;
- conservative for reflection of isomorphisms.

None may substitute for another.

## Quotient gate

If states are considered modulo an admissible equivalence \(q:X_D\to Q_D\), reconstruction requires a descended coordinate

\[
\bar r:Q_D\to Y_D
\]

with \(r_D=\bar r q\), followed by proof that \(\bar r\) is monic. Injectivity on chosen representatives does not prove this descent or monicity.

## Physical record gate

Calling \(y\) a physical record additionally requires a source-defined realization of the instrument, an admitted effect or detector channel, a positive state-effect pairing where applicable, and a physical record map. A mathematical fiber census supplies none of these arrows by itself.

## Finite diagnostic

Four states \(a_0,a_1,b_0,b_1\) have a coarse record that retains only the letter and a second probe that retains only the index. Each probe has two-element fibers. Their combined map is injective. The coarse-record functor between discrete categories is faithful on hom-sets while identifying objects, providing a direct counterexample to the claim that categorical faithfulness implies state reconstruction.

## Disposition

Readout ambiguity is retained as a kernel pair or explicit fibers. State distinction requires a monic coordinate; a family suffices exactly when jointly monic. Functor faithfulness controls morphisms and cannot authorize object-level reconstruction or physical selection.
