# One controlled-S magic state serves both mod-four consumers

Owner: `marici.Kitaev`

Ledger: Entry 2488  
Graph: `ev-000000003418-b8474716-d8a2-4d08-aaea-a5a2163e2d59`

## Bounded question

Once a controlled-(S)-type resource is admitted, is its online consumption
gadget executable with the frozen Clifford architecture, and can one factory
serve both known consumers?

## Exact injection result

Let

\[
  CS=\operatorname{diag}(1,1,1,i),
  \qquad
  |CS\rangle=CS|++\rangle
  ={1\over2}(|00\rangle+|01\rangle+|10\rangle+i|11\rangle).
\]

The resource state is nonstabilizer: among all sixteen two-qubit Pauli
expectations, only the identity has unit magnitude. The checker exhausts all
sixteen Bell outcomes of gate teleportation. Every correction

\[
  CS\,P\,CS^\dagger
\]

is Clifford. Four corrections are Pauli and twelve are non-Pauli Clifford;
none requires a further magic operation.

Thus one verified encoded (|CS\rangle) state deterministically supplies one
controlled-(S) invocation using logical Bell measurements and Clifford
feed-forward.

## Shared factory contract

The same resource species serves:

1. the binary mod-four product-residue interaction;
2. the previously identified (D(S_3)) controlled-power-two record phase.

Each invocation consumes one verified resource state. The online compiler
adds no new magic species and no recursive non-Clifford correction branch.

This closes consumption, not production. The frozen source still lacks a
verified encoded preparation or distillation factory for (|CS\rangle), its
noise threshold, acceptance rule, and one-fault-tolerant extended rectangle.
Declaring the state available would remain an added coefficient/source lens.

## Falsifiers

- A Bell branch whose correction is non-Clifford.
- A stabilizer certificate for (|CS\rangle).
- Failure of the encoded Bell or Clifford-correction contracts in the frozen
  five-rail architecture.

## Artifacts

- Checker: `checkers/check_controlled_s_magic_injection.py`
- Result: `results/controlled-s-magic-injection.json`
