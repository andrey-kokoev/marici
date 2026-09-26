# E trees acting on E trees: substitution and curried templates

## Result

For an explicit inductive E-tree signature, generic tree elimination constructs
substitution and staged template application. The K and S expansion equations
follow from that one mechanism; no K/S-specific rewrite axioms are used.

The result is a restricted abstraction/application interface. It is not an
equivalence between E squared and the full P function space.

Active SCC obligations: forward realization, route/coherencer compatibility,
and readout descent. Model: `nima-e-tree-templates`.

## Source specification

`ETreeSubstitution.agda` declares finite trees with labelled leaves and binary
nodes:

\[
T(A)=\mu X.\bigl(A+(X\times X)\bigr).
\]

The one-step layer is encoded with the existing E constructor: one supplied
Boolean tag distinguishes a leaf from a pair of subtrees. An explicit isomorphism
between trees and their unfolded layer is checked.

The source assumptions are the two constructor forms, their tags, finite
inductive closure and its eliminator. These are not derived from the original
twelve resolution schemas. Leaf types are supplied. Later, variable scopes and
arities are also explicit data.

## Generic elimination gives substitution

The eliminator takes a leaf interpretation and a node interpretation. The
module proves uniqueness of the resulting function when both interpretations
and their compatibility equations are fixed. It does not prove uniqueness of
all possible retained proofs of those equations.

Choosing leaf interpretation sigma and preserving the node constructor gives

\[
\operatorname{plug}(\operatorname{leaf}(a),\sigma)=\sigma(a),
\]

\[
\operatorname{plug}(\operatorname{node}(l,r),\sigma)
=
\operatorname{node}(\operatorname{plug}(l,\sigma),
                    \operatorname{plug}(r,\sigma)).
\]

The unit and composition laws are proved for all finite trees:

\[
\operatorname{plug}(t,\operatorname{leaf})=t,
\]

\[
\operatorname{plug}(\operatorname{plug}(t,\sigma),\tau)
=
\operatorname{plug}(t,\lambda a.\operatorname{plug}(\sigma(a),\tau)).
\]

This goes beyond opaque pairing: the eliminator inspects each tree constructor
and recursively transforms the subtrees. The earlier pairing-only obstruction
did not admit this operation.

## Staged application, with scope checked

`ECurriedTemplates.agda` represents an n-input template as a tree whose leaves
are either free data or one of n formal slots. An environment is a finite tuple
of argument trees, not an arbitrary function supplied as an operation.

Applying a template to one argument replaces slot zero by that argument,
preserves free data, and shifts every remaining slot down by one. It returns
a template with n remaining inputs:

\[
\operatorname{partial}:\operatorname{Template}_{n+1}(A)\times T(A)
\to\operatorname{Template}_n(A).
\]

The general beta compatibility law is proved by induction:

\[
\operatorname{instantiate}(\operatorname{partial}(t,a),\rho)
=
\operatorname{instantiate}(t,a::\rho).
\]

Repeated staged application therefore agrees with simultaneous instantiation.

## K and S are template instances

Choose the bodies

\[
K=[0],
\qquad
S=\operatorname{node}(\operatorname{node}([0],[2]),
                     \operatorname{node}([1],[2])).
\]

The generic application theorem gives

\[
\operatorname{run}(K,[x,y])=x,
\]

\[
\operatorname{run}(S,[f,g,x])
=
\operatorname{node}(\operatorname{node}(f,x),\operatorname{node}(g,x)).
\]

These are the K/S expansion shapes. The templates are explicit chosen programs;
the construction does not uniquely select them from all possible templates.
There is no special K or S branch in the application procedure.

Here a node may denote application syntax, but the procedure does not execute
arbitrary resulting nodes as functions. In particular, it does not yet provide
an autonomous evaluator for combinator expressions. Templates and argument
trees are separate roles, with arity tracked explicitly.

## Three checked boundaries

**The function space is larger than insertion templates.** The map that flips
every Boolean leaf label is definable by tree elimination, but no unary insertion
template represents it. This is a quantified impossibility theorem, not merely
a failure to find a template. A template can insert an argument; it cannot
inspect that argument's labels. Internal code for such elimination is missing.

**Flattening loses a construction boundary.** The same substitution defines

\[
\mu:T(T(A))\to T(A).
\]

A leaf containing a binary tree and a binary tree containing two leaf-trees
flatten to the same result. For every inhabited A, Agda proves that no inverse
can recover all original nested trees from their flattened values.

**The eliminator does not select node execution semantics.** Left-projection
and right-projection node algebras give different answers on one tree, while
both satisfy the generic fold equations for their respective algebras. Choosing
an interpretation remains an input to the fold.

## Retention

A completed instantiation stores its template, environment, result and
compatibility path. Each partial application stores its source template,
argument, residual template and compatibility path. These records are packaged
as Q values, with input recovery proved. K's unused input remains in the retained
application even when absent from the result.

This packages actual evidence; it does not assert that the original Resolve
calculus generated these packages without an additional source rule.

## Verification

Formal sources:

- `agda/ETreeSubstitution.agda`
- `agda/ECurriedTemplates.agda`

Fresh safe/cubical closure compilation passed through the shell runner
`checkers/check_e_tree_templates.ps1`. It also rejects two deliberate errors:
omitting the second use of x in S, and capturing the next slot when applying
the first argument.

The source-bound finite checker independently tests 7,776 substitution
associativity cases, 7,272 scoped application cases, 252 K/S instances, and 147
unary templates against the function-space obstruction. Its flattening control
has 42 nested inputs and 38 distinct outputs. These controls supplement the
quantified Agda proofs.

Receipts: `results/agda-ECurriedTemplates.json`,
`results/e-tree-templates-formal-audit.json`, and
`results/e-tree-templates.json`.

The remaining supplied foundations are inductive elimination and the syntax
signature. The missing internal capabilities are code for structural elimination,
typed execution of application nodes, and the full dependent P interface.
