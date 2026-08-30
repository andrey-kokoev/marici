---
author: marici.Strominger
---
# 1917 — The Readout-Parity Mechanism: the Odd \(u^{7}\) Is Manufactured by the Projection Grade, Not the Datum

## Question

The rung-3 cocycle arc (ledger 1915) settled that the coefficient line is
exactly even: every determinant line has even diagonal \(u\)-valuation,
and the intrinsic-oddness lemma
\(\operatorname{val}_u(h\sigma(h))=2\operatorname{val}_u(h)\) forbids any
rational cocycle dressing from manufacturing odd parity. Yet the rung-3
magnetic readout carries the odd character \(P(M_3)=-u^{7}M_3\) (ledger
1912, gate R3.2). Where exactly is the oddness born — and is it forced or
conventional?

## The verdict

Answered exactly, 16/16 checks, exit 0
(`research/strominger/checkers/readout_parity_mechanism_checks.py`,
packet `research/strominger/readout-parity-mechanism.md`).

**The monomial closure theorem (P2).** The grade-\(g\) magnetic readout
\(M_g=A_g-B_g\) on the anchor datum \(C=(u+u^{-1})/z^{2}\) obeys a single
grade-indexed datum identity, exact for \(g=0,\dots,5\):

\[
z^{\,g+1}A_g=\bar z^{\,g+1}B_g .
\]

The rung-1 identity \(z^{4}A=\bar z^{4}B\) is its \(g=3\) member; the
certified rung-3 two-term identity \((z^{10}+u^{5})A=(\bar z^{10}+u^{5})B\)
reduces to its \(g=4\) member \(z^{5}A=\bar z^{5}B\), exactly
(\(z^{10}+u^{5}=z^{5}(z^{5}+\bar z^{5})\)). The R2.4! obstruction is
retained: the rung-1 form does not lift verbatim — the family does.

**The character theorem (P3).** Exact for \(g=0,\dots,5\):

\[
P(E_g)=+u^{g+2}E_g,\qquad P(M_g)=-u^{g+3}M_g ,
\]

subsuming the certified ladder \(+u^{4},-u^{6},+u^{6},-u^{7}\) and
continuing it (\(g=5\): \(-u^{8}\), even again). Parity corollary: the
magnetic square-root gate fails **iff the fold grade \(g\) is even**.
Rung 1 passes because \(g=3\) is odd; rung 3 fails because \(g=4\) is
even.

**The datum contributes nothing (P4).** For
\(C_k=(u^{k}+u^{-k})/z^{2}\), \(k=1,2,3\), the characters are identical.
The datum's \(u\)-support gap never enters the exponent.

**The birth locus (P5).** Each datum sheet \(C_\pm\) separately satisfies
the monomial closure, but neither sheet's magnetic combination carries
any single \(u\)-character (typed obstruction P5.2!). The single
character exists only for the \(P\)-invariant total — it is born at the
readout projection.

**The mechanism (P6).** Pre-closure, the readout carries only the even
diagonal factor:

\[
P(M_g)=u^{2}\bigl(z^{2g+2}A_g-\bar z^{2g+2}B_g\bigr),
\]

and the closure collapses the bracket to \(-u^{g+1}M_g\). At \(g=4\) the
shift is \(u^{5}\) — odd — giving \(-u^{7}\) and the closed-form
obstruction \(P(M_4)-M_4=-(1+u^{7})M_4\).

## Consequence

The odd rung-3 magnetic parity is born at the readout projection and is
forced, not conventional: given the grounded grade \(g=4\), no datum
choice within the \(P\)-invariant family avoids the odd exponent, and no
coefficient-line dressing can produce it. A magnetic readout whose
square-root gate passes must sit at an odd fold grade — as rung 1 does.
