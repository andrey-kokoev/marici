# Continuous CP-odd carrier (WP387)

## Bounded question

Can WP386's binary branch carrier arise as the vacuum sector of a healthy
continuous source field while preserving the same physical16 shell?

## Source potential

Introduce a real CP-odd carrier $q$ and positive coefficients $a,\lambda$:

\[
V(C,D,q)=a(C-\beta Dq)^2+\lambda(q^2-1)^2.
\]

Under the simultaneous CP action $(C,q)\mapsto(-C,-q)$, the potential is
exactly invariant. It has two zero-energy stationary points,

\[
(C,q)=(\beta D,1),\qquad (C,q)=(-\beta D,-1).
\]

Their projection onto flavor space is precisely the two-branch WP378 shell.

## Exact stability

At either vacuum the Hessian in $(C,q)$ has determinant

\[
\det H=16a\lambda>0,
\]

with positive leading minor and trace. Both vacua are strict local minima.
Thus the continuous carrier supplies a healthy classical realization of the
binary branch structure rather than an indefinite multiplier.

Choosing $q=C/(\beta D)$ can cancel the portal away from a carrier vacuum,
but the double-well term becomes

\[
\lambda\frac{(C^2-\beta^2D^2)^2}{\beta^4D^4},
\]

which vanishes only on the intended shell. The enlarged potential therefore
does not acquire a continuous zero-energy escape direction.

## Remaining source insertion

The construction derives the binary carrier from a continuous double well,
but it does not derive the flavor interface. The term $C-\beta Dq$ already
contains the desired relative normalization and shell geometry. Since $C$
and $D$ have bifundamental field degree 12, the highest term $D^2q^2$ has
field degree 26 and the mixed term $CDq$ has degree 25. The completion remains
a high-degree EFT source rather than a renormalizable microscopic model.

Selecting one vacuum prepares a CP orientation and changes the operational
groupoid to the stabilizer of that preparation. Summing both vacua restores
the unlabelled CP quotient. Domain walls, tunnelling, finite temperature, and
detector coupling to $q$ remain physical preparation questions.

## Disposition

WP387 repairs one WP386 gate: the binary carrier can be realized by a healthy
continuous CP-symmetric source with stable branch vacua. It remains a
conditional selector because $\beta$ and the degree-25/26 flavor interface
are inserted rather than derived.

The smallest exact falsifier is the attempted portal-cancelling trajectory
$q=C/(\beta D)$, on which the double-well residual remains nonzero off shell.
The next gate is a lower-degree microscopic source that derives the mixed
interface and its normalization.

Run `uv run --with sympy python
research/flavor/checkers/wp387_continuous_cp_carrier.py` to regenerate the
result.
