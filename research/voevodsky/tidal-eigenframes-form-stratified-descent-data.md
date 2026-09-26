# Tidal eigenframes form stratified descent data, not a global preferred frame

## Result

The prior Machian stabilizer result has a concrete fibration interpretation.
Above each real symmetric trace-free tidal tensor sits its space of oriented,
ordered orthonormal eigenframes. Generic fibers contain four sign-related
frames; axial fibers have O(2) freedom; the zero-tensor fiber is SO(3).

Three consequences are now explicit:

1. Spectral projectors give canonical unoriented eigenaxes on the simple-spectrum
   stratum, but not a globally continuous choice of signed eigenframe.
2. Pairwise tensor-preserving overlap maps need not satisfy triple coherence.
   Actual frame comparisons do; arbitrary individually admissible ones may not.
3. At a double eigenvalue, the combined eigenspace projector survives, while
   individual axes have no unique continuous extension from all directions.

These are a kinematic descent model and obstructions. They do NOT establish
nonlinear causal Einstein gluing or a gravitational connection/holonomy law.

## Recovered prior work

- `src/ledger/20260821-1737 Machian Gravity Survives as Stratified Relational Symmetry Reduction.md`
  identifies the surviving physical programme: complete gravitational state,
  causally glued local curvature, then reduction of its residual stabilizer.
- `research/nima/marici-machian-gravity-direction.md`, section 'Local-curvature
  stabilizer correction', already distinguishes generic, axial and flat strata.
- `research/nima/checkers/check_machian_local_tidal_frame.py` checks the generic
  four-sign ambiguity and the continuous stabilizer dimensions 0,1,3.
- `research/aspect/a-berry-eigenline-falsifies-frozen-v10.md` already warns that
  globally defined spectral projectors do not imply a globally trivial frame.
  Its complex Berry-line example is not claimed as this real tidal example.
- `research/nima/table-fibration.md` supplies the general retain-fibers-and-
  totalize pattern. The spectral family below is an additional concrete
  realization, not a derivation of real linear algebra from those table rules.

## The indexed family

Fix an oriented three-dimensional Euclidean observer rest space (V,h). In an
orthonormal reference frame, let B=Sym_0(3,R). Write the real eigenvalues in
nondecreasing order lambda_1(E)<=lambda_2(E)<=lambda_3(E), and define

    F_E = { R in SO(3) : R^T E R = diag(lambda_1,lambda_2,lambda_3) },
    F = {(E,R) : R in F_E},     p(E,R)=E.

This is an indexed family over all B and a locally trivial principal finite
cover over the simple-spectrum stratum. It is NOT an ordinary locally trivial
bundle with a fixed fiber across degeneracies. No global topological fibration
property is asserted there.

For a reference diagonalization, F_E is a torsor for

    H_E = {S in SO(3) : S diag(lambda) S^T = diag(lambda)}.

- Simple spectrum: H_E=V4, the four diagonal sign matrices of determinant +1.
- Axial spectrum: H_E is isomorphic to O(2), embedded as diag(det A,A) when
  the first axis is the simple eigenspace. Its identity component is SO(2),
  but a disconnected component can also reverse the simple eigenaxis.
- E=0: H_E=SO(3).

The full axial group is O(2), not only SO(2). The older continuous-dimension
statement remains correct; this note retains its discrete part as well.
No time axis or observer worldline is selected by this purely spatial model.

## Canonical projectors, not canonical signed axes

For distinct eigenvalues,

    P_i(E) = product_{j!=i} (E-lambda_j I)/(lambda_i-lambda_j).

The projectors satisfy

    P_i P_j = delta_ij P_i, sum_i P_i=I, E=sum_i lambda_i P_i,
    P_i(A E A^T)=A P_i(E) A^T for A in SO(3).

They are continuous on the simple-spectrum stratum and determine unoriented
orthogonal lines. Their denominators expose the gap dependence; no uniform
conditioning near eigenvalue collision follows from their mere existence.

No SO(3)-equivariant full-frame selector can exist even pointwise across all
rotations of one generic tensor: a nonidentity stabilizer element fixes E,
whereas equivariance would demand R(E)=S R(E), impossible for invertible R(E).
Retaining the V4 ambiguity is necessary, not a missing clever formula.

For the actual Newtonian fixture,

    E=diag(-229,74,155)/1728,

all eigenvalues are distinct, so its axes are fixed but its oriented signed
frame still has exactly four choices. No exterior direction is needed to
recover these unoriented axes; an extra reference is needed to resolve signs.

## A loop obstructs a globally continuous signed-frame selector

Let D have three distinct ordered eigenvalues, and let R(theta) rotate about
the third axis. For 0<=theta<=pi, define

    E(theta)=R(theta) D R(theta)^T.

Since R(pi)=diag(-1,-1,1) is in V4, E(pi)=E(0). All points of this closed
parameter loop have the same simple spectrum. A continuous eigenframe lift
must be

    F(theta)=R(theta) S(theta),     S(theta) in V4.

Continuity forces S(theta) constant. Hence

    F(pi)=R(pi) F(0) != F(0).

Therefore this loop cannot support a single-valued continuous signed-frame
section, and neither can the full simple-spectrum base. This holds even
though the ambient Euclidean vector bundle and all the spectral projectors
are globally defined. The obstruction concerns the eigenframe cover.

This is covering-space monodromy of a loop of tensor VALUES. It is not yet
parallel transport along a spacetime loop, a Berry connection, or measured
gravitational holonomy. Relating those notions requires an actual field,
observer/connection and transport law. Frame history can be retained without
claiming that every such sign return is a new physical observable.

## Overlap coherence

Suppose actual chart frames R_i map local coordinates into one already
identified Euclidean space. The coordinate transitions

    g_ij=R_i^T R_j           (j-local coordinates -> i-local coordinates)

obey

    E_i=g_ij E_j g_ij^T,
    g_ij g_jk=g_ik.

Both facts are checked for three nontrivial rational frames of the actual
fixture. For general bundles the same equations are the required descent
conditions on overlaps; they are not manufactured by the spectrum alone.

A hostile is already visible with the SAME generic diagonal tensor on all
three charts. Let

    g_01=I, g_12=I, g_02=diag(-1,-1,1).

Every pair map preserves that tensor, yet g_01 g_12 != g_02. Pairwise
compatibility does not imply a coherent descent datum. Independent chart
reframings conjugate the triple defect and cannot turn a nonidentity defect
into identity without changing the overlap data.

Conversely, g_ij=R_i^T R_j coming from actual retained frames always satisfies
the cocycle. The hostile is not evidence that genuine coordinate changes
fail to compose; it detects fabricated or incompletely certified overlaps.

One can retain local tensors, local frames, overlap maps and triple equations
as a complete package. Forgetting the signed frames projects to the tensor
or projector package. Reconstructing an arbitrary global signed frame from
that quotient alone is blocked by the loop above.

## Degeneration and the correct coarse boundary readout

Let

    D_epsilon=diag(-2,1-epsilon,1+epsilon),  epsilon>0,
    E_epsilon(alpha)=U(alpha) D_epsilon U(alpha)^T,

where U rotates within the last two coordinates. All these paths approach
A=diag(-2,1,1) as epsilon tends to zero. However, the second rank-one projector
along each path is U(alpha) P_2 U(alpha)^T and depends on alpha, independently
of epsilon. Thus there is no continuous extension of that individual ordered
axis at A valid for all these paths.

The simple first-axis projector and the combined plane projector P_2+P_3 do
have an unambiguous limit. The correct intrinsic boundary readout is therefore
one line plus one plane, not a secretly selected pair of axes within the plane.
At E=0 even that splitting is absent. A particular approach history may retain
a limiting frame, but it is extra data beyond the limiting tensor.

This gives a precise retention distinction:

    history-bearing frame -> limiting tensor plus eigenspace clusters

can forget directional information. It is not invertible simply because every
individual nondegenerate tensor has an eigenframe.

## Relation to causal gluing

The original programme asks for actual local gravitational solutions and their
causal boundary agreements. This note handles only the induced frame layer.
It presupposes that the local spatial fibers have already been identified on
overlaps, so it does not construct the Lorentz/spacetime gluing itself.

A candidate causal solution gluing should induce tensor transitions obeying
the first overlap equation, with composition obeying the second. Its spectral
readout should retain sign-transition data on generic strata and eigenspace
clusters at collisions. Whether a spacetime history realizes the value-space
loop or a degeneration path is a separate dynamical existence question.

The next scientifically useful input is an actual existing family of local
solutions and their observer transport, not an assertion that these abstract
matrix overlaps already solve Einstein constraint/evolution gluing.

## Verification

Run:

    python research/voevodsky/check_tidal_eigenframe_descent.py

All 23 exact Fraction controls passed. They cover the actual tidal fixture,
projector identities and rotation naturality, four sign choices, tensor overlap
and triple coherence, the hostile triple, loop endpoints, axial degenerations,
cluster retention, disconnected axial symmetry and flat symmetry.

Receipt: `research/voevodsky/tidal-eigenframe-descent.json` includes source hashes.
The all-loop no-section proof and all-epsilon degeneration argument above are
written mathematics. Finite checks supplement them; no new Agda topology proof
or physical curvature-transport theorem is claimed.
