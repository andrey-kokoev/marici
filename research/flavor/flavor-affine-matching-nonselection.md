# Affine matching nonselection: WP702

## Free boundary packet

Let the two radial quartics at the low scale be obtained from independently
free UV boundaries and finite source-derived corrections:

\[
\begin{pmatrix}
\lambda\\p
\end{pmatrix}_{\mathrm{low}}
=
\begin{pmatrix}
\lambda\\p
\end{pmatrix}_{\mathrm{UV}}
+
\begin{pmatrix}
\Delta_\lambda\\\Delta_p
\end{pmatrix}.
\]

The Jacobian with respect to the UV boundary packet is the identity. Every
low-energy target has the exact preimage

\[
\lambda_{\mathrm{UV}}=\lambda_* -\Delta_\lambda,
\qquad
p_{\mathrm{UV}}=p_* -\Delta_p.
\]

Consequently the matching operation reaches points inside the WP700 corridor,
stable points outside it, and the exact zero-portal stratum.

## Positive threshold is not selection

Even if \(\Delta_p>0\), the allowed boundary value

\[
p_{\mathrm{UV}}=-\Delta_p
\]

gives \(p_{\mathrm{low}}=0\). Source-generated radiative support therefore
rigidifies the operator grammar but does not select a nonzero portal value or
the high-contrast coupling corridor.

## Decisive disposition

On the currently admitted free-boundary domain, finite threshold matching is
an affine bijection, not a proper-subspace selector. Selection would require a
new noninvertible source boundary condition, a fixed point with an independently
admitted basin, a positivity domain excluding the cancellation preimage, or an
equivalent UV constructor that actually removes boundary freedom.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp702_affine_matching_nonselection.py

Generated result: results/wp702_affine_matching_nonselection.json.
