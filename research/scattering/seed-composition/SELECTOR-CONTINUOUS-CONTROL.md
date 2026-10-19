# Bounded continuous feedback generators with an identity complement

**Fourth batch, iteration 4 of 20.**

**Strength:** exact Hermitian generator, spectral pulse identity and conditional control algebra. Not implemented continuous control or physical spin identification.

[Previous feedback](SELECTOR-FAILURE-FEEDBACK.md) · [Checker](check_selector_continuous_control.py) · [Receipt](results/selector-continuous-control.v1.json)

## 1. Fresh continuous construction

For a half-quaternion failure branch let S_g=sign(a_g)T_g P_plus. The previous exact identity S_g+S_g*=P_plus gives the Hermitian generator

    J_g=(S_g-S_g*)/(i sqrt(3)).

Exact checks establish

    J_g*=J_g, J_g²=P_plus, tr(J_g)=0,
    J_g P_minus=P_minus J_g=0.

Its ground spectrum is {-1,0,0,1}; its norm is one. The rank-one eigenprojectors on plus are (P_plus±J_g)/2. Consequently its exponential for any real angle is

    exp(-i theta J_g)=P_minus+cos(theta)P_plus-i sin(theta)J_g.

Choose

    theta=acos(-1/(2 sqrt(19))),
    cos(theta)=-1/(2 sqrt(19)),
    sin(theta)=5 sqrt(3)/(2 sqrt(19)).

The pulse is exactly the prior inverse-polar feedback. The checker compares its coefficients in the same X+sqrt(19)Y representation, not by fitting a numerical exponential. The central branches need zero generator and zero angle. A floating-point angle is included only as an illustration in the receipt.

## 2. Full gauge-preserving extension

Using the prior individually gauge-preserving group representation and its fundamental central projector,

    J_full,g=sign(a_g)(U_hat_g-U_hat_g*)P_full/(i sqrt(3)).

Every fundamental copy obeys the same square identity. Thus this is a bounded Hermitian operator of norm one with square P_full; its generator is zero on the complement, whose pulse is identity. It commutes with each Gauss generator and preserves total charge. The inherited joint symmetry makes it compatible with the physical Hamiltonian and ground.

This is an operator construction, not a local hardware Hamiltonian. No off-kernel Hamiltonian commutation is claimed. The central projector and joint matter/field controls still require implementation.

## 3. Conditional control algebra

The sixteen half-quaternion branches give eight distinct nonzero ground axes. Their Hermitian span has dimension three. Exact commutator closure on a three-axis basis verifies the traceless su(2) algebra on plus, with zero action on minus.

Hence supplying these continuous generators would supply logical continuous rotations, not merely the finite native symmetry words. This is conditional control availability. It does not establish continuous physical spatial rotations, spin statistics or a natural particle interpretation.

## 4. Pulse and work obligations

A declared control Hamiltonian is

    H_ctrl(t)=hbar Omega_g(t) J_full,g,
    integral Omega_g(t) dt=theta.

For this fixed-axis pulse family, a bound |Omega|≤Omega_max implies duration at least theta/Omega_max. Action units, timing, phase reference, branch-conditioned addressing and pulse synthesis remain extra inputs. The native fixed Hamiltonian alone cannot implement the nontrivial feedback; its action on the degenerate ground is scalar.

An ideal physical pulse commutes with the endpoint Hamiltonian, so that Hamiltonian's expectation is conserved continuously. This does not make the physical control supply, clock, readout or feedback work-free. It is distinct from the earlier swap factorization, whose individual stages can change charging energy.

With the same exact axis/projector but a pulse-area error delta, the residual operation is exp(-i delta J_g). Its operator distance from identity is 2|sin(delta/2)|. It remains sector preserving and unitary, so failure probabilities are unchanged, while plus logical state can change. Axis or complement-coupling errors are not covered by that statement.

## 5. Next calibration gate

Compute the history-averaged logical channel of these residual rotations over the actual branch probabilities and retries. Retain the branch histories rather than treat the averaged channel as intrinsic information destruction. Compare sector-preserving calibration error with an explicit complement-coupling perturbation, distinguishing logical fidelity from selection probability.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical feedback platform, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_selector_continuous_control.py
python research/scattering/seed-composition/check_selector_continuous_control.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The prerequisite branch feedback is freshly recomputed. Exact field arithmetic checks spectra, pulse coefficients and control-algebra closure. The exponential formula and full-isotypic extension are stated mathematical arguments, not new machine-formal or physical admission.
