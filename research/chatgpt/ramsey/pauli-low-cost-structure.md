# Why the two low-cost Ramsey patterns fit in eight qubits

Status: exact certificates for two graphs; a motif discriminator verified on the supplied 191-record catalogue. Not an unrestricted classification theorem or a new Ramsey bound.

## A structural discriminator: parity-closed heptagons

Call an induced seven-cycle S **parity-closed** when every vertex of the whole graph has an even number of neighbors in S. This is a graph-only test: find a chordless seven-cycle, then count its incidences with all vertices. It does not require computing a matrix rank.

| Minimum qubits | Parity-closed induced C7s per graph | Catalogue records |
|---:|---:|---:|
| 8 | 4 | 2 |
| 9 | 0 | 13 |
| 10 | 0 | 115 |
| 11 | 0 | 61 |

Both low-cost graphs have four such heptagons; no other catalogue graph has one. For each of these heptagons, fourteen outside vertices have two neighbors on the cycle and one outside vertex has none. The four cycle supports have binary span dimension three; their XOR is zero. Their pairwise intersections have sizes 1 or 3.

The heptagons alone do **not** explain all six dependencies. Their three independent relations plus the all-vertices relation account for four. Two further even-neighborhood relations complete the certificate.

## Why even-neighborhood relations save qubits

Let A be the binary anticommutation adjacency matrix and let 1_S be the incidence vector of a vertex subset. The parity condition is exactly A 1_S = 0. Graphically, each operator anticommutes with an even number of operators in S, so the ordered product over S commutes with every listed operator.

In a minimum-register realization spanning the full nondegenerate symplectic space, this product is a scalar ±I. In a nonminimal realization it need only be central relative to the chosen family; the scalar conclusion must not be assumed there.

Six independent parity relations give nullity(A) ≥ 6, hence rank(A) ≤ 22−6 = 16. A separately exhibited nonsingular 16×16 principal submatrix gives rank(A) ≥ 16. Together these certify **exactly eight qubits**, without relying on a single full-matrix rank assertion.

## Catalogue record 187

Graph6:
```text
UsaC?GAAWb@`CcIAiAiHAGoL`e?x?Ou?`cI@Wd?_
```

Independent parity relations (vertex labels are 1-based; products use increasing label order):

| Support | Graph structure | Product in the saved minimal realization |
|---|---|---|
| 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 | all vertices (even 6-regular degree) | -I |
| 1, 2, 5, 9, 10, 11, 21 | parity-closed induced C7 | -I |
| 1, 3, 4, 8, 10, 11, 22 | parity-closed induced C7 | -I |
| 2, 4, 8, 18, 19, 20, 22 | parity-closed induced C7 | +I |
| 1, 6, 7, 10, 11, 16, 17 | induced C5 plus two isolated vertices | +I |
| 1, 4, 6, 8, 13, 14, 16, 18, 21 | 9-vertex even-neighborhood support | -I |

A nonsingular principal submatrix is supported on: 1, 2, 3, 14, 4, 11, 5, 10, 6, 8, 7, 9, 12, 16, 13, 19.

## Catalogue record 188

Graph6:
```text
UsaC?GGC?DccQDCpKEJAOKW`Bo?kD_[_okHCUR??
```

Independent parity relations (vertex labels are 1-based; products use increasing label order):

| Support | Graph structure | Product in the saved minimal realization |
|---|---|---|
| 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 | all vertices (even 6-regular degree) | +I |
| 1, 3, 7, 10, 11, 12, 13 | parity-closed induced C7 | +I |
| 1, 4, 6, 9, 10, 12, 18 | parity-closed induced C7 | -I |
| 3, 7, 13, 17, 18, 19, 21 | parity-closed induced C7 | -I |
| 1, 2, 4, 9, 13, 15, 16, 17, 20 | 9-vertex even-neighborhood support | +I |
| 1, 3, 4, 8, 10, 14, 16, 19, 20 | 9-vertex even-neighborhood support | -I |

A nonsingular principal submatrix is supported on: 1, 2, 3, 12, 4, 10, 5, 9, 6, 8, 7, 11, 14, 16, 15, 17.

## What this does and does not explain

- The low cost comes from six independent global even-neighborhood relations; the certificates exhibit those relations explicitly.
- Parity-closed heptagons supply a non-rank structural signature distinguishing the two examples within this catalogue.
- Both examples have degree six, but eight other catalogue graphs are also 6-regular and require nine or ten qubits. Regularity alone is insufficient.
- The four heptagons account for only three independent relations. The additional supports are essential to the eight-qubit certificate.
- This report itself is catalogue-relative. The subsequent `heptagon-normal-form-theorem.md` gives a separate, catalogue-independent computer-assisted proof that the exact 22-vertex hypotheses force rank 16. It includes independently checked UNSAT proofs and completion certificates; it is not a short human-only derivation.
- Follow-up: `heptagon-forcing-investigation.md` gives a 21-vertex, 6-regular counterexample to the unrestricted-size implication (nine qubits) and a graph-only boundary lemma. The exact 22-vertex claim is subsequently settled by the normal-form computation.
- No identification with ESD7, physical braid carriers, or an unrestricted qudit-dimension minimum follows.

## Verification

The heptagons are found by a direct induced-cycle search and independently matched against weight-seven kernel vectors. Certificate verification checks every neighborhood parity, independence of all six supports, the 16×16 minor, and each stated Pauli product.

```sh
python research/chatgpt/ramsey/pauli_low_cost_structure.py
python -m unittest discover -s tests -p "test_pauli_low_cost_structure.py"
```

Full per-graph features and certificates: `pauli-low-cost-structure.json`. Input catalogue and its SHA-256 are pinned by `pauli_realization_audit.py`.
