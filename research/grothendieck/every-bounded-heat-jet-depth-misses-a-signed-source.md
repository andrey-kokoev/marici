# Every bounded heat-jet depth misses a signed source

## Question

Can complete monotonicity of the scalar source be replaced by checking heat jets only through a fixed derivative order?

## Hostile signed measure

Fix a derivative cutoff `M>=0` and choose `a>1`. On the squared spectral half-line, take

\[
\nu_M=\delta_1-a^{-M}\delta_a.
\]

Its Laplace transform is

\[
H_M(t)=e^{-t}-a^{-M}e^{-at}.
\]

The heat jets are

\[
J_k^{(M)}(t)
=(-1)^kH_M^{(k)}(t)
=e^{-t}-a^{k-M}e^{-at}.
\]

For every `0<=k<=M` and `t>0`,

\[
a^{k-M}e^{-at}
\le e^{-at}<e^{-t},
\]

so

\[
J_k^{(M)}(t)>0.
\]

At the next order,

\[
J_{M+1}^{(M)}(t)
=e^{-t}-a e^{-at}.
\]

This is negative whenever

\[
0<t<\frac{\log a}{a-1}.
\]

Thus the signed source passes every heat-scale test through order `M` and fails at order `M+1`.

## Entire-kernel conformance

The symmetric square-root lift is

\[
\mu_M
=
\frac12(\delta_1+\delta_{-1})
-
\frac{a^{-M}}2
(\delta_{\sqrt a}+\delta_{-\sqrt a}).
\]

Its kernel

\[
K_M(t,z)
=e^{-t}\cos z
-a^{-M}e^{-at}\cos(\sqrt a\,z)
\]

is even, entire, satisfies `K_t=K_zz`, and obeys every heat-jet, Gram-evaluation, and imaginary-character conformance identity exactly. The failure is purely order-theoretic.

## Gram manifestation

Since `mu_M` has a negative component, the translation kernel is not positive definite. Joint faithfulness guarantees some finite translate packet has a negative Gram direction, although its required rank and geometry need not be bounded by `M`.

## Meta-observer consequence

For every bounded jet depth there is a coherent signed source invisible to all tested inequalities. Therefore the natural constructor must quantify over all derivative orders or produce the Bernstein measure directly. Increasing arithmetic cutoff or checking more heat scales at the same bounded derivative depth does not repair the deficiency.

## Disposition

This fixture proves bounded heat-jet nonfaithfulness with exact residual localization: orders `0` through `M` are strictly positive, and the first forced negative residual occurs at order `M+1` for small positive heat scale.
