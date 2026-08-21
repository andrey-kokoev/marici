# Logarithmic cutoff matching cancels the prime and oscillator variances

The critical prime source truncated at `p<=P` has positive covariance trace

```
V_prime(P)=sum_(p<=P) 1/p
          =log log P+B_1+o(1),                         (1)
```

where `B_1` is the prime Mertens constant.

The canonical even oscillator for the gamma factor has spectrum

```
lambda_k=k+1/4,             k=0,1,2,... .              (2)
```

Its inverse covariance trace through `K` modes is

```
V_gamma(K)=sum_(k=0)^(K-1) 1/(k+1/4)
          =psi(K+1/4)-psi(1/4)
          =log K-psi(1/4)+o(1).                       (3)
```

Prime incidence lives at logarithmic source positions `u=log p`. Therefore a
prime cutoff `p<=P` canonically corresponds to an archimedean mode cutoff

```
K(P)=floor(log P).                                     (4)
```

With this pairing,

```
V_prime(P)-V_gamma(K(P))
  -> B_1+psi(1/4).                                     (5)
```

The leading `log log P` divergence cancels without fitting a cutoff exponent.
The finite archimedean constant is fixed by the same quarter shift that
produces the gamma factor and the metaplectic eighth phase:

```
psi(1/4)=-EulerGamma-pi/2-3 log 2.                     (6)
```

## What this achieves

This supplies the first source-motivated relative covariance subtraction for
the failed Cameron--Martin prime vector:

- the prime side fixes the logarithmic coordinate and harmonic-prime
  divergence;
- the gamma side fixes the oscillator spectrum and quarter shift;
- their natural cutoff relation cancels the leading positive divergence;
- no Xi zeros enter the prescription.

It also makes the regulator scale falsifiable. Replacing `K(P)` by
`floor(c log P)` preserves the divergence cancellation but shifts the finite
part by `-log c`. A successful source construction must fix `c=1` through the
shared Mellin/logarithmic coordinate, not choose it to match Xi.

## Why this is relative, not positive

Equation (5) is a difference of two positive divergent traces. It is not the
variance of a positive Gaussian probability measure. The natural analytic
object is a relative determinant or a Krein/Gaussian partition-function
ratio in which the gamma reference cancels the prime self-contraction.
Positivity, if it emerges, must do so only after the completed relative
quotient, consistently with the earlier Krein graph architecture.

The cancellation controls the Hermitian magnitude divergence. It does not by
itself retain the bilinear phase `sum_p p^(-1-2iT)`, construct the linear
channel `C_1`, or identify a determinant with Xi. Those require off-diagonal
prime--gamma coupling before scalarization.

## Falsifiers

A relative Gaussian proposal fails if:

1. its prime and oscillator cutoffs are unrelated;
2. their covariance traces do not have equal `log log P` coefficients;
3. it chooses the scale `c` after comparing with Xi;
4. it calls the signed difference (5) a positive covariance;
5. it cancels the magnitude divergence but discards all `T`-dependent
   bilinear or off-diagonal information.

## Next target

Construct the finite-cutoff relative determinant for the prime incidence
operator against the even oscillator reference under `K=floor(log P)`, and
derive its finite constant and `T`-dependent quadratic phase from one block
operator. Equation (5) is only the necessary diagonal counterterm theorem.
