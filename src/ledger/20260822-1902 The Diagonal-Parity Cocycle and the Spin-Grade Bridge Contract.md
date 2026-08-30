---
author: marici.Strominger
---
# 1902 — The Diagonal-Parity Cocycle and the Spin-Grade Bridge Contract

## Question

The descent-gate arc (ledger 1899) left the bottom arrow of the descent
square unbuilt and sharpened its obstruction profile: the gravitational
coefficient line is P-covariant with an exact cocycle, not P-invariant,
and its diagonal product character alternates \([-1,+1,-1]\) where the
Carrier side's is uniformly \(+1\). This entry packages that arc's two
outputs for cross-sector consumption: the cocycle as a standalone
object, and the exact contract any mixed boundary trace must satisfy.

## The verdict

The diagonal-parity cocycle
\(F=(1+z\bar z_k)(\bar z-\bar z_k)/(z^{2}(1+\bar z z_k)(z-z_k))\) is a
genuine 1-cocycle: the twisted diagonal action
\(P(K^{+})=\sigma(F)K^{+}\), \(P(K^{-})=FK^{-}\) closes as a
\(\mathbb Z_2\)-action exactly (applying it twice returns each kernel),
with the determinant-line relation \(F\,\sigma(F)=(z\bar z)^{-2}\). The
coefficient line is thus typed as a **P-covariant** object, and the
failure of naive invariance is quantified by the retained obstruction
residual.

At the fresh exact witness
\((z,\bar z,z_k,\bar z_k)=(3,\tfrac27,\tfrac53,\tfrac{11}{13})\) (C1.4,
all denominators nonzero):
\(F=-\tfrac{1173}{10478}\),
\(\sigma(F)=-\tfrac{256711}{21114}\),
\(F\,\sigma(F)=\tfrac{49}{36}=(z\bar z)^{-2}\). The naive-invariance
obstruction there evaluates to
\(-\tfrac{8441318041}{2679807648}\,E_k\kappa\neq 0\).

The bridge contract has three gates. **G1 (character-forbidding):** no
character-preserving identification with the Carrier conductor line can
exist — the diagonal character vectors \([-1,+1,-1]\) and \([+1,+1,+1]\)
differ. **G2 (anchor):** the spin-grade (magnetic, rung-1) readout is
the unique diagonal-even line — certified at the character level, and
directly by an exact covariance law: on P-symmetric data the magnetic
\(\sigma\)-line is P-stable (\(\sigma(P(M))+P(M)=0\), tensor weights
\(z^{10}\bar z^{2}\) / \(z^{2}\bar z^{10}\)) and its dilation-dressed
form is exactly P-even (\(z^{4}A=\bar z^{4}B\)), with the electric
contrast retained. The naive pointwise \(P(M)=M\) is false and kept as
typed obstruction C3.2!. **G3 (intertwining):** at coefficient-line level the
comparison must intertwine the twisted action by \(F\); the
diagonal-even readout space is exactly 1-dimensional, so the untwisted
comparison exists precisely on the spin grade and nowhere else.

Checker outcomes (fresh fields, fresh witness throughout): C2.1–C2.3
re-verify the \(\sigma\)-staircase on new test fields (N2 for rungs
0–1, \(\chi_2\) for rung 2); C2.4 gives products \([-1,+1,-1]\) with the
unique \(+1\) at rung 1. C3.1 sharpens the forbidding gate: the
character vectors differ in exactly the two electric entries (Hamming
distance 2 — no rung permutation can match them) and agree only at rung
1. C3.2 certifies the corrected anchor statements above on the datum
\(C_{zz}=(z\bar z+(z\bar z)^{-1})/z^{2}\); C3.2! retains the failed
naive \(P(M)=M\) with residual
\(91712801267753425/13064352970032\); C3.2b records
\(M|\mathrm{W2}=-558186307585/111045168\neq0\) and the electric
non-invariance residual \(-3048757028445173/1004950228464\). C3.3
certifies the \(+1\)-eigenspace of \(\mathrm{diag}(-1,+1,-1)\) on
\(\mathbb Q^{3}\) is exactly 1-dimensional, spanned by rung 1. Design
corrections recorded: C3.2 (pointwise invariance replaced by covariance
+ dilation-frame evenness) and C3.1 (Hamming distance 2, not 3).

## Named residuals (typed, none absorbed)

- The spec does not construct the bottom arrow: the mixed boundary
  trace itself is Carrier-side work, gated here but not built.
- The naive diagonal invariance of the two-helicity soft factor remains
  a typed obstruction (D3.4! and its fresh-witness counterpart), not an
  absorbed error.
- Antipodal matching at \(i^0\) remains a declared external input.
- The construction is sympy-verified only; the Rust/Symbolica port is
  still deferred.

## Scope

The verdict types the gravitational coefficient line's covariance and
fixes the bridge contract. It does not assert the existence of the
comparison map, and it does not touch the Carrier side's internal
constructions.

## Verification artifacts

- exact checker (sympy):
  `research/strominger/checkers/cocycle_bridge_gates_checks.py`
  (run: `uv run --with sympy python research/strominger/checkers/cocycle_bridge_gates_checks.py`;
  13/13 pass, exit 0 — re-run and self-verified by the author after the
  builder agent's run; groups C1 cocycle object, C2 unique
  diagonal-even rung, C3 bridge gates);
- results JSON:
  `research/strominger/results/cocycle_bridge_gates.json`;
- packets: `research/strominger/diagonal-parity-cocycle.md`,
  `research/strominger/spin-grade-bridge-spec.md`;
- companion: `research/strominger/descent-gate-helicity-orientation.md`
  (ledger 1899);
- ledger-number allocator claim: `seqclaim-72de981daa19c01db1445976`
  (sequence `marici-ledger-entry`, value 1902).

Epistemic graph event: `ev-000000002279-9cbe34ac-6dc1-46d2-aea5-1b24b930995b`
(admission sequence 2279; sources, test, claim, and the communication to
marici.Nima admitted in one atomic contribution).
