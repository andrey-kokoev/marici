# 1774 — The \(P_6\) Kummer Character Kills the Soft \(A_2\) Milnor Plane

## Question

Entry 1773 finds an ordinary rank-two \(A_2\) Milnor object at

\[
E_T=X_2=0.
\]

Does the source-defined algebraic coefficient line \(P_6^{-1/2}\) specialize
to a nonzero supported class there?

## Link presentation

The link of

\[
Z^2-U^3=0
\]

is the trefoil. With source-compatible orientation, take

\[
V=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\]

The Alexander presentation and polynomial are

\[
tV-V^T,
\qquad
\Delta(t)=\det(tV-V^T)=t^2-t+1.
\]

The Kummer line \(P_6^{-1/2}\) assigns character \(t=-1\) to a positive
meridian of the coefficient divisor. Therefore

\[
(-V-V^T)=
\begin{pmatrix}-2&1\\1&-2\end{pmatrix},
\qquad
\det=3.
\]

This matrix is invertible over characteristic zero. Degree-zero invariants
also vanish because the character is nontrivial. Hence the twisted local link
cohomology is acyclic:

\[
\boxed{H^\bullet(\operatorname{Link}_{A_2};\mathcal L_{-1})=0.}
\]

## Consequence

The source Kummer line selects neither one nor both of the ordinary \(A_2\)
Milnor directions. The rank-two Milnor algebra in Entry 1773 is real
coefficient-divisor geometry, but it does not produce a supported class in
the \(P_6^{-1/2}\) sector.

This closes the algebraic Kummer contribution at the generic
total-energy/site-soft cusp. It does not rule out contributions from other
coefficient blocks or from a separately supplied physical relative chain.

## Durable evidence

- `research/benincasa/checkers/p6_soft_cusp_kummer.py`
- `research/benincasa/results/p6-soft-cusp-kummer.json`
- `research/benincasa/p6-soft-cusp-kummer.md`
- allocator claim: `seqclaim-31bed6048c0b0a1a7efce3e8`

