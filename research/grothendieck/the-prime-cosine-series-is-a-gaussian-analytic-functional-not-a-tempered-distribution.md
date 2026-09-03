# The prime cosine series is a Gaussian analytic functional, not a tempered distribution

## Question

What is the smallest explicit distributional completion on which the infinite prime cosine functional is defined before any positivity assertion?

## Failure of tempered-distribution growth

Place the prime-power coefficients on logarithmic frequency space:

\[
\mu_P=\sum_{n\ge2}\Lambda(n)n^{-1/2}\delta_{\log n}.
\]

The mass below frequency `R` is

\[
\mu_P([0,R])=
\sum_{n\le e^R}\Lambda(n)n^{-1/2}.
\]

This grows exponentially in `R` rather than polynomially. Consequently `mu_P` is not a tempered measure, and its Fourier cosine synthesis cannot be justified as a tempered distribution merely from coefficient growth. Schwartz decay in logarithmic frequency is insufficient.

## Gaussian test spaces

For `a>0`, define the even Fourier test space

\[
\mathcal B_a=
\left\{f:
\|f\|_a=
\sup_{\lambda\in\mathbb R}
e^{a\lambda^2}|\widehat f(\lambda)|<\infty
\right\},
\]

restricted to functions for which the Fourier transform and inversion convention are defined. On this space set

\[
\mathcal P(f)=
-\frac1{2\pi}
\sum_{n\ge2}\Lambda(n)n^{-1/2}
\operatorname{Re}\widehat f(\log n).
\]

Then

\[
|\mathcal P(f)|
\le C_a\|f\|_a,
\qquad
C_a=rac1{2\pi}
\sum_{n\ge2}\Lambda(n)n^{-1/2}e^{-a(\log n)^2}<\infty.
\]

Convergence follows because Gaussian decay in `log n` dominates every exponential growth in that variable. Thus the prime cosine series defines a continuous functional on every `B_a`.

Let

\[
\mathcal B_G=\bigcup_{a>0}\mathcal B_a
\]

with its natural inductive-limit interpretation: a test is admitted when its Fourier transform has some strictly positive Gaussian decay rate. The prime functional is well-defined stepwise on this Gaussian analytic test class.

## Inclusion of every finite Hankel probe

For a degree-`d` polynomial `p`, the function

\[
f_{t,h,p,q}(u)=
e^{-tu^2}(1-e^{-hu^2})
p(e^{-hu^2})\overline{q(e^{-hu^2})}
\]

is a finite linear combination of Gaussians `e^{-A u^2}` with `A>0`. Its Fourier transform is a finite linear combination of Gaussians

\[
\sqrt{\frac{\pi}{A}}e^{-\lambda^2/(4A)}.
\]

Hence every finite polynomial matrix coefficient belongs to `B_G`, although the available decay rate decreases as the polynomial degree and largest Gaussian exponent increase.

The infinite prime form therefore has an exact sesquilinear definition on the entire polynomial core:

\[
q_P(p,q)=\mathcal P(f_{t,h,p,q}).
\]

This definition uses absolute convergence in logarithmic frequency and does not require a pointwise multiplier `W_P(u)`.

## Coupled completion

The gamma and endpoint functionals are already defined on these Gaussian probes by their explicit kernels. Their sum gives a well-defined coupled analytic functional and hence a sesquilinear form on polynomials. This is the requested distributional completion at the level of test functions.

It is not yet a closed Hilbert-space form. The constants `C_a` diverge as `a` decreases to zero, exactly matching the monomial concentration obstruction at increasing degree. Continuity on each Gaussian test step supplies no bound in the original moment norm and no common graph norm over all degrees.

## Relation to the order completion

Heat-evaluation Riesz vectors are total in the order Hilbert space, so Gaussian probes are not deficient in ordinary Hilbert density. What remains unproved is graph or form-core density for the coupled analytic functional. The distinction is necessary because the operator norm deteriorates across the Gaussian steps.

## Disposition

A source-derived distributional completion now exists: the prime side is a Gaussian analytic functional on `B_G`, and the completed gamma–prime form is defined on every finite polynomial probe. The remaining obstruction is precisely Hilbert closability and semiboundedness across the inductive limit. Calling this object tempered, Radon-measure-valued, or closed would be unsupported.