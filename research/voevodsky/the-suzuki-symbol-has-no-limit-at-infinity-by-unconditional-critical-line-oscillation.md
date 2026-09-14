# The Suzuki symbol has no limit at infinity by unconditional critical-line oscillation

## Real-axis normal form

Put

\[
X(x)=\xi(1/2-ix).
\]

By the functional equation and conjugation symmetry, `X(x)` is real for real `x`. Differentiating with respect to `x` gives

\[
X'(x)=-i\xi'(1/2-ix),
\qquad
\xi'(1/2-ix)=iX'(x).
\]

Suzuki's de Branges candidate therefore has boundary values

\[
E(x)=X(x)+iX'(x),
\qquad
E^\#(x)=X(x)-iX'(x),
\]

and

\[
\boxed{
\Theta(x)=\frac{X(x)-iX'(x)}{X(x)+iX'(x)}.
}
\]

This proves `|Theta(x)|=1` wherever the quotient is defined, without RH.

## Values at zeros and stationary points

At a simple real zero `gamma` of `X`,

\[
\Theta(\gamma)=-1.
\]

The same limiting value holds at a zero of any finite multiplicity: near a zero, the derivative term dominates the function term in the quotient after cancelling the common vanishing order.

At a real stationary point `c` with

\[
X'(c)=0,
\qquad X(c)\ne0,
\]

one has

\[
\Theta(c)=1.
\]

## Unconditional oscillation at arbitrarily large height

It is a classical unconditional theorem that zeta has infinitely many nontrivial zeros on the critical line. Hence `X` has an unbounded sequence of distinct real zeros

\[
\gamma_1<\gamma_2<\cdots.
\]

Choose consecutive distinct zeros. On the open interval between them, `X` has no zero. Rolle's theorem supplies a point `c_n` with

\[
X'(c_n)=0.
\]

Because there is no zero in the open interval,

\[
X(c_n)\ne0.
\]

Therefore there are unbounded sequences satisfying

\[
\Theta(\gamma_n)=-1,
\qquad
\Theta(c_n)=1.
\]

It follows that

\[
\boxed{
\lim_{x\to+\infty}\Theta(x)
\text{ does not exist}.
}
\]

By even/conjugate symmetry, the same obstruction occurs at the opposite end.

## Consequence for compact-Hankel tests

The symbol does not belong to the algebra of continuous functions on the one-point compactification of the real line. Thus the simplest route to Hartman compactness--treating `Theta` itself as a continuous compactified boundary symbol--is unavailable.

This does **not** prove that the associated Hankel leakage is noncompact. Hartman's criterion is modulo the analytic Hardy algebra: a symbol may fail to be continuous while still belong to

\[
H^\infty+C
\]

through cancellation by an analytic component. The result only rules out the naive `Theta in C(dot R)` argument.

## Phase interpretation

Writing

\[
\Theta(x)=e^{-2i\arctan(X'(x)/X(x))}
\]

away from zeros shows that every critical-line zero forces the boundary phase through `-1`, while every intervening real extremum returns it to `+1`. The oscillation is not an artifact of unknown off-axis zeros; it is forced by the already-known infinite critical-line divisor.

Accordingly, any compactness proof must absorb infinitely many phase turns into the analytic `H^infinity` summand. This is a substantially stronger approximation problem than decay or smoothness of the raw symbol.

## Relation to finite-rank leakage

A finite-rank Hankel compression would require the nonanalytic part of the symbol to be rational in the appropriate half-plane sense. The persistent alternating values do not alone disprove rationality modulo analytic functions, but they make a direct rational boundary model implausible. A rigorous infinite-rank proof should exhibit arbitrarily many linearly independent shifted negative-frequency components, or invoke a precise Kronecker theorem after identifying the linear Hankel symbol.

## Revised next test

The first nonredundant analytic question is no longer whether `Theta` is continuous at infinity; it is not. It is whether there exists `h in H^infinity(C_+)` such that

\[
\Theta-h
\]

has a continuous compactified boundary representative. Equivalently, determine whether `Theta` belongs to `H^infinity+C(dot R)` under the exact half-plane Hartman theorem.

A negative answer proves noncompact leakage. A positive answer, combined with an infinite-rank argument, proves nonclosed range and rules out the coercive pseudoinverse construction.

## Disposition

The completed-zeta boundary symbol has unconditional large-height phase oscillation:

\[
\boxed{
\Theta(\gamma_n)=-1,
\qquad
\Theta(c_n)=1,
\qquad
\gamma_n,c_n\to\infty.
}
\]

Therefore it has no boundary limit at infinity and cannot enter compact-Hankel theory through raw continuity. Only the subtler analytic-modulo-continuous Hartman class remains open.
