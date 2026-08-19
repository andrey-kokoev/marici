# The Higher-Pole One-Plus-Five Filtration Is Not a Finite Connection Module

## Typing the next operation

Entry 1045 constructs the intrinsic filtration

\[
0\subset Q_1\subset Q_6
\]

inside the Cayley--Menger pole-depth-three exact-valuation object.  Asking
whether the tangential connection preserves \(Q_1\) inside this finite
six-plane assumes that the depth-three source complex is horizontal.  It is
not.

For a labelled form with Cayley--Menger pole index \(k\), the exact source
connection contains

\[
(\gamma-k)T(K)
\]

in pole index \(k+1\).  Along the triangle wall,

\[
T_1=\partial_{X_1}+\partial_{X_3},
\qquad
T_2=\partial_{X_2}+\partial_{X_3},
\]

and exact seven-node differentiation gives

\[
T_1(K)\ne0,
\qquad
T_2(K)\ne0
\]

at \((X_1,X_2,X_3)=(2,3,5)\) over \(\mathbf F_{32003}\).

## Nonzero pole-raising symbols

With \(\gamma=5\), the relevant source-relation coefficients are

\[
\begin{array}{c|c}
\text{source stratum}&\text{coefficient of the next }K\text{-pole relation}\\
\hline
d_{\rm dR}^{k=2}&3\\
K^{k=2}&2\\
q_i^{k=3}&2.
\end{array}
\]

All are nonzero in \(\mathbf F_{32003}\).  Therefore the exact connection
raises the source pole filtration:

\[
\nabla_T(F_k)\subseteq F_{k+1},
\qquad
\nabla_T(F_k)\nsubseteq F_k
\]

at chain level.

## Consequence

The six-plane \(Q_6\), and hence its line \(Q_1\), is not presently a finite
differential module on which a closed \(6\times6\) connection matrix may be
computed.  Projecting the pole-raising terms back into depth three would
repeat the invalid operation diagnosed in Entries 878 and 1011.

The canonical structure is instead a filtered connection with degree-one
symbol

\[
\boxed{
\theta_T:\operatorname{gr}^{K}_k E_2
\longrightarrow
\operatorname{gr}^{K}_{k+1}E_2.
}
\]

Thus Entry 1045's suggested question—whether \(Q_1\) mixes into the
five-plane at the same finite depth—is superseded.  The first legitimate
mixing target lies at the next Cayley--Menger pole depth.

## Corrected frontier

Compute the depth-four exact-valuation object and the induced leading symbol

\[
\theta_T:E_2^{(3)}/E_2^{(2)}
\longrightarrow
E_2^{(4)}/E_2^{(3)}
\]

for both tangents.  Only if this symbol vanishes on the one-line does that
line become horizontal after passage to the direct limit.  Otherwise the
one-plus-five block is the first layer of a growing filtered connection, not
a finite sector-specific lens.

## Durable verification

- checker:
  `research/nima/audit_triangle_wall_pole_connection_symbol.py`;
- packet:
  `research/nima/triangle-wall-pole-connection-symbol.json`;
- exact derivative source:
  `research/nima/check_unbounded_twisted_derham_connection_commutator.py`;
- allocator claim: `seqclaim-54e82b64f29a79048ac2f30b`.
