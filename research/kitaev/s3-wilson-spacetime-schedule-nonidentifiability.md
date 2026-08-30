# Wilson fault-tolerant spacetime scheduling is not yet identifiable

Owner: `marici.Kitaev`

## Bounded question

Do the exact algebraic resource bounds through ledger entry 2499 determine a
preferred fault-tolerant schedule?

## Exact negative answer

No. The frozen capability contract types physical depth and magic-ancilla
count as `undefined`, not unknown numerical values. Its future magic envelope
is proposed, and its verified magic source is not admitted.

For the worst controlled target \(H\), the phase-native compiler supplies an
algebraic upper bound of 85 \(T\) states. Serial term execution reuses at most
two clean work blocks. Full term parallelism uses five and has an idealized
module-depth bound of 31.

Two completions of the absent factory data reverse the preference:

- a single-lane factory cannot improve the 85-round injection lower bound by
  parallelizing terms, so serial reuse dominates on footprint;
- an unconstrained parallel factory reduces the abstract term schedule from
  85 to 31 rounds, so parallel execution wins on depth.

Both are compatible with every currently frozen theorem. Therefore no unique
fault-tolerant schedule follows from the algebraic compiler.

## Reopening data

A genuine optimization requires an admitted factory, acceptance and output
error contracts, throughput and latency, encoded primitive exRecs, verified
work-block lifecycle costs, layout concurrency, and an ordering or weighting
of depth, footprint, and failure probability.

## Falsifiers

- Existing admitted source data supplying every reopening field.
- A schedule theorem invariant under all compatible factory completions.
- Failure of either compatible completion or of the preference reversal.

## Artifacts

- Checker: `checkers/check_s3_wilson_spacetime_nonidentifiability.py`
- Result: `results/s3-wilson-spacetime-nonidentifiability.json`
- Result SHA256:
  `B4F6874883884EA890B8B6ECC7B3FAF418956CA226DC2AF167658A0DFD1D48C4`
- Graph admission: `ev-000000003446-99c06bda-adb5-4e55-bbe2-9d81113a9f4d`
- Ledger: entry 2501, `seqclaim-b3eaaac3af19684ab43631aa`
