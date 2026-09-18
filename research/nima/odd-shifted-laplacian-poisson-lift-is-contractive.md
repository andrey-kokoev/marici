# Odd shifted-Laplacian Poisson lift is contractive

On the interval `[-L,L]`, consider

$$
P=\partial_x^2-\frac14.
$$

The harmonic odd function with normalized endpoint values

$$
d_L(L)=\frac1{\sqrt2},
\qquad
d_L(-L)=-\frac1{\sqrt2}
$$

is

$$
d_L(x)
=\frac1{\sqrt2}
\frac{\sinh(x/2)}{\sinh(L/2)}.
$$

It satisfies

$$
Pd_L=0.
$$

In the completion graph norm

$$
\|f\|_{G_P}^2=\|f\|_{L^2}^2+\|Pf\|_{L^2}^2,
$$

its energy is therefore

$$
\|d_L\|_{G_P}^2
=\frac{\sinh L-L}{2\sinh^2(L/2)}.
$$

Using

$$
2\sinh^2(L/2)=\cosh L-1,
$$

the contractive inequality `||d_L||^2<=1` is equivalent to

$$
\sinh L-L\le\cosh L-1,
$$

or

$$
1-L-e^{-L}\le0.
$$

This follows from the elementary convexity bound

$$
e^{-L}\ge1-L.
$$

For every `L>0` the inequality is strict. As `L->infinity`, the norm tends to one, so there is no uniform strict margin over unbounded interval lengths.

Thus the normalized odd endpoint vector lies in the shifted-Laplacian energy range and has a contractive Poisson/Douglas lift at every finite interval. This proves the finite rank-one Schur inequality in the normalized local endpoint model.

Successor naturality and the infinite-length limit still require the declared interval resegmentation maps; the pointwise family `d_L` must not be assumed compatible merely from its formula.

Status: finite-interval odd endpoint leverage bound proved exactly; uniform strictness and successor coherence remain open.
