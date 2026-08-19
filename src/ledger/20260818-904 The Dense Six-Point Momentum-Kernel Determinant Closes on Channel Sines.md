# 904 — The Dense Six-Point Momentum-Kernel Determinant Closes on Channel Sines

## Frozen source object

Use the string momentum kernel of Bjerrum-Bohr, Damgaard, Sondergaard, and Vanhove, arXiv:1010.3933, equation (17):

\[
\mathcal S_{\alpha'}[i_1,\ldots,i_k\mid j_1,\ldots,j_k]_p
=
(\pi\alpha'/2)^{-k}
\prod_{t=1}^k
\sin\!\left(\pi\alpha'\left(
p\cdot k_{i_t}
+\sum_{q>t}\theta(i_t,i_q)k_{i_t}\cdot k_{i_q}
\right)\right),
\]

where \(\theta=1\) precisely when the pair has opposite order in the two words.

At six points freeze the dense basis

\[
S_3=(234,243,324,342,423,432)
\]

on both variances and take \(p=k_1\). No block-atlas basis change is used.

## Exact Laurent encoding

Write

\[
x_i=e^{i\pi\alpha' k_1\cdot k_i},
\qquad
y_{ij}=e^{i\pi\alpha' k_i\cdot k_j},
\]

and represent each sine, up to its common invertible scalar, by

\[
\sin(\arg X)\longmapsto X-X^{-1}.
\]

This converts the complete dense \(6\times6\) determinant into an exact Laurent calculation.

## Determinant certificate

The channel factors and multiplicities are

\[
\begin{array}{c|c}
\text{Laurent monomial} & \text{multiplicity}\\
\hline
x_2,x_3,x_4 & 2,2,2\\
y_{23},y_{24},y_{34} & 2,2,2\\
y_{23}y_{24}y_{34} & 1\\
x_2x_3y_{23},x_2x_4y_{24},x_3x_4y_{34} & 1,1,1\\
x_2x_3x_4y_{23}y_{24}y_{34} & 2.
\end{array}
\]

Equivalently, these are the one-particle, internal two-particle, internal three-particle, pivoted two-particle, and full pivoted channel sines.

For every factor, the exact truncated-series determinant has the displayed valuation on both branches

\[
X=+1,
\qquad
X=-1.
\]

The multiplicities sum to

\[
6+6+1+3+2=18,
\]

which saturates the determinant degree bound. At six additional generic points the quotient by the displayed product is the constant \(-1\). The complete calculation replicates over the independent primes

\[
2305843009213693951,
\qquad
2305843009213693921.
\]

The durable checker is

research/benincasa/marici-gm/src/bin/string_six_point_dense_momentum_kernel.rs,

and its convention packet is

research/benincasa/string-six-point-dense-momentum-kernel.json.

## Narrow result

The standard dense six-point momentum kernel introduces no determinant divisor beyond source-derived channel sines in the exact two-prime certificate:

\[
\boxed{
\det\mathcal S_{\alpha'}^{(6)}
\sim
-\prod_A \sin(\pi\alpha' s_A)^{m_A},
}
\]

with the eleven labelled factors and multiplicities above.

In particular, the internal three-particle factor

\[
\sin\!\bigl(\pi\alpha'(k_2+k_3+k_4)^2/2\bigr)
\]

is required. Omitting it leaves one unsaturated determinant degree and can be mistaken for a new mixed divisor.

## Implication for the sector comparison

Entry 903's block diagonalization did not hide a dense-basis obstruction. The same incidence channels reappear in a different coefficient presentation:

\[
\text{associahedral channel carrier}
+
\text{rank-one Koba--Nielsen local system}
+
\text{momentum-kernel basis transport}.
\]

This strengthens the string-sector analogue of H2: changing from the Pochhammer block atlas to a canonical dense source basis changes the coefficient matrix, not the carrier divisor set.

## Scope boundary and next falsifier

This is a determinant/support theorem at six points. It does not construct a chain-level equivalence between the dense momentum-kernel basis and Entry 903's block atlas.

The next test is therefore coherence rather than another determinant scan: derive the explicit twisted-cycle transition matrix between the two source bases and verify that it intertwines their residue factorizations on every channel wall, including codimension-two intersections.
