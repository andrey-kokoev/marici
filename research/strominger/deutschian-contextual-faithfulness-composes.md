# Contextual faithfulness composes

## Conjecture

After the blind-interface falsifier, the sharp replacement is:

> Let a source object map faithfully into a route packet.  If every downstream
> interface is faithful on the image delivered by the preceding composite,
> then the complete observation net is faithful.

This is contextual faithfulness.  It does not require an interface to be
injective on states that can never reach it.

## Theorem

Let

\[
X\xrightarrow{f}Y\xrightarrow{g}Z
\]

be typed maps.  Suppose \(f\) is injective and the restriction of \(g\) to
\(\operatorname{im}f\) is injective.  Then \(g\circ f\) is injective.

Indeed, if

\[
g(f(x_1))=g(f(x_2)),
\]

contextual injectivity of \(g\) gives \(f(x_1)=f(x_2)\), and injectivity of
\(f\) gives \(x_1=x_2\).

The argument iterates through any finite typed chain.  No additional
faithfulness tower is required once each arrow is tested on the actual image
of its predecessor.

## Exact seven-valued classification

For the route embedding

\[
R(x)=(x,-x)
\]

over \(\mathbb F_7\), consider every linear scalar interface

\[
g_{u,v}(a,b)=ua+vb.
\]

Its composite with the route packet is

\[
(g_{u,v}\circ R)(x)=(u-v)x.
\]

Therefore it is contextually faithful exactly when \(u\neq v\).

Among the forty-nine labelled interfaces:

- seven with \(u=v\) are completely blind on the route image;
- forty-two with \(u\neq v\) are faithful on the route image.

No scalar interface is injective on the full two-dimensional route-record
space.  Requiring global injectivity would therefore reject every useful
scalar port.  Contextual injectivity is the exact condition.

## Attempted falsification

The complete finite census over \(\mathbb F_7\) finds no counterexample.  The
general proof shows why none exists in the category of sets, modules, or any
category where the stated monomorphisms and pullbacks are actually defined.

Apparent counterexamples must violate at least one typing premise:

- the downstream map was tested on the wrong domain;
- the intermediate quotient changed;
- the image inclusion was not preserved;
- a merely measured coordinate was mistaken for a faithful one;
- two factorization paths lacked a coherence comparison.

## Deutschian stopping rule

This is a genuine closure law rather than another protective constructor:

> Do not demand global faithfulness from every component.  Prove monicity on
> the source-reachable image and verify that each composition preserves that
> image.  Then complete-network faithfulness follows.

Higher associators remain necessary when several composition paths must be
identified.  They do not create a new exception to this one-path monicity
theorem.
