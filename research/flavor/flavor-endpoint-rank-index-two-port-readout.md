# Endpoint rank-index two-port readout: WP763

## Question

Can an endpoint-resolved K-theory packet carry and physically read the faithful
rank-index coordinate isolated by WP762?

## Claim boundary

The admitted mathematical state is the positive cone of endpoint ranks

\[
(n_0,n_\pi)\in\mathbb Z_{>0}^2.
\]

Before a reference labels the endpoints, their exchange acts by

\[
S=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

The two complementary scalar probes are total rank and oriented index,

\[
T=n_0+n_\pi,
\qquad
I=n_0-n_\pi.
\]

## Exact two-port theorem

Each scalar probe has rank one. The joint response is

\[
\begin{pmatrix}T\\I\end{pmatrix}
=
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\begin{pmatrix}n_0\\n_\pi\end{pmatrix},
\]

with determinant \(-2\). It is faithful on the parity-compatible integer
image. One scalar linear port cannot reach rank two.

The complementary hostile pairs are exact:

- \((2,1)\) and \((3,2)\) have the same index but different total rank.
- \((2,1)\) and \((1,2)\) have the same total rank but opposite index.

Thus neither ordinary index nor aggregate rank suffices; together they
reconstruct the ordered endpoint class.

## Reference typing

Endpoint exchange preserves \(T\) and reverses \(I\). Separately labelling and
addressing both endpoints therefore changes the physical groupoid: the swap
quotient is replaced by the stabilizer of the chosen endpoint labels. This is
a new relational experiment. It does not reveal an absolute label hidden in
the original unreferenced experiment.

Two independently calibrated endpoint ports would implement the identity
response on \((n_0,n_\pi)\), equivalently the rank-index response above. But
algebraic rank is not executable control. A physical instrument requires
source-derived endpoint couplings, a common calibration frame, threshold
transfer functions, finite resolution, and uncertainties.

## Disposition

WP763 closes the mathematical readout problem conditionally: two complementary
endpoint-sensitive probes are necessary and sufficient for faithfulness on the
ordered rank packet. This is a relational readout and presentation rigidifier,
not a source selector. It reconstructs whichever endpoint class was prepared
and gives no reason that \(T=3\) or \(T=4\) should be prepared.

The next constructor must derive both the rank-index class and the two physical
endpoint couplings from one compactification or defect action. Only then can
the threshold response Jacobian, RG survival, `physical16` map, and detector
calibration be computed without sewing unrelated frames together.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp763_endpoint_rank_index_two_port_readout.py

Generated result:
research/flavor/results/wp763_endpoint_rank_index_two_port_readout.json
