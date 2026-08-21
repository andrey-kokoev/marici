# The completed log derivative has an RH-equivalent coupled Herglotz kernel

Write the centered completed function and its logarithmic derivative as

```
Xi(z)=xi(1/2+z),
F(z)=Xi'(z)/Xi(z).                                     (1)
```

The functional equation makes `Xi` even. Consider the right half-plane
`Re(z)>0` and define

```
H_Xi(z,w)
 =[F(z)+conj(F(w))]/[z+conj(w)].                       (2)
```

## Boundary-zero decomposition under RH

If RH holds, the zeros of `Xi` are `i gamma` on the imaginary boundary. In
the symmetric canonical-product interpretation,

```
F(z)=sum_gamma m_gamma/(z-i gamma),                    (3)
```

with conjugate/symmetric regularization. For each boundary zero,

```
[1/(z-i gamma)+1/(conj(w)+i gamma)]/[z+conj(w)]
 =1/[(z-i gamma)(conj(w)+i gamma)].                    (4)
```

Therefore

```
H_Xi(z,w)
 =sum_gamma m_gamma
   [1/(z-i gamma)] conj[1/(w-i gamma)],                (5)
```

a positive Cauchy-feature Gram kernel.

## Converse

If `F` is holomorphic on `Re(z)>0` and the kernel (2) is positive definite,
then its diagonal gives

```
Re F(z)>=0.                                            (6)
```

Holomorphy already excludes Xi zeros in the open right half-plane. Evenness
then excludes zeros in the left half-plane. All nontrivial zeros lie on the
imaginary boundary, which is RH.

Thus, with the standard canonical-product and boundary conventions,

```
RH iff H_Xi is a positive kernel on Re(z)>0.            (7)
```

This is the two-point strengthening of the earlier positive-real
Caratheodory target.

## Source-side form

Since `F=xi'/xi`, it splits into endpoint, gamma, and prime terms after
transport to their valid domains. Substitution into (2) gives a corresponding
sum of two-point kernels. The research problem is to prove positivity only
after the completed pieces are coupled; the Euler-local no-go forbids
expecting every prime contribution to be positive separately.

The desired coefficient--Betti correspondence should realize (5) without
assuming the zero ordinates are real. Equivalently, it should produce (2)
from the source side as a Gram kernel.

## Falsifiers

1. Any off-line zero in `Re(z)>0` creates a pole of `F` inside the kernel
   domain, immediately violating the Schur/Herglotz realization.
2. A finite set of sample points yielding a negative Gram minor falsifies
   positivity.
3. A source decomposition that drops endpoint or gamma completion is not a
   proof of (7).

Equation (7) is an equivalence, not a proof. Its value is that the abstract
transfer-kernel target is now tied to a canonical Xi function.

