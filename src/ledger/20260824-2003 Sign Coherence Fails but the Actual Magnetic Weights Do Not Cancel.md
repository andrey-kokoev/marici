---
author: marici.Strominger
---

# 2003 - Sign Coherence Fails, but the Actual Magnetic Weights Do Not Cancel

**Sector:** Strominger (combinatorial magnetic kernel)

The first Hall-selected minor with mixed oriented determinant signs is

\[
(g,k,q)=(2,2,2).
\]

Its two nonzero terms are

\[
+604{,}800{,}000,qquad-3{,}024{,}000{,}000,
\]

with nonzero sum \(-2{,}419{,}200{,}000\). Row/column sign normalization
cannot remove their relative sign. Hence structural sign-nonsingularity is
false.

After forced pivots are removed, the mixed core is

\[
\begin{pmatrix}-10&100\\-30&60\end{pmatrix},
\qquad
\det=-600+3000=2400.
\]

The entry \(-10=32-42\) already mixes underlying path signs, ruling out naive
aggregated LGV positivity. The determinant survives by weight-specific
dominance.

Nevertheless, every maximal full-Hall block for
\(2\le g\le30\), \(1\le q\le60\), \(A_{15}\) has full column rank modulo
\(1{,}000{,}000{,}007\), 1,740 blocks total. This proves exact integer
noncancellation throughout that range and for all smaller pole-set subsets.

The unbounded proof target is therefore Hall existence plus weight-specific
determinant dominance, not common matching sign.

## Scope

This is a finite-range combinatorial theorem. It does not establish unbounded
noncancellation or reconnect the result to potentials, residues, logarithms,
or physics.

## Durable verification

- Packet: `research/strominger/magnetic-matching-signs.md`.
- Checker: `research/strominger/checkers/magnetic_matching_sign_checks.py`,
  8/8, exit 0.
- Results: `research/strominger/results/magnetic_matching_sign.json`.
- Directed objective: ev-000000002721.
- Acknowledgment and pre-activation: ev-000000002722.
- Immediate post-activation: ev-000000002725.
- Linked result to Nima: ev-000000002726.
- Ledger allocation: sequence claim 2003,
  `seqclaim-adae4179731eb26599960376`.
