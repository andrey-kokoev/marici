# Correction: the relative projection-trace formula does not directly evaluate the left-Hardy-compressed product

## Two different relative operators

Let

\[
\Delta Q_L
=Q_L^T-Q_L^0.
\]

The standard localized projection-pair formula evaluates

\[
\boxed{
\operatorname{Tr}_{rel}
(M_f\Delta Q_L)
=
\frac1{2\pi i}
\int
f(s)
\partial_s
\log\gamma(s)ds
+
e_{end}(f).
}
\]

Connes's transported ordered product contains instead

\[
\boxed{
\operatorname{Tr}
(M_f\Pi\Delta Q_L)
}
\]

or its exactly transported asymmetric observer variant.

These are not the same operator or trace.

## Invalid inference being withdrawn

A previous argument established that two-sided observer localization can make

\[
M_{m_h}^*
\Pi\Delta Q_L
M_{m_g}
\]

trace class. It then asserted that its trace is obtained by integrating the diagonal divided difference of `Delta Q_L`.

That assertion is invalid. The kernel of

\[
\Pi\Delta Q_L
\]

is a composition kernel

\[
(\Pi\Delta Q_L)(s,t)
=
\int
\Pi(s,u)
\Delta q_L(u,t)du,
\]

not `Delta q_L(s,t)`. Its diagonal contains an additional Hardy singular-integral contribution.

Trace-class membership does not identify its trace with the uncompressed relative projection trace.

## Exact algebraic split

Let

\[
J_\Pi
=2\Pi-I
\]

be the Hardy reflection. Then

\[
\Pi
=
\frac12
(I+J_\Pi).
\]

Therefore

\[
\boxed{
\Pi\Delta Q_L
=
\frac12
\Delta Q_L
+
\frac12
J_\Pi\Delta Q_L.
}
\]

After exact observer localization,

\[
\boxed{
\begin{aligned}
\operatorname{Tr}
(M_f\Pi\Delta Q_L)
&=
\frac12
\operatorname{Tr}_{rel}
(M_f\Delta Q_L)\\
&\quad+
\frac12
\operatorname{Tr}
(M_fJ_\Pi\Delta Q_L),
\end{aligned}
}
\]

provided both regularized terms are defined in the same cyclic placement.

The first term is the Tate logarithmic derivative. The second is the unresolved Hardy-placement correction.

## Placement correction

Define

\[
\boxed{
\mathcal P_L(f)
=
\frac12
\operatorname{Tr}
(M_fJ_\Pi\Delta Q_L).
}
\]

Then

\[
\boxed{
\operatorname{Tr}
(M_f\Pi\Delta Q_L)
=
\frac1{4\pi i}
\int
f\partial_s\log\gammads
+
\frac12e_{end}(f)
+
\mathcal P_L(f).
}
\]

To recover the full Tate coefficient, one would need

\[
\mathcal P_L(f)
=
\frac1{4\pi i}
\int
f\partial_s\log\gammads
+
\frac12e_{end}(f),
\]

not merely `P_L(f)->0`.

Alternatively, a different orientation/cyclic observer placement may move the full projection difference into the trace. That must be demonstrated algebraically, not inferred from the scalar relative formula.

## Finite-dimensional sanity check

Take finite-dimensional projections `Pi,Q_T,Q_0`. In general,

\[
\operatorname{Tr}
(Q_T-Q_0)
\ne
\operatorname{Tr}
(\Pi(Q_T-Q_0)).
\]

For example, with

\[
\Pi
=
\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
\Delta Q
=
\begin{pmatrix}a&b\\\bar b&-a\end{pmatrix},
\]

one has

\[
\operatorname{Tr}(\Delta Q)=0,
\qquad
\operatorname{Tr}(\Pi\Delta Q)=a.
\]

Thus no universal factor relates the two traces.

## Relation to eight-leg dilation

The eight-leg feature correctly realizes the Hermitian part

\[
\frac12
(\Pi\Delta Q_L
+
\Delta Q_L\Pi).
\]

Its signed trace equals the real part of the ordered compressed product. This exact positive realization remains valid.

What is withdrawn is the claim that the eight-leg readout is automatically evaluated by the standard uncompressed projection-pair formula.

The eight-leg feature solves typing and placement representation; it does not solve the placement trace calculation.

## Relation to the anti-Hermitian channel

Reality of Connes's limiting ordered trace still implies that the anti-Hermitian channel vanishes **if** the transported ordered product is already known to converge to the Hermitian Weil value.

But the uncompressed relative projection formula alone does not establish that premise.

Therefore the earlier anti-Hermitian conclusion remains a conditional implication, not an independent proof of ordered regulator convergence.

## Trace-class status

The two-sided Schwartz argument may still prove

\[
M_{m_h}^*
\Pi\Delta Q_L
M_{m_g}
\in
\mathcal S_1.
\]

This is useful because it makes the placement correction an ordinary regulator-independent trace.

However, one must compute that trace or compare it with Connes's orbit-volume expression. Trace-class membership alone supplies neither its value nor its asymptotic.

## Correct remaining scalar gate

The actual scalar comparison is

\[
\boxed{
\operatorname{Tr}
(M_{m_h}^*
\Pi\Delta Q_L
M_{m_g})
\stackrel{?}{=}
W_S(g*h^*)
+
o(1),
}
\]

with exact transported regulators and endpoint conventions.

Equivalently, compute the placement correction `P_L(g,h)` and show that it supplies the missing half of the Tate relative trace, or identify the precise alternative coefficient dictated by Connes's product theorem.

## Correction to centered scalar closure

The earlier statement that

\[
\text{centered Connes cutoff form}
\to
W_S
=
\text{centered Tate--Hardy relative form}
\]

is valid as equality of their separately sourced scalar limits only after proving that the ordered physical regulator corresponds to the uncompressed relative form or after evaluating the placement correction.

The local Tate distribution identity identifies `W_S` with the uncompressed projection-pair trace. Connes's theorem identifies `W_S` with the physical ordered cutoff finite part. Equality of limits does not itself provide equality of the intermediate transported operators.

## Revised status table

| Statement | Status |
|---|---|
| uncompressed localized relative trace equals `d log gamma` | established under admitted projection-pair formula |
| exact finite physical regulator transports to left-compressed Hardy product | established algebraically |
| left-compressed localized operator is trace class | plausible/proved under Schwartz regularity assumptions |
| trace of left-compressed operator equals uncompressed relative trace | false in general |
| Hardy-placement correction has required Tate value | open |
| anti-Hermitian channel vanishes if ordered limit is Hermitian | valid conditional implication |

## Acceptance routes

One of the following is required:

### Direct Hardy calculation

Compute

\[
\operatorname{Tr}
(M_fJ_\Pi\Delta Q_L)
\]

from the divided-difference kernel and identify its endpoint contribution.

### Orbit-volume comparison

Transport Connes's geometric orbit-volume defect characterwise and prove it equals the placement correction plus half the uncompressed Tate trace.

### Exact cyclic reformulation

Find a source-valid trace cyclicity/factorization that converts the physical ordered product into an uncompressed relative projection trace with observer localization on both sides.

The last route cannot move `Pi` through the observer multiplier without paying its commutator.

## Disposition

The projection-pair formula computes `Tr_rel(M_f Delta Q)`, while the exact transported Connes placement is `Tr(M_f Pi Delta Q)`. Their difference is the explicit Hardy-reflection trace

\[
\boxed{
\mathcal P_L(f)
=
\frac12
\operatorname{Tr}
(M_f(2\Pi-I)\Delta Q_L).
}
\]

This placement term is the remaining scalar `C_34` gate. Previous claims of complete centered scalar sewing or automatic trace evaluation must be read as conditional on its calculation.
