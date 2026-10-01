# Iteration 10: explicit photon vector and available-output contract

## Constructed vector and its conditional photon state

In the original two-packet order (AB,BC,CA,BA,AD,DB),

    v_lin=(1,-1,1/2,-1,1,-1/2)=(g_plus+g_minus)/2.

This is a vector on six two-endpoint packet records, not a pair of photons. With the declared seed-to-spacetime adapter it gives d=(sqrt(3),0,0). The conserved current is built from M^{0i}=d_i f, M^{i0}=-d_i f and j^mu=partial_nu M^{nu mu}.

For the Fourier-normalized, unit-width Gaussian envelope and normalized physical helicity polarizations, an explicit normalized outgoing one-photon state is

    |1_psi>=sum_h integral dmu(k) psi_h(k) a_h^dagger(k)|vac>,
    dmu(k)=d^3k/(2 omega), omega=|k_vec|,
    psi_h(k)=sqrt(6/pi)*(omega*epsilon_h,x(k)^*
                       -k_x*epsilon_h,0(k)^*)*exp(-omega^2).

A common phase is immaterial. In radiation gauge epsilon_h,0=0, the formula reduces to sqrt(6/pi)*omega*epsilon_h,x^* exp(-omega^2). The full expression is unchanged under epsilon_h -> epsilon_h+beta*k. Its normalization follows from the checked current radiation norm N_source=pi/2. Thus

    <1_psi|1_psi>=1, N_gamma|1_psi>=|1_psi>.

This profile is a NEW broad-spectrum radiation profile, not the compact momentum top-hat excluded by the compact-source audit. Quantization, spacetime, physical units and the source envelope remain declared assumptions.

## Three distinct production/readout claims

### 1. Source-only herald: high fidelity, not exact photon number

The real-current degenerate-qubit model gives the exact outgoing state and odd coherent herald described in `photon-coherent-herald.md`. At mu=1/10:

    P_source_flip in [9/100,1/10],
    1-F_1 <= 10/6007 < 0.002.

There is nonzero three-photon weight for every positive mu. A source-only herald is not an exact number-one certificate.

### 2. Additional ideal nondemolition number measurement: exact conditional output

Declare the EXTRA two-outcome Lüders instrument

    K_yes=Pi_1, K_no=I-Pi_1,

where Pi_1 projects onto total field photon number one. This is a mathematical measurement assumption, not a detector derived from the packet data or a demonstrated local apparatus.

For the complete driven output S|e,0>,

    (I_source tensor Pi_1)S|e,0>
       = common_phase*sqrt(mu)*exp(-mu/2)|g>|1_psi>.

The accepted field is exactly the normalized wavepacket above. The JOINT success probability is

    P_exact=mu*exp(-mu).

There is no extra multiplication by the source-herald probability: the one-photon component already has the source in |g>. At mu=1/10,

    9/100 <= P_exact <= 1/11.

This is conditional, not deterministic production. Over all mu, mu*exp(-mu) has its maximum 1/e at mu=1; inserting a number filter does not establish the earlier engineered pi/2 transfer law for this local-current control.

The instrument must preserve the photon AND the mode coherence. Resolving frequency/polarization and then discarding the result need not preserve |1_psi>. It must also refer to the total relevant field: finding one photon in a monitored mode does not exclude photons in unmonitored modes. Tests include an extra-mode counterexample. No finite-band/finite-apparatus realization of the total-continuum-number projector is claimed.

### 3. An absorbing one-photon count: same event probability, no remaining photon

In a two-mode fixture, an ideal absorbing one-count operation has Kraus operators

    L_h=|vac><1_h|,
    sum_h L_h^dagger L_h=Pi_1.

It has exactly the SAME one-count event probability as the nondemolition instrument, but its accepted output is vacuum. The detector/environment branches are added incoherently; coherently adding their amplitudes gives a wrong instrument.

This is why a matching measurement probability or a detected photon does not itself certify an available output photon.

## A tap-click is not a substitute for the number-QND assumption

For a lossless beamsplitter with real amplitudes t,r, t^2+r^2=1, exactly one photon absorbed in the reflected arm has transmitted-field Kraus operators

    T_h=r*t^N*a_h.

The number operator acts after annihilation. For an n-photon input the one-reflected-count probability is n*r^2*t^(2(n-1)). A one-photon input leaves transmitted vacuum after that click.

More strongly, an odd-photon source-heralded input followed by an EXACTLY ONE reflected count leaves only even transmitted photon numbers: 0,2,4,... . It cannot be called an exactly-one-photon output. This particular conclusion assumes number-resolved one-count detection; a threshold click has additional branches and also does not certify a single surviving photon.

## What is and is not complete

The work now supplies:

- an explicit vector on the retained two-packet records;
- a conditional Maxwell/Fock one-photon state with an explicit normalized profile;
- an exact engineered global-transfer model, kept separate from local-current dynamics;
- conserved local source alternatives and an obstruction to the old top-hat;
- a driven quantum-current control with exact all-orders photon statistics;
- a certified high-fidelity source herald;
- an exact conditional available-photon route ONLY after an additional ideal number-QND assumption;
- checks rejecting absorbing detectors and tap clicks as substitutes for that assumption.

It does NOT derive spacetime, field quantization, electromagnetic coupling, an autonomous energy reservoir, source recoil, or an actual readout/detector apparatus from seed incidence data. The source in the soluble local-current control is degenerate; external control supplies radiated energy. The positive-gap circular-source all-orders continuum dynamics remain open.

Consequently, “a conditional photon-producing construction has been specified” is supported. “The packet algebra alone produces physical photons” and “an exact available-photon apparatus has been built” are not supported.

## Verification

    python research/nima/checkers/check_photon_output_contract.py

This freshly reruns the full prior chain and checks projector completeness/idempotence, retained one-sector coherence, equal counting effects with different output states, incoherent Kraus summation, total-number controls, tap-count probabilities and rejection of unsupported exact-output claims. Finite-mode checks audit universal operator identities; the continuum measurement contract is an additional mathematical assumption.

Implementation: `checkers/photon_output_contract.py`.
Report: `results/photon-output-contract.json`.

## Nonredundant continuation

Quantify transmission loss and false source heralds. An ideal number-QND event followed by loss need not leave one photon, and a false source herald can reintroduce vacuum. Detector/readout tolerance requirements must be specified before translating ideal-model fidelity into an apparatus-level claim.
