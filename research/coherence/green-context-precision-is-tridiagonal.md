# Green context precision is tridiagonal

## Exact inverse

For ordered contexts \(x_1<\cdots<x_n\), let

\[
K_{ij}=e^{-|x_i-x_j|},
\qquad
\rho_i=e^{-(x_{i+1}-x_i)}.
\]

Although \(K\) is dense, its inverse \(Q=K^{-1}\) is tridiagonal. The off-diagonal entries are

\[
Q_{i,i+1}=Q_{i+1,i}
=-\frac{\rho_i}{1-\rho_i^2}.
\]

The endpoint entries are

\[
Q_{11}=\frac1{1-\rho_1^2},
\qquad
Q_{nn}=\frac1{1-\rho_{n-1}^2},
\]

and the interior entries are

\[
Q_{ii}
=
\frac1{1-\rho_{i-1}^2}
+
\frac{\rho_i^2}{1-\rho_i^2}.
\]

For one context, \(Q=(1)\).

## Local energy

Equivalently, for a coordinate vector \(c\),

\[
c^TQc
=c_1^2+
\sum_{i=1}^{n-1}
\frac{(c_{i+1}-\rho_ic_i)^2}{1-\rho_i^2}.
\]

Thus complete labelled-context geometry is governed by a nearest-neighbor energy despite its dense covariance matrix.

## Consequences

### Local computation

Evaluation, conditioning, and determinant updates can be implemented with linear rather than dense cubic complexity. The unbounded realization has finite interaction width.

### Markov separation

Once the state at a context point is retained, contexts strictly to its left and right are conditionally decoupled. This is the matrix form of the local innovation theorem.

### Collision singularity

As two contexts collide, \(\rho_i\to1\), so the corresponding precision coefficients diverge. The covariance loses rank while the precision penalizes their difference infinitely strongly. This gives the dual description of determinant-line degeneration.

## Structural distinction

```text
covariance/Hankel matrix: dense and full rank
precision/generator:      tridiagonal and local
```

Therefore Hankel rank alone measures state dimension, not computational locality. The minimal realization is infinite in the complete limit but retains a second-order nearest-neighbor precision law.

## Verification

```text
python research/coherence/check_green_gram_tridiagonal_precision.py
```

The checker verifies the exact inverse and bandwidth through twelve contexts.

Artifacts:

- `check_green_gram_tridiagonal_precision.py`
- `green-gram-tridiagonal-precision.v1.json`
