# Five-rail code freeze and transversal obstruction

Owner: `marici.Kitaev`

Status: exact explicit code and recovery tables; railwise multiplication and
Fourier assumptions falsified.

## Explicit component codes

Every six-state rail is frozen as a qubit tensor a qutrit.  The qubit factor
uses the cyclic five-qubit perfect code with generators

```text
X Z Z X I
I X Z Z X
X I X Z Z
Z X I X Z
```

The qutrit factor uses four frozen generalized-Pauli rows, written as
`(X exponents | Z exponents)` over `F3`:

```text
2 1 0 1 0 | 1 2 1 2 2
0 1 0 1 1 | 1 1 2 0 0
1 1 1 0 2 | 2 0 0 1 0
2 1 0 0 0 | 1 1 0 1 1
```

Exhaustive symplectic enumeration proves parameters `[[5,1,3]]_2` and
`[[5,1,3]]_3`.  The checker derives logical Pauli pairs rather than inserting
them, verifies centralizer sizes `2^6` and `3^6`, and emits the complete
single-rail syndrome/recovery tables: 15 distinct qubit syndromes and 40
distinct qutrit syndromes.

Thus a six-state bus is the componentwise tensor code on five physical
six-state rails.  The eight-state label bus is three componentwise five-qubit
codes on five physical eight-state rails.  Their logical dimensions are six
and eight and their distances are exactly three.

## Transversal tests

The candidate railwise SUM acts symplectically on two blocks.  For both
component codes, all eight product-stabilizer generator images lie outside
the product stabilizer span.  Hence neither transversal qubit SUM nor
transversal qutrit SUM preserves the two-block code space.

This falsifies railwise `S3` multiplication because its parity update requires
logical qubit SUM and its rotation update requires logical qutrit SUM.

The same normalizer test gives:

- transversal qubit `H`: zero of four stabilizer images remain inside;
- transversal qutrit `F3`: zero of four remain inside;
- componentwise inversion: four of four remain inside for each code.

The earlier phrase “fault-transversal logical multiplication and Fourier” was
therefore a genuine conditional interface, not an executable property of the
five-rail codes now frozen.  The next admissible resources are verified
encoded teleportation, code switching, or another explicit error-corrected
nontransversal gadget.

## Verification and falsifiers

Run:

```text
python research/kitaev/checkers/check_s3_five_rail_code_freeze.py
python research/kitaev/checkers/check_s3_five_rail_transversal_gate_obstructions.py
```

Saved outputs:

- `research/kitaev/results/s3-five-rail-code-freeze.json`
- `research/kitaev/results/s3-five-rail-transversal-gate-obstructions.json`

Falsifiers are a failed isotropy/rank/distance check, colliding single-rail
syndromes, an incorrect logical symplectic pair, or any claimed transversal
gate whose stabilizer images do not remain in the relevant stabilizer span.
The present obstruction does not rule out nontransversal fault-tolerant
gadgets.
