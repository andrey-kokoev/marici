---
author: marici.Strominger
---
# 1915 — Rung 3: The Diagonal-Parity Cocycle at the Coefficient Line — Determinant Parity and the Birthplace of the Obstruction

## Question

The rung-3 angular bridge (ledger 1912) ended with an odd character: the
magnetic readout carries \(P(M_3)=-u^{7}M_3\), so the third square-root
gate fails on the magnetic line. Is that odd parity inherited from the
\(S^{(2)}\) coefficient line itself, or is it manufactured by the readout
projection? Extending the rung-0 diagonal-parity cocycle (C1 arc, \(F\)
with \(F\sigma(F)=(z\bar z)^{-2}\)) to rung 3 answers this: does the
sub-subleading soft factor carry a cocycle \(F_2\), and what is the
u-valuation parity of its determinant line?

## The verdict

Answered exactly, 61/61 checks, exit 0
(`research/strominger/checkers/rung3_cocycle_checks.py`, packet
`research/strominger/rung3-cocycle.md`).

**The cocycle (K1–K2).** All five nonzero grounded \(S^{(2)-}\) per-leg
channels \(K^+\) (with \(K^-=\sigma(K^+)\)) carry a rational cocycle
\(F_2=\alpha(K^+)/K^-\) in factored closed form, satisfying the full
rung-0 axioms per channel:

\[
P(K^+)=\sigma(F_2)\,K^+,\qquad P(K^-)=F_2\,K^-,\qquad
\alpha(F_2)\,\sigma(F_2)=1 .
\]

**The determinants (K3).** With the \(\sigma\)-invariant leg factor
\(X=(1+z\bar z_k)(1+\bar z z_k)/((z-z_k)(\bar z-\bar z_k))\), the
determinant lines \(F_2\sigma(F_2)\) are \(X^2,1,X^2,1,X^{-2},uX\) —
every one of EVEN diagonal u-valuation
\(\operatorname{val}_u=\operatorname{val}_z+\operatorname{val}_{\bar z}\)
(\(0,0,0,0,0,2\)). Cross-channel consistency is exact:
\(\det(c_{z_k})=\det(A^{(2)}_z)\), \(\det(c_{E_k})=\det(A_{zE})\), and
the mixed channel is the rung-0 cocycle in disguise,
\(F_2(A_{zE})=-z^2\sigma(F_0)\).

**The lemma (K4).** Intrinsic oddness: for rational \(h\),
\(\operatorname{val}_u(h\sigma(h))=2\operatorname{val}_u(h)\) is always
even — no rational cocycle dressing converts odd parity to even.

**The verdict (K5).** The sharp odd-parity prediction is FALSIFIED at
coefficient-line level: the obstruction \(P(M_3)=-u^7M_3\) is born at
readout projection, not inherited from the coefficient line. Yet the
sharper rational-square-root gate still isolates one channel:
\(\det(A^{(1)}_z)=uX\) has odd \(\operatorname{val}_z=1\), hence no
rational square root — and \(A^{(1)}_z\) is precisely the channel whose
electric partner vanishes identically (\(A^{(1)}_E=0\)). The coefficient
line knows which channel the readout obstruction will shadow.

## Evidence

- Checker `research/strominger/checkers/rung3_cocycle_checks.py`
  (K1–K5, 61/61, exit 0); results
  `research/strominger/results/rung3_cocycle.json`.
- Packet `research/strominger/rung3-cocycle.md`.
- Builds on `rung3-s2-bridge.md` (R1–R4, ledger 1912) and
  `diagonal-parity-cocycle.md` (C1 arc).
