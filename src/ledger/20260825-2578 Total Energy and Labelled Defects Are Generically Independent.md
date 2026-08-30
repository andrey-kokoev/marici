# 2578 — Total Energy and Labelled Defects Are Generically Independent

## Claim

For the frozen generic three-site kinematics, let

\[
E=X_1+X_2+X_3,
\qquad
\nu_i=P_i^2-X_i^2.
\]

The map

\[
(X_1,X_2,X_3,P_1,P_2,P_3)
\longmapsto
(E,\nu_1,\nu_2,\nu_3)
\]

is dominant. Consequently, generic
kinematic incidence does not supply a map from the second total-energy normal
grade to the labelled square-free quadratic defect module.

## Exact certificate

The Jacobian minor on the columns \((X_1,P_1,P_2,P_3)\) is

\[
\begin{pmatrix}
1&0&0&0\\
-2X_1&2P_1&0&0\\
0&0&2P_2&0\\
0&0&0&2P_3
\end{pmatrix},
\]

with determinant

\[
\boxed{8P_1P_2P_3}.
\]

Thus \(E,\nu_1,\nu_2,\nu_3\) are algebraically independent on a dense open
locus.

The displayed minor alone must not be interpreted as the full rank-drop
ideal. On \(P_1=0,P_2=0,P_3=0\), alternative minors are

\[
8X_1P_2P_3,
\qquad
-8X_2P_1P_3,
\qquad
8X_3P_1P_2,
\]

so every simple soft divisor still has generic rank four.

## Relation to Entry 2573

Entry 2573 proved that cyclic symmetry leaves only the projective target

\[
\mathbf Q\langle
\nu_1\nu_2+\nu_1\nu_3+\nu_2\nu_3
\rangle.
\]

The present result proves that symmetry does not acquire existence from the
generic carrier algebra. If the desired total-energy-to-quadratic map exists,
it must instead be derived from a coefficient connection/Hessian, a physical
relative-cycle specialization, or an existing supported construction.

## Scope

This excludes a generic carrier-algebra map and the tempting generic
simple-soft rank-drop mechanism. It does not exclude a coefficient- or
cycle-derived map, nor one on a deeper existing support intersection.

## Next falsifier

1. derive a candidate map from the frozen coefficient connection/Hessian or
   physical relative cycle, rather than from kinematic incidence;
2. alternatively, compute the full rank-drop scheme and retain only deeper
   intersections already present in the Carrier;
3. test whether the derived image reaches the cyclic quadratic line;
4. prohibit extending a supported map by a chosen splitting.

## Artifacts

- `research/benincasa/total-energy-defect-independence.md`
- `research/benincasa/checkers/check_total_energy_defect_independence.py`
- `research/benincasa/results/total-energy-defect-independence.json`

Ledger sequence claim: `seqclaim-d93ed0f0069a4e34660ee8b4`.

Epistemic event: `ev-000000003700-ab70de14-048d-47c2-b7d5-acb08f031a82`.

Soft-divisor correction event:
`ev-000000003709-c5c2bc59-d649-42c2-a408-9fdbfe93cba4`.
