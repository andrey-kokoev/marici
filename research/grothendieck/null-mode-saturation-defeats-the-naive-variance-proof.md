# Null-mode saturation defeats the naive variance proof

## Exact model at the convergence wall

The positive precursor has tail

\[
K_0(u)=\frac12e^{-u/2}.
\]

For `0 < x < 1/4`, its tilted transform is

\[
I_0(x)=\int_0^\infty K_0(u)\cosh(\sqrt{x}u)\,du
=\frac{1}{4(1/4-x)}.
\]

The central-strip response used in the variance argument is

\[
H_0(x)=1+(x-1/4)\frac{I_0'(x)}{I_0(x)}=0.
\]

Consequently its response-versus-variance inequality is saturated identically. As `x` approaches `1/4` from below, both the deterministic response and the weighted variance diverge at the same leading order and cancel exactly.

## Source-specific residual

The actual precursor splits as

\[
K=K_0-R_\theta,
\qquad
R_\theta(u)=e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}}>0.
\]

Completion removes the saturated null mode and gives

\[
C(w)=\frac14+(w-1/4)T(w),
\qquad
T(w)=\int_0^\infty R_\theta(u)\cosh(\sqrt w u)\,du.
\]

Thus no concentration theorem based only on positivity or exponential decay of `K` can provide the strict sign. The entire margin comes from the signed subtraction by the source-specific theta remainder and the endpoint constant retained by completion.

At the center, the exact local margin is

\[
H(1/4)=0,
\qquad
H'(1/4)=4T(1/4)>0.
\]

This proves only a neighborhood result. Extending it requires a coupled inequality for `T`, `T'`, and the denominator `1/4+(w-1/4)T`; ordinary variance bounds on the precursor lose precisely this coupling.

## Disposition

The naive tilted-law concentration route is exhausted. A valid continuation must use a source-specific comparison identity for the theta remainder, or directly prove positivity of the coupled endpoint-remainder Loewner kernel. Generic positivity, decay, log-concavity, and repeated Green transfer cannot supply the missing strict margin.
