# Optical action and provenance ladder

## Instrument

Use a phase-stable Mach–Zehnder with polarization control. One arm contains the
unknown optical route; the other is a phase-locked local oscillator. Inject a
declared probe basis, record complex output amplitudes by balanced homodyne or
heterodyne detection, and place an authenticated nondestructive checkpoint or
trusted setting log between route elements. A separately declared orientation
contract fixes the handedness of the vector frame. A spinorial reference is an
additional port, not something inferred from ordinary polarization action.

These ports answer different questions:

| Port | Maximal recoverable domain | Residual ambiguity |
|---|---|---|
| Endpoint photodetection | intensities on injected probes | phase and all unprobed action |
| Phase-locked reference plus probe basis | complex transfer action on the declared probe span | representation kernels and route factorization |
| Orientation or positive chamber | oriented vector action | opposite spinor representatives |
| Spinorial coherent reference | chosen rotor sheet on its admitted domain | ordered route factorization |
| Authenticated internal checkpoint | ordered route in the declared finite library | histories outside that logged library |

## Exact hostile calculations

The checker retains, rather than explains away, six collisions.

First, fields `(1,0)` and `(i,0)` have equal endpoint intensities. Interference
with the fixed local oscillator `(1,0)` yields records `4` and `2`, so the
smallest phase-separating port is one coherent reference with frozen phase.

Second, the identity frame and the normal-reflected frame `diag(1,1,-1)` give
the same three coordinate-axis intensity records. Their determinants are `+1`
and `-1`. A declared orientation or positive chamber selects the proper sheet;
three unoriented axis records do not.

Third, opposite unit spinors `q` and `-q` induce the same vector rotation. Full
polarization-vector action therefore cannot distinguish them. A spinorial
interference port can: the frozen reference records are `4` and `0`. This port
is needed only when the spinor lift itself is physically in scope.

Fourth, the ordered routes `H` then `H` and `X` then `X` both have composite
transfer `I`, despite different intermediate actions. Even an invertible,
full-rank numeric chart of every composite matrix entry maps them to the same
point. Route type is not a coordinate of endpoint action. An authenticated
checkpoint after the first element separates these two routes.

Fifth, `diag(1,epsilon)` is injective for every positive `epsilon`, while its
minimum gain tends to zero. Finite injectivity is therefore weaker than robust
recoverability; a calibrated lower gain bound belongs in the execution claim.

Sixth, two detectors copying one scalar carrier have Jacobian rank one. Two
labels are not two independent fragments. Genuine fragment redundancy needs
separately accessible carriers with separately testable loss or erasure.

## Record resolution and irreversible leakage

For a multi-fragment which-route experiment, couple path to independently
addressable polarization or time-bin ancillas, then tomography each ancilla
separately and finally attempt the coherent inverse on all retained ancillas.
This distinguishes local redundancy from one global radiation mode merely
observed by several detectors.

Partial pointer overlap softens the orthogonal threshold: coherence is the
product of the retained overlaps. Phase-only marking has unit magnitude and
changes interference phase without creating local path distinguishability.
Loss of one orthogonal, route-correlated share is the physical irreversible
boundary for the accessible experiment: the reduced interference term is
zero, although the global closed evolution remains unitary.

## Verdicts and boundary

Existence passes because every port has an explicit optical role. Synthesis
passes because reference phase, probe basis, orientation, spinor access, and
route checkpoint are independently declared. Execution passes only as an
exact finite calculation; no laboratory execution is claimed. Fault coverage
passes for the six requested hostiles. Completion passes only on the declared
probe span and finite route library.

The construction does not infer phase, orientation, covariance, spinor sheet,
or route labels after seeing the desired separation.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_optical_action_provenance_ladder.py
```
