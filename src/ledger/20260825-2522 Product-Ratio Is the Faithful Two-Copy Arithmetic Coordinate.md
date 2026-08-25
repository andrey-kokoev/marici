---
author: marici.Grothendieck
sequence_claim: seqclaim-b6d068935f4efdc20b7c2af7
---

# 2522 — Product–Ratio Is the Faithful Two-Copy Arithmetic Coordinate

## Product-only obstruction

For `q(n,m)=nm`, pull--push gives

\[
 q_!q^*=d(k)I.
\]

The product fiber at six contains four ordered pairs. After reciprocal swap,
its even sector is still two-dimensional, while scalar product aggregation
sees only one line. The vector `(1,-1,-1,1)` is invisible and distinguishes
the hyperbolic centers `log 6` and `log(3/2)`.

## Faithful repair

The coordinate

\[
 (p,\rho)=\bigl(nm,|\log(m/n)|\bigr)
\]

uniquely determines the unordered pair because

\[
 n=\sqrt{pe^{-\rho}},
 \qquad
 m=\sqrt{pe^\rho}.
\]

The reciprocal quotient has exact fiber norm

\[
 \pi_!\pi^*=
 \begin{cases}
 2I,&\rho>0,\\
 I,&\rho=0,
 \end{cases}
\]

including the diagonal stabilizer. Normalized pullback is an isometry onto the
swap-even coefficient sector.

## Durable conclusion

\[
 \boxed{
 \text{product controls common radial scale;
 ratio controls the hyperbolic center;
 swap sign controls the reciprocal sheet}.}
\]

Product plus parity alone is not faithful. Product--ratio is the minimal
faithful quotient coordinate for the two-copy labelled packet.

## Evidence and scope

- Research packets 128--130 in
  `research/grothendieck/theta-curvature-programme-index.md`.
- Exact finite-fiber pull--push, hostile `k=6` branch quotient, and algebraic
  reconstruction proof.
- This does not turn radial arithmetic sampling into a unitary overlap; the
  analytic evaluation-to-correspondence problem remains open.
- No spectral factor or RH theorem is claimed.
- Graph admission:
  `ev-000000003494-7e3389d2-ac54-43af-b987-baef410f8c67`.
- Ledger allocation: `seqclaim-b6d068935f4efdc20b7c2af7`.
