# Finite Paley--Wiener windows realize the affine crossing clutching by trace-class rank-two operators

## Scope

The affine boundary-current clutching has a concrete operator realization on every finite Paley--Wiener spectral window.

This is a finite-regularization theorem. It does not give a uniformly trace-class operator on ambient \(L^2(\mathbb R)\), and it does not identify the operator with the unresolved prolate Birman--Krein scattering determinant.

## Paley--Wiener carrier

Use the Fourier convention

\[
f(t)
=
\frac1{\sqrt{2\pi}}
\int_{-L}^{L}

e^{itx}
F(x)
\,dx
\]

and let

\[
PW_L
=
\mathcal F
L^2([-L,L]).
\]

This is a reproducing-kernel Hilbert space with kernel

\[
K_L(t,s)
=
\frac{
sin L(t-s)
}
{
\pi(t-s)
},
\]

where

\[
K_L(t,t)
=
\frac L\pi.
\]

For every real \(u\), evaluation

\[
E_{u,L}f
=
f(u)
\]

is bounded, with reproducing vector

\[
k_{u,L}
=
K_L(\,
\cdot
,u)
\]

and

\[
\|k_{u,L}\|^2
=
\frac L\pi.
\]

## Atomic current operator

For a finite signed atomic cycle

\[
A
=
\sum_{j=1}^N
c_j
\delta_{t_j},
\qquad
c_j\in\mathbb R,
\]

define

\[
T_{A,L}
=
\sum_{j=1}^N
c_j
|
k_{t_j,L}
\rangle
\langle
k_{t_j,L}
|.
\]

Then for \(f,g\in PW_L\),

\[
\langle
T_{A,L}f,
g
\rangle
=
\sum_j
c_j
f(t_j)
\overline{g(t_j)}
=
\langle
A,
f\overline g
\rangle.
\]

Thus \(T_{A,L}\) is the exact operator representative of the atomic boundary-current form on \(PW_L\).

It is self-adjoint, finite rank, and trace class. Its rank is at most \(N\), with collisions combined by adding coefficients before constructing the operator.

## Trace and trace-norm estimates

The trace is

\[
\operatorname{Tr}
T_{A,L}
=
\frac L\pi
\sum_j
c_j.
\]

The trace norm satisfies

\[
\|T_{A,L}\|_1
\le
\frac L\pi
\sum_j
|c_j|.
\]

If all \(c_j\) have the same sign, equality holds.

Consequently the operator is trace class at every finite \(L\), but its natural trace norm grows linearly with the spectral window.

This growth is the real-boundary analogue of the stronger exponential growth of fixed off-real endpoint evaluation.

## Symmetry-completed hostile cycle

For

\[
A_\gamma
=
\delta_\gamma+
\delta_{-\gamma},
\qquad
\gamma>0,
\]

define

\[
P_{\gamma,L}
=
T_{A_\gamma,L}
=
|
k_{\gamma,L}
\rangle
\langle
k_{\gamma,L}
|
+
|
k_{-\gamma,L}
\rangle
\langle
k_{-\gamma,L}
|.
\]

This operator is positive and has rank two unless the two evaluation vectors become linearly dependent in a degenerate window.

Its trace and trace norm are

\[
\operatorname{Tr}
P_{\gamma,L}
=
\|P_{\gamma,L}\|_1
=
\frac{2L}{\pi}.
\]

The overlap of the two crossing directions is

\[
\langle
k_{\gamma,L},
k_{-\gamma,L}
\rangle
=
K_L(
\gamma,-\gamma
)
=
\frac{
sin(2L\gamma)
}
{
2\pi\gamma
}.
\]

Hence the two nonzero Gram eigenvalues are

\[
\lambda_\pm
=
\frac L\pi
\pm
\frac{
sin(2L\gamma)
}
{
2\pi\gamma
}.
\]

Both are positive for \(L>0\) and \(\gamma>0\), confirming the two independent finite-window crossing modes.

## Operator jump law

For an oriented multiplicity-\(m\) crossing cycle

\[
A_0
=
m\sigma
A_\gamma,
\]

the boundary-current jump becomes

\[
\Delta T_{\nu,L}
=
-2m\sigma
P_{\gamma,L}.
\]

The cumulative index operator jumps by

\[
\Delta T_{I,L}
=
m\sigma
P_{\gamma,L}.
\]

Therefore

\[
\boxed{
\Delta(
T_{\nu,L}
+
2T_{I,L}
)
=0.
}
\]

The affine-clutched current has an exact trace-class realization on every finite window.

## Relation to the kernel crossing

For the hostile family, the two-dimensional model-space kernel collapses on fixed interior packets as \(a\to0\). After boundary normalization, its two modes converge to the evaluation vectors

\[
k_{\gamma,L},
\qquad
k_{-\gamma,L}.
\]

Thus the finite-window operator picture realizes the transfer

\[
\text{positive rank-two interior model space}
\longrightarrow
P_{\gamma,L}
\longrightarrow
\text{negative rank-two interior model space}.
\]

The middle operator is not zero. It is the rank-two boundary trace retained by the affine current channel.

## Green realization

Let \(G_{a,L}^{phase}\) denote the finite-window Green operator associated with the regular phase current. Across the crossing,

\[
\Delta G_{a,L}^{phase}
=
-2m\sigma
P_{\gamma,L}.
\]

Define the index-corrected Green operator

\[
G_{a,L}^{aug}
=
G_{a,L}^{phase}
+
2T_{I_a,L}.
\]

Then

\[
\Delta G_{a,L}^{aug}
=0.
\]

This is an operator-level form of the rigged-dual affine clutching.

It is a signed Green identity: for downward crossings, the oriented index operator has negative coefficient. No positivity is inferred from trace-class continuity.

## Successor pullback

Mellin multiplication need not preserve one fixed Paley--Wiener window. Let an admitted successor instead be represented by a bounded map

\[
S_c:PW_L\to PW_{L'}
\]

that satisfies the pointwise intertwining law

\[
E_{t_j,L'}S_c
=
m_c(t_j)E_{t_j,L}
\]

at every active atom. This law must be checked for the declared source and window transition; it is not automatic for an orthogonal compression of multiplication.

The pulled-back atomic operator is

\[
T_{A,L}^{(c)}
=
S_c^*
T_{A,L'}
S_c.
\]

Its form is

\[
\langle
T_{A,L}^{(c)}f,
g
\rangle
=
\sum_j
c_j
|m_c(t_j)|^2
f(t_j)
\overline{g(t_j)}.
\]

Thus successors satisfying the evaluation-intertwining law preserve the clutching identity. If \(m_c(t_j)=0\), the corresponding rank-one row is annihilated on the successor image.

## Dagger

Boundary reflection acts by

\[
(Rf)(t)
=
\overline{f(-t)}.
\]

It satisfies

\[
R
k_{\gamma,L}
=
k_{-\gamma,L}
\]

under the induced antiunitary convention. Therefore

\[
R
P_{\gamma,L}
R^{-1}
=
P_{\gamma,L}.
\]

The symmetry-completed clutching operator is dagger invariant.

## Failure of uniform ambient completion

Because

\[
\|P_{\gamma,L}\|_1
=
\frac{2L}{\pi},
\]

there is no uniform trace-norm bound as

\[
L\to\infty.
\]

Real-axis evaluation is not a bounded functional on ambient \(L^2(\mathbb R)\). Accordingly, the operators \(P_{\gamma,L}\) do not converge in trace norm to an ambient \(L^2\) operator representing \(\delta_\gamma+\delta_{-\gamma}\).

The affine identity survives under source pairing and in the rigged dual, but not as an unrenormalized ambient trace-class limit.

## Possible renormalized limit

The normalized operators

\[
\widetilde P_{\gamma,L}
=
\frac\pi L
P_{\gamma,L}
\]

have trace two. However, this normalization rescales the boundary current and therefore does not represent the original Green form without a compensating normalization elsewhere.

It is a candidate only if the physical cutoff trace carries the reciprocal Plancherel-volume factor. That matching has not been proved.

## Tetrahedral placement

At finite \(L\), the affine terminal node has an operator representative

\[
C_{13,7}^{aff,L}
=
(
C_{13,7}^{reg,L},
[T_{\nu,L},T_{I,L}],
\beta_{end,L}
).
\]

The clutching face is the exact finite-rank identity

\[
\Delta T_{\nu,L}
+
2\Delta T_{I,L}
=0.
\]

Thus every finite-window tetrahedron closes in the trace-class category. The exhaustion \(L\to\infty\) exits that category unless a physical renormalization or cancellation theorem is supplied.

## What this closes

The construction provides:

1. a concrete operator representing every finite atomic crossing cycle;
2. exact rank, trace, and trace-norm formulas;
3. a trace-class affine clutching identity at finite regularization;
4. dagger and successor compatibility;
5. an operator-level augmented Green jump cancellation.

## Remaining gate

The unresolved physical theorem is now precise:

\[
\boxed{
\text{Does the transported prolate/relative cutoff supply a volume renormalization or cancellation that controls }
P_{\gamma,L}
	ext{ as }
L\to\infty?
}
\]

Without such a theorem, finite-window trace-class clutching does not imply a global Hilbert-space realization or positivity.

## Disposition

The hostile crossing admits an exact rank-two trace-class clutching operator on every finite Paley--Wiener window. Its trace norm grows like \(L\), so the remaining hostility is precisely the global cutoff-removal problem.
