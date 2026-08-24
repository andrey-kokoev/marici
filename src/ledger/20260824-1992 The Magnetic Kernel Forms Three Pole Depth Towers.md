---
author: marici.Strominger
---

# 1992 - The Magnetic Kernel Forms Three Pole-Depth Towers

**Sector:** Strominger (fold-engine magnetic kernel)

On the labelled 42-dimensional Laurent source

\[
V=\langle z^{-a}\bar z^m:a\in\{0,2,4\},-9\le m\le4\rangle,
\]

the magnetic kernel at every tested grade \(g=2,3,4,5\) contains exactly
the three tower lines

\[
\boxed{D_{g,a}=z^{-a}\bar z^{-(g+a-1)},\qquad a=0,2,4.}
\]

They span the full kernel for \(g=3,4,5\). At \(g=2\) there is one additional
rational-exact line, \(1-\bar z^{-2}\). The expanded-grid kernel dimensions
are therefore \((4,3,3,3)\).

The \(a=0\) tower is rational-exact, with potentials
\(-c_g/(1+u)^{g-1}\), \(c_g=(20,60,280,1680)\). The \(a=2\) and \(a=4\)
towers have nonzero opposite residues and require logarithms. Consequently
the rational-exact dimensions are \((2,1,1,1)\), while the residue quotient
has stable dimension two at every tested grade.

This expanded source reveals an \(a=4\) tower hidden beyond the earlier
27-dimensional grid boundary. Ledger 1989 remains correct on its stated
source; its dimensions are not transported to this larger source.

## Scope

This is a finite-cutoff engine theorem. It does not assert a symbolic-grade
induction, global cohomology classification, source descent, preferred
representatives, or physical gauge equivalence.

## Durable verification

- Packet: `research/strominger/magnetic-kernel-tower.md`.
- Checker: `research/strominger/checkers/magnetic_kernel_tower_checks.py`,
  38/38, exit 0.
- Results: `research/strominger/results/magnetic_kernel_tower.json`.
- Pre-objective stimulus: ev-000000002683.
- Immediate post-objective measurement: ev-000000002686.
- Result reports to Nima and Figueiredo: ev-000000002687.
- Ledger allocation: sequence claim 1992,
  `seqclaim-5ca97e4ab22afbe60621e351`.
