# Uniform relative pairings bypass the limiting-absorption endpoint for the mixed theta block

## Separation of two seam questions

The failure

\[
B_\Sigma:U\not\to L^2_\sigma,
\qquad \sigma>\frac12,
\]

blocks the standard weighted-space construction of a full arithmetic history
state. It does not automatically block the finite-rank mixed covector

\[
B_\Sigma^\dagger h_\theta
\]

for a particular theta relative history \(h_\theta\).

## Source-metric calculation

Let

\[
b_p=p^{-1/2}u_p
\]

be the primitive incidence columns and suppose the declared relative Green
pairing with one theta history obeys

\[
\sup_p
\left|
\langle u_p,h_\theta\rangle_{\rm rel}
\right|
\le C_h.
\]

The source adjoint is

\[
(B_\Sigma^\dagger h_\theta)_p
=
\frac{p^{-1/2}
\langle u_p,h_\theta\rangle_{\rm rel}}
{\log p}.
\]

Therefore

\[
\|B_\Sigma^\dagger h_\theta\|_U^2
=
\sum_p(\log p)
\left|
(B_\Sigma^\dagger h_\theta)_p
\right|^2
\le
C_h^2
\sum_p\frac1{p\log p}
<\infty.
\]

Hence a uniform relative-pairing bound is sufficient to define the mixed
arithmetic covector at the seam.

## Why this avoids the endpoint conflict

The weighted limiting-absorption test estimates every possible arithmetic
input after its history packet has moved to logarithmic distance. The mixed
block tests only one source-derived theta history against each moved cut atom.
Its arithmetic half-density and source adjoint provide the convergent factor
\(1/(p\log p)\).

Thus the estimates have different quantifiers:

- full state LAP: uniform operator control on all arithmetic packets;
- mixed scalar boundary: one bounded family of relative pairings.

Failure of the first does not imply failure of the second.

## Application to the dressed scalar

If the theta boundary history

\[
h_\theta(x)=R_{H,+}(x)V1
\]

exists as a relative class and satisfies the uniform pairing bound, then

\[
g_U(x)=B_\Sigma^\dagger h_\theta(x)
\in U.
\]

Whenever \(Q_U(x)^{-1}\) has a boundary value on the arithmetic complement,
the correction term is the source pairing

\[
\langle g_U(x),Q_U(x)^{-1}g_U(x)\rangle_U.
\]

Consequently the scalar boundary value of \(F_\theta\) may exist even when the
reconstructed full history state does not belong to a standard LAP space.

## Remaining proof obligation

The required bound is not generic. It must be computed for the actual twisted
causal and anti-causal theta histories and the wall-extended cut atoms:

\[
\sup_{p,k}
\left|
\langle u_{p,k},h_{\theta,\pm}(x)\rangle_{\rm rel}
\right|<\infty
\]

on the declared compact seam interval. Constant or decaying bounds close the
primitive summation. Growth of order \((\log p)^{1/2}\) reaches the divergent
threshold and does not suffice.

The square and connected grades again have stronger arithmetic decay.

## Disposition

The standard LAP endpoint obstruction blocks full-state reconstruction but
not necessarily the mixed scalar boundary value. G4 can split the seam gate
into:

1. a uniform relative-pairing theorem for the scalar Evans determinant;
2. a stronger rigged-history theorem for kernel-state realization.

Neither theorem is currently proved for the twisted theta histories. No RH
conclusion is authorized.
