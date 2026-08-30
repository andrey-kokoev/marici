# Massive-vector current exchange fixes a sign but leaves a scale fiber: WP767

## Question

Can the D-term-specific constructor requested by WP766 make the asymmetric
portal unavoidable and threshold-stable?

## Source operation

Admit two light current multiplets and one source-defined Higgsed Abelian
vector multiplet. In a fixed normalization its algebraic Kähler sector is

\[
K(V)=\frac{M_V^2}{2}V^2+JV,
\qquad
J=2g\left(q_n N^\dagger N+q_x X^\dagger X\right).
\]

The vector equation gives (V=-J/M_V^2), so classical elimination is not a
fitted projection:

\[
K_{\mathrm{eff}}=-\frac{J^2}{2M_V^2}.
\]

With

\[
M_V^2=2g^2q_\phi^2v^2,
\]

the mixed portal coefficient is

\[
\lambda_{nx}=-\frac{2q_nq_x}{q_\phi^2v^2}.
\]

Thus a declared charge orientation fixes the tree-level sign, and the gauge
coupling cancels. This is stronger than merely allowing an independent
difference of low-energy couplings.

## Exact hostile fibers

The constructor does not fix the Higgs clock. At unit charges,

\[
v=1\;\Longrightarrow\;\lambda_{nx}=-2,
\qquad
v=2\;\Longrightarrow\;\lambda_{nx}=-\frac12.
\]

Both theories have the same field grammar, current channel, charge
orientation, and tree matching mechanism. Their magnitudes differ by a factor
of four.

WP766 also permits an independent renormalized Kähler boundary. The completed
coefficient is

\[
\lambda_{nx}^{\mathrm{IR}}
=-\frac{2q_nq_x}{q_\phi^2v^2}+c_K.
\]

The symmetry-admissible choice

\[
c_K=\frac{2q_nq_x}{q_\phi^2v^2}
\]

cancels the portal. Unique-mediator exchange therefore does not by itself
prove threshold survival.

## Classification

Massive-vector current exchange is a genuine source constructor and a
tree-level sign selector after charge orientation is admitted. It is not a
complete numerical selector: the Higgs scale is continuous, the D-term
boundary remains legal, and no calibrated physical readout has been derived.

The next progressive mechanism must jointly provide:

1. a source-derived orientation of (q_nq_x);
2. a quantized or isolated value of (q_\phi v) in the physical clock;
3. a D-term Ward identity or complete matching theorem eliminating (c_K);
4. an RG basin preserving the selected class;
5. a calibrated instrument descending to `physical16`.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp767_massive_vector_current_exchange_scale_fiber.py

Generated result:
research/flavor/results/wp767_massive_vector_current_exchange_scale_fiber.json
