# The native vacuum energy can supply the qutrit bridge if fusion is coherently reversible

## Bounded question

Do the frozen \(D(S_3)\) ribbon, charge-projector, and charge-instrument packets
already contain a coherent first-pair phase distinguishing fusion channels
\(A\) and \(C\) on the protected \(C,C,C\to C\) qutrit?

They do not yet contain an executable coherent pair phase. But the missing
resource is narrower than an arbitrary new Hamiltonian. The fixed-point source
already distinguishes vacuum charge \(A\) energetically. A reversible coherent
fusion–wait–unfusion corridor would convert that native energy into exactly the
required pair-channel bridge.

## Four distinct levels

The present source contains four different objects that must not be
identified.

### Fusion-channel projectors

The categorical fusion basis supplies rank-one effects

\[
P_A^{(12)},
\qquad
P_B^{(12)},
\qquad
P_C^{(12)}
\]

on the first-pair channel of \(V_{CCC}^{C}\). These are exact mathematical
projectors once the fusion basis is frozen.

### Localized charge idempotents

The lattice crossed-product algebra supplies source-derived local charge
projectors

\[
Q_A,Q_B,Q_C
\]

at one localized identity-flux endpoint. Their operator formulas are finite
character-weighted sums. Only \(Q_A\), the vacuum constraint, belongs directly
to the native fixed-point Hamiltonian structure; \(Q_B\) and \(Q_C\) are not
independently tunable native terms.

### Charge measurement

The exact charge PVM and its Lüders branches exist as an instrument target.
The physical controlled extractor, centralizer Fourier circuit, and garbage
uncomputation remain uncompiled.

### Coherent charge clock

A nondegenerate unitary

\[
U_Q=\sum_e\lambda_eQ_e
\]

would provide charge-dependent phase kickback. It is equivalent to a clean
coherent charge extractor under additional controlled operations, but neither
side of that equivalence is native merely because the spectral formula exists.

Only the fourth level directly gives arbitrary coherent pair phases. The first
three do not automatically promote to it.

## Why Lüders measurement is not the bridge

Measuring the first-pair fusion channel and discarding the outcome produces

\[
\Delta_{12}(\rho)
=\sum_{e=A,B,C}P_e^{(12)}\rho P_e^{(12)}.
\]

This deletes every off-diagonal logical matrix element between distinct
fusion paths. A selective branch

\[
\rho\longmapsto P_e^{(12)}\rho P_e^{(12)}
\]

is rank reducing rather than unitary.

By contrast, the desired phase is

\[
e^{-itH_{12}}
=\sum_e e^{-itE_e}P_e^{(12)},
\]

which preserves coherence while changing relative phases. Equal outcome
probabilities or the existence of the same projectors does not equate these
instruments.

A destructive fusion measurement can contribute to a measurement-only
protocol only with additional ancillas, feed-forward, charge restoration, and
a proof of the resulting coherent logical channel. None is currently frozen.

## Conditional coherent fusion corridor

Suppose there exists a reversible isometry \(F_{12}\) that coherently brings
the first two \(C\) anyons into a localized fusion region and records their
total channel as the local charge at that region, without measuring it or
leaking it to the environment.

On the logical fusion basis, require

\[
F_{12}|e_L\rangle
=|\Phi_e\rangle,
\qquad
e\in\{A,B,C\},
\]

where \(|\Phi_e\rangle\) are mutually coherent physical branches with localized
total charge \(e\), and where the spectator third \(C\) charge and global total
\(C\) are preserved.

Let the fused region evolve under a native local Hamiltonian
\(H_{\mathrm{site}}\) with channel energies

\[
H_{\mathrm{site}}|\Phi_e\rangle
=E_e|\Phi_e\rangle.
\]

Then the closed corridor

\[
U_{12}(t)
=F_{12}^\dagger e^{-itH_{\mathrm{site}}}F_{12}
\]

acts on the qutrit as

\[
U_{12}(t)
=\operatorname{diag}
\bigl(e^{-itE_A},e^{-itE_B},e^{-itE_C}\bigr).
\]

The effective pair Hamiltonian is

\[
H_{12}^{\mathrm{eff}}
=E_AP_A^{(12)}+E_BP_B^{(12)}+E_CP_C^{(12)}.
\]

This is exactly the algebraic bridge family required by the preceding packet.

## Native vacuum split is sufficient

The fixed-point source distinguishes the vacuum projector \(Q_A\) from
nonvacuum charge. A local term of the form

\[
H_{\mathrm{site}}=\Delta(I-Q_A)
\]

gives

\[
E_A=0,
\qquad
E_B=E_C=\Delta.
\]

After coherent fusion, the corresponding pair Hamiltonian is

\[
H_{12}^{\mathrm{eff}}
=\Delta(P_B^{(12)}+P_C^{(12)}).
\]

Its bridge incidence is

\[
\langle w_2|H_{12}^{\mathrm{eff}}|u\rangle
=-\frac{\sqrt2}{3}\Delta.
\]

This is nonzero whenever \(\Delta\ne0\). Therefore an independently tunable
\(Q_C\) term is unnecessary for algebraic qutrit completion. Vacuum versus
nonvacuum energy already distinguishes \(A\) from \(C\).

The existing missing electric bridge can consequently be reduced to a coherent
configuration-control problem: map pair fusion channels reversibly into the
native local energy distinction, wait for a calibrated time, and map back.

## Why ordinary fusion is not automatically reversible

If the pair fuses to \(A\), the two excitations may annihilate into vacuum. If
it fuses to \(B\) or \(C\), a localized electric charge remains. These branches
have different apparent excitation content.

A destructive fusion process may therefore leave branch-dependent radiation,
workspace, position, or energy records. Once the environment can distinguish
the branches, qutrit coherence is lost.

The isometry \(F_{12}\) must retain enough coherent workspace to make every
branch reversible. Its inverse must recreate the two separated \(C\) anyons
with the original fusion amplitudes. A fusion rule

\[
C\otimes C=A\oplus B\oplus C
\]

asserts the allowed channels; it does not supply this physical isometry.

## Ribbon transport status

The frozen ribbon algebra gives exact oriented operators and fusion incidence
at the algebraic level. It establishes how charges can be created, transported,
and composed as source operators.

It does not yet provide a timed, reversible, leakage-bounded unitary that moves
the two encoded anyons into one fusion region and back while preserving an
unknown superposition of \(A,B,C\) channels. Applying a ribbon operator or
postselecting a fusion outcome is weaker than the required corridor.

Thus the source audit yields:

- abstract fusion channels: established;
- local vacuum projector and gap: established at fixed-point level;
- formal pair-channel measurement: available as an effect or Lüders target;
- clean coherent pair fusion and unfusion: unproved;
- calibrated closed pair phase: conditional on that unproved corridor.

## Fault surface of the corridor

Even an ideal \(F_{12}\) plus native waiting phase is not automatically
one-fault tolerant.

### Transport fault

A fault while moving one anyon may create leakage or alter the fusion channel.
It must remain local and be corrected before the moving excitation contacts
the other.

### Fusion fault

The recombination region touches both logical constituents. One elementary
fault there can become a logical pair-channel error unless the fusion gadget is
encoded, transversal, or verified.

### Timing or energy fault

An error in \(\Delta t\) is an overrotation in the intended logical bridge
direction. Storage syndrome does not detect it.

### Unfusion garbage

Branch-dependent workspace left after \(F_{12}^\dagger\) dephases the qutrit
even when the anyon positions and charges look correct.

### Corridor closure fault

If the anyons are not returned to their protected separation, later local
faults may retain joint logical access.

The coherent corridor solves the source incidence problem. A separate extended
gadget theorem must solve these fault modes.

## Highest-information next test

The next test is not another charge-probability calculation. It is:

> Construct or exclude a reversible microscopic isometry \(F_{12}\) from the
> separated \(C,C,C\to C\) code space to a fused local-charge configuration,
> with one common output workspace for the \(A,B,C\) branches and bounded
> leakage throughout the path.

The first falsifier is branch-dependent environment output. The second is a
path on which the spectral gap closes without a controlled code deformation.
The third is a single fusion-location fault with unrestricted logical support.

## Exact falsifiers

- Abstract pair projectors called coherent phase actuators.
- A Lüders pair measurement identified with unitary pair-channel evolution.
- Selective fusion postselection called a deterministic qutrit gate.
- The spectral formula for a charge clock called a native controlled unitary.
- Independent \(Q_C\) control claimed necessary despite a native vacuum versus
  nonvacuum energy split.
- The fusion rule claimed to provide a reversible microscopic fusion map.
- Vacuum and charged branches allowed to leave distinguishable garbage during
  the closed corridor.
- Waiting under the fused Hamiltonian claimed fault tolerant against timing
  error.
- Ribbon incidence promoted to a timed leakage-bounded transport unitary.

## Machine-readable source audit

```json
{
  "code": "fusion_wait_unfusion_qutrit_bridge",
  "encoding": "C,C,C_to_C",
  "pair_channels": ["A", "B", "C"],
  "abstract_pair_projectors": true,
  "localized_charge_projectors": true,
  "formal_luders_measurement": true,
  "coherent_charge_clock_native": false,
  "native_vacuum_projector": true,
  "native_energy_pattern": [0, "Delta", "Delta"],
  "bridge_incidence": "-sqrt(2)*Delta/3",
  "independent_QC_control_required": false,
  "coherent_fusion_isometry_compiled": false,
  "coherent_unfusion_compiled": false,
  "closed_pair_phase_executable": false,
  "primary_missing_constructor": "reversible coherent fusion corridor",
  "fault_tolerant_extended_gadget": false
}
```

## Deutschian explanation

The source already knows how to assign different energy to vacuum and charge.
The qutrit needs only to present its hidden pair channel to that existing
distinction without letting the environment learn which channel it presented.

Coherent fusion would do exactly that. It temporarily converts a distributed
relation into a local charge, lets the native Hamiltonian accumulate phase,
and restores the distributed encoding. Measurement fails because it turns the
temporary local distinction into a permanent external record.

The missing explanation is therefore a reversible physical history, not a new
spectral projector.

## Shared Carrier geometry and quantum coefficient lens

The shared Carrier pattern is encode–expose–act–hide: a protected relational
coordinate is reversibly exposed to a native local distinction, acted on, and
hidden again without residual records.

The quantum coefficient lens supplies coherent fusion amplitudes, local charge
projectors, dynamical phase, and the distinction between a Lüders instrument
and a unitary clock.

## Claim boundary

This packet proves the conditional fusion–wait–unfusion compiler and shows
that the native vacuum energy split is algebraically sufficient for the qutrit
bridge. It audits the frozen source and finds no existing executable coherent
fusion corridor. It does not construct \(F_{12}\), establish a microscopic gap
path, calibrate the phase, or prove fault tolerance.

## Process calibration

Excitement is 10/10 and confidence in the source audit is 9.5/10. The control
gap has narrowed from “find a new bridge Hamiltonian” to “construct a reversible
coherent fusion corridor using an already native vacuum-energy distinction.”
