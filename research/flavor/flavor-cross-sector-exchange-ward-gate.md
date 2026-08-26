# Cross-sector exchange Ward gate (WP362)

## Bounded question

Can a Ward identity fix WP361's dimensionless portal coefficient without
fitting it?

Let

\[
x=J^2,
\qquad
y=\rho=\frac{Q}{M^2},
\]

and write the portal as the rank-one quadratic form

\[
V_{\mathrm{int}}=\lambda(x-\alpha y)^2.
\]

Under the existing product groupoid, \(x\) is a flavor weak-basis invariant
and \(y\) is an effective-source reparameterization invariant. Each is a
singlet in a different sector. Their separate invariance imposes no relation
between their normalizations, so every \(\alpha>0\) remains admitted.

## Exchange calculation

For \(v=(x,y)^T\), the quadratic matrix is

\[
K_\alpha=
\begin{pmatrix}
1&-\alpha\\
-\alpha&\alpha^2
\end{pmatrix}.
\]

If a new source symmetry exchanges the two ports through

\[
P=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

then Ward invariance requires \(P^T K_\alpha P=K_\alpha\). This gives
\(\alpha^2=1\), and positivity leaves \(\alpha=1\). The selected shell becomes

\[
J^2=\frac{Q}{M^2}.
\]

The algebraic normalization is therefore fixable by an exchange Ward identity.

## Typing boundary

The exchange is not a symmetry of either original experiment. It maps a flavor
observable to a source response and is meaningful only after constructing a
common two-port state space, normalization, dynamics, and apparatus action.
It therefore defines a new relational experiment over the stabilizer
groupoid of the cross-sector exchange. It does not reveal a pre-existing
absolute normalization.

Without that named interface constructor, imposing \(P\) is an algebraic
parallelization of two valid objects in different frames. Algebraic
compatibility is not executable control.

## Disposition

The exchange symmetry would turn WP361 into a unit-normalized conditional
codimension-one selector. It still leaves fifteen CP-even coordinates and the
CP-conjugate orientation pair. At present it is a precise progressive target,
not an admitted flavor theorem: the necessary cross-sector port and physical
instrument have not been derived.

The smallest exact falsifier is \(P^T K_2P-K_2\ne0\), showing that the
otherwise legal \(\alpha=2\) portal violates the proposed exchange. The
physical falsifier is failure to construct one operation that swaps or jointly
calibrates \(J^2\) and \(Q/M^2\) while preserving the declared dynamics.

Run `uv run --with sympy python
research/flavor/checkers/wp362_cross_sector_exchange_ward_gate.py` to
regenerate the exact result.
