# Native phase comparisons for actively strained pentachora

Date: 2026-10-11  
Status: Conditional geometric and finite phase-record reconstruction. **Not a new electron–positron scattering prediction.**

## 1. Result and inherited boundary

The preceding axial-deformation calculation changed the entrance comparison cost and its active patch, but deliberately held all native phase matrices fixed. Its section 8 already derived the changed ABE sewing phase. The present calculation carries the prescribed strain through every native face projector and full-spinor fold at ABE, then through the two rigid hinge endpoints and all eight final pairing configurations.

Three effects are now explicit:

- Equal-face local readout no longer preserves the cell-spinor norm. Actual face areas supply an exact isometric continuation.
- Compression changes the additional faces' selected-line overlaps and splits the doubled-tetrahedron's previously equal seam-energy levels.
- The old five-cycle cannot remain a geometric symmetry of one fixed compressed shape. A checked geometric continuation retains five different compression-axis configurations instead.

No new full entrance-to-product flux is calculated. In particular, the preceding flux table is not relabeled as the result of these rebuilt operators.

## 2. Provenance and explicit choices

The unchanged `inputs/pentachoron_axial_deformation_bundle.zip` is the sole archive input. Its SHA256 is

    9ae458bf376749df53a2e8a7ba521d40f67f8aa81c303184f5b183d1ea9277a6.

The checker verifies that archive, its file manifest, the nested open-product manifest, and the compact source payload hashes. The source supplies marked vertex coordinates, oriented face occurrences, native phase matrices, the hinge generator, and the original material-cycle matrix. Ancestral topology or physical-identification claims are not reverified by this hash audit.

Inherited conventions:

- Active compression C_lambda=diag(lambda,1,1,1), with fixed Euclidean metric and 0<lambda<=1.
- Opposite chiralities in the supplied common reference frames.
- Positive-trace shortest normal folds, with the source's full-spinor extension across bodies.
- Equal positive coefficient epsilon on the full-spinor seam residuals; epsilon is uncalibrated.
- All twenty cell-spinor coordinates and all twenty seams retained in each topology.

New or clarified choices:

1. Normalize the chiral bivector of each actual, generally irregular triangle, rather than divide every face by the old regular-face constant.
2. Use face-area scalar weights in the local selected-line encoder. This is an isometric continuation; it does not assign face-transition probabilities or replace the equal seam-energy coefficients.
3. Freeze the deformed shape at ABE, then move it by rigid hinge rotations. The material strain rotates with each body. This is NOT continuous re-compression along a fixed laboratory axis during the hinge.
4. Continue the antipodal face-half-turn signs continuously from the source at lambda=1. A distorted tetrahedron no longer has the full regular tetrahedral symmetry formerly used to motivate one common sign.
5. Audit the old cycle term X separately as a retained material-history control. It is not called a newly derived fixed-pose geometric symmetry.
6. Construct a separate enlarged configuration family carrying compression-axis orientation, to realize the old cycle geometrically. Its added configuration coordinate has no derived kinetic cost or incident preparation here.

There is no lambda(v), externally fitted branching fraction, QED interaction, physical particle mass, or energy-to-speed calibration.

## 3. Rebuild actual face geometry

For a simplex's outward normal nu_c, active compression gives

    nu_c(lambda) = C_lambda^(-T) nu_c /
                   ||C_lambda^(-T) nu_c||.

The implementation checks these normals independently against tangent-nullspace normals reconstructed from the strained vertices. Using the regular formula 'normal proportional to negative vertex displacement' directly on a nonregular simplex would be wrong.

For an oriented triangle, let b=u wedge v be the full edge bivector. Its area is A_f=||b||/2. In the inherited chiral convention,

    s_eta(b)=(b_yz+eta b_xw, b_zx+eta b_yw, b_xy+eta b_zw),
    n_f=s_eta(b)/(2 A_f),
    P_f=(I-n_f.sigma)/2.

Because b is a simple bivector, ||s_eta(b)||=||b||. Each P_f is a rank-one orthogonal projector. The old 4 sqrt(3) denominator is valid only for the regular faces (and for ABE, which is not tangentially strained here).

### Area-normalized local encoder

For a tetrahedral cell c, oriented face closure gives

    sum_f A_cf n_cf=0.

Consequently

    J_c z = [sqrt(2 A_cf / sum_g A_cg) P_cf z]_f,
    J_c^dagger J_c=I_2.

At lambda=1 every face area is equal and this recovers the original P_f/sqrt(2) encoder. At lambda=0.5 the maximum error of the old equal-face Gram operator is approximately 0.07733 in operator norm. The new area's Gram residual is at floating precision; the closure identity is also checked symbolically for arbitrary positive lambda.

These weights are uniquely fixed within the restricted class of scalar weights on the same four rank-one face projectors: sum w_f=2 and sum w_f n_f=0. This does not establish uniqueness among all possible encodings, interactions, or amplitude laws.

## 4. The ABE phase and a shorter rigid hinge

The previous sewing coefficient is recovered by rebuilding the actual folds:

    mu_lambda=(sqrt(5)lambda+i sqrt(3))/sqrt(5lambda^2+3),
    |mu_lambda|=1.

The exposure tilt remains delta_c=atan(1/sqrt(5)). ABE has its original intrinsic area and a spatially projected line.

For the rigid continuation specified in section 2, the two D-apex components perpendicular to ABE are

    d_R=(lambda sqrt(30)/3,-1,1,0),
    d_L=(-lambda sqrt(30)/3,-1,1,0).

The angle taking one to the other is

    theta_*(lambda)=2 atan(sqrt(5/3)lambda),
    cos(theta_*)=(3-5lambda^2)/(3+5lambda^2).

At that endpoint an entire ABDE tetrahedron coincides. The negative hinge direction gives the corresponding ABCE route. These are the same retained combinatorial 2+8 routes, now with distorted cell metrics. Common-tetrahedron coincidence is checked directly in both directions.

In the perpendicular plane, each simplex wedge has half-width atan(sqrt(3/5)/lambda); the open angular gap is pi minus twice that half-width minus the hinge angle. It remains nonnegative up to theta_*. This proves that the admitted rigid path has no overlapping interiors before its endpoint. It does not provide a driving torque or a collision trajectory.

| lambda | ABE fold phase | Required rigid hinge angle |
|---:|---:|---:|
| 1 | 37.761244 deg | 104.477512 deg |
| 0.75 | 45.924286 deg | 88.151428 deg |
| 0.50 | 57.157870 deg | 65.684261 deg |
| 0.25 | 72.112587 deg | 35.774826 deg |

The identity theta_*+2 arg(mu_lambda)=pi is geometrical. Neither angle is a speed or a measured particle parameter.

The connected native seam matrix along this RIGID path still satisfies

    L_C(theta,lambda)=F(theta)L_C(0,lambda)F(theta)^dagger.

A shorter path does not imply a new downhill eigenenergy force. Updated kinetic geometry and actual phase preparation would still be needed for dynamics.

## 5. A local sewing magnitude from projected versus hidden area

On a crossed face at full-tetrahedron contact, keep the source's opposite-chirality comparison and geometric fold U. Define c_f by

    (P_R U P_L)^dagger(P_R U P_L)=c_f P_L.

The fold fixes the triangle, hence acts by a phase on its selected incoming line. With the opposite induced face orientations, the chiral formula gives

    c_f = sum_i b_iw^2 / ||b||^2
        = 1 - (A_spatial_projection/A_intrinsic)^2.

This is a squared local selected-line amplitude. Its complementary component 1-c_f is retained by the full-spinor operator. It is NOT an entire recombination probability, nor an interpretation of w as physical complex space.

For the positive hinge route,

    c_ABE=1,
    c_ABD=1/(4+5lambda^2),
    c_ADE=c_BDE=(13+15lambda^2)/[4(4+5lambda^2)].

| lambda | c_ADE=c_BDE | c_ABD |
|---:|---:|---:|
| 1 | 0.777778 | 0.111111 |
| 0.75 | 0.786697 | 0.146789 |
| 0.50 | 0.797619 | 0.190476 |
| 0.25 | 0.807971 | 0.231884 |

All three additional faces still have c_f<1 for every positive lambda. Their formal limits as lambda tends to zero are 13/16,13/16,1/4, not perfect matching. Lambda=0 itself is excluded because the four-simplex collapses. Thus this strain does not repair the strict selected-line sewing obstruction. The earlier full-spinor switching extension remains substantive model input.

The formulas are checked symbolically using the actual triangle wedges, and independently through rebuilt spinor projectors and fold matrices on both incident seams.

## 6. Compression splits the small product's seam energies

Continue the same full-spinor mismatch functional,

    E_seam=epsilon sum_(i->j) ||z_j-U_ij z_i||^2.

Area weights in J_c normalize readout only; they have NOT been substituted for the inherited equal seam-energy weights.

For the small doubled tetrahedron, ABE has area 2 sqrt(3) ell^2 and the other three faces have area

    A_side=(2/sqrt(3)) sqrt(4+5lambda^2) ell^2.

Face closure implies that the sum of the four UNIT conormals no longer vanishes. Its magnitude is

    d(lambda)=3/sqrt(4+5lambda^2)-1.

The four continued half-turn maps are i times the associated Pauli directions. The small operator consequently has the exact spectrum

    epsilon [4-d(lambda)], multiplicity 2,
    epsilon [4+d(lambda)], multiplicity 2.

Equivalently its characteristic polynomial is

    [(x-4)^2-d(lambda)^2]^2.

| lambda | Small seam level / epsilon | Other small seam level / epsilon | Large seam minimum / epsilon |
|---:|---:|---:|---:|
| 1 | 4.000000 | 4.000000 | 0.944737 |
| 0.75 | 3.850608 | 4.149392 | 0.930422 |
| 0.50 | 3.690693 | 4.309307 | 0.944775 |
| 0.25 | 3.555370 | 4.444630 | 1.023295 |

The small formula is analytical; the large minimum is numerical with independent eigensolver and eigenpair checks. These are normalized direct-sum phase-record energies. They are not independently occupied product rest masses, binding energies, or production thresholds. Persistent source-cycle terms still need the treatment below and the inherited memory construction before physical outgoing independence could be claimed.

Original and connected seam matrices are also rebuilt from all twenty links. The source unstrained matrices are recovered. Strain splits their degeneracies and changes their spectra even though the seam count remains fixed. Full matrices and spectra are saved in the NPZ/JSON.

## 7. The old five-cycle needs a compression-direction record

At ABE the original marked cycle sends edge AB to BC. The actual strained squared lengths are

    |AB|^2=8 ell^2,
    |BC|^2=(14+10lambda^2)ell^2/3.

They agree only at lambda=1. Therefore that label cycle is not an isometry of the fixed actively compressed simplex. Its unique affine realization C_lambda R C_lambda^(-1) remains a five-cycle, but is not Euclidean orthogonal. The old spin matrix still exists as an abstract unitary; it no longer supplies the same geometric covariance at this fixed pose.

There is an explicit geometric continuation if compression-axis orientation is retained. For a unit axis n define

    C_lambda(n)=I+(lambda-1) n n^T.

For the original proper rotation R,

    R C_lambda(n)=C_lambda(R n) R.

Thus one cycle arrow carries BOTH the vertex/cell label and the strain direction. It moves between the five configurations n,Rn,...,R^4n and closes after five operations. It does not secretly preserve one laboratory-axis deformation.

The checker constructs the corresponding fifty-coordinate single-body record (five pose records, five cells, two spin coordinates), retaining the source spin lift. Its cycle is unitary, has fifth power -I, and intertwines the rebuilt native seams. This is a new configuration-register extension, not five new particles or a derivation of the register's dynamical occupation/energy cost. At lambda=1 the distinct metric configurations coalesce, so adding the register is not presented as an unchanged minimal source representation.

For comparison only, the receipt also evaluates L_O(lambda)+X_reference and L_C(lambda)+X_reference. They are positive, valid material-history operators but not fixed-shape geometric-cycle operators. The old reference cycle no longer commutes with the strained original seams. A finite forty-coordinate pulse is checked with that declared control; its temporary connected occupation is explicitly not new outgoing product flux.

## 8. Why the previous incoming scattering preparation cannot be reused silently

The source compresses after the material x-w tilt. Rebuilding its native seams at different tilts changes the spectrum. At lambda=0.5:

| Material tilt | Original seam minimum / epsilon |
|---:|---:|
| 0 deg | 1.501019 |
| 24.094843 deg | 1.514772 |
| 45 deg | 1.448643 |
| 90 deg | 1.213700 |

A change of spin frame cannot remove an eigenvalue change. Thus a full phase update requires coupled tilt–phase incoming eigenmodes rather than the old free rotor times a constant native-ground vector. Corresponding kinetic/frame conventions and the cycle-axis record must be specified together. Changing just mu_lambda in the old solver would not complete this task.

## 9. Verification and reproduction

The default run passes 319 named checks: 41 symbolic identities, 266 numerical checks, 9 negative controls, and 3 provenance groups. The numerical groups include positive spectra without residual fields as well as residual-bounded identities.

Tests cover inverse-transpose normals versus independent tangent-nullspace normals; face-area closure; isometric local encoders and uniqueness within scalar weighting; unitary folds and covariance on all six bivectors; ABE selected-line sewing; both endpoint geometries and all eight native pairing matrices; exact face-overlap formulas; the small-product spectrum; matrix Hermiticity/positivity; original-source recovery; independent eigensolvers and phase propagation; rigid hinge covariance; a passive-coordinate/metric control; and the enlarged geometric cycle.

The largest recorded numerical residual is approximately 2.91e-12, in near-endpoint hinge covariance at lambda=0.1. These are numerical algebra diagnostics, not spatial-scattering convergence errors or experimental uncertainties. No scattering-grid refinement, full flux scan, or new physical correspondence is claimed.

Run:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python pentachoron_strained_phase.py

The unchanged source archive is safely extracted to `.source_cache/` after its manifest is checked. Dependencies: Python, NumPy, SciPy, SymPy. No network access, repository modification, or experimental calibration is used.

## 10. Next constructive connection

The native strained projectors, folds, local normalization, product spectra, and geometric cycle continuation are now explicit. The next scattering update should first construct the incoming joint tilt–phase/strain-direction modes, then use the consistent interface and kinetic operators throughout the full route. A law generating lambda from incoming momentum, and the work of preparing or maintaining strain, remain separate missing dynamics. No new speed threshold, photon channel, three-product path, or 372:1 prediction follows here.
