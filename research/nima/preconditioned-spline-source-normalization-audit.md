# Source-normalization audit for the preconditioned spline

## Question

Does an authoritative source in the repository identify the checker’s conventions with a standard Riemann–Weil explicit formula?

## Audited implementation

The checker computes the arithmetic term

\[
-2\sum_{p^m}\frac{\log p}{\sqrt{p^m}}f(\log p^m),
\]

with every supported prime power enumerated. Its archimedean term is

\[
-(\gamma+\log\pi)f(0)
+\sum_{n\ge0}\left(\frac{f(0)}{n+1}-\int_0^\infty f(x)e^{-(n+1/4)x}\,dx\right).
\]

Thus the executable convention data are the argument `log(p^m)`, weight `log(p)/sqrt(p^m)`, arithmetic coefficient `-2`, kernel shift `n+1/4`, and constant `-(gamma+log pi)f(0)`.

## Source search

A repository search for an explicit-formula citation or convention theorem found research packets that refer internally to a Weil form, but no bibliographic source or source-derived map fixing all five executable conventions above. In particular, no located object derives the transform convention connecting the spline variable to the standard test function, or proves that this exact archimedean expansion and arithmetic sign are the same convention used by the intended Weil criterion.

The prior results field `c=5/4` was not read anywhere by the computation. The actual kernel is `n+1/4`; the field was inert metadata, not a normalization parameter. It has been replaced by `kernel_shift=1/4`, and the finite-theorem packet records the retraction.

## First missing typed object

The missing object is an authoritative convention map from a cited explicit-formula theorem to the checker tuple

\[
(\log p^m,\;\log p/\sqrt{p^m},\;-2,\;n+1/4,\;-(\gamma+\log\pi)f(0)).
\]

Acceptance requires a source locator, the source theorem’s test-function and Fourier/Mellin convention, and an algebraic derivation of each component of this tuple. Equal numerical output or checker consistency does not construct that map.

## Disposition

The positive interval remains a theorem about the declared executable form. Promotion to a source-authorized Riemann–Weil criterion is blocked at the missing convention map. No claim about RH or canonical radial–G4 comparison follows.
