# The two-node cellular boundary derives unit e6 incidence

The previous primitivity argument was insufficient: a map \(\mathbb Z\to\mathbb Z\) can multiply by two even when both lattices are primitive. The required coefficient can instead be read from the explicit normalization graph.

At the split infinity fiber, let the two normalization components be

\[
C_+,C_-.
\]

Let \(\Theta_+,\Theta_-\) denote the two node bridges. The Bunch--Davies calculation orients both from \(C_+\) to \(C_-\). Therefore the cellular boundary map is

\[
\partial:
\mathbb Z\langle\Theta_+,\Theta_-\rangle
\longrightarrow
\mathbb Z\langle C_+,C_-\rangle,
\qquad
[\partial]=
\begin{pmatrix}
-1&-1\\
1&1
\end{pmatrix}.
\]

Each individual node has unit boundary

\[
\partial\Theta_\pm=C_--C_+.
\]

The equally oriented pair satisfies

\[
\partial(\Theta_++\Theta_-)
=2(C_--C_+).
\]

The width-two primitive half-boundary is consequently

\[
\frac12\partial(\Theta_++\Theta_-)
=C_--C_+.
\]

This class is primitive, with coefficients \((-1,1)\). Hence its incidence with the dual component-difference generator is exactly \(\pm1\), not \(\pm2\).

The opposite-orientation ablation gives

\[
\partial(\Theta_+-\Theta_-)=0,
\]

confirming that equal Bunch--Davies orientation is the datum responsible for the odd class.

Thus the first parity is derived directly:

\[
a=1.
\]

No inference from saturation or torsion-freeness is used. Together with the typed marked-extension column

\[
g_{111}^{\rm top}\longmapsto
\frac{1}{8(x+y)}e_6+0\,v_{\rm alg},
\]

this yields

\[
(a,b)=(1,0).
\]

Certificate:

- `research/voevodsky/checkers/two_node_cellular_unit_incidence.py`;
- `research/voevodsky/results/two_node_cellular_unit_incidence.json`.
