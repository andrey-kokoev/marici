# Strain-resolved product flux: redistribution, selection and interference

Date: 2026-10-12  
Status: New diagnostics of the supplied finite-basis quantum-strain model. No Hamiltonian change, physical electron–positron claim, classical path attribution, or continuum-convergence certification.

## 1. Result

The outgoing product-record strain distribution is centered slightly above the undeformed value lambda=1. Its width increases at the highest of the three tested energies. Signed currents inside the connected/switching subsystem demonstrate transport between strain slices during the stationary interaction. Contributions associated with different strain slices interfere substantially.

These results distinguish dynamical redistribution from a mere list of pre-existing shapes. They do **not** divide converting events into unique percentages caused by pre-existing compression versus newly generated compression. The present coherent stationary calculation contains no recorded trajectory that would make those two histories mutually exclusive events. A final strain marginal alone cannot establish such a history.

No minimum strain from a classical trajectory is inserted into a scattering table. No rare component is independently normalized and relaunched. The original coherent scattering solution is reused, with additional readouts.

## 2. Source and unchanged model

The basis is the supplied `pentachoron_quantum_strain_bundle.zip`, in particular `quantum_strain_route.py` and `quantum_strain_note.md`. The source explicitly identifies a ready quantum strain width and requests a channel-resolved diagnostic in sections 6 and 8. The earlier fixed-strain or semiclassical models are not substituted for this source.

Retained without change:

- The quantum strain–tilt kinetic prescription, material-frame cross-strain comparison, elastic energy 8 epsilon (1-lambda)^2, and domain choices.
- The original radial square-root kinetic law, native matrices, geometric entrance patch, connected quantum hinge, full-spinor face-switch graph, and outgoing 2+8 record channels.
- Every positive comparison coefficient, common energy reference, outgoing flux factor, and the equal incoming lowest-mode mixture.
- The phase-record direct-sum interpretation. The model is not a tensor-product preparation of two independently occupied physical products.

The read-only instrumentation adds two attributes to the original solver: its already solved downstream field and its already solved entrance state. The original numerical equations and return values are unchanged. Exact source snippets are checked before inserting these hooks. The source file itself is not edited. Source hashes and compact copied-input hashes appear in `input_provenance.json`.

New choices concern **diagnostics**, not evolution: outgoing internal energy is resolved before reporting a positive strain histogram; a source amplitude is partitioned at the reference lambda=1; and local stationary currents are reported with their signs. These different quantities must not be interchanged.

## 3. Incoming and outgoing strain distributions

Let S_ai be a unit-flux product scattering amplitude from prepared incoming mode i to outgoing mode a. Let phi_a(lambda) include the product cell records. For each exactly degenerate outgoing internal-energy subspace B, form

    f_Bi(lambda) = sum_(a in B) phi_a(lambda) S_ai.

The energy-resolved outgoing strain density is

    p_F(lambda) = (1/d_in) sum_i sum_B ||f_Bi(lambda)||^2.

Its integral is the **unconditional product flux** P_F. Only the reported conditional histogram is divided by P_F. Coherence within degenerate energy subspaces is retained. Rotating an eigensolver basis within those subspaces cannot change the answer, and is tested explicitly.

This is a defined energy-resolved output diagnostic, not an assertion that all strain measurements have this marginal. A coherent observation at a particular output distance can retain cross-energy interference and has to specify that distance/preparation. A local stationary current density need not itself be a positive strain probability distribution.

The finest source grid has incoming mean lambda=1.011392861 and standard deviation 0.304924319. Its strain uncertainty already exists before contact. At the same incoming preparation:

| Incoming radial K/epsilon | Product flux, finer fixture | Product conditional mean lambda | Product conditional standard deviation |
|---:|---:|---:|---:|
| 1.0 | 0.0443292% | 1.015783 | 0.303404 |
| 2.3 | 0.1925656% | 1.027199 | 0.305157 |
| 4.0 | 2.2889264% | 1.040427 | 0.380006 |

The two symmetry-related exits are both included; they give equal resolved strain statistics for this preparation. Each exit's internal-energy subspaces are also tabulated individually in the JSON files. An outgoing memory/cell or small/large record component remains a record component, not evidence that two physical particles are independently occupied.

The mean is slightly on the expansion side; the highest-energy output is appreciably broader. Neither fact says that no intermediate component was compressed. This is a stationary final-state diagnostic, not a rebound trajectory.

The complete outgoing ensemble, including the much more frequent original-record output, has mean lambda approximately 1.02673, 1.02911 and 1.03555 at the same three energies. These values are distinct from product-conditioned means.

## 4. Signed currents test dynamical redistribution

Let b_j be the actual self-consistent entrance forcing of the downstream matching port at strain node j, with coupling coefficient included. Let y_j be its matched hinge trace. The net current from entrance to downstream at that slice is

    J_entry,j = 2 Im average_i(b_ji^dagger y_ji).

For endpoint eta_111,j and outgoing trace zeta_j, the product normal current is

    J_exit,j = 2 g_exit Im average_i(eta_111,ji^dagger zeta_ji).

With the source's flat strain kinetic coefficient a=5/16, the current toward increasing strain between neighboring slices is

    J_lambda,j+1/2 = (2a/Delta_lambda^2) Im average_i[
        integral du chi_ji(u)^dagger chi_(j+1)i(u)
        + sum_(both endpoint graphs, masks) eta_ji^dagger eta_(j+1)i].

The finite-element hinge integration weights are retained. The outgoing trace nodes themselves are not extra finite-volume occupation nodes: their strain dynamics are already in the exact output lead operator.

An independent reconstruction verifies every strain-slice balance:

    J_entry,j - J_exit,j
      = J_lambda,j+1/2 - J_lambda,j-1/2.

Summing over strain gives

    sum J_entry = sum J_exit = P_F.

Thus there is no hidden sink or source in the decomposition. The ready ground mixture has zero integrated strain current. During scattering the downstream solution has nonzero currents. In the K=4 fixture, current toward smaller lambda occurs in one region and toward larger lambda in another. This is redistribution, not a static selection of unchanged strain labels.

The currents are signed net stationary rates. They include returns and interference and are **not** first-passage probabilities, histories of individual objects, or exclusive percentages of impact-compressed events. A node-resolved entry or exit current can be negative. Its magnitude must not be silently converted into a positive probability histogram.

The current near any single chosen cutoff is more sensitive to its location and grid than the integrated balance. A linearly interpolated diagnostic at lambda=1 is supplied separately; it is not treated as a universal threshold or a calibrated probability of compression.

## 5. Product-feeding strain amplitudes do not add as event counts

At fixed total energy, the retained downstream problem has a linear source-to-output map M. The full self-consistent entrance source b includes returns from the downstream network. Partitioning it by strain gives

    A_j = M_j b_j,
    A_product = sum_j A_j.

For the incoming mixture,

    P_F = sum_j ||A_j||^2/d_in
          + 2 Re sum_(j<k) tr(A_j^dagger A_k)/d_in.

The source Gram matrix and all A_j are saved, rather than only their squared norms. Reassembly agrees with the unaltered product scattering amplitude.

Group source nodes into lambda<1 and lambda>=1. This is a reporting partition at the undeformed reference, not a new geometric tolerance or a detector inserted into the model. At K=2.3 on the finer grid:

| Contribution to the same squared-amplitude calculation | Percentage of incoming unit flux |
|---|---:|
| Squared summed amplitude from source nodes below 1 | 0.0176663% |
| Squared summed amplitude from source nodes at or above 1 | 0.0940086% |
| Cross term between the two groups | +0.0808907% |
| Actual coherent product flux | 0.1925656% |

The last displayed digit in the total is rounded; the JSON retains the full numerical sum. The two bin squares alone sum to only 0.1116749%, not the actual approximately 0.192566% result. The omitted difference is interference, not an unaccounted third event class.

These bins describe strain **at the matching source**, not the initial strain of a classical object. A source component can propagate across strain values downstream, return, and interfere. Consequently the two bin terms must not be called 'pre-existing' and 'created by impact'.

No calculation here physically blocks either bin and resolves the altered Hamiltonian. Such a change would modify feedback and preparation and would be a separate intervention. Likewise resolving every strain node and dropping all cross terms introduces a resolution-dependent dephasing prescription; the diagonal sum alone is not a derived probability law.

## 6. Refinement and verification

Fresh solves used the source's refined and finer settings, plus the finer strain grid with an increased internal-mode cutoff at K=2.3 and 4. A smaller pilot used tighter patch quadrature than the original pilot, and is separately labeled. In all, eleven diagnostic solves are retained.

| K/epsilon | Mean lambda: refined / finer / increased cutoff | Width: refined / finer / increased cutoff |
|---:|---|---|
| 1.0 | 1.015717 / 1.015783 / not run | 0.302455 / 0.303404 / not run |
| 2.3 | 1.027200 / 1.027199 / 1.027198 | 0.304246 / 0.305157 / 0.305159 |
| 4.0 | 1.038820 / 1.040427 / 1.040470 | 0.370227 / 0.380006 / 0.379863 |

These observed refinement differences are not error bounds. The higher-energy width changes by about 0.010 on spatial/strain refinement. The existing source's total product-flux sensitivity remains; no newly converged continuum conversion curve is claimed.

`verify_diagnostics.py` performs a fresh audit of stored wavefunctions, not just saved success flags. It independently rebuilds output native matrices from the endpoint geometry, projects actual boundary fields into their open energy subspaces, reconstructs velocity-normalized strain densities, and recalculates all strain currents from raw hinge and graph fields. It checks the full S matrix, current continuity, the coherent-amplitude Gram ledger, and the ready state's zero integrated strain current. The diagnostic runner also tests arbitrary unitary rotations within degenerate outgoing eigenspaces.

The final independent audit has 122 passing entries across eleven cases and the ready-state control. Its largest absolute reported algebra/current/density residual is about 3.81e-13 in the frozen model units. These are implementation identities, not that many independent physical results, a second solution of the full entrance PDE, experimental uncertainties, or continuum accuracy bounds.

## 7. Interpretation and next experiment

The defensible finding is that the admitted collision model redistributes strain and produces coherent interference between different strain contributions. Its outgoing product-record distribution is not a persistently shortened copy of the incoming shape. However, neither that final distribution nor a stationary source split identifies unique event-by-event causes of compression.

A useful next calculation is an incoming time-dependent packet with strain currents resolved before contact, during contact and at release. It should retain the full branch amplitudes and the same energy ledger. A first-passage or monitored-history definition would be an additional measurement specification, not something read directly from the present stationary amplitudes.

Remaining inherited limits include the phase-record rather than independent-particle interpretation, admitted material connections and strain boundary, unconverged high closed-mode truncation, physical preparation, stability/species identification, and missing calibrated speed or Lorentz-contraction law. This step supplies no new lambda(v), photon identification or 372:1 ratio.

## 8. Reproduction

The compact `source/` contains the original quantum-strain solver verbatim and its unchanged immediate nested archive, plus the relevant source note and numerical receipts. Large cached nested extractions are not bundled. The small `inputs/ready_ground_modes.npz` is an explicitly recorded extraction of the supplied finer-mode ground columns, not a new solver result.

Run:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python strain_diagnostics.py \
      --nlam 17 --N 25 --nm 100 --nD 16 --nu 40 --K 1 2.3 4 --name refined

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python strain_diagnostics.py \
      --nlam 25 --N 25 --nm 120 --nD 20 --nu 60 --K 1 2.3 4 --name finer

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python strain_diagnostics.py \
      --nlam 25 --N 25 --nm 144 --nD 20 --nu 60 --K 2.3 4 --name cutoff

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify_diagnostics.py

Dependencies: Python, NumPy, SciPy and SymPy. No network access or repository mutation is used. JSON files contain per-channel diagnostics and interpretation flags. NPZ files contain the unaltered scattering matrices, output boundary fields, hinge/graph fields, source amplitudes and Gram matrices needed for the independent audit.
