# Orthogonal prime penalties fail on the first centered gamma two-prime block

Write `a=log m`, `b=log n` and

```
F(a)=psi(1/4+a/2)-psi(1/4).                           (1)
```

Expanding the gamma density as

```
2e^(-u/2)/(1-e^(-2u))=2 sum_(k>=0)e^{-(2k+1/2)u}
```

and integrating the endpoint-centered vectors gives the closed formula

```
G(m,n)=F(log m)+F(log n)-F(log(mn)).                  (2)
```

This is the exact centered gamma Gram derived previously.

## The naive prime typing

A tempting model represents the negative von Mangoldt contribution as an
orthogonal penalty on each prime label:

```
Q_P = G_P - diag((log p)/sqrt(p)).                     (3)
```

It passes every one-prime test in the initial range: for example
`G(2,2)` is about `1.7960`, much larger than `log(2)/sqrt(2)`, about
`0.4901`. But the first coupled block, for primes `2` and `3`, has

```
Q_{2,3} approximately
[[1.30588065, 2.06759606],
 [2.06759606, 1.77538305]],                            (4)
```

whose determinant is approximately `-1.95651509`. Thus it is indefinite.
The numerical sign has a margin far larger than the explicit truncation bound
from the positive digamma series.

## Meaning

This falsifies the *orthogonal diagonal-penalty model*, not Weil positivity.
The centered gamma vectors for `2` and `3` are strongly correlated; subtracting
their prime costs independently destroys the narrow positive transverse
channel even though neither individual cost exceeds its diagonal energy.

Hence the prime contribution must be represented by a coupled evaluation or
incidence operator whose off-diagonal terms participate in the same Schur
complement. Equivalently, the source-derived prime map cannot factor through
an orthogonal Hilbert space with one unrelated negative coordinate per prime.
The next construction must retain the additive prime-power translation map
before forming its norm.

## Scope

Equation (2) is exact. The hostile computation is a certified numerical
falsifier of (3). Model (3) has not been identified with the actual Weil
form, so its failure is a typing correction and not evidence against RH.
