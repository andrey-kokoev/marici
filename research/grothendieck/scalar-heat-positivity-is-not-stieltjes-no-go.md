# Scalar heat positivity is weaker than the Stieltjes/RH gate

Let

```
S(x)=integral_0^infinity e^(-xt) Theta(t) dt.           (1)
```

If `Theta(t)>=0`, then `S` is completely monotone as a function of `x`, and
the primitive `B` with `B'=S` is a Bernstein function. This does **not** imply
that `S` is Stieltjes or that `B` is complete Bernstein.

The missing condition is complete monotonicity of the heat kernel itself:

```
(-1)^k partial_t^k Theta(t)>=0       for all k>=0.     (2)
```

By Bernstein's theorem, (2) is equivalent to

```
Theta(t)=integral_[0,infinity) e^(-lambda t)dmu(lambda) (3)
```

for a positive measure. Then (1) becomes the Stieltjes transform
`S(x)=integral dmu(lambda)/(x+lambda)`.

## Explicit positive counterexample

For `0<epsilon<1`, set

```
Theta_(epsilon,b)(t)=e^(-t)[1+epsilon cos(bt)]>0.       (4)
```

Its Laplace transform is

```
S(x)=1/(x+1)
 +epsilon(x+1)/[(x+1)^2+b^2].                         (5)
```

Equation (5) has poles at `x=-1+/-ib`; it is not Stieltjes when `b!=0`.
For suitable `epsilon,b`, even the first derivative sign in (2) fails. Thus a
positive scalar heat kernel can hide an oscillatory off-axis spectral pair.

## Corrected hierarchy of gates

The implications are

```
Theta>=0
 => S completely monotone in x and B Bernstein,

Theta completely monotone in t
 <=> S Stieltjes
 => squared poles lie on the negative real axis.       (6)
```

With the completed Xi meromorphy, normalization, and positive integer
residues, the second line is the RH-equivalent scalar gate. Pointwise
nonnegativity alone is only an order-zero necessary condition.

The full all-character Gaussian condition remains different: positivity of
every Gaussian convolution in `(sigma,xi)`, followed through the approximate
identity, makes the entire Weil spectral distribution positive and is
RH-equivalent. Its equivalence does not rely on the erroneous scalar
implication.

## Research consequence

The scalar source program must control the derivative hierarchy
`(-1)^k partial_t^k Theta`, or an equivalent Stieltjes/Pick representation,
not merely the sign of `Theta`. The negative-mass and first-contact program is
still valid for the stronger all-character Weil kernel, but a clean zero slice
cannot certify RH by itself.
