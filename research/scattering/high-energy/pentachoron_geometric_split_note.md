# A geometric two-product exit from the connected pentachoron boundary

Date: 2026-10-11  
Status: Constructive extension of the supplied geometric and phase-record toys. Not an electron–positron scattering prediction.

## Result

The connected ten-tetrahedron boundary admits a reversible route to two *different metric boundary complexes*: a doubled tetrahedron with two tetrahedral cells, and the boundary of a four-dimensional bipyramid with eight cells.

The route has two distinct ingredients:

1. A rigid hinge motion fixing the existing common triangle ABE, through the exact angle `acos(-1/4) = 104.4775121859 degrees`.
2. Three additional face-pairing switches once the whole tetrahedron ABDE is coincident. They act on ABD, ADE, BDE; the earlier ABE switch stays in place.

The original full-dimensional vertices, edge lengths, all ten cell occurrences, and pairing history are retained. This is not the claim that cell count is particle identity or mass.

At this full-tetrahedron pose, all sixteen possible local pairing patterns are valid closed oriented three-manifold complexes. Fourteen remain connected. The two disconnected patterns are the original 5+5 boundaries and the new 2+8 boundaries. There is **no three-output pattern at this pose** under the retained local switching rule.

The phase calculation constructs a conditional seam-only operator for the products and identifies a separate obstacle to promoting them to independent outgoing channels: four previously retained cycle-comparison links still connect the prospective products. No decay width, conversion probability, or physical speed threshold is assigned.

## Inputs and explicit additions

The supplied boundary-gluing archive provides the marked regular pentachoron, mirrored pair, critical x–w tilt, face occurrences, orientation-compatible triangle switch, retained provenance, and exact chain/link checker. The connected-phase-energy archive provides the native chiral fold formulas and the additional source-cycle comparison matrix.

Both archives are included unchanged and SHA-256 checked. The new result file records their hashes and the inherited source metadata. No GitHub repository file is modified. No outside particle theory is inserted.

New choices or extensions:

- Admit a hinge coordinate for the joined pair, fixing ABE. The predecessor's one-dimensional autonomous contact model does not contain or generate this motion.
- At full tetrahedron coincidence, apply the *same* local triangle switch independently to the three additional coincident faces. No noncoincident faces are silently admitted.
- For the product's doubled tetrahedron, extend the existing full-spinor seam functional to antipodal facet normals using face-specific half-turns. The ABE hinge history fixes the common spin-lift sign; extend that sign uniformly by tetrahedral symmetry. This is an explicit continuation convention, not a new measured phase.
- Keep the distinction between a twenty-coordinate direct sum of boundary phase records and a tensor product of independently occupied physical particles.

## 1. Two different geometric angles

The previous internal tilt was

    delta_c = atan(1/sqrt(5)) = 24.0948425521 degrees.

At that tilt the contact triangle ABE is genuine in the retained four coordinates but projects to a spatial line. The new hinge angle is **not** that tilt and is not a velocity divided by c.

Translate the left body so its ABE centroid is the origin. In units ell its vertices are

    A = (0, 1, 1, -sqrt(6)/3)
    B = (0,-1,-1, -sqrt(6)/3)
    C = (-sqrt(30)/3, 1,-1,0)
    D = (-sqrt(30)/3,-1, 1,0)
    E = (0,0,0,2sqrt(6)/3).

The right body initially reflects the x coordinate. Quotient by the ABE tangent plane. The perpendicular components of the D vertices are

    d_R = ( sqrt(30)/3,-1,1,0),
    d_L = (-sqrt(30)/3,-1,1,0).

Their squared norms are 16/3 and their dot product is -4/3. Consequently

    cos(theta_*) = -1/4.

The exact endpoint hinge rotation on the right body is

    [ -1/4       sqrt(30)/8  -sqrt(30)/8  0 ]
    [ -sqrt(30)/8    3/8         5/8      0 ]
    [  sqrt(30)/8    5/8         3/8      0 ]
    [      0          0           0       1 ].

It is proper orthogonal, fixes ABE pointwise, and leaves the fourth coordinate unchanged. In this pose it is a spatial hinge about the projected AB line, while the complete hidden triangle remains registered.

### Continuous nonoverlap argument

In the perpendicular two-plane, each simplex occupies a wedge of half-width

    alpha = atan(sqrt(3/5)).

Initially the right wedge has angular interval `[-alpha,alpha]`, and the left wedge has `[pi-alpha,pi+alpha]`. Rotating the right wedge by theta leaves an angular gap

    gap = pi - 2alpha - theta.

This is nonnegative for every `0 <= theta <= theta_*`, with equality only at the endpoint. Thus the interiors do not overlap along the path. The same perpendicular plane controls the projected spatial tetrahedra, so the path also respects projected nonoverlap.

For intermediate angles only ABE is shared. At the endpoint A, B, D, E coincide pointwise: an entire tetrahedron ABDE is common. The remaining right vertex C is the reflection of the left C across that tetrahedron's hyperplane.

This is an *admissible path*, not a force law, a generated torque, or a demonstrated scattering trajectory along it.

## 2. Reconnection and the two outputs

A triangle is indexed by its two omitted labels. At the original merger, the omitted pair is C,D and the interface is ABE. The original internal cell adjacencies across ABE have been replaced by

    L_C <-> R_C,
    L_D <-> R_D.

At whole-tetrahedron contact, the additional coincident triangles are:

| Triangle | Omitted labels |
|---|---|
| BDE | A,C |
| ADE | B,C |
| ABD | C,E |

Switch all three while retaining the ABE pairing. Each of the four faces of cell L_C is now paired to the corresponding face of R_C. Those two tetrahedra form a separate doubled tetrahedron.

The remaining eight cells form the external boundary of the two four-simplices glued along ABDE. Since the nonshared vertices lie on opposite normals through the shared tetrahedron's centroid, their union is the explicit convex four-dimensional bipyramid.

| Output | Vertices | Edges | Triangles | Tetrahedra |
|---|---:|---:|---:|---:|
| Doubled ABDE | 4 | 6 | 4 | 2 |
| Bipyramid boundary | 6 | 14 | 16 | 8 |
| Total | 10 | 20 | 20 | 10 |

Both have sphere homology and pass the inherited exact manifold-link and orientation tests. Their sphere topology also has a direct construction: doubling a tetrahedral three-ball along its whole boundary gives a three-sphere; the boundary of the explicit convex four-polytope is a three-sphere.

These are distinct intrinsic metric outputs, not merely counts assigned to species. With the unchanged regular tetrahedral metric, each cell has three-volume `8 ell^3/3`; the product volumes are `16 ell^3/3` and `64 ell^3/3`, instead of `40 ell^3/3` for each original boundary.

The small output's tetrahedra still have nonzero intrinsic three-volume, but their spatial projection has rank two. The doubled complex has two retained sheets occupying the same ambient tetrahedron in this realization. It is not asserted to be an embedded nondegenerate four-dimensional bulk, a stable free particle, or a photon.

The large bipyramid has four-volume `4sqrt(5) ell^4/3`. Its two apices are separated by `2sqrt(5) ell`.

The six orders of the three extra switches all pass the topology checks and reach the same retained final pairing. Their instruction histories can be reversed. Six histories do not imply six times an amplitude or any probability without their phase operators.

## 3. Local completeness and broader census

At full ABDE coincidence there are four eligible triangles. Each has two allowed fixed-orientation pairings. Enumerating the resulting `2^4=16` local patterns gives:

| Local pattern type | Number | Components |
|---|---:|---|
| No crossed faces | 1 | Original 5+5 |
| Nonempty proper subsets | 14 | Connected 10 |
| All four crossed faces | 1 | New 2+8 |

All sixteen are valid closed oriented three-manifold boundary complexes. None has three components.

A broader *combinatorial* audit permits toggling any of the ten label-matched triangles, regardless of current spatial coincidence. Of its 1024 patterns, 834 pass the manifold-link tests and 190 are singular. This larger graph is not an assertion that all its moves can occur at the current contact.

Starting from the original ABE merger, the shortest nontrivial two-output routes take three additional switches. There are two symmetry-related endpoint patterns, each with six switch orders. A chosen hinge direction selects the ABDE family described above.

The shortest three-output endpoints take six additional switches in the abstract valid-pattern graph; they partition the cells as 2+2+6. This is a combinatorial lower bound and a candidate for another geometric construction, not a three-product route admitted at the ABDE pose. Extra energy alone does not satisfy the missing contact incidences.

## 4. Conditional product seam energy

Reuse the native functional

    E_seam(z) = epsilon sum_(i->j) ||z_j - U_ij z_i||^2,
    sum_i ||z_i||^2=1.

All twenty seams and all twenty complex coordinates remain. The right-body chirality, common reference identification, and non-antipodal positive-trace lifts keep the predecessor's conventions.

At coincident tetrahedra the outward four-normals of L_C and R_C are opposite. A shortest normal rotation alone no longer selects a plane or spin lift. Each triangle provides its own tangent plane and hence the complementary half-turn plane. Let n_C be the left cell normal and n_j the other left facet normals. Define

    t_j = (n_j + n_C/4)/sqrt(15/16),
    U_j = +i s_+(n_C wedge t_j).sigma.

The sign matches the continuous ABE fold limit along the hinge; using it on the other faces is the declared uniform tetrahedral convention. Exact checks verify unitarity, normal transfer, fixation of each triangle, and covariance on all six independent four-dimensional bivectors.

The four face conormals sum to zero. Hence `sum_j U_j=0`, so the doubled tetrahedron's seam matrix is exactly

    L_small = 4 I_4.

The other product has a sixteen-dimensional seam matrix. The full product matrix is block diagonal between these two objects. Its small-sector minimum is 4 epsilon; the large-sector minimum is approximately

    0.944737463963210 epsilon.

The complete exact matrices and numerical spectrum are in the JSON. Two eigensolvers and full eigenpair residuals check the large-sector numerical values.

This is **not** a threshold for creating two physical particles. The inherited normalization is a direct sum of cell phase records, not two independently normalized occupied particle states. Taking its minimum can concentrate the record in one component; it does not automatically represent two product rest energies. A different state-space and energy dictionary would need explicit construction.

## 5. The retained cycle links cannot be hidden

The previous autonomous model used native seams **plus** the two original five-cycle comparison terms, `X=2I-T-T^dagger`.

For the 2+8 product partition, four directed cycle comparisons cross between the products:

    L_B -> L_C, L_C -> L_D,
    R_B -> R_C, R_C -> R_D.

The small-to-large block of X has exact rank four and squared Frobenius norm eight. A consistent right-body spin-frame rotation preserves these quantities. Thus simply keeping X unchanged does not give a sum of independent product Hamiltonians at separation.

The script neither silently deletes these links nor presents the seam-only minimum as the full outgoing energy. Turning persistent comparisons off, transporting their information into local records, or retaining an explicit mediating apparatus are changes requiring a common conserved-energy construction.

Consequently the preceding original-topology excitation percentages have **not** been relabeled as recombination probabilities. There is no new output width or absorbing sink in this step.

## 6. Scattering interface and next construction

A genuine product channel would have its own relative-motion coordinate and a joint Hamiltonian containing original, connected, and split sectors under one reference. At any common total energy, an outgoing internal eigenvalue e_F would leave kinetic energy `E_total-e_F`; negative values describe closed channels. But the required final physical internal operator, state preparation and exit coupling are not supplied merely by the two product cell counts or the seam-only audit.

The geometric route is now explicit. The next constructive object is an energy-conserving exit gate that transports the four cross-product comparison records into local retained records as the products separate, while keeping the independently specified hinge dynamics explicit.

No QED assumption, measured branching ratio, fitted geometric tolerance, or threshold in units of c follows from this result.

## Reproduction

    python pentachoron_geometric_split.py

Keep the included `inputs/` directory and `input_hashes.json` beside the script. The script reads the unchanged predecessor archives and writes the full check ledger, exact matrices, local paths, and 1024-pattern census. The analytic wedge argument establishes the continuous nonoverlap statement; the finite-angle samples are supplementary implementation controls, not its proof.
