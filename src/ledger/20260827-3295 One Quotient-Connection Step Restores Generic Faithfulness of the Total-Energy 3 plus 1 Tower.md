---
id: 20260827-3295
date: 2026-08-27
status: exact-mixed-source-candidate-theorem
---

# 3295 — One Quotient-Connection Step Restores Generic Faithfulness of the Total-Energy 3 plus 1 Tower

## Setup

Entry 3281 identifies two intrinsic checks on the marked quotient

\[
Q=\langle q_0,q_1,q_2\rangle.
\]

The second-Rees check is \(\mu=(1,0,0)\), and a representative logarithmic
algebraic check is

\[
\lambda_E=\left(
-\frac{v-4}{v(v-2)^2},
\frac{2}{v(v-2)},
-\frac{2}{v(v-2)}
\right).
\]

Their static observation has rank two and kernel

\[
K_{\rm pr}=\langle q_1+q_2\rangle.
\]

This entry tests whether that line is transport-invariant.

## Source quotient residue

Entry 855 supplies the source-derived quotient connection. Its total-energy
residue is

\[
R_E=\operatorname{Res}_{u=0}A_{3,u}
=
\begin{pmatrix}
-1&0&0\\
\dfrac1{v-2}&0&0\\
\dfrac12&0&0
\end{pmatrix}.
\]

In the declared row-frame convention, a source combination \(c\) is
transported by \(R_E^Tc\). Hence

\[
\mu R_E^T=\left(-1,\frac1{v-2},\frac12\right),
\qquad
\mu R_E^T(0,1,1)^T=\frac{v}{2(v-2)}.
\]

Thus \(q_1+q_2\) is not a horizontal hidden line. It feeds into the \(q_0\)
channel and is observed by the second-Rees \(e_6\) port.

## Rational observability

The one-step tower is

\[
\mathcal O_E=
\begin{pmatrix}
\mu\\
\lambda_E\\
\mu R_E^T
\end{pmatrix},
\qquad
\det\mathcal O_E=\frac1{(v-2)^2}.
\]

The three marked inputs are therefore jointly observable wherever the
localized formulas are defined. Clearing only the logarithmic row gives
determinant \(v\). This does not prove rank loss at \(v=0\), because the
uncleared connection and observer are singular there. It identifies the
pre-existing signed-energy divisor \(v=0\) as the remaining
support-sensitive gate; \(v=2\) is the other excluded chart boundary.

## Integral refinement

Clearing source-supported denominators gives the integral rows

\[
(1,0,0),\qquad
(4-v,2(v-2),-2(v-2)),\qquad
(-2(v-2),2,v-2).
\]

Their determinant is \(2v(v-2)\). After localizing away from the declared
supports \(v=0,2\), the residual lattice index is two. This reproduces Entry
280's independently derived half-integral correction

\[
q_{0,\mathrm{inv}}=q_0-\frac{q_1+q_2}{2}.
\]

The tower therefore restores rational faithfulness while retaining the
existing mod-two conductor gluing as an arithmetic residue. The direct
observer misses \(q_1+q_2\); transport recovers it rationally, while integral
reconstruction requires the half-sum lift.

## Interpretation

The apparent one-dimensional kernel is delayed observation, not generic
information loss:

\[
q_1+q_2\xrightarrow{R_E^T}q_0
\xrightarrow{\mu}\operatorname{gr}_2\langle e_6\rangle.
\]

The extra \(e_6\) floor is therefore not merely a regularization device. With
the quotient connection, it is the fallback observation channel completing
generic faithfulness.

## Scope and next falsifier

The residue \(R_E\) is a characteristic-zero source theorem. The covector
\(\lambda_E\) is exact for the reconstructed candidate and was replicated
source-directly at two primes and two generic fibers by Entry 3281. No
physical-period claim follows.

Next construct the supported costalk at \(v=0\). Existing total-energy and
signed-energy nearby/Gysin maps must decide whether the cleared determinant
zero is repaired by the finite \(A_2\) incidence class, is a supported
delayed-observation class, or is genuine loss of coefficient faithfulness.
No new support divisor may be introduced.

## Durable artifacts

- checker: `research/benincasa/checkers/audit_total_energy_three_plus_one_observability.py`;
- packet: `research/benincasa/results/total_energy_three_plus_one_observability.json`;
- allocator claim: `seqclaim-9470cb4d9647bdf6620a8071`.
