# Rank-two Weil convexity also propagates only toward broader smoothing

## Rank-two field

Use forward heat parameter

\[
\tau=\frac1{4t}
\]

and let `U(tau,xi)` be the positively rescaled completed Gaussian kernel, so

\[
U_\tau=U_{\xi\xi}.
\]

On a region where `U>0`, put

\[
F=\log U,
\qquad
q=F_{\xi\xi}+\frac1{2\tau}.
\]

For the spectral multiplication form, the midpoint Gram determinant condition is exactly `q>=0`, since rescaling by a parameter-only positive factor does not change character curvature and `2t=1/(2tau)`. This is not yet the source-translation Weil Gram condition: source translation Fourier-transforms to a character-weighted centered Gaussian.

## Exact evolution

The logarithmic heat equation is

\[
F_\tau=F_{\xi\xi}+F_\xi^2.
\]

Differentiating twice and substituting `F_xixi=q-1/(2tau)` gives

\[
q_\tau
=q_{\xi\xi}+2F_\xi q_\xi+2q^2-\frac{2}{\tau}q.
\]

At a first spatial minimum where `q=0`,

\[
q_\tau=q_{\xi\xi}\ge0.
\]

Hence nonnegative rank-two curvature propagates under forward heat flow, toward increasing `tau` and therefore decreasing `t`.

## No-go consequence

The known broad-smoothing regime is already the forward direction. The curvature maximum principle cannot transport rank-two PSD from broad probes to narrower probes. As with pointwise positivity, the desired continuation in increasing `t` is backward parabolic.

This equation does explain the conditional RH model: convolution of a positive spectral measure has `q` equal to a tilted variance and remains nonnegative under smoothing. It does not establish that the source distribution before smoothing is positive.

## Disposition

Reject a heat-flow proof of global rank-two Gram positivity that starts only from broad smoothing. The remaining rank-two proof must establish

\[
\partial_\xi^2\log\Theta(t,\xi)+2t\ge0
\]

directly from the completed endpoint--gamma--prime formula, or supply a narrow-probe boundary condition. Higher-rank PSD requires additional matrix inequalities beyond this scalar curvature field.
