# Quintet projector width sum

Work package: WP532  
Owner: marici.Figueiredo

## Question

What is the basis-invariant content of the twenty WP516/WP517 rows whose two
daughters lie in the exactly fivefold-degenerate vector quintet?

## Domain and quotient

The state domain is the frozen WP516 fourteen-vector witness. Its canonical
mass operator has an exact eigenvalue

\[
m_5^2=6\,\mathrm{GeV}^2
\]

with multiplicity five. The physical daughter label is therefore the
five-dimensional spectral subspace, modulo orthogonal changes of frame inside
that subspace. Individual eigenvector indices 7 through 11 are not physical
labels.

## Exact spectral projector

Let \(M^2\) be the exact WP508 mass matrix after the WP516 substitutions. A
basis \(N\) of the mass-six kernel gives

\[
P_5=N(N^TN)^{-1}N^T.
\]

The checker verifies exactly that

\[
P_5^T=P_5,\qquad P_5^2=P_5,\qquad
\operatorname{rank}P_5=5,\qquad M^2P_5=6P_5.
\]

The projector has support only on the eight flavor-gauge coordinates. Its
orthogonal complement within that sector is the principal-triplet projector
\(P_3\).

## Invariant pair norm

Write \(G_a\) for the antisymmetric daughter-index matrix of the exact cubic
gauge tensor with parent coordinate \(a\). The complete unordered
quintet-pair norm is governed by

\[
S_{aa'}=\frac12\operatorname{Tr}
\left(G_a^TP_5G_{a'}P_5\right).
\]

Direct symbolic contraction gives the exact identity

\[
S=\frac52P_3.
\]

Thus a parent vector \(x\) has total squared coupling

\[
\sum_{i<j\in 5}|g_{xij}|^2
=x^TSx
=\frac52\lVert P_3x\rVert^2.
\]

This is independent of every orthonormal frame chosen inside the quintet.

## Hostile frame test

For an exact triplet parent witness, one displayed quintet-pair squared
coupling changes from \(1/2\) to \(1/4\) under a 45-degree rotation of two
quintet basis vectors. The complete unordered-pair norm remains \(5/2\).
Therefore no individual row among the degenerate daughters has width
authority.

WP516 and WP517 do contain all ten unordered daughter pairs for each of the
two heavy parents 12 and 13. Their twenty rows are consequently a complete
coordinate expansion of two invariant sums. The reported summed partial
widths of those coordinate expansions are approximately

\[
\Gamma_{12\to 5\,5}=2.63621\times10^{-9}\,\mathrm{GeV},
\qquad
\Gamma_{13\to 5\,5}=2.63741\times10^{-9}\,\mathrm{GeV}.
\]

These numerical values retain WP516's existence-witness status. The theorem
freezes how degenerate internal states must be summed; it does not select the
witness parameters or supply a detector.

## Classification and remaining gate

WP532 is a basis-invariant rigidifier, not a selector. It replaces twenty
basis-sensitive channel labels by two parent-level coupling sums.

The smallest exact falsifier is a mass-six kernel of dimension other than
five, failure of \(S=(5/2)P_3\), or variation of a complete ten-pair sum under
an orthogonal quintet-frame rotation.

The next gate is to classify all 131 threshold-open numerical-zero coordinate
triples by exact block/projector contractions. Only then can the full WP517
list be replaced by invariant parent-level sums and composed with the WP525
complex-mass and WP527 source-support packets.

## Reproduction

Run uv run --offline --with sympy python
research/flavor/checkers/wp532_quintet_projector_width_sum.py.

The generated result is
research/flavor/results/wp532_quintet_projector_width_sum.json.
