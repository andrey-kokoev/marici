---
author: marici.Strominger
---

# The Fold Law Is Derived, Not Fitted: Covariant Chain, Diagonal Kernel, the [−(n−1), p] Support Law, and the ⌈p/2⌉ Depth Floor

**Sector:** Strominger (soft theorems / memory / cocycle program)
**Artifacts:** `research/strominger/rung4-foldrule.md` (packet),
`research/strominger/checkers/rung4_foldrule_checks.py` (16/16, exit 0),
`research/strominger/results/rung4_foldrule.json`;
`research/strominger/rung4-foldgrade.md` (Update note corrected)

## What was done

The depth-graded fold rule of the previous arc was a pattern fitted to the
order-2/3 closure table. This arc found its **mechanism** and, through it,
discovered that the fitted rule was wrong at the first untested point. The
law is now derived end to end and re-certified on all 22 channels of tower
orders 2, 3, 4.

## Results

- **Mechanism (checker group M, certified).** The fold's regular part IS
  the covariant chain \(D_{w_0+g-1}\cdots D_{w_0}(G)\),
  \(D_w=\partial_z-w\Gamma\), and the connection trivializes:
  \(D_w=S^{-w}\partial_z S^{w}\), \(S=(1+u)^2\). In \(x=1+u\) the chain is
  \(\bar z^{g}x^{-2(w_0+g-1)}(\partial_x M_{x^2})^{g-1}\partial_x(x^{2w_0}G)\);
  \(\partial_x M_{x^2}\) is diagonal on monomials
  (\(x^e\mapsto(e+2)x^{e+1}\)), so the coefficient of \(x^e\) acquires the
  factor \(e(e+1)\cdots(e+g-1)\). The kernel is exactly
  \(\operatorname{span}\{x^{-(g-1)},\dots,x^0\}\). Closure is pure support
  arithmetic: \(\operatorname{supp}(x^{2w_0}G)\subseteq\ker\).
- **Support law (group S, UNREDUCED, all 22 channels).**
  \(\operatorname{supp}G=[-(n-1),\,p]\) exactly, no interior gaps; the lower
  edge is the pole law of the previous arc, the upper edge is \(p\) with
  single-term factored edge coefficients — no cancellation possible.
- **The law (R2/R3, 22/22).** Channel \((a,b)\), \(p=a+b\), closes iff
  \(2w_0+p\le0\) and grade \(\ge n-2w_0\); minimal pair
  \((n+2\lceil p/2\rceil,\,-\lceil p/2\rceil)\). Closures certified, both
  sharpness directions witness-proven (one grade below at minimal weight;
  one weight shallower at the same grade — the weight gate fails there
  independent of grade).
- **Correction, recorded.** The fitted rule \(k\ge\max(1,p-1)\) coincides
  with \(\lceil p/2\rceil\) for all \(p\le3\) — every datum then in hand —
  and is **refuted at \(p=4\)**: the five order-4 \(p=4\) channels close at
  \((8,-2)\), not first at \((10,-3)\) (certified; grade 7 open,
  witness-proven). The discriminate-and-test discipline caught what the fit
  could not.
- **Grounded-weight explained.** Every tower channel has \(p\ge1\), so no
  channel ever closes at \(w_0=0\).
- **Rung-5 consequence.** The full-operator minimal pair at order 4 is
  \((8,-2)\), not \((10,-3)\). Parity unchanged (even), so the
  character-theorem prediction stands: electric gate passes (root \(u^5\)),
  magnetic gate FAILS at rung 5.

## Method note

Finite-fiber discipline held throughout: nonzero claims witness-proven
(exact), zero claims certified symbolically in the proven-faithful reduced
ring, and the support law certified unreduced. The order-4 fork between the
two candidate rules (\(k\ge p-1\) vs the kernel law) was settled by
designing discriminating points where the rules disagree *before* trusting
either — the mechanism (chain reduction + kernel) then explained the
answer. A t-tagging probe (deleted scratch) showed the closure is pure
interference across connection-count sectors — no termwise mechanism in
connection count — which is what forced the covariant-chain viewpoint.

## Verification

- Checker: `uv run --with sympy python research/strominger/checkers/rung4_foldrule_checks.py` — 16/16, exit 0 (groups H, M1–M5, S, R1–R5).
- Team notification admitted to the epistemic graph as event `ev-000000002484-dc64291c-9ba5-4288-bf37-064128d34244` (reply to Nima's triage handoff `communication:f3b89e0488e2760d4a03`).

## Status boundary

The law is certified on tower orders \(\le4\) (support law) and the chain
identity on orders \(\le3\) plus a sample; no all-\(n\) induction is
recorded — the mechanism reduces higher orders to a support computation,
but that computation is certified only through order 4. The rung-5 readout
oscillation is a prediction under the declared fold-grade = readout-grade
identification, not a certified readout. The refuted rule remains visible
in the packet's correction note and in the history of
`rung4-foldgrade.md`'s Update paragraph.
