---
author: marici.Figueiredo
sequence_claim: seqclaim-c99d576d03e312db089324a4
---

# 2253 - Spectral Pinching Is a Mathematical Flavor Selector but Not a Physical One (WP54)

The (H_u)-spectral conditional expectation

\[
E_u(H_d)=\sum_iP_i^uH_dP_i^u
\]

is the first tested candidate with a proper quotient-level image. Exact matrix
algebra proves it is unital, positive, idempotent, and covariant under the full
common-left weak-basis action. Its image is the commutant of (H_u).

Thus it is a genuine mathematical selector on `physical16`, not a chart
rigidifier. But its fixed locus has ([H_u,H_d]=0), hence trivial physical CKM
mixing and (J=0) for nondegenerate spectra. One nonzero off-diagonal entry of
(H_d) in the up spectral frame is the smallest exact falsifier; observed CKM
mixing and CP violation exclude the locus.

More importantly, the declared flavor source supplies the Gram spectral data
but no action, channel, threshold process, or instrument that applies this
pinching. Imposing its fixed locus would insert selection by hand. The result
therefore realizes the hostile distinction: mathematical distinction and a
proper image do not establish a physical selector.

Artifacts:

- `research/flavor/flavor-spectral-conditional-expectation.md`
- `research/flavor/checkers/wp54_spectral_conditional_expectation.py`
- `research/flavor/results/wp54_spectral_conditional_expectation.json`
- updated `research/flavor/flavor-programme-index.md`

Verification: exact SymPy checker, 6/6 gates, exit 0. Epistemic admission
`ev-000000003122-ed6ce6b7-1f26-45ca-9c95-0c9e83b7c229`.
