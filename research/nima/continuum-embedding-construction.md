# Continuum embedding claim — withdrawn for the stated construction

## Current disposition — 7 October 2026

The earlier “construction complete” and smooth-metric convergence claims are
withdrawn. The literal radial interpolant fails even on the expressly allowed
constant metric. Its cited implementations compute finite Grams and grid counts,
not that interpolant or a continuum comparison.

**Current result:** `continuum-embedding-evidence-boundary.md`.
**Exact comparison:** `checkers/check_continuum_embedding_evidence_boundary.py`.
**Original text:** `quarantine/20261007-continuum-evidence/continuum-embedding-construction.md`,
with its SHA-256 recorded in that directory's `manifest.json`.

## The rejected construction

The old construction supplied the embedding p=(i,j,k)/L in Euclidean R^3,
epsilon=1/L, and the weights

\[
\phi_p(x)=\max(0,1-\lVert x-p\rVert/\varepsilon),\qquad
g_L(x)=\sum_p\phi_p(x)g(p).
\]

For g(p)=I3, at the fixed interior point x=(1/2,1/2,1/2), every odd L>=3
has total weight 8-4*sqrt(3), whereas every even L>=4 has total weight one.
Thus the claimed partition of unity fails and there is no pointwise limit
along all integer L. The original unscaled hats also have mass
pi*epsilon^3/3, tending to zero rather than unit Dirac mass.

These radial cones are not the simplex barycentric basis invoked by the old
finite-element analogy. Renormalizing them or supplying a triangulation would
change the construction, not verify this one.

## What the existing computations actually retain

`check_machian_metric_larger.py` constructs permutation-label Grams under a
supplied Euclidean dot product. `check_continuum_limit.py` counts whole-grid
neighbors and forms the Gram of six supplied Euclidean axis vectors. Their
finite calculations survive; their live output now explicitly limits its scope.
Neither supplies the missing map from those objects to a tangent metric.

The historical claims about cubic symmetries approaching O(3), arbitrary spectral
embeddings, heat kernels, discrete Poisson brackets and ADM promotion are not
established by these computations. They are quarantined as parts of the withdrawn
construction, not adjudicated as universal impossibility claims here. Properly
normalized weak limits of discrete measures are not refuted by this result.

A new source-bound reconstruction and convergence theorem is a separate question.
The finite barycentric preservation result in `barycentric-refinement-coherence.md`
remains valid at its stated scope; this failure must not be promoted to a claim
that the programme has no geometric realization.
