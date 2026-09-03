# Scalar Markov Green strict partial double-category fragment

## Question

Do the analytic associator, interchange, Beck–Chevalley, and completion results assemble into an instantiated categorical structure rather than disconnected fixtures?

## Claim boundary

This packet constructs a strict partial double-category fragment for scalar Markov Green chains. It is not an equipment: companions and conjoints for all vertical arrows are not constructed. It does not represent the full coherence pyramid.

## Objects

Objects are normalized finite scalar Markov Green chains

\[
G(a_1,\ldots,a_n),
\qquad |a_i|<1,
\]

together with uniformly contractive one-sided completions satisfying \(|a_i|\le\rho<1\).

## Arrows

Horizontal arrows are seam-compatible chain extensions and contiguous inclusions. Their composition concatenates ordered edge lists. It is partial because seam labels and normalizations must agree.

Vertical arrows are vertex-sign gauge isometries

\[
G\mapsto D_\varepsilon GD_\varepsilon.
\]

Vertical composition is pointwise sign multiplication. Horizontal and vertical identities are the empty extension and the all-positive vertex gauge.

## Squares

An admitted square consists of compatible horizontal extensions and vertical gauges agreeing at every shared seam. Its 2-cell is equality of the resulting full path-product Gram certificates. Nonmatching seam signs or non-path-product completions emit no square.

## Double-category laws

The existing analytic certificates establish:

- horizontal associativity and unit laws strictly on ordered edge lists;
- vertical associativity and units strictly by pointwise sign multiplication;
- interchange strictly on full Gram matrices;
- associator pentagon and unitor triangles as identity-isometry equations;
- invertible contiguous Beck–Chevalley identity cells with strict pasting.

Thus this restricted domain is a strict partial double category: composition is partial by typed admission predicates, but every defined law holds as equality rather than only up to an unconstructed token.

## Completion

Uniformly contractive nested chains define bounded positive operators on \(\ell^2\). Principal compression gives a strict finite-to-closed completion functor on the contiguous-inclusion subcategory. Its comparison cells are identities and preserve the restricted Beck–Chevalley cells.

This completion functor is additional structure on the partial double-category fragment; it does not construct companions or conjoints.

## Counterboundary

The fragment refuses:

- unrestricted Green amalgamation;
- mismatched seam gauges;
- noncontiguous probes masquerading as contiguous pullbacks;
- completion without uniform contraction;
- operator-valued kernels without range and commutation certificates.

## Disposition

A genuine analytic partial double-category fragment now exists inside the coherence-pyramid presentation. The full representation remains open because other sectors lack sourced associators/interchange, general Beck–Chevalley, and completion coherence, and no global companion/conjoint structure is proved.

## Verification

- `research/voevodsky/checkers/check_scalar_markov_green_partial_double_category.py`
- `research/voevodsky/results/scalar_markov_green_partial_double_category.json`
