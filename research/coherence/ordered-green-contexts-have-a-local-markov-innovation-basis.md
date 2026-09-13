# Ordered Green contexts have a local Markov innovation basis

## Construction

Let

\[
x_1<\cdots<x_n,
\qquad
k_i(t)=e^{-|t-x_i|},
\qquad
\rho_i=e^{-(x_{i+1}-x_i)}.
\]

Define

\[
r_1=k_1,
\]

\[
r_i=k_i-\rho_{i-1}k_{i-1}
\qquad(i\ge2).
\]

For every \(j<i\), exponential multiplicativity gives

\[
\langle k_i,k_j\rangle
=\rho_{i-1}\langle k_{i-1},k_j\rangle.
\]

Hence

\[
\langle r_i,k_j\rangle=0.
\]

The innovations \(r_i\) are therefore mutually orthogonal.

## Norms

Their squared norms are

\[
\|r_1\|^2=1,
\]

\[
\|r_i\|^2=1-\rho_{i-1}^2.
\]

Thus the ordered Green realization decomposes canonically as

\[
E_{\{x_1,\ldots,x_n\}}
=
\mathbb C r_1
\mathbin{\perp}
\mathbb C r_2
\mathbin{\perp}\cdots\mathbin{\perp}
\mathbb C r_n.
\]

Each new state direction depends only on the new point and its immediate predecessor.

## Gram diagonalization

Let \(R\) be the lower bidiagonal change-of-basis matrix with diagonal entries one and subdiagonal entries \(-\rho_i\). Then

\[
RKR^T
=
\operatorname{diag}
(1,1-\rho_1^2,\ldots,1-\rho_{n-1}^2).
\]

The determinant product formula follows immediately.

## Interpretation

Full contextual rank does not imply globally entangled state coordinates. In ordered one-dimensional geometry, the minimal realization has one local orthogonal innovation per newly crossed edge:

```text
context point x_1: base state
context point x_i: innovation relative to predecessor x_(i-1)
```

The state dimension remains \(n\), but its dependency graph is first-order Markov. This sharpens the earlier complexity distinction:

```text
behavioral dimension = unbounded
interaction width     = nearest neighbor
local operator order  = two
```

## Infinite limit

For a locally finite increasing context sequence, normalized innovations

\[
e_i=r_i/\sqrt{1-\rho_{i-1}^2}
\]

form an orthonormal system. When the context set is dense, collision-scale factors tend to zero and normalization becomes singular, while the unnormalized directed system remains valid. This is the determinant-line degeneration already seen at collision strata.

## Verification

```text
python research/coherence/check_green_markov_innovation_basis.py
```

The checker exactly diagonalizes Green Gram matrices through ten ordered points.

Artifacts:

- `check_green_markov_innovation_basis.py`
- `green-markov-innovation-basis.v1.json`
