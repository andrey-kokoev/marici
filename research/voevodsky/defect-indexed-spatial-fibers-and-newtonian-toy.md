# Defect-indexed spatial fibers and the Newtonian toy

## Result

The earlier spatial metric reconstruction and Nima's Newtonian fixture admit
one explicit mathematical realization: a family of Euclidean spatial vector
spaces indexed by timelike momentum-defect directions. The original potential,
gradient and tidal tensor are recovered in one fiber, and transporting both
sources and frame by a Lorentz isometry preserves their spatial readouts.

This is a conditional bridge, not a derivation of Newtonian physics from the
new table-fibration primitive. In particular, a momentum-space metric is not
by itself a physical position-space metric with length units.

## Recovered sources

- `src/ledger/20260814-124 Spatial Geometry from the Cosmological Defect.md`
  (Nima and Benincasa): Q=sum_i p_i is a non-null total momentum defect,
  timelike in the cosmological region. Orthogonal projection reconstructs the
  spatial Gram metric from the ambient Lorentzian pairing. This is a written
  linear-algebra argument, not a machine-checked continuum theorem.
- `research/nima/table-fibration.md`: grouping retains the coordinate selector,
  rows and membership witnesses; totalization recovers the original rows.
- `research/nima/newtonian-tidal-rrc-bridge.md` and
  `research/nima/newtonian-two-route-comparison.md`: the Newtonian field is a
  supplied model whose fixed tidal calculation and route comparison are checked.
- `research/nima/checkers/check_machian_newtonian_localization.py`: the source
  fixture and exact potential/gradient/Hessian readout.

Use D for the momentum defect below, reserving Q for retained packages. No
identification of those two meanings is established by shared notation.

## 1. The spatial family

Supply a four-dimensional real vector space V with Lorentzian form g of
signature (-,+,+,+), and a time orientation. Let B be its future timelike cone.
Define

    Spatial = {(D,v) : D in B, g(D,v)=0},
    p(D,v) = D.

The fiber H_D=D^perp is three-dimensional. Its inherited metric is positive
definite: in a Lorentz orthonormal frame with D=(d,0,0,0), its vectors have
vanishing time component and g restricts to the sum of three squares.

For arbitrary v in V, set

    P_D(v) = v - g(v,D)/g(D,D) D,
    h_D(v,w) = g(v,w) - g(v,D)g(w,D)/g(D,D).

Then P_D^2=P_D, its image is H_D, and

    h_D(v,w)=g(P_D(v),P_D(w)).

On all of V, h_D is degenerate with kernel span(D); it is a Euclidean metric
only after restriction to H_D (or passage to the corresponding quotient).
The spatial metric is not a new independent primitive given g and D.
The number three comes from the supplied ambient dimension four.

Scaling D by a positive nonzero scalar leaves P_D and H_D unchanged. Thus this
spatial family descends to future timelike rays, equivalently to normalized
unit timelike vectors. The magnitude of the momentum defect is forgotten by
this geometric readout; retain it separately if needed.

This is a smooth vector-bundle realization of the indexed-family idea. We
have not added an Agda encoding of real manifolds or identified it with all
rules of the existing Q calculus.

## 2. Comparing fibers

For a Lorentz isometry Lambda carrying D to D',

    P_D' Lambda = Lambda P_D,
    g(Lambda v,Lambda w)=g(v,w).

Consequently Lambda restricts to an isometry H_D -> H_D'. For different defect
magnitudes one can instead compare normalized directions.

Endpoints alone do not specify WHICH Lorentz isometry was used. If R fixes D,
then Lambda and Lambda R have the same defect endpoint but generally different
spatial actions. At normalized D, the proper spatial stabilizer is SO(3).
This is residual frame freedom, not a failure of the metric reconstruction.

The ambient structure does allow an extra useful convention: the rotation-free
boost in the plane of two unit timelike directions, fixing its orthogonal
complement. It need not agree with composition through a third direction;
non-collinear boost composition can include a spatial rotation. This note
neither checks such loops nor equates their rotations with gravitational tides.

Naively projecting a vector from H_D onto H_D' is generally NOT an isometry.
The exact checker exhibits this: with a boost of gamma=5/4 in the x direction,
the projection of the old unit x vector has squared norm 25/16 in the new fiber.
A transport convention or retained isometry is therefore needed for comparisons.

## 3. Newtonian fields within a fixed fiber

To interpret H_D as physical displacement space, SUPPLY an affine position
space A_D modeled on it, an origin for the fixture, length units and a time
parameter for acceleration. This is an explicit physical interpretation of
an isomorphic Euclidean vector space, not an identification of momentum units
with length units. Alternatively an independently specified position space
can be equipped with a metric pulled back through an authorized identification.

For source positions r_alpha in A_D, masses m_alpha and coupling G, assume

    Phi_D(x) = -G sum_alpha m_alpha / ||x-r_alpha||_h.

Away from the sources, using the flat affine derivative associated with this
Euclidean space, its Hessian is

    E_D(v,w) = G sum_alpha m_alpha [
        h(v,w)/R_alpha^3
        - 3 h(x-r_alpha,v)h(x-r_alpha,w)/R_alpha^5 ],
    R_alpha = ||x-r_alpha||_h.

The Hessian is a bilinear form; relative acceleration uses its raised-index
endomorphism:

    delta a = -h_D^{-1} E_D(xi, -) + O(||xi||^2).

In an orthonormal frame this is the familiar matrix equation -E xi.
In a nonorthonormal frame omitting the inverse metric is incorrect.

For D=(2,0,0,0), G=1, masses 2 at 3e_1 and 1 at 4e_2, evaluated at the origin,

    Phi = -11/12,
    grad Phi = (-2/9, -1/16, 0),
    E = diag(-229,74,155)/1728.

Thus trace_h E=0, while the tidal tensor is nonzero. The linearized relative
acceleration for xi=e_1 has x component 229/1728. This is a derivative-level
coefficient, not an exact finite-separation acceleration difference.

Transporting D, source displacement vectors and the orthonormal frame together
by Lambda preserves all the inner products in this formula. It therefore
preserves potential, frame components of gradient, and frame components of E.
This is covariance of Euclidean spatial models under supplied isometries,
NOT Lorentz covariance of Newtonian time evolution or a relativistic boost of
a source worldline solution. There is no time evolution in this test.

## 4. Two distinct fibrations

    Spatial -> timelike defect directions

organizes spatial vectors and their metrics. Within a spatial fiber,

    local second jets -> tidal Hessians

organizes potential data by their affine-invariant readout: adding c+b(x)
changes the potential and gradient but not the Hessian. These are distinct
base spaces and distinct forgetful operations.

The momentum defect D selects a rest-space direction. The tidal tensor E is
spatial variation of acceleration. Neither is a literal Q^4-Q, and no equality
between them is claimed. A homogeneous flat fiber can carry a nonzero tidal
field: Euclidean intrinsic curvature and Newtonian tidal curvature are not
being identified.

## 5. Verification and remaining inputs

Run:

    python research/voevodsky/check_defect_spatial_newtonian_bridge.py

The standard-library Fraction checker passed 20 exact finite checks, including:
projector laws, scaling invariance, Lorentz naturality, inherited radii,
recovery of all three original jet readouts, transported tidal components,
residual frame ambiguity, failure of naive projection to preserve lengths,
and rejection of null/zero/spacelike defect inputs. Wrong tidal sign and
forgetting the boosted time component are also detected.

Receipt: `research/voevodsky/defect-spatial-newtonian-bridge.json`.
It records source hashes. The fixture is explicitly repeated from Nima's
checker and compared with its saved output, not independently extracted or
recomputed through its implementation. These are finite exact arithmetic tests;
the universal arguments above remain written mathematics, not Agda proofs.

Still supplied: ambient Lorentzian dimension/signature, timelike defect, the
position-space interpretation and units, source locations/masses, Newtonian
potential (or Poisson plus its hypotheses), acceleration coupling and any
inter-fiber transport convention. No cosmological source configuration is
shown here to generate the specific two Newtonian point sources.

## Next discriminating question

Does the original sourced kinematics provide an authorized position/displacement
realization and a rule for comparing rest spaces, rather than merely a spatial
momentum Gram matrix? That is the missing bridge to investigate before claiming
that the physical spatial geometry of the Newtonian toy has been derived.
