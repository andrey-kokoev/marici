# Acyclic endpoint reduction leaves a small positive completed coupling

Let

```
L(s)=xi'(s)/xi(s)
=1/s+1/(s-1)-(1/2)log(pi)
 +(1/2)psi(s/2)+zeta'(s)/zeta(s).                     (1)
```

The squared resolvent is

```
S(x)=L(1/2+sqrt(x))/(2sqrt(x)).                        (2)
```

At `x=1/4`, choose the branch `s->1`. With `epsilon=s-1`,

```
zeta'(s)/zeta(s)=-1/epsilon+EulerGamma+O(epsilon),     (3)
psi(1/2)=-EulerGamma-2log 2.                           (4)
```

After cancellation of `1/(s-1)` against (3), equation (1) gives

```
L(1)=1+EulerGamma/2-log(2sqrt(pi)).                    (5)
```

Since `2sqrt(x)=1` there,

```
S(1/4)=1+EulerGamma/2-log(2sqrt(pi))
      approximately 0.0230957 >0.                     (6)
```

Functional reflection gives `L(1-s)=-L(s)`. On the `s->0` branch both the
numerator and denominator in (2) change sign, so the same squared-coordinate
value is obtained after the reflected elementary--gamma pole cancellation.

## Meaning

The acyclic cone removes only the pole state. Its finite completed coupling is
fixed by the Euler constant and the archimedean normalization; there is no
counterterm freedom. The small positive remainder measures cancellation among
order-one pieces:

- elementary plus zeta finite part: `1+EulerGamma`;
- gamma finite part: `-EulerGamma/2-log 2`;
- pi normalization: `-(1/2)log pi`.

Their sum is positive by a margin of only about `2.3e-2`. This is a scalar
boundary value, not yet a reflection-positive Gram theorem. It provides an
exact normalization checkpoint that every reduced source operator and
one-time moment construction must reproduce.

## Conditional spectral reading

Under the Stieltjes/RH representation,

```
S(1/4)=sum_(gamma>0)m_gamma/(gamma^2+1/4).             (7)
```

Equation (6) derives the same number from completed source constants without
using zero locations. The equality (7) is conditional on the positive
spectral interpretation; the positivity of the explicit constant itself is
unconditional.
