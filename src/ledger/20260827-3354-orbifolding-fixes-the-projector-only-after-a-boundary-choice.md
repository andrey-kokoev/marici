---
author: marici.Figueiredo
---

# 3354 — Orbifolding Fixes the Projector Only After a Boundary Choice

## Claim

For an (SO(5)) vector on (S^1/Z_2), the parity

\[
P=\operatorname{diag}(1,1,1,1,-1)
\]

with positive intrinsic field parity leaves a rank-four zero-mode carrier.
Under the declared diagonal (SO(3)), it decomposes exactly as (3+1). The
geometric projection therefore removes WP739's unwanted second singlet and
conditionally inherits WP736's squared Clebsch ratio (4).

It does not derive its own boundary data. Reversing the intrinsic parity
retains the rank-one complementary singlet instead. Moreover,

\[
g_4=\frac{g_5}{\sqrt\ell}
\]

retains the bulk coupling and compactification-length fibers, while independent
residual-symmetry boundary terms shift the ordered contrast by
(delta_B-delta_A).

## Classification

The orbifold is a conditional labelled-projector selector and presentation
rigidifier. It is not a source selector because the boundary equivalence class,
intrinsic parity, compactification clock, and localized operators remain input
data. It supplies no calibrated physical16 detector channel.

## Scope

This audits the declared equal-endpoint parity packet. It does not exclude a
fundamental dynamics that uniquely selects its boundary class and intrinsic
parity, nor a UV completion that fixes the compactification clock and boundary
counterterms.

## Durable verification

- Packet:
  `research/flavor/flavor-orbifold-projector-conditional-rigidifier.md`
- Checker:
  `research/flavor/checkers/wp742_orbifold_projector_conditional_rigidifier.py`
- Generated result:
  `research/flavor/results/wp742_orbifold_projector_conditional_rigidifier.json`
- Exact checker outcome: 15/15 PASS.
- Sequence authority: `seqclaim-9d1c0ebb09c49ffece4c4f71`.
- Epistemic-graph admission:
  `ev-000000007188-50a6684a-0fec-42e0-a16f-b42c73cda391`.
