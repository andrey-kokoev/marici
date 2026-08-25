# Global parity splits every harmonic into equal electric and magnetic sectors

## 1. Antipodal-helicity action

In the standard spin frame, antipodal transport obeys

\[
 \mathsf P\,{}_sY_{lm}=(-1)^l,{}_{-s}Y_{lm}.
\]

On the paired shear coefficient space

\[
 V_l=V_l^{(+2)}\oplus V_l^{(-2)},
\]

the reflection-helicity involution is therefore

\[
 Q_l=(-1)^l
 \begin{pmatrix}0&I_{2l+1}\\I_{2l+1}&0\end{pmatrix}.
\]

Its electric and magnetic projectors are

\[
 \Pi_{E,l}=\frac{1+Q_l}{2},\qquad
 \Pi_{M,l}=\frac{1-Q_l}{2}.
\]

Each has complex rank `2l+1` before imposing reality. On a real shear pair,
each eigenspace has real dimension `2l+1`.

## 2. Reality structure

Spin-harmonic conjugation is

\[
 \overline{{}_sY_{lm}}=(-1)^{s+m}{}_{-s}Y_{l,-m}.
\]

For `s=2`, a real tensor field satisfies

\[
 c^-_{l,-m}=(-1)^m\overline{c^+_{lm}}.
\]

This condition is preserved by `Q`, by both parity projectors, and by the
grade-three multiplier because `lambda_l` is real.

## 3. Intertwining with grade three

The paired grade-three operator is block scalar at fixed `l`:

\[
 \mathcal A_{3,l}=\lambda_l
 \begin{pmatrix}I&0\\0&I\end{pmatrix}.
\]

Consequently

\[
 [\mathcal A_{3,l},Q_l]=0,
 \qquad
 \mathcal A_3\Pi_E=\Pi_E\mathcal A_3,
 \qquad
 \mathcal A_3\Pi_M=\Pi_M\mathcal A_3.
\]

The operator does not manufacture parity mixing. A magnetic-only readout first
discards the complete electric sector, then applies the same spectral
multiplier to the magnetic sector.

## 4. Kernel by parity

For `l>=5`, both parity sectors are detected. For `l=2,3,4`, both lie in the
paired transport kernel. Hence on real fields

\[
 \boxed{
 \dim_\mathbb R\ker(\mathcal A_3|_E)=21,
 \qquad
 \dim_\mathbb R\ker(\mathcal A_3|_M)=21.}
\]

The kernel of the composite magnetic readout on the full real shear space is

\[
 \boxed{
 \ker(\mathcal A_3\Pi_M)
 =\mathcal H_E\oplus
 \bigoplus_{l=2}^{4}\mathcal H_{l,M}.}
\]

This refines the finite-puncture theorem. On finite point-supported packets,
the second summand has zero intersection, so only the electric projection
alias remained. In smooth or Sobolev completions, the 21-dimensional magnetic
low-mode kernel is genuinely present.

## 5. Antipodal matching

Past-to-future matching transports each coefficient by the same invertible
`Q_l` block, possibly with the convention-fixed crossing sign. Restricting to
its graph remains faithful. The low-mode kernel exists on each matched copy
and is transported isomorphically; matching neither creates nor removes it.

## Evidence

`checkers/global_parity_helicity_harmonic_checks.py` verifies the involution,
projector ranks, reality compatibility, commutation with arbitrary spectral
multipliers, the 21+21 low-mode split, and graph faithfulness through hostile
harmonic cutoffs.
