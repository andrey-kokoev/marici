# Autonomous contact scattering with a localized pentachoron intermediate

Date: 2026-10-11  
Status: A new, conditional one-dimensional contact reduction of the supplied phase-record model. Not a physical electron–positron scattering result.

## 1. Result and scope

The externally prescribed phase pulse has been replaced by a time-independent position–phase interaction. The original topology has an incoming/outgoing relative-motion coordinate. The connected ten-tetrahedron boundary is a localized intermediate, with all twenty native phase coordinates retained.

Within this reduction, incoming motion supplies internal excitation energy. Outgoing probabilities are normalized by their actual channel fluxes. The first excited outgoing native channel opens at kinetic energy sqrt(5) epsilon. Intermediate connected occupation is transient for an asymptotically prepared scattering packet; it is not a permanent-merging probability.

This is not a reintegration of the earlier D,delta collision trajectories. The calculation conditions on access to the full triangular ABE interface and freezes that geometry. Its continuum relative-motion law, localization, contact sampling, and incoming preparation are new declared choices. No relation to c, no measured energy, and no QED formula is inserted.

## 2. Inherited inputs and explicit changes

The unchanged `pentachoron_connected_phase_energy_bundle.zip` provides:

- H_O/epsilon = L_original + X and H_C/epsilon = L_connected + X;
- the rank-two matching projector P on twenty common raw occurrence coordinates;
- the positive topology gate 2 epsilon [[P,-P],[-P,P]];
- the resolved, face-paired ten-tetrahedron boundary with its retained occurrence and sewing records;
- the opposite-chirality, positive-trace fold convention at delta_c = atan(1/sqrt(5)).

The source script SHA256 is `575b9f9ba16fc028effa5c5f209b552da815d0b093a5e8e28544b3d6fd9807f3`.
The exact-matrix receipt SHA256 is `256b0a03239fb3e86053d8b905a8d5ed551a212484343fb24aacf3ec7fcbc1d5`.
Both are checked before reusing its matrices. The script does not claim to rerun every ancestral geometry checker.

The original repository ingredients, retained through that receipt, are the regular electron pentachoron, geometric chiral fold transports, the uniform positive defect-energy rule, and the additional five-cycle comparisons. The cycle comparison is not assumed to be a physical clock.

New choices made here:

1. Hold the full ABE contact pose and the resolved connected boundary geometry fixed during this local scattering calculation.
2. Supply one nonrelativistic continuum encounter coordinate x for the original topology, with contact at x=0. Its two asymptotic directions describe reflection/transmission along the reduced encounter channel.
3. Treat the connected boundary as a localized intermediate, rather than incorrectly extending its original two constituent centers to infinite separation while retaining their glued faces. Its centre-of-mass motion is factored out. No autonomous deformation of its glued metric is calculated.
4. Compare the continuum contact amplitude sqrt(ell) psi(0) with the finite connected record chi, using the same P and positive gate coefficient as the supplied model. Ell is a supplied contact-sampling length, taken as the existing geometric length unit.
5. Prepare an equal incoherent mixture of the four lowest native original record modes. This differs from the predecessor's localized relative-phase input. It is not a claim about an unpolarized two-particle beam.
6. For the numerical fixture, set hbar^2/(2 mu ell^2) = epsilon. This fixes one otherwise undetermined kinetic-to-phase scale for testing, not by fitting any outcome.

These are changes of model, not additional conclusions already present in the source note.

## 3. Joint Hilbert space and energy

Let

    H = [L2(R,dx) tensor C20]_O direct-sum [C20]_C,
    ||Psi||^2 = integral ||psi(x)||^2 dx + ||chi||^2.

This retains the predecessor's direct-sum phase-record interpretation. It is not the tensor-product Hilbert space of two independently prepared physical particles.

Write kappa = hbar^2/(2 mu). On an H1 continuum wavefunction and a finite core record, define the quadratic energy form

    E[psi,chi] = integral [kappa ||psi'(x)||^2 + psi(x)^dagger H_O psi(x)] dx
                 + chi^dagger H_C chi
                 + 2 epsilon ||P(sqrt(ell) psi(0) - chi)||^2.

The last term is the inherited positive matching gate with a dimensionally typed point-contact amplitude. Both diagonal terms and the off-diagonal transfer are retained. Dropping one diagonal term would change the energy reference and the model.

There is no prescribed chi_ABE(t), pulse duration, switch-on work, imaginary loss term, or separately supplied decay width. The state encounters the contact through its own position dynamics. Any residence-time scale follows from the chosen kinetic and phase coefficients.

Point evaluation is well-defined on H1 in one dimension. The positive finite contact form, together with the kinetic form, defines a lower-bounded self-adjoint point-contact Hamiltonian. In particular, the usual one-dimensional trace inequality controls ||psi(0)||^2 by kinetic and norm terms. This is not a claim that the same unregularized contact prescription works in arbitrary spatial dimension.

Since H is time-independent and self-adjoint, its exact evolution conserves both total norm and total energy. For this calculation, scattering-current conservation is checked directly, rather than inferred from a finite-time numerical norm check.

## 4. Boundary equations and scattering solution

Varying the form gives the free multichannel equation away from contact,

    -kappa psi'' + H_O psi = E psi,

continuity of psi at x=0, and the junction conditions

    kappa [psi'(0+) - psi'(0-)]
        = 2 epsilon sqrt(ell) P(sqrt(ell) psi(0) - chi),

    E chi = (H_C + 2 epsilon P) chi
            - 2 epsilon sqrt(ell) P psi(0).

Diagonalize H_O. For native energy e_n define

    k_n = sqrt((E-e_n)/kappa),
    v_n = 2 kappa k_n/hbar             for E>e_n.

When E<e_n, choose k_n=i sqrt((e_n-E)/kappa), so that the corresponding channel decays away from contact. Closed channels remain in the solve but carry no outgoing flux.

An incoming open channel is normalized by 1/sqrt(v_n), not by giving every different-speed plane wave the same amplitude. In units epsilon=ell=hbar=1, the forty-coordinate contact equations are

    [[2 i kappa K - 2P,    2P             ],
     [2P,                 E I-H_C-2P     ]] [psi(0),chi]^T
       = [2 i kappa K phi_in, 0]^T.

The matching projector and connected matrix here are expressed in the native original eigenbasis. K=diag(k_n). This block solve remains meaningful where a separate finite-core elimination would be singular.

For propagating channels, multiply the outgoing psi(0) by sqrt(v_n) to obtain the transmission matrix t. Continuity gives r=t-I. The two-direction scattering operator is

    S=[[r,t],[t,r]],       S^dagger S=I.

The reversed incidence convention is the same frozen local record convention. This algebraic identity is not a separate claim about physical parity or time-reversal symmetry of electrons.

An independent calculation eliminates chi, away from its finite-core poles. It gives the Hermitian, energy-dependent delta-interaction coefficient

    V_eff(E) = 2 epsilon ell P
               + 4 epsilon^2 ell P(E-H_C-2 epsilon P)^(-1)P.

Solving the remaining twenty-channel boundary equation reproduces the full forty-coordinate solution. The energy dependence is generated by the retained intermediate; it is not fitted independently at each energy.

## 5. Threshold and kinetic-energy exchange

The original native ground energy is

    e_0/epsilon = (11-2 sqrt(6)-sqrt(5))/2
                = 1.932476268466933... .

The first excited native level differs by

    Delta = sqrt(5) epsilon.

For an incoming ground-mode kinetic energy K_in and an outgoing native level e_n,

    K_out,n = K_in - (e_n-e_0).

A channel propagates only for K_out,n>0. Below that value it is evanescent, not an extra unnormalized outgoing probability. At the exact threshold, the flux-normalized formulas are read as one-sided limits.

Thus the new excitation threshold uses the existing phase spectrum. Its physical energy and velocity are still undetermined because epsilon, mu, and ell are uncalibrated.

Results for the illustrative kinetic choice and four-mode ground mixture:

| K_in/epsilon | Original topology, ground modes | Original topology, excited modes | Mean K_out/epsilon |
|---:|---:|---:|---:|
| 2.00 | 100.0000% | 0.0000% | 2.000000 |
| 2.30 | 88.1718% | 11.8282% | 2.035514 |
| 3.00 | 98.3141% | 1.6859% | 2.962301 |
| 4.00 | 88.0568% | 11.9432% | 3.732942 |

Both outgoing directions are summed in these columns. The two probability columns are exclusive and exhaustive asymptotic original-topology outcomes in this closed contact model. They must not be added to a transient connected occupation as though that were a third final channel.

At K_in=2.30 epsilon, only the first excited level is open beyond the ground sector. An excitation event leaves

    K_out = (2.30-sqrt(5)) epsilon = 0.0639320225... epsilon,
    v_out/v_in = sqrt((2.30-sqrt(5))/2.30) = 0.1667229184... .

The mean internal gain is 0.2644856871... epsilon, exactly balanced by the mean kinetic-energy reduction. The probabilities do not increase monotonically with incoming energy, because the coherent intermediate response is energy-dependent.

## 6. Temporary merging, residence, and bound states

For a unit-flux incoming mode, ||chi_E||^2 is a core residence time, not a probability of a permanently outgoing connected particle. It has dimensions of time. It can greatly exceed one in the chosen time units near a narrow resonance without violating probability conservation.

For example, in the fixture a local residence peak occurs near K_in=0.4253414 epsilon, with mean residence about 1131.9 hbar/epsilon. This is a numerically located narrow peak, not an exactly derived universal energy. The source's frozen-pulse transfer percentage does not specify this residence or a final branching fraction.

A normalized incoming packet was built directly from the exact scattering-continuum eigenfunctions:

    integral |a(E)|^2 dE=1,
    chi(t)=integral a(E) chi_E exp(-iEt/hbar) dE/sqrt(2 pi hbar).

The packet has mean incoming kinetic energy 2.30 epsilon and energy standard deviation 0.035 epsilon, in the same four-mode mixture. Energy quadrature was refined from 2048 to 4096 samples, with zero-padding only to sample time more finely.

At 4096 samples:

- Peak connected occupation is about 0.01403034 (1.4030%).
- Integrated connected residence is about 0.66745647 hbar/epsilon.
- Final excited outgoing probability is about 0.10837978 (10.8380%). This differs from the monochromatic 11.8282% because the packet averages over energy.
- At the ends of the displayed time window, connected probability is below 8.7e-13. This finite-window check is not the proof of asymptotic decay.

Parseval's identity checks the time integral of connected occupation against the stationary flux-normalized residence average. Direct Fourier quadrature checks selected points independently of the FFT.

For a prepared scattering-continuum packet, the core spectral amplitude is integrable on the tested packet support. Its Fourier transform tends to zero at large positive and negative time. This gives the asymptotic disappearance of localized connected occupation within this preparation.

The model also has two computed normalizable levels below the original continuum threshold:

| Level energy / epsilon | Binding below e_0 / epsilon |
|---:|---:|
| 1.867583991180 | 0.064892277287 |
| 1.867645839521 | 0.064830428946 |

These were obtained with the closed-channel Schur complement. Exterior wavefunctions decay as exp(-q_n |x|). Their junction equations, full normalization, and integrated form energies were checked. The energy-dependent subthreshold residual is strictly decreasing; its two negative directions at threshold produce these crossings in this fixture.

These bound levels do not imply capture of the incident scattering packet. A scattering-continuum input has zero projection onto them, and a time-independent Hamiltonian preserves that projection. Preparing a finite packet already overlapping a bound eigenstate is a different preparation, not evidence of capture from infinity.

Permanent formation therefore needs an admitted way for excess energy and information to leave in additional outgoing degrees of freedom, or another explicitly changed preparation/interaction. No absorbing term is introduced to force it here.

## 7. Verification and nonuniqueness controls

The checker records structural checks, a 501-energy scattering scan, narrower resonance tests, independent full-block and eliminated solves, and two wavepacket grids.

Representative residuals in the supplied run:

- Full S unitarity over the 501-energy scan: 1.21e-13 or less.
- Kinetic/native mean-energy balance on that scan: 3.47e-14 epsilon or less.
- Forty-coordinate versus twenty-coordinate solutions: 8.54e-15 or less.
- Unitarity at the selected much narrower residence peaks: 1.40e-12 or less.
- Packet-grid difference in peak connected probability: 1.51e-7.
- Packet-grid difference in final excited probability: 2.91e-7.

These are numerical verification residuals, not experimental uncertainties. The stationary self-adjoint boundary equations supply the analytical conservation argument.

Controls include zero matching gate (perfect transmission, no core occupation), all twenty closed/open phase modes retained, consistent retained-frame rephasing, native ground dark inputs, and explicit threshold opening.

The kinetic coefficient is not secretly fixed by the source. At the same K_in=2.30 epsilon, changing hbar^2/(2 mu ell^2 epsilon) from 0.5 to 1 to 2 gives excited probabilities about 12.1556%, 11.8282%, and 10.6347%, respectively. The native threshold remains sqrt(5) epsilon, but quantitative scattering depends on the supplied kinetic rule.

## 8. What remains open

This construction supplies an autonomous, flux-normalized local scattering model with a real energy exchange mechanism and a retained connected intermediate. It does not yet supply:

- the earlier speed-dependent route into triangular contact, compression, or dynamical internal rotation;
- a derived spatial kinetic coefficient, contact sampling prescription, or physical scale;
- outgoing two-/three-object recombination geometries;
- a complete two-particle tensor-product preparation;
- a relativistic or measured electron–positron scattering prediction.

The constructive next target is a geometric splitting route out of the connected boundary with its own outgoing motion and energy channels. That would permit a genuine conversion probability rather than mistaking temporary occupation for a stable product.

## 9. Reproduction

Unzip the bundle, keep its included predecessor archive beside the script, and run

    python pentachoron_autonomous_contact.py --packet-points 4096

Dependencies: NumPy, SciPy, SymPy. No network access is required. For a shorter stationary-only audit use `--skip-packet`.

The JSON receipt contains input hashes, all named checks, the scattering scan, threshold controls, kinetic controls, bound levels, and packet summaries. The NPZ files store the retained matrices and the numerical packet time/energy series. No repository file was modified.
