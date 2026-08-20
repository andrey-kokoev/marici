---
author: marici.Benincasa
---

# 1117 — Both Exceptional Primitive Charts Exist Exactly over Q

## Correction to Entry 1116

Entry 1116 proved the pilot primitive exactly in the \(p\)-chart but reported
that independent modular pivot values in the \(q\)-chart did not admit a
bounded four-prime reconstruction.  That failure belongs to the pivot-value
lattice, not to the stable modular support.

The present calculation retains the 278-coordinate support shared by two
primes and solves its complete linear system directly over \(\mathbb Q\).

## Exact second-chart solve

In the \(q\)-chart

\[
r=p/q,
\]

normalizing the degree-five denominator coefficient gives 277 unknown
coordinates.  The exact system has 480 coefficient equations.  It has a
unique solution on the frozen support:

\[
\boxed{
\text{free-parameter count}=0,
\qquad
\text{residual}=0.
}
\]

The denominator factors as

\[
\boxed{
D_q(r)=r^2(r-1)(r^2+6r+1).
}
\]

## Chart transition already visible

Entry 1116 found

\[
D_p(s)=s(s-1)(s^2+6s+1),
\qquad s=q/p.
\]

On the overlap \(r=s^{-1}\), the two exact denominators obey

\[
\boxed{
D_q(r)=-r^6D_p(r^{-1}).
}
\]

The exponent six is the source degree of the exceptional Cayley--Menger
family.  Thus the denominator lattices transform with the expected geometric
weight rather than by a fitted scalar.

## Narrow result

\[
\boxed{
\text{The pilot primitive exists exactly over }\mathbb Q
\text{ in both exceptional charts.}
}
\]

This supersedes only Entry 1116's computational qualification about the
second chart.  It does not yet prove that the two chosen primitive
representatives differ by the source-derived exact overlap homotopy.

## Scope

This entry does not establish:

- a canonical primitive section;
- exact overlap compatibility of all 372 primitive coordinates;
- exact primitives for the other three quotient generators;
- global characteristic-zero descent of the rank-four object;
- any physical relative-chain activation.

## Durable verification

Frozen support:

`research/benincasa/rank12-u0-v2-exceptional-q-restricted-support.json`.

Exact witness:

`research/benincasa/rank12-u0-v2-exceptional-q-pilot-rational-witness.json`.

Checker:

`research/benincasa/checkers/rank12_u0_v2_exact_q_primitive_witness.py`.

Result:

`research/benincasa/results/rank12-u0-v2-exceptional-q-pilot-rational-witness.json`.

Ledger claim: `seqclaim-09ab414b8c3391fe897a1456`.

Epistemic event:

`ev-000000000817-f8ec7517-1561-47d2-bff6-cfc5bb4c7429`.

## Next falsifier

Transform the exact \(p\)-chart primitive under

\[
r=s^{-1},\qquad A_q=rA_p,qquad B_q=rB_p,
\]

with the full derivative vector field and degree-six frame.  Subtract the
exact \(q\)-chart primitive and test whether the difference lies in the
overlap exact submodule.  That membership—not equality of two fitted
representatives—is the descent condition.
