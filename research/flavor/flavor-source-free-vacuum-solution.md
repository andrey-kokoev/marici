# Source-free two-adjoint vacuum solution (WP438)

## Frozen dependency

WP438 imports WP437 unchanged and solves its preregistered potential. No
invariant, coefficient, source, or acceptance condition is added after the
freeze.

## Global minimization

Write

$$
R=\lVert A\rVert_F^2+\lVert D\rVert_F^2,
\qquad
c=rho-\frac{lambda}{2}>0.
$$

The commutator bound gives

$$
V_{437}\geq-\frac{m^2}{2}R+cR^2.
$$

Equality requires both the Bottcher-Wenzel and equal-norm bounds to saturate.
It is attained by a Pauli pair embedded in a two-dimensional subspace:

$$
A=a\begin{pmatrix}1&0&0\\0&-1&0\\0&0&0\end{pmatrix},
\qquad
D=a\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix}.
$$

For this pair,

$$
R=4a^2,
\qquad
\lVert[A,D]\rVert_F^2=8a^4=\frac12R^2.
$$

The exact radial minimum is

$$
R_*=\frac{m^2}{4c},
\qquad
a^2=\frac{m^2}{16c},
\qquad
V_{min}=-\frac{m^4}{16c}.
$$

This is a nonzero noncommuting global minimum for the full open WP437
coefficient domain.

## Stability and residual gauge group

At the exact benchmark (m^2=lambda=rho=1), the complete Hessian on the sixteen
real adjoint components has spectrum

$$
0^{(7)},\qquad3^{(4)},\qquad4^{(3)},\qquad6^{(2)}.
$$

There are no negative modes. The seven zero modes are precisely the gauge orbit
of the breaking pattern

$$
SU(3)_F\longrightarrow U(1).
$$

The unbroken generator is proportional to

$$
\operatorname{diag}(1,1,-2),
$$

which commutes with both embedded Pauli adjoints. Consequently the gauge-boson
mass Gram has rank seven, not the preregistered rank eight.

## Preregistered disposition

WP437 acceptance results:

- nonzero global minimum: pass;
- stable Hessian modulo gauge zero modes: pass;
- noncommuting adjoints: pass;
- gauge-mass rank eight: fail, exact rank seven;
- open coefficient domain: pass;
- no measured flavor coordinate: pass.

The minimal symmetric source-free potential therefore generates a healthy
dynamical flavon vacuum, but only an (SU(2))-embedded breaking pattern. It
does not reproduce WP433's generic full-rank shape.

The smallest exact falsifier is the frozen rank-eight acceptance condition
itself: the commuting generator above is a nonzero kernel vector. Repair
requires a preregistered invariant that breaks the residual (U(1)). Cubic or
mixed trace invariants are possible, but they relax WP437's sign symmetry and
must be justified independently rather than chosen to fit flavor.

The absolute scale remains

$$
g_Ff\mathrel{\propto}\frac{g_Fm}{\sqrt c},
$$

so this vacuum result does not select (g_Ff/v).

Run `uv run --with sympy python
research/flavor/checkers/wp438_source_free_vacuum_solution.py` to regenerate the
JSON result.
