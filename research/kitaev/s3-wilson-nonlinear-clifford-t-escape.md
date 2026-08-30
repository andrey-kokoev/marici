# Nonlinear Clifford+T escapes the Wilson parity-phase obstruction

Owner: `marici.Kitaev`

## Bounded question

Does ledger entry 2494 obstruct all exact Clifford+\(T\) synthesis, or only
ancilla-free diagonal parity networks?

## Construction

Write each exact mod-eight phase function in its Boolean multilinear basis.
For every nonzero degree-\(d\) monomial:

1. compute its conjunction into a clean work bit using a \(d-1\) Toffoli
   ladder;
2. apply \(T^c\) for its coefficient \(c\in\mathbf Z/8\);
3. uncompute the ladder.

Work bits are reusable between monomials. The checker independently verifies
the standard exact seven-\(T\) Toffoli matrix and reports conservative finite
resource upper bounds for every logical and controlled Wilson quarter gate.

## Disposition

The parity-polynomial obstruction is architectural, not a general algebraic
Clifford+\(T\) obstruction. All twelve targets have exact nonlinear
clean-ancilla constructions. No resource optimum, source-derived magic-state
factory, accepted-error contract, or fault-tolerant extended rectangle is
claimed.

## Falsifiers

- Nonzero matrix residual for the seven-\(T\) Toffoli decomposition.
- Failure of Boolean Möbius reconstruction of a target phase.
- A target requiring more work bits than the declared conjunction ladder.
- A proof that clean ancillas or nonlinear reversible computation are absent
  from the intended executable architecture.

## Artifacts

- Checker: `checkers/check_s3_wilson_nonlinear_clifford_t_escape.py`
- Result: `results/s3-wilson-nonlinear-clifford-t-escape.json`
- Result SHA256:
  `E16467F51E7E6D6A25992EE9FBF0ECF10A6A9F822AE75752049FCB1E441F1935`
- Graph admission: `ev-000000003438-4e662d8d-2981-49f4-8714-41c6847ea28e`
- Ledger: entry 2496, `seqclaim-7fbb14d545f91dbdd94e404b`
