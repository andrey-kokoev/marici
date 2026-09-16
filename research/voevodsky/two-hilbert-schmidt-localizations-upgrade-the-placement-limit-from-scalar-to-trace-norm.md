# Two Hilbert--Schmidt localizations upgrade the placement limit from scalar to trace norm

## The missing compactness mechanism

The placement remainder has the operator form

\[
R_L
=
[M_{m_h}^*,\Pi_L]\,
\Delta Q_0M_{m_g}.
\]

Set

\[
K=[M_{m_h}^*,\Pi]\in\mathcal S_2,
\qquad
H=\Delta Q_0M_{m_g}\in\mathcal S_2.
\]

Since observer multipliers commute with the Mellin modulation \(U_L\),

\[
[M_{m_h}^*,\Pi_L]
=U_L^*KU_L.
\]

Therefore

\[
R_L=U_L^*KU_LH
\]

and unitary invariance gives

\[
\|R_L\|_1=\|KU_LH\|_1.
\]

The earlier oscillatory-trace argument used only the scalar pairing. The second Hilbert--Schmidt localization supplies enough compactness for trace-norm convergence.

## Compact sandwich lemma

Let \(U_L\) be a uniformly bounded family converging weakly to zero on a Hilbert space. If

\[
K,H\in\mathcal S_2,
\]

then

\[
\boxed{\|KU_LH\|_1\longrightarrow0.}
\]

### Proof

Choose finite-rank approximations \(K_0,H_0\) in Hilbert--Schmidt norm. Schatten Hölder gives, uniformly in \(L\),

\[
\begin{aligned}
\|KU_LH-K_0U_LH_0\|_1
&\le
\|(K-K_0)U_LH\|_1
+
\|K_0U_L(H-H_0)\|_1\\
&\le
\|K-K_0\|_2\|H\|_2
+
\|K_0\|_2\|H-H_0\|_2.
\end{aligned}
\]

This error can be made arbitrarily small independently of \(L\).

For finite-rank \(K_0,H_0\), the operator \(K_0U_LH_0\) acts between fixed finite-dimensional spaces. Every matrix coefficient tends to zero by weak convergence of \(U_L\), hence every norm on that finite-dimensional operator space tends to zero, including trace norm. Combining the two statements proves the lemma.

## Weak decay of Mellin modulation

On \(L^2(\mathbb R)\),

\[
(U_Lf)(s)=e^{2iLs}f(s).
\]

For \(f,g\in L^2\), the product \(f\overline g\) lies in \(L^1\), so Riemann--Lebesgue gives

\[
\langle g,U_Lf\rangle
=
\int e^{2iLs}f(s)\overline{g(s)}ds
\longrightarrow0.
\]

Thus \(U_L\rightharpoonup0\).

## Placement consequence

Applying the compact sandwich lemma yields

\[
\boxed{
\|[M_{m_h}^*,\Pi_L]
\Delta Q_0M_{m_g}\|_1
\longrightarrow0.
}
\]

Hence the placement decomposition improves from scalar convergence to operator trace-norm convergence, provided both declared Hilbert--Schmidt estimates hold.

The exterior term also converges in trace norm. Indeed, if

\[
T_{g,h}=M_{m_h}^*\Delta Q_0M_{m_g}\in\mathcal S_1
\]

and \(\Pi_L\to I\) strongly, then

\[
\|(I-\Pi_L)T_{g,h}\|_1\to0.
\]

Therefore

\[
\boxed{
M_{m_h}^*\Pi_L\Delta Q_0M_{m_g}
\longrightarrow
M_{m_h}^*\Delta Q_0M_{m_g}
\quad\text{in }\mathcal S_1.
}
\]

## Angular assembly

Suppose

\[
\|R_{L,\chi}(g,h)\|_1
\le
\|K_{h,\chi}\|_2\|H_{g,\chi}\|_2
\]

and the right side is summable in \(\chi\). Characterwise trace-norm convergence plus dominated summation gives

\[
\sum_\chi\|R_{L,\chi}(g,h)\|_1\to0.
\]

The Hardy commutator energy controls \(K_{h,\chi}\); the Tate phase-energy estimate controls \(H_{g,\chi}\). Schwartz angular decay supplies the summable majorant.

## Why the rank-one hostile example does not apply

A family \(|U_Lu\rangle\langle v|\) has constant trace norm, but it contains only a translated left factor. The physical remainder has the stronger compact sandwich form

\[
U_L^*KU_LH.
\]

The fixed compact right localization \(H\) converts weak translation decay into norm decay. Omitting it changes the operator being tested.

## Completion

Under the already recorded two Hilbert--Schmidt estimates and angular majorant, the minimal product route is an ordinary trace-class operator completion, not merely a scalar trace completion. The remaining source bookkeeping is to verify that the exact transported physical placement has precisely this compact-sandwich form in every endpoint and conductor channel.
