# Source formula for the Gaussian translation rectangle

## Question

How can the complete stationary Weil correlations on `1,2,3,6` be evaluated without zero data?

## Correct Gaussian family

Let a logarithmic test have spectral amplitude

`G(u)=exp(-t u^2/2)`.

Translating the logarithmic test by `a` multiplies its spectral amplitude by `exp(i a u)`. Therefore the cross correlation between translates separated by `a` is the Weil functional applied to

`h_(t,a)(u)=exp(-t u^2) cos(a u)`.

This is not the shifted-spectral Gaussian `exp(-t(u-xi)^2)`. The latter tests a different family. The stationary rectangle must use modulation by the logarithmic displacement.

## Explicit source formula

Define

`K_t(a)=W(h_(t,a))`.

The completed explicit formula gives

`K_t(a)=E_t(a)+Gamma_t(a)+P_t(a)`,

with endpoint term

`E_t(a)=exp(t/4) cosh(a/2)`,

archimedean term

`Gamma_t(a)= -log(pi)/(4 sqrt(pi t)) exp(-a^2/(4t))`

` +1/(4pi) integral_R exp(-t u^2) cos(a u) Re psi(1/4+i u/2) du`,

and prime term

`P_t(a)= -1/(4 sqrt(pi t)) sum_(n>=2) Lambda(n)/sqrt(n)`

` * [exp(-(log n-a)^2/(4t))+exp(-(log n+a)^2/(4t))]`.

At `a=0` this reduces to the known centered Gaussian heat formula. Every term is source-side; no zero ordinate is used.

## Rectangle values

When `K_t(0)>0`, normalize

`k_t(a)=K_t(a)/K_t(0)`.

The multiplicative rectangle has

`r=k_t(log2)`,

`s=k_t(log3)`,

`c=k_t(log6)`,

`d=k_t(log(3/2))`.

Its two exact parity determinants are

`D_+=(1+c)(1+d)-(r+s)^2`,

`D_-=(1-c)(1-d)-(r-s)^2`.

A negative value is a finite Gaussian negative Weil square and would disprove RH. Positive sampled values are only finite evidence.

## Numerical certification contract

A valid scout must:

1. bound the digamma integral tail uniformly;
2. enumerate all prime powers with Gaussian tails enclosed;
3. use directed interval arithmetic for `K_t(0),r,s,c,d`;
4. certify the sign of both determinants;
5. include a deliberate normalization failure using the shifted-spectral Gaussian to show the two families differ.

Broad-smoothing positivity guarantees a nonempty small-`t` region where all finite Gaussian Gram matrices are positive. The hostile search should move toward narrower smoothing while preserving certified source evaluation.

## Disposition

The previously missing complete four correlations now have an explicit zero-free source formula. The next executable step is a directed interval scout over `t`; no G4 carrier is required for this first mixed-prime falsifier.
