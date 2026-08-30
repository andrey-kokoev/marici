# The enlarged Adams cell has two nested contraction gates

## Full positive block

On reduced supports, let

\[
\mathcal G=
\begin{pmatrix}
A&C\\
C^{*}&D
\end{pmatrix},
\qquad
A>0,
\qquad
D>0.
\]

The endpoint Schur complement is

\[
G_{\mathrm{eff}}=A-CD^{-1}C^{*}.
\]

Define the normalized endpoint loading operator

\[
L=D^{-1/2}C^{*}A^{-1/2}.
\]

Then the factorization is exact:

\[
G_{\mathrm{eff}}
=
A^{1/2}(I-L^{*}L)A^{1/2}.
\]

Therefore

\[
\mathcal G\ge0
\quad\Longleftrightarrow\quad
\|L\|\le1,
\]

with strict endpoint coercivity when \(\|L\|<1\).

This is distinct from positivity of the auxiliary reciprocal block.

## Internal and external contractions

For

\[
D_{\pm}=S\pm iT
=
S^{1/2}(I\pm K)S^{1/2},
\qquad
K=S^{-1/2}(iT)S^{-1/2},
\]

the internal quarter-turn gate is

\[
\|K\|<1.
\]

Once a reciprocal sheet is selected, its external loading operator is

\[
L_{\pm}
=
D_{\pm}^{-1/2}C^{*}A^{-1/2}.
\]

The full cell requires

\[
\|K\|<1
\quad\text{and}\quad
\|L_{\pm}\|<1.
\]

The first states that the even tail/PV energy can carry the Fourier orientation. The second states that the resulting auxiliary carrier does not exhaust the bare endpoint energy.

Neither implies the other.

## Reciprocal pair condition

Source reciprocity must provide a conjugation or reflection intertwining \(D_{+}\) with \(D_{-}\), together with the correctly transformed incidence. If \(C\) is reflection invariant in the declared frame, both endpoint sheets must satisfy

\[
\sup_{\epsilon\in\{+,-\}}\|L_{\epsilon}\|<1.
\]

One-sheet loading control is insufficient. The more singular reciprocal sheet can fail even when the internal contraction \(K\) is uniformly separated from one.

## Completion margins

Define

\[
\delta_{\mathrm{int}}
=
1-\|K\|,
\qquad
\delta_{\mathrm{load}}
=
1-\max(\|L_{+}\|^2,\|L_{-}\|^2).
\]

Uniform completion requires positive lower bounds for both on compact off-seam sets, as well as absolute equivalence bounds for \(A\) and \(S\).

These margins have different roles:

- \(\delta_{\mathrm{int}}\) is local constructor admissibility of the Fourier-oriented auxiliary block;
- \(\delta_{\mathrm{load}}\) is the first assembled Green coercivity margin of the enlarged cell.

The second should feed the existing diagonal or mixed global Green margin rather than be counted independently after global assembly.

## Comparison bound

Since

\[
D_{\pm}^{-1}
=
S^{-1/2}(I\pm K)^{-1}S^{-1/2},
\]

we have

\[
\|L_{\pm}\|
\le
\frac{
\|S^{-1/2}C^{*}A^{-1/2}\|
}{
\sqrt{1-\|K\|}
}.
\]

Thus a sufficient joint condition is

\[
\|S^{-1/2}C^{*}A^{-1/2}\|^2
<
1-\|K\|.
\]

This exhibits the exact competition: quarter-turn saturation amplifies the incidence loading budget.

The estimate is sufficient, not generally necessary, because it discards spectral alignment between \(K\) and the incidence range. The exact theorem remains the pair of sheetwise norms \(\|L_{\pm}\|<1\).

## Radical-safe statement

If \(A\) or \(D\) is semidefinite, first quotient by the declared radicals and prove

\[
\ker D\subseteq\ker C,
\qquad
\ker A\subseteq\ker C^{*}.
\]

Only reduced square roots may be used. Pseudoinverse formulas before these containments can hide a dark endpoint or auxiliary direction.

## Hostiles

1. **Internally valid, externally overloaded:** \(\|K\|<1\) but \(\|L_+\|\ge1\). The auxiliary phase cell exists while the full Green block is indefinite.
2. **Weak phase, large incidence:** \(K=0\) and \(\|L\|\ge1\). Failure has nothing to do with reciprocal orientation.
3. **Sheet imbalance:** \(\|L_+\|<1\) but \(\|L_-\|\ge1\).
4. **Scale escape:** both dimensionless margins stay positive while \(A^{-1/2}\) or \(S^{-1/2}\) loses uniform control.
5. **Spectral-alignment false negative:** the sufficient scalar bound fails although the exact sheetwise loading operators remain contractions.

## Next source calculation

After deriving \(S_p,T_p,C_p,A_p\), compute both normalized objects

\[
K_p=S_p^{-1/2}(iT_p)S_p^{-1/2},
\qquad
L_{p,\pm}=D_{p,\pm}^{-1/2}C_p^{*}A_p^{-1/2}.
\]

This gives a complete finite positivity certificate for the first enlarged Adams cell before global prime assembly.
