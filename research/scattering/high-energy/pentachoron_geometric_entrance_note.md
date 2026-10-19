# A geometric separation-and-tilt entrance for the open-product model

Date: 2026-10-11  
Status: New conditional quantum-configuration construction and numerical tests. **Not physical electron–positron scattering, Lorentz contraction, or a calibrated speed law.**

## 1. Result and source boundary

The supplied open-product model began with access to ABE already supplied. This extension replaces its original point-sampled encounter line by a two-coordinate entrance: center separation D and a common internal x–w tilt delta. The earlier nearest-nonoverlapping comparator supplies a scalar deformation cost. Its exact ABE-active region supplies the spatial support of a new coherent entrance comparison.

The remaining connected hinge, both endpoint graphs of eight pairing states, full-spinor face-switch gates, retained memory, and 2+8 output leads are reused. One stationary boundary-value problem now covers the entrance region and those downstream components. No probabilities from separate stages are multiplied.

The numerical fixture has nonzero product flux and a nonmonotonic energy response. The finite geometry selects the contact region, **not its coupling normalization, incoming preparation, or all the dynamics**. An important analytical control is that there is no strictly positive geometric potential barrier to the closure of that region when free tilt is allowed. No universal threshold speed follows.

Retained source files:

- `pentachoron_configuration_comparison.py`: marked centered pentachoron, mirrored head-on pair, exact retained-vertex correction cost, global comparison routine.
- `pentachoron_open_product_flux_bundle.zip`: compact native matrices, quantum hinge and its kinetic coefficients, endpoint topology graphs, full-spinor gates, memory, outgoing operators, reference normalization.
- The source open-product note, sections 3 and 10, explicitly does not include collision-driven access to ABE.

Copies of the source code and compact payloads are under `inputs/`. Hashes are in the result receipt and manifest. The previous full source verification chain is not claimed to have been rerun. No external particle theory or experimental number is used.

## 2. Explicit new modeling choices

1. Separation is D >= 0. At D=0 impose zero normal derivative: the original pair does not exchange its retained center ordering. This is a new conservative boundary choice, not a derived short-distance physical law.
2. The tilt is a full periodic material-frame rotor, delta modulo 2pi. Retained phase frames follow each body's tilt; kinetic derivatives are ordinary in this chosen transported frame. An ambient-frame formulation must transport the kinetic operator too. This is a specified kinetic/transport convention; it is not automatically the ambient-frame convention used for the connected hinge. The periodic material-frame boundary condition is additional data.
3. Quantize the inherited equal-vertex-cost kinetic metric. Keep H_O constant in these entrance material frames. Native comparison of a configuration with its ABE correction uses the reference-frame coefficients at delta_c.
4. Set the earlier geometric energy unit E_* equal to the phase energy epsilon in the numerical fixture. The source did not derive that identification.
5. Couple the entire ABE-active configuration patch coherently and uniformly in its metric measure to the hinge's s=0 trace. Uniform sampling and the normalized patch mode are NEW, not consequences of the patch boundary or a count of arrows.
6. Keep the downstream source couplings fixed; use the same positive entrance coefficient 2 epsilon. Preserve every diagonal term in the new comparison energy.
7. Prepare a fixed, finite-width angular flux superposition centered around zero tilt, with no average angular momentum, in each of the four original native ground modes. This is NOT an exactly unrotated classical object or a derived physical beam preparation.

These choices replace the source's full original encounter line and its already-eligible point contact. Consequently its odd-parity 1/4 access bound and its numerical fractions are not unchanged prerequisites for the new model. The two dark native ground combinations remain dark to the matching gate, but original spatial parity is no longer the source's full-line parity sector.

## 3. Exact ABE-active region

Use dimensionless d=D/ell and

    h = 1/sqrt(5),
    delta_c = atan(h),
    a(t)/ell = max(|cos t| - h sin t, 4 h sin t).

The inherited dimensionless correction cost is

    v(d,delta) = min_t { (5/2)[2a(t)/ell-d]_+^2
                        +32[1-cos(t-delta)] }.

At the ABE cusp,

    a(delta_c)/ell = 4/sqrt(30),
    d_* = 2a(delta_c)/ell = 8/sqrt(30) = 1.460593486680443,
    a'_-(delta_c)/ell = -2/sqrt(6),
    a'_+(delta_c)/ell = 4/sqrt(6).

For 0 <= d < d_*, put q=d_*-d. The unique nearest admissible comparator uses ABE exactly when

    delta_c - asin[5q/(8sqrt(6))]
        <= delta <=
    delta_c + asin[5q/(4sqrt(6))].

The branch is taken in the stated neighborhood of delta_c; equivalent angles are modulo 2pi. The point at d=d_*, delta=delta_c is a zero-cost boundary point rather than a positive-area active region. For d>d_* there is no ABE patch.

This is a geometry-dependent width, not a fitted angular tolerance.

| D/ell | Lower actual tilt | Upper actual tilt |
|---:|---:|---:|
| 0 | 2.213971 degrees | 72.284528 degrees |
| 0.5 | 9.907075 degrees | 53.448624 degrees |
| 1.0 | 17.345684 degrees | 37.689155 degrees |
| 1.4 | 23.208972 degrees | 25.866796 degrees |
| d_* | 24.094843 degrees | 24.094843 degrees |

The *actual* pair generally has overlap and tilt different from delta_c. Its nearest corrected configuration has the complete ABE face. Using this comparator to trigger coupling remains the inherited modeling interpretation; the comparator is not a second realized particle configuration.

### Why the local derivative test is sufficient here

Write u=(cos t,sin t) and v0=(cos delta,sin delta). Extend the objective to the unit disk:

    F(u)=(5/2)[2 max(u_x-hu_y,-u_x-hu_y,4hu_y)-d]_+^2
          +32(1-u.v0).

This is convex in u. At u_c the tangential subgradient condition is exactly the two inequalities above. A selected subgradient is -lambda u_c, where

    lambda = 32 cos(delta_c-delta) - 10q a(delta_c)/ell.

Throughout the stated patch, cos(delta_c-delta)>=2/3 and
10q a(delta_c)/ell<=32/3, so lambda>=32/3>0. For every other point u in the unit disk,

    F(u) >= F(u_c)+lambda(1-u_c.u) > F(u_c).

Thus this is the unique global circle minimum, not merely a stationary cusp. Necessity follows from the one-sided derivative test and comparison with the equal-support reflected cusp at pi-delta_c, which excludes the opposite cos(delta) half-plane. The result is independently checked against the inherited global minimizer on 4000 random configurations and against a dense-bracketing minimizer at 27 interior patch fixtures.

### Metric area, and the absence of a positive geometric barrier

Define y=(4/sqrt(5)) ell delta. With measure dD dy, the patch has finite area

    |Omega_ABE| = 1.521810286455744 ell^2.

For a=5/(8sqrt(6)) and b=5/(4sqrt(6)), its exact expression divided by ell^2 is

    (4/sqrt(5)) sum_{r=a,b}
       [d_* asin(r d_*) + (sqrt(1-r^2 d_*^2)-1)/r].

This is area in configuration space, not a measured collision cross section.

At D=4ell the comparison cost is zero for every tilt. One may continuously tilt from zero to delta_c there, then approach D=d_*ell, with zero comparison cost throughout. This proves zero *potential barrier* to the patch closure under free tilt. It does not prove a specified incoming state follows that path, has zero kinetic cost, or takes finite time at zero speed. It excludes an intrinsic strictly positive energy cutoff obtained from this scalar geometry alone.

## 4. Quantized entrance, with all energy accounted for

The inherited ten-vertex displacement metric gives

    T = (m/4) D_dot^2 + (8m ell^2/5) delta_dot^2
      = (m/4) D_dot^2 + (m/2) y_dot^2.

Under the new quantization choice the entrance operator is

    H_ent = -(hbar^2/m) d_D^2 -(hbar^2/(2m)) d_y^2
             + H_O + E_* v(D/ell,delta).

Its state is Psi(D,y) in L2(R_+ x S1, dD dy) tensor C20. This is still a direct sum of retained phase records, not the tensor product of independently occupied particles. The hinge has its previous interval field chi(s).

Let f=1/sqrt(|Omega_ABE|) on Omega_ABE. Replace the old point entrance by

    Q_join = 2 epsilon integral_Omega
       ||P Psi(D,y) - f sqrt(ell) P chi(0)||^2 dD dy.

P is the inherited rank-two matching projector in the common reference frames. The square retains the entry-side diagonal, the hinge-side diagonal, and the off-diagonal comparison. Modes orthogonal to the sampled bright combination are not discarded or renormalized away; they remain in the entrance field.

A point-to-point contact from a two-dimensional entrance would need additional care. The construction deliberately uses an area-supported bounded sample on the entrance, and only the already well-defined one-dimensional hinge trace. The finite patch sample is bounded by Cauchy–Schwarz. The hinge trace is bounded on H1. Together with the positive native and kinetic forms, this defines a closed lower-bounded quadratic form and a self-adjoint time-independent Hamiltonian.

Add the source's hinge, both eight-state endpoint graphs, memory, and outgoing leads unchanged. No external switching function, stochastic stage handoff, absorbing sink, or independently multiplied entrance probability appears. For a common total energy E, each outgoing native/tilt channel retains kinetic energy E-e_channel. Closed modes are retained without outgoing current.

This construction includes separation and tilt dynamics. **It contains no speed-dependent metric contraction or relativistic dispersion.** It is not yet a test of near-c Lorentz-like flattening.

## 5. Incoming state and the meaning of the energy axis

As D tends to infinity the scalar geometric potential vanishes. Material rotor modes exp(i n delta) have kinetic energies

    e_rot(n) = (5/32) n^2 epsilon

in the numerical fixture epsilon=hbar=ell=m=E_*=1. Native ground energy is

    e0 = (11-2sqrt(6)-sqrt(5))/2 epsilon.

At E=e0+K, prepare the same angular **flux** coefficients

    c_0=3/2, c_{+1}=c_{-1}=1, c_{+2}=c_{-2}=1/4,
    sum |c_n|^2 = 35/8,

normalized by sqrt(35/8), in every one of the four native ground modes. Their phases are fixed at the reference section D=4ell, outside the interaction. They are the Fourier coefficients of (1+cos delta)^2. Each propagating mode also has its required radial unit-flux factor 1/sqrt(v_n).

Thus K is the sum of incoming separation and tilt kinetic energy above e0, not the radial kinetic energy alone. The fixed superposition has zero mean signed angular momentum but nonzero angular kinetic energy. Its continuum mean rotational contribution is 5epsilon/56. The actual boundary probability density varies slightly with K through the flux factors; no assertion of an identical spatial probability wavefunction at every energy is made.

All five prepared angular modes are open at the four listed energies. The code refuses a lower energy where that fixed preparation would require a closed incident mode; it does not silently discard one and renormalize. A separate uniform-rotor preparation is an explicit control.

## 6. Stationary product flux

The finest reported grid has 128 radial intervals on 0<=D<=4ell, 128 periodic tilt nodes, and 320 hinge intervals. Exterior radial and product leads are eliminated through their outgoing logarithmic derivatives. Radial motion outside the computational region is not placed in a reflecting box.

| K/epsilon | Original record output | Negative product route | Positive product route | Total 2+8 product flux |
|---:|---:|---:|---:|---:|
| 1.0 | 99.996297% | 0.000991% | 0.002712% | 0.003703% |
| 2.3 | 99.967857% | 0.016191% | 0.015952% | 0.032143% |
| 4.0 | 96.611226% | 2.077725% | 1.311049% | 3.388774% |
| 6.0 | 99.115114% | 0.612765% | 0.272120% | 0.884886% |

These digits describe the saved discrete solve. Appropriate summaries are about 0.0037%, 0.032%, 3.4%, and 0.88%. The two exits are symmetry-related two-boundary outputs, not two- versus three-particle channels. No physical particle identification or near-c speed is assigned.

The rate is not monotone over these samples. Geometry determines where the gate acts, while the incident motional state, kinetic operator, internal evolution, and coherent interface set the amplitude. No maximum or resonance energy is certified by four samples.

For K=4epsilon the mean energy ledger, in epsilon units, is

    E_in = 1.932476268466933 + 4,
    E_out = 2.827962458562902 + 3.104513809904033.

The first outgoing term includes native/memory energy and, on the original lead, tilt energy. The second is outgoing radial kinetic energy. They sum to the common total. Conditional internal energies are not interpreted as physical product masses.

## 7. Controls, sensitivity, and numerical limits

All source face-switch coefficients remain fixed in the principal tests. At the 64-by-64 entrance / 160-hinge grid:

| Change | Product flux at K=2.3epsilon | Product flux at K=4epsilon |
|---|---:|---:|
| Principal finite-width tilt input | 0.03223% | 3.37259% |
| Uniform incoming rotor | 0.01159% | 1.25703% |
| Geometric potential set to zero, patch retained | 0.02990% | 0.60070% |
| Entrance coefficient halved | 0.01511% | 3.28746% |
| Entrance disconnected | 0 | 0 |
| Subsequent face switches disabled | 0 | 0 |

A finite product signal therefore requires both access and the later admitted switches. Its numerical size is not fixed by canonical incidence alone. Removing the geometric potential is a changed model, not a coordinate change.

Verification actually performed:

- Symbolic support, derivative, cusp-width, kinetic, and convex-disk certificate identities.
- 4000 global-minimizer classification checks and 27 independent dense-bracketing cost checks.
- Exact-form area versus independent quadrature.
- Incoming/output current and common-energy ledgers for 28 recorded stationary solves.
- Complete S matrices, including incident product modes, at four energies on the 32-by-32 entrance / 80-hinge grid. Maximum unitarity residual: 9.87e-14. On the finer principal grids, only the four prepared input columns and their mutual flux orthogonality are checked, not every incoming mode.
- Refinement from 32 to 64 to 128 entrance intervals/nodes with hinge refinement. The last product-probability changes are about 2.00e-7, 8.74e-7, 1.62e-4, and 3.43e-5. The largest is 0.0162 percentage points. Exact numerical conservation is much stronger than the continuum discretization accuracy and must not be confused with it.
- Moving the exterior matching section from 4ell to 5ell while preserving the incident reference phases gives small finite-difference phase errors consistent with refinement.
- An independent known solution: with geometric potential and entrance gate absent, the original radial channel has free Neumann reflection. Complex amplitude errors decrease from 0.03934 to 0.00983 when the radial spacing is halved, confirming second-order phase convergence, not just current conservation.

The new calculation does not claim an independent full two-dimensional continuum solver, a 501-energy scan, or rerunning every inherited checker. The saved verification driver records 17 grouped checks. Residuals are numerical diagnostics, not experimental uncertainty.

## 8. What this establishes and the next boundary

A conditional, conservative chain is now explicit:

    separation + material tilt + geometric correction cost
      -> ABE-active comparison region
      -> quantum connected hinge
      -> retained face-switch graph
      -> memory-preserving exit
      -> 2+8 record flux.

The source's assumption of *already being at ABE* is no longer the entrance boundary condition. However the interpretation of the nearest comparator, the uniform coherent sampling law, material-frame rotor kinetic convention, incoming angular preparation, and common scale choice are admitted rules—not results of arrow counting.

Remaining gaps include speed-dependent compression, relativistic kinetic and covariance laws, physical length/energy calibration, microscopic selection of the interface rule, independently occupied product states, stability/species identity, and a geometrically admitted three-output route. No QED statement, photon assignment, or 372:1 prediction is inferred.

A useful next test is a relativistic kinetic extension at fixed contact geometry, keeping its new assumptions distinct from a derivation of contraction or a physical calibration.

## 9. Reproduction

Run from this directory:

    OPENBLAS_NUM_THREADS=1 python geometric_entrance.py --nD 64 --nt 64 --ns 160 --K 1 2.3 4 6
    OPENBLAS_NUM_THREADS=1 python run_controls.py
    OPENBLAS_NUM_THREADS=1 python verify_geometric_entrance.py

The saved highest-resolution receipts can be audited without regenerating them. The verifier freshly runs the small free-reflection control unless passed `--receipts-only`. Dependencies: Python, NumPy, SciPy, SymPy. No network or repository mutation is used.
