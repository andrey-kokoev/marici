# D(S3) Wilson quarter gates: phase-polynomial resource reduction

Owner: `marici.Kitaev`

## Bounded question

Do the two previously separated Wilson magic species require genuinely new
ideal gate resources, or can their logical and controlled quarter evolutions
be synthesized from verified \(T/T^\dagger\) injections and Clifford parity
networks?

## Frozen model

For \(n\) binary label bits, an ancilla-free diagonal CNOT+\(T\) circuit has
phase function

\[
 f(x)=\sum_{m\ne0}a_m\,(m\cdot x\bmod2)\pmod8,
 \qquad a_m\in\mathbf Z/8.
\]

Odd coefficients consume \(T/T^\dagger\)-type injections; even coefficients
are diagonal Clifford phases. The checker solves the exact congruences and
minimizes the number of odd coefficients. It audits three-bit logical Wilson
quarter gates and their four-bit controlled versions separately.

## Claim boundary

The exact test gives a split verdict.

- The \(\{D,E\}\) logical species is realizable with minimum \(T\)-count four.
- The \(\{C,F,G,H\}\) logical species is not an ancilla-free CNOT+\(T\)
  phase polynomial.
- None of the six exact controlled quarter evolutions is such a phase
  polynomial.

The obstruction is structural. Expanding a parity phase into Boolean
multilinear monomials forces every degree-\(d\) coefficient to be divisible
by \(2^{d-1}\). Modulo eight, cubic coefficients must be divisible by four
and quartic coefficients must vanish. The failed species exhibit explicit
violations in the result packet.

Thus verified \(T\) states alone close only the ideal logical \(D/E\) species,
not the coherent controlled-Wilson interface. The result does not exclude
ancilla-assisted or measurement-assisted Clifford+\(T\) synthesis, nor does
it establish a source-derived \(T\)-state factory, fault-tolerant extended
rectangles, or physical error rates.

## Falsifiers

- Any target phase function outside the parity-polynomial image modulo eight.
- A nonzero exact reconstruction residual.
- A lower odd-coefficient solution than the optimizer's certified minimum.
- A required physical operation that cannot be represented by the frozen
  binary sector-label phase function.

## Artifacts

- Checker: `checkers/check_s3_wilson_phase_polynomial_resources.py`
- Result: `results/s3-wilson-phase-polynomial-resources.json`
- Result SHA256:
  `F96F5A8F1DE372D4A0A1898A317C35E96F282B08A4C6965B772B133473FD1304`
- Graph admission: `ev-000000003433-fc2db9ea-575e-4c3a-accb-22c59222232a`
- Canonical-witness hash correction:
  `ev-000000003435-bccc9cbd-1273-4302-98c7-2edbbfada83e`
- Ledger: entry 2494, `seqclaim-f0fae9871fcc092d47c9a2e2`
