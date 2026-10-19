# Five zeta-completion arrows against Strominger's 12-to-4 descent

## Obligation and source

The active SCC obligation is **attachment transport and route compatibility**:
can each of the five previously proposed zeta-completion arrows commute with
the supplied reduction, while preserving both triangle compositions?

Strominger's current research distinguishes two different targets:

- `source-arrow-hamiltonian-top-down-descent.md`: twelve directed-arrow
  coefficients projected to four cycle-cover coefficients, retaining a hidden
  record; a direct projection and a reducing-mode schedule are available.
- `interface-preserving-carrier-hamiltonian.md`: the original 137-record native
  presentation transported to a complete 201-coordinate chart with 137
  independent coordinates, not four independent numbers. Its retained chart
  has a left inverse. Its outer means alone lose active information.

The newer `shared-leg-controllability-audit.md` further distinguishes readable
coordinates from admitted independently writable controls. We therefore test
mathematical operators without treating them as available physical actuators.
No Strominger source is changed.

## The actual projection used here

Use the source cycle A->D->B->C->A, its twelve-arrow representation, and the
fixed Gram matrix G=10I+J. Order the visible arrows AD,CA,DB,BC first. With E
embedding those four coordinates, Strominger's metric-adjoint projection is

  P=(E^T G E)^(-1) E^T G = [I4 | J_(4,8)/14],
  N=I12-EP.

An operator U on the twelve coefficients has a well-defined four-coordinate
operator u precisely when P U N=0. Then u=P U E and P U=u P. Necessity follows
by applying an intertwiner to N; sufficiency follows from I=EP+N. A hidden
vector h with Ph=0 but PUh nonzero disproves descent.

This is the finite coefficient projection called the four-mode target in that
research. It is not an identification of Postnikov stages or of the complete
native T9 target with four numbers.

## Test 1: the original five arrows, extended as scalar multipliers

The proposed function-level arrows have factors

  AB: g=Gamma(s/2), BC: p=pi^(-s/2), AC: pg,
  CD: q=s(s-1)/2, AD: qpg.

To place them on the coefficient carrier, an extra typing choice is required.
The simplest is extension of scalars to meromorphic functions of s, with
U_e=a_e(s) I12 at the source and u_e=a_e(s) I4 at the target. Then

  P U_e=u_e P

for all five arrows, and both compositions BC o AB=AC and CD o AC=AD survive.
This holds over the meromorphic function field, or pointwise wherever the
factors are finite. Pole cancellation in completed zeta is not licensed for
arbitrary coefficient sections merely by this matrix identity.

This descent is exact but automatic: any supplied scalar multiplier commutes
with this constant P. It neither derives gamma/pi factors from the carrier nor
makes the twelve-arrow source necessary. No scalar function of s is discarded;
the coordinate count changes, not the analytic information content of a single
function-valued coordinate. Hidden coordinates are scaled too and remain in
the retained record.

## Test 2: attach each factor only to its named carrier edge

A different, explicitly tested interpretation is

  U_e=I12+(a_e-1)Q_e,

where Q_e projects onto the coordinate named e. The vertices of the function
diagram are not intrinsically the vertices of the carrier; this assignment is
a proposed attachment, not something implied by their matching letter names.

For EVERY one of AB,BC,AC,CD,AD, P Q_e N has rank one. Unless a_e=1, this
operation fails the four-coordinate descent test. The checker records an exact
hidden input and its nonzero visible output at multiplier 2 for each edge.
These rational controls reject the generic operator claim without estimating
gamma or zeta numerically. The actual meromorphic factors are not identically 1.

More strongly, solving the constraints for an arbitrary diagonal operator
D=diag(d_1,...,d_12) gives eleven independent equations: all d_j must agree.
Thus the ONLY diagonal operators that descend through this P are scalar
multiples of the identity. Independent edge scaling is excluded in this class.

There is an earlier route failure too: scaling AB and then BC affects two
coordinates; scaling AC affects a third. Consequently this literal edge-local
assignment does not even represent the original multiplication triangles
before reduction. It cannot be repaired by calling the projection a descent.

## Relation to the latest retained native chart

For Strominger's full retained chart T with decoder L, LT=I. Any already
specified linear operator U on the original 137-record value space can be
transported to T U L on the consistent image of T, since (T U L)T=T U.
Composition is preserved there, and the identity is TL, not the ambient I201.
This is retention, not information-losing four-coordinate compression.

For scalar factors the natural full ambient extension is simply a I201.
For edge-specific analytic operators, however, a map from our five function
arrows to the original labelled-record domain is still missing. In particular,
AB is precisely the omitted ordered arrow in the selected eleven-arrow native
interface. We do not insert a missing native slot or claim that the scalar
extension constructs this attachment. The present checker does not replay the
137-record native T9 suite or construct a native analytic action.

## Result and next boundary

The five original scalar function arrows survive the four-mode projection by
uniform scalar extension. Interpreting them instead as five independently
scaled carrier edges fails both route representation and reduction. These are
different attachment choices, not contradictory outcomes for one operator.

A nontrivial follow-up must supply an operation-preserving attachment from the
function diagram to source operators that act differently on carrier modes,
then test P U N=0 for those operators. Off-diagonal operators are not ruled out
by the diagonal classification. Choosing target operators first and lifting
with E and P would demonstrate a supplied lift, not derive the analytic
factors from the native source.

## Verification

Run `uv run research/voevodsky/checkers/check_zeta_five_arrow_descent.py`.
The checker reconstructs the source using Strominger's constructor, validates
its pinned receipt hashes, tests all five scalar intertwiners and both routes,
exhibits five edge-local leakage witnesses, and solves the full diagonal
classification exactly. Results are in `results/zeta-five-arrow-descent-v1.json`.

Scope: exact finite coefficient descent of supplied meromorphic multipliers.
No RH proof, physical actuation, native T9 equivalence, or Postnikov tower is
claimed.
