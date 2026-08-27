# The Augmentation Bivector Is the Canonical Complete-Graph Seam Coboundary

## Canonical incidence

Let the finite labelled endpoint state be

\[
g=(g_1,\ldots,g_d),
\qquad
\Omega=(1,\ldots,1).
\]

Orient every pair `i<j` and define the complete-graph coboundary

\[
(\delta g)_{ij}=g_j-g_i.
\]

In the standard exterior basis, these are precisely the coefficients of
`Omega wedge g`, up to the fixed orientation convention. Thus the faithful
augmentation bivector is not an added observer chosen after scalar failure. It
is the canonical pair-label incidence of the labelled source fiber.

## Exact Laplacian identity

The complete-graph Laplacian is

\[
\delta^*\delta=dI-\Omega\Omega^*.
\]

Consequently

\[
\lVert\delta g\rVert^2
=d\lVert g\rVert^2-|\langle\Omega,g\rangle|^2.
\]

On the scalar-null subspace this reduces to

\[
\delta^*\delta g=dg,
\qquad
\lVert\delta g\rVert^2=d\lVert g\rVert^2.
\]

The pair-label endpoint therefore reconstructs every scalar-hidden state by a
canonical source-symmetric incidence map.

## What this closes

The missing finite-seam incidence exists without importing prime weights,
zero data, or a preferred label ordering. The finite boundary packet has a
natural two-term complex

\[
\mathbb C^d/\langle\Omega\rangle
\mathrel{\mathop{\longrightarrow}^{\delta}}
\Lambda^2\mathbb C^d.
\]

Its left inverse on the scalar-null fiber is `delta*/d`.

## What remains

This incidence preserves and reconstructs the boundary defect; it does not
make its flux vanish. The next rung must identify which arithmetic boundary
channel receives the edge current `delta g` and with what orientation.

Primitive and square currents are vertex- or occupation-labelled. To absorb
the bivector boundary faithfully, their source construction must lift to an
edge current whose divergence is the scalar-null endpoint state. A diagonal
vertex correction cannot reproduce arbitrary relative-label phases.

The sharp next test is whether prime multiplication and reciprocal sewing are
chain maps for this complete-graph incidence. Failure would mean the natural
finite-seam complex is not preserved by the arithmetic constructors.

