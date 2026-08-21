# Gaussian smoothing of the Weil distribution produces the full character kernel

Let `W` be the centered additive Weil distribution, with Fourier conventions
fixed so that under RH its spectral transform is the positive divisor measure

```
W_hat = sum_gamma m_gamma delta_gamma.                 (1)
```

For `t>0`, multiply `W` in log displacement by the normalized Gaussian and
Fourier transform:

```
Theta(t,xi)
 = Fourier[ W(x) exp(-x^2/(4t))/(2 sqrt(pi t)) ](xi).  (2)
```

Multiplication becomes convolution. Since the Fourier transform of the
normalized Gaussian is `exp(-t xi^2)`, equation (1) gives

```
Theta(t,xi)
 = (1/2) sum_(gamma signed) m_gamma
   exp[-t(xi-gamma)^2] >= 0.                           (3)
```

Thus the completed all-character smoothed kernel is a Gaussian mixture
centered at the Xi ordinates. Its zero-character slice is

```
Theta(t,0)=sum_(gamma>0) m_gamma exp(-t gamma^2),      (4)
```

the spectral heat trace already reconciled with the endpoint, gamma, and
prime source formula. The factor `1/2` in (3) removes double counting of the
reflection pair `+/-gamma`.

## Arithmetic side

The prime atoms at displacements `+/- log n` contribute, in the normalization
already fixed by the scalar heat kernel,

```
K_prime(t,xi)
 =-1/(2 sqrt(pi t)) sum_(n>=2) Lambda(n)/sqrt(n)
   exp[-(log n)^2/(4t)] cos(xi log n).                 (5)
```

At `xi=0` this is exactly the known negative prime heat kernel. Equation (5)
is also the nonzero-character multiplier of the Gaussian-smoothed paired
translation adjacency, with its universal scalar factor. Endpoint and gamma
terms must be transformed by the same Gaussian and character; they may not be
copied unchanged from the zero slice.

## Positivity equivalence

If RH holds, (3) proves `Theta(t,xi)>=0` for every `t>0` and real `xi`.
Conversely, if these Gaussian regularizations are positive for all `t,xi`,
then letting the displacement Gaussian tend to one gives positivity of `W` as
a tempered distribution (tested first on Gaussian-regularized Schwartz
squares and then by density). By Weil's criterion this forces RH.

Hence full Gaussian-kernel positivity is an RH-equivalent formulation, not a
strictly stronger operator conjecture, provided the limiting distributional
argument is carried out on the declared test space.

## New source-only target

Derive explicit `K_endpoint(t,xi)` and `K_gamma(t,xi)` and prove

```
K_endpoint(t,xi)+K_gamma(t,xi)+K_prime(t,xi) >= 0      (6)
```

without using zero locations. A negative value at one finite `(t,xi)` is a
direct Weil-square falsifier. Unlike the zero slice, varying `xi` exposes the
translation characters and therefore supplies the kernel needed for a GNS
self-adjoint construction.

The remaining analytic cautions are convergence of the zero sum away from
RH, exact Fourier normalization, and justification of the Gaussian limit;
none may be replaced by a finite zero sweep.
