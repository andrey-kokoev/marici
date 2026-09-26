# Source instantiation: restore external legs before interpreting contact responses

## Fresh primary read

Read `GeomCosmoCorr.tex` lines730–811, especially eq:CC3, eq:CG and eq:CGrules, and ledger2159's component-factorization identity. The primary source distinguishes the normalized physical correlator from its stripped graph coefficient:

    <product_j Phi(p_j)> = L_ext <product_j Phi(p_j)>',
    L_ext=product_j K(E_j), K(E)=1/(2 Re psi_2(E)).

The graph/deletion rules operate on the primed correlator. Removing external legs is NOT the normalization by integral |Psi|^2. The latter was already part of the derivation of the normalized expectation. Do not apply the universal vacuum-normalization recurrence a second time to a graph coefficient merely because it is primed.

This is a source-specified comparison, rather than a new toy observable.

## Actual retained contact packet

Ledger2158/2159/2174 retains, for each channel,

    A=4P_jk*(2q_jk/y_jk), B=-8C_j C_k,
    C_j C_k/P_jk=q_jk/y_jk.

Thus A=8C and B=-8C with C=C_j C_k, retaining the spectator P_jk until the source identity is used. At fixed baseline kinematics and source coefficients, varying the erased-edge covariance multipliers gives the primed contact family

    F'(g)=8C g_j g_k(1-g_i).

The corresponding contribution to the physical correlator is L_ext(g) F'(g), provided the source contact grade commutes with multiplication by this external factor. This is automatic for a regular scalar factor independent of the selected normal; if it has normal dependence, the requisite lower jets must be retained. A pole or zero on the grade face needs its own shifted-filtration treatment.

Neither this formula nor the prior coefficient identities identify a fixed uncontracted Gaussian L2 operator. The present instantiation is at the contracted graph/readout level.

## First susceptibility is protected by the contact zero

For a covariance tangent D, write alpha=D log L_ext. Then

    D(L_ext F')=L_ext(D F'+alpha F').

At the baseline contact cancellation F'=0, the external-variation term vanishes:

    D_i F_phys=-8 L_ext C.

Thus varying a common covariance function at an external energy does not by itself add a background to this first response at the contact zero. This does not remove internal occurrence collisions, variation of other wavefunction coefficients, or raw non-contact backgrounds. The source coefficient deformation and contact projection must still be specified.

## Higher responses retain an external-leg connection

For a repeated covariance derivative,

    D^2(L_ext F')=L_ext[D^2 F'+2alpha D F'
                               +(D alpha+alpha^2)F'].

At F'=0, the cross term2alpha D F' remains. Test a covariance multiplier shared by the selected internal edge and m external legs, with other multipliers fixed:

    L_ext=L0*g^m, F'=8C(1-g), D=g*d/dg.

At g1,

    D F_phys=-8L0 C,
    D^2 F_phys=-8L0 C(2m+1).

Ignoring external legs therefore gives the wrong higher response when m!=0. The source-defined covariant derivative

    nabla=D-alpha

satisfies nabla(L_ext f)=L_ext Df and transports the full response jet. On a nonvanishing scalar chamber the multi-parameter connection is d-d log L_ext and is flat. This is exact comparison coherence, not a statement that its inverse is bounded at external-energy boundaries.

Repeated Gaussian score insertions also require the derivative-of-score terms; the formula is for source family derivatives, not an identification of D^2 with multiplication by a fixed score squared.

## Completion and operator gates

Physical contact-response magnitudes contain L_ext C, not C alone. If L_ext or its inverse degenerates, previously normalized finite-packet bounds cannot be imported unchanged. Physical source relations among contact energies and external momenta must decide that behavior; L_ext is not a freely adjustable compensating scale.

The source specifies the contracted contact map and its external-leg comparison. The still-missing operator-level input is the selected perturbative/contact extraction before contraction, with its norms. The existing operator-lift handoff remains open.

Next evaluate the actual source relation between contact-infinity coordinates, external momenta and L_ext. Classify zeros/poles and retain the resulting physical asymptotic degree before seeking a completion theorem. This keeps the source comparison and physical selection distinct from a convenient normalized Gaussian model.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_contact_external_legs.py` checks the source component identity, all cyclic first contact derivatives, external-factor cancellation at the scalar zero, higher-response corrections and covariant transport through third order for m0–4. Primary inputs are hashed and remain unchanged. The checker does not prove contact-grade regularity or a Hilbert-space operator lift.
