# An occupation-sensitive belt port and its vacuum-stability test

## New result

The symmetric combination of the two actual bridge-endpoint modes couples to the coherent belt state. Its squared overlap is exactly **1193/4485**. This complements the previously derived antisymmetric mismatch port, which is dark to that state.

The symmetric port is not a pure coherent-state selector. Its remaining weight lies in two source-derived collective excitations. We computed all three weights and the exact response, without introducing independent internal record factors.

A subsequent neutral-reference exchange test exposes an important physical distinction: hybridizing a zero-energy carrier mode produces an excitation below the putative empty vacuum. That is a vacuum-stability failure of this trial, not automatically a positive particle mass.

## Prior research reused

The preceding `belt-interface-response-and-prior-audit.md` documents the rotor, Gauss-law, locality, protected-kernel and minimal-interface-record audit. This step additionally inspected Nima's `research/nima/photon-source-emission.md`.

That emission construction already distinguishes an empty source/field vacuum from a one-excitation transfer block and explicitly supplies the source gap and coupling. We reuse that distinction rather than calling a new two-level mixing formula a vacuum derivation. The sector-offset issue is also already established in `mass-gap-symmetry-and-protected-kernel.md`.

What is new here is the **actual belt contact**, its spectral weights, and the resulting source-specific stability condition.

## 1. The coherent contact

Use the C3-aligned, normalized symmetric combination of bridge endpoints 0 and 3. It lies in the face-even sector. Its energies and spectral weights are

| Energy in common units | Contact weight |
|---|---:|
| 0 | 1193/4485 |
| 4485/3292 | 2099/8970 |
| 5391/3292 | 1/2 |

The weights are positive and sum to one. Therefore the exact port response is

    S_plus(z) = -(1193/4485)/z
                + (2099/8970)/(4485/3292-z)
                + (1/2)/(5391/3292-z).

Unlike the mismatch response, this has a pole at the coherent zero mode. It can sense or exchange amplitude with that mode.

A contact-density interaction |w><w| also generally changes the carrier state: on the normalized coherent state, its squared leakage outside the coherent line is r0(1-r0), where r0=1193/4485. Thus replacing this local contact by an exact coherent-occupation projector would erase real excitation channels.

## 2. A declared neutral-reference exchange test

Supply a neutral reference excitation of positive energy epsilon, an exchange strength g, and a possible common carrier offset mu. The one-excitation block is

    H_1 = [[epsilon, g<w|],
           [g|w>, K+mu I]].

The empty zero-excitation state has energy zero. Total excitation number is conserved by this trial. The reference is not identified with a charged electron, and this is not a source-derived creation law.

At mu=0, restrict a trial vector to the reference excitation and the coherent carrier mode. Choosing reference amplitude -g sqrt(r0)/epsilon gives the negative Rayleigh quotient

    -g^2 r0 epsilon / (epsilon^2+g^2 r0).

For any nonzero g, there is therefore an excitation below the empty reference vacuum. Calling the lowered eigenvalue a new vacuum changes the physical sector assignment; it cannot be done silently while preserving the original interpretation of empty and occupied states.

This conclusion applies to the declared exchange test. Interacting fields, new constraints or a different physical vacuum could change it, but none is supplied by the finite carrier geometry alone.

## 3. Exact stability condition

For mu>0, the carrier block is positive. Schur reduction gives the necessary and sufficient condition for this one-excitation block to be positive semidefinite:

    epsilon >= g^2 S_plus(-mu).

The right side decreases strictly from infinity to zero as mu increases. A unique positive threshold exists. At equality the coupled block has a **zero** eigenvalue; above it the block is positive definite.

Illustrative checks with epsilon=1 give:

| g | Offset threshold mu |
|---|---:|
| 1/10 | 0.002672706416 |
| 1/2 | 0.075029142027 |
| 1 | 0.424523745879 |

These are test parameters, not mass fits. Selecting the threshold cannot derive a nonzero particle mass: the excitation gap at that threshold is zero. Choosing an offset above it still requires a physical law fixing that offset and the reference interaction.

## 4. Where this leaves the mass bridge

We now have both source-derived interface responses:

- **Mismatch port:** three odd modes; coherent state dark.
- **Symmetric contact:** coherent mode plus two even excitations; nonzero occupation sensitivity.

The previously missing overlap is therefore explicit. The next missing object is a physical vacuum/reference interaction whose charge, excitation sectors and positive spectrum are consistent together. A bare exchange with the zero-energy constraint state does not supply that object, and redefining its negative level as vacuum would change the model rather than complete the existing mass derivation.

## Verification

    python research/voevodsky/checkers/check_belt_coherent_port_vacuum.py

Results: `research/voevodsky/results/belt_coherent_port_vacuum.json`.

Exact rational calculations verify the spectral projectors, contact weights, response, negative Rayleigh witnesses and rational brackets on the stability thresholds. No independent internal qubits, measured mass calibration or relativistic mass identification is introduced.
