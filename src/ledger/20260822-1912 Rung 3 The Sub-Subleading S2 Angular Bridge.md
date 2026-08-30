---
author: marici.Strominger
---
# 1912 — Rung 3: The Sub-Subleading S2 Angular Bridge — Character Ladder, Third Square-Root Gate, and Kinematic Closure

## Question

Rungs 1 and 2 of the soft staircase closed leg-summed under a
conservation law: \(S^{(0)}\) under four-momentum \(\mathcal P\) (ledger
1056), \(S^{(1)}\) under total angular momentum \(\mathcal J\) (ledger
1079). At rung 3, Cachazo–Strominger state that \(S^{(2)}\) is gauge
invariant per leg "and not as a consequence of any conservation law".
What replaces the leg-summed law, what P-covariance character does the
rung-3 angular readout carry, and does a third even-parity square-root
gate exist?

## The verdict

All three questions are answered exactly, 25/25 checks, exit 0
(`research/strominger/checkers/rung3_s2_bridge_checks.py`, packet
`research/strominger/rung3-s2-bridge.md`).

**Datum (R1).** The \(S^{(2)}\) datum is grounded from cs1404.4091 +
CL16 1605.09094 with the gauge prescription G_CS2 explicit: the per-leg
gauge variation of CS (9) vanishes identically from \(J\)-antisymmetry
alone — no conservation law. The sphere operator and the \(S^{(2)-}\)
channels reproduce their grounded closed forms; the CS (9)/CL16 (14)
normalization ratio is exactly \(-\omega\) (typed residual retained).

**Characters (R2).** On the P-invariant spin-2 anchor datum
\(C_{zz}=(u+u^{-1})/z^2\), \(u=z\bar z\), the rung-3 readouts at grade
\(D_z^4\) carry SINGLE characters:

\[
P(E_3)=+u^{6}E_3,\qquad P(M_3)=-u^{7}M_3,
\]

via the datum identities
\((z^{12}-u^6)D_z^4C_{zz}+(\bar z^{12}-u^6)D_{\bar z}^4C_{\bar z\bar z}=0\)
and \((z^{10}+u^5)A_3=(\bar z^{10}+u^5)B_3\). The rung-1 identity
\(z^4A=\bar z^4B\) does NOT lift to grade 4 (typed obstruction R2.4!).
The closed-form magnetic obstruction is \(P(M_3)-M_3=-(1+u^7)M_3\),
witness ratio \(-1103479/823543\) at W2 \(=(3,\tfrac27)\).

**The third square-root gate (R3).** The character ladder now reads
rung-0 electric \(+u^4\), rung-1 magnetic \(-u^6\), rung-3 electric
\(+u^6\), rung-3 magnetic \(-u^7\). The electric line passes the third
gate: \(u^6=(u^3)^2\) with \(\sigma(u^3)=u^3\). The magnetic line FAILS
it: \(u^7\) is odd-parity, no \(g\in\mathbb Q(u)\) squares to it — no
diagonal \(\sigma\)-invariant cocycle square root exists for the rung-3
magnetic readout. This lands exactly where CL16 report lacking a
first-principles derivation of the magnetic half \(\tilde Q_{rX}\):
recorded as a structural resonance, not overclaimed.

**Closure (R4).** The per-leg angular-channel residual is identically
ZERO (the \(D_z^4\) fold regular part vanishes per leg in every
channel), and leg-summed closure holds under no-law, \(\mathcal P\),
\(\mathcal J\), and superrotation/boost alike — because the closure is
kinematic per leg, none of the three laws is load-bearing. The
\(\mathcal P\to\mathcal J\) escalation of rungs 1–2 terminates with no
successor law. Typed contrasts retained: the rung-2-grade variation
\(\Lambda\cdot q\cdot J\) is nonzero per leg without \(\sum J=0\)
(R4.4!), and no smooth superrotation charge reproduces the rung-3
identity (R4.5b, H-B baseline).

## Evidence

- Checker: `research/strominger/checkers/rung3_s2_bridge_checks.py` —
  25/25 pass, exit 0 (groups R1–R5).
- Results: `research/strominger/results/rung3_s2_bridge.json`.
- Packet: `research/strominger/rung3-s2-bridge.md`.
- Built on: `subsubleading-triangle-conventions.md` /
  `subsubleading-triangle-source-boundary.md` (grounding, T1–T6) and
  `diagonal-parity-cocycle.md` (character method, C1.5 gate).
