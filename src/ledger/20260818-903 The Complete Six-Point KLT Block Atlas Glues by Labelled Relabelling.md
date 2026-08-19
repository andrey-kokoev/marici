# 903 — The Complete Six-Point KLT Block Atlas Glues by Labelled Relabelling

## Frozen source bases

The source six-point columns are ordered as

\[
\begin{aligned}
&(123456),(124356),\\
&(132456),(134256),\\
&(142356),(143256),
\end{aligned}
\]

and the rows as

\[
\begin{aligned}
&(153462),(154362),\\
&(152463),(154263),\\
&(152364),(153264).
\end{aligned}
\]

The source matrix is block diagonal with three \(2\times2\) blocks. Entry 901 derived the first block and its inverse from Pochhammer cells.

## Labelled transition packet

Let \(B_0\) denote the first block in its displayed row and column bases.

The second block is obtained by the source-labelled permutation

\[
\sigma_{23}=(2\;3):
\]

\[
(123456,124356)
\mapsto
(132456,134256),
\]

\[
(153462,154362)
\mapsto
(152463,154263).
\]

Hence

\[
B_1=\sigma_{23}B_0.
\]

For \(\sigma_{24}=(2\;4)\), the raw images are reversed relative to the published bases:

\[
(123456,124356)
\mapsto
(143256,142356),
\]

\[
(153462,154362)
\mapsto
(153264,152364).
\]

Therefore the third transition necessarily contains the exchange matrix

\[
J=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

on both variances:

\[
\boxed{
B_2=J\,(\sigma_{24}B_0)\,J.
}
\]

This is a basis-ordering transport, not an adjustable sign or gauge.

## Complete inverse audit

Each block is reconstructed from the relabelled Pochhammer \(\csc\) and \(\cot\) cells before inversion. Its inverse is obtained by applying the same labelled transition to Entry 901's source-derived inverse.

The assembled matrices are

\[
M_6=\operatorname{diag}(B_0,B_1,B_2),
\qquad
K_6=\operatorname{diag}(B_0^{-1},B_1^{-1},B_2^{-1}).
\]

At a generic nonresonant labelled Mandelstam point,

\[
\|M_6K_6-I_6\|_{\max}
=
9.22\times10^{-16}.
\]

Every off-block entry remains exactly zero. The evidence packet is at

research/benincasa/string-six-point-block-atlas.json.

## Narrow result

The complete source six-point block atlas glues under explicit occurrence relabelling:

\[
\boxed{
\text{one Pochhammer block}
+
\sigma_{23}
+
J\sigma_{24}J
\Longrightarrow
\text{full }6\times6\text{ kernel}.
}
\]

No new gluing divisor, off-block extension, or coherence cell is required. The only nontrivial atlas datum is the forced reversal \(J\) in the third published basis.

## Implication

Entries 895–903 now establish, through six points, that the string sector's finite corrections are compiled from

\[
\text{associahedral incidence carrier}
+
\text{rank-one Koba–Nielsen local system}
+
\text{oriented Pochhammer/Koszul calculus}.
\]

This is structurally parallel to cosmology's proposed shared-carrier architecture, but with a simpler sector-specific coefficient object.

## Scope boundary and next falsifier

The block atlas is source-block-diagonal. It does not test a basis whose KLT matrix is generically dense.

The next falsifier is a non-block-adapted six-point basis change. Freeze one dense source basis, derive it from the same twisted-cycle atlas, and test whether inversion creates only existing sine-letter support. A new irreducible determinant factor there would be the first string-sector challenge to the current shared-calculus thesis.
