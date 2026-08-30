# Rung 3: the sub-subleading S2 angular bridge — character ladder, third square-root gate, and kinematic closure

Companion to `checkers/rung3_s2_bridge_checks.py` (groups R1–R5, 25/25,
exit 0; results in `results/rung3_s2_bridge.json`). This packet opens rung
3 of the soft staircase — the sub-subleading Cachazo–Strominger \(S^{(2)}\)
— in the covariance-character framework of the descent-gate arc
(`diagonal-parity-cocycle.md`), on top of the grounded triangle maps
(`subsubleading-triangle-conventions.md`,
`subsubleading-triangle-source-boundary.md`, checks T1–T6).

Rungs 1 and 2 closed leg-summed under a conservation law: \(S^{(0)}\)
under \(\mathcal P\) (ledger 1056), \(S^{(1)}\) under \(\mathcal J\)
(ledger 1079). At rung 3, CS state that \(S^{(2)}\) is gauge invariant per
leg "and not as a consequence of any conservation law". This packet
certifies what replaces the law, computes the rung-3 readout's
P-covariance character, and answers the square-root existence question for
the third time — with a new outcome.

## 1. The grounded datum (R1)

The \(S^{(2)}\) datum is taken from the locally grounded sources [CS] =
arXiv:1404.4091 (tensor form (9), spinor form (20)) and [CL16] =
arXiv:1605.09094 (boundary form (14)), conventions of the sub-subleading
triangle packets. Explicitly declared, and re-certified in this checker:

- **Gauge prescription G_CS2.** Under the declared shift
  \(\delta E_{\mu\nu}=q_\mu\Lambda_\nu+\Lambda_\mu q_\nu\) the per-leg
  variation of CS (9) vanishes IDENTICALLY (R1.1b), from the antisymmetry
  mechanism \(q_\mu q_\nu J^{\mu\nu}=0\) alone (R1.1a). No conservation
  law, no \(\Sigma\)-constraint anywhere in the gauge step.
- **The per-leg sphere operator.** \(C=(\varepsilon^-\!\cdot q\cdot J)\)
  acts as \((c_{z_k},c_{\bar z_k},c_{E_k})=(-\sqrt2\,\omega(z-z_k)^2/
  (1+z\bar z),\ 0,\ -\sqrt2\,E_k\omega(z-z_k)(1+z\bar z_k)/((1+z\bar z)
  (1+z_k\bar z_k)))\) (R1.2), and the \(S^{(2)-}\) channels
  \(\omega^{-1}(2q\cdot k)^{-1}C^2\) have the grounded closed forms with
  the \(\partial_E\) first-order channel vanishing (R1.3).
- **Normalization explicit.** CS (9) per leg equals exactly \(-\omega\)
  times the CL16 (14) per-leg insertion (R1.4b); the ratio being
  \(-\omega\) and not \(1\) is retained as a typed residual (R1.4c), same
  family as the rung-2 \(\kappa\) residual S3. Never absorbed.

## 2. The rung-3 readouts and their P-covariance characters (R2)

On the P-invariant spin-2 anchor datum \(C_{zz}=(u+u^{-1})/z^2\),
\(u=z\bar z\), \(C_{\bar z\bar z}=\sigma(C_{zz})\) (spin-2 tensor
invariance \(P(C_{zz})=z^4C_{zz}\) re-certified, R2.1), the rung-3
angular readouts at derivative grade \(D_z^4\) are

\[
E_3 = D_z^4C_{zz}+D_{\bar z}^4C_{\bar z\bar z}
\quad\text{(electric, \(\sigma\)-even)},\qquad
M_3 = \partial_{\bar z}D_z^4C_{zz}-\partial_zD_{\bar z}^4C_{\bar z\bar z}
\quad\text{(magnetic, \(\sigma\)-odd)} .
\]

The separate diagonal weights at grade 4 are
\(P(D_z^4C_{zz})=z^{12}D_z^4C_{zz}\),
\(P(\partial_{\bar z}D_z^4C_{zz})=z^{12}\bar z^{2}\partial_{\bar z}D_z^4C_{zz}\)
and conjugates (R2.3). They collapse to SINGLE characters (R2.5)

\[
\boxed{\,P(E_3)=+\,u^{6}\,E_3\,}\qquad
\boxed{\,P(M_3)=-\,u^{7}\,M_3\,}
\]

via the exact datum identities (R2.4)

\[
(z^{12}-u^6)\,D_z^4C_{zz}+(\bar z^{12}-u^6)\,D_{\bar z}^4C_{\bar z\bar z}=0,
\qquad
(z^{10}+u^5)\,A_3=(\bar z^{10}+u^5)\,B_3 ,
\]

with \(A_3=\partial_{\bar z}D_z^4C_{zz}\), \(B_3=\partial_zD_{\bar z}^4
C_{\bar z\bar z}\). The rung-1 dilation-frame identity \(z^4A=\bar z^4B\)
does NOT lift to grade 4 (typed obstruction R2.4!, exact residual
retained) — the grade-4 identity is the weaker \((z^{10}+u^5)\) form.
The closed-form magnetic obstruction is

\[
P(M_3)-M_3=-(1+u^{7})\,M_3 ,
\]

with witness ratio \(-(1+(6/7)^7)=-1103479/823543\) at the fresh point
W2 \(=(3,2/7)\) (R2.6).

## 3. The character ladder and the third square-root gate (R3)

The certified P-covariance characters of the angular readouts now form
the ladder

| readout | \(\sigma\)-parity | character | exponent parity | square root |
|---|---|---|---|---|
| rung 0 electric \(E_0=D_z^2C_{zz}+\mathrm{c.c.}\) | +1 | \(+u^4\) | even | \(u^2\) |
| rung 1 magnetic \(M\) | −1 | \(-u^6\) | even | \(u^3\) |
| rung 3 electric \(E_3\) | +1 | \(+u^6\) | even | \(u^3\) |
| rung 3 magnetic \(M_3\) | −1 | \(-u^7\) | **odd** | **none** |

Signs alternate with \(\sigma\)-parity; exponents are non-decreasing
\([4,6,6,7]\). The square-root existence rule of the cocycle arc (C1.5:
even character parity permits a diagonal \(\sigma\)-invariant square
root, odd parity forbids it) now separates the two magnetic readouts:

- **Electric line, gate passes (R3.1):** \(u^6=(u^3)^2\) with
  \(\sigma(u^3)=u^3\) — the third even-parity square root exists, as it
  did for the cocycle (\(u^{-2}=(u^{-1})^2\)) and the rung-1 magnetic
  character (\(u^6\)).
- **Magnetic line, gate FAILS (R3.2):** \(u^7\) has odd valuation at
  \(u=0\) — no \(g\in\mathbb Q(u)\) squares to \(u^7\) (no integer
  solution of \(2m=7\); the odd family \(k=5,7,9\) is likewise rootless).
  No diagonal \(\sigma\)-invariant cocycle square root exists for the
  rung-3 magnetic readout, and the obstruction factor \(1+u^7\) is a
  nonzero rational function, so \(P(M_3)-M_3\) can never vanish.

**Structural resonance (recorded, not overclaimed).** The odd-parity
character obstruction on the rung-3 magnetic readout lands exactly where
[CL16] report lacking a first-principles derivation of the magnetic half
\(\tilde Q_{rX}\) (their lines 115–120). The character computation does
not prove anything about the charge construction; it does say that the
cocycle mechanism which certifies the diagonal parity structure at rungs
0–1 cannot extend to the rung-3 magnetic line in the same form — the
square root that the mechanism needs does not exist there. This is a
candidate cross-sector selection rule of the same family as C1.5, now
acting as an *obstruction* rather than an existence gate.

## 4. Per-leg residual and leg-summed closure under four law classes (R4)

The rung-2 bridge closed leg-summed under \(\sum_kJ_k=0\) with a named
nonzero per-leg residual \(M=D_z^2\mathrm{mix}^--D_{\bar z}^2
\mathrm{mix}^+\). At rung 3 each candidate law was tested separately:

- **Per-leg angular residual (R4.1): ZERO.** With the declared fold
  weight sequence \((-1,0,1,2)\) the regular part of the \(D_z^4\) fold
  of every \(S^{(2)-}\) operator channel vanishes per leg — "all terms
  are proportional to (derivatives of) delta functions" holds without
  any inter-leg input. Contrast rung 2's nonzero per-leg \(M\).
- **No-law (R4.2): closes.** The two-leg gauge variation with
  independent generic \(J_1,J_2\) vanishes with no \(\Sigma\)-constraint
  — each leg closes separately.
- **\(\mathcal P\) (R4.3): closes; law not load-bearing.** The per-leg
  variation vanishes for a single leg with fully generic momentum, where
  no \(\sum k=0\) relation can even be stated.
- **\(\mathcal J\) (R4.4): closes; law not load-bearing.** The typed
  contrast R4.4! shows what *would* need the law: the rung-2-grade
  variation \(\Lambda_\mu q_\nu J^{\mu\nu}\) is nonzero per leg without
  \(\sum J=0\). The \(\mathcal P\to\mathcal J\) escalation terminates.
- **Superrotation/boost (R4.5): closes; class not load-bearing.** The
  per-leg operator annihilates the gauge direction (R4.5a), and the
  smooth-superrotation baseline is obstructed exactly (R4.5b, H-B
  retained): the rung-2-grade \(D_z^3\) smearing leaves the pinned
  regular part \(-3(1+\bar z z_k)^3(1+z_k\bar z_k)/(E_k(1+z\bar z)^4
  (\bar z-\bar z_k))\); the \(D_z^4\) grade is forced.

**Verdict.** The rung-3 angular bridge closes leg-summed under all four
classes because it already closes PER LEG: the closure is kinematic
(J-antisymmetry), not conservation-law-mediated. This is the checkable
content of CS's "not as a consequence of any conservation law", and it
answers the packet-§8 research question in the H-A form with the
character-level refinement of §3: no successor conservation law exists
at rung 3, and the magnetic line — where a new charge would have to live
— is exactly where the square-root gate fails.

## 5. Typed residuals (none absorbed)

1. R1.4c: CS (9)/CL16 (14) per-leg ratio is exactly \(-\omega\), not 1.
2. R2.4!: the rung-1 identity \(z^4A=\bar z^4B\) does not lift to grade
   4; the grade-4 datum identity is the weaker \((z^{10}+u^5)\) form.
3. R4.4!: the rung-2-grade variation \(\Lambda\cdot q\cdot J\) is
   nonzero per leg without \(\sum J=0\) — retained as the termination
   marker of the \(\mathcal P\to\mathcal J\) escalation.
4. R4.5b: no smooth superrotation charge reproduces the rung-3
   distributional identity (H-B baseline falsified, pinned residual).
5. From the triangle arc, still open: the factor-\(\tfrac12\) delta
   drift (T3.5c), the magnetic half \(\tilde Q_{rX}\) first-principles
   derivation (CL16 lines 115–120), FPR collinear corrections, loop-level
   non-universality, and the rung-3 memory observable (H-mem).

## Verification

`uv run --with sympy python research/strominger/checkers/rung3_s2_bridge_checks.py`
— 25/25 pass, exit 0 (verified by the author from repo root); see
`research/strominger/results/rung3_s2_bridge.json`.
