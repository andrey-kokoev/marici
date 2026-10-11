# Continuous energy accounting and fault tolerance need the same implementation

## What is now checked

For the pair transfer F=(X tensor X) SWAP, the existing uniform spectral rule gives

    Q=(I-F)/2=(I+Z_n Z_b-X_n X_b+Y_n Y_b)/4,
    U(t)=I+(exp(-i*theta(t))-1)*Q.

At theta(T)=pi this is the previously checked transfer. In the native coherent
carrier sector, the hold Hamiltonian is

    H_hold=J*I+(J-epsilon)*(Z_n-Z_b)/2.

The exact identity [Q,H_hold]=0 proves bare-energy conservation at **every pulse
angle**, not merely at the endpoint. The actual source seam projectors still
annihilate N; no carrier-excitation conservation claim is added.

The checker constructs the encoded operators from the owning five-qubit code,
checks all four logical pair basis states, and evaluates exact half and full
pulses. The half-pulse phase -i lies in the existing exact coefficient field.
Linearity and the projector/commutator identities supply the all-time result.

## Control work remains explicit

For H(t)=H_hold+lambda(t)*Q, ideal control power is lambda_dot*<Q>.
Q commutes with the ideal total Hamiltonian, so its expectation is constant.
A pulse with lambda initially and finally zero therefore has zero **net** ideal
switching work, although coupling energy is present while it is on.

This is not a free controller or clock. Timing, switching, physical apparatus,
preparation and dissipation have not been derived. An indefinitely active pulse
returns amplitude rather than latching it. The earlier finite autonomous-clock
boundary remains in force.

## A physical mid-pulse error invalidates the previous fault guarantee

The direct encoded Q has Pauli interaction terms of weights 6, 6 and 10. It is
not the earlier circuit of physical block SWAPs and single-qubit Paulis. That
circuit's bounded fault propagation cannot be transferred merely because both
implement the same logical endpoint.

The checker inserts one physical Z fault halfway through the direct pulse, at
a site that anticommutes with both owning logical X and Z. It then finishes the
pulse and applies the correct single-error syndrome correction.

For encoded input |00>, the target is |11>, but the corrected output has target
fidelity exactly 1/2. The syndrome is corrected and the output lies in the code,
yet its logical state is wrong. The pulse commutes with stabilizers, so it does
not change the error syndrome while its interaction propagates a logical error.
Bare hold energy is unchanged in this explicit fixture.

This is a different failure from assuming a logical history error was a physical
single-qubit fault. Here the injected fault really is one physical Pauli. It
occurs **during an interacting gate**, outside the idle-storage recovery theorem.

## Updated comparison

| Implementation | Checked energy statement | Checked fault statement |
|---|---|---|
| Physical SWAP/Pauli circuit | Matched-sector endpoint energy | Bounded separated one-fault propagation |
| Direct spectral pulse | Matched-sector all-time bare-energy conservation | One mid-pulse physical fault can leave a logical error |

No single construction yet establishes both continuous physical energy accounting
and fault tolerance. A many-body Hamiltonian with the right endpoint is not a
substitute for that joint requirement.

## Verification and next gate

    python research/voevodsky/checkers/check_bond_battery_transfer_pulse.py

Fresh execution passed. Receipt: `results/bond_battery_transfer_pulse.json`,
with previous implementation hash, exact pulse identities and the fault witness.

Next search the existing error-transparent and energy-conserving gate work, then
test both requirements on the same implementation. Do not repair this by silently
switching between the two witnesses. Microscopic coupling, noise rates, locality,
autonomous holding and physical mass/lifetime claims remain outside the result.
