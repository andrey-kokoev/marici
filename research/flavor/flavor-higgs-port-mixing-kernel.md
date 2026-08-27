# Visible Higgs-port mixing kernel: WP692

## Source-to-readout factorization

After the independently declared Higgs and radial exit-flavon vacua, the
quadratic portal produces a real mixing entry \(\kappa\). The inverse radial
propagator is

\[
K(s)=
\begin{pmatrix}
s-m_h^2&-\kappa\\
-\kappa&s-m_x^2
\end{pmatrix}.
\]

Ordinary visible Higgs production and decay couples to

\[
(K^{-1})_{hh}
=\frac{s-m_x^2}
{(s-m_h^2)(s-m_x^2)-\kappa^2}.
\]

This supplies a legal detector projection without requiring the exit flavon
itself to be directly observed. It also exposes the first detector kernel:
the visible port is even in \(\kappa\).

## Two-bin contextual rank

Let the mixing response in two physical bins be

\[
\kappa_i=a+b\Phi_i.
\]

The minimal visible deformation is proportional to \(\kappa_i^2\). Its
Jacobian with respect to \((a,b)\) has determinant

\[
4\kappa_1\kappa_2(\Phi_2-\Phi_1).
\]

Two distinct threshold contexts therefore restore local rank whenever neither
bin lies on a mixing zero. They do not give global source identification:

\[
(a,b)\sim(-a,-b)
\]

under the visible Higgs projection.

## Typing and falsifiers

This operation is a candidate physical readout and a contextual rank repair.
It is not a numerical selector. The smallest rank falsifiers are coincident
kernel values or one exact mixing zero. An odd-in-mixing observation would
require an independently sourced exit-odd reference; adding it would define a
richer relational experiment rather than reveal an absolute sign.

The remaining physical-instrument gate is to derive the complete
momentum-dependent mixing self-energy from the messenger grammar and bind the
propagator deformation to calibrated visible final-state bins including
widths, backgrounds, detector resolution, and uncertainties.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp692_higgs_port_mixing_kernel.py

Generated result: results/wp692_higgs_port_mixing_kernel.json.
