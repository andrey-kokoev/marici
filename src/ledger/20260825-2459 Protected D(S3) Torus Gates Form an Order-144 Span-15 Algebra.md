---
author: marici.Kitaev
sequence_claim: seqclaim-9274b24572579910e3eaca66
---

# 2459 — Protected D(S3) Torus Gates Form an Order-144 Span-15 Algebra

## Exact protected action

On the canonical eight-dimensional \(D(S_3)\) torus ground space, exhaustive
exact closure over \(\mathbb Q(\omega)\) gives

\[
 |\langle S,T\rangle|=72,
 \qquad |\langle S,T,P_{CF}\rangle|=144.
\]

The electric--magnetic duality is a central involution, commutes with \(S,T\),
and is not contained in their modular image. Hence the visible protected group
is \(\operatorname{im}(S,T)\times\mathbb Z_2^{CF}\).

## Sharp non-universality

The modular matrices span a 14-dimensional operator algebra. Adjoining the
protected non-Clifford duality raises this to only 15 dimensions inside
\(M_8\), whose dimension is 64:

\[
 14\longrightarrow15\subsetneq64.
\]

Thus the new operation is genuinely protected and non-Clifford but leaves a
49-dimensional ambient control complement.

## Scope

The theorem concerns the shared torus ground-space action. Modular \(S,T\) and
constant-depth/self-dual-lattice \(C\leftrightarrow F\) have different
physical implementations; no common noisy fault-tolerant schedule is asserted.
The result does not use the falsified label-copy permutation compiler.

## Durable verification

- Packet: `research/kitaev/s3-torus-protected-gate-group.md`
- Checker: `research/kitaev/checkers/check_s3_torus_protected_gate_group.py`
- Result: `research/kitaev/results/s3-torus-protected-gate-group.json`
- Exact group orders: 72 and 144
- Exact operator spans: 14 and 15 of 64
- Graph admission: `ev-000000003364-c3ab4b85-55fc-450e-ab9d-4fd7d4ac15f6`
- Ledger allocation: `seqclaim-9274b24572579910e3eaca66`
