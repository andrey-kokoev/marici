# Quantum strain carried through the retained entrance-to-product route

Date: 2026-10-12  
Status: **New conditional quantum-configuration construction with finite-basis scattering tests. Not an electron–positron prediction, a converged continuum flux curve, or a Lorentz-contraction law.**

## 1. Result and source boundary

The source `dynamical_strain_note.md` gives an autonomous *semiclassical entrance diagnostic*: separation and axial strain are classical mean variables, while tilt and native phase records evolve coherently. It explicitly does not execute the product gates. Its final section requests a quantum strain coordinate, a common energy reference and a comparison between different strains on the whole route.

This calculation makes strain a quantum coordinate in the entrance, connected hinge, all intermediate face-switch records, and outgoing product-record fields. The same incoming lowest-mode preparation is used as radial energy changes. No classical trajectory's minimum strain is substituted into a fixed-strain scattering table; no independently normalized rare component is relaunched as the whole input; and no stage probabilities are multiplied.

Nonzero asymptotic 2+8 record flux survives the tested refinements. The highest sampled energy remains noticeably sensitive to numerical discretization and closed-mode truncation. The results below are provisional finite-model fractions, not physical particle branching fractions.

The new incoming state has finite strain width even before contact. In the finer fixture, its mean axial factor is 1.01139 and its standard deviation is 0.30492. This pre-impact width must not be labeled collision-induced compression. Its kinetic and elastic energy is included in the incoming energy reference.

## 2. Retained inputs and additional choices

The unchanged archive `inputs/pentachoron_dynamical_strain_bundle.zip` contains the previous semiclassical diagnostic and the nested joint-pose scattering sources. Their manifests are checked before functions are reused. Its source geometry supplies the material-frame native folds, nearest-nonoverlapping comparison, pose-covariant route, full-spinor switch projectors, and common positive gate coefficients.

Retained source equations, in the preceding notation:

    M_lambda = (8/5) m ell^2,
    I_delta(lambda) = M_lambda (1+lambda^2),
    U_el(lambda) = 8 epsilon_el (1-lambda)^2.

The main fixture keeps epsilon_el=epsilon and epsilon=hbar=m=ell=1. The source square-root radial kinetic coefficient has rho=mc^2/epsilon=1. Strain, tilt, hinge and product motion remain nonrelativistic. None of these equalities supplies physical calibration.

**New rules in this turn:**

1. Quantize the strain–tilt metric using its Laplace–Beltrami kinetic form. This is a stated quantization choice, not a theorem of arrow counting.
2. Use zero-value boundaries at the collapsed limit lambda=0 and at a numerical upper strain cutoff. The principal cutoff is 2.4; a 2.8 control is included. The singular zero-size simplex is not used as a geometric configuration. These boundary/domain choices are additional data.
3. Identify corresponding material record coordinates at different positive strains without an extra prescribed phase rotation. This is a new cross-strain comparison/connection, not the unique connection forced by the vertex metric.
4. On the connected hinge use the fixed fractional arc coordinate u=s/s_star(lambda), with -1<=u<=1. The cross-strain derivative holds u and those material records fixed. It is **not** claimed to be the complete two-variable kinetic metric obtained by differentiating all hinged vertices; mixed mechanical terms and alternative connections are not resolved by this choice.
5. Carry the same strain coordinate, its kinetic energy, restoring energy and measure through every topology sector. Thus outgoing record channels carry strain energy too. This is a continuation of one retained pair-deformation record, not a construction of independently deformable occupied physical particles.
6. Extend the existing positive-strain fold/hinge formulae through lambda>1 to allow rebound/expansion. Direct tangent-normal, endpoint and product-partition tests check that extension. For expansion, the ABE patch is determined by the actual global comparator, not by silently extrapolating the old compression-only patch theorem.
7. Prepare the equal mixture of the new lowest *joint strain–tilt–phase* modes. Exact lambda=1 and zero strain momentum are not imposed on a quantum input. This is not the same preparation as the previous classical mean-strain fixture.

The geometric pose register remains the preceding pose-covariant register. Its conserved cycle channel is retained analytically. The older fixed-cell memory swap is not reintroduced into the changed pose-covariant model, which already had no cross-product pose-cycle links.

No QED formula, fitted branching ratio, measured mass, lambda=1/gamma prescription, or new geometry-based numerical speed cutoff is inserted.

## 3. Quantum measure and incoming internal operator

Apart from a constant, the strain–tilt metric volume is

    r(lambda) d lambda d delta,
    r(lambda)=sqrt(1+lambda^2).

In the selected model units, the natural-frame kinetic operator is

    T_int = -(5/16) [ r^(-1) partial_lambda(r partial_lambda)
                       +(1+lambda^2)^(-1) partial_delta^2 ].

A unitary change to flat measure is

    u(lambda,delta)=sqrt(r(lambda)) psi(lambda,delta).

It gives the exact flat-measure expression

    T_int,flat = -(5/16) partial_lambda^2
                 -5/[16(1+lambda^2)] partial_delta^2
                 + V_metric(lambda),

    V_metric(lambda)=5(2-lambda^2)/[64(1+lambda^2)^2].

The metric term is not a fitted elastic force. The two expressions are the same admitted kinetic rule in different measures. Symbolic differentiation checks the equivalence, and independent weighted-volume and flat-coordinate finite differences converge to the same scalar eigenvalues.

For one body record in the conserved pose channel, define

    h_in = T_int,flat + L_0(delta,lambda) + 8(1-lambda)^2.

The other body is the inherited opposite-chirality mirror copy. The common lowest pose-cycle energy c0=(3-sqrt(5))/2 is added on both sides of scattering. All body sectors remain direct sums of phase records, not a tensor-product two-particle preparation.

Periodic material tilt, the strained native matrices and the physical preparation are handled together. No replacement of the evolving record by an instantaneous fixed-lambda ground state is made.

The principal finite-difference/Fourier incoming results are:

| Strain nodes | Tilt Fourier nodes | Total lowest energy / epsilon | Mean lambda | Standard deviation of lambda |
|---:|---:|---:|---:|---:|
| 9 | 17 | 3.532811 | 1.011135 | 0.299844 |
| 17 | 25 | 3.553013 | 1.011358 | 0.303990 |
| 25 | 25 | 3.557585 | 1.011393 | 0.304924 |

The full lowest preparation has eight modes after accounting for the two body records and two conserved lowest pose modes; only one identical pose block needs solving. The incoming reference differs from the earlier 1.932476-epsilon mean-strain ready state because the quantum strain mode now contributes energy and changes the native preparation. The difference is not a measured particle mass or a discovered radiation energy.

## 4. Carrying strain through the changing route geometry

The hinge interval depends on strain. The inherited quantities are

    theta_star(lambda)=2 atan(sqrt(5/3)lambda),
    I_hinge(theta,lambda)=[6+8lambda^2-2lambda^2 cos(theta)]/15,
    s_star(lambda)=integral_0^theta_star sqrt(I_hinge) dtheta.

To compare Hilbert spaces at different strains, use u=s/s_star and

    chi_tilde(lambda,u)=sqrt(s_star(lambda)) chi(lambda,s_star(lambda)u).

This preserves the hinge norm. Its u kinetic coefficient is 1/[2 s_star(lambda)^2]. The source physical trace at the middle or endpoint is chi_tilde/sqrt(s_star), **not** chi_tilde without that factor. All entrance and endpoint diagonal and off-diagonal comparisons retain this normalization.

Add the flat strain kinetic term and V_metric+U_el to the hinge field, every one of the eight pairing records at each endpoint, and both output fields. At a fixed lambda, the native connected and final seam operators and the three full-spinor face-switch operators are rebuilt from that strain's geometry. Material record labels are retained across strain nodes.

The two final native product blocks remain separate because the strain derivative acts on the same retained cell identity. This does not turn a common phase-record deformation coordinate into two independently occupied particles.

The original radial coordinate retains the source's spectral square-root Neumann half-line kinetic operator. The original comparator and its ABE-active patch now depend on the quantum coordinate lambda. The patch sampler is normalized separately within each strain fiber; integrating over strain preserves coherence between different lambda components through the strain kinetic operator.

For expansion, local cusp inequalities give a necessary interval and the source global minimizer checks and, where needed, clips that interval. A 2500-configuration control checks the resulting marked-patch classification. An independent dense-bracket minimizer additionally checks the comparator on compression and expansion samples. The old analytic area formula is recovered on its stated 0<lambda<=1 domain. Numerical patch quadrature is not a new physical tolerance.

## 5. One Hamiltonian and conserved-energy scattering

In schematic form the operator is

    H = T_radial + T_strain + T_tilt/hinge
        + U_el + H_native + H_comparisons + H_face_switches + H_output.

Each term acts on the appropriate retained topology sector. The original and downstream fields and finite configuration records form one direct-sum state. The energy is not counted once for each simultaneously occupied classical shape: it is the expectation of this one operator with the source's phase-record norm.

Before the flat-measure change, the admitted internal kinetic forms are nonnegative. Elastic and comparison energies are nonnegative. The native operators are bounded Hermitian functions of positive strain. On the supplied domains, the form can be closed from smooth records supported away from collapse; the zero-value/Friedrichs choice specifies that extension. At shrinking hinge lengths, the strain Dirichlet kinetic form controls inverse-lambda endpoint weights by the half-line Hardy bound, together with the one-dimensional u trace estimate. A different collapse boundary or cross-strain connection would be another model.

For every numerical finite strain/Fourier truncation used here, the conservative interior matrices are Hermitian. Exterior fields are eliminated with the original outgoing resolvents/logarithmic derivatives, not absorbing sinks. Open native strain–phase modes have their actual velocities and unit-flux normalization; all open modes are required below the retained internal cutoff. Closed modes remain in the projected solve, with a varied high-mode cutoff.

At the same total energy on every branch,

    P_original + P_product,- + P_product,+ = 1,
    K_out,a = E_total - E_internal,a.

Strain energy is part of E_internal,a on both sides. There is no external timed compression pulse, lost deformation energy, or product percentage obtained by averaging fixed-strain percentages. The common pose energy cancels from kinetic differences but is retained in the ledger.

## 6. Provisional product flux and energy ledger

K is radial kinetic energy above the **new joint quantum ground**. The three preparations are the same internal lowest-mode mixture at different radial energies, not three prescribed compressions.

| K/epsilon | Coarse joint grid | Refined joint grid | Finer joint grid | Finer grid with more closed modes |
|---:|---:|---:|---:|---:|
| 1.0 | 0.041424% | 0.042526% | 0.044329% | Not recomputed |
| 2.3 | 0.166388% | 0.190305% | 0.192566% | 0.186441% |
| 4.0 | 2.132629% | 2.569921% | 2.288926% | 2.191554% |

These are both 2+8 product-record exits summed. The remainder is outgoing original-record flux, including excited joint internal modes. The two geometric directions give equal flux for this symmetric preparation and continuation, not a universal physical left/right rule.

The tested ranges are approximately 0.04–0.05%, 0.16–0.20%, and 2.1–2.6%. They are **observed numerical ranges, not rigorous error bounds or certified continuum predictions**. In particular, changes at K=4 are large compared with numerical current-conservation residuals.

At K=2.3 in the finer grid:

    E_in/epsilon = 3.557585372764 + 2.3,
    E_out/epsilon = 3.918311300205 + 1.939274072558.

The radial loss, about 0.360726 epsilon, equals the increase in the outgoing mean joint internal energy. That internal energy includes strain, tilt and native phase; it is not solely elastic strain energy. The two totals agree. The separately saved cutoff refinement changes this ledger slightly, so those decimals describe the saved finite solve.

A stationary solution does not produce one trajectory-specific minimum lambda. Nor do these flux fractions show that every converting component was compressed by impact rather than accessing a smaller-lambda component already present in the ready quantum state. Resolving that distinction requires further channel-resolved strain diagnostics.

## 7. Verification and actual numerical limits

The verifier records 81 passing checks, including repeated receipt audits; that number is not a count of independent theorems. Its actual scope includes:

- exact metric volume, inverse metric, and flat-measure transformation;
- source-manifest verification, without upgrading ancestral physical identifications;
- expanded positive-strain tangent normals, hinge endpoints and product independence;
- direct native-source reconstruction over the strain grid;
- global patch classification and independent dense-bracketing comparator controls;
- independent weighted-volume versus flat-coordinate scalar strain discretizations;
- strain-dependent phase-frame covariance and an omitted-kinetic-link negative control;
- all open channels retained, eigenpair residuals, full S-matrix flux and common-energy checks;
- zero entrance and zero subsequent face-switch controls, both giving exactly zero product flux;
- strain/tilt, radial/hinge and closed-internal-mode refinements;
- extension of the upper strain cutoff from 2.4 to 2.8;
- an independent exact-per-u-segment matrix differential solver for the strain-resolved hinge, compared against finite elements at two resolutions.

There are seventeen saved main/refinement/segment stationary solves and eight additional control solves. The largest main full-S unitarity residual is about 1.27e-13. Main common-energy bookkeeping residuals are below 9e-15 epsilon. These verify conservative algebra, **not** continuum convergence or physical accuracy.

On the coarser strain grid, finite elements and the independent segment solver approach one another when u resolution doubles. At K=4 their difference falls from about 0.0975 to 0.0251 percentage points. Both methods still share the finite strain grid and incoming Galerkin truncation; this is not a second independent solution of the entire continuous three-coordinate entrance problem.

The main-to-finer combined refinement changes K=4 by about 0.281 percentage points; increasing its retained one-body mode count from 120 to 144 then changes it by about 0.0974 percentage points. No all-energy scan, resonance location, maximum, time-domain compression distribution, or physical uncertainty interval is claimed.

## 8. What advanced and the next test

A quantum strain degree of freedom now remains in one conservative, conditional route from incoming motion to product-record flux. The elastic budget is present before and after the topology changes; incoming strain preparation is explicitly different from an exactly uncompressed classical object.

Still not established: a unique cross-strain connection or collapse boundary, a full vertex-derived strain–hinge kinetic metric, a converged continuum curve, independent occupied-product states, physical strain preparation, stable species, a three-output geometric route, a Lorentz-covariant theory, or lambda(v)=1/gamma. The source impact-deformation proposal has not become a free-motion contraction law.

The useful next diagnostic is to resolve the strain distribution feeding each product channel, distinguishing impact-induced compression from selection of the incoming ground state's pre-existing width. It should use the joint state and its common energy, not a fixed-strain probability table or a normalized-and-relaunched subbranch.

## 9. Reproduction

The unchanged immediate source archive is included. Source modules are safely extracted into `.source/` and their nested manifests checked. There is no network access or repository mutation.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python quantum_strain_route.py \
      --nlam 25 --N 25 --nm 120 --nD 20 --nu 60 --nquad 64 --npatch 24 \
      --K 1 2.3 4 --output rerun_finer.json

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify_quantum_strain.py

The retained-receipt audit is `python verify_quantum_strain.py --receipts-only`; it still freshly executes small algebra, mode and geometry checks. Dependencies are Python, NumPy, SciPy and SymPy. `quantum_strain_route_v1.py` is retained solely to match the first two saved implementation hashes; the current solver uses a below-spectrum shift for low-mode extraction and adds the independent segment method. These changes do not alter the declared principal Hamiltonian.
