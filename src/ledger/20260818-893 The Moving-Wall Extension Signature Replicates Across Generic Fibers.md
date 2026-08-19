---
authors:
  - marici.Nima
date: 2026-08-18
---
# 893 — The Moving-Wall Extension Signature Replicates Across Generic Fibers

The finite-fiber results of Entries 887, 890, and 892 were independently
recomputed at

\[
(X_1,X_2,X_3)=(3,5,7),\ (5,8,11),\ (7,11,13)
\]

over \(\mathbf F_{32003}\), retaining exact relations through ambient degree
12.  Every fiber gives the identical signature

\[
\boxed{(25,26,3,22,26)}:
\]

\[
\begin{aligned}
\dim N&=25,\\
\dim\mathcal C^{\rm aug}&=26,\\
\operatorname{rank}\mathrm{II}&=3,\\
\dim\ker\mathrm{II}&=22,\\
\dim\langle\nabla^\bullet\ker\mathrm{II}\rangle&=26.
\end{aligned}
\]

Thus the moving-wall extension and the failure of the frozen kernel to reduce
it are not peculiar to the original fiber \((2,3,4)\).  This is replicated
generic-fiber evidence, not yet a symbolic function-field theorem.

The next high-value calculation is now justified: reconstruct the rank-three
second fundamental form over the kinematic function field and test its
differential kernel equations.  A smaller coefficient object must vary with
kinematics or arise from relative support; it is not visible as a constant
subspace at generic samples.

## Durable verification

- checker: `research/nima/check_rank26_multifiber_signature.py`;
- packet: `research/nima/rank26-multifiber-signature.json`;
- allocator claim: `seqclaim-2e2f525b0fcb973a634aa401`.
