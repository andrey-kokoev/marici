---
authors:
  - marici.Nima
date: 2026-08-18
---
# 650 — The Physical Wall Cocycle Has No Canonical T7 Lift

## Hard-to-vary claim

The closed physical shared-wall cocycle of Entry 648 is liftable to the
three-wall relative module, but the frozen normalization and localization
data do not select a canonical lift into the absolute nine-master module or
its rank-seven algebraic kernel.

## Exact localization ranks

For the three shared walls, deletion--restriction gives

\[
\operatorname{rank}H^2(S_E)=9,
\qquad
\operatorname{rank}H^2(S_E\setminus W_{123})=15.
\]

Entry 279 proves

\[
H^3(S_E)=0.
\]

Consequently the localization sequence is the canonical short exact
sequence

\[
0\longrightarrow H^2(S_E)
\longrightarrow H^2(S_E\setminus W_{123})
\xrightarrow{\partial_W}H^1(W_{123})(-1)
\longrightarrow0,
\]

with ranks

\[
\boxed{0\longrightarrow\mathbb Q^9
\longrightarrow\mathbb Q^{15}
\longrightarrow\mathbb Q^6\longrightarrow0.}
\]

The rank-six quotient agrees with the three source-ordered wall increments

\[
1+2+3=6.
\]

## Lift torsor

Let \(\rho_{\rm phys}\) be Entry 648's closed cocycle. Since
\(H^3(S_E)=0\), lifts exist. But if \(\widetilde\rho\) is one lift, every
other lift is

\[
\widetilde\rho+m,
\qquad m\in H^2(S_E).
\]

Thus the space of lifts is an affine torsor of rank nine. Localization
provides no preferred origin.

Entry 150 gives

\[
0\longrightarrow\mathcal T_7
\longrightarrow\mathcal M_q^{(9)}
\longrightarrow\mathbb V_{\rm ell}(-1)
\longrightarrow0.
\]

Even if one separately requires zero elliptic image, two admissible lifts
may differ by any element of \(\mathcal T_7\). The remaining ambiguity is
therefore rank seven:

\[
\boxed{\text{zero-elliptic lifts form a }\mathcal T_7\text{-torsor}.}
\]

## Correction to the frontier

There is no normalization-derived supported pushforward

\[
H^1(W)(-1)\longrightarrow H^2(S_E).
\]

That arrow reverses the canonical localization direction. Entry 648
constructs a legal quotient class, not canonical absolute coordinates.
This is the physical specialization of the general type gate in Entry 326.

Entry 649 independently shows why ordinary IBP does not repair the defect:
at \(\epsilon=0\), the Cayley--Menger boundary homotopy is obtained by
meromorphic continuation rather than literal boundary contraction.

## Updated frontier

The next admissible test is not another absolute projection. It is the
finite-part specialization of a source IBP primitive at \(\epsilon=0\).
Only a proof that this finite part is independent of both regulator path and
primitive representative could choose an origin in the lift torsor.

## Evidence

- `research/benincasa/physical_shared_wall_no_canonical_t7_lift.py`;
- Entries 150, 279, 326, 648, and 649.

## Outcome contract

~~~json
{
  "claim": "The frozen normalization sequence canonically pushes the physical shared-wall cocycle into T7.",
  "status": "falsified",
  "localization_ranks": [9, 15, 6],
  "H3_rank": 0,
  "lift_exists": true,
  "absolute_lift_torsor_rank": 9,
  "zero_elliptic_lift_torsor_rank": 7,
  "canonical_T7_lift": false,
  "next_experiment": "Compute the epsilon-zero finite part of a source IBP primitive and test regulator-path and representative independence."
}
~~~
