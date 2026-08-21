# First finite coupled Li positivity theorem: degree two

## Exact channel decomposition

Put

`c_0=lambda_1`,

`c_1=(lambda_2-2lambda_1)/2`,

`c_2=(lambda_3-2lambda_2+lambda_1)/2`.

The degree-two energy for `p(z)=a+bz+cz^2` has Toeplitz matrix

`T_3=[[c_0,c_1,c_2],[c_1,c_0,c_1],[c_2,c_1,c_0]]`.

Reflection separates the antisymmetric endpoint vector `(1,0,-1)` from the
endpoint-symmetric plane. In the normalized basis consisting of the
antisymmetric endpoint, symmetric endpoint, and center channels, `T_3` is

```
[ c_0-c_2       0             0      ]
[    0        c_0+c_2      sqrt(2)c_1 ]
[    0        sqrt(2)c_1      c_0     ]
```

Consequently degree-two positivity is equivalent to positivity of these two
channels. Written in Li coefficients, the genuinely new inequalities are

`A_2=(lambda_1+2lambda_2-lambda_3)/2 >= 0`,

and

`D_2=(lambda_1 lambda_3+2lambda_1 lambda_2-lambda_1^2-lambda_2^2)/2 >= 0`,

together with the required diagonal conditions. The full determinant is
exactly `A_2 D_2`.

## Interpretation

`A_2` is the reflection-odd channel. `D_2` is the first irreducibly coupled
channel: it measures whether the symmetric endpoint mode and the center mode
can coexist in one positive Gram system. Proving the three individual Li
coefficients positive does not imply either inequality.

The previous high-precision reconnaissance values give positive values in
both channels, but those decimal evaluations are not certified. The algebraic
factorization itself is exact and is verified by the symbolic checker.

## Arithmetic attack

The next step is to substitute the completed-zeta decomposition of
`lambda_1,lambda_2,lambda_3` into `A_2` and `D_2`, retaining endpoint,
archimedean, and prime-power components. The determinant `D_2` necessarily
contains cross-products between these components. Those cross-products are
not artifacts: they are the first explicit location where coupled completion
can repair the indefinite isolated-prime sector.

A satisfactory identity must explain the sign of `D_2` through a rule that
extends to higher Toeplitz ranks. Merely inserting numerical values or taking
a Cholesky factor of this one matrix does not count.

## Completed-zeta jet reduction

Write

`log xi(1+t)=constant+a_1 t+a_2 t^2+a_3 t^3+...`.

Then the two channels reduce exactly to

`A_2=(2a_1-2a_2-3a_3)/2`,

`D_2=(2a_1^2+2a_1a_2+3a_1a_3-4a_2^2)/2`.

The coefficients `a_1,a_2,a_3` have closed forms using only the Euler
constant, the first two nontrivial Stieltjes constants, `pi`, `zeta(3)`, and
logarithms. Thus degree-two certification needs no numerical differentiation
and no zero enumeration. The exact derivation is checked by
`checkers/li_degree_two_stieltjes_reduction.py`.

## Geometric meaning

For any finite positive symmetric circle measure with moments `c_k`, the two
channels are

`A_2=2 integral sin(theta)^2 dmu`,

`D_2=2 mu(T)^2 Var_(mu/mu(T))(cos(theta))`.

Thus `D_2` is literally a spectral variance. See
`li-degree-two-variance-theorem.md` for equality cases and the source-side
boundary of this interpretation.
