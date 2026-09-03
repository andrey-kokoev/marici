# Modular provenance replay prototype

Problem: test whether sparse input-row combinations certify modular pivots and
dependencies.

Bold conjecture: carrying a provenance vector through every row operation gives
replayable certificates and detects corruption.

Rivals: rank-only reduction; pivot rows without source combinations; and
provenance output without replay checks.

Risky consequences: each pivot combination must reproduce its normalized row;
each null combination must reproduce zero; changing one certificate coefficient
must yield a nonzero residual.

Strongest falsification attempt: a six-row presentation over the prime 101
produced four pivot and two null certificates. All six replayed exactly. Every
one-coefficient corruption produced a nonzero residual. Maximum row and
provenance supports were three and four entries, respectively.

Disposition: retained for the bounded modular prototype. A certificate needs a
stable row id, normalized pivot, sparse source combination, prime, input digest,
and replay residual. This constructs no integral generator. The next test
measures whether provenance density is feasible for representative full Rees
prefixes or requires checkpointed replay.
