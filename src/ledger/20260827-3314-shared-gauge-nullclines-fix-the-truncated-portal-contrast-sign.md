# Shared Gauge Nullclines Fix the Truncated Portal-Contrast Sign

Author: `marici.Figueiredo`

## Claim

The separately published one-loop model-A and model-B Yukawa nullclines of
arXiv:2008.08606 can be evaluated over common electroweak gauge coordinates
without identifying their scalar flavor frames. Including a common top-bottom
contribution, the induced additive portal contrast has the form

\[
-4q_A+3q_B=\frac{2g_1^2}{27225}P(r,t),
\]

where (r=g_2/g_1), (t=(\alpha_t+\alpha_b)/g_1), and (P(r,t)) is strictly
positive throughout the domain where the displayed Yukawa nullcline
coordinates are positive. Hence the cancellation ratio (q_B/q_A=4/3) is
absent from that truncated domain.

## Boundary

The simultaneous A+B theory contains cross anomalous-dimension terms through
the shared Standard Model lepton and Higgs fields, and its combined matter
content changes the gauge beta functions. These effects are absent from the
separately published systems. The result fixes the truncated sign, not the
full-theory magnitude or RG basin.

## Verification

- Packet:
  `research/flavor/flavor-gauge-parallelized-yukawa-contrast-sign-theorem.md`
- Checker:
  `research/flavor/checkers/wp733_gauge_parallelized_yukawa_contrast_sign.py`
- Result:
  `research/flavor/results/wp733_gauge_parallelized_yukawa_contrast_sign.json`
- Exact checker outcome: 12/12 PASS.
- Epistemic-graph admission:
  `ev-000000007085-8fc1e1f4-bfb1-4a74-8f04-eb9175a611bf`.
- Primary source: arXiv:2008.08606v1, equation A.1 and table 7.

## Remaining gate

Derive the simultaneous gauge–Yukawa beta system, including cross A/B
anomalous dimensions and combined gauge coefficients, and test whether the
strict sign and irrelevant contrast margin survive its interacting fixed
point.
