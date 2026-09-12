# Four-prime valuation hypercube

## Construction

Choose the axes

\[
(p_0,p_1,p_2,p_3)=(2,3,5,7).
\]

A vertex is a support vector

\[
\epsilon\in\{0,1\}^4
\]

and carries the arithmetic label

\[
n(\epsilon)=2^{\epsilon_0}3^{\epsilon_1}5^{\epsilon_2}7^{\epsilon_3}.
\]

An oriented edge in direction \(i\) is multiplication by \(p_i\). Thus the full cell is the squarefree interval from \(1\) to \(210\) inside the valuation lattice \(\mathbb N^{(\mathbb P)}\).

A cell is encoded by a disjoint pair \([S;D]\): axes in \(S\) are fixed at one, axes in \(D\) vary, and all remaining axes are fixed at zero. Its dimension is \(|D|\). Its vertices have supports \(S\cup U\), for \(U\subseteq D\).

## Three labels on each cell

Every cell retains three different grades.

1. **Arithmetic position:** the lower label \(n(S)=\prod_{i\in S}p_i\).
2. **Traversal grade:** vertex grades range from \(|S|\) to \(|S|+|D|\).
3. **Coherence dimension:** the cell has dimension \(|D|\).

Therefore traversal power and coherence dimension do not coincide. For example:

- the vertex \(210\) has traversal grade four but coherence dimension zero;
- the full cell \([\varnothing;\{0,1,2,3\}]\) has coherence dimension four while its vertices span traversal grades zero through four;
- a depth-four label \(2^4\) has traversal grade four but lies on one arithmetic axis and is absent from this squarefree cube.

This separates same-axis cyclic depth, independent-axis cubical dimension, and lattice position.

## Faces and residuals

For ordered varying axes \(D=(i_0,\ldots,i_{d-1})\), define

\[
\partial[S;D]
=
\sum_{a=0}^{d-1}(-1)^a
\left(
[S\cup\{i_a\};D\setminus\{i_a\}]
-
[S;D\setminus\{i_a\}]
\right).
\]

The checker verifies

\[
\partial^2[S;D]=0
\]

for every cell. For a square this is the strict arithmetic interchange

\[
T_pT_q=T_qT_p.
\]

For cubes and the 4-cell it says that oriented face residuals cancel pairwise. This is the strict source skeleton. A decorated transport may replace equality by comparison cells; its nonzero residual would measure failure to preserve this skeleton.

## Census

The generated cube has:

| dimension | cells |
|---:|---:|
| 0 | 16 |
| 1 | 32 |
| 2 | 24 |
| 3 | 8 |
| 4 | 1 |

The complete machine-readable enumeration is `four-prime-hypercube.v2.json`.

## Source transport decoration

Each edge in prime direction \(p\) now carries the existing weight-zero source arrow

\[
d_p=c_p\otimes R_p,
\]

where \(c_p\) creates the prime label and

\[
(R_pf)(q)=f(q+\log p)
\]

moves the seam oppositely. Its two Mellin-position weights cancel:

\[
[H_{\rm lab},c_p]=(\log p)c_p,
\qquad
[Q,R_p]=-(\log p)R_p,
\]

and hence

\[
[H_{\rm lab}+Q,d_p]=0.
\]

The checker records this cancellation on all 32 edges. Fermionic creation supplies the cubical orientation: for distinct primes,

\[
d_pd_q+d_qd_p=0.
\]

Consequently the earlier combinatorial identity \(\partial^2=0\) is exactly the algebraic identity \(d^2=0\) for the decorated source cube, rather than an accidental matching of cell counts.

On the full seam line these arrows form a contractible Koszul complex. On the half-line, contraction leaves the edge-labelled window

\[
P_p=1_{[0,\log p)}.
\]

Thus the strict 4-cube is the source interior, while its physically retained information lies in the collection of boundary windows decorating its directions. The next nontrivial residual is not the undecorated cube boundary—it is the mixed transport of the \(P_p\) windows around its square and cubic faces.

## Result

The suspected unity is real but graded:

\[
\boxed{
\text{valuation vectors give position,}
\quad
\text{prime support gives traversal grade,}
\quad
\text{commuting prime directions give cubical coherence.}
}
\]

They are three projections of one labelled higher-incidence object, not one numerical grading. The next comparison should decorate each prime edge by its actual source transport and compute whether every square, cube, and 4-cell remains fillable after analytic and boundary readout.

## Verification

Run:

```text
python research/coherence/check_four_prime_hypercube.py
```

It checks the cell census, all 32 weight cancellations, and every integral cubical identity \(\partial^2=0\), then regenerates the v2 JSON artifact.
