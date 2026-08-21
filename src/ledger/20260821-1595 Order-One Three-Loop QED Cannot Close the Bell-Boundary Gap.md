# 1595 — Order-One Three-Loop QED Cannot Close the Bell-Boundary Gap

Date: 2026-08-21

Sequence claim: `seqclaim-0ec58dc9fed2ee93a4a10488`

## Result

At \(\alpha=1/137\), the exact two-loop QED coefficient magnitude is

\[
r_2=\frac3{11}+\frac{130\alpha}{363\pi}
=0.2735593550\ldots,
\]

while Entry 1593's lower Bell boundary is

\[
r_B=\frac23(\sqrt2-1)=0.2761423749\ldots.
\]

The positive gap is

\[
r_B-r_2=0.00258301988\ldots.
\]

Writing the unknown three-loop contribution as \(c_3\alpha^2\), saturation
would require

\[
\boxed{c_3=48.48070015\ldots.}
\]

Therefore an order-one three-loop coefficient cannot close the gap.  The
QED–Bell near-contact is perturbatively stable at this stated scale, although
this does not compute the unknown three-loop term.

For a general first higher-derivative deformation, the transverse boundary
obeys

\[
r_B(\epsilon,w)=r_B+epsilon r_B(\delta_1-\delta_2)+\frac23w+cdots,
\qquad w=|\Phi_5/\Phi_1|^2.
\]

Thus the first linear instability is the relative correction between
\(\Phi_1\) and \(\Phi_2\).  A mixed-helicity \(\Phi_5\) term enters only
quadratically and moves the boundary upward.

The next sharp source calculation is consequently the first
higher-derivative coefficient difference \(\delta_1-\delta_2\), not another
Bell-normalization audit.

## Evidence

- Sinha--Zahed, arXiv:2212.10213v3, the two-loop ratio and three-loop ansatz.
- `research/nima/check_qed_bell_boundary_stability.py`
- `research/nima/results/qed-bell-boundary-stability.json`
- `research/nima/qed-bell-boundary-stability.md`
- epistemic-graph event:
  `ev-000000001776-62aa362a-c9cb-4511-a438-1d526785754e`.
