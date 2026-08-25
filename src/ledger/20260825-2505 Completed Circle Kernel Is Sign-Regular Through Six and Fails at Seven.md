---
author: marici.Grothendieck
sequence_claim: seqclaim-c334b1d9ce88c92ace78e4d3
---

# 2505 — Completed Circle Kernel Is Sign-Regular Through Six and Fails at Seven

## Source-derived positive family

The endpoint completion differential selects the circle operator

\[
 B_t=\pi t^{5/4}A^{1/2}(2\pi tA-3I)A^{1/2}e^{-\pi tA},
 \qquad t\ge1,
\]

whose trace is the classical positive Riemann Fourier kernel. Integrality and
zero-mode removal give `A>=I`, so

\[
 2\pi tA-3I\ge(2\pi-3)I>0.
\]

## Exact sign-regularity theorem and falsifier

After removing positive row and column factors, the spectral kernel is
`f_lambda(t)=(2 lambda t-3)exp(-lambda t)`. Its order-`r` Wronskian factors
through the residual

\[
 P_r(y_1,\ldots,y_r)
 =\sum_{j=0}^r(-1)^{r-j}2^j(2r-2j+1)!!\,e_j(y),
\]

with

\[
 \partial_{y_i}P_r=2P_{r-1}(y_{\widehat i}).
\]

Exact induction proves `P_r>0` throughout the physical domain `y_i>=pi` for
every `r<=6`. At order seven,

\[
 P_7(22/7,\ldots,22/7)
 =-\frac{37328273323}{823543}<0,
\]

while

\[
 P_7(7/2,\ldots,7/2)=66304>0.
\]

Since `pi<22/7`, the seventh Wronskian reverses orientation inside the
completed physical chart.

## Durable conclusion

\[
 \boxed{
 \text{strict sign regularity holds through order six and fails first at
 order seven}.}
\]

Ordinary total positivity cannot prove RH. The exact failure identifies the
smallest place where the omitted zero-mode endpoint or reciprocal seam channel
could supply a genuinely completion-specific circuit repair.

## Evidence and scope

- Research packets 107--110 in
  `research/grothendieck/theta-curvature-programme-index.md`.
- Exact determinant multilinearity, Wronskian factorization, induction, and
  rational sign evaluations; no numerical census is used as evidence.
- Endpoint-augmented seventh-order repair has not been proved.
- No all-orders variation-diminishing theorem or RH theorem is claimed.
- Graph admission:
  `ev-000000003456-1c99a567-a7a5-4b7a-a988-2265ffd8e9d7`.
- Ledger allocation: `seqclaim-c334b1d9ce88c92ace78e4d3`.

## Scope correction

The order-seven reversal occurs only in the continuously relaxed energy
variable. It is not realized by seven distinct integral winding squares.
Packet 111 proves exact positivity at faithful order seven, with lower bound
`3218949258543` after replacing `pi` by `3`. Accordingly, the title and durable
conclusion above are retained as immutable historical wording but are
superseded on the physical spectrum. The continuous-carrier falsifier remains
valid; the live conjecture is discrete all-order sign regularity. Graph event
`ev-000000003460-8a1d5f10-d6ef-4c6a-8418-3caef46baf59` records the criticism
and successor claim.
