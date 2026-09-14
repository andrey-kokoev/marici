# Trace-class localization makes transported regulator removal automatic

## Abstract compression lemma

Let `H` be a Hilbert space, let

\[
T\in\mathcal S_1(H)
\]

be trace class, and let `Z_r` be uniformly bounded operators satisfying

\[
Z_r
\xrightarrow[s]{r\to\infty}
I,
\]

\[
Z_r^*
\xrightarrow[s]{r\to\infty}
I.
\]

Then

\[
\boxed{
\|Z_rTZ_r^*-T\|_1
\longrightarrow0.
}
\]

In particular,

\[
\boxed{
\operatorname{Tr}(Z_rTZ_r^*)
\longrightarrow
\operatorname{Tr}(T).
}
\]

For increasing orthogonal projections, the uniform boundedness and adjoint conditions are automatic.

## Proof by finite-rank approximation

Fix `epsilon>0`. Choose a finite-rank operator `T_epsilon` such that

\[
\|T-T_\varepsilon\|_1
<\varepsilon.
\]

Uniform boundedness gives

\[
\|Z_r
(T-T_\varepsilon)
Z_r^*\|_1
\le
M^2\varepsilon,
\]

where

\[
M
=
\sup_r\|Z_r\|.
\]

On the finite-dimensional range and corange of `T_epsilon`, strong convergence is norm convergence. Hence

\[
\|Z_rT_\varepsilon Z_r^*-T_\varepsilon\|_1
\longrightarrow0.
\]

Combining the three terms and then sending `epsilon->0` proves the lemma.

## Transported regulators

Let

\[
Z_R^{physical}
\xrightarrow[s]{R\to\infty}
I
\]

be the exact physical outer regulators. For a unitary physical-to-Hardy map `U_chi`, define

\[
\widetilde Z_{R,\chi}
=
\mathcal U_\chi
Z_R^{physical}
\mathcal U_\chi^*.
\]

Then

\[
\boxed{
\widetilde Z_{R,\chi}
\xrightarrow[s]{R\to\infty}
I.
}
\]

No description of `widetilde Z` as a Mellin multiplier is required.

## Observer-sandwiched relative operator

For observer pair `g,h`, define on one angular fiber

\[
\boxed{
T_{L,\chi}(g,h)
=
M_{m_{h,\chi}}^*
\Pi
(Q_{L,\chi}^T-Q_L^0)
M_{m_{g,\chi}}.
}
\]

The exact left/right positions may be modified according to the finite cyclic trace placement; the argument applies to whichever transported operator is actually obtained.

If

\[
\boxed{
T_{L,\chi}(g,h)
\in
\mathcal S_1,
}
\]

then

\[
\boxed{
\left\|
\widetilde Z_{R,\chi}
T_{L,\chi}(g,h)
\widetilde Z_{R,\chi}
-
T_{L,\chi}(g,h)
\right\|_1
\to0.
}
\]

Thus outer-regulator removal is automatic in trace norm.

## Independence of cutoff-uniformity

For each fixed `L`, the compression lemma needs no estimate uniform in `L`. Therefore the iterated limit

\[
R\to\infty
\quad
\text{before}
\quad
L\to\infty
\]

is justified by characterwise trace class alone.

For a joint limit `R=R(L)`, one needs quantitative uniform trace-norm tails:

\[
\boxed{
\sup_{L\in\mathcal L}
\|(I-\widetilde Z_R)
T_L\|_1
+
\|T_L(I-\widetilde Z_R)\|_1
\longrightarrow0.
}
\]

Hence the exact order of regulator limits must be declared.

## Angular removal

At finite angular cutoff `N`, sum over finitely many characters. To remove `N`, a sufficient condition is

\[
\boxed{
\sum_\chi
\|T_{L,\chi}(g,h)\|_1
<\infty.
}
\]

Then

\[
T_{L,S}(g,h)
=
\bigoplus_\chi
T_{L,\chi}(g,h)
\]

is trace class and

\[
\boxed{
\operatorname{Tr}
T_{L,S}(g,h)
=
\sum_\chi
\operatorname{Tr}
T_{L,\chi}(g,h).
}
\]

Dominated convergence permits outer and angular regulator removal without changing observer placement.

## Conductor-filtered version

At fixed conductor level `F`, only finitely many angular character sectors occur for Bruhat--Schwartz observers modulo the chosen compact open subgroup. Therefore angular trace-norm summability is automatic after the characterwise `S_1` estimate.

The full conductor limit requires bounds such as

\[
\boxed{
\|T_{L,\chi}(g,h)\|_1
\le
C_N(g,h)
(1+\kappa_S(\chi))^{-N}
}
\]

for arbitrarily large `N`, or another summable majorant incorporating the conductor growth of the gamma derivative.

## Relative trace versus ordinary trace

The projection-pair formula is sometimes stated as a localized **relative trace** even when the operator written formally is not in `S_1`. In that case the compression lemma does not apply.

One must distinguish:

1. `T in S_1`, with ordinary trace independent of regulator;
2. a conditionally convergent diagonal integral;
3. a spectral-shift/relative trace defined after subtraction;
4. a semifinite trace-density pairing.

Only the first case gives automatic transported-regulator removal by the lemma.

## Schatten acceptance test

For the exact observer placement, prove a factorization

\[
\boxed{
T_{L,\chi}(g,h)
=X_{L,\chi}(h)^*
Y_{L,\chi}(g)
}
\]

with

\[
X_{L,\chi}(h),
Y_{L,\chi}(g)
\in
\mathcal S_2.
\]

Then

\[
\boxed{
\|T_{L,\chi}(g,h)\|_1
\le
\|X_{L,\chi}(h)\|_2
\|Y_{L,\chi}(g)\|_2.
}
\]

This is the cleanest route from observer-localized Hankel estimates to genuine trace-class regulator independence.

The observer must remain on both Gram legs. A factorization using one bare Hardy transition is invalid because that transition has infinite Hilbert--Schmidt norm.

## Natural two-sided factorization target

Using

\[
Q_{L,\chi}^T
=M_{\gamma_\chi}
Q_L^0
M_{\gamma_\chi}^*
\]

after common translation, write

\[
Q_{L,\chi}^T-Q_L^0
=
[M_{\gamma_\chi},
Q_L^0]
M_{\gamma_\chi}^*.
\]

A candidate is to split observer localization as

\[
M_{m_g}
=M_{a_g}M_{b_g}
\]

with rapidly decreasing square-root weights and place one factor on each side of the Hardy commutator.

The required theorem is not merely

\[
[Q_L^0,M_\gamma]
M_{m_g}
\in\mathcal S_2.
\]

It is a two-sided estimate sufficient to express the fully sandwiched relative operator as a product of two Hilbert--Schmidt factors.

## Trace formula after the criterion

If the `S_1` and angular summability criteria hold, then exact transported-regulator removal gives

\[
\boxed{
\lim_{R,N}
\operatorname{Tr}
\left(
\widetilde Z_{R,N}
T_{L,S}(g,h)
\widetilde Z_{R,N}
\right)
=
\operatorname{Tr}
T_{L,S}(g,h).
}
\]

The localized projection-pair identity then evaluates the right side as

\[
\boxed{
\sum_\chi
\frac1{2\pi i}
\int
\overline{m_{h,\chi}(s)}
m_{g,\chi}(s)
\partial_s
\log\gamma_\chi(s)ds
+
E_{end}(g,h).
}
\]

Thus the regulator comparison becomes a standard trace-ideal theorem.

## Endpoint caveat

An endpoint/winding index may not be represented by the ordinary trace of the regular `S_1` kernel alone. If the relative projection pair has nonzero Fredholm index, split

\[
\boxed{
T_{relative}
=T_{regular}
+
T_{index}
}
\]

where `T_regular in S_1` after observer localization and `T_index` is the finite-rank/index channel. The compression lemma applies separately to both.

This prevents branch winding from being lost by an overaggressive trace-class regularization.

## Exact remaining gate

The outer-regulator geometry is no longer mysterious. The remaining analytic assertion is:

\[
\boxed{
M_{m_h}^*
\Pi
(Q_{L,\chi}^T-Q_L^0)
M_{m_g}
\in
\mathcal S_1
}
\]

with a characterwise summable trace-norm majorant, after separating endpoint index terms.

If this holds, transported outer and angular regulator convergence follows formally.

## Disposition

Strongly convergent transported regulator projections satisfy

\[
\boxed{
\widetilde Z_R
T
\widetilde Z_R
\to T
\quad
\text{in }\mathcal S_1
}
\]

for every observer-localized trace-class relative operator `T`. Hence the sole analytic `C_34` regulator gate is a two-sided observer-localized Schatten factorization plus angular summability; no special geometric description of the transported regulator is needed.
