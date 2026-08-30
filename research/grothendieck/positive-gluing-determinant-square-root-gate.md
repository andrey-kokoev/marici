# A positive gluing determinant models a square, not the signed Xi function

On the critical line, the Krein graph construction produces

```
D(T)=det[I-C(T)*C(T)] >=0                              (1)
```

whenever the completed graph is nonnegative. Since `D(T)` is real analytic,
every isolated zero has even order. A nonnegative analytic function cannot
cross transversely through zero.

Therefore a positive graph Gram determinant cannot directly equal the signed
critical-line function

```
Xi(T)=xi(1/2+iT),                                     (2)
```

unless every zero has even multiplicity. The architecture must instead be
interpreted as a squared object, naturally

```
D(T) proportional to Xi(T)^2=|Xi(T)|^2.               (3)
```

The functional equation makes `xi(s)xi(1-s)=xi(s)^2`, so a paired
reflection determinant is expected to lose orientation and square the
underlying determinant-line section.

## Singular-value contact order

If one singular value satisfies `sigma(T)<=1` and reaches one at an interior
point `T_0`, then `T_0` is a local maximum of `sigma`. For a smooth generic
contact,

```
1-sigma(T)^2 = c(T-T_0)^2+... ,       c>0.             (4)
```

so the positive determinant has a double zero even when the underlying Xi
zero should be simple. Nullity records geometric multiplicity, while the
positive Gram determinant doubles the oriented analytic multiplicity.

## Pfaffian/determinant-line repair

For a real skew-symmetric family `A(T)`,

```
det A(T)=Pf(A(T))^2.                                   (5)
```

The Pfaffian is an oriented square root: it can change sign and have simple
zeros. The smallest model is

```
A(T)=[ 0  T]
     [-T  0],
Pf(A)=T,
det A=T^2.                                             (6)
```

Thus a viable Xi construction likely needs two levels:

1. a positive Hermitian/Krein graph determinant controlling `xi^2` and RH;
2. a canonical orientation, Pfaffian, or determinant-line section recovering
   `xi` itself and its true multiplicities.

The metaplectic phase and Maslov orientation found in the archimedean lane
are plausible data for this square-root choice.

## Falsifier

A proposal fails if it equates an everywhere nonnegative critical-line Gram
determinant directly with `Xi(T)` while also claiming generic simple zeros.
It must state whether it represents `xi`, `xi^2`, or an absolute square, and
explain the orientation needed to pass between them.

