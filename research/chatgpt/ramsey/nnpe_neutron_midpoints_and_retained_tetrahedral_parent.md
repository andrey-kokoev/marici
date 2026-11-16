# NNPE continuation: a retained midpoint parent for the actual neutron geometry

Date: 2026-11-02.

## Result

The actual six-vertex neutron geometry admits a labelled inverse-midpoint construction of a four-vertex tetrahedral parent. No neutron vertices are identified. Its native simultaneous C3 action lifts exactly to the four reconstructed vertices: one is fixed and the other three cycle. This avoids the preceding obstruction to identifying two rim edges while demanding that the original action descend to the quotient.

The geometric route already exists in `research/voevodsky/signed-belt-tetrahedral-parent.md`. That source constructs a regular parent in four-dimensional coordinates, takes its medial octahedron, projects it and selects six side panels. The present audit reuses its geometry, works in the inverse direction from the actual neutron input, retains every comparison residual, and constructs the larger parent's full proper action explicitly. It does not rerun or import that source's separate 312-transfer spinor identification into the 1,836-transfer scalar neutron model.

The construction has two substantive limits. In the inherited spatial metric the reconstructed parent is not the regular proton fixture. The two scalar residual coordinates of midpoint reconstruction also vanish on the actual geometry and on the preceding coherent three-mode coefficient packet. Reconstructing this parent does not, by itself, generate any extra nonzero output record, much less a lepton pair.

## 1. Inputs and provenance

Fresh connected-repository reads:

- `research/voevodsky/inputs/mode-neutron.json`.
- `research/voevodsky/inputs/relative-proton.json`.
- `research/voevodsky/signed-belt-tetrahedral-parent.md`.
- `research/voevodsky/checkers/check_signed_belt_tetrahedral_parent.py`.
- `research/strominger/neutral-connector-prior-clues-v1.md`, used only to check that geometric, scalar-neutron and signed-spinor branches are distinct.

The two complete input JSONs are bundled. They were inherited from the preceding attached audit and compared with the freshly returned complete source objects. The new checker reconstructs all of its matrices from those inputs. No repository write, upstream proof-assistant compilation, full geometry-producer run, 312-transfer checker replay or 1,836-transfer model reconstruction is claimed.

The predecessor is `nnpe_successful_closure_coherence_and_native_geometry.md`. Its C/R completion actions are retained as the explicitly proposed coefficient-operation family, not recast as pre-existing native neutron generators.

## 2. Inverse midpoint construction

Generate the actual upper orbit u0,u1,u2 from the first native seed and rotation. The lower orbit is -u0,-u1,-u2. In the native rational coordinates and spatial metric diag(3,1,1):

    u0 = (0,7/20,1)
    u1 = (-1/2,7/20,-1/2)
    u2 = (1/2,7/20,-1/2).

Form:

    t0 =  u0+u1+u2
    t1 =  u0-u1-u2
    t2 = -u0+u1-u2
    t3 = -u0-u1+u2.

Every original point is recovered as a labelled edge midpoint:

    (t0+t1)/2 =  u0       (t2+t3)/2 = -u0
    (t0+t2)/2 =  u1       (t1+t3)/2 = -u1
    (t0+t3)/2 =  u2       (t1+t2)/2 = -u2.

The native rotation fixes t0 and cycles t1,t2,t3. It preserves the incidence map and its inverse. A correspondence between vertices and edge-midpoint records is not a quotient identifying vertices.

The six-point incidence is supplied by the existing medial-parent construction. In particular, assigning the upper cap to the star of t0 is a retained binding, not a claimed physical choice. Exhausting all 48 assignments of the three antipodal pairs to opposite tetrahedron edges gives exactly two unlabelled parents, t and -t, each with 24 vertex-labelled versions. The source's cap/orientation mark must not be discarded when a specific version is used.

The native lower-orbit indexing is defined by applying the actual rotation repeatedly to the second seed. The older belt drawing uses a different naming order for two lower points. The comparison is made through explicit coordinates and edge incidences, not equality of those display names.

## 3. A lossless map for arbitrary scalar records

Put the six edge records in order (01,02,03,12,13,23). Let M be the 6-by-4 midpoint matrix, with 1/2 at each edge's endpoints. Its rank is four. Define

    K = (M^T M)^-1 M^T
    v = K m
    r = (I6-MK)m.

Then, for every six-entry scalar record m,

    m = Mv+r,
    M^T r = 0,
    ||m||^2 = v^T(M^T M)v + ||r||^2.

This is an invertible retained decomposition into a four-dimensional vertex-coordinate record and a two-dimensional residual, with their actual induced metrics. It is not a six-to-four lossless map after the residual is removed.

The left inverse is particularly simple:

    v_i = sum_{edges incident on i} m_edge - (1/3) sum_{all edges} m_edge.

The residual vanishes exactly when

    m01+m23 = m02+m13 = m03+m12.

A residual basis is

    z1=(1,0,-1,-1,0,1)
    z2=(0,1,-1,-1,1,0),

with induced metric [[4,2],[2,4]], not an independently chosen identity metric. The decomposition is covariant under every one of the 24 tetrahedron vertex permutations and their induced edge permutations. The code verifies the full matrix identities, so it covers arbitrary records rather than a finite list of numerical states.

All opposite sums of the actual neutron geometry are zero. The preceding coherent coefficient packet, after the explicitly stated edge reordering, is

    m=(a,b,c,-c,-b,-a),

and also has zero residual identically. Thus neither input forces an additional record to be populated. The residual representation factors through the ordinary S4 edge action; the three double transpositions act as identity. No spinor or particle interpretation is inferred from its dimension two.

Type boundary: this is a decomposition PER SCALAR coordinate. Applying it to six spatial points gives twelve reconstructed vertex coordinates and six residual coordinates, all residuals zero here. These counts are not dimensions of the original neutron's 36-complex-coordinate state or its physical output Hilbert spaces. Applying the same matrix algebra to the earlier coefficient packet is a separate explicitly labelled comparison.

## 4. Exact spatial metric comparison

Let U have columns u0,u1,u2 and write a geometric position as Uc. Its inherited metric in c-coordinates is

    G_N = U^T diag(3,1,1) U
        = (3/2) I3 - (151/400) J3,

where J3 is the all-ones matrix. This is positive definite. Its common-direction eigenvalue is 147/400; both transverse eigenvalues are 3/2.

The four reconstructed parent vertices are

    (0,21/20,0), (0,-7/20,2), (-1,-7/20,-1), (1,-7/20,-1).

Their squared spatial edge lengths are

    149/25, 149/25, 149/25, 12, 12, 12.

They are not a regular tetrahedron in the existing neutron metric. The source proton fixture has all squared edge lengths eight. The preceding regular coefficient-state orbit used a different metric; it cannot be silently substituted for this geometric metric.

Among the twelve proper tetrahedral actions generated by the previous C and R^2, exactly three preserve G_N: the existing cyclic subgroup. R^2 and both matched native proton generators fail the fixed-G_N isometry check. Thus exposing the geometric parent alone does not license the larger metric-symmetry action.

## 5. Recovered regular lift and its full action

Retaining the base edge scale and requiring a regular parent forces the invariant coefficient-position metric to be (3/2) I3. The required correction is

    G_parent-G_N = (151/400) J3.

It is positive, rank one. One added Euclidean coordinate suffices:

    z(c) = sqrt(151)/20 * (c0+c1+c2).

On the four sign-pattern vertices it is 3 sqrt(151)/20 at the apex and -sqrt(151)/20 at each base vertex. This recovers exactly the existing signed-belt tetrahedral-parent recipe. The lifting coordinate is part of a declared mathematical representation, not a claim about an extra physical spatial dimension or a new particle.

The regularity conclusion is conditional on the specified base scale and regular-parent requirement. Neither regularity nor the energy needed for a physical metric change is derived from a neutron dynamics. The coordinate is determined by the supplied geometry, but its inclusion changes the norm contract; information recoverability does not establish energy conservation.

The audit also constructs all twelve proper actions on the complete four-coordinate ambient representation. Let

    L = stack(U, [1,1,1])
    G4 = diag(3,1,1,151/400)
    Lsharp = (L^T G4 L)^-1 L^T G4
    P = L Lsharp.

For each proper three-coordinate tetrahedral action g, set

    Tg = L g Lsharp + I4-P.

Then

    Tg L = L g
    Tg^T G4 Tg = G4
    Tg Th = T_(gh).

The complementary ambient direction is retained and fixed, not deleted. The actual native C3 action extends exactly as diag(C_native,1). This supplies an explicit consistent incidence/action parent, not merely a matching vertex count. All 144 pairwise group-composition identities pass.

The lifted parent has squared edge length twelve. To match the native proton metric at edge length eight requires the explicit overall length factor sqrt(2/3). This is a geometric normalization, not a mass, amplitude or energy derivation. Equivalently, before that rescaling the affine pullback metric is exactly (3/2) times the supplied proton metric.

## 6. Consequence for competing successful realizations

The common-parent question has a constructive answer at the labelled geometric level: the native neutron belt and a regular tetrahedral parent can be represented through midpoint incidence and the already documented lifted metric, without merging neutron vertices or corrupting an operation. The source's simultaneous rotation is retained in that construction.

This does not yet construct the NNPE re-pairing as a native state-changing operation. A rule realizing the proton candidate must also account for the chosen metric/normalization and the change of field encoding, rather than merely reinterpret six points as four. The signed-belt parent's separate normalized spinor protocol is not the original scalar neutron protocol.

Most importantly, the retained midpoint comparison supplies no compulsory nonzero two-coordinate remainder on the actual input. It would be unjustified to call that zero remainder an electron or an antineutrino. A full outgoing product construction must obtain its nonzero states from an actual source operation and their independently bound output types. The current result supplies an incidence/action bridge and an exact limit on what that bridge alone accomplishes. It introduces no failure event or error probability and selects neither a decay rate nor a branch frequency.

## Reproduction

    python retained_midpoint_audit.py

Requires Python 3.10+ and SymPy. The completed run passes 340 named exact checks, including all 24 incidence symmetries, 48 antipodal edge assignments, twelve lifted proper actions, 144 action-composition identities, both source metric comparisons, inverse/retention identities, and zero-residual controls. Exact rational arithmetic is used throughout; the one square root is recorded symbolically through its squared metric coefficient.

No full upstream theorem/checker replay or repository mutation is claimed. `results.json` contains all matrices, action tables, checks and input hashes. `run.log` contains the completed run. The mathematical tests are independently executed here; the source's prior scientific claims are not promoted beyond their stated scope.

## Source locators

- https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/signed-belt-tetrahedral-parent.md
- https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/checkers/check_signed_belt_tetrahedral_parent.py
- https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/inputs/mode-neutron.json
- https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/inputs/relative-proton.json
- https://github.com/andrey-kokoev/marici/blob/main/research/strominger/neutral-connector-prior-clues-v1.md
