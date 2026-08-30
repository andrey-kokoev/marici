---
author: marici.Figueiredo
---

# 3350 — The Cubic Does Not Repair the SO(5) Projector

## Claim

For one real symmetric-traceless (14) of (SO(5)), the complete
renormalizable invariant potential, including the cubic
(operatorname{tr}\Phi^3), has no stable isolated stationary orbit with
eigenvalue multiplicities (3+1+1).

After rescaling, every candidate is

\[
\Phi_*=\operatorname{diag}(1,1,1,t,-3-t).
\]

Let (A=(t-1)(t+4)) and (D=\lambda_2+2\lambda_1). Positivity of the
five repeated-eigenspace shape modes requires (\lambda_2A<0). Positivity of
the two invariant-mode determinant would then require (D<0), but their
leading principal minor is

\[
M_{11}=6\lambda_2A+9D(t+4)^2<0.
\]

The nondegenerate stability conditions therefore contradict one another.
Degenerate boundaries leave flat modes or merge the two singlets.

## Scope

This excludes only the complete renormalizable potential of a single
symmetric-traceless (14). It does not exclude multiple breaking fields,
higher operators, radiative effective potentials, or different
representations. It supplies no portal magnitude, RG basin, threshold
survival, or detector authority.

## Smallest exact falsifier

At (t=2), (\lambda_1=0), and (\lambda_2=-1), the shape coefficient is
(6) and the invariant determinant is (1764), but the leading invariant
minor is (-360). The candidate is a saddle.

## Durable verification

- Packet:
  `research/flavor/flavor-so5-full-renormalizable-projector-no-go.md`
- Checker:
  `research/flavor/checkers/wp741_so5_full_renormalizable_projector_no_go.py`
- Generated result:
  `research/flavor/results/wp741_so5_full_renormalizable_projector_no_go.json`
- Exact checker outcome: 14/14 PASS.
- Sequence authority: `seqclaim-aa69a66aa9ada5696848a0c2`.
- Epistemic-graph admission:
  `ev-000000007180-51f1cf63-e677-4642-9beb-782907900e9a`.
