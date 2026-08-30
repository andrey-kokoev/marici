# UV-limit trajectory kernel (WP270)

## Hostile trajectories

Fix the complete affine beta function

\[
\frac{dc}{dt}=-c+1.
\]

Its finite trajectories are

\[
c_A(t)=1+Ae^{-t}.
\]

Every finite amplitude \(A\) has the same UV limit \(c_*=1\). In particular,

\[
c_0(t)=1,
\qquad
c_1(t)=1+e^{-t}
\]

solve the same beta function and converge to the same attractive fixed point.
At the finite matching scale \(t=0\), however, they give coefficients one and
two. With the same unit linear mixing term, they select \(x=1/2\) and
\(x=1/4\).

## First nonfaithful arrow

The UV-limit projection forgets the trajectory amplitude. Fixed-point
attractiveness erases differences forward toward the UV but does not reconstruct
which finite trajectory supplies the low-energy matching coefficient. This is
an exact source-coordinate kernel, not a detector imperfection.

At finite resolution \(1/100\), the two trajectories already differ by only
\(1/100\) at \(t=\log100\), although their matching-scale difference is one.
An increasingly precise UV-limit observation still does not determine the
finite integration constant without a trajectory law.

## Corrected selector classification

WP269 supplies a genuine asymptotic boundary-class selector conditional on its
beta coefficients. It is not yet a finite-scale `physical16` selector. The
remaining constructor must fix the trajectory amplitude through a renormalized
boundary condition, finite threshold match, or a UV critical surface with no
free trajectory directions.

Run `uv run --with sympy python
research/flavor/checkers/wp270_uv_limit_trajectory_kernel.py` for the exact
flow residuals, common limit, finite-scale hostile pair, and resolution
witness.
