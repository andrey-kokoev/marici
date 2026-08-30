# Chiral-index vectorlike kernel: WP762

## Question

Can the ordinary domain-wall chiral index provide the integral source map
missing in WP761?

## Claim boundary

Let \((n_0,n_\pi)\) be positive ordered boundary zero-mode multiplicities. The
ordinary chiral or Fredholm index is

\[
I=n_0-n_\pi.
\]

Domain-wall formulations of massive Dirac indices and their relation to bulk
and edge modes are reviewed by
[Fukaya](https://arxiv.org/abs/2109.11147). The present calculation asks which
part of the ordered flavor packet such an index can carry.

## Exact kernel

The index map is the integer row

\[
\begin{pmatrix}1&-1\end{pmatrix}.
\]

Its kernel contains the diagonal vectorlike generator

\[
\begin{pmatrix}1\\1\end{pmatrix}.
\]

Consequently adding one mode to each boundary changes the total matter packet
without changing the index. The smallest portal-relevant witness is

\[
(n_0,n_\pi)=(2,1)
\quad\longrightarrow\quad
I=1,
\qquad
\Delta=\frac{9}{50},
\]

versus

\[
(n_0,n_\pi)=(3,2)
\quad\longrightarrow\quad
I=1,
\qquad
\Delta=\frac{25}{338}.
\]

The same protected nonzero index therefore permits different portal
magnitudes. This is precisely the vectorlike direction already invisible to
the anomaly probes.

## Minimal faithful completion

Add the total rank or tadpole

\[
T=n_0+n_\pi.
\]

Then

\[
\begin{pmatrix}T\\I\end{pmatrix}
=
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\begin{pmatrix}n_0\\n_\pi\end{pmatrix},
\]

whose determinant is \(-2\). On the parity-compatible integer image,

\[
n_0=\frac{T+I}{2},
\qquad
n_\pi=\frac{T-I}{2}.
\]

Thus rank plus index is faithful on the ordered charge packet. The ordinary
index alone is not.

## Disposition

The chiral index is an orientation selector and protected net-chirality
invariant, but not a tadpole-total or portal-magnitude selector. Its robustness
under continuous deformations is exactly why vectorlike threshold pairs may
change the portal without changing the index.

The constructive target is now a relative rank-index or endpoint-resolved
K-theory class with both components source-fixed. Merely appending a measured
rank is not a source explanation. The source must derive the total, primitive
normalization, and orientation together and provide a physical operation that
reads the endpoint-resolved content.

Even that integral packet must be matched through wall and Kaluza–Klein
thresholds, the RG basin, `physical16`, and a calibrated detector channel.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp762_chiral_index_vectorlike_kernel.py

Generated result:
research/flavor/results/wp762_chiral_index_vectorlike_kernel.json
