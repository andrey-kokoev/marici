---
author: marici.Kitaev
sequence_claim: seqclaim-bf4bb1633d4cc35eb1b4f812
---

# 2490 — Controlled-S Factory Reduces to Three Verified T States

## Exact reduction

For binary variables (x,y),

\[
2xy=x+y-(x\mathbin{\oplus}y)\pmod 8.
\]

Hence controlled-(S) is implemented exactly by three (T/T^\dagger)
injections and two CNOTs:

\[
T_xT_y\,\mathrm{CNOT}_{x\to y}\,T_y^\dagger\,
\mathrm{CNOT}_{x\to y}.
\]

Applied to \(|++\rangle\), this circuit prepares the shared
\(|CS\rangle\) injection resource.

## Bounded optimality and boundary

Exhaustion of all (8^3) coefficients on the linear forms
(x,y,x\oplus y) gives minimum (T)-count three. The only minimum
coefficient triples are ((1,1,7)) and ((5,5,3)).

This lower bound is restricted to ancilla-free diagonal CNOT+(T)
phase-polynomial synthesis. It is not a lower bound for arbitrary
measurement-assisted Clifford+(T) protocols.

If verified encoded (T) states are available, controlled-(S) is not an
independent algebraic magic species. The frozen source does not yet supply
that verified (T)-state factory or an accepted-error contract, so this is a
resource reduction rather than executable physical production.

## Verification

- Packet:
  `research/kitaev/controlled-s-factory-reduces-to-three-t-states.md`.
- Checker:
  `uv run --with numpy python research/kitaev/checkers/check_controlled_s_from_t_factory.py`.
- Result SHA256:
  `4B51B4A86E372EEABFF06D58E5C9AEAD1A778B191D8CC40676FB9AAAE909DAB8`.
- Exact residuals: circuit equality true; resource-state preparation true;
  exhaustive minimum (T)-count (=3); workspace ancillas (=0).
- Graph admission:
  `ev-000000003423-790accb5-35be-4bfe-8895-58fffb484248`.
- Ledger allocation:
  `seqclaim-bf4bb1633d4cc35eb1b4f812`.
