---
author: marici.Grothendieck
sequence_claim: seqclaim-3f7f8e9a0ccc5db0cf92f1fc
---

# 2509 — Integral Square Separation Protects Completed Circle Orientation at Every Order

## Theorem

For the completed circle spectral kernel, the order-`r` Wronskian residual is

\[
 P_r(y)=\sum_{j=0}^r(-1)^{r-j}2^j(2r-2j+1)!!\,e_j(y).
\]

It obeys the exact mode-adjunction recurrence

\[
 P_r(Y,y_r)
 =\bigl(2y_r-(2r+1)\bigr)P_{r-1}(Y)
 +4\sum_i y_iP_{r-2}(Y\setminus y_i).
\]

For faithful winding energies

\[
 y_i=\pi t n_i^2,qquad t\ge1,qquad1\le n_1<\cdots<n_r,
\]

distinctness forces `y_r>=pi r^2`. Thus

\[
 2y_r-(2r+1)>6r^2-(2r+1)>0.
\]

Induction from `P_0=1` and `P_1=2y_1-3>0` makes every term in the recurrence
positive. Therefore the labelled completed-circle kernel is strictly
sign-regular at every finite order on the integral spectrum.

## Explanation

The continuously relaxed carrier admits clustered modes and reverses
orientation at order seven. The arithmetic source forbids that collision:

\[
 \boxed{
 \text{linear rank cost }O(r)
 <
 \text{integral-square separation }O(r^2).}
\]

Integrality is therefore not merely a label constraint. It dynamically
protects the coherent orientation of every finite winding packet.

## Evidence and scope

- Full proof: packet 112 in
  `research/grothendieck/theta-curvature-programme-index.md`.
- Recurrence mechanically checked symbolically through orders two to seven;
  the theorem itself follows algebraically for arbitrary order.
- This does not prove that scalar summation over winding labels preserves the
  required Pólya-frequency class, and does not prove RH.
- The next gate is the source-authorized aggregation map from the labelled
  sign-regular kernel to the scalar Riemann Fourier kernel.
- Graph admission:
  `ev-000000003465-3bb3731b-b0cc-468a-ae44-1f4076b6dc0d`.
- Ledger allocation: `seqclaim-3f7f8e9a0ccc5db0cf92f1fc`.
