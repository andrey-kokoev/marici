# Does the actual triangle circuit implement the hidden-contrast response?

## Fresh sources

Inspected the three-stage construction in `check_twelve_triangle_positive_geometry.py`, the native-composition audit, and `NativeTableRules.agda`'s actual `compose-comparisons` definition. The question is whether the previously tested nonlinear covariance response is already implemented by these ports, not whether an additional formula could detect the contrast.

## Exact restriction to the relevant mode sector

The twelve local source vectors obey v_i=R_i v_0. Represent a prepared field in this invariant subspace by its twelve coefficients a_i:

    x_i=a_i v_i.

Local selection acts as the identity. The symmetry block R_i R_j^T/12 gives

    (Sx)_i=v_i * (sum_j a_j/12).

The collective projector has the same action on this subspace. Thus the actual stages restrict exactly to I, M, M, where M_ij=1/12 and M^2=M.

Every finite word in these stages is I or M. Even allowing linear combinations gives only span{I,M}. This is a statement about the fixed stage operators, not all operations constructible in the native calculus or all individually marked graph paths.

## The needed response is not one of these operators

For the AB/BA contrast, let D(a) be diagonal with entries +1,-1 on those slots and zero elsewhere. Exact tests show [M,D(a)] is nonzero. Hence D(a) is outside the commuting two-dimensional stage algebra.

If this extra state-dependent gate were supplied, the two schedules would differ:

    M D(a) D(a) M = M/6,
    M D(a) M D(a) M = 0.

The first measures retained same-slot correlation before averaging; the second loses the contrast between factors. The actual source circuit supplies neither amplitude-dependent D(a) gate. Its fixed matrix multiplication is not multiplication of two state amplitudes.

The number 1/6 remains a correct quadratic diagnostic of the trial data. Doubling the prepared amplitude makes it 2/3. A nonlinear observer can read it from retained records without changing those records. Turning that observation into a state update or binding interaction is the missing operation.

## Native comparison does not automatically supply that operation

The native rule receives two pointed equivalences through the same middle package. It composes the equivalences and their value-preservation witnesses, retaining both parents. It has no instruction to convert these particular triangle amplitudes into local response gates, multiply them at common triangle slots, or choose the uniform numerical reader.

There is also a useful control on interpreting the previous residual formula literally as a represented equivalence. At unit trial amplitude, I+D(a) has rank eleven, not twelve. It cannot itself represent an invertible comparison in this linear adapter. At amplitude 1/2 it is invertible but still not a counting-metric isometry. Those facts do not invalidate a more general dissipative response/readout: they require that interpretation to be supplied rather than silently treated as the original equivalence or conservative geometry.

## Outcome of this branch

The suggested inner-face excitation has yielded a genuine retained contrast and a nonzero diagnostic, but not a source-derived birth or persistence law:

- Horn-shaped geometric candidates recover existing cells or coarsen them.
- The current collective cycle kills the contrast in its active readout and spreads the in-phase preparation.
- The nonlinear response that would detect the contrast is not implemented by that circuit's existing stage operators.
- Generic native composition does not select the missing numerical gates or schedule.

We are therefore blocked on a specific new source law, not on another choice of location or a missing arithmetic calculation. A further experiment would need an independently justified state-dependent local interaction/record-return operation and an explicit binding to these triangle ports. Adding one can be investigated as a new hypothesis, but must not be reported as discovery that the present model already generates an electron.

No mass, charge, spin, statistics, lifetime or detachment behavior has been derived. This bounded failure does not rule out all internal-boundary excitation models.

## Verification

`python research/nima/checkers/check_inner_face_response_port_binding.py` passes with exact rational arithmetic. Receipt: `results/inner-face-response-port-binding.json`. Tests cover projector algebra, the missing diagonal gate, two response orderings, amplitude scaling and invertibility/isometry controls. The twelve-coefficient restriction is derived above from the freshly inspected source blocks; no native execution or new Agda proof is claimed. No historical dynamics or source-owner artifacts were modified.
