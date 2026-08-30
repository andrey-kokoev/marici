# The completed determinant needs mixed prime-sewing naturality

## What the finite prime theorem settles

Distinct finite prime additions act on separate labelled diagonal components. Their normalized determinant increments commute exactly. Complete rank-two coverage therefore settles all finite prime-order coherence.

It does not settle compatibility with completion. The remaining faces mix different constructor types:

- finite prime addition;
- archimedean completion;
- reciprocal transport between the two valuation sectors;
- restricted-product or cutoff completion.

## The local reciprocal square

For one prime, define the two local Euler charts

\[
E_p^+(s)=\frac{1}{1-p^{-s}},
\qquad
E_p^-(s)=\frac{1}{1-p^{s-1}}.
\]

Their source transition is

\[
\gamma_p(s)=\frac{1-p^{-s}}{1-p^{s-1}},
\qquad
E_p^-(s)=\gamma_p(s)E_p^+(s).
\]

Taking logarithmic connections gives the exact naturality identity

\[
d\log E_p^- - d\log E_p^+ = d\log\gamma_p.
\]

This is the mixed prime-sewing square. Reciprocal transport does not commute with a prime addition as the same arrow; it transports the positive-cone constructor into the negative-cone constructor, with \(\gamma_p\) as the typed comparison cell.

## The archimedean square

Let \(A_X(s)\) denote the completion factor attached to cutoff \(X\). Prime addition commutes with archimedean completion only if

\[
\frac{A_{X\cup\{p\}}(s)}{A_X(s)}
\]

is the source-declared mixed comparison. If \(A_X=A\) is truly cutoff-independent, this ratio is \(1\). If endpoint regularization or boundary renormalization makes \(A_X\) cutoff-dependent, its logarithmic derivative and basepoint value are additional anomaly coordinates.

Finite prime holonomy cannot detect such an anomaly because it lives on a different family of faces.

## Completion as a natural transformation

The completed determinant family is coherent only when completion is a normalized natural transformation on the finite cutoff diagram. For every prime and cutoff, the compiler must test:

1. equality of source and target domains on the two mixed paths;
2. equality of logarithmic connections after inserting the declared comparison cell;
3. identity basepoint holonomy;
4. compatibility of the comparison with subsequent prime additions;
5. local uniform convergence of the normalized mixed cells on compact zero-free regions.

The reciprocal comparison is typed by \(\gamma_p\), not by identity. The archimedean comparison may be identity only after source derivation proves cutoff independence.

## Finite falsifier

For reciprocal sewing, compute

\[
R_p(s)=d\log E_p^- - d\log E_p^+ - d\log\gamma_p.
\]

For archimedean completion, compute

\[
R_{A;X,p}(s)=d\log A_{X\cup\{p\}}-d\log A_X-d\log\alpha_{X,p},
\]

where \(\alpha_{X,p}\) is the declared source comparison. Any nonzero residual or nonidentity basepoint holonomy falsifies functorial completion.

## Scope

Passing these mixed squares proves that finite determinant authority survives the completion constructors. It still does not orient the resulting divisor or prove zero confinement. It prevents completion from silently changing the finite source section.

