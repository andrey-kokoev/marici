# A prior quantum code protects the history under an explicit physical-noise model

## Reused construction

Kitaev's `research/kitaev/s3-five-rail-code-and-transversal-obstruction.md`
already freezes exact five-qubit and five-qutrit component codes, derives their
logical operators, and provides complete single-rail recovery tables.
`research/kitaev/s3-five-rail-shor-recovery.md` supplies an explicit bounded
syndrome/recovery schedule. We reuse these, rather than proposing a new code.

The stored bond history has 22 labels: ready plus 21 seam indices. Embed them
as the first 22 computational labels of five logical qubits. Encode each logical
qubit with the existing [[5,1,3]] qubit code. This uses 25 physical data qubits,
with ten unused logical labels. It is a storage-code construction, not a claim
that the original source history already consists of those physical qubits.

## Exact adapter and recovery tests

The checker imports the owning frozen code and reruns its qubit certificate.
It constructs the logical zero by the joint stabilizer/logical-Z projector and
logical one by the derived logical-X operator. Their Gram matrix is a positive
scalar times identity. Normalization gives an explicit isometry; tensoring five
copies gives the history encoding without enumerating 2^25 amplitudes.

It verifies all 484 history basis Gram entries. All 1024 component error/logical
matrix elements satisfy the exact nondegenerate correction identities for
identity and the fifteen single-qubit Paulis. Five components give 75 distinct
nonzero global syndromes, plus the no-error case. Cross-component error overlaps
factor through the verified vanishing component overlaps.

Consequently the declared noise class is correctable:

    identity and the linear span of X,Y,Z on any one
    of the 25 physical data qubits per fault-free recovery interval.

This includes arbitrary single-qubit error channels and coherent combinations
in that error span, not only a known Pauli flip. Recovery preserves every logical
history amplitude and transfers the error label into a retained syndrome record.
Reset or disposal of that record is not declared free.

The bond/battery hold Hamiltonian acts as identity on the degenerate history.
Transport through this isometry therefore changes no stored bond/battery energy.
It does not supply an energy law for the encoder, correction apparatus or ancillas.

## Recovery implementation already available, with its original boundary

The prior generalized-Shor schedule repeats the syndrome three times with
verified fresh cats. Applying its qubit component schedule to five blocks uses:

- 240 cat/data contacts;
- 180 cat verification checks;
- 240 fresh cat qubits prepared across the recovery.

These are consumed preparation counts, not peak ancilla width. Its separated
1-EC guarantee remains: fault-free recovery corrects one input error; with clean
input, one recovery fault leaves at most one correctable error. A simultaneous
input error and recovery fault is not covered by that statement.

The owning Shor recovery checker was freshly executed successfully. No new
fault-tolerant modular-history gate compiler is inferred: the prior work also
explicitly refutes naive transversal multiplication/Fourier assumptions.

## Two controls prevent overclaiming

### The old history-phase fault is not automatically repaired

The earlier failure was a phase flip on a logical history label. Its transported
operator maps the encoded code space to itself. Every stabilizer still has
outcome +1, so it has zero syndrome and remains uncorrected. The earlier fidelity
loss survives any isometric encoding of that same logical operation.

Calling it a single physical-qubit fault would change the noise model. The new
code protects physical faults only after an actual physical-noise coupling has
been identified. It does not establish that the source's logical phase error
has become such a fault.

An optional stabilizer penalty eta*sum_a(I-S_a)/2 would give single physical
Paulis a positive cost at least eta. The coefficient eta would be additional
input, and logical history phase operations would still have zero cost. No new
penalty is silently appended to the stored-energy law here.

### Two errors can alias a one-error syndrome

The checker applies Z faults to two different physical qubits of one component.
Their syndrome matches a single-error entry; that correction leaves a nontrivial
logical operation. Thus the one-error result is not a threshold or an arbitrary
noise guarantee.

## Verification and remaining physical gate

    python research/voevodsky/checkers/check_encoded_history_memory.py
    python research/kitaev/checkers/check_s3_five_rail_shor_recovery.py

Both passed; the adapter was rerun after its final edits. Receipt:
`results/encoded_history_memory.json`, including source hashes, the complete
75-error syndrome table and the two-error control.

The next physical obligation is to specify how noise couples to the encoded
history and implement the encoder/decoder and history-address controls. Existing
code algebra does not choose that coupling. Recovery work, ancillary readiness,
retained error information, microscopic locality and an autonomous latch remain
explicit obligations. No mass, lifetime or isotope-stability prediction follows.
