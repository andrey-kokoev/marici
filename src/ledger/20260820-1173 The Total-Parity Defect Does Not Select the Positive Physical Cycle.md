---
title: "The Total-Parity Defect Does Not Select the Positive Physical Cycle"
date: 2026-08-20
entry: 1173
status: active
sector: cosmology
---

# 1173 — The Total-Parity Defect Does Not Select the Positive Physical Cycle

Sequence claim: `seqclaim-44b14abace8168350d88b4eb`.

## Question

Entry 1172 replaces the free local node packet \(\mathbf Q^8\) by

\[
V_{\rm van}=\mathbf Q^8/\langle r\rangle,
\qquad
r_\epsilon=\epsilon_2\epsilon_3\epsilon_4.
\]

Could this global relation make the literal positive radial chain into a
canonical functional on the global vanishing lattice?

## Descent test

Let \(p_+=[1:1:1:1]\), and let \(f_+\) be the coordinate functional that
reads only the coefficient of the positive occurrence. A functional on
\(\mathbf Q^8\) descends to \(V_{\rm van}\) precisely when it annihilates
\(r\). But

\[
\boxed{f_+(r)=1.}
\]

Therefore

\[
\boxed{f_+\text{ does not descend to }V_{\rm van}.}
\]

The invariant orbit sum does descend:

\[
f_{\rm orb}=\sum_\epsilon f_\epsilon,
\qquad
f_{\rm orb}(r)=
\sum_\epsilon\epsilon_2\epsilon_3\epsilon_4=0.
\]

But Entry 1171 shows that the literal positive chain reaches only \(p_+\).
Replacing it by the full deck-orbit sum would be a new averaging operation,
not a consequence of the frozen physical contour.

## Meaning

The defect relation globally reduces eight local cycles to seven, but it
does not remove Entry 1170's local hemisphere ambiguity. In fact, the
positive-node coordinate is precisely sensitive to the relation by which
the quotient is formed.

Thus the current evidence separates cleanly:

\[
\boxed{
\text{global coefficient lattice: canonical rank seven}
}
\]

while

\[
\boxed{
\text{literal physical functional on that lattice: not defined}.
}
\]

This is not a carrier failure. It is another instance in which the
coefficient object exists algebraically but the frozen source does not
provide the required supported physical comparison.

## Next frontier

Retire the attempt to obtain physical activation from the global defect
alone. The remaining source-defined calculation is the Gauss--Manin
transport of the rank-seven node lattice under external kinematic motion:
determine whether its total-parity defect line is preserved and whether
collision with existing Gram support produces only the already frozen
Kato/Gysin strata. Physical activation should remain a separate question.

## Evidence

- `research/benincasa/checkers/four_site_qg_physical_node_functional.py`
- `research/benincasa/results/four-site-qg-physical-node-functional.json`
- Entries 1170--1172.
