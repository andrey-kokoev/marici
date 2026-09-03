# Common graph-norm pullback domain

## Question

Can the positivity-adapted leading GNS observer and the closability-adapted Hardy observer be placed over one closed common domain?

## Claim boundary

Their algebraic polynomial core has a canonical graph-norm completion with continuous projections to both observers. This constructs a comparison span, not the missing source-derived map from the arithmetic presentation to Hardy space, and it does not transfer semiboundedness to the weaker leading GNS norm.

## Algebraic core

Let \(\mathcal P\) be the polynomials in the Bernstein coordinate. It carries two norms:

\[
\lVert p\rVert_0
\]

from the positive leading archimedean form, and

\[
\lVert p\rVert_{H^2}
\]

from Hardy coefficient space.

Define the common graph norm

\[
\lVert p\rVert_*^2
=
\lVert p\rVert_0^2
+
\lVert p\rVert_{H^2}^2.
\]

Let \(\mathcal D_*\) be the completion of \(\mathcal P\) in this norm.

## Comparison span

The inequalities

\[
\lVert p\rVert_0
\leq
\lVert p\rVert_*
\]

and

\[
\lVert p\rVert_{H^2}
\leq
\lVert p\rVert_*
\]

extend the identity on polynomials to continuous maps

\[
J_0:\mathcal D_*
\longrightarrow
\mathcal H_0
\]

and

\[
J_H:\mathcal D_*
\longrightarrow
H^2(\mathbb D).
\]

Thus the two observer spaces admit the comparison span

\[
\mathcal H_0
\longleftarrow
\mathcal D_*
\longrightarrow
H^2(\mathbb D).
\]

The polynomial core gives dense ranges, although injectivity or closed range of either completed projection requires separate proof.

## Form transport

The bounded zero-side Hardy form pulls back along \(J_H\) to a bounded form on \(\mathcal D_*\). The leading positive form pulls back along \(J_0\). Therefore both forms coexist continuously on one complete domain, and identities proved on polynomials extend there.

This constructs a diagnostic comparison span only. It does not fill the categorical model's `common_closed_form_domain` layer, because no common closed realization of the arithmetic and Weil forms on a declared \(D(Q)\), and no graph-norm-dense Gaussian-jet inclusion, has been constructed.

## Why it does not prove RH

A lower bound in the stronger graph norm has the form

\[
q(p)
\geq
-C\lVert p\rVert_*^2.
\]

RH positivity requires control relative to the leading norm alone, ultimately

\[
q(p)
\geq
-\lVert p\rVert_0^2.
\]

Since the Hardy term in \(\lVert p\rVert_*\) may be much larger than \(\lVert p\rVert_0\), the first inequality does not imply the second.

Moreover, the Hardy realization was constructed using the zero-side nodes \(y_\rho\). It is an unconditional diagnostic target topology, but it is not an arithmetic source construction. Using it to prove the arithmetic form closed would require an independently derived prime--theta map into Hardy space.

## Exact remaining arrows

A source-valid proof needs at least one of:

1. a continuous embedding
   \[
   \mathcal H_0
   \longrightarrow
   H^2(\mathbb D);
   \]
2. a source-derived prime--theta map into \(H^2(\mathbb D)\);
3. a closed coupled arithmetic form directly on \(\mathcal H_0\);
4. a comparison estimate that eliminates the Hardy component from the lower graph-norm bound.

The first arrow is doubtful for interval moment norms, and no other arrow is currently constructed.

## Coherence interpretation

The common graph completion is a pullback-style coherencer: it receives the shared polynomial core and maps to both higher observers. Its algebraic residue is zero because both projections restrict to the identity on polynomials.

Its authority residue is nonzero: only the zero-side presentation currently supplies the Hardy extension. Its quantitative residue is also nonzero: the graph norm is stronger than the positivity reference norm.

## Disposition

A completion carrying the two diagnostic norms exists abstractly, but the required common form domain remains unconstructed. The unresolved source problem is to define both relevant closed or closable forms on one declared \(D(Q)\), prove graph-norm density of the Gaussian-jet subcategory, construct the source--Weil comparison there, and retain a lower bound measured in \(\lVert\cdot\rVert_0\), not merely in the stronger auxiliary graph norm.

## Verification

- `research/voevodsky/checkers/check_common_graph_norm_pullback.py`
- `research/voevodsky/results/common_graph_norm_pullback.json`
