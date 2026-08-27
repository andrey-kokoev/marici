# Radial portal vacuum: WP685

## Declared candidate model

To test existence without pretending to complete the full scalar grammar,
restrict to the Higgs radius (h) and exit-flavon radius (x):

\[
V=-\frac{\mu_h^2h^2}{2}-\frac{\mu_x^2x^2}{2}
+\frac{\lambda_hh^4}{4}+\frac{\lambda_xx^4}{4}
+\frac{\lambda_ph^2x^2}{2}.
\]

This is an explicitly declared radial truncation. It excludes all
orientation-dependent adjoint and port-vector invariants.

## Stable mixed vacuum

On the nonzero branch,

\[
\begin{pmatrix}h^2\\x^2\end{pmatrix}
=\frac{1}{\lambda_h\lambda_x-\lambda_p^2}
\begin{pmatrix}
\lambda_x\mu_h^2-\lambda_p\mu_x^2\\
\lambda_h\mu_x^2-\lambda_p\mu_h^2
\end{pmatrix}.
\]

The radial Hessian is

\[
2\begin{pmatrix}
\lambda_hh^2&\lambda_phx\\
\lambda_phx&\lambda_xx^2
\end{pmatrix},
\]

with determinant

\[
4h^2x^2(\lambda_h\lambda_x-\lambda_p^2).
\]

The exact witness

\[
(\lambda_h,\lambda_x,\lambda_p,\mu_h^2,\mu_x^2)=(2,3,1,3,4)
\]

gives (h^2=x^2=1) and a positive radial determinant of twenty. A stable
nonzero mixing domain therefore exists.

## Nonselection

The mixing entry is (2\lambda_phx). The same source grammar permits
(\lambda_p=0), where two independent stable vacua can remain while the
coherent reference vanishes exactly. Existence does not select nonzero portal
support.

This packet is neither a complete scalar potential nor a numerical selector.
Orientation-dependent invariants, RG closure, thresholds, and a principle
excluding the zero-portal stratum remain open.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp685_radial_portal_vacuum.py

Generated result: results/wp685_radial_portal_vacuum.json.
