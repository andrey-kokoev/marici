# The opposite-polarity dagger has a canonical joint-graph comparison but no canonical ambient extension

## Problem

The source star determines an antiunitary dagger between the minimal generated feature carriers

\[
D_{min}:
\mathcal H_{min}^+
\to
\mathcal H_{min}^-.
\]

The physical prolate, Green, or Clifford carriers can be larger:

\[
\mathcal H_{phys}^+
=
\mathcal H_{gen}^+
\oplus
\mathcal N^+,
\]

\[
\mathcal H_{phys}^-
=
\mathcal H_{gen}^-
\oplus
\mathcal N^-.
\]

Here \(\mathcal H_{gen}^{\pm}\) is the closure reached by the labelled source, while \(\mathcal N^{\pm}\) is source orthogonal.

The source data determine \(D_{min}\) on \(\mathcal H_{gen}^+\), but do not read either complement.

## Ambient extension criterion

An antiunitary extension

\[
D_{amb}:
\mathcal H_{phys}^+
\to
\mathcal H_{phys}^-
\]

with

\[
D_{amb}|_{\mathcal H_{gen}^+}
=D_{min}
\]

exists exactly when the orthogonal complements are antiunitarily isomorphic:

\[
\mathcal N^+
\cong_{anti}
\mathcal N^-.
\]

For Hilbert spaces, this is equivalent to equality of Hilbert dimension.

## Proof

If \(D_{amb}\) exists, antiunitarity sends the orthogonal complement of \(\mathcal H_{gen}^+\) onto the orthogonal complement of \(\mathcal H_{gen}^-\). Its restriction therefore gives an antiunitary

\[
D_\perp:
\mathcal N^+
\to
\mathcal N^-.
\]

Conversely, given such a \(D_\perp\), define

\[
D_{amb}
=
D_{min}
\oplus
D_\perp.
\]

This is the required antiunitary extension.

## Nonuniqueness

Suppose one complement extension \(D_\perp^0\) is chosen. Every other extension has the form

\[
D_\perp
=
U^-D_\perp^0,
\]

where

\[
U^-\in\mathcal U(\mathcal N^-).
\]

Thus ambient extensions form a torsor under the unitary group of the source-orthogonal complement.

Unless the complement is zero or carries an independently specified Real structure, the source does not select a point of this torsor.

## Comparison with a given physical symmetry

Suppose the physical carrier already has an antiunitary

\[
J_{phys}:
\mathcal H_{phys}^+
\to
\mathcal H_{phys}^-.
\]

A source-authorized comparison with \(D_{min}\) exists precisely when:

1. \(J_{phys}\mathcal H_{gen}^+=\mathcal H_{gen}^-\);
2. on every labelled source vector,
   \[
   J_{phys}A_{phys}^+p
   =
   A_{phys}^-p^*;
   \]
3. \(J_{phys}\) preserves the declared endpoint and Krein signatures.

Under these conditions, continuity and source-range density imply

\[
J_{phys}|_{\mathcal H_{gen}^+}
=D_{min}.
\]

No further homotopy is needed on the generated carrier: the comparison is strict there.

## Discrepancy cocycle

If both \(J_{phys}\) and an ambient extension \(D_{amb}\) exist, their ratio

\[
U
=
J_{phys}^{-1}D_{amb}
\]

is unitary on \(\mathcal H_{phys}^+\).

The two daggers agree on the generated carrier exactly when

\[
U|_{\mathcal H_{gen}^+}=I.
\]

Hence every unresolved discrepancy is supported on \(\mathcal N^+\). It cannot affect a source pullback form, but it matters for claims about a canonical ambient physical symmetry.

## Canonical joint graph

A comparison can be retained without choosing an ambient extension. Define the source-labelled joint graph

\[
\mathcal J_r^+
=
\overline{
\{
(A_{min,r}^+p,A_{phys,r}^+p):
p\in\mathscr G_r
\}
}
\]

inside

\[
\mathcal H_{min,r}^+
\oplus
\mathcal H_{phys,r}^+.
\]

Define \(\mathcal J_r^-\) similarly.

If the physical source symmetry identity holds, then

\[
D_{joint,r}(x,y)
=
(D_{min,r}x,J_{phys,r}y)
\]

maps \(\mathcal J_r^+\) antiunitarily onto \(\mathcal J_r^-\).

On a generating pair,

\[
D_{joint,r}
(
A_{min,r}^+p,
A_{phys,r}^+p
)
=
(
A_{min,r}^-p^*,
A_{phys,r}^-p^*
).
\]

This joint-graph dagger is canonical relative to the two declared source observations. It never acts on unobserved ambient vectors separately.

## Endpoint compatibility

On the endpoint graph, both models must induce

\[
J_\partial
\begin{pmatrix}u_+\\u_-\end{pmatrix}
=
\begin{pmatrix}\overline{u_-}\\\overline{u_+}\end{pmatrix}.
\]

Therefore the joint graph decomposes into invariant even and odd endpoint sectors. The odd sector retains its negative metric sign; dagger does not cancel it.

## Successor compatibility

Assume the physical successor maps satisfy the source equations for left and right convolution. Then the joint dagger obeys

\[
D_{joint,r+s}D_{a}^{L,+}
=
D_{a^*}^{R,-}D_{joint,r}
\]

on generated joint-graph vectors.

Density extends the equation whenever the successor maps are bounded in both graph norms.

The same argument applies to conductor, seam, and aperture successors once their physical source symmetry identities are supplied.

## Common-positive-bulk obstruction

The joint graph identifies opposite-polarity symmetries, but it does not identify the positive metrics of the minimal and physical legs.

To fill the polarity cube positively, one still needs a common positive remainder \(G_r\) and contractions from it to both observed legs. Equivalently, the relevant Gram forms must satisfy the Schur--Douglas domination.

Thus the symmetry comparison and the positive filler are distinct:

1. dagger comparison is fixed by source reflection identities;
2. positive cube filling is fixed by metric domination;
3. the first does not imply the second.

## Physical Clifford specialization

For the Clifford carrier, a candidate physical antiunitary must specify its action on all four Clifford channels and satisfy:

\[
J_{phys}\mathbb D_S^+
=
\mathbb D_S^-J_{phys}
\]

on a common invariant core, together with the endpoint trace identity.

The abstract joint-graph construction applies as soon as those operator-domain statements are proved. Kernel agreement alone proves the identity only on source-generated boundary observations, not on the full Clifford domain.

## Result

The comparison problem has the following exact resolution:

1. the dagger is canonical on source-generated minimal carriers;
2. ambient extension exists exactly when the source-orthogonal complements have equal Hilbert dimension;
3. such an extension is generally noncanonical;
4. a given physical antiunitary agrees with the minimal dagger exactly when it satisfies the labelled source identity;
5. the canonical comparison object is the source-labelled joint graph;
6. positive polarity-cube filling remains a separate Douglas domination problem.

## Disposition

No arbitrary ambient extension should be added to the semilocal construction. The joint-graph dagger is the maximal canonical symmetry comparison authorized by the source.

Further promotion requires concrete physical operator data on the source-orthogonal complement, not another categorical homotopy.
