# Wilson-interface magic is activated by coherent control

Owner: `marici.Kitaev`

## Bounded question

Could the Wilson pointer use only a task-specific subset of native ququart
states that crosses the digit interface freely, despite the obstruction for
the full stabilizer theory?

## Exact separation

For each (k\in\mathbb Z_4), the fixed character state

\[
|\chi_k\rangle=\frac12\sum_{r=0}^3 i^{kr}|r\rangle
\]

has exactly four unit-magnitude two-qubit Pauli expectations after the digit
identification (r=2a+d). Every resolved pointer branch is therefore a
binary stabilizer state.

That branchwise fact is insufficient. Apply the odd native Wilson primitive

\[
\sum_{b=0}^1 |b\rangle\!\langle b|\otimes Z_4^b
\]

to the native stabilizer product ( |+\rangle_b|+_4\rangle_r). Under digit
exposure the operation is (CZ(b,a)CS(b,d)). The exact output has only two
unit-magnitude three-qubit Pauli expectations; a pure three-qubit stabilizer
state requires eight. Thus the coherent trajectory, not any fixed classical
branch, activates the nonstabilizer resource.

## Consequence and typing boundary

A partial interface covering faithful coherent Wilson extraction cannot be
certified free merely because its resolved pointer states are binary
stabilizers. Odd controlled-(Z_4) is already a task-local magic witness.
This proves a qualitative resource lower bound, not a numerical code-switch
cost or a fault-tolerant interface.

## Falsifiers

- Any fixed (F_4) character branch has other than four unit Pauli
  expectations.
- The coherent output has eight unit Pauli expectations.
- The odd primitive is absent because every Wilson predicate is measured or
  dephased before interaction; that would change the coherent-readout task.
- An admitted fault-tolerant interface implements the primitive freely while
  preserving the declared binary stabilizer resource theory.

## Artifacts

- Checker: `checkers/check_ququart_wilson_coherence_magic.py`
- Result: `results/ququart-wilson-coherence-magic.json`
- Result SHA256:
  `0A85E7D28474151369F3FF436A285558000A666908D595296718B555B75911B8`
- Graph admission: `ev-000000003481-69561b26-82e7-4f9a-a9a7-2e00344f297c`
- Ledger: entry 2514, `seqclaim-ac071a8741654a3ec2b337e5`
