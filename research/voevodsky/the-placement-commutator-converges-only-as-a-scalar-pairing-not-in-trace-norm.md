# The placement commutator converges only as a scalar pairing, not in trace norm

## The remaining term

After recentering the Tate/reference difference, the placement remainder is

\[
\mathcal C_L(g,h)
=
\operatorname{Tr}
\left(
[M_{m_h}^*,\Pi_L]
\Delta Q_0M_{m_g}
\right).
\]

Writing the two factors as Hilbert--Schmidt kernels produces

\[
\mathcal C_L(g,h)
=
\iint e^{-2iL(s-t)}
K_h(s,t)\overline{R_g(s,t)}\,dsdt.
\]

Since \(K_h\overline{R_g}\in L^1\), Riemann--Lebesgue proves

\[
\mathcal C_L(g,h)\to0.
\]

This is scalar convergence of the trace pairing.

## Why it is not trace-norm convergence

Oscillatory unitary conjugation does not reduce Schatten norms. In particular, let \(u,v\) be nonzero vectors and let

\[
T_L=|U_Lu\rangle\langle v|,
\]

where \(U_L\) is a modulation or translation unitary. Then

\[
\|T_L\|_1=\|u\|\,\|v\|
\]

for every \(L\), while

\[
\operatorname{Tr}(T_L)
=\langle v,U_Lu\rangle\to0
\]

under the usual Riemann--Lebesgue hypotheses.

Thus an oscillatory trace may vanish while the operator has no trace-norm limit at all.

The same obstruction applies to the placement commutator unless additional compactness forces its complete singular-value mass to vanish.

## Correct completion level

The currently available argument establishes

\[
\boxed{
\operatorname{Tr}
\left(
M_{m_h}^*\Pi_L\Delta Q_0M_{m_g}
\right)
\longrightarrow
\operatorname{Tr}
\left(
M_{m_h}^*\Delta Q_0M_{m_g}
\right).
}
\]

It does **not** establish

\[
M_{m_h}^*\Pi_L\Delta Q_0M_{m_g}
\longrightarrow
M_{m_h}^*\Delta Q_0M_{m_g}
\quad\text{in }\mathcal S_1.
\]

Accordingly, the minimal physical completion presently constructed is a completed scalar bilinear sewing form, not a trace-class operator-valued product limit.

## Two ways to obtain a genuine product completion

A trace-norm product theorem would require one of the following stronger inputs.

### Norm-small placement remainder

Prove a factorization

\[
R_L=X_L^*Y_L
\]

with

\[
\|X_L\|_2\|Y_L\|_2\to0.
\]

The known factors have cutoff-independent Hilbert--Schmidt norms, so oscillation alone does not provide this.

### Quotient completion

Place oscillatory translates in a quotient or weak trace module that identifies weakly vanishing translation orbits. The scalar trace functional then descends, but the result is no longer ordinary \(\mathcal S_1\)-norm completion.

## Angular assembly of the scalar limit

Characterwise scalar convergence remains sufficient after summation. If

\[
|\mathcal C_{L,\chi}(g,h)|
\le
\|[M_{m_{h,\chi}},\Pi]\|_2
\|\Delta Q_{0,\chi}M_{m_{g,\chi}}\|_2
\]

and the right side is summable in \(\chi\), dominated convergence gives

\[
\sum_\chi\mathcal C_{L,\chi}(g,h)\to0.
\]

The phase-energy majorant supplies the second factor; the standard Hardy commutator energy and Schwartz angular decay supply the first.

## Revised status

- Positive relative difference feature: strong Hilbert--Schmidt completion is closed.
- Signed scalar sewing cell: completed by trace pairing and angular dominated convergence.
- Ordinary trace-class product operator: not completed by the existing oscillatory argument.

The first genuinely missing estimate for an operator-valued product completion is trace-norm smallness of the placement remainder, not merely Riemann--Lebesgue decay of its trace.
