# 883 — The Source Five-Point KLT Basis Is Diagonal by Common Vertices

## Record

Date: 2026-08-18

Status: exact five-point support and inversion theorem in the source KLT bases. This records a cycle-pairing/KLT-kernel statement, not yet the full twisted period identity with period matrices.

## Frozen source bases

Mizera's five-point KLT example uses

\[
\mathcal B=\{12345,12435\},
\qquad
\mathcal C=\{13254,14253\}.
\]

The inverse KLT matrix is

\[
m_{\alpha'}(\mathcal B\mid\mathcal C)
=
\begin{pmatrix}
\dfrac1{\sin(\pi\alpha's_{23})\sin(\pi\alpha's_{45})}&0\\[2mm]
0&\dfrac1{\sin(\pi\alpha's_{24})\sin(\pi\alpha's_{35})}
\end{pmatrix}
\]

up to the paper's declared common normalization.

## Carrier derivation of the zero pattern

For an ordering \(\beta\), let \(F(\beta)\) be its five two-particle boundary channels. Direct labelled incidence gives

\[
F(12345)\cap F(13254)=\{23,45\},
\]

\[
F(12435)\cap F(14253)=\{24,35\},
\]

while

\[
F(12345)\cap F(14253)=\varnothing,
\qquad
F(12435)\cap F(13254)=\varnothing.
\]

Each nonempty intersection is one compatible codimension-two vertex of \(\overline{\mathcal M}_{0,5}(\mathbb R)\). Thus the native associahedral carrier forces

\[
\boxed{
\operatorname{supp}m_{\alpha'}=
\begin{pmatrix}
(23)\cap(45)&0\\
0&(24)\cap(35)
\end{pmatrix}.
}
\]

No cancellation or fitted basis transformation is used.

## Coefficient valuation and inversion

The Koba--Nielsen loading assigns the two common vertices their sine valuations. Matrix inversion is therefore entrywise:

\[
\boxed{
m_{\alpha'}^{-1}=
\begin{pmatrix}
\sin(\pi\alpha's_{23})\sin(\pi\alpha's_{45})&0\\
0&\sin(\pi\alpha's_{24})\sin(\pi\alpha's_{35})
\end{pmatrix}.
}
\]

At the physical sample of Entry 881,

\[
(s_{12},s_{23},s_{34},s_{45},s_{51})=(2,3,5,11,17),
\]

momentum conservation gives

\[
s_{24}=s_{51}-s_{23}-s_{34}=9,
\qquad
s_{35}=s_{12}-s_{34}-s_{45}=-14.
\]

After removing the common \((\pi\alpha')^2\) factor, the field-theory kernel is

\[
\operatorname{diag}(33,-126),
\]

which exactly inverts

\[
\operatorname{diag}\left(\frac1{33},-\frac1{126}\right).
\]

## Narrow conclusion

The five-point KLT basis is not diagonal because of an arbitrary algebraic convenience. Its zero pattern is selected by common associahedral vertices, while its nonzero values require the string coefficient local system:

\[
\boxed{
\text{carrier incidence selects entries}
\quad+\quad
\text{Koba--Nielsen monodromy values them}.
}
\]

This is a first circuit-level compatibility result for the string sector. It supports shared carrier/calculus with sector-specific coefficients; it does not identify string coefficients with scattering coefficients.

## Next falsifier

Retain these cycle bases and the source Parke--Taylor cocycle basis. Construct the two period matrices and test the typed twisted-period identity

\[
\mathbf C=\mathbf P^{\mathsf T}\mathbf H^{-1}\mathbf P^\vee
\]

with source orientation and normalization. The identity must be checked as a homology--cohomology comparison, not inferred from invertibility of \(\mathbf H\).

## Certificate

Run:

```text
cargo run --quiet --bin string_five_point_diagonal_klt_basis
```

Artifacts:

- `research/benincasa/marici-gm/src/bin/string_five_point_diagonal_klt_basis.rs`
- `research/benincasa/string-five-point-diagonal-klt-basis.json`

## Source

Sebastian Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*, arXiv:1706.08527, Section 3.3, five-point KLT example; Sections 3.1--3.2 for the cycle and Parke--Taylor bases.
