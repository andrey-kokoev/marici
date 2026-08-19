# 901 — The Mixed Six-Point KLT Block Introduces No New Determinant Divisor

## Frozen source block

Take the first source \(2\times2\) six-point inverse-KLT block

\[
M=
\begin{pmatrix}
\dfrac1{S_{12}S_{34}S_{345}}
&
-\dfrac{C_{34}+C_{35}}{S_{12}S_{345}}
\\[3mm]
-\dfrac{C_{34}+C_{45}}{S_{12}S_{345}}
&
\dfrac1{S_{12}S_{34}S_{345}}
\end{pmatrix},
\]

where

\[
S_I=\sin(\pi s_I),
\qquad
C_I=\cot(\pi s_I),
\]

and source kinematics gives

\[
s_{345}=s_{34}+s_{35}+s_{45}.
\]

The diagonal entries are trivalent common-vertex contributions. The off-diagonal entries mix two four-point self-intersection histories. This is the first tested block where multiple vertices and an internal coefficient sum coexist.

## Pochhammer reconstruction

Every entry is built before inversion from the source cells

\[
\csc(\pi s)=
2i\frac{e^{\pi i s}}{e^{2\pi i s}-1},
\]

\[
\cot(\pi s)=
2i\left(\frac1{e^{2\pi i s}-1}+\frac12\right).
\]

No target inverse entry or determinant factor is used to choose the block representative.

## Determinant factorization

The only nontrivial identity required is

\[
\sin(\pi s_{35})\sin(\pi s_{45})
-
\sin\pi(s_{34}+s_{35})
\sin\pi(s_{34}+s_{45})
=
-\sin(\pi s_{34})\sin(\pi s_{345}).
\]

It yields

\[
\boxed{
\det M
=
-\frac1{
S_{12}^{,2}S_{34}S_{35}S_{45}S_{345}}.
}
\]

Thus block inversion introduces no divisor involving the mixed sums

\[
s_{34}+s_{35},
\qquad
s_{34}+s_{45}.
\]

Those sums occur only in numerator entries of the inverse.

## Published inverse recovered

Direct inversion gives

\[
M^{-1}
=
\begin{pmatrix}
-S_{12}S_{35}S_{45}
&
-S_{12}S_{45}\sin\pi(s_{34}+s_{35})
\\[2mm]
-S_{12}S_{35}\sin\pi(s_{34}+s_{45})
&
-S_{12}S_{35}S_{45}
\end{pmatrix},
\]

exactly matching the frozen source formula.

At a generic nonresonant point, the maximum inverse-entry error is

\[
1.11\times10^{-16},
\]

and the matrix-product error is

\[
2.22\times10^{-16}.
\]

The durable packet is at

research/benincasa/string-six-point-klt-block.json.

## Narrow result

The first mixed six-point block closes under the existing coefficient calculus:

\[
\boxed{
\text{Pochhammer local cells}
+
\text{four-point self-intersection sums}
+
\text{source kinematic relation}
\Longrightarrow
\text{published block inverse}.
}
\]

Neither a new carrier divisor nor a higher coherence correction appears. The mixed sine sums are numerator transport data, not new support.

## Scope boundary

This proves one \(2\times2\) block only. The complete six-point KLT matrix has three relabelled blocks and a nontrivial basis organization. Compatibility of the blockwise construction with all relabelling transitions is not yet established.

## Next falsifier

Assemble the complete source six-point block-diagonal kernel, derive the relabelling maps between its three \(2\times2\) blocks, and test cyclic/parity covariance. Any mismatch must be classified as orientation transport, coefficient monodromy, or genuinely missing coherence.
