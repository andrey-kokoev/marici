# Phase-native compression of exact D(S3) Wilson circuits

Owner: `marici.Kitaev`

## Bounded question

How much of ledger entry 2496's conservative Clifford+\(T\) cost is an
artifact of compiling every nonlinear phase through two full Toffoli ladders?

## Frozen phase library

- \(CS\) and \(CS^\dagger\): three \(T/T^\dagger\) injections.
- \(CCZ\): seven \(T/T^\dagger\) injections.
- A compute--uncompute Toffoli pair: fourteen injections.
- Clifford single-qubit phases and \(CZ\): zero \(T\) cost.

A degree-\(d\) controlled-\(S\) phase uses a conjunction ladder on the first
\(d-1\) variables, a phase-native \(CS\), and uncomputation. A higher
controlled-\(Z\) phase analogously terminates in \(CCZ\). Reusable work bits
are charged explicitly.

## Claim boundary

The checker selects the cheaper of this nonlinear compiler and the exact
parity compiler where the latter exists. It reports deterministic exact upper
bounds. It does not prove global circuit optimality, physical error rates, or
fault-tolerant executability.

## Falsifiers

- Failure of the previously checked three-\(T\) \(CS\) or seven-\(T\) Toffoli
  identities.
- A monomial not reproduced by the stated compute--phase--uncompute gadget.
- A reported bound exceeding its entry-2496 baseline.
- Hidden simultaneous use of work bits declared reusable.

## Artifacts

- Checker: `checkers/check_s3_wilson_phase_native_compression.py`
- Result: `results/s3-wilson-phase-native-compression.json`
- Result SHA256:
  `6EAFDFD4B38DE1481DABB019634C6D4B056D476B87216112CA83BBD8F88F57F7`
- Graph admission: `ev-000000003441-253f85cc-3a05-460f-9e69-f6870405fd63`
- Ledger: entry 2499, `seqclaim-e8f146cb1b199c70df550a16`
