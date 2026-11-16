# Neutron record-controlled rim exchange and healthy-state test

Continuation date: 2026-11-01. Status: exact algebraic and numerical audit of specified models, not a physical neutron-decay derivation.

## Findings

1. The complete real linear span of the source's eighteen rim–bank exchange projectors was tested. Requiring an added generator to fix the original coherent neutron leaves an eight-dimensional coefficient family. Every member also annihilates both collective rim columns. With the existing static invariant-subspace structure, none can release the previously dark sector contrast. Nonnegative sums satisfying the healthy-state condition are all zero.

2. A separate, explicitly added coherent comparison controller can condition a source exchange on sector disagreement. Its binary flag stays zero on the intact preparation and on every uniform-loss completion. Its work register can be uncomputed without resolving the two nontrivial rotation characters. All 36 input omissions against all six addresses were tested.

3. A supplied local-input omission is not an orthogonally distinguishable classical event in the existing amplitude record. The healthy/fault overlap is 1-r/3. A deterministic perfect failure flag cannot be extracted from these amplitudes alone. Requiring zero false triggers for all uniform-loss states gives the exact upper bound 4r/9 for a single-sector loss. The coherent controller attains that bound, but choosing maximal sensitivity is a declared policy, not a source-derived physical coupling.

4. Under the unchanged illustrative always-open contact, the pristine **bare** coherent core preparation has continuum spectral weight 0.22022050248191013. A no-fault pulse flag does not eliminate that background. The result concerns this prepared model state, not a prediction that measured neutrons radiate that fraction. A stationary dressed preparation would be a different initial state requiring a new binding to the local reconstruction protocol.

## Inputs and what was actually reconstructed

The attached `neutron_native_rim_escape_audit.zip` supplies the pure source-formula `geometry()` reconstruction, the exact two-parity contact response, and the source invariant-subspace argument. The present scripts import only its pure geometry function and independently reconstruct the relevant rational contact functions. No upstream repository producer, proof-assistant suite or generated source receipt was rerun. No repository file was modified.

Fresh read-only GitHub reads:

- [Neutron canonical rotation frame](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/neutron-canonical-rotation-frame.md).
- [Canonical record binding checker](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/checkers/check_neutron_canonical_record_binding.py).
- [Source-pulse particle intertwiners checker](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/checkers/check_source_pulse_particle_intertwiners.py).

The source states explicitly that its three-valued moving frame is a discrete control record, that its pulse schedule is supplied, and that no autonomous controller or physical clock is derived. Having a classical address label does not automatically provide coherent controlled rotations on a new quantum register.

The two-rim outgoing model and its parameters are inherited from the prior attached audit: kinetic coefficient 1, positive contact strength 2, length 1, both lead thresholds 1/2, and action unit 1. These are model inputs, not fits to neutron measurements.

## A. Entire native-generator family, not a sampled schedule

Let f_a, a=0,...,5, be the six orthonormal native rim modes. Let b_i be the six normalized source-bank features. They are independent but not mutually orthogonal. In a convenient interleaved ordering the labels are AB, BC, CA, BA, AD, DB. Native rotation cycles the two rims as (AB CA AD) and (BC BA DB).

The source bank metric is retained exactly. With G=10I_4+J_4 and label i=(i_1,i_2),

    D_ij = G_(i_1,j_1) G_(i_2,j_2) / 121.

Its rank is six. The calculation does not replace this Gram matrix with identity. The twelve-dimensional active coordinate metric is diag(I_6,D); all other original neutron and bank directions remain spectators for this family.

At source frame t=0,1,2 the existing projector is

    d_(i,t) = f_(pi^t(i)) - b_i,
    P_(i,t) = d_(i,t) d_(i,t)^sharp / 2.

The proposed autonomous family is

    H_mix = sum_(i,t) h_(i,t) P_(i,t),       h_(i,t) real.

All eighteen projectors have the same nonzero overlap with the healthy coherent neutron u. Its rim amplitudes equal sqrt(rho/3), where rho=2099/8970. Consequently H_mix u=0 is exactly the balance equation

    sum_(i,t) h_(i,t) d_(i,t)=0.

The 12-by-18 direction matrix has rank ten and nullity eight. An exact rational nullspace is retained in `autonomous_generator_results.json`.

Each of the two rims contributes a complete three-by-three bipartite incidence pattern between rim sites and bank features. The balance equation requires every rim row sum and every bank column sum to vanish. In a balanced combination, the native diagonal and bank diagonal blocks cancel. Its remaining off-diagonal block has zero sum over the three sites of each rim. Thus, for the collective columns

    W_h = (f_(h,0)+f_(h,1)+f_(h,2))/sqrt(3),

one has, for every allowed H_mix,

    H_mix W = 0,       W^sharp H_mix = 0.

This is checked on all eight exact basis generators; linearity establishes it for the entire family. The result is independent of any numerical energy threshold or stochastic rate.

### Why this also excludes delayed escape in this family

The source's static core preserves the six-dimensional aligned triangle subspace A and its metric-orthogonal complement, and its leads attach only through W contained in A. The balanced generators act only on rim/bank directions and annihilate all of A: within A each rim has equal amplitudes at its three sites. They therefore preserve the original dark complement as well. Adding such a generator to that static model cannot make a sector-contrast input reach the leads.

The same invariant-subspace argument covers time-dependent balanced combinations if the healthy-state condition holds at each instant. It does **not** cover arbitrary switching through generators that disturb the healthy state and restore it only later, nonlinear laws, additional coherent controller interactions, modified contacts or different stationary preparations.

If every h_(i,t) is nonnegative, positivity gives a stronger statement: each primitive has healthy-state expectation 2099/53820, so H_mix u=0 forces all coefficients to vanish. Allowing signs yields the eight-dimensional family but does not cure the escape obstruction.

The actual u has nonzero support outside the rim modes. Thus requiring H_mix u=epsilon u forces epsilon=0, since this mixer vanishes on those spectators. Adding an overall identity energy shift does not change the conclusion.

## B. A coherent comparison flag: constructive, but additional control

The local selected data are three amplitudes x. A specified omission produces the completed state

    Psi = (V T x) direct-sum (D x),
    T=diag(1-r_s),
    D=diag(sqrt(r_s(2-r_s))),
    T^dagger T + D^dagger D=I_3.

V embeds the three sector modes in the 36 native coordinates. The completion record is not automatically the native source bank. It is retained separately in the present test.

On native coordinates, the source rotation R cycles the three sectors. Let it cycle the completion coordinates in the same way and leave the addressed bank feature fixed. Define

    P0=(I+R+R^2)/3,
    Pc=I-P0.

On the selected six-dimensional completed input, P0 has rank two and Pc rank four. P0 retains the sector averages of both data and completion record. Pc retains both disagreements.

Append a ready bit |0>. The coherent flag operation is

    S = P0 tensor I_bit + Pc tensor X_bit.

It is a self-adjoint unitary. In particular,

    S(Psi tensor |0>) = P0 Psi tensor |0> + Pc Psi tensor |1>.

No measurement, threshold on a floating norm, ad hoc renormalization, or classical declaration that a failure occurred is used.

### Finite implementation and its authority boundary

A three-state Fourier transform and coherent controlled applications of I,R,R^2 compute the rotation character into a work qutrit. Flip the output bit for either nontrivial character; then uncompute the work qutrit. The exact projector identity and a 36-dimensional circuit check establish that the work register returns to its blank state while preserving coherence between the two nontrivial characters.

Coherent controlled rotations, blank auxiliary preparation and the comparison-to-pulse coupling are **additional control capabilities**. The source's available R and its supplied classical moving frame do not alone prove these capabilities are physically implemented. The construction is a precise candidate operation for that missing contract, not a claim to have discovered its autonomous execution.

## C. Exact trigger limit

For x=a=(1,1,1)/sqrt(3), one omitted input of weight r in sector s gives

    <Psi_healthy,Psi_(s,r)> = 1-r/3.

This is nonzero for the inherited weights. A deterministic device cannot map the healthy and all these faulty preparations to perfectly distinct flags: an isometry preserves their overlap. This statement concerns the given amplitude records. A separately supplied orthogonal classical fault-history record would change the available input and the conclusion.

Requiring no trigger on **every uniformly attenuated completed preparation** means that the positive trigger effect F annihilates span{(a,0),(0,a)}. Positivity and 0<=F<=I imply

    0 <= F <= Pc.

For the single-sector omission,

    ||Pc Psi||^2 = 2r^2/9 + 2r(2-r)/9 = 4r/9.

The coherent comparison flag saturates this upper bound. The native-data part has weight 2r^2/9; the completion-record part has weight 2r(2-r)/9. The source rim exchange currently acts only on the former. Treating the whole flag weight as outgoing rim flux would double-count an unimplemented record-to-bank binding.

The four inherited weights give trigger weights from 148/40365 to 30/299, approximately 0.00366654 to 0.10033445. These are conditional squared norms after a prescribed omission, not a frequency of omissions or a physical lifetime. A weaker positive effect also satisfies the no-false-trigger condition. Attaining the upper bound is a chosen detector policy, not a derivation of a unique physical strength.

The three sector-address contrast states at fixed r are trine states: each normalized pair has inner product -1/2 and their sum is zero. No exact unambiguous sector label can be inferred solely from these contrasts: a detector vanishing on either pair of other sectors also vanishes on the entire two-dimensional contrast plane. The source address must not silently be set equal to the unknown failed sector.

Primary background: [Bergou, Herzog and Hillery, Optimal unambiguous filtering of a quantum state](https://arxiv.org/abs/quant-ph/0504138). The concrete projectors, bound and address calculation here are derived from the stated Marici trial data, not taken from that paper.

## D. Conditioned existing exchange, with all amplitudes retained

For each of the six possible supplied addresses, use the unchanged source exchange E_h,t at pulse area pi. The conditional gate applies identity in flag zero and E_h,t in flag one. Only one addressed bank direction is active in each experiment; using a one-mode bank representation here is exact for this single pulse from an empty bank, not for arbitrary multi-pulse histories.

The data space has 36 native coordinates, one source-bank direction and three completion-record coordinates. With the binary controller it has dimension eighty. The full comparison-plus-controlled-exchange is unitary and its inverse exactly recovers the prepared input.

In flag one the native input is the original contrast c; the common neutron component is in flag zero. Thus the earlier contrast escape calculation can now be counted within an explicitly orthogonal branch, without silently adding interfering common and contrast probabilities.

For failure sector s, supplied rim sector t and input weight r,

    flagged bright norm = rho r^2 (3 delta_(s,t)-1)^2 / 81,
    flagged escaping norm = chi_escape times flagged bright norm,
    chi_escape = 0.780828766716157897...

The previous four-to-one ratio is preserved. Every one of the 216 fault/address combinations was checked. There is no automatic identification of t with s.

### Additional control: retaining too much measurement information changes the answer

If a permanent record instead distinguishes the two nontrivial rotation characters, their outgoing amplitudes cannot interfere after that register is ignored. The bright norm becomes

    2 rho r^2 / 81,

independent of the supplied sector address. Both implementations have zero false triggers and the same total trigger weight. Their escape differs because their record back-action differs. The coarse binary construction uncomputes the character register and therefore retains the original contrast interference. The source must select a specific record operation, not merely an abstract yes/no predicate.

## E. Healthy preparation under the always-open contact

Controlling the added pulse is not sufficient to make the whole old model an unstable-particle model. Even when the flag is zero, its original two-rim contact remains open and observes u.

For the exact source even-channel bare-core resolvent,

    g_+(z) = (z-2099/3292)/(z(z-4485/3292)),

the zero-energy pole corresponds to the normalized bare common state u and has rim weight 2rho. At the inherited contact parameters the even bound state has

    E_b = 0.23956486709177237258...,
    Z_rim = 0.20938777629259723386....

The bound overlap of the *bare common core preparation* is

    Z_u = Z_rim (2rho)/(E_b^2 g_+(E_b)^2)
        = 0.77977949751808986947... .

Its remaining continuum weight is

    1-Z_u = 0.22022050248191013053... .

An independent integration of the common-state continuum spectral density reproduces this weight. The odd bound state has zero overlap with this even input. This is a mathematical spectral decomposition of a supplied bare preparation and illustrative contact, not a neutron radiation measurement or a probability per Planck tick.

A bound dressed eigenstate would not disperse under the unchanged autonomous contact. Replacing u by such a state is a substantive new preparation: it includes a continuum tail and a changed core, and its compatibility with the local L/G reconstruction must be checked rather than assumed. Alternatively a physically derived conditional contact could close the healthy channel, but simply adding that gate would be another assumption.

## Conclusion

The completed missing-input record can support a well-defined coherent comparison flag. That flag can condition the existing addressed exchange without false triggers on the specified symmetric controls. This closes a conditional circuit construction, not the source's autonomous-control or physical-production problem.

The exact full-span test rules out one proposed shortcut: an always-on linear combination of the retained exchange generators cannot both preserve u and release the dark contrast. Independently, the bare u plus the always-open continuum contact already has an outgoing background. A viable next source construction must specify a stationary occupied preparation and its comparison-controlled interaction with the exit field. It must also supply the joint particle-production and occupation-replacement law. No error rate, pulse duration, neutron mass, weak coupling, Planck tick or measured lifetime was fitted here.

## Verification and reproduction

Run:

    python autonomous_generator_probe.py
    python coherent_trigger_probe.py

Dependencies: NumPy, SymPy, SciPy and mpmath. Exact rational computation establishes the source Gram matrix, generator constraints, eight-dimensional nullspace and dark-coupling identities. Analytic projection and overlap proofs establish the trigger bounds. Floating complex-matrix checks implement the controller and all finite fault/address controls; the largest observed residual is below 1.9e-15. Continuum integration is numerical, with its estimated quadrature error retained; high-precision printed digits are not interval certification.

Outputs:

- `autonomous_generator_results.json`: exact source-family classification.
- `coherent_trigger_results.json`: controller, probability-bound and spectral checks.
- `controlled_fault_address_census.json`: all 216 cases, with exact rational input and bright weights.
- `run.log`: completed executions.

The included `prior/` files are copied unchanged from the attached earlier audit and carry their inherited reconstruction limitations. New script hashes and the imported geometry hash are recorded. No live repository dependency hash or full producer replay is claimed.
