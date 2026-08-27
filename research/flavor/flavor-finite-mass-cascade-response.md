# Finite-mass cascade response: WP675

## Domain

Take the WP674 cascade with an unpolarized parent, narrow widths, real positive
reciprocal vertices, a massless exit quark, and a purely chiral exit vertex.
Write \(u=|y|^2\), \(v=|z|^2\), and

\[
A=M_A^2+M_B^2-m_n^2,
\]

\[
\Lambda=left[M_A^2-(M_B+m_n)^2\right]
\left[M_A^2-(M_B-m_n)^2\right].
\]

After removing the common phase-space normalization, the finite-mass total
rate and signed angular numerator are

\[
W=A(u+v)+4M_AM_B\sqrt{uv},
\qquad
N=\sqrt\Lambda\,(u-v).
\]

The interference term is source-derived; it is not fitted away.

## Exact rank

The nonlinear response determinant is

\[
\det\frac{\partial(W,N)}{\partial(u,v)}
=-\sqrt\Lambda\left[
2A+2M_AM_B\left(\sqrt{v/u}+\sqrt{u/v}\right)
\right].
\]

It is nonzero throughout the open positive-real threshold domain. At the exact
witness \((M_A,M_B,m_n,u,v)=(5,3,1,1,1)\), it equals
\(-378\sqrt{21}\). In the massless limit, the polarization reduces to
\((u-v)/(u+v)\), recovering WP674.

At \(M_A=M_B+m_n\), \(\Lambda=0\) and the signed port collapses exactly.
Threshold support is therefore part of the faithfulness domain, not an
optional numerical correction.

## Disposition

Finite masses do not destroy local magnitude identification on the declared
positive-real slice. Complex relative phase, finite widths, off-shell
transport, reconstruction of \(X\), and detector calibration remain open.

This is still an identification operation, not a source selector.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp675_finite_mass_cascade_response.py

Generated result: results/wp675_finite_mass_cascade_response.json.
