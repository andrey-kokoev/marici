# CDFG is robust over the nonnegative primitive-cost cone

Owner: `marici.Kitaev`

## Bounded question

Was ledger entry 2504's CDFG selection an artifact of assigning costs
\(CS=3\), \(CCZ=7\), and a Toffoli compute--uncompute pair \(=14\)?

## Symbolic resource vectors

Count each complete two-power faithful family in coordinates

\[
(n_{CS},n_{CCZ},n_{\mathrm{pair}},U).
\]

The selected family has

\[
CDFG=(13,14,16,16).
\]

Every rival differs from this vector by a componentwise nonnegative vector.
The nearest rival is

\[
CEFG-CDFG=(0,1,0,0).
\]

Therefore CDFG weakly minimizes every nonnegative linear cost functional on
these four primitives. It is uniquely minimizing exactly when the CCZ weight
is positive and at least one of the CS, Toffoli-pair, or work-episode weights
is positive.

## Boundary

This robustness is relative to the selected primitive library. A compiler
that shares gates across ports, uses measurement-assisted identities, or
introduces a different primitive can alter the vectors. Physical correlated
failure costs are not linearized here.

## Falsifiers

- A rival family with a negative coordinate difference from CDFG.
- A nonnegative weight vector for which CDFG is not a minimizer.
- Failure of the stated uniqueness condition on a cone face.
- A source-admissible compiler with different primitive vectors.

## Artifacts

- Checker: `checkers/check_s3_faithful_family_cost_cone.py`
- Result: `results/s3-faithful-family-cost-cone.json`
- Result SHA256:
  `30CE03225D6916755A6757B81D8B1630E729155BBD60E3247C0FD712FF582651`
- Graph admission: `ev-000000003459-7eaabc3a-4fd7-401f-9c5e-399b08b806f2`
- Ledger: entry 2506, `seqclaim-cc4ac0e6a605d7c4f756bd60`
