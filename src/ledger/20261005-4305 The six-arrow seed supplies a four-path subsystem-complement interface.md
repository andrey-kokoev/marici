# 4305 — The six-arrow seed supplies a four-path subsystem–complement interface

## Source boundary

The existing directed seed consists of the two cycles ABC and ADB, retaining six primitive occurrences:

\[
AB,\ BC,\ CA,\ BA,\ AD,\ DB.
\]

Choose the marked subsystem A and complement {B,C,D}. The crossing ports are AB and AD outward, BA and CA inward. The complement's internal arrows form D -> B -> C. This is an explicit subsystem choice, not a derivation of a uniquely preferred physical split.

## Exhaustive first-return packet

Exactly four paths leave A and return without visiting A in between:

| Outward port | Inward port | Retained path | Traversals |
|---|---|---|---:|
| AB | BA | ABA | 2 |
| AB | CA | ABCA | 3 |
| AD | BA | ADBA | 3 |
| AD | CA | ADBCA | 4 |

The complement incidence matrix is nilpotent of index three. This proves that the first-return list is exhaustive, rather than the result of an arbitrary path cutoff. Repeated excursions through A are not included in this finite inventory.

With rows (BA,CA), columns (AB,AD), and z a formal traversal-count grade, the port readout is

\[
K(z)=\begin{pmatrix}z^2&z^3\\z^3&z^4\end{pmatrix}.
\]

Each entry retains its actual directed path in the result packet. Summing entries gives z^2+2z^3+z^4, but the aggregate is not substituted for the port-level data.

## Why this boundary matters

The older Machian eigenline-response model uses all twelve directed dependencies between four anchors. Six are not primitive occurrences in this seed. That richer support needs an explicit generation or coupling argument; it cannot be imported as though it were the original interface.

The present packet supplies a concrete source on which a proposed outward comparison and complementary response can act, without inserting the old gravitational coefficients 1/90 or -1/5280.

**Scope.** This is an exact directed-path and incidence result. A returning path is not automatically an identity witness or a null-homotopy; AB followed by BA retains two traversals. No physical time, probability, energy, response law, value of G, or identification of the complement with the physical universe has been derived. Additional arrows are not forbidden, but their provenance must be supplied.

## Durable verification

- Source: `research/nima/checkers/check_natural_tower_return.py:PACKETS`.
- Packet: `research/nima/seed-subsystem-complement.md`.
- Checker: `research/nima/checkers/check_seed_subsystem_complement.py`.
- Results: `research/nima/results/seed-subsystem-complement.json`, including source digest, typed ports, complete path records and exact nilpotence checks.

Fresh checker execution passed with exit code zero: `structured_command_execution:e_32876_1791230099029041900_57`.

Epistemic graph admission: proposal `ep_7d1e4fef-adba-44ce-8dbc-24a010a62ecc`, event `ev-000000015791-63d5a89d-65be-4ad8-bf30-af3472099cbb`, sequence 15791. Admission records provenance, not mathematical truth. This event remains uncommitted.

Site validation: `pnpm run build` passed with exit code zero via `structured_command_execution:e_32876_1791230182792390100_58` (VitePress and Pagefind).

Sequence allocation: `seqclaim-a249b36419c30a13c53241b9`, value 4305. No commit or push is claimed.
