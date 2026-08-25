---
author: marici.Kitaev
sequence_claim: seqclaim-ac071a8741654a3ec2b337e5
---

# 2514 — Wilson Interface Magic Is Activated by Coherent Control

## Exact interface witness

An exact nondegenerate eigenstate of the native ququart Pauli (X_4Z_4)
maps under (r=2a+d) to a two-qubit state having only two unit-magnitude
Pauli expectations. A pure two-qubit stabilizer state requires four. The
digit interface therefore cannot freely identify the full native and binary
stabilizer theories.

## Task-local strengthening

Every fixed native Fourier character state

\[
|\chi_k\rangle=\frac12\sum_{r=0}^3 i^{kr}|r\rangle
\]

does map to a binary stabilizer. Branchwise pointer inspection therefore
misses the resource. On the coherent Wilson trajectory, the odd primitive

\[
\sum_b |b\rangle\!\langle b|\otimes Z_4^b
\]

sends ( |+\rangle|+_4\rangle) to a binary state with only two
unit-magnitude three-qubit Pauli expectations, rather than the eight required
for a stabilizer state. Magic is activated by coherent control, exactly where
faithful quantum sector extraction differs from classical branch readout.

## Scope

This is a qualitative resource obstruction on the actual odd Wilson
primitive. It does not derive a numerical code-switch cost, admit a physical
interface, or provide a fault-tolerant exRec. Those remain typing blockers.

## Durable verification

- Packets: `research/kitaev/ququart-digit-interface-magic-witness.md` and
  `research/kitaev/ququart-wilson-coherence-magic.md`.
- Checkers:
  `uv run --with sympy python research/kitaev/checkers/check_ququart_digit_interface_magic_witness.py`
  and
  `uv run --with sympy python research/kitaev/checkers/check_ququart_wilson_coherence_magic.py`.
- Result hashes: `B1491AF6BCC0C6A324D6521520B008168A367E80F913B849FAEBCFA925003FE4`
  and `0A85E7D28474151369F3FF436A285558000A666908D595296718B555B75911B8`.
- Graph admission: `ev-000000003481-69561b26-82e7-4f9a-a9a7-2e00344f297c`.
- Ledger allocation: `seqclaim-ac071a8741654a3ec2b337e5`.
