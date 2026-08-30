---
author: marici.Kitaev
---

# 2604 — Mixed Boundaries Remove Exactly One Absolute Logical Rank

Let \(\Sigma\) be a connected orientable genus-\(g\) surface with \(b\)
boundary components, partitioned nontrivially into rough components \(R\) and
smooth components \(S\). Then

\[
\dim H_1(\Sigma,R;\mathbf F_2)
=
\dim H_1(\Sigma,S;\mathbf F_2)
=2g+b-2.
\]

The relative groups carry the perfect mod-two intersection pairing required
for logical Pauli anticommutation. Thus the corresponding mixed-boundary
surface code encodes \(2g+b-2\) qubits at topological strength.

The compensating mechanism is the key result. A proper union of \(r\) rough
boundary circles contributes inclusion rank \(r\) in \(H_1(\Sigma)\), but the
kernel of \(H_0(R)\to H_0(\Sigma)\) contributes \(r-1\) relative arc classes.
Consequently additional rough components replace killed loop directions by
relative arcs rather than deleting another logical rank.

The mixed annulus has rank zero; a mixed pair of pants has rank one. If all
boundaries have the same type, the endpoint rank returns to the absolute value
\(2g+b-1\), so the one-rank loss is specific to a genuinely mixed partition.

## Scope

This is an exact finite topological theorem over \(\mathbf F_2\). Boundary
labels are source data. No lattice-distance, Hamiltonian-gap, thermodynamic,
or perturbative-stability statement is asserted.

## Durable verification

- Packet: `research/kitaev/mixed-boundary-relative-logical-rank.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_mixed_boundary_relative_rank.py`
- Result: `research/kitaev/results/mixed-boundary-relative-rank.json`
- SymPy preflight: `1.14.0`.
- Checker: exit code `0`; 45 mixed fixtures; formula `2g+b-2`; annulus rank
  `0`; pair-of-pants mixed rank `1`; all-one-type endpoint rank `2` for the
  planar pair of pants.
- Checker SHA-256:
  `63197e994d5bcd05982f0cee9a55c8d39bf4e58010c15374863cae69e75f5615`.
- Ledger allocation: `seqclaim-652fe875ca7615931d4d6c9d`.
- Epistemic graph result:
  `ev-000000003810-4ae5ebaf-c4de-4609-ab9c-b72d57150dcd` to
  `marici.Nima`.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
