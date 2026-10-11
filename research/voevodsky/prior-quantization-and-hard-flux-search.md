# Prior research clues: quantization and implementation of hard source flux

## Search scope and evidence status

Repository document search across research, followed by targeted reading in nima, voevodsky and kitaev. Searches included quantization, compact rotors, Fock construction, prequantization, phase locking, flatness projectors and constraint penalties. This is a bounded search, not a claim that the repository contains no other relevant work.

No mathematical checker was rerun for this audit. Statements about checks below describe the inspected documents' reported results. The rotor-action checker was also inspected to confirm its exact-arithmetic implementation and its explicit physical assumptions. These findings should not be represented as fresh verification.

## 1. Compact rotor quantization and a variational exact constraint already exist

Read `research/nima/mass-rotor-action-and-external-charge.md` and inspected `research/nima/checkers/check_mass_rotor_action_charge.py`.

The existing construction explicitly assumes compact angles with integer conjugate momenta and hbar=1. It compares two DIFFERENT mechanisms:

- Josephson-type phase locking, with potential J sum[1-cos(theta_s-theta_t)]. In the ideal rigid reduction the inertias add. Finite-J phase slips and relative-mode zero-point effects are not claimed to vanish.
- Auxiliary temporal gauge fields with action (dot(theta)-B a-A0*1)^T C (dot(theta)-B a-A0*1)/2. Varying a imposes the exact momentum constraint B^T n=0. The effective inertia is harmonic rather than additive.

This is already a candidate action-level realization of an exact constraint, not merely a penalty term. But it constrains charges/momenta, not the source-face coordinate flux C A of the present spinor. Transferring it requires a new, explicit adapter; changing the constraint type silently would be wrong. The auxiliary fields and action are admitted physical inputs, not derived from incidence alone.

Direct reuse: compact-coordinate/integer-momentum conventions, exact constraint variation, and separate audits of the external charge and energy normalization. Do not build another generic rotor model before comparing with this one.

## 2. The primitive quotient and sector protection have already been analyzed

`research/nima/mass-primitive-quotient-charge.md` constructs the quotient torus, its primitive degree-one character and explicit incidence flows relating different charge lifts. Its joint charge is Q=k-n_e. It repairs an earlier external-charge mismatch conditionally, but does not select the charging inertias. An allowed charge-preserving mixing operator also shows that charge conservation alone does not identify a particle sector.

`research/nima/mass-local-sector-protection.md` then supplies a conditional exact support theorem: exact Gauss constraints, a specified tensor-factor locality and charge conservation can forbid sector-changing matrix elements. It explicitly warns that finite constraint penalties admit virtual excursions and that diagonal local terms can still change energy gaps.

Checkers named there:

    research/nima/checkers/check_mass_primitive_quotient_charge.py
    research/nima/checkers/check_mass_local_sector_protection.py

Direct relevance: the three lead holonomies and their conjugate fluxes need a compactness/representation/charge-normalization audit before quantization. Our four classical optimal lead assignments are real numbers; they cannot simply be declared exact eigenvalues of standard integer rotor momenta. A choice of units, boundary conditions or representation must be explicit. This is a new application of the prior warning, not an already checked impossibility theorem for our model.

## 3. Rotor return was already tested and does NOT derive quantization

`research/nima/rotor-period-does-not-quantize-reduced-action.md` uses the completed phase/Hamilton–Jacobi lift, not a discarded precursor. Closed lifted rotor paths allow I=2*pi*r^2 for continuously variable r. Complete trajectory-action phase closure survives, but reduced-action integrality does not follow.

Horizontal transport PLUS an additional closed phase-fiber condition is a different protocol and can impose an integrality condition. It is not the dynamical rotor path and is not a spectral quantization theorem.

Checker: `research/nima/checkers/check_rotor_period_action_boundary.py`.

Consequence for us: the binary full-turn minus sign, a closed slow oscillation, or a lifted lead winding cannot by itself choose a quantum Hilbert space or hbar. The earlier claim that only the Born rule remained missing was explicitly withdrawn in that research. It should not be revived through the four-ray construction.

## 4. Executable quantum coefficient models already exist, conditionally

`research/nima/photon-creation-state.md` constructs an untruncated finite-support Fock-polynomial representation: creation by multiplication, annihilation by differentiation, factorial inner product and exact adjoint/CCR tests, including a high-occupation boundary control. Vacuum, bosonic algebra and inner product are declared extra physical assumptions, not inferred from a finite seed spectrum.

`research/nima/photon-local-quantum-dynamics.md` goes further: it constructs a Hermitian source/field interaction and tests rotating versus counter-rotating terms. The full interaction preserves excitation parity but not excitation number. Source-ground heralding therefore does not guarantee exactly one photon. The note separates its continuum first-order suppression bound from all-orders claims.

Checkers:

    research/nima/checkers/check_photon_creation_state.py
    research/nima/checkers/check_photon_local_quantum_dynamics.py

Direct reuse: exact algebra/adjointness tests, no false finite-cutoff CCR, and explicit symmetry-versus-number-protection checks. This is not an existing quantization of the spinor CP^3 phase space and does not select bosonic versus fermionic matter for it. Neither four classical rays nor their span supply a Fock prescription automatically.

## 5. Local quantum flatness projectors have a source model

`research/kitaev/s3-local-hamiltonian-source-model.md` constructs an oriented square on C[S3] tensor-powered over four edges. It derives the edge holonomy, based gauge action, diagonal flux projectors and Haar vertex projector. Its native Hamiltonian is the sum of commuting gauge and flatness projector penalties.

This is stronger than naming a formal flux projector: the microscopic edge support and commutators are supplied. It also finds that noncentral element-resolved flux pulses are not native commuting terms; physical availability of such extra controls remains conditional.

Checker: `research/kitaev/checkers/check_s3_local_source_model.py`.

Direct clue: construct an actual edge Hilbert space and check whether the proposed matter/current Hamiltonian preserves a sourced flux subspace. But the finite S3 flat sector is NOT our continuous U(1) relative flux with intrinsic +/-i Wilson phases. Changing gauge group, representation or projector changes the model. This packet supplies a reusable test pattern, not a completed physical implementation of our hard constraint.

## 6. Protection against perturbations has already been bounded carefully

`research/kitaev/toric-code-braiding-boundaries-perturbation.md` shows an explicit local perturbation that preserves the cellulation and homology but mixes neighboring plaquette syndromes. In the frozen example the relevant exact block has eigenvalues +/-sqrt(5). Its particular logical degeneracy survives, but the bare plaquette values do not remain conserved.

The note distinguishes its special finite test from generic perturbative stability, for which it points to spectral-flow/Lieb–Robinson control and a narrow low-energy band rather than exact commuting syndromes.

Consequence: topological geometry or a large gap cannot be cited as exact preservation of the present source holonomy. The already checked finite-cosine obstruction in `spinor-face-magnetic-action.md` remains operative. Any alternative protection mechanism must show invariance under the actual current-carrying matter coupling.

## What the search changes

The open tasks should be narrowed, not restarted:

1. **Quantization:** reuse the existing rotor and quantum-algebra machinery, but first specify the representation, symplectic/action normalization, matter statistics and ordering for this reduced model. Compare quantizing the constrained parent with quantizing the reduced state space; agreement is not automatic. The classical four-ray orbit is evidence about an energy functional, not four preselected orthogonal quantum states.
2. **Exact constraint:** reuse the auxiliary-field action pattern or the microscopic commuting-projector audit pattern. Either route needs a source-specific construction for C A=0, its secondary constraints, matter compatibility and the unchanged exterior cycles. Neither located predecessor already supplies that adapter.
3. **Finite stiffness:** retain it as a physically distinct model. It has already failed exact native-flux preservation classically. Any approximate quantum protection needs quantitative leakage/gap estimates, not an identification with the hard sector.

Recommended next executable step: a compact-lead representation audit using the existing rotor conventions, alongside an explicit parent-action proposal for source-face flatness. Test admissible charges, normalization and constraint preservation before trying to identify a quantum ground doublet or a measured mass.
