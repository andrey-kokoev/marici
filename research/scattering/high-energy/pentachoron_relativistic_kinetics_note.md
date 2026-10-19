# Fixed-geometry square-root separation kinetics

Date: 2026-10-11  
Status: Conditional semirelativistic extension of the supplied geometric-entrance phase-record model. **Not physical electron–positron scattering, Lorentz contraction, or a Lorentz-covariant theory.**

## 1. Result

Changing the incoming/original separation kinetic law, while holding the geometric comparison potential, ABE contact patch, sampling rule, native phase operators, face-switch graph, memory, and output couplings fixed, changes the outgoing 2+8 phase-record flux. It suppresses conversion at two tested energies and enhances it at two higher tested energies. The response remains nonmonotonic.

The calculation implements the nonlocal square-root operator through its free spectral resolvent. It does **not** obtain a purported relativistic result by replacing a wave number in the old local second-order boundary equation. The nonrelativistic version of the new integral solver independently approaches the predecessor's finite-difference results.

The existing contact geometry and asymptotic internal/rotor threshold energies stay unchanged. This isolates a kinetic contribution to amplitude changes. It provides neither evidence for speed-induced flattening nor a determination of the relativistic energy scale.

## 2. Retained source and new assumptions

The unchanged supplied `pentachoron_geometric_entrance_bundle.zip` was extracted under `inputs/geometric_source/`. Its 25-file SHA256 manifest is checked. The retained open-product code additionally verifies its compact native, hinge, exit, and geometry payloads. This is not a rerun of every ancestral checker or of any experimental correspondence.

Source quantities retained:

- The regular pentachoron geometry, nearest-nonoverlapping correction cost, and exact marked ABE-active patch.
- Original phase operator H_O, connected operator H_C, rank-two matching projector P, native cycles and fold conventions.
- Periodic material tilt, its kinetic coefficient, and the quantum connected hinge with both geometric endpoints.
- Eight pairing configurations at each endpoint, full-spinor face-switch gates, memory encoder, and outgoing 2+8 record operators.
- All inherited positive comparison coefficients and the common energy reference.
- The source's four-ground-mode mixture and incident angular **flux** coefficients (1/4,1,3/2,1,1/4), on n=-2,-1,0,1,2, with phases specified at D=4 ell.

New physical/model input: change only the original radial/separation kinetic energy to

    T_D(p) = 2 [sqrt(m² c⁴ + c² p²) - m c²].

Here p is conjugate to separation; the two equal mass parameters carry opposite momenta in the selected center-of-mass description. The kinetic expansion starts at p²/m, matching the source. The mass m remains the source's uncalibrated inertial parameter, not an independently established electron mass.

The inserted velocity parameter c and ratio

    rho = m c² / epsilon

are not derived from configurations or arrow counts. The principal example sets rho=1 as a declared test. The rotor, connected hinge, and output motion are left nonrelativistic to isolate the effect of **approach/separation** kinetics. Native internal energies remain additive. This is not a complete relativistic treatment of composite objects or the state-dependent rest masses of their products.

The radial kinetic operator is the spectral function of the source's nonnegative Neumann half-line Laplacian. That specifies the nonlocal boundary convention; it is not an independent local derivative condition for the interacting square-root equation.

A relevant outside mathematical comparison is the square-root kinetic-plus-static-potential class reviewed by Lucha and Schöberl, *Spinless Salpeter Equation: Analytic Results*, arXiv:hep-ph/9807342, and Hall, Lucha and Schöberl, *Discrete Spectra of Semirelativistic Hamiltonians*, arXiv:hep-th/0210149. Only this operator distinction is used. No QED interaction, propagator, charge, experimental branching fraction, or fitted collision energy is imported.

## 3. Dispersion, speed and unchanged channel thresholds

Keep the source units epsilon=hbar=m=ell=1. Then

    T_rho(k) = 2 rho [sqrt(1+k²/rho)-1],
    T_infinity(k) = k².

For radial energy z>0,

    k(z) = sqrt[z + z²/(4rho)],
    v_D(z) = dT/dk = 2k/[1+z/(2rho)].

The individual counterpropagating mass parameters have speed v_D/2. Thus

    beta(z) = (v_D/2)/c = sqrt[1-(1+z/(2rho))^(-2)] < 1.

The separation-coordinate speed can approach 2c without either body having speed greater than c. It is not a relativistic relative velocity measured in either body's rest frame.

The original asymptotic channel energy is e_j + 5 n²/32. At total energy E, z=E-e_j-5 n²/32. Because T_rho is nonnegative, vanishes at zero momentum, and has unbounded range, the same channels are open (z>0) for all rho. Their momenta, velocities, normalization, and virtual propagation differ.

For the tested rho=1 preparation, the different occupied rotor modes have different radial speeds:

| Total incoming motional K/epsilon | Range of individual beta across the prepared rotor modes |
|---:|---:|
| 1 | 0.5393–0.7454 |
| 2.3 | 0.8389–0.8852 |
| 4 | 0.9282–0.9428 |
| 6 | 0.9625–0.9682 |

These are consequences of the **assumed** rho and dispersion, not calibrated electron beam speeds. K includes radial and tilt kinetic energy, as in the source. The prepared superposition cannot be assigned one common radial velocity.

## 4. A genuinely nonlocal entrance calculation

Let A_N be the nonnegative Neumann half-line Laplacian. The continuum entrance energy becomes

    H_ent = T_rho(sqrt(A_N)) + T_tilt + H_O + V_geometry.

The notation expresses the spectral multiplier T_rho(k); it is not a square root of the full interacting Hamiltonian. In particular V_geometry stays outside the square root, and the entire source Hamiltonian is not spectrally reparameterized.

The area-supported entrance comparison remains

    2 epsilon integral_Omega ||P Psi(D,y) - f sqrt(ell) P chi(0)||² dD dy,
    f = 1/sqrt(|Omega|),
    |Omega| = 1.521810286455744 ell².

All its diagonal and off-diagonal terms remain. Original-to-hinge contact is area-supported, not a newly introduced point trace on a half-order radial domain. The entrance potential and patch multiplication are bounded, its area sample is bounded in L2, and the hinge trace is controlled by its existing H1 kinetic form. Together with the positive source downstream forms, this supplies a lower-bounded closed form and a self-adjoint, time-independent model. Norm and total energy are conserved.

For each asymptotic native/rotor channel, the retarded free kernel is

    G_z(D,D') = (2/pi) integral_0^infinity
        cos(kD) cos(kD') / [z-T_rho(k)+i0] dk.

The numerical method integrates this against normalized radial-cell form factors, not point evaluations. For cell width h and center x_i,

    C_i(k) = sqrt(h) sinc(kh/2) cos(k x_i).

The projected resolvent is (2/pi) integral C_i C_j/[z-T+i0] dk. The sinc factors make the high-momentum cell integrals converge. A finite cell grid is numerical approximation, not a new physical tolerance.

### Pole extraction and the retained nonlocal correction

For z>-2rho set u=sqrt(rho)+z/(2sqrt(rho)) and k0²=z+z²/(4rho). Exactly,

    1/[z-T_rho(k)] = (1+z/(2rho))/(k0²-k²)
                    -1/[2sqrt(rho)(sqrt(k²+rho)+u)].

The first term is integrated analytically using the Neumann resolvent, with its outgoing pole. The second real term is also retained and evaluated by cosine quadrature. Omitting it would not implement the proposed kinetic operator.

For z<=-2rho, the entire closed-channel multiplier is integrated directly. This avoids the spurious poles of an inappropriate rationalized continuation. Closed modes remain in the solve and carry no asymptotic flux.

The continuum free optical identity after cell projection is

    Im G_z = -(1/2) F_z F_z^dagger,

where the columns of F_z contain the standing-wave factors 2 C_i(k)/sqrt(v_D). This identity is checked, as is the full multichannel scattering matrix.

## 5. Numerical reduction without deleting phase modes

The scalar geometric potential commutes with H_O. Its five distinct native energy levels permit five scalar radial/rotor resolvent solves. The rank-two matching projector couples those solutions only in the geometric patch. A Schur complement then connects them to the **unchanged** full hinge, pairing, memory, and product solve. All twenty original native coordinates and closed modes are retained; dark components are not discarded.

Radial cells use a finite interaction support 0<=D<=4ell, outside which the source scalar potential is zero. The exterior remains the infinite spectral half-line, not a reflecting box. The rotor uses a Fourier grid with exact truncated n² kinetic energies. The scalar potential is midpoint sampled and the exact curved patch is integrated over each cell. This is a different conservative numerical approximation from the source's finite-difference entrance, converging toward the same nonrelativistic continuum model.

The source's finite-element hinge with 320 intervals is retained for the principal results. The exterior product logarithmic derivatives and flux factors remain those of the unchanged output kinetics.

## 6. Computed fixed-geometry comparison

Each row uses the same incident angular flux coefficients and the same four-mode native mixture at E=e0+K, e0=(11-2sqrt(6)-sqrt(5))/2 epsilon. Only the separation law changes between columns.

| K/epsilon | Nonrelativistic separation: total product flux | Square-root separation, rho=1: total product flux |
|---:|---:|---:|
| 1.0 | 0.00369980% | 0.00323905% |
| 2.3 | 0.0321087% | 0.0289191% |
| 4.0 | 3.38758% | 3.58386% |
| 6.0 | 0.883339% | 1.01795% |

The first two rows use 40 radial cells, 48 rotor nodes and 320 hinge intervals. The last two use 48 radial cells, 64 rotor nodes and 320 hinge intervals. Appropriate public summaries are 0.0037 versus 0.0032 percent, 0.032 versus 0.029 percent, 3.4 versus 3.6 percent, and 0.88 versus 1.0 percent.

Both symmetry-related 2+8 product exits are summed. The remainder is original-channel outgoing flux. These are stationary record-channel fractions, not rare-branch renormalizations or multiplication of separate stage probabilities. No product is identified as a photon or independently occupied physical particle.

At K=4 and rho=1, one mean energy ledger is

    E_in/epsilon = 1.932476268466933 + 4,
    E_out/epsilon = 2.576681589593752 + 3.355794678873187.

The first output term includes native/memory energies and original-channel tilt energies; the second is the actual outgoing radial kinetic energy under the law used for each lead. Their sum agrees with the common total energy. This bookkeeping is not by itself the proof of conservation; the autonomous self-adjoint model and current identity provide that argument.

The graph, patch and all couplings are unchanged. The differences are therefore a kinetic effect in this admitted model, not activation of extra geometric arrows. Four samples do not establish the complete curve or a global resonance.

## 7. Verification actually performed

The final verification receipt records 24 passing grouped checks. These include:

- All 25 retained-source manifest hashes and the inherited native payload checks.
- Algebraic low-momentum expansion, dispersion inversion with the positive-root condition, and the exact pole/correction identity.
- Correct open thresholds and sub-c individual group velocities.
- Direct principal-value spectral quadrature independent of the analytic-cell/DCT method, on open and closed channels. The largest element difference is about 4.73e-8 at the stated finite cutoffs.
- Positivity of the projected comparison and preservation of the analytical patch area.
- Complete entrance/product S matrices at every recorded comparison energy, not only four selected preparation columns. Maximum unitarity residual over the principal and refined runs is below 3.6e-13.
- Coupled scattering approaching the nonrelativistic result when rho is increased, and agreement with the predecessor's largest-energy nonrelativistic fractions within 1.6e-5 absolute probability.
- Zero entrance and zero subsequent face-switch controls, each giving zero product flux.
- Momentum-integral cutoff/step refinement: product-probability change around 1.13e-9 on the tested control grid.
- Spatial refinement through 12x16, 24x32, 40x48, and (for the two larger energies) 48x64 entrance grids. The last largest-energy product change is about 1.01e-4 absolute probability, or 0.0101 percentage points.

These errors are numerical diagnostics, not experimental uncertainties. Spatial convergence is much weaker than algebraic flux conservation; they must not be conflated. There is no claim of a 501-energy scan in this extension.

The first verification receipt is retained as `verification_initial.json`. A symbolic equality query did not simplify the dispersion inversion to zero. The completed checker instead certifies the exact squared identity **and** the positive-root condition; the kinetic formula and numerical solver were not changed. The initial record is not erased.

## 8. Interpretation and next boundary

This is a controlled, one-sector kinetic comparison. It shows that a bounded-speed square-root approach law can alter amplitudes while the geometric configurations and channel thresholds remain fixed. It does not derive special relativity, physical c, or speed-induced dimensional reduction.

Still missing are a complete relativistic/covariant treatment of all sectors, independently occupied particle/product state spaces, physical calibration, a microscopic justification of the sampling and face gates, stable identified products, and a three-output geometric route. No 372:1 ratio is obtained or fitted.

The next distinct test is a specified **physical axial deformation** of the comparison geometry with this kinetic baseline held fixed. A consistent coordinate transformation of shapes and metric must not be advertised as such a deformation.

## 9. Reproduction

From this directory:

```sh
OPENBLAS_NUM_THREADS=1 python relativistic_entrance.py --nD 40 --nt 48 --ns 320 --K 1 2.3 4 6 --rho inf 1 --output refine40.json
OPENBLAS_NUM_THREADS=1 python relativistic_entrance.py --nD 48 --nt 64 --ns 320 --K 4 6 --rho inf 1 --output refine48.json
OPENBLAS_NUM_THREADS=1 python verify_relativistic_kinetics.py
```

Dependencies: Python, NumPy, SciPy, SymPy. No network access or repository mutation is performed by the scripts. The bundle includes unchanged source payloads, exact source hashes, all recorded comparison/refinement runs, control runs, and verification receipts.
