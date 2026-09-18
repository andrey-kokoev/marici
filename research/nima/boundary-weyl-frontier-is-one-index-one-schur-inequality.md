# Boundary-Weyl frontier is one index-one Schur inequality

Prior contour and graph calculations already identify the signed spectral and Green pullbacks on the common source core. The boundary kernel before physical compression belongs to the generalized Nevanlinna class `N_1`: it has exactly one negative square, carried by the odd endpoint parity line.

After adjoining the independent endpoint graph sector, write the relevant positive/negative block as

$$
\begin{pmatrix}
C_k&b_k\\
b_k^*&1
\end{pmatrix}.
$$

Nonnegativity is equivalent to the rank-one Schur leverage inequality

$$
C_k\succeq b_kb_k^*.
$$

Equivalently, when `C_k` is reduced to its support,

$$
b_k^*C_k^\dagger b_k\le1,
$$

with `b_k` annihilating `ker C_k`. Strict inequality gives a positive margin; equality gives a semidefinite boundary direction that must be tested for transversality with the Xi kernel.

Thus the common boundary-Weyl construction does not need a new signed comparison. Its remaining positive content is the physical compression

$$
N_1\longrightarrow N_0,
$$

which occurs exactly when the endpoint leverage inequality holds.

The vertical endpoint obstruction explains why `C_k` must include the augmented endpoint graph energy; the unaugmented bulk admits sequences of vanishing norm with unit endpoint value and cannot dominate `b_k`.

Status: signed boundary coherence closed; the lowest missing positive coherence is the augmented rank-one endpoint leverage inequality.
