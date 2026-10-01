# Photon-producing two-packet vector: construction programme

## Objective and current status

Objective: construct a photon-producing vector from the retained two-endpoint packet data, rather than merely name a rank-two space after photon polarization.

Through iteration 10, the conditional seed/Maxwell/Fock construction, engineered emission model and local-current alternatives have been checked. The zero-gap real-current control has exact all-orders statistics and a certified approximate-one-photon source herald. An explicit EXACT AVAILABLE-ONE-PHOTON output contract is now checked only under an ADDITIONAL ideal total-number nondemolition instrument; an absorbing count leaves vacuum instead. The positive-gap circular-source continuum dynamics, seed-only model selection and apparatus realization remain open. A “two-packet” here means the existing `TwoPacket(label, source, target)` primitive; it does not mean two photons or a vector with only two entries.

Fresh source state read for this iteration:

- `checkers/check_triangle_half_phase.py`: actual two-endpoint packet type and complex arithmetic convention;
- `checkers/check_natural_tower_return.py`: the actual six-arrow registry and four-vertex spectrum;
- `checkers/check_whole_seed_occurrence_spectrum.py`: lifted occurrence eigenprojectors and retained zero sector;
- `research/flavor/flavor-complete-gauge-gram-rank.md`: the separate conditional electromagnetic null direction, which assumes gauge fields/vacuum and is not a seed-packet identification.

## Explicit seed-supported candidate

Keep the primitive order

    (AB, BC, CA, BA, AD, DB)

and the incoming continuation convention K[b,a]=1 when target(a)=source(b). With omega=(-1+i sqrt(3))/2, define the coefficient vectors

    g_plus  = (1,-1,-omega^2,-1,1,omega^2),
    g_minus = conjugate(g_plus).

These are actual vectors on the six registered two-packet occurrences, not newly inserted arrows or fictitious photon records. They obey

    K g_plus = omega g_plus,
    K g_minus = conjugate(omega) g_minus,
    K^3 g_plus/minus = g_plus/minus.

The previously constructed global complex eigenprojectors select exactly these lines. All real-eigenvalue projectors and the rank-two zero-sector projector annihilate them. Thus the candidate is not obtained by interpreting a zero incidence eigenvalue as zero particle mass.

Each coefficient has unit modulus. The overall amplitude is a convention; no physical energy scale is fixed. Dividing by sqrt(6) normalizes each line in the metrics discussed below, but does not establish a photon-number or preparation interpretation.

The pair spans the complexification of a real two-plane. It is not an assertion of a two-photon state.

## The norm check matters

In the inherited six-slot counting metric, the two eigenvectors are NOT orthogonal:

    <g_plus,g_minus> = 3-i sqrt(3).

For the superposition g_plus+g_minus, the counting norm squared changes from 18 to 12 under K. Therefore unit-modulus incidence eigenvalues alone do not establish unitary transport of arbitrary polarization superpositions in that metric.

Write g_plus=u+i sqrt(3) w, with rational six-vectors u,w. In their real-plane coordinates,

    T = [[-1/2,  1/2],
         [-3/2, -1/2]],
    G0 = [[9/2, 1/2],
          [1/2, 1/2]].

Finite-group averaging of the declared counting metric gives

    G = (G0+T^T G0 T+(T^2)^T G0 T^2)/3
      = diag(3,1),
    T^T G T = G.

This is positive definite on the candidate plane and makes the conjugate eigenvectors orthogonal with squared norm six. It is an explicit mathematical metric construction, not an independently derived physical energy or Born metric.

## Photon-identification hostile

Even if one additionally declares the C3 generator to represent a physical rotation through 2pi/3, its characters cannot distinguish helicity one from helicity four:

    omega^1 = omega^4 = omega^7 = omega^(-2).

The conjugate characters also coincide. At angle pi/3 the hypothetical continuous lifts with weights one and four differ. That angle's physical action is not present in the seed incidence data.

Consequently the candidate supports a conjugate phase pair, but does not yet select continuous helicities +1 and -1. The interpretation of K as a spatial rotation is itself extra data. No physical time, frequency, Planck relation or mass shell follows from its three-step period.

## Photon gates

| Gate | Status after iteration 1 |
|---|---|
|Explicit vector on the actual two-packet registry|Constructed and checked|
|Conjugate cyclic mode pair|Constructed and checked|
|Positive invariant inner product on its real plane|Constructed by an explicit averaging convention|
|Continuous spacetime helicities +1 and -1|Open; the same C3 characters also admit +4 and -4|
|Nonzero null four-momentum and massless dispersion|Not supplied|
|Transverse polarization modulo gauge|Not supplied|
|Electromagnetic current coupling / Ward-compatible readout|Not supplied|
|Physical preparation of these packet coefficients|Not supplied|

## Verification

    python research/nima/checkers/check_photon_two_packet_candidate.py

Fresh exact checks pass for the candidate, spectral-projector selection, norm boundary, invariant metric and helicity-alias control. The run invokes the previous whole-seed closure checker, including retained composition and observation checks. Reversed packet manifests, zero vectors, incorrect eigenvalues and a local-triangle-only truncation are rejected.

Report: `results/photon-two-packet-candidate.json`.

## Iteration 2: conditional Maxwell adapter completed

`photon-maxwell-adapter.md` records the explicit map

    a*u+b*w -> [(0,sqrt(3)*a,-b,0)]

at supplied k=(E,0,0,E), E>0, in Minkowski signature (+---), modulo epsilon~epsilon+alpha*k. Exact nullness, transversality, Maxwell/Bianchi, gauge-decode, transverse-metric and continuous rotation-helicity checks pass. With U(R_theta)=exp(-i*h*theta), g_plus maps to helicity -1 and g_minus to +1. Conserved-current pairing is gauge invariant under an explicit supplied conservation condition.

This does not derive the imported geometry, null momentum or spin-one vector representation. The same seed works at two distinct energies, and the spin-four alias is excluded only by the added continuous rotation action. These are explicit selection gaps, not completed seed derivations.

Fresh command: `python research/nima/checkers/check_photon_maxwell_adapter.py`.

Report: `results/photon-maxwell-adapter.json`.

## Iteration 3: conditional Lorentz/gauge transport completed

`photon-lorentz-transport.md` records exact proper orthochronous transport, field-strength and Maxwell-operator covariance, frame-aware seed decoding, and retained operation histories. The null little-group translation part acts only by gauge, while its rotation part supplies the previously declared helicity phases, including at noncollinear transported momentum.

A same-momentum/wrong-frame control shows why the frame cannot be discarded: little-group rotations can change linear polarization rather than merely its gauge. Lorentz and gauge operations remain imported physical-model structure, not output of the source incidence.

Fresh command: `python research/nima/checkers/check_photon_lorentz_transport.py`.

Report: `results/photon-lorentz-transport.json`.

## Iteration 4: conditional one-photon creation state completed

`photon-creation-state.md` constructs, for v=a*u+b*w,

    C(v)=beta*a_+^dagger+alpha*a_-^dagger,
    beta=(a+i*b/sqrt(3))/2, alpha=(a-i*b/sqrt(3))/2,
    |gamma(v)>=C(v)|0>/sqrt(|beta|^2+|alpha|^2).

Exact untruncated finite-support bosonic algebra checks give photon number one with zero number variance, gauge-independent coefficients and the correct fixed-frame helicity phases. In particular g_plus maps to a_-^dagger|0> and g_minus to a_+^dagger|0> in the declared normalized mode fixture. The vacuum, bosonic algebra and normalized mode are explicit imported assumptions. A creation operator is not a unitary emission apparatus.

Fresh command: `python research/nima/checkers/check_photon_creation_state.py`.

Report: `results/photon-creation-state.json`.

## Iteration 5: continuum wavepacket completed

`photon-momentum-wavepacket.md` supplies a compact light-front momentum profile with q in [1,2], u,v in [-1/2,1/2] and invariant measure dmu=(q/2)dq du dv. Its volume is 3/4. Smearing the creation operators with c_h*1_box/sqrt(V*sum|c|^2) gives exact unit norm and one photon under the declared continuum CCR.

Analytic moments give <P>=(49/54,0,0,35/54), <P^2>=0 but <P>^2=98/243. The latter is directional spread, not photon mass. Momentum-dependent Wigner phases, invariant-measure Jacobians, chart-pole transport and overlapping-profile controls pass. Free evolution leaks out of the single fixed profile with norm squared Var(H)>0; a stationary single-frequency oscillator is not an adequate emission model.

Fresh command: `python research/nima/checkers/check_photon_momentum_wavepacket.py`.

Report: `results/photon-momentum-wavepacket.json`.

## Iteration 6: conditional driven emission completed

`photon-source-emission.md` constructs V_I(t)=g(t)[zeta*sigma_- A_psi^dagger+h.c.]. Its exact one-excitation unitary takes |e,0> to cos(theta)|e,0>-i*zeta*sin(theta)|g,psi>. A pi/2 matched pulse depletes the source and emits one photon; partial pulses retain the no-emission branch. The Schrödinger coupling explicitly includes exp[-i(omega-Omega)t]; the outgoing free profile phase is retained rather than dropped.

For full transfer at source gap 1, the mean external work is -5/54 and its TPM variance is 799/23328. Matching the gap to mean photon energy gives zero mean work but leaves the positive continuum commutator norm/variance. This is a driven global-control model, not autonomous source-plus-field energy conservation.

Fresh command: `python research/nima/checkers/check_photon_source_emission.py`.

Report: `results/photon-source-emission.json`.

## Iteration 7: conserved local source and profile obstruction

`photon-local-current.md` constructs d=(sqrt(3)*a,-b,0), M^{0i}=d_i f, M^{i0}=-d_i f and j^mu=partial_nu M^{nu mu}. Conservation is identical; the reduced Fourier current J=(k_vec.d,omega*d) satisfies the off-shell Ward identity and gives gauge-independent radiation.

A compact-spacetime transition current has analytic on-shell Fourier amplitude, so it cannot reproduce the nonzero exact compact momentum top-hat. Compact smooth bump and Gaussian envelopes give different normalizable radiation profiles. The Fourier-normalized unit-width Gaussian circular candidate has amplitude norm pi, <omega>=3*sqrt(pi)/(4*sqrt(2)) and <omega^2>=1. Local electric-dipole radiation correlates helicity with direction; the +z helicity assignment is not global helicity purity.

This is a FIRST-ORDER quantum transition-current construction, not the previous exact global-control transfer law. A classical current would instead generate a coherent field. No unit-probability emission or all-orders single-photon claim is inherited by the new local source.

Fresh command: `python research/nima/checkers/check_photon_local_current.py`.

Report: `results/photon-local-current.json`.

## Gap/counter-rotating audit (iteration 8, completed during 9)

`photon-local-quantum-dynamics.md` includes the source gap inside the antisymmetric-tensor construction. Differentiating the source phase is essential to current conservation. The complete bilinear interaction preserves excitation PARITY, not excitation number; a source-ground herald can retain three photons. An exact two-mode witness and an integrated Gaussian first-order counter/emission ratio below 10^-12 are checked, with their distinct scopes explicit. That ratio is not an all-orders multiphoton bound.

Command: `python research/nima/checkers/check_photon_local_quantum_dynamics.py`.
Report: `results/photon-local-quantum-dynamics.json`.

## Iteration 9: exact driven control and certified approximate-one-photon herald

`photon-coherent-herald.md` uses the retained real seed vector

    v_lin=(g_plus+g_minus)/2=(1,-1,1/2,-1,1,-1/2).

A separately declared degenerate qubit controls a real conserved current, j_hat=X*j_real. Central field commutators give an exact conditional displacement. Source-flip heralding selects an odd coherent superposition, with

    P_flip=(1-exp(-2mu))/2, F_1=mu/sinh(mu).

At supplied gain mu=1/10, the ALL-ORDERS one-photon infidelity is at most 10/6007<0.002 and the herald probability is at least 0.09. At mu=1/100, infidelity is below 0.00002 with herald probability at least 0.0099. The mathematical source readout does not absorb the output field.

The source gap is explicitly zero; radiated energy comes from external control. This is not a solution of the positive-gap circular-source model, and source heralding still does not certify EXACTLY one photon.

Command: `python research/nima/checkers/check_photon_coherent_herald.py`.
Report: `results/photon-coherent-herald.json`.

## Iteration 10: exact available-output contract and detector controls

`photon-output-contract.md` states the explicit normalized Gaussian one-photon wavepacket produced conditionally from v_lin. It verifies that an additional ideal total-number Lüders instrument Pi_1 preserves that wavepacket, with JOINT success probability mu*exp(-mu). At mu=1/10 this lies between 9/100 and 1/11.

The instrument is a declared mathematical assumption, not a derived detector. An absorbing exact-one counter has the same event effect Pi_1 but leaves vacuum. An exactly-one tap count after the odd source herald leaves even photon numbers, not one. Extra-mode and coherence controls prevent confusing a partial number measurement with the required total-number, coherence-preserving instrument.

Command: `python research/nima/checkers/check_photon_output_contract.py`.
Report: `results/photon-output-contract.json`.

## Current photon gates after iteration 10

- Seed-supported vector and conditional Maxwell/Lorentz/Fock realization: checked with imported assumptions.
- Exact engineered global transfer: checked within its own driven model, not a local realization.
- Conserved local-current alternatives: constructed; exact old top-hat excluded.
- Gap/counter-rotating audit: parity protection established, excitation-number protection rejected without an approximation.
- Zero-gap real-current control: exact all-orders output statistics and a certified approximate-one-photon herald established.
- Positive-gap circular-source all-orders continuum dynamics: still open; the separate control is not a replacement proof.
- Exact available-photon output: mathematically certified only with an additional ideal total-number nondemolition instrument; an absorbing one-count event is not sufficient.
- Source/readout implementation, recoil, reservoir closure and detector calibration: not supplied by the seed.

## Native clock/spatial continuation audit

`photon-native-spatial-step.md` returns to the native evolution question rather than adding another field/readout model. It attaches the established unit-rate phase clock to the actual continuation through q=sqrt(3)*a, p=b in the existing adjoint rotor. The specified positive lift gives Delta T=pi/3 per K update, with adjoint phase increment 2*pi/3.

A correction matters: the earlier circular spatial adapter is compatible but is NOT the existing target-incidence spatial contrast. That endpoint reader gives (0,-3,1) -> (0,0,-2) -> (0,3,1) -> (0,-3,1), with squared Euclidean lengths 10,4,10. It is a signed amplitude contrast, not a particle trajectory.

Full histories grow from 6 to 26 records across the three-step coefficient return. Open and closed endpoint paths coexist at that return; the clock and retained histories do not reset. Every path still has bounded net displacement in the fixed tetrahedral carrier. All 24 frame relabellings and the two unchanged-seed automorphisms are checked.

Command: `uv run --with sympy python research/nima/checkers/check_photon_native_spatial_step.py`.
Report: `results/photon-native-spatial-step.json`.

## Full spatial placement at a phase return

`photon-spatial-phase-return.md` tests actual labelled triangle/body placements in the EXISTING 24-triangle area realization, not the earlier signed amplitude contrast. The global word (ABC)^3 returns all 24 frames exactly, with zero translation. Native three-step continuation has 26 paths, however, and is not that single global word.

The existing pointed-comparison constructor requires an actual supplied equivalence. Exhausting its compatible fibers gives 216 possible witness histories per three-step path, with six composite witnesses and two area-anchor positions. These are alternative source inputs, not probabilities. The bare two-packet records do not select them.

For the closed continuation B->C->A->B, the previously classified endpoint-swap policy yields holonomy (AC). Its area action sends B to -B and exchanges T with -T by a half-turn; repeating the loop returns. The other equivariant policy, swapping the two uninvolved labels as well, gives identity. Both keep the body centre fixed. Thus an endpoint-label return can hide a spatial body exchange, but neither result establishes translational propagation.

Command: `uv run --with sympy python research/nima/checkers/check_photon_spatial_phase_return.py`.
Report: `results/photon-spatial-phase-return.json`.

## Next executable gate

Native priority: extract or supply the actual comparison witness on each primitive continuation, including its spectator action, and check its compatibility with the retained phase evolution. If an intended spatial reader uses history beyond the composite S4 action, identify that existing reader and its input explicitly. Do not choose a transport policy to obtain the desired propagation, or invent a new space or drift vector.

Separate field-model branch: transmission loss and false source heralds remain to be quantified before apparatus-level performance claims. The ten-step conditional construction is documented, but seed-only physical production and apparatus realization have not been established.
