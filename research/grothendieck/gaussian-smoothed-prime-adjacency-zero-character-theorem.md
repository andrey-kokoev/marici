# The prime heat kernel is the zero character of a smoothed adjacency

For `t>0`, apply the common log-Gaussian cutoff to the prime-power translation
adjacency:

```
A_t = sum_(n>=2) Lambda(n)/sqrt(n)
      exp[-(log n)^2/(4t)] (S_(log n)+S_(log n)^*).     (1)
```

The coefficient series converges absolutely for every `t>0`, so `A_t` is a
bounded self-adjoint convolution operator. Its Fourier multiplier is

```
a_t(xi)=2 sum_(n>=2) Lambda(n)/sqrt(n)
        exp[-(log n)^2/(4t)] cos(xi log n).             (2)
```

All coefficients are nonnegative. Hence the triangle bound is attained at
the trivial character:

```
||A_t|| = a_t(0)
        =2 sum_(n>=2) Lambda(n)/sqrt(n)
          exp[-(log n)^2/(4t)].                        (3)
```

The previously derived prime heat kernel is exactly

```
K_prime(t) = -a_t(0)/(4 sqrt(pi t)).                   (4)
```

Thus the inverse-Laplace heat calculation and the translation-adjacency
calculation are two views of the same smoothed arithmetic object.

## The zero-character limitation

The completed scalar heat target

```
Theta(t)=K_endpoint(t)+K_gamma(t)+K_prime(t)           (5)
```

tests only the trivial translation character `xi=0`. Its positivity for all
`t` is the complete-Bernstein/Stieltjes gate already identified with the
squared Xi divisor. It does not, without another theorem, imply positivity of
a completed convolution operator at every `xi`.

An operator construction would need either

```
h_t(xi)-a_t(xi) >= 0             for every real xi,    (6)
```

for a correctly completed archimedean symbol `h_t`, or a positive dilation
whose compression gives the completed quadratic form. Knowing (5) controls
only `xi=0`; a scalar value cannot control all Fourier characters.

## Two distinct research routes

1. **Scalar Stieltjes route:** prove that `Theta(t)` is completely monotone in
   `t`, not merely nonnegative. This is the RH-equivalent Laplace-measure gate
   and reconstructs a positive squared-zero measure, subject to the
   previously recorded multiplicity issue.
2. **Translation-operator route:** construct the full two-variable completed
   kernel and prove all-character positivity. This could explain
   self-adjointness directly but may be strictly stronger than RH.

These routes share the same zero-character arithmetic kernel but must no
longer be conflated. The next operator-level falsifier should probe a nonzero
character under one common gamma/endpoint/prime smoothing.
