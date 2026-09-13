# Dense Green-context refinement has quadratic conditioning cost

## Uniform contexts

Take uniformly spaced contexts with gap \(h>0\) and set

\[
\rho=e^{-h}.
\]

The Green Gram matrix is

\[
K_{ij}=\rho^{|i-j|}.
\]

Its infinity norm obeys

\[
\|K\|_\infty
\le\frac{1+\rho}{1-\rho}.
\]

The exact tridiagonal inverse has the same row-sum bound:

\[
\|K^{-1}\|_\infty
\le\frac{1+\rho}{1-\rho}.
\]

Therefore

\[
\kappa_\infty(K)
\le
\left(\frac{1+\rho}{1-\rho}\right)^2.
\]

## Dense-spacing asymptotic

As \(h\to0\),

\[
\rho=e^{-h}=1-h+O(h^2),
\]

so

\[
\left(\frac{1+\rho}{1-\rho}\right)^2
\sim\frac4{h^2}.
\]

On a fixed interval of length \(L\), uniform refinement has

\[
h=\frac{L}{n-1},
\]

and hence the conditioning bound grows as

\[
O(n^2).
\]

## Meaning

Exact full rank does not imply stable coordinate recovery. As contexts become dense, neighboring kernel states become nearly dependent. The innovation norm

\[
1-\rho^2\sim2h
\]

shrinks, while the corresponding precision coefficient diverges like \(1/(2h)\).

Thus the complete realization has two distinct finite-depth costs:

```text
state count:          n
nearest-neighbor work: O(n)
worst-case conditioning bound: O(n^2) on a fixed interval
```

The local innovation basis avoids dense matrix inversion but cannot remove the intrinsic collision-scale amplification.

## Protocol implication

Approximate finite controllers should select context spacing using a conditioning threshold, not rank alone. Adding contexts below the noise-resolved separation scale contributes exact algebraic rank but little stably recoverable information.

This does not justify quotienting those contexts in the exact theory. It supplies a quantitative criterion for an explicitly approximate protocol.

## Verification

```text
python research/coherence/check_uniform_green_conditioning_bound.py
```

The checker verifies the norm bound exactly for 16 combinations of context count and rational correlation.

Artifacts:

- `check_uniform_green_conditioning_bound.py`
- `uniform-green-conditioning-bound.v1.json`
