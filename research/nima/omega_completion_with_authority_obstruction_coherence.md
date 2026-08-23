# Omega completion with source authority, obstructions, and coherence cells

## Objective

The first omega fixed point used only model and readout edges. This packet
tests whether the construction survives three load-bearing Marici features:

1. source authority that cannot be manufactured by reflection;
2. first-class typed obstruction objects;
3. higher coherence relating two parallel explanatory paths.

The result remains a formal typed-computad theorem, not a physical Carrier
theorem.

## The typed 2-computad

Start with a source record \(s\), a physical claim \(x\), and the only
authority-bearing edge \(s\longrightarrow x\), labelled `warrants`.

For every node \(y\), the enriched self-modeling operator \(\mathsf V\) adds
four first-class nodes: \(m_y\) (model), \(r_y\) (record), \(o_y\)
(obstruction), and \(c_y\) (coherence witness).

It adds two parallel paths

\[
r_y\longrightarrow m_y\longrightarrow y,
\qquad
r_y\longrightarrow o_y\longrightarrow y,
\]

labelled respectively `classifies, models` and `records, locates`, plus a
2-cell \(c_y\) whose boundary is those paths. The operator never adds a
`warrants` edge. Every coherence witness is itself a node and is therefore
modeled, recorded, obstructed, and cohered at the next stage.

## Exact finite-stage laws

With \(B\) base nodes and one base authority edge, stage \(n\) has

\[
N_n=B\frac{4^{n+1}-1}{3},
\qquad
E_n=1+4B\frac{4^n-1}{3},
\qquad
C_n=B\frac{4^n-1}{3}.
\]

Its unresolved frontier has \(\delta_n=B4^n\) nodes. The checker verifies
these identities through depth five, checks every 2-cell boundary exactly,
and verifies that the unique source-authority edge is preserved and never
replicated.

## Omega result

Nodes in the union have normal form

\[
wy,\qquad w\in\{m,r,o,c\}^*,\quad y\in X_0.
\]

Every finite word receives all four children, four boundary edges, and its
coherence 2-cell one stage later. Hence

\[
\boxed{\mathsf V(X_\omega)=X_\omega.}
\]

The source-authority invariant also survives:

\[
\operatorname{Warrants}(X_\omega)
=\operatorname{Warrants}(X_0).
\]

Reflection can generate arbitrarily deep accounts of authority, obstruction,
and coherence, but it cannot generate new authority.

## Meaning and next falsifier

The omega phenomenon survives a finite first-class higher-coherence signature
with a negative authority constraint. This is evidence for a standard term
closure fact: a finitary polynomial signature reaches all finite terms at
\(\omega\). It is not yet distinctive evidence for physical Marici.

Omega closure may fail for infinite-arity operations, non-monotone deletion,
global quotient equations, source-derived identifications requiring
transfinite completion, analytic completion, or semantic authority rules.
Therefore the next serious test is not another finite constructor. It is one
source-derived quotient or coherence equation from a physical sector, tested
for preservation under the filtered union.

