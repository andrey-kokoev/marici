# Relevant Portal Modes Must Be Contrast-Invisible

Author: `marici.Figueiredo`

## Claim

For the simultaneous representation-labelled portal block

\[
M=
\begin{pmatrix}a&c\\c&b\end{pmatrix},
\qquad
s=
\begin{pmatrix}4q_A\\3q_B\end{pmatrix},
\]

the unique fixed contrast is

\[
\Delta_*=
\frac{4q_A(b+c)-3q_B(a+c)}{ab-c^2}.
\]

The mixed scalar channel shifts the exact cancellation fiber to

\[
\frac{q_B}{q_A}=\frac{4(b+c)}{3(a+c)}.
\]

If the portal stability block is positive definite, both portal fluctuations
are irrelevant. If a relevant portal eigenmode remains, the contrast is still
predicted only when the covector ((1,-1)) annihilates that eigenvector. A
relevant odd eigenmode restores a free contrast amplitude.

## Boundary

This is an exact acceptance theorem for the linearized direct-sum block. It
does not derive the coefficients from the simultaneous matter action or prove
that the scalar fixed point is physically stable.

## Verification

- Packet:
  `research/flavor/flavor-direct-sum-portal-block-acceptance-theorem.md`
- Checker:
  `research/flavor/checkers/wp730_direct_sum_portal_block_acceptance.py`
- Result:
  `research/flavor/results/wp730_direct_sum_portal_block_acceptance.json`
- Exact checker outcome: 12/12 PASS.
- Epistemic-graph admission:
  `ev-000000007045-3d510726-2667-4b79-9848-81cda4df0ad9`.

## Remaining gate

Compute the full direct-sum beta coefficients and stability eigenvectors from
the anomaly-free singlet-plus-triplet action. Then prove that no relevant mode
outside the portal block re-enters the contrast through finite matching.
