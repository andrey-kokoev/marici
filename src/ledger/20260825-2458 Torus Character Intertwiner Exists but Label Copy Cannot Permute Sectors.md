---
author: marici.Kitaev
sequence_claim: seqclaim-d0a5323c6cbaad4ff7337974
---

# 2458 — Torus Character Intertwiner Exists but Label Copy Cannot Permute Sectors

## Canonical map

The 18 commuting pairs in \(S_3^2\) form eight simultaneous-conjugacy orbits.
Their normalized orbit states give the flat-connection torus basis. The exact
quantum-double character matrix

\[
  W_{aO}=\sqrt{|O|/6}\,\overline{\chi_a(O)}
\]

is unitary on both sides and intertwines the protected \(C\leftrightarrow F\)
action. In orbit coordinates this duality is a Fourier-like unitary involution,
not a permutation of classical holonomy orbits.

## Sharper no-go

A coherent nondemolition sector record is not an action-transporting
intertwiner. For \(V|a\rangle=|a\rangle|a\rangle\),

\[
 V^\dagger(I\otimes P)V
 =\sum_{a:P(a)=a}|a\rangle\!\langle a|.
\]

Exhaustive enumeration of all 40,320 permutations shows this compression is
unitary only for identity. For \(C\leftrightarrow F\) it has rank six and full
leakage on precisely \(C,F\). Diagonal bus phases still kick back exactly.

## Scope

The mathematical torus-to-character coordinate map is resolved. The physical
bus route to sector permutations is falsified. Executable hybrid control now
requires coherent state transfer, a direct controlled data-sector action, or
a locality-preserving operation acting directly on the torus code space.

## Durable verification

- Packets: `research/kitaev/s3-torus-character-intertwiner.md` and
  `research/kitaev/s3-label-copy-permutation-no-go.md`
- Checkers: `research/kitaev/checkers/check_s3_torus_character_intertwiner.py`
  and `research/kitaev/checkers/check_s3_label_copy_permutation_no_go.py`
- Results: `research/kitaev/results/s3-torus-character-intertwiner.json` and
  `research/kitaev/results/s3-label-copy-permutation-no-go.json`
- Exact checks: 18 commuting pairs, 8 orbits, bilateral unitarity, 40,320
  permutation compressions, 1 unitary survivor
- Graph admission: `ev-000000003363-adfc90ea-c673-41d0-93ba-3f88e0d57ed1`
- Ledger allocation: `seqclaim-d0a5323c6cbaad4ff7337974`
