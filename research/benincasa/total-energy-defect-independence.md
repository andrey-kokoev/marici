# Total energy and labelled defects are generically independent

## Hard-to-vary claim

In the frozen generic kinematic source, define

\[
E=X_1+X_2+X_3,
\qquad
\nu_i=P_i^2-X_i^2.
\]

Consider the source map

\[
F:(X_1,X_2,X_3,P_1,P_2,P_3)
\longmapsto
(E,\nu_1,\nu_2,\nu_3).
\]

Its Jacobian contains the minor on columns
\((X_1,P_1,P_2,P_3)\):

\[
\begin{pmatrix}
1&0&0&0\\
-2X_1&2P_1&0&0\\
0&0&2P_2&0\\
0&0&0&2P_3
\end{pmatrix},
\]

whose determinant is

\[
\boxed{8P_1P_2P_3}.
\]

Therefore \(F\) is dominant. The four functions
\(E,\nu_1,\nu_2,\nu_3\) are generically algebraically independent.

The displayed minor vanishes on \(P_i=0\), but the full Jacobian does not
generically lose rank there. Alternative minors on the three simple soft
divisors are respectively

\[
8X_1P_2P_3,
\qquad
-8X_2P_1P_3,
\qquad
8X_3P_1P_2.
\]

## Consequence

No generic algebraic relation in the frozen kinematic carrier can induce a
nonzero map

\[
\operatorname{gr}_{E}^{(2)}
\longrightarrow
\langle\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3\rangle.
\]

Entry 2573 identifies the unique cyclic target if an equivariant map exists,
but the carrier source does not supply its existence. Any surviving map must
come from:

- a coefficient object and its Hessian/connection;
- an independently derived construction on a deeper support intersection;
- a physical relative-cycle specialization.

It cannot be inferred from generic kinematic incidence alone.

## Finite falsifier

The simple coordinate-soft divisors do not supply a generic Jacobian
rank-drop kernel. The next test must therefore start from an independently
existing coefficient or physical-cycle map, or from a deeper intersection
where the full Jacobian rank actually drops. Do not infer such a map from the
vanishing of one coordinate minor.

## Pre-activation observation

- excitement: 9/10;
- confidence in generic independence: 9/10;
- expected information gain: 9/10;
- epistemic status: process observation, not evidence.

## Result

The exact symbolic checker reproduces the displayed minor and verifies all
four gates. Hence generic kinematic incidence is excluded as the missing
source of the map. This is a negative typing theorem, not a claim that the
quadratic line is physically absent.

The simple soft-divisor route is also generically closed: alternative minors
retain rank four. The next admissible test must be coefficient-derived,
physical-cycle-derived, or supported on a deeper intersection where the full
Jacobian rank actually drops.
