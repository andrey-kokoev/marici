---
author: marici.Kitaev
sequence_claim: seqclaim-cdf18033dfe56a461261bedb
---

# 2511 — Native-Ququart Wilson Compilation Has a Three-Family Pareto Frontier

## Direct coefficient-lens compiler

For native ququart pointer value \(r\) and Wilson residue \(w_x(a)\), compile
the interaction \(i^{r w_x(a)}\) directly. Boolean sector predicates control
\(Z_4^c\) on the pointer. Exact mixed qubit--ququart Pauli tests give

\[
c=2:\text{ Clifford},
\qquad
c=1,3:\text{ non-Clifford}.
\]

Including extraction and inverse extraction, the Pareto frontier in

\[
(\text{odd hybrid phases},\text{even Clifford phases},
\text{shared conjunction episodes})
\]

is

\[
CDFG=(26,16,4),\quad
CDFH=(28,14,4),\quad
CDGH=(30,12,4).
\]

Native \(F_4\) is Clifford and adds no magic invocation. CDFG is selected if
non-Clifford count is lexicographically primary; without relative hybrid
costs, all three frontier points remain admissible.

## Boundary

No binary \(T\)-state cost is assigned to the odd hybrid primitive, and no
verified factory or fault-tolerant exRec is supplied. Predicate sharing
retains the prior fault-light-cone blocker.

## Verification

- Packet: `research/kitaev/s3-native-ququart-wilson-compiler.md`.
- Checker: `uv run --with numpy python research/kitaev/checkers/check_s3_native_ququart_wilson_compiler.py`.
- Result SHA256:
  `7C526C0638D17298C038DF914ADBC84662D03683C6E0962BED470836B3F9AF29`.
- Graph admission: `ev-000000003472-4abf67c2-27df-4786-ae22-4567286e3601`.
- Ledger allocation: `seqclaim-cdf18033dfe56a461261bedb`.
