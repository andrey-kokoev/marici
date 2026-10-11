# A uniform source-operation energy lift and the belt's missing coherence

## Constructive result

Following Nima's clarified construction discipline, we fixed one operation-to-energy rule and applied it to the actual proton and intrinsic-belt source operations. We did not require uniqueness of that rule before constructing a witness, and did not insert the final return projector as the Hamiltonian target.

The result identifies a concrete difference in assembly:

| Construction stage | Proton | Belt |
|---|---:|---:|
| Native triangle cycles | 12 | 18 |
| Selected phase lines before alignment | 12 | 18 |
| Native global alignment generators | 2 | 1 |
| Modes after phase selection and native alignment | 1 | 6 |
| Shared-edge seams inside the declared local groups | 0 | 21 |
| Independent within-group amplitude constraints | 0 | 15 |
| Modes after shared-edge matching and alignment | 1 | 1 |

The belt's six residual modes are connected by actual shared-edge matching. The resulting common energy constructor recovers the existing rank-one return for both carriers. This is a realization of the sector-coherence step, not a numerical neutron mass yet.

## 1. Reuse Nima's construction without confusing native operations

Nima's `research/nima/uniform-local-core-proof.md` constructs, for a native self-adjoint involution P,

    H_P = pi (I-P)/2.

Our proton and belt are not Bool-factor flips. Their native local triangle cycles have order three. In the retained geometric metric these cycles are not unitary. A unitary path cannot have a nonunitary endpoint, so directly applying a Hermitian logarithm to those cycles would silently change the metric or the operation.

The native global spatial rotations are unitary, but their orders are also three. Thus the exact involution endpoint theorem does not apply to every source operation unchanged.

We use the following explicit extension as a **positive constraint-energy constructor**:

    D -> H_D = (pi/4) D^sharp D.

Here sharp is the adjoint in the declared physical metric. For an involution, taking D=P-I gives

    (P-I)^*(P-I)/4 = (I-P)/2,

so this rule exactly recovers Nima's generator. For a general operation T and retained character chi, take D=T-chi I. This is not claimed to interpolate to T at time one. Its purpose is to construct positive dynamics whose ground states satisfy the source operation's character equation.

The factor pi/4 is shared, inherited from the involution normalization. A conversion to physical energy still requires a common time/energy unit. No separate proton and neutron stage coefficients are fitted.

## 2. Actual local triangle operations

For the proton, the stored triangle record gives its three vertex columns X and the primitive three-cycle C. Reconstruct

    A = X C X^(-1).

The selected source character is omega=(-1+i sqrt(3))/2, and the retained local vector is X(1,omega,omega^2). Thus (A-omega I)v=0 directly from the source, before a Hamiltonian is supplied. A has the three distinct cube-root eigenvalues, so this local character line is one-dimensional.

For the belt, use the actual two-dimensional plane coordinates of each small triangle. Its retained vector is r+i sqrt(3)s. The cyclic vertex operation restricts to

    A r = -r/2 - 3s/2,
    A s = r/2 - s/2.

This uniquely determines its real action on the independent plane vectors r,s. The checker constructs it in the stored numerator-coordinate basis and verifies its order-three and character equations. The two nonreal eigenvalues are simple, leaving one selected line per triangle.

The source's geometric metric is retained. In numerator coordinates y_i=sqrt(d_i)x_i, it is diag(1/d_i), not the identity. Adjoint operations and every energy calculation use this metric.

The direct sum of local character-defect energies therefore has ground dimension twelve for the proton and eighteen for the belt.

## 3. Alignment comes from native rotations

For the proton, use the two original oriented tetrahedral rotation generators, as permutations of the four corner labels:

    (A B C), and the stored (B A D) orientation.

Their retained matrices generate all twelve proper tetrahedral rotations. The checker reconstructs their joint action on placement and coordinate labels and verifies that the group average is exactly the old alignment projector G. Consequently the common kernel of their T-I defects is im(G), of dimension three.

For the belt, use its actual 120-degree sector rotation. In the co-rotating intrinsic charts this shifts the three sectors and preserves their twelve local coordinates. Its three-element average is exactly the stored G, of rank twelve.

The phase-line projector commutes with G in both cases. Their intersection has dimension one for the proton but six for the belt. These six belt modes are the independent amplitudes of the six triangle orbits under the sector rotation. Native rotation alone does not identify them.

## 4. Construct the sector coherence using actual shared edges

The already declared local groups differ:

- Each proton local-selection block contains one small triangle, with three ambient coordinates.
- Each belt local-selection block contains six small triangles, with two intrinsic coordinates each. These are the three triangles on each of two adjacent belt faces.

These are operator-local groups, not the four larger proton face sectors used elsewhere in the visualization.

For a retained triangle mode v_t, define its amplitude readout

    ell_t(x) = <v_t,x_t>/||v_t||^2.

Within each local group, include one interface equation for every pair of triangles sharing an actual edge:

    ell_t(x) - ell_u(x) = 0.

This is the new declared interface law. It identifies coefficients relative to the source's retained oriented modes; it does not equate arbitrary Cartesian vector components or impose equal norm-normalized intensities. The choice to match these mode amplitudes is explicit, while the list of seams is read from geometry.

A paired belt sector supplies two three-cycles of small triangles, joined by one shared-edge seam. Its graph has six vertices and seven edges. Its incidence rank is five. Therefore its six phase amplitudes become one, without guessing a complete graph or adding nonadjacent seams.

Across all three sectors there are 21 seams and 15 independent equations. Phase selection plus these equations has kernel dimension three, exactly the image of the existing sector-local L. Native alignment then makes their sector amplitudes agree, recovering exactly the original rank-one N.

Equivalently, if alignment is applied first, six amplitudes remain and the same seam equations impose five independent relations on them. The source already supplied the right collective vector; this construction explains how the selected local sector coherence can be enforced by its internal geometric interfaces.

## 5. Normalize the seam operation through the metric

A raw amplitude-difference functional b=ell_t-ell_u has dual squared norm

    ||b||_*^2 = 1/||v_t||^2 + 1/||v_u||^2.

Its normalized mismatch projector is

    Pi_e = b^sharp b / ||b||_*^2.

The metric-derived reflection R_e=I-2Pi_e is an involution. Apply Nima's construction to this **constructed seam operation**:

    H_e = pi(I-R_e)/2 = pi Pi_e.

This fixes the seam normalization once its equality rule and the source metric are supplied. It also makes the energy independent of a common nonzero rescaling of the retained mode references. The checker verifies projection, involution and an exact rescaling control.

No claim is made that the original source contained these reflection gates as primitive physical interactions. They are now explicit outputs of a uniform interface construction, rather than a desired rank-one projector supplied without a mechanism.

## 6. One explicit Hamiltonian for both carriers

With all the native phase and alignment defects, and all within-group shared-edge seams, define

    H = (pi/4) [sum D_phase^sharp D_phase + sum D_align^sharp D_align]
        + pi sum_e Pi_e.

Every term is positive. The kernel is the simultaneous solution space of the native character equations, native alignment equations and the constructed shared-edge amplitude equations.

For both carriers this kernel is exactly im(N). The completed local energy commutes with G. The checker verifies the actual coefficient equations and identifies the kernels through the simple character eigenspaces and exact incidence ranks, rather than estimating ranks numerically.

This implements the same declared construction discipline on different source organizations. It does not assert that all uniformly constructible dynamics are equivalent. The native operations, selected character, metric, local grouping and the new amplitude-matching rule are the inputs/declared rules, not outputs selected by an observed mass.

## 7. Coordinate transport and quantitative controls

For the belt's actual embedding W and its metric decoder W^sharp, the new Hamiltonian obeys

    W^sharp H_ambient W = H_intrinsic,
    H_ambient W = W H_intrinsic,

where H_ambient=W H_intrinsic W^sharp on the image. This verifies representation independence for the new operator, not only for the earlier a(I-L)+b(I-G) model.

Exact traces in units of 4H/pi are:

| Term | Proton | Belt |
|---|---:|---:|
| Phase defects | 232 | 805811/3700 |
| Native alignment defects | 144 | 72 |
| Normalized seam defects | 0 | 84 |
| Total | 376 | 1383011/3700 |

These are sums of excitation energies, not rest energies. In particular, the belt's total is slightly smaller here; the constructed seam work does not license declaring its total energy larger. Both selected states still have zero constraint energy. No measured neutron mass was used to select a coefficient or discard a term.

The nonzero seam operator quantifies how departures from paired-face coherence are penalized. It does not imply a permanent energy expense when all its interfaces are satisfied. Linking this assembly dynamics to persistent dressing-register occupations remains the rest-energy bridge.

## 8. What has advanced

Previously the belt's sector-wide rank-one local selection was a supplied projector. We now realize that same selection from:

    triangle-cycle character lines
    -> seven actual shared-edge equations per paired sector
    -> one mode per sector
    -> native threefold alignment
    -> the retained single collective mode.

The proton needs no corresponding within-group six-mode stitching: its native triangle lines and tetrahedral alignment already select the collective mode.

This gives a concrete formation distinction before any mass interpretation. The next useful comparison is to put the already constructed physical record/occupation mechanism on these explicit seam operations and native phase operations. We can ask which registers remain occupied in a persistent belt, rather than assigning a generic cost to 'selection' as a whole.

## Verification and artifacts

    python research/voevodsky/checkers/check_native_operation_energy_lift.py

All coefficient, metric, incidence, kernel and intertwining tests pass with exact rational/quadratic-field arithmetic. Pi remains a symbolic common factor; no floating eigenvalue threshold is used. This is a written standard finite-dimensional construction supported by exact checks, not a new Agda kernel theorem.

- `results/native_operation_energy_lift.json`: construction checks, dimensions, seams and exact traces.
- `results/native_operation_energy_lift_store.json`: both complete scaled Hamiltonians, coordinate metrics and source hashes.

Nima's source results: `research/nima/uniform-local-core-proof.md` and `research/nima/spectral-whole-return-proof.md`. This construction reuses the former's involution rule. It does not claim a whole-Tick return proof for the new proton/belt operations or an order-three endpoint interpolation.
