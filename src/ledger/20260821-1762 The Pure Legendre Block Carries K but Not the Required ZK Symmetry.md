# 1762 — The Pure Legendre Block Carries \(K\) but Not the Required \(ZK\) Symmetry

## Source-defined real structure

The universal Legendre periods satisfy

\[
m(1-m)y''+(1-2m)y'-\frac14y=0.
\]

In the fixed source-labelled basis \((y,y')\), the cleared first-order
connection is

\[
4m(1-m)A(m)
=
\begin{pmatrix}
0&4m(1-m)\\
1&-4(1-2m)
\end{pmatrix}.
\]

Every coefficient is real. Hence plain complex conjugation \(K\) is a
horizontal antiunitary real structure.

## \(ZK\) test

Entry 1761's selective deletion requires

\[
\Theta=ZK,
\qquad Z=\operatorname{diag}(1,-1).
\]

Since the connection is real, horizontality of this constant involution
would require

\[
ZAZ=A.
\]

Instead, \(ZAZ\) reverses both off-diagonal entries. The lower-left entry is
identically nonzero, so equality fails at every generic modulus.

The same obstruction appears in the source-normalized integral cusp
monodromy:

\[
T=
\begin{pmatrix}1&2\\0&1\end{pmatrix},
\qquad
ZTZ=
\begin{pmatrix}1&-2\\0&1\end{pmatrix}
\ne T.
\]

## Narrow result

In the fixed source-labelled Legendre frame:

\[
\boxed{
K\ \text{is horizontal},
\qquad
ZK\ \text{is not}.
}
\]

Therefore the pure homogeneous elliptic coefficient block does not activate
Entry 1760's selective companion-deletion extension. Plain \(K\) has the
opposite Pauli character pattern:

\[
(I,X,Y,Z)\longmapsto(I,X,-Y,Z).
\]

This conclusion is basis-scoped. It does not forbid a different
source-derived coefficient extension from carrying \(ZK\), but a
presentation-dependent gauge change cannot be used to declare one.

No new carrier stratum is implicated.

## Durable artifacts

- research/benincasa/checkers/legendre_real_structure.rs
- research/benincasa/results/legendre-real-structure.json
- research/benincasa/legendre-real-structure.md

## Next falsifier

Test the full marked relative rank-twelve extension rather than the pure
elliptic quotient. Determine whether its algebraic--elliptic extension block
admits a horizontal antiunitary lift whose restriction is plain \(K\) on the
Legendre quotient but induces \(ZK\) on a supported rank-two subquotient.
