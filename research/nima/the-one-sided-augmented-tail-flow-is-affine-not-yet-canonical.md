# The one-sided augmented tail flow is affine, not yet canonical

## Direct finite-cell audit

The source-derived one-sided tail state satisfies

\[
(\partial_q+s)G_s(q)+f(q)=0
\]

and its homogeneous augmentation is

\[
\Psi_s=
\binom{G_s}{1},
\qquad
\partial_q\Psi_s=
\begin{pmatrix}
-s&-f(q)\\
0&0
\end{pmatrix}\Psi_s.
\]

This is a valid rank-two source system, but it is not yet a positive canonical system.

A canonical system requires

\[
J\partial_qY=zH(q)Y,
\qquad H(q)=H(q)^*\ge0,
\]

after a source-authorized spectral centering \(s=s_0+\alpha z\). In the raw augmented flow:

- the forcing entry \(-f(q)\) is independent of \(z\);
- the spectral coefficient acts only on the tail coordinate;
- the displayed generator is triangular rather than \(J\)-Hamiltonian;
- the constant source channel is affine data masquerading as a homogeneous coordinate.

Therefore the rank-two augmentation cannot simply be relabeled as the desired canonical system.

## Gauge-removal test

One may try a source-dependent triangular gauge

\[
\Psi_s(q)=T(q)Y_s(q)
\]

to remove the \(z\)-independent forcing. The transformed equation is

\[
\partial_qY_s
=
\left(
T^{-1}
\begin{pmatrix}
-s&-f\\
0&0
\end{pmatrix}
T
-
T^{-1}T'
\right)Y_s.
\]

For this to authorize a canonical system, the same \(T\) must satisfy all of:

1. it is independent of the spectral parameter;
2. it is source-derived from the tail/history cell;
3. it preserves the boundary and wall ports;
4. it is symplectic, or carries the source Green form to a declared symplectic form;
5. the remaining spectral coefficient equals \(-JH\) with \(H\ge0\);
6. \(T\) and \(T^{-1}\) remain uniformly controlled at completion.

An arbitrary variation-of-constants gauge can remove \(f\), but generally does not satisfy the symplectic and metric conditions. It would reproduce endpoint scalars without authorizing Wronskian positivity.

## Consequence

The one-sided flow supplies the outgoing solution and boundary evaluation, not the positive Hamiltonian by itself. The missing positive canonical geometry must arise from the doubled reciprocal system together with the wall and archimedean channels, exactly where the indefinite forcing polarization can cancel or become a source norm.

The next finite object is therefore not a \(2\times2\) canonicalization of the one-sided triangle. It is the doubled finite-cell generator

\[
\mathcal D_{s}^{+}\oplus\mathcal D_{1-s}^{-}
\]

with its complete Green matrix. The audit should ask whether a source-derived reduction of that matrix produces a nondegenerate symplectic quotient and a positive Hamiltonian.

## Minimal hostiles

- A triangular gauge removes \(f\) and matches the endpoint transform but is not symplectic.
- A symplectic gauge exists but produces an indefinite \(H\).
- The finite doubled quotient is positive, but its wall direction lies in the radical.
- Valid finite gauges have unbounded inverse norms as the tail cutoff grows.

Thus the first real canonical-system theorem is a doubled Green reduction theorem, not a relabeling of the one-sided homogeneous augmentation.
