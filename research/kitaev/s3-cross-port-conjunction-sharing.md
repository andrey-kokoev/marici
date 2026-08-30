# Cross-port conjunction sharing preserves CDFG selection

Owner: `marici.Kitaev`

## Bounded question

Can the repeated sector-label conjunctions used by distinct Wilson ports and
controlled powers be computed once and shared, and does this structural
compiler change overturn CDFG?

## Ideal algebraic result

All eight faithful families use the same four data-conjunction episodes: the
three pair predicates \(011,101,110\), plus one triple extension for \(111\).
The triple extension reuses \(011\) as its first ladder level. Computing each
predicate once, applying every associated
pointer-controlled phase, and uncomputing changes CDFG's primitive vector from

\[
(13,14,16,16)
\quad\hbox{to}\quad
(13,14,4,4).
\]

With the exact \(3/7/14\) component costs, its upper bound falls from 361 to
193 \(T\) states. Every family has the same two shared-conjunction coordinates,
while CDFG remains componentwise minimal in CS and CCZ counts. Hence the
family selection survives this structural attack.

## Fault boundary

The ideal shared predicate stays live across several pointer contacts. A
persistent predicate fault may therefore reach several pointer blocks, or the
same pointer block more than once across powers. No one-fault-safe contact
order, hygiene schedule, or exRec is yet proved. Four is an ideal algebraic
work-episode count, not an admitted fault-tolerant resource count.

## Falsifiers

- A faithful family needing a different data-conjunction set.
- Failure of the grouped phase product to equal the ungrouped commuting
  product.
- A rival with a negative shared primitive-coordinate difference from CDFG.
- A fault-safe sharing theorem with a different charged episode count.

## Artifacts

- Checker: `checkers/check_s3_cross_port_conjunction_sharing.py`
- Result: `results/s3-cross-port-conjunction-sharing.json`
- Result SHA256:
  `446F4A425C1F2A15E13389CE273EEDF2E371E9565EE675E95FCCC0B396131DB7`
- Graph admission: `ev-000000003461-c57a15fe-bc9f-4244-99d9-7b8ebd59071f`
- Ledger: entry 2507, `seqclaim-0b4d1836aafb5d26ec170fa0`
