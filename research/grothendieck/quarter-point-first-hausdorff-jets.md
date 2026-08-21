# The first quarter-point Hausdorff jets are positive after extreme cancellation

Put `epsilon=s-1` and

```
h=x-1/4=s(s-1)=epsilon+epsilon^2.                      (1)
```

Expand the completed logarithmic derivative after pole cancellation:

```
L(1+epsilon)=l_0+l_1 epsilon+l_2 epsilon^2+O(epsilon^3). (2)
```

Using the standard Stieltjes-constant convention

```
zeta(1+epsilon)=1/epsilon+gamma_0-gamma_1 epsilon
 +gamma_2 epsilon^2/2+O(epsilon^3),                    (3)
```

and the half-argument polygamma values gives

```
l_0=1+gamma_0/2-log(2sqrt(pi)),                        (4)

l_1=-1-2gamma_1-gamma_0^2+pi^2/8,                    (5)

l_2=1+gamma_0^3+3gamma_0gamma_1+(3/2)gamma_2
       -(7/8)zeta(3).                                  (6)
```

Since

```
S(x)=L(1+epsilon)/(1+2epsilon),
epsilon=h-h^2+O(h^3),                                  (7)
```

the first compact moments
`A_k=(-1)^kS^(k)(1/4)/k!` are

```
A_0=l_0,                                               (8)
A_1=2l_0-l_1,                                         (9)
A_2=l_2-3l_1+6l_0.                                   (10)
```

Numerically,

```
A_0 approximately 2.3095708966e-2,
A_1 approximately 3.7100636437e-5,
A_2 approximately 1.4367786028e-7.                    (11)
```

The first ordinary coupled determinant is

```
Delta_1=A_0A_2-A_1^2
       approximately 1.9418848217e-9 >0.              (12)
```

The first upper-support diagonal is also positive:

```
4A_0-A_1 approximately 9.2345735228e-2.               (13)
```

## Interpretation

These are unconditional completed constants derived at `s=1`; no zero
locations enter their formulas. Under RH they become

```
A_k=sum_(gamma>0)m_gamma/(gamma^2+1/4)^(k+1).         (14)
```

The observed positivity verifies only the first tiny corner of the compact
Hausdorff hierarchy. The determinant margin is nine decimal orders below
unity, demonstrating that coarse sectorwise estimates are structurally
unlikely to prove even the first coupled inequality.

## Verification boundary

Equations (4)--(10) are exact symbolic identities. The displayed signs use
standard high-precision decimal values of `gamma_0,gamma_1,gamma_2,zeta(3)`.
The checker is a numerical regression, not an interval certificate. A formal
record should insert rigorous enclosures for those four constants; the margins
are ample relative to modern enclosures but especially small for (12).

The next algebraic step is `A_3`, requiring `gamma_3`, `pi^4`, and the next
polygamma value, followed by the first lower- and upper-localizer `2x2`
determinants.
