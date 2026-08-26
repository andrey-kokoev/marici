# Theta distinguished-output barrier collapses to homogeneous scalar closure

## Status

Exact finite-dimensional control no-go. A quadratic barrier whose zero set is
exactly the kernel of the distinguished scalar readout can be invariant under
ambient linear dynamics only when that readout kernel is itself invariant.

Equivalently, the readout covector must evolve by a scalar homogeneous law.
Unless this law is independently derived from the theta source, the barrier is
only another form of the already rejected zero-free scalar closure.

## State and distinguished output

Let the resolved finite state satisfy

\[
\dot x=A(t)x
\]

and let the distinguished scalar output be

\[
y=u(t)^*x.
\]

The canonical nonnegative output barrier is

\[
b=x^*Hx,
\qquad
H=uu^*.
\]

Then

\[
b=|y|^2,
\qquad
\ker H=\ker u^*.
\]

## Lyapunov barrier gate

Suppose one seeks a differential inequality

\[
\dot b\geq-\kappa b
\]

for all ambient states, with locally bounded real \(\kappa\). In matrix form
this requires

\[
K=\dot H+A^*H+HA+\kappa H\geq0.
\]

Take any (v\in\ker H\). Since (Hv=0\),

\[
v^*Kv=0.
\]

For a positive semidefinite matrix, zero quadratic form implies

\[
Kv=0.
\]

Using (Hv=0\) leaves

\[
(\dot H+HA)v=0.
\]

Because (H=uu^*\), this condition is equivalent to preservation of the
moving readout kernel. Hence there is a scalar function \(\alpha(t)\) such that

\[
\dot u^*+u^*A=\alpha u^*.
\]

Along every solution,

\[
\dot y=\alpha y.
\]

The barrier certificate has collapsed to homogeneous scalar closure.

## Fixed-readout specialization

When (u) is fixed, the condition becomes

\[
u^*A=\alpha u^*.
\]

Thus the distinguished readout must be a left eigen-covector of the state
generator. Equivalently,

\[
A(\ker u^*)\subseteq\ker u^*.
\]

Any dynamics that mixes a hidden state into the observed direction violates
the ambient rank-one barrier inequality.

## Affine forcing

For

\[
\dot x=Ax+f,
\]

the output obeys

\[
\dot y=u^*Ax+u^*f.
\]

At a state with (y=0\), a source term with (u^*f\neq0\) crosses the readout
kernel. To obtain a homogeneous barrier one must either require

\[
u^*f=0
\]

on the zero-output locus or adjoin a constant source channel and prove kernel
invariance in the augmented state space. The latter again yields homogeneous
closure for the augmented scalar output.

## Why first-order boundary tests miss the issue

For (b=|y|^2\),

\[
\dot b=2\operatorname{Re}(\overline y\dot y).
\]

At (y=0\), this derivative vanishes for every \(\dot y\). Therefore a mere
Nagumo-style first derivative check at the barrier boundary is vacuous: a
trajectory can cross (y=0\) with quadratic contact in (b\).

The useful inequality must hold in a neighborhood, and that stronger condition
forces the kernel-invariance result above.

## Equivalent scalar inequality

On a connected path, an estimate

\[
|\dot y|\leq C|y|
\]

with locally integrable (C) prevents a nonzero initial value from reaching
zero. But for (y\neq0\) it is exactly a bound on

\[
\frac{\dot y}{y}.
\]

Near a zero this quotient diverges unless the closure has already removed the
zero. Therefore deriving such an estimate from the completed scalar section is
circular. It is admissible only if the state-level source construction supplies
the bounded coefficient before scalar projection.

## Minimal finite falsifier

Let

\[
u^*=\begin{pmatrix}1&0\end{pmatrix},
\qquad
A=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]

Then (v=(0,1)^T\) lies in \(\ker u^*\), but

\[
u^*Av=1.
\]

The hidden state immediately enters the distinguished output. No ambient
rank-one Lyapunov barrier with zero set \(\ker u^*\) can exist.

This two-state shear is the finite falsifier for any proposed output-barrier
law.

## Surviving route

The no-go applies to an ambient barrier on the full state space. A genuinely
new theorem may still exist if the theta source constructs a strict admissible
submanifold or cone \(\mathcal O\) such that

\[
\mathcal O\cap\ker u^*=\varnothing
\]

away from the seam. That is an orbit-restriction theorem, not a generic
Lyapunov barrier.

Its source authority must include:

- construction of \(\mathcal O\) before scalar projection;
- invariance of \(\mathcal O\) under completed primal-dual Poisson dynamics;
- disjointness from the readout kernel;
- failure on hostile self-Fourier carriers;
- stability under infinite-label completion.

## Consequence

Control theory sharpens the remaining choice. Either theta supplies a
source-specific restricted orbit disjoint from the readout kernel, or every
ambient distinguished-output barrier reduces to the RH-equivalent homogeneous
scalar equation. The next search should therefore target the admitted orbit,
not another quadratic energy on the full reconstructed state space.
