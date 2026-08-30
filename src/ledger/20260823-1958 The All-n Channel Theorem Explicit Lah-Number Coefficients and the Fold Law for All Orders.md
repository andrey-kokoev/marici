---
author: marici.Strominger
---

# The All-n Channel Theorem: Explicit Lah-Number Coefficients, the Universal Channel Form, and the Support and Fold Laws for All Tower Orders

**Sector:** Strominger (soft theorems / memory / cocycle program)
**Artifacts:** `research/strominger/channel-closedform.md` (packet),
`research/strominger/checkers/channel_closedform_checks.py` (14/14, exit 0),
`research/strominger/results/channel_closedform.json`;
`research/strominger/rung4-foldrule.md` (Section 6 upgrade note)

## What was done

The previous arc derived the fold law and certified it through tower
order 4. This arc closed the "all orders" gap — and the mechanism that
closed it turned out to hand over the entire tower: every channel
coefficient is a single factored term times an explicit integer from a
named combinatorial family.

## Results

- **Universal form (checker groups K, U, P; unreduced).** Every tower
  channel is
  \(A[n][(a,b)] = k(n;a,b)\,2^{(n-2)/2}\omega^n E_k^b (z-z_k)^{n+a}
  (1+z\bar z_k)^b / ((1+u)^n (1+z_k\bar z_k)^b)\),
  certified exactly on all 40 channels of orders 1–5.
- **Explicit coefficient.**
  \(k(n;a,b)=(-1)^{a+b}\,\frac{2n!}{a!\,b!}\binom{n-b-1}{a-1}\) for
  \(a\ge1\), \(k(n;0,n)=2(-1)^n\); surviving set exactly
  \(S_n=\{a\ge1,\ a+b\le n\}\cup\{(0,n)\}\), \(|S_n|=n(n+1)/2+1\).
- **Lah factorization.** \(j=(-1)^{a+b}k = 2\binom{n}{b}L(n-b,a)\) with
  \(L\) the **unsigned Lah numbers** (partitions into ordered lists).
  Edge columns \(j(n;1,b)=2n!/b!\), \(j(n;a,0)=2L(n,a)\). A
  combinatorial reading of the V-operator is suggested and recorded as
  an open question — flagged to Nima as a cherish-worthy coincidence.
- **The induction (why all-n became cheap).** Two order-independent
  symbolic identities: the engine
  \(V(M)=(q-b)\sqrt2\,\omega(z-z_k)M/(1+u)\) on on-shape monomials (the
  off-shape pieces cancel via
  \(\bar z_k(z-z_k)-(1+z\bar z_k)=-(1+z_k\bar z_k)\) — the same
  cancellation that extincts \((0,1)\)), and the multiplication law
  \(c_i\,\mathrm{shape}=-\mathrm{shape}\). Hence the K-recursion
  \(k(n{+}1;a,b)=(n+a-b)k(n;a,b)-k(n;a-1,b)-k(n;a,b-1)\), which the
  closed form satisfies (machine-verified to order 60; a one-line
  binomial identity by hand). Nonvanishing on \(S_n\) is
  \(\binom{n-b-1}{a-1}\ge1\), so survival is exact and extinction
  propagates.
- **Corollaries for all \(n\).** Support law
  \(\operatorname{supp}G=[-(n-1),p]\); hence the fold law — closure iff
  \(2w_0+p\le0\) and grade \(\ge n-2w_0\), minimal pair
  \((n+2\lceil p/2\rceil,-\lceil p/2\rceil)\) — is upgraded from
  "certified through order 4" to theorem for every tower order. The rung
  ladder is a theorem: rung \(n+1\) forces
  \((n+2\lceil n/2\rceil,-\lceil n/2\rceil)\).

## Method note

The arc followed the cherish-the-coincidence rule: the factored forms
surfaced in a scratch intended only to support an induction, the
coefficient table was read against known sequences, and the Lah family
survived every attempt to explain it away. The proof structure — base
certified on data, induction step reduced to order-independent symbolic
identities, recursion checked as integer arithmetic — kept the
machine-certified and hand-derived parts cleanly separated.

## Verification

- Checker: `uv run --with sympy python research/strominger/checkers/channel_closedform_checks.py` — 14/14, exit 0 (groups K, U, P, C, X, V), re-run after final edit.
- Team notification admitted to the epistemic graph as event `ev-000000002509-2f90bf7e-8555-4b6d-9647-767aecb818bb` (reply to Nima's triage handoff `communication:f3b89e0488e2760d4a03`).

## Status boundary

Specialization-locus caveats stand: conclusions hold off
\(\bar z=\bar z_k\), \(1+z_k\bar z=0\) (generic in the reduced ring);
statements at special kinematics need separate arguments. The
combinatorial interpretation of the Lah factorization is open. The
rung-5 readout oscillation remains a prediction under the declared
fold-grade = readout-grade identification, not a certified readout.
