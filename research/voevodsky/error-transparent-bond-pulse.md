# One error-transparent pulse can conserve one explicitly extended hold law

## Result and prior recovery

The search found no ready-made error-transparent pulse in the prior packets.
The already verified code, syndrome table and reversible recovery circuit do
supply a uniform construction. It now gives **one implementation** with both
continuous energy conservation and correction of a single physical fault at any
pulse time, under the stated direct-Hamiltonian implementation assumption.

The important qualification is exact: the hold Hamiltonian agrees with the old
one on the code, but changes its extension into error sectors. This is not
silently counted as a coordinate change or a uniquely sourced physical law.
A separate witness shows that leaving that old extension unchanged is
incompatible with the desired error-transparent transfer on one actual sector.

## Construction from the existing recovery unitary

Let V be the existing one-logical-qubit encoding and E_s the identity or one of
the fifteen single-physical-qubit Pauli representatives. The actual coherent
recovery decoder R satisfies

    R E_s V|psi> = phase_s |s> tensor |psi>.

The phases do not depend on psi. The syndrome label is retained. Exact Gram
checks establish that these sixteen two-dimensional sectors are an orthogonal
basis of the full 32-dimensional component space, so R is unitary there.

Define uniformly

    X_ET = R^dagger (I_syndrome tensor X) R,
    Z_ET = R^dagger (I_syndrome tensor Z) R,
    Y_ET = i X_ET Z_ET.

For each representative,

    X_ET E_s V = E_s V X,
    Z_ET E_s V = E_s V Z.

The checker verifies these identities directly on the actual encoded states,
not just on an abstract syndrome table.

For the bond/battery pair take

    Q_ET = (I+Z_ET,A Z_ET,B-X_ET,A X_ET,B+Y_ET,A Y_ET,B)/4,
    H_ET = J*I + delta*(Z_ET,A-Z_ET,B)/2.

Here delta=J-epsilon=1/4 and J=1/2 remain the existing fixture. The same logical
projector and hold matrix occur in all 256 two-block syndrome sectors.
Therefore Q_ET is a positive projector and [Q_ET,H_ET]=0 on the whole pair
space. The pulse exp(-i theta Q_ET) reaches the old pair transfer at theta=pi.

The intertwining identities imply error transparency for every fault time:

    U_ET(T-t) E_s V U_logical(t) = E_s V U_logical(T).

Ideal recovery removes E_s and retains its syndrome, giving the intended logical
endpoint. This covers coherent errors in the declared error span, not just a
known classical Pauli. It does not cover repeated faults in one block or errors
during a noisy implementation of R itself.

## Why the old energy law cannot simply be retained off the code

Use the same physical Z fault that broke the previous direct pulse. It
anticommutes with the owning logical Z on the first block. Under the **old**
bare hold Hamiltonian:

    energy of E|00> = J-delta = 1/4,
    energy of E|11> = J+delta = 3/4.

An error-transparent transfer must carry E|00> to E|11>. That changes the old
bare energy by 1/2. Consequently such a transfer cannot commute with that
unchanged hold Hamiltonian on this error sector.

The new H_ET gives both states energy J, retaining the old code energies while
changing which energy is assigned to their error copies. It therefore resolves
the conflict only by an explicit new syndrome-resolved coupling law. An
alternative retaining the old error energies would need an additional energy
exchange degree of freedom with its coherence and recovery accounted for.

## Verification

    python research/voevodsky/checkers/check_error_transparent_bond_pulse.py

Fresh execution passed. Receipt: `results/error_transparent_bond_pulse.json`.
Checks include all 32 component recovery inverses, 1024 error-basis Gram entries,
actual error-sector X/Z intertwining, the logical energy/projector identities,
120 mid-pulse physical-fault/logical-input cases, and the old-energy obstruction.
The all-time result follows algebraically from those generator identities,
not from sampling fault times.

## Physical boundary

These generally many-body operators must be implemented as the declared direct
Hamiltonian for the transparency statement to apply. Merely performing a noisy
decode/gate/re-encode sequence does not inherit it. Local synthesis, noise rates,
physical admission of the changed error-sector energy law, recovery resources
and an autonomous controller/latch remain open.

This is a uniform existence witness with its changed physical input exposed.
It does not infer mass, isotope stability or memory lifetime, and does not repair
prior mass-comparison failures by changing an unreported energy reference.
