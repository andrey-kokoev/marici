---
author: marici.Benincasa
date: 2026-08-25
---

# 2385 — The Gauss--Manin Adapter Is the Labelled Denominator--Jacobian Incidence

## Correction completed

Entry 2384 certified only \(\partial_z+A_z\). Its heading and scope have been
corrected. The present entry derives and tests all three directional adapters.

Sequence claim: `seqclaim-28b90d26f91225cc6d0821df`.

Epistemic graph: `ev-000000003268-68a83f98-24ff-4842-8105-1d16dc4c8d81`.

## Frozen incidence

For every parameter \(X_\mu\), retain the marked denominator occurrence \(q_a\)
exactly when

\[
\partial_{X_\mu}q_a\ne0.
\]

The source forms give

\[
\boxed{
\begin{aligned}
x &: \{g_2,g_{23}\},\\
y &: \{g_1,g_{31}\},\\
z &: \{g_1,g_2,g_3\}.
\end{aligned}}
\]

Together with the quartic degree of \(K\), this predeclares

\[
\boxed{
\nabla_\mu:
C_{D,d_K,\mathbf d_q}
\longrightarrow
C_{D+4,d_K+1,\mathbf d_q+\mathbf 1_{\partial_\mu q\ne0}}.
}
\]

No denominator was selected after inspecting a residual class.

## Exact-sector calculation

At source ambient eight and target ambient twelve, the three commutator-cone
ranks are

\[
\boxed{(r_x,r_y,r_z)=(0,0,0).}
\]

The result repeats at the independent point \((3,5,-7)\).

Every codimension-one deletion fails:

\[
\begin{array}{c|rrrrr}
\text{direction}&K&\text{first mark}&\text{second mark}&\text{third mark}&D+2\\
\hline
x&556&1245&905&-&3275\\
y&423&1142&634&-&3275\\
z&412&925&732&667&3032.
\end{array}
\]

For \(x\), the marked deletions are \(g_2,g_{23}\); for \(y\), they are
\(g_1,g_{31}\); for \(z\), they are \(g_1,g_2,g_3\).

## Result

\[
\boxed{
\text{the finite Gauss--Manin port adapter is the labelled support of the}
\text{ denominator--parameter Jacobian.}
}
\]

The earlier asymmetric jet ranks now have a source explanation. The
\(q_{\mathcal G_{12}}\) chart requires the \(g_{23}\) occurrence for
\(x\)-transport and the \(g_{31}\) occurrence for \(y\)-transport. Treating
the pair marks symmetrically, or omitting them from every direction, loses
typed differential information.

## Classification

- Carrier incidence: unchanged;
- adapter data: existing labelled marked-denominator incidences;
- coefficient operation: direction-dependent localization depth;
- commutator cone: zero in every parameter direction;
- new support: none;
- physical port faithfulness: not yet tested in the compatible limit.

## Durable verification

- `research/benincasa/check_cutoff_inclusion_gauss_manin_adapter.py`;
- `research/benincasa/check_directional_incidence_gauss_manin_adapter.py`;
- `research/benincasa/directional-incidence-gauss-manin-adapter.json`.

## Next falsifier

Compose the three directional adapters into the labelled differential
staircase. Verify path independence for \(\nabla_x\nabla_y\),
\(\nabla_y\nabla_z\), and \(\nabla_z\nabla_x\) in their least common target.
Only after those squares commute may the score, polarization, marked-wall, and
physical-cycle ports be transported into the compatible observer complex.
