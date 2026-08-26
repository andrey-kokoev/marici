# Dimensionless portal normalization (WP361)

## Bounded question

Does WP359's intrinsic fluctuation scale remove the free matching coefficient
in WP360 by dimensional analysis?

The canonical source supplies two invariant quantities with mass dimension
two: the squared displacement \(Q\) and pole-curvature scale \(M^2\). Their
dimensionless ratio is

\[
\rho=\frac{Q}{M^2}.
\]

The dimensionally closed portal family is

\[
V_{\mathrm{int}}=\lambda(J^2-\alpha\rho)^2,
\qquad \alpha>0.
\]

Every value of \(\alpha\) has the same weak-basis, CP-even, field-rescaling,
and dimensional typing. Dimensional analysis therefore replaces the
dimensionful coefficient \(c\) by a dimensionless Wilson coefficient; it does
not select that coefficient.

## Source quotient loss

Using WP359's exact inverse,

\[
U=-\frac{M^2}{Q},
\]

so \(\rho=-1/U\). The portal shell is consequently

\[
J^2=-\frac{\alpha}{U}.
\]

It sees the canonical quartic coupling but discards the independent sextic
direction. For example, source readouts \((Q,M^2)=(1,4)\) and \((2,8)\) share
\(\rho=1/4\) and select the same flavor shell, while their reconstructed
canonical sextic coefficients are 3 and \(3/2\).

## Authority and disposition

The selected shell responds independently to both surviving quantities:

\[
\frac{\partial J^2}{\partial\alpha}=\rho,
\qquad
\frac{\partial J^2}{\partial U}=\frac{\alpha}{U^2}.
\]

The operation remains a conditional codimension-one selector and shell
rigidifier. It is neither a numerical selector nor a faithful identifier of
the WP359 source quotient. Setting \(\alpha=1\) is a normalization convention
only if a source symmetry or matching theorem enforces it; dimensional
analysis alone supplies no such authority.

The smallest exact falsifier is that \(\alpha=1\) and \(\alpha=2\) are equally
typed but select different shells for the same source. The remaining physical
gate is a microscopic matching calculation or Ward identity fixing
\(\alpha\), plus an instrument measuring \(Q/M^2\) and \(J^2\) in one scheme.

Run `uv run --with sympy python
research/flavor/checkers/wp361_dimensionless_portal_normalization.py` to
regenerate the exact result.
