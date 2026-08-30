# Heat smoothing repairs the prime Hermitian norm but diagonalizes away spectral location

On the critical line, the prime amplitude operator has diagonal entries

```
q_T(p)=p^(-1/2-iT).                                    (1)
```

Its Hermitian squared norm is

```
sum_p |q_T(p)|^2=sum_p 1/p=infinity.                  (2)
```

This is the quadratic `k=2` obstruction removed by the third regularized
determinant. Oscillation in `T` cannot help because conjugation cancels it.

For `tau>0`, introduce logarithmic heat smoothing

```
q_(T,tau)(p)
 =p^(-1/2-iT) exp[-tau(log p)^2/2].                    (3)
```

Then

```
||q_(T,tau)||_2^2
 =sum_p p^(-1) exp[-tau(log p)^2] < infinity.          (4)
```

The Gaussian beats every fixed power at sufficiently large prime, so the
sum converges for every positive `tau`.

## Phase-blindness obstruction

The right side of (4) is independent of `T`. Thus heat smoothing repairs the
Hilbert norm but a diagonal norm of prime amplitudes cannot detect spectral
height or distinguish a Riemann zero from a generic point on the critical
line.

To retain spectral information one needs off-diagonal correlations such as

```
q_T(p) conj(q_T(q))
 =(pq)^(-1/2) exp[-iT(log p-log q)],                   (5)
```

whose phase depends on the logarithmic difference. This returns exactly to
the relative difference correspondence. The diagonal `p=q` sector supplies
the divergent norm; the quotient/off-diagonal sector carries spectral
location.

## Relation to the existing heat kernel

The previously derived source heat kernel contains Gaussian factors in
`log n`. Equation (3) shows why such smoothing is the natural Schatten
regularization of prime amplitudes. But the explicit heat kernel is a signed
linear prime-power sum, whereas (4) is a positive quadratic prime sum. A
paired source theorem must derive the correct off-diagonal kernel and its
renormalized diagonal, not identify these two objects by analogy.

## Falsifier

A proposed Hermitian prime norm fails as an RH detector if it is only the
diagonal quantity (4): it is finite and positive but independent of `T`.
Conversely, the unsmoothed diagonal norm (2) is not a legitimate finite
observable.

