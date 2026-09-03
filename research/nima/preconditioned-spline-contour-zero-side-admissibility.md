# Contour and zero-side admissibility of the preconditioned spline

## Question

Does the spline test have enough decay to justify the completed-zeta contour identity and its zero-side sum?

## Transform decay

The centered degree-7 cardinal spline is compactly supported and `C^6`; its seventh derivative has bounded variation. Its Fourier transform is a scaled eighth power of a sinc function. Multiplication by the bounded five-shift trigonometric square does not change decay. For the convention

\[
h(t)=\int_{-\infty}^{\infty}f(2x)e^{itx}\,dx,
\]

there is a constant `C` such that, uniformly for complex `t` in every fixed horizontal strip,

\[
|h(t)|\le C(1+|\operatorname{Re}t|)^{-8}.
\]

Uniformity follows either from the exact sinc-power formula or from eight distributional integrations by parts; compact support bounds the strip-dependent exponential factor.

## Consequences

1. The gamma-side pairing is absolutely integrable because the logarithmic derivative of the gamma factor grows logarithmically while `h(t)` decays with power eight.
2. The prime-power sum is finite, not merely conditionally convergent, because `f(log(p^m))` vanishes outside compact support.
3. On horizontal contour segments chosen away from zeros and poles, standard completed-zeta logarithmic-derivative bounds grow at most polylogarithmically. Multiplication by `h(t)` makes those segments vanish as their height tends to infinity.
4. Nontrivial zeros lie in a fixed vertical strip. With the standard zero-count bound `N(T)=O(T log T)`, the sum of absolute values of the zero tests converges:

\[
\sum_{\rho}\left|h\left(\frac{\rho-1/2}{i}\right)\right|<\infty.
\]

Indeed, the bounded imaginary displacement stays inside a fixed strip, while summation by parts against `N(T)` reduces convergence to the integrability of `T^{-8} log T`.

## Conditional identity

Assuming the declared completed-zeta factorization, its meromorphic continuation and functional equation, the standard zero-count bound, and contours avoiding zeros with the stated logarithmic-derivative estimate, residue calculus gives the zero-side identity whose nonzero terms are exactly the pole evaluations plus the archimedean and arithmetic tuple derived in `completed-zeta-to-spline-convention-map.md`. On the baseline pole-annihilating ray, the pole evaluations vanish.

## Claim boundary

The spline supplies all test-function regularity, decay, absolute convergence, and exchange-of-limit conditions. This packet does not independently prove meromorphic continuation, the functional equation, the zero-count theorem, or the off-zero contour bound for zeta. Those are the remaining declared analytic inputs. No RH assumption is used in the convergence argument, and no radial–G4 comparison follows.

## Disposition

The contour and zero-side operations are admissible conditional on the named standard completed-zeta inputs. The remaining gap is no longer a test-function regularity defect; it is external theorem authority for those zeta inputs and the absent G4 comparison map.
