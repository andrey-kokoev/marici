---
author: marici.Kitaev
---

# 2217 — Sector Dephasing Is Not the D(S3) Central Readout Quotient

**Sector:** Kitaev (conditional expectation / operational quotient)

## Claim

For the frozen simple-sector decomposition, the central readout is the
conditional expectation

\[
\mathbb E_Z(X)=\sum_a\frac{\operatorname{Tr}(P_aX)}{d_a}P_a.
\]

It is a unital, trace-preserving, idempotent, Hilbert--Schmidt self-adjoint
quantum channel with 36 explicit Kraus operators.  It factors as sector
measurement followed by preparation of the maximally mixed state in the
recorded block, and is therefore measure--prepare and entanglement breaking.

This map is strictly coarser than sector dephasing.  Their dimensions are

\[
\begin{array}{c|cc}
&\dim\operatorname{im}&\dim\ker\\ \hline
\text{block dephasing}&36&220\\
\mathbb E_Z&8&248.
\end{array}
\]

The traceless diagonal inside the `C` block is fixed by dephasing but killed
by `E_Z`, with exact noncentral-pairing residual 2.

## Scope

This finite theorem constructs a canonical channel relative to the frozen
trace and block decomposition.  It does not prove that Hamiltonian controls
or a laboratory apparatus implement that channel.  Superselection dephasing
alone does not authorize the additional within-block depolarization.

## Durable verification

- Packet:
  `research/kitaev/s3-center-conditional-expectation-and-operational-quotient.md`
- Checker:
  `research/kitaev/checkers/check_s3_center_conditional_expectation.py`
- Result:
  `research/kitaev/results/s3-center-conditional-expectation.json`
- Command: `uv run --with sympy python -u research/kitaev/checkers/check_s3_center_conditional_expectation.py`
- Exact result: ten aggregate gates pass and fresh stdout matches the saved
  JSON after newline normalization.
- Epistemic graph event:
  `ev-000000003099-f40ecf22-8a82-4425-a605-04612388a6e4`
