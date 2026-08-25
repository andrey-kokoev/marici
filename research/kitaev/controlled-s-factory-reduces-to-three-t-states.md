# The controlled-S factory reduces to three verified T states

Owner: `marici.Kitaev`

## Exact synthesis

For binary variables (x,y),

\[
  2xy=x+y-(x\oplus y)\pmod8.
\]

Therefore controlled-(S) has the exact circuit

\[
T_x\,T_y\,\mathrm{CNOT}_{x\to y}\,T_y^\dagger\,
\mathrm{CNOT}_{x\to y}.
\]

It uses three (T/T^\dagger) injections, two Clifford CNOTs, and no workspace
ancilla. Applied to (|++\rangle), it prepares the shared
(|CS\rangle) injection state.

## Bounded optimality

The checker exhausts all (8^3) coefficient assignments on the three
nonzero binary linear forms (x,y,x\oplus y). A coefficient is non-Clifford
exactly when it is odd. The minimum number of odd coefficients is three, with
solutions

\[
  (1,1,7),\qquad(5,5,3).
\]

Thus three is optimal for ancilla-free diagonal CNOT+(T) phase-polynomial
synthesis. This is not a lower bound against arbitrary measurement-assisted
Clifford+(T) protocols.

## Factory consequence

If a verified encoded (T)-state factory exists, (|CS\rangle) is not an
independent magic species: its factory consumes three verified (T) or
conjugate-(T) states and a Clifford parity network. The mod-four kernel and
the (D(S_3)) power-two record phase can then share this derived resource.

The frozen source currently supplies no verified (T)-state factory. The
reduction therefore moves the production blocker upstream; it does not close
physical executability. A fault-tolerant implementation must schedule three
injection extended rectangles and two logical CNOTs and propagate their
accepted-error contracts.

## Falsifiers

- Failure of the exact circuit matrix or prepared resource state.
- An ancilla-free diagonal phase polynomial with fewer than three odd
  coefficients.
- An already admitted verified (T)-state factory in the frozen source.

## Artifacts

- Checker: `checkers/check_controlled_s_from_t_factory.py`
- Result: `results/controlled-s-from-t-factory.json`
- Result SHA256:
  `4B51B4A86E372EEABFF06D58E5C9AEAD1A778B191D8CC40676FB9AAAE909DAB8`
- Epistemic-graph admission:
  `ev-000000003423-790accb5-35be-4bfe-8895-58fffb484248`
- Ledger: entry 2490,
  `seqclaim-bf4bb1633d4cc35eb1b4f812`
