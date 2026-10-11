# Pairwise storage removes the history-address controls

## Constructive simplification

The earlier controller needed a history lookup to skip the initially occupied
bond. A different explicit battery architecture removes that operation entirely.
Give each of the 21 bond bits its own battery bit with the inherited gap

    delta = J-epsilon = 1/4.

For each pair use the reversible map

    F=(X tensor X) SWAP,
    (n,b) -> (1-b,1-n).

The four-state action exchanges 00 with 11 and fixes 01 and 10. Thus with ready
batteries, already occupied bonds are automatically skipped. No modular address
addition, history comparison or non-Clifford controlled lookup is needed.

This replaces the previous simple battery ladder plus separate history. The new
battery has independently addressable qubits and degenerate energy levels; it
is a different physical resource architecture, not a coordinate change.

## Where the history goes

For every occupation pattern n,

    |n>|0...0> -> |1...1>|complement(n)>.

The battery retains the old pattern. The map is a tensor product of involutions,
so it preserves arbitrary superpositions, phases and inputs with populated
batteries. Applying it again restores the input.

For the one-hot amplitude bank, the output is

    |all_filled> tensor sum_j c_j |all_battery_bits_except_j>.

The 21 history directions are now the 21 battery states of weight twenty.
All have the same battery energy five. No amplitude is discarded, and there
is no need for a separate ready-plus-21-label quantum history register.

The ready all-empty bond state with a **present coherent carrier** is also
filled by this map, charging all 21 battery bits. Its initial consistency
penalty 21J supplies the energy. This differs from the previous history-disabled
extension, which fixed that input. It is not charging the absent-carrier vacuum:
this construction is admitted in the occupied coherent sector.

## Energy boundary

On the coherent carrier, a pair has energy

    h(n,b)=epsilon*n+J*(1-n)+delta*b.

All four pair transitions preserve h. Therefore all matched-sector patterns
conserve energy under the complete endpoint map. For the one-hot input the
account remains

    initial 41/4 = filled bonds 21/4 + battery 5.

For a general carrier with seam mismatch P_e, the exact energy change is

    2*J*P_e*(n_after-n_before).

Every actual P_e annihilates N, but this is not a global energy-conservation
statement off that sector. The native carrier remains unchanged by the pair
operation; its physical protection is still a separate issue.

## Encoded implementation without the rejected transversal gate

The existing five-qubit code makes this gate particularly simple:

1. Swap the two identical code blocks using five corresponding physical SWAPs.
2. Apply the owning logical-X Pauli word to each block, six single-qubit Pauli
   operations in total.

Whole-block SWAP preserves the product code. It does **not** assume the railwise
logical CNOT/SUM that prior work refuted. The checker applies the actual physical
gates to all four encoded logical pair states with exact arithmetic and verifies
F, including phases.

For all pairs this uses 105 physical SWAPs and 126 single-qubit Pauli operations.
Encoding 21 bond bits and 21 battery bits uses 42 logical blocks / 210 physical
data qubits, excluding the native carrier, preparation and recovery ancillas.
These are gate-model resource counts, not physical energies or a minimality claim.

The physical decomposition gives the right endpoint. It does not prove that
every intermediate SWAP/Pauli commutes with the bare hold Hamiltonian. Pulse,
control and energy accounting during that implementation remain additional work.

## Bounded fault test

For one encoded pair, exact Pauli-support propagation checks:

- all 30 single physical-input-qubit Pauli cases remain one error under ideal
  gates;
- all 93 single-gate fault cases leave at most one error in each affected code
  block, assuming clean input. A SWAP fault may affect both participating qubits.

Fault-free component recovery therefore corrects those outputs using the prior
code theorem. This is a separated one-fault guarantee, not a threshold. A tested
input error plus a later SWAP fault leaves two errors in one block and lies
outside that guarantee. Arbitrary correlated logical battery-pattern phases
also remain outside the single-physical-qubit correction model.

## Verification and remaining tasks

    python research/voevodsky/checkers/check_pairwise_bond_battery_storage.py

Fresh final execution passed. Receipt: `results/pairwise_bond_battery_storage.json`.
It binds the actual seam source, owning code and preceding encoder receipt.

The modular-address bottleneck is removed in this declared architecture, rather
than supplied by an unjustified transversal gate. Remaining tasks are physical
noise coupling, encoded preparation/recovery resources, spatial routing,
intermediate control energy and an autonomous hold/release mechanism. The
battery's logical history still requires protection. No mass, isotope binding,
lifetime or stability prediction is added.
