# A native ququart stabilizer becomes binary magic under digit exposure

Owner: `marici.Kitaev`

## Bounded question

Is the ququart-to-binary digit interface merely a bookkeeping change, or does
it carry an operational magic resource?

## Exact witness

The normalized state

\[
|\psi\rangle=
\frac12\left(-1,\frac{1+i}{\sqrt2},1,
\frac{1+i}{\sqrt2}\right)^T
\]

is an exact eigenstate of the native ququart Pauli \(X_4Z_4\), with
eigenvalue \((-1+i)/\sqrt2\). Under the computational digit identification
\(r=2a+d\), treat the same amplitudes as a two-qubit state.

The checker evaluates all sixteen two-qubit Paulis exactly. Only two have
expectation value of unit magnitude. A pure two-qubit stabilizer state has a
four-element stabilizer and therefore four unit-magnitude Pauli expectations.
Thus the digit image is a binary nonstabilizer state.

## Consequence and boundary

The digit interface cannot freely transport the full native stabilizer theory
to the binary stabilizer theory. This state witness complements the earlier
Pauli-group element-order obstruction.

It does not exclude a restricted, task-specific interface defined only on the
states and operations traversed by the Wilson pointer compiler. Such a partial
interface needs its own domain, coherence, and fault contract.

## Falsifiers

- Nonzero native Pauli eigenstate residual.
- Four unit-magnitude binary Pauli expectations for the displayed state.
- A full reversible free interface preserving both stabilizer theories.
- A task-specific partial interface covering the Wilson trajectory.

## Artifacts

- Checker: `checkers/check_ququart_digit_interface_magic_witness.py`
- Result: `results/ququart-digit-interface-magic-witness.json`
- Result SHA256:
  `B1491AF6BCC0C6A324D6521520B008168A367E80F913B849FAEBCFA925003FE4`
- Graph admission: `ev-000000003481-69561b26-82e7-4f9a-a9a7-2e00344f297c`
- Ledger: entry 2514, `seqclaim-ac071a8741654a3ec2b337e5`
