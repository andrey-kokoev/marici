# Universal ratio profile has zero mass and first moment minus two

Let

$$
\kappa(r)
=\frac32
\frac{r^2(-6+23r^2-6r^4)}{(1+r^2)^{9/2}}.
$$

Using

$$
\int_0^\infty
\frac{r^m}{(1+r^2)^{9/2}}\,dr
=rac12
B\left(\frac{m+1}{2},\frac{8-m}{2}\right),
$$

direct evaluation gives

$$
\int_0^\infty\kappa(r)\,dr=0.
$$

Indeed, the three beta integrals are

$$
\frac8{105},\qquad\frac2{35},\qquad\frac17,
$$

and

$$
\frac32\left(
-6\frac8{105}
+23\frac2{35}
-6\frac17
\right)=0.
$$

The next moment is

$$
\int_0^\infty r\kappa(r)\,dr=-2.
$$

Thus continuum summation over the ratio variable has no leading mass term. The apparent `O(1)` contribution per large denominator cancels only after retaining the complete sign-changing profile. Termwise positive or negative estimates destroy this cancellation.

The nonzero first moment shows that the next Euler–Maclaurin or lattice-boundary correction survives. It is a natural candidate for the endpoint/seam current accompanying common-scale renormalization.

This moment cancellation explains why raywise absolute estimates are too crude while a Poisson/Euler–Maclaurin resummation may still yield a completed distribution.

Status: leading ratio-mass divergence cancelled exactly; first boundary moment computed as `-2`; arithmetic lattice-error control remains open.
