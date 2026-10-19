# Scattering Hamiltonian bridge: conceptual audit

## Question and disposition

Can the interface-preserving retained coefficient Hamiltonian be identified with an autonomous scattering model? The literal whole-system identification is obstructed on an absolutely continuous scattering sector. A finite internal-core or boundary-response contribution remains possible but requires a different, explicit contract.

This is a new written mathematical analysis, not an assigned conjecture outcome or a change to the frozen scattering net. It does not certify that either model is physically selected. No stationary scattering solve, measurement work, source-owner checker replay, or new formal-kernel proof is performed here.

Sources read:

- `research/strominger/interface-preserving-carrier-hamiltonian.md`
- `research/strominger/retained-hamiltonian-observer.md`
- `research/strominger/neutron-autonomous-rim-scattering.md`
- `research/scattering/high-energy/pentachoron_autonomous_contact_note.md`
- `research/nima/contracts/scattering-strominger-update.v1.json`

The neutron two-rim model, the earlier pentachoron contact reduction and the latest strained packet model are different models. Their operators and channel maps are not identified here.

## 1. Type the two systems before comparing energy

### Retained coefficient system

Per scalar response channel the source is a real 137-dimensional field f. Four such channels give the matrix field F. Its declared evolution and energy are

    f' = A f,       A^T = -A,
    H_coeff(F) = ||A F||^2 / 4.

The reported squared-frequency bands are 32 (dimension 36), 128 (dimension 2), and 0 (dimension 99). Complete retained T9 is an injective redundant chart, not extra independent dynamics: LT=I and B_T9 T=T A. The 38-row reader reconstructs this particular quadratic energy; its kernel records remain retained.

The classical quadratic-energy Hessian is K_coeff=A^T A/2. It is NOT automatically the operator generating a quantum Schrödinger equation. In the natural complexification of f'=Af, the Schrödinger generator is Q=i*hbar*A. Q is Hermitian but has both signs on each nonzero rotation plane. K_coeff instead has the same positive eigenvalue on both signs of such a plane.

Thus matching H_coeff to a quantum expectation, or substituting K_coeff for the scattering generator, needs an explicit encoding, metric, complex structure and normalization. A different positive-frequency quantization might be possible; this observation does not exclude it. It does exclude treating that quantization as already supplied by the energy reader.

### Autonomous contact scattering

For the two-rim source, the state is

    H_sc = (L2(R) tensor C^2) direct-sum C^24.

Its lead kinetic operator is -kappa*d^2/dx^2+H_lead. Its core operator is K_core, with contact eta*||sqrt(ell)*psi(0)-W^dagger*chi||^2. The inherited metric is whitened before these expressions are used.

The earlier pentachoron reduction has 20 lead and 20 core coordinates instead. Neither finite core is the whole scattering state. Propagating leads have continuous energy and incoming/outgoing unit-flux channel normalization. Bound/dark states and prepared scattering states are distinct spectral sectors.

## 2. Written obstruction: no finite autonomous encoding of an AC scattering sector

Let H be self-adjoint, and let H_ac be an invariant absolutely continuous spectral subspace. Let Q be any finite-dimensional Hermitian generator, including a complexified finite coefficient system after units are declared.

There is no nonzero time-independent linear map J from the finite space into H_ac satisfying

    exp(-itH/hbar) J = J exp(-itQ/hbar)    for every real t.

Proof: diagonalize Q. For an eigenvector v with eigenvalue q, intertwining gives U_H(t)Jv=exp(-itq/hbar)Jv. If Jv is nonzero, Stone's generator characterization makes it an H eigenvector of energy q. An absolutely continuous spectral subspace contains no nonzero eigenvectors. Hence Jv=0 for every eigenvector, so J=0. A finite-domain linear map is bounded automatically.

Likewise any bounded linear intertwiner from H_ac to a finite unitary system is zero: its adjoint intertwines in the reverse direction, reducing to the same proof. Equivalently, exact autonomous finite observation would require a finite point-spectral component, not an AC scattering component.

Scope: this theorem is conditional on the specified sector being absolutely continuous; it does not prove asymptotic completeness of the supplied contact model. It does not rule out maps to bound or dark sectors, energy-dependent generalized-state encodings, finite truncations, nonlinear observations, driven finite systems or infinite-dimensional extensions. Generalized plane waves are not normalizable counterexamples. A map to a bound sector would not explain incoming/outgoing scattering.

Conclusion: stop searching for exact whole-scattering equivalence with the unchanged finite coefficient model. Equal energies, equal conserved norms, matching dimensions of a boundary solve, and a common word such as Hamiltonian cannot remove this obstruction.

## 3. Why the core alone is not an autonomous scattering state

Put

    D = K_core + eta W W^dagger,
    B = eta sqrt(ell) W.

The actual core equation is

    i*hbar*chi'(t) = D chi(t) - B psi(0,t).

The boundary value of the moving lead drives the core. Identical chi with different psi(0) can have different derivatives. Conversely identical lead fields with different retained chi give different boundary forces. Discarding either component is not an autonomous quotient of the interacting system.

With initial time t0 the exact core solution is

    chi(t) = exp(-iD(t-t0)/hbar) chi(t0)
             + (i/hbar) integral[t0,t] exp(-iD(t-s)/hbar) B psi(0,s) ds.

Eliminating chi produces a memory kernel plus an initial-core term, not a closed instantaneous law on the lead alone. Setting the initial bound/dark component to zero is a preparation condition, not a reset law for arbitrary states.

At stationary energy away from core poles,

    V_eff(E) = eta ell I + B^dagger (E-D)^(-1) B.

For real E outside the spectrum of D,

    dV_eff/dE = -B^dagger (E-D)^(-2) B.

On every channel vector u with Bu nonzero this derivative has strictly negative quadratic form. Consequently an energy-independent boundary coefficient cannot equal this retained-core response on an open energy interval, unless the relevant coupling vanishes. The derivative statement is not a claim that scattering probabilities are monotone: solving lead matching, thresholds and interference changes that question.

A finite autonomous core can therefore be part of scattering, but its coupled response is energy dependent and lead driven. This is the proper place to look for a retained coefficient contribution.

## 4. Replacement bridge contract

A proposal must choose one scope, not slide between them:

1. **Bound/dark-sector map:** intertwine with a point-spectral sector; explicitly excludes explaining scattering amplitudes.
2. **Internal-core realization:** encode a specified coefficient subsystem into a specified core, and separately supply the lead/contact extension. This is the relevant candidate.
3. **Boundary response realization:** specify an input/output system with retained memory and prove equality of its transfer function on a declared energy/domain set; not whole-state equivalence.
4. **Approximation:** provide a norm, energy band, time interval and error estimate; no exact-equivalence claim.

For an internal-core proposal the required data are:

- A declared real-to-complex encoding/complex structure and physical or model time convention. State explicitly which operator Q generates encoded motion and which observable represents H_coeff.
- A named scattering model, its metric, form domain and core operator D. Do not import the two-rim result into the strained pentachoron model by analogy.
- A state map J with retained-kernel policy and a generator square D J=J Q on the stated subspace. An energy shift or time scale must be declared, not fitted silently.
- A separate energy-form comparison. Generator intertwining alone does not identify the coefficient quadratic energy with the scattering energy ledger.
- Contact maps B and B^dagger, lead thresholds/kinetic law, and retained contact diagonal terms. If a smaller core is used, establish invariance of the channel-generated Krylov subspace and retain its complement.
- Incoming/outgoing channel maps with unit-flux normalization and covariance under source basis changes. Prove equality of the resulting resolvent/contact response, not just equality of a core spectrum.
- An explicit preparation class: incoming scattering continuum with no incoming bound/dark component, or another separately justified preparation.

The reported five-dimensional accessible neutron core is a candidate comparison target, not a supplied map from the 38-dimensional active coefficient system. Equality of its boundary-solve dimension or selection of five convenient coefficient coordinates would not satisfy this contract.

## 5. Next bounded conceptual task

First inventory the actual encoded generator, metric, active spectrum and channel-coupling subspace on both sides. Decide whether a source-authorized nonzero invariant coefficient subsystem can intertwine with the named core while preserving the required energy and contact maps. If it cannot, record model separation and retain both constructions independently. Do not adjust source laws to fit desired amplitudes.

Only after that test should a new lead-coupled coefficient model be considered. Adding a continuum kinetic law, threshold and coupling is new model input; it is not derived by the current finite observer. Independent justification of the switching/contact law remains a separate conceptual obligation even if a mathematical core bridge succeeds.

## Verification boundary

`research/nima/checkers/check_scattering_bridge_conceptual_audit.py` provides exact finite illustrative controls: opposite-frequency energy separation, retained-core dependence, a nonconstant resolvent response, finite spectral obstruction examples and coupling-versus-core separation. These controls do not formally verify the general spectral theorem or verify the actual source matrices. The no-go and memory/resolvent identities above are written arguments; no Agda/Rzk closure is claimed.

Fresh execution passed all five illustrative controls via structured-command, exit 0: `structured_command_execution:e_12616_1791929751233846400_109`. Receipt: `research/nima/results/scattering-bridge-conceptual-audit-v1.json`. The checker is replayed after this report update so the receipt hashes the final note. The execution reference above names the initial successful run.
