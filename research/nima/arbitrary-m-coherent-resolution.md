# Coherent Resolution at every finite type-A rank

## Question

Can the finite A3 resolution be extended uniformly without assuming an arbitrary-cutoff history-to-positroid compiler?

## Construction

For every integer `m >= 1`, let `P_m` be the inclusion poset of pairwise noncrossing diagonal sets in an `(m+3)`-gon. Its objects are partial triangulations, including the empty set. Define `CR_m` to be the augmented simplicial chain complex of strict chains in `P_m`.

For a generator

\[
F_0\subsetneq F_1\subsetneq\cdots\subsetneq F_k,
\]

the differential is alternating deletion:

\[
d[F_0<\cdots<F_k]
=
\sum_{i=0}^k(-1)^i[F_0<\cdots<\widehat F_i<\cdots<F_k].
\]

Degree-zero generators augment to `1`.

## Exactness

The empty partial triangulation is the minimum of `P_m`. Define

\[
h(1)=[\varnothing],
\]

and

\[
h(\sigma)=
\begin{cases}
[\varnothing<\sigma],&\varnothing\notin\sigma,\\
0,&\varnothing\in\sigma.
\end{cases}
\]

Direct cancellation gives

\[
dh+hd=\operatorname{id}.
\]

Therefore the augmented complex is exact for every finite `m`. The checker exhaustively verifies the differential and contraction through `A4`.

## Relation to the physical programme

This gives an arbitrary-rank combinatorial Coherent Resolution without choosing cellular orientations: it is the barycentric subdivision of the associahedral face carrier. For NNMHV cutoff `n`, the positive-root rank is `m=n-5`.

This does not solve the arbitrary-`n` history-to-positroid problem. A physical lift requires a natural family of maps

\[
H_n\longrightarrow CR_{n-5}
\]

from labelled history cells, together with canonical-weight coefficient transport commuting with the differentials.

## Claim boundary

The quantifier is: for every finite `m`, there is an exact finite complex `CR_m`. No single cutoff is asserted to resolve all ranks, and no colimit or completed exactness is claimed.

Verification:

- `research/nima/checkers/check_arbitrary_m_coherent_resolution.py`
- `research/nima/results/arbitrary-m-coherent-resolution.json`
