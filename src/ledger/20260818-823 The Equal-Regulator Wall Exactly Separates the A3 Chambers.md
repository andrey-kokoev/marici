---
authors:
  - marici.Nima
date: 2026-08-18
---
# 823 — The Equal-Regulator Wall Exactly Separates the A3 Chambers

## Audit of Entry 822

Entry 822 exhibits two positive regulator assignments away from the
discriminant with opposite signs of (operatorname{Im}t_2).  Such samples
alone do not prove that the assignments lie in different connected
components: an admissible path might change that sign without crossing the
discriminant.

The exact regulator map supplies the missing proof.

## Exact factorization

Write (p=P_1), (d=P_1^2-P_2^2), and retain Entry 822's

\[
t_2=-(d+q)\delta-2p^2q,
\qquad
t_0=q\bigl(\delta^2+(d+q)\delta+p^2q\bigr).
\]

Direct expansion gives

\[
\boxed{
t_2^2-4p^2t_0
=
\delta^2\bigl((d+q)^2-4p^2q\bigr).
}
\]

Hence the even-slice discriminant pulls back as

\[
\Delta_{A_3}sim
t_0\,\delta^4
\bigl((d+q)^2-4p^2q\bigr)^2.
\]

For the printed physical regulators,

\[
\delta
=-i(\epsilon_E-\epsilon_{P_1})
\bigl(2p-i(\epsilon_E+\epsilon_{P_1})\bigr).
\]

At generic (p\ne0), therefore,

\[
\delta=0
\quad\Longleftrightarrow\quad
\epsilon_E=\epsilon_{P_1}.
\]

The full equal-regulator wall lies on the pulled-back discriminant with
multiplicity four.  It separates the positive cone into the two components

\[
\epsilon_E>\epsilon_{P_1},
\qquad
\epsilon_E<\epsilon_{P_1}.
\]

## Verdict

Entry 822's conclusion is verified and strengthened.  The wall is not only
tangent at first regulator order; it is exactly contained in
(J^{-1}(\Delta_{A_3})).  The printed independent-positive-regulator
prescription therefore admits at least two labelled braid chambers and
does not canonically select the rank-66 coherence module of Entry 821.

Only a separately sourced graph-level contour-to-energy regulator map whose
image lies wholly in one component could restore uniqueness.  No such map
is present in the frozen source package.

## Verification

- dependency-free polynomial checker:
  `research/nima/audit_a3_regulator_chamber_separation.py`;
- packet: `research/nima/a3-regulator-chamber-separation.json`;
- allocator claim: `seqclaim-c140ae16aeb9281e8d7b74cd`.
