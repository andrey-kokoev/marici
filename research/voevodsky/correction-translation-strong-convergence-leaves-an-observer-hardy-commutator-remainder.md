# Correction: translation strong convergence leaves an observer--Hardy commutator remainder

## Overstated argument

A proposed placement proof rewrote

\[
\operatorname{Tr}
(M_{m_h}^*
\Pi_L
\Delta Q_0
M_{m_g})
\]

and attempted to use

\[
\Pi_L
\xrightarrow[s]I
\]

directly against the trace-class sandwich

\[
T_{g,h}
=M_{m_h}^*
\Delta Q_0
M_{m_g}.
\]

But `Pi_L` lies between the left observer multiplier and `Delta Q_0`. It is not an exterior factor of `T_(g,h)`.

Strong convergence cannot be moved through `M_(m_h)^*` without a commutator.

## Exact commutator decomposition

Use

\[
M_{m_h}^*
\Pi_L
=
\Pi_L
M_{m_h}^*
+
[M_{m_h}^*,\Pi_L].
\]

Therefore

\[
\boxed{
\begin{aligned}
&M_{m_h}^*
\Pi_L
\Delta Q_0
M_{m_g}\\
&
=
\Pi_L
\left(
M_{m_h}^*
\Delta Q_0
M_{m_g}
\right)
+
[M_{m_h}^*,\Pi_L]
\Delta Q_0
M_{m_g}.
\end{aligned}
}
\]

Taking traces gives

\[
\boxed{
\begin{aligned}
&\operatorname{Tr}
(M_{m_h}^*
\Pi_L
\Delta Q_0
M_{m_g})\\
&
=
\operatorname{Tr}(\Pi_L T_{g,h})
+
\mathcal C_L(g,h),
\end{aligned}
}
\]

where

\[
\boxed{
\mathcal C_L(g,h)
=
\operatorname{Tr}
\left(
[M_{m_h}^*,\Pi_L]
\Delta Q_0
M_{m_g}
\right).
}
\]

## Exterior term

The two-sided Schwartz theorem gives

\[
T_{g,h}
\in
\mathcal S_1.
\]

Hence strong convergence of `Pi_L` implies

\[
\boxed{
\operatorname{Tr}(\Pi_LT_{g,h})
\longrightarrow
\operatorname{Tr}(T_{g,h}).
}
\]

This part of the translation argument is valid.

## Remaining commutator term

The placement theorem is therefore equivalent to

\[
\boxed{
\mathcal C_L(g,h)
\longrightarrow0.
}
\]

This does not follow from trace-class membership of `T_(g,h)` alone.

The commutator is observer-localized and Hilbert--Schmidt under the standard Hardy estimate, while

\[
\Delta Q_0M_{m_g}
\]

is also expected to be Hilbert--Schmidt. Thus the product is trace class and

\[
\boxed{
|\mathcal C_L(g,h)|
\le
\|[M_{m_h}^*,\Pi_L]\|_2
\|\Delta Q_0M_{m_g}\|_2.
}
\]

However, the first Hilbert--Schmidt norm need not tend to zero merely because `Pi_L->I` strongly. Strong convergence is not Hilbert--Schmidt convergence.

## Translation of the commutator

Since

\[
\Pi_L
=U_L^*\PiU_L
\]

and observer multipliers commute with `U_L`,

\[
\boxed{
[M_{m_h}^*,\Pi_L]
=
U_L^*
[M_{m_h}^*,\Pi]
U_L.
}
\]

Therefore

\[
\|[M_{m_h}^*,\Pi_L]\|_2
=
\|[M_{m_h}^*,\Pi]\|_2.
\]

Its Hilbert--Schmidt norm is constant in `L`, not decaying.

Any vanishing of `C_L` must come from relative translation/oscillation against `Delta Q_0 M_(m_g)`, not norm decay of the commutator alone.

## Trace pairing form

By unitary conjugation and cyclicity in the Hilbert--Schmidt pairing,

\[
\mathcal C_L(g,h)
=
\left\langle
[M_{m_h},\Pi_L],
\Delta Q_0M_{m_g}
\right\rangle_{HS}
\]

up to adjoint/sign convention.

Thus `C_L->0` is a weak-mixing statement: a translated Hardy commutator must converge weakly to zero against the fixed observer-localized relative projection block.

## Compactness route

If

\[
[M_{m_h},\Pi]
\in
\mathcal S_2
\]

and conjugation by `U_L` sends it weakly to zero in `S_2`, then

\[
\mathcal C_L(g,h)
\to0.
\]

A sufficient condition is that both Hilbert--Schmidt kernels are in `L2(R^2)` and the modulation

\[
e^{2iL(s-t)}
\]

has no stationary component on a positive-measure diagonal set. The diagonal has measure zero in `R^2`, so the Riemann--Lebesgue lemma can apply to their `L1` kernel product.

## Kernel oscillation

The translated commutator kernel is

\[
\boxed{
[M_{m_h},\Pi_L](s,t)
=
e^{-2iL(s-t)}
[M_{m_h},\Pi](s,t)
}
\]

with sign determined by the translation convention.

Hence

\[
\mathcal C_L(g,h)
\]

is an oscillatory integral of the form

\[
\boxed{
\iint
 e^{-2iL(s-t)}
K_h(s,t)
\overline{R_g(s,t)}dsdt.
}
\]

Since `K_h,R_g in L2`, their product lies in `L1` by Cauchy--Schwarz. The Riemann--Lebesgue lemma in the variable `s-t` then gives

\[
\boxed{
\mathcal C_L(g,h)
\longrightarrow0,
}
\]

provided `R_g` is independent of `L` after the common translation has been conjugated out.

This supplies the missing argument under the declared Hilbert--Schmidt hypotheses.

## Exact sufficient hypotheses

The corrected translation theorem holds if:

1. `T_(g,h)=M_(m_h)^* Delta Q_0 M_(m_g) in S_1`;
2. `[M_(m_h),Pi] in S_2`;
3. `Delta Q_0 M_(m_g) in S_2`;
4. the common cutoff translation has been completely removed from `Delta Q_0`;
5. the kernel product is measured in the same Hardy coordinates.

Then

\[
\boxed{
\operatorname{Tr}
(M_{m_h}^*
\Pi_L
\Delta Q_0
M_{m_g})
\longrightarrow
\operatorname{Tr}
(M_{m_h}^*
\Delta Q_0
M_{m_g}).
}
\]

## Status of the Hilbert--Schmidt factors

For Schwartz observer multipliers:

\[
[M_{m_h},\Pi]
\in
\mathcal S_2
\]

by the standard `H^(1/2)` Hardy commutator criterion.

The second factor

\[
\Delta Q_0M_{m_g}
\]

has kernel equal to a smooth polynomially controlled divided difference times a Schwartz function in the right variable. It is Hilbert--Schmidt under the observer-localized Hankel estimate already used in the characterwise analysis.

Thus the oscillatory `L1` product criterion is available on the Bruhat--Schwartz observer core.

## Angular summation

At fixed conductor level, sum finitely many character sectors. For infinite smooth angular support, dominate

\[
|\mathcal C_{L,\chi}(g,h)|
\]

by the product of the two Hilbert--Schmidt norms. Rapid observer angular decay and polynomial gamma bounds make this summable.

Dominated convergence then yields

\[
\sum_\chi
\mathcal C_{L,\chi}(g,h)
\to0.
\]

## Correction to the previous note

The earlier claim that strong convergence of `Pi_L` alone proves placement convergence is withdrawn. The valid proof has two steps:

\[
\boxed{
\text{trace-class exterior term}
+
\text{Riemann--Lebesgue commutator term}.
}
\]

The final placement conclusion survives under the stated two Hilbert--Schmidt estimates, but it is not a consequence of strong convergence alone.

## Disposition

The exact remainder is

\[
\boxed{
\mathcal C_L(g,h)
=
\operatorname{Tr}
([M_{m_h}^*,\Pi_L]
\Delta Q_0M_{m_g}).
}
\]

Its factors are Hilbert--Schmidt on the Schwartz observer core, and its kernel pairing acquires the modulation `e^(-2iL(s-t))`. Riemann--Lebesgue therefore gives `C_L->0`. This repairs the placement proof while retaining the conclusion in the iterated regulator model.
