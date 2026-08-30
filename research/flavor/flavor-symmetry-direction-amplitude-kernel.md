# Symmetry direction-amplitude kernel (WP302)

## Symmetric selector architecture

Apply the coordinate swap symmetry to the WP301 quadratic selector. The most
general symmetric two-coordinate Hessian and invariant linear source are

\[
A=\begin{pmatrix}a&c\\c&a\end{pmatrix},
\qquad
b=\beta\begin{pmatrix}1\\1\end{pmatrix}.
\]

For $a>c\geq0$, the action is strictly convex. Its selected point is

\[
x_*=\frac{\beta}{a+c}\begin{pmatrix}1\\1\end{pmatrix}.
\]

The symmetry forces the direction and the ratio $x_1/x_2=1$. It does not fix
the amplitude $\beta/(a+c)$.

## Exact hostile pair

With the same symmetric Hessian $a=2,c=1$, choosing $\beta=3$ selects
$(1,1)$, while $\beta=6$ selects $(2,2)$. Both sources obey the same
symmetry and selector architecture.

If symmetry forbids the linear source entirely, the convex quadratic selects
only the origin. A nonzero physical point then needs symmetry breaking or an
independently normalized constraint. Either route introduces new numerical
source data.

## Classification

Swap symmetry is a presentation and direction rigidifier. It becomes part of a
numerical selector only after the invariant source amplitude and Hessian scale
are independently derived. A fixed-norm condition does not remove this gate;
it relocates the free number into the norm.

Run `uv run --with sympy python
research/flavor/checkers/wp302_symmetry_direction_amplitude_kernel.py` to
regenerate the exact symmetry audit.
