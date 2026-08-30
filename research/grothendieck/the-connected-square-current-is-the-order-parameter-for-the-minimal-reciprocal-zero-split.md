# The connected square current is the order parameter for the minimal reciprocal zero split

## Positive reciprocal three-cell family

Let

\[
\nu_{A,B}=B\delta_{-1}+A\delta_0+B\delta_1,
\qquad A,B>0,
\]

and put `c=A/B`. With `r=exp(z)`, its bilateral Laplace transform vanishes
exactly when

\[
r^2+cr+1=0.
\]

The roots are reciprocal. Their location has three regimes:

- `c<2`: a conjugate pair on the unit circle;
- `c=2`: a double seam root `r=-1`;
- `c>2`: two distinct negative reciprocal roots, one inside and one outside
  the unit circle.

The last regime is precisely an off-seam reciprocal zero pair in the
logarithmic coordinate `z`.

## Connected square coefficient

In the right chart, factor

\[
r^2+cr+1=(r+\alpha)(r+\alpha^{-1}),
\qquad
\alpha+\alpha^{-1}=c.
\]

After removing the invertible leading monomial, the connected logarithm has
coefficients

\[
a_k=\frac{(-1)^{k+1}}{k}
(\alpha^k+\alpha^{-k}).
\]

At grade two,

\[
a_2
=-\frac12(\alpha^2+\alpha^{-2})
=1-\frac{c^2}{2}.
\]

Consequently

\[
c^2-4=-2(a_2+1).
\]

The square current therefore gives the exact bifurcation trichotomy:

```text
a_2 > -1   reciprocal zeros remain on the seam
a_2 = -1   double seam collision
a_2 < -1   reciprocal pair splits off the seam
```

## Meaning

In the smallest positive reciprocal source, the grade-two connected current
is not merely an auxiliary provenance label. Relative to the canonical seam
value `-1`, it is exactly the discriminant of the zero-pair split.

This supplies a finite model of the proposed geometry:

```text
two reciprocal sectors
-> collision at the common unitary seam
-> square-current threshold
-> symmetric off-seam unfolding
```

It also explains why a primitive-only description misses the transition:
`a_1=c` remains positive in all three regimes. The distinction first appears
at the second connected grade.

## Scope

This theorem concerns the minimal three-cell reciprocal family. It does not
show that the global theta prime-square current controls the Riemann divisor;
that requires a source-derived comparison map from the pro-valued arithmetic
square current to the completed zero-state boundary condition. The theorem
identifies the exact finite local model that such a comparison must extend.

## Durable verification

- Checker: `checkers/check_square_current_reciprocal_zero_split.py`
- The checker verifies all three regimes with exact rational witnesses and
  the discriminant identity.
