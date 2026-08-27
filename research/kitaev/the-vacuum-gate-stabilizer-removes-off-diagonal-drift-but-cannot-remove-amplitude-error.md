# The vacuum-gate stabilizer removes off-diagonal drift but cannot remove amplitude error

Owner: `marici.Kitaev`

## Bounded question

Can a subgroup of the finite braid-plus-cube-root gate set dynamically
decouple errors while preserving continuous evolution under the native vacuum
projector?

Partially. The target projector has an 18-element stabilizer inside
`G(3,1,3)`, of projective order six. Its uniform twirl removes every error
coupling among three distinguished one-dimensional subspaces, but leaves the
full diagonal algebra on those subspaces. In particular it cannot remove a
timing or amplitude fault proportional to the commanded projector.

The surviving fault is not an accident of the chosen group. Command and
multiplicative amplitude error have the same Hamiltonian direction, so any
frame that preserves the command also preserves that error.

## Target line and complementary frame

Use the monomial qutrit basis

\[
|q_0\rangle,
\qquad
|q_1\rangle,
\qquad
|q_2\rangle.
\]

The vacuum fusion projector is

\[
P_v=|v\rangle\langle v|,
\]

where

\[
|v\rangle
=
{|q_1\rangle+|q_2\rangle\over\sqrt2}.
\]

Define its orthogonal partner inside the same coordinate plane by

\[
|w\rangle
=
{|q_1\rangle-|q_2\rangle\over\sqrt2}.
\]

Then

\[
\{|q_0\rangle,|v\rangle,|w\rangle\}
\]

is an orthonormal basis.

## Exact finite stabilizer

Every element of `G(3,1,3)` is a monomial matrix

\[
g
=
\operatorname{diag}
(\omega^{a_0},\omega^{a_1},\omega^{a_2})P_\sigma.
\]

For `g` to preserve the line spanned by `v`, its permutation must preserve the
support set `{q_1,q_2}`. Therefore

\[
\sigma\in\{e,(12)\}.
\]

The two phases on that support must agree:

\[
a_1=a_2.
\]

The phase on `q_0` is independent. Hence the stabilizer is

\[
K_v
=
\left{
\operatorname{diag}(\alpha_0,\alpha,\alpha)P_\sigma
:
\alpha_0^3=\alpha^3=1,
\quad
\sigma\in\{e,(12)\}
\right}.
\]

Its order is

\[
3\cdot3\cdot2=18.
\]

After quotienting the common cube-root phase, its projective order is six.

Every element satisfies

\[
gP_vg^\dagger=P_v.
\]

Therefore frame changes from `K_v` preserve the desired vacuum Hamiltonian
exactly.

## Stabilizer representation

In the basis

\[
q_0,v,w,
\]

the stabilizer acts diagonally. The independent phase ratio distinguishes
`q_0` from the `v,w` plane, while the transposition `(12)` acts as

\[
v\longmapsto v,
\qquad
w\longmapsto-w.
\]

Thus the three lines carry three distinct one-dimensional characters of the
projective stabilizer. Schur averaging over `K_v` removes all operators between
different lines and retains each line projector.

For every qutrit operator `E`, define

\[
\mathcal T_{K_v}(E)
=
{1\over18}
\sum_{g\in K_v}gEg^\dagger.
\]

Then

\[
\mathcal T_{K_v}(E)
=
\langle q_0|E|q_0\rangle P_{q_0}
+\langle v|E|v\rangle P_v
+\langle w|E|w\rangle P_w.
\]

The target-compatible twirl is the conditional expectation onto the
three-dimensional diagonal algebra

\[
\operatorname{span}
\{P_{q_0},P_v,P_w\}.
\]

It removes six complex off-diagonal matrix units but leaves two independent
traceless Hermitian diagonal directions in addition to the identity.

## First-order protected gate model

Suppose the intended Hamiltonian is

\[
H_{\rm tar}=\Omega P_v
\]

up to an irrelevant scalar. Let a quasistatic additive defect be `E`. Toggle
through the target stabilizer with equal dwell time while leaving the command
on.

Because every frame fixes `P_v`, the first average Hamiltonian is

\[
\overline H^{(1)}
=
\Omega P_v
+\mathcal T_{K_v}(E).
\]

All error terms coupling `v` to its complement disappear at first order. So do
terms coupling `q_0` and `w`. The residual is diagonal in the
`q_0,v,w` frame and commutes with the desired gate.

This suppresses leakage-like coherent drift within the accepted qutrit. It
does not suppress phase drift among the three lines.

## Exact amplitude-error obstruction

Let the physical wait have a multiplicative error

\[
H_{\rm actual}
=
(1+\epsilon)\Omega P_v.
\]

For every target-preserving frame,

\[
gP_vg^\dagger=P_v.
\]

Therefore

\[
\mathcal T_{K_v}(\epsilon\Omega P_v)
=
\epsilon\Omega P_v.
\]

The error survives unchanged. It is an overrotation of the intended logical
gate and remains inside the accepted code space.

This has the exact Knill--Laflamme form. If the inner fusion code corrected
the infinitesimal error set

\[
\{I,P_v\},
\]

then it would require

\[
P_{\rm code}P_vP_{\rm code}
=
cP_{\rm code}.
\]

But `P_v` is a non-scalar logical projector on the qutrit. Hence the same inner
code cannot exactly correct arbitrary primitive amplitude error in the
Hamiltonian it uses for control.

## Extremality of exact target preservation

Consider any positive weighted frame average of conjugated rank-one target
projectors:

\[
\sum_jp_j g_jP_vg_j^\dagger,
\qquad
p_j>0,
\qquad
\sum_jp_j=1.
\]

If this average equals `P_v` exactly, then every term must equal `P_v`.
Rank-one projectors are extreme points of the density-operator convex set.

Thus an exact positive-dwell bang--bang average that preserves the same target
projector cannot use frames outside its stabilizer. The surviving diagonal
fault algebra cannot be removed by enlarging the exact-preservation twirl.

A stronger dynamically corrected gate must allow a nontrivial time-dependent
target path whose net propagator is correct even though its instantaneous
Hamiltonian is rotated.

## What stronger constructions remain possible

The obstruction does not exclude all composite-pulse correction. It excludes
the simple strategy of leaving the target Hamiltonian fixed while averaging
errors over target-preserving frames.

Possible stronger layers are:

- composite pulses whose target axes trace a closed noncommutative path;
- dynamically corrected gates tailored to a declared low-dimensional error
  model;
- randomized compiling that converts coherent residuals into a stochastic
  channel for an outer code;
- encoding the fusion qutrit in an outer error-correcting code;
- independent calibration and feedback for slow amplitude drift.

Each layer requires a fault model and an executable sequence. Full ideal
`U(3)` controllability alone does not prove robust synthesis.

## Common-mode interpretation

The stabilizer twirl can reject relative frame components of a defect while
leaving the command direction untouched. A common-mode scale error lies in
that untouched direction.

Controller replication may verify that several classical timers requested
the same duration. It cannot determine whether the physical gap `Delta` or
the actuator coupling was uniformly mis-scaled. An independent analog
reference or outer logical verification is required.

## Exact falsifiers

- A monomial stabilizer element with a permutation outside `{e,(12)}`.
- Unequal phases on `q_1,q_2` claimed to preserve the vacuum line.
- Stabilizer order other than 18 or projective order other than six.
- An off-diagonal matrix element surviving the `K_v` twirl.
- The diagonal algebra claimed to be reduced to scalars.
- A multiplicative `P_v` error claimed canceled by target-preserving frames.
- The inner fusion code claimed to exactly correct `{I,P_v}` while `P_v`
  remains a non-scalar logical actuator.
- Exact preservation of a rank-one target obtained by positively averaging
  distinct conjugate projectors.
- The obstruction promoted to a no-go for all composite pulses or outer-code
  constructions.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies target stabilizers, conditional
expectations, commuting residual faults, positive-dwell extremality,
command--fault collinearity, and the distinction between idle decoupling and
gate-compatible decoupling.

The quantum coefficient lens supplies the fusion-qutrit vacuum projector,
finite monomial gate group, Knill--Laflamme compression, and logical
overrotation interpretation.

## Result

The finite constructor group provides a nontrivial target-compatible
decoupling layer: it removes every off-diagonal quasistatic fault while the
vacuum gate runs. Its exact residual is a three-dimensional commuting algebra.
The commanded projector itself lies in that residual, so primitive amplitude
and timing errors survive unchanged and cannot be corrected by the same inner
fusion code. Robust universal control therefore needs composite dynamics,
calibration, or an outer code beyond target-preserving frame averaging.

No build or checker was run for this research-only packet.
