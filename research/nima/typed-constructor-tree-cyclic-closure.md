# Typed constructor-tree cyclic closure

## Generalization

The Krylov closure

\[
\operatorname{span}\{T_wJv\}
\]

is correct only for unary transports forming a freely composable word
algebra. Operative sources generally have partial, multi-input constructors

\[
\mu:(\alpha_1,\ldots,\alpha_n)\rightharpoonup\beta.
\]

The intrinsic source-generated carrier is therefore the closure under
well-typed, source-authorized constructor trees, not arbitrary words.

For each type \(\alpha\), begin with the admitted leaf space
\(S_\alpha^{(0)}\). Iteratively define

\[
S_\beta^{(k+1)}
=S_\beta^{(k)}
+\sum_{\substack{\mu:(\alpha_1,\ldots,\alpha_n)\rightharpoonup\beta\\
\mu\ {\rm authorized}}}
\operatorname{span}\mu(
S_{\alpha_1}^{(k)},\ldots,S_{\alpha_n}^{(k)})
\]

only where the partial constructor's support, resource, temporal, and fault
preconditions hold. The stabilized family \(S_\alpha^{(\infty)}\) is the
typed tree-cyclic carrier.

## Why unary closure is incomplete

Let the only admitted leaf types be \(A\) and \(B\), each one-dimensional,
and let the output carrier \(C=\mathbb R^2\). A unary transport may generate
only \(e_1\). An authorized binary constructor

\[
\mu:A\times B\to C,\qquad \mu(a,b)=ab\,e_2
\]

generates the missing direction \(e_2\). Word/Krylov closure reports rank
one; constructor-tree closure reports rank two.

Conversely, the same numerical map supplied under an undeclared constructor
identifier generates no authority-bearing direction. Numerical image and
constructor authority are separate fields.

## Coherence is part of closure

Two defined trees with identical output vectors are not thereby equivalent.
For

\[
\mu(\nu(-,-),-),\qquad \lambda(-,\kappa(-,-)),
\]

substitution is authorized only if each node is authorized, every interface
signature matches, accumulated support obligations hold, and any required
comparison cell

\[
\omega:\mu(\nu(-,-),-)\Rightarrow\lambda(-,\kappa(-,-))
\]

is present. Without \(\omega\), the trees occupy distinct provenance
classes even if scalar projection identifies their outputs.

Thus the completed object is not merely a carrier subspace. It is a typed
carrier indexed by constructor-tree provenance modulo explicitly admitted
coherence cells.

## Finite compiler gate

For each node, verify:

1. constructor identifier has a source authority root;
2. ordered input and output signatures match exactly;
3. the partial constructor is defined on the supplied support;
4. resource, epoch, and fault equations hold;
5. support obligations accumulate rather than disappear;
6. every reassociation or alternative factorization uses an admitted
   invertible coherence cell.

The first failure is a finite falsifier, classified as
\(undeclared\_authority\_constructor\), \(signature\_mismatch\), or
\(constructor\_tree\_coherence\_failure\), with the failing node and missing
cell reported.

## Cross-sector consequences

- **Strominger.** The DPC compiler should compute exactly this typed tree
  closure. A flat conjunction of capability, policy, intent, certificate,
  and lease does not produce execution authority without the authorized
  multi-input constructor.
- **Arithmetic/RH.** Prime multiplication, endpoint augmentation, and
  archimedean completion are differently typed constructors, not freely
  interchangeable unary transports. The missing orientation cannot be
  smuggled in as an implicit coherence cell. It must be a source-authorized
  constructor or inequality joining the coupled channels.
- **Kitaev.** State injection is a multi-input constructor combining encoded
  data, a verified resource state, measurement, and branch correction.
  A gate identity or phase polynomial establishes numerical action but does
  not authorize the resource-state production node.
- **Benincasa.** External controls, integrated period readout, and analytic
  dressing have different signatures. A latent score-Gram operation cannot
  be substituted for the authorized linear period constructor merely
  because it increases formal rank.

## Refined theorem

> Every source-generated operative direction is represented by a finite,
> well-typed, source-authorized constructor tree. The minimal completed
> carrier is the span of such trees modulo admitted coherence cells.

This strictly refines transport cyclicity. Unary Krylov closure is recovered
when every constructor is unary, total, and freely associative.

