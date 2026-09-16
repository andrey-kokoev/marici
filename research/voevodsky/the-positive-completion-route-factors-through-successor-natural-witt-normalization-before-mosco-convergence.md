# The positive completion route passes through a metric minimalization gate before Mosco convergence

## Coordinates

Use

\[
\beta\in\operatorname{esd}_7(\Delta^3)
\]

for lattice position and

\[
\lambda=(\Lambda,R,N,n,F)
\]

for regulator data.

At \((\beta,\lambda)\), remove the shared physical face already identified by strict cell commutativity. Let the resulting two positive residual Grams be

\[
P_{\beta,\lambda}\succeq0,
\qquad
Q_{\beta,\lambda}\succeq0.
\]

Their signed difference is

\[
D_{\beta,\lambda}
=
P_{\beta,\lambda}-Q_{\beta,\lambda}.
\]

## Forced common remainder

A positive common feature can reduce the residual pair to the Jordan legs only in the form

\[
P_{\beta,\lambda}
=(D_{\beta,\lambda})_+
+K_{\beta,\lambda},
\]

\[
Q_{\beta,\lambda}
=(D_{\beta,\lambda})_-
+K_{\beta,\lambda}.
\]

The common remainder is uniquely determined:

\[
K_{\beta,\lambda}
=
\frac{
P_{\beta,\lambda}
+Q_{\beta,\lambda}
-
|P_{\beta,\lambda}-Q_{\beta,\lambda}|
}{2}.
\]

Thus exact positive minimalization is equivalent to

\[
K_{\beta,\lambda}\succeq0.
\]

Equivalently,

\[
|P_{\beta,\lambda}-Q_{\beta,\lambda}|
\preceq
P_{\beta,\lambda}+Q_{\beta,\lambda}.
\]

This is a metric order condition. Lattice incidence supplies common-face identifications; the order condition supplies positive source-level reduction.

## Exact reduced form

When

\[
K_{\beta,\lambda}\succeq0,
\]

the reduced positive form is

\[
q_{\beta,\lambda}^{min}
=
P_{\beta,\lambda}
+Q_{\beta,\lambda}
-2K_{\beta,\lambda}.
\]

Hence

\[
q_{\beta,\lambda}^{min}
=
|D_{\beta,\lambda}|.
\]

A Kolmogorov factorization of \(K_{\beta,\lambda}\) gives the common positive feature removed from both polarities.

## Noncommuting obstruction

For noncommuting positive Grams, \(K_{\beta,\lambda}\) may have a negative part. The existing two-dimensional hostile fixture proves this possibility exactly.

Define

\[
K_{\beta,\lambda}
=
(K_{\beta,\lambda})_+
-
(K_{\beta,\lambda})_-.
\]

The finite obstruction is

\[
\mathcal O_{\beta,\lambda}^{min}
=
(K_{\beta,\lambda})_-.
\]

Exact minimalization holds precisely when

\[
\mathcal O_{\beta,\lambda}^{min}=0.
\]

An asymptotic minimalization theorem may instead establish

\[
\left\|
\mathcal O_{\beta,\lambda}^{min}
\right\|_{graph}
\longrightarrow0.
\]

## Successor compatibility

For a regulator successor from \(\lambda\) to \(\lambda'\), let

\[
S_{\lambda'\lambda}
\]

be the transported feature map. The metric gate must satisfy

\[
S_{\lambda'\lambda}^*
P_{\beta,\lambda'}
S_{\lambda'\lambda}
=
P_{\beta,\lambda},
\]

\[
S_{\lambda'\lambda}^*
Q_{\beta,\lambda'}
S_{\lambda'\lambda}
=
Q_{\beta,
\lambda}.
\]

For unitary successors, functional calculus then gives

\[
S_{\lambda'\lambda}^*
K_{\beta,\lambda'}
S_{\lambda'\lambda}
=
K_{\beta,\lambda}.
\]

For isometric inclusions, this equality becomes an additional compression-compatibility theorem because absolute value need not commute with compression.

## Mosco candidate

The unreduced sum

\[
P_{\beta,\lambda}+Q_{\beta,\lambda}
\]

contains balanced mass. The exact Mosco candidate is \(|D_{\beta,\lambda}|\) whenever the metric gate passes.

Under asymptotic minimalization, use the positive approximation obtained after removing \((K_{\beta,\lambda})_+\), and retain \((K_{\beta,\lambda})_-\) as a controlled error form.

The completion target is

\[
q_{|\mathcal A_S|}(u)
=
\left\|
|\mathcal A_S|^{1/2}u
\right\|^2.
\]

The convergence statement is

\[
\operatorname{Mosco\!\!\!-\!lim}_{\lambda}
q_{\beta,\lambda}^{min}
=
q_{|\mathcal A_S|},
\]

with lattice compatibility in \(\beta\).

## Incidence role

The polarized incidence diagram identifies feature rows already shared by opposite polarities. It supplies canonical candidates for positive common factors and coherence among their removals.

Its metric obligations are:

1. identify the physical residual pair \((P_{\beta,\lambda},Q_{\beta,\lambda})\);
2. compute the forced remainder \(K_{\beta,\lambda}\);
3. test positivity or estimate its negative part;
4. compare incidence-generated common rows with a Kolmogorov factor of \((K_{\beta,\lambda})_+\);
5. verify successor compatibility.

## Cell-count audit

The signed edgewise subdivision has 343 maximal tetrahedra. Earlier positive-polarity notes refer to a 210-cell analytic incidence system. Their relationship requires an explicit combinatorial map before incidence data can be transferred between them.

This count audit is independent of the metric gate and should be resolved as a typing obligation.

## Sonin branch

The interior condition is

\[
K_B=\{0\}.
\]

The subsequent endpoint condition is

\[
b_r^*b_r
\preceq
A_{S,r}^*A_{S,r}.
\]

These provide the parallel positive-lift gate for the Sonin and endpoint sector.

## Immediate program

1. extract the explicit physical residual Grams \(P_{\beta,\lambda}\) and \(Q_{\beta,\lambda}\) from the transported feature;
2. compute \(K_{\beta,\lambda}\);
3. test \(K_{\beta,\lambda}\succeq0\) on every available finite packet;
4. measure \((K_{\beta,\lambda})_-\) when positivity fails;
5. test successor and compression compatibility;
6. submit the reduced forms to the finite-to-closed completion interface;
7. prove horizontal and vertical transport of completion certificates.

The first active analytic datum is the physical residual Gram pair. The first decision is the positivity of its forced common remainder.
