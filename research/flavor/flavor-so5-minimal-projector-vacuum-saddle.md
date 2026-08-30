# SO(5) minimal projector vacuum saddle: WP740

## Question

Can one renormalizable (SO(5)) breaking field fix WP739's rank-one singlet
projector without introducing an adjustable orientation?

## Minimal projector field

Let (Phi) be a real symmetric traceless (5\times5) matrix, the (14) of
(SO(5)), with the (Z_2)-even renormalizable potential

\[
V(\Phi)=-\frac{m^2}{2}\operatorname{tr}\Phi^2
+\frac{\lambda_1}{4}(\operatorname{tr}\Phi^2)^2
+\frac{\lambda_2}{4}\operatorname{tr}\Phi^4.
\]

A vacuum with eigenvalue multiplicities (3+1+1) would break (SO(5)) to
the desired physical (SO(3)), while distinct last two eigenvalues would fix
the two singlet projectors.

The traceless stationarity equation is

\[
-m^2\Phi+\lambda_1\operatorname{tr}(\Phi^2)\Phi
+\lambda_2\left(\Phi^3-\frac15\operatorname{tr}(\Phi^3)I_5\right)=0.
\]

For three distinct eigenvalues (a,b,c), the (Z_2)-even equation has no
quadratic term, so its three roots obey (a+b+c=0). Tracelessness with
multiplicities (3+1+1) gives (3a+b+c=0). Hence

\[
a=0,\qquad c=-b.
\]

Up to scale and gauge rotation, the only candidate projector vacuum is

\[
\Phi_*=\operatorname{diag}(0,0,0,v,-v),
\qquad
m^2=(2\lambda_1+\lambda_2)v^2.
\]

This is exactly the desired hard-to-vary projector pattern: it distinguishes
the two singlets by opposite eigenvalues and contains no continuous mixing
angle.

## Exact Hessian obstruction

For a symmetric traceless fluctuation (H), the quadratic Hessian form at
(Phi_*) is

\[
\begin{aligned}
Q(H)={}&-\lambda_2v^2\operatorname{tr}H^2
+2\lambda_1(\operatorname{tr}\Phi_*H)^2\\
&+2\lambda_2\operatorname{tr}(\Phi_*^2H^2)
+\lambda_2\operatorname{tr}(\Phi_*H\Phi_*H).
\end{aligned}
\]

The symmetric-traceless fluctuations supported inside the upper (3\times3)
block have coefficient (-\lambda_2v^2). Their stability requires

\[
\lambda_2<0.
\]

The remaining two diagonal (SO(3))-singlet fluctuations can be written as

\[
H=\operatorname{diag}(x,x,x,y,-3x-y).
\]

Their Hessian matrix, after removing the common positive (v^2), is

\[
M=\begin{pmatrix}
18\lambda_1+15\lambda_2&12\lambda_1+6\lambda_2\\
12\lambda_1+6\lambda_2&8\lambda_1+4\lambda_2
\end{pmatrix},
\]

with determinant

\[
\det M=24\lambda_2(2\lambda_1+\lambda_2).
\]

Existence with (m^2>0) and (v^2>0) requires
(2\lambda_1+\lambda_2>0). Combined with (lambda_2<0), the determinant is
strictly negative. Hence the singlet Hessian has one negative eigenvalue. If
(lambda_2>0) instead, the upper-block shape modes are negative. At
(lambda_2=0), flat directions remain.

Therefore the projector pattern is never a strict local minimum of the
minimal (Z_2)-even renormalizable potential.

## Disposition

The (14) supplies the correct representation and an algebraically unique
projector pattern, but it cannot dynamically select that pattern in the
minimal potential. Adding the allowed cubic invariant
(operatorname{tr}\Phi^3) or higher operators may stabilize a (3+1+1)
vacuum, but then its coefficient and the resulting eigenvalue ratios become
new source data unless fixed by a stronger principle. The cubic must be
derived rather than fitted to stabilize the desired answer.

This closes the minimal simple-group projector repair before gauge fixed-point,
threshold, and detector calculations. The smallest exact falsifier is the
negative determinant above under the conditions required to stabilize the
triplet-shape modes and set a nonzero vacuum.

Reproduce with:
`uv run --with sympy python research/flavor/checkers/wp740_so5_minimal_projector_vacuum_saddle.py`.

Generated result:
`results/wp740_so5_minimal_projector_vacuum_saddle.json`.
