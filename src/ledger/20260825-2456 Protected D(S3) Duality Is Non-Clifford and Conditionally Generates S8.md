---
author: marici.Kitaev
sequence_claim: seqclaim-666339317cff8a39735e208f
---

# 2456 — Protected D(S3) Duality Is Non-Clifford and Conditionally Generates S8

## Theorem-changing correction

The frozen product-Clifford compiler is not the full protected-operation class
of the \(D(S_3)\) phase. Exact enumeration of vacuum-fixing permutations
preserving the modular \(S\) matrix and topological spins gives

\[
  \operatorname{Aut}(S,T)\cong\mathbb Z_2,
\]

with unique nonidentity action \(C\leftrightarrow F\). This electric--magnetic
duality also preserves every fusion coefficient. In the frozen binary sector
coordinates it is the single transposition \(010\leftrightarrow101\), which
does not normalize the product Pauli group and is therefore non-Clifford.

Recent primary sources supply constant-depth quantum-double anyon-permutation
circuits and an independent self-dual \(S_3\) lattice realization of this
exchange.

## Conditional hybrid closure

The affine three-bit group has order 1,344 and is two-transitive. Conjugating
\((C\;F)\) produces all 28 transpositions, hence

\[
  \langle\operatorname{AGL}(3,2),(C\;F)\rangle=S_8,
  \qquad |S_8|=40320.
\]

The checker enumerates the entire closure.

## Scope and blocker

The \(S_8\) result is conditional algebraic closure, not executable physical
control. The protected duality acts on the torus sector basis; the affine
controls act on an encoded record/control presentation. Matching eight labels
does not provide their source identity. A microscopic intertwiner, locality
contract, recovery map, and noisy implementation remain unproved.

## Durable verification

- Packets:
  `research/kitaev/s3-protected-anyon-permutation-frontier.md` and
  `research/kitaev/s3-duality-affine-hybrid-closure.md`
- Checkers:
  `research/kitaev/checkers/check_s3_protected_anyon_permutation.py` and
  `research/kitaev/checkers/check_s3_duality_affine_hybrid_closure.py`
- Results:
  `research/kitaev/results/s3-protected-anyon-permutation.json` and
  `research/kitaev/results/s3-duality-affine-hybrid-closure.json`
- Exact counts: \(2,168,1344,28,40320\)
- Graph admission: `ev-000000003360-3a86cf53-35bf-4933-b2c8-81073ff14dd5`
- Ledger allocation: `seqclaim-666339317cff8a39735e208f`
