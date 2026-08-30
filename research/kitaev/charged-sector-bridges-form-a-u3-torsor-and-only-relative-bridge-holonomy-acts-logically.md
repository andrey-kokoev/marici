# Charged sector bridges form a `U(3)` torsor and only relative bridge holonomy acts logically

Owner: `marici.Kitaev`

## Bounded question

Once the total-`A` and total-`B` four-`C`-anyon qutrit sectors and a
compensating `B`-charge reference are available, does sector hopping itself
supply a new logical qutrit gate?

Not canonically. After the rigidity frames are fixed, the six-dimensional
workspace factorizes as a logical qutrit times a sector bit. The canonical
charged bridge acts only on the sector bit and is the identity on the qutrit.

All unitary charged bridges form a torsor over `U(3)`. A physical route must
select one qutrit-valued bridge coordinate. A nontrivial logical gate appears
only by comparing two inequivalent charged routes, or by coupling the sector
bit to the qutrit through a separately derived interaction. The loop of one
bridge followed by the inverse of another has logical holonomy equal to their
relative `U(3)` element.

## Claim boundary

This packet classifies the exact finite-dimensional bridge freedom after the
two qutrit sectors and normalized rigidity frames are given. It does not prove
that any noncanonical bridge is realized by a microscopic ribbon, dyon,
boundary, or Hamiltonian path.

The torsor is an ambiguity and a design space, not physical authority. Charge
typing determines that a bridge is off-diagonal between `A` and `B`; it does
not determine its action on the three-dimensional multiplicity coordinate.

## Product coordinates on the workspace

Let

\[
\mathcal H=\mathcal H_C^{(3)}
\]

be the original qutrit, and let

\[
J_A:\mathcal H\longrightarrow\mathcal H_A^{(4)},
\qquad
J_B:\mathcal H\longrightarrow\mathcal H_B^{(4)}
\]

be normalized rigidity isomorphisms.

Define a unitary identification

\[
F:\mathcal H\otimes\mathbb C^2
\longrightarrow
\mathcal W_{AB}
\]

by

\[
F(\psi\otimes|0\rangle)=J_A\psi,
\qquad
F(\psi\otimes|1\rangle)=J_B\psi.
\]

In these coordinates, the total-charge projectors are

\[
P_A^{(4)}=I_{\mathcal H}\otimes|0\rangle\langle0|,
\qquad
P_B^{(4)}=I_{\mathcal H}\otimes|1\rangle\langle1|.
\]

The sector measurement is therefore a nondemolition measurement of the second
factor. It need not reveal any logical qutrit coordinate.

## Canonical bridge is logically trivial

The rigidity frames define

\[
X_0=J_BJ_A^{-1}:
\mathcal H_A^{(4)}\longrightarrow\mathcal H_B^{(4)}.
\]

Under `F`, this map is

\[
I_{\mathcal H}\otimes|1\rangle\langle0|.
\]

With the compensating reference charge included, a neutral swap built from
`X_0` moves the unknown qutrit between the two sector ports while acting as
the identity on its logical state.

This is valuable routing and makes rank-safe measurement possible. It is not
a new qutrit gate.

## Classification of unitary charged bridges

Let

\[
X:\mathcal H_A^{(4)}\longrightarrow\mathcal H_B^{(4)}
\]

be any unitary charged bridge. Define its qutrit coordinate

\[
R_X=J_B^{-1}XJ_A.
\]

Then

\[
R_X\in U(3),
\]

and

\[
X=J_BR_XJ_A^{-1}.
\]

Conversely, every `R` in `U(3)` defines an algebraic unitary bridge

\[
X_R=J_BRJ_A^{-1}.
\]

Hence the set of unitary `A`-to-`B` bridges is a `U(3)` torsor.
There is no preferred origin until the rigidity frames and one physical
transport route are fixed.

If reversibility is weakened to mere invertibility, the corresponding torsor
is `GL(3,C)`. The unitary restriction is the coherent, norm-preserving bridge
contract used here.

Charge conservation sees only that `X_R` carries `B` charge. It is blind to
`R`.

## Neutral relational swap

Include the charge reference described in the preceding packet. In product
coordinates, the neutral Hermitian swap associated with `R` acts on the
fixed-global-charge relational subspace as

\[
S_R
=
R\otimes|1\rangle\langle0|
+
R^*\otimes|0\rangle\langle1|.
\]

For unitary `R`,

\[
S_R^*=S_R,
\qquad
S_R^2=I.
\]

Thus it is an exact sector-exchange involution. Applied to sector zero, it
transports the qutrit to sector one while applying `R`.

The canonical choice `R=I` is a pure sector swap. Every other choice couples
the sector route to the logical qutrit.

## Relative bridge holonomy

Let `X_R` and `X_S` be two charged bridge routes with the same typed endpoints.
Start in the total-`A` qutrit sector, traverse `X_R`, and return through the
inverse of `X_S`. The logical loop is

\[
X_S^*X_R
=
J_A S^*R J_A^{-1}.
\]

Therefore the induced qutrit holonomy is

\[
H_{S,R}=S^*R.
\]

One bridge followed by its own exact inverse gives identity. Nontrivial
logical action requires two inequivalent routes, an imperfect inverse, or a
sector-dependent operation inserted between the crossings.

This is the charged-sector analogue of path interferometry. A gate is encoded
in the relative route, not in the fact that either route changes charge.

## Frame covariance

Change the qutrit frames by

\[
J_A'=J_AU_A,
\qquad
J_B'=J_BU_B.
\]

The bridge coordinate transforms as

\[
R'=U_B^*RU_A.
\]

For two routes, their relative holonomy transforms by conjugation in the
initial qutrit frame:

\[
S'^*R'
=
U_A^*S^*RU_A.
\]

Thus matrix entries depend on the based fusion frames, while the conjugacy
class of a closed relative loop is frame covariant. A source-fixed logical
basis is still required to call the holonomy a specific gate.

## Charge measurement is blind to bridge holonomy

After either bridge reaches the total-`B` sector, a total-charge measurement
reports `B` with certainty. It cannot distinguish `R` from `S` because both
maps have the same charge endpoints and full rank.

Likewise, a final return to total `A` can close every charge syndrome while
leaving the logical holonomy `S*R` nontrivial. Charge closure therefore does
not certify logical closure.

This is the exact common-mode fault on the sector-hopping architecture: the
reference and charge records return correctly while the multiplicity frame
moves.

## When sector measurement adds no logical power

Suppose every admitted sector-changing constructor has `R=I`, and every
qutrit unitary acts identically in the two sectors. Then the complete
constructor algebra factorizes into logical and sector operations. Measuring
the sector and conditioning later operations can only select among qutrit
gates already present in the logical factor.

It cannot synthesize a new coherent qutrit gate from the sector bit alone.
The sector record supplies routing and heralding, not a new coefficient.

To enlarge the qutrit gate set, at least one constructor must have nontrivial
operator-Schmidt content across the logical and sector factors. Equivalent
forms are:

- a bridge `X_R` with non-scalar `R`;
- a sector-controlled pair of distinct qutrit gates;
- a joint measurement whose full-rank logical branches are not all
  proportional;
- two charged routes with nontrivial relative holonomy.

## Minimal two-route gate packet

A claimed logical gate from charged transport should provide:

1. two independently typed `B`-charge transfer routes;
2. their complete microscopic constructor words;
3. normalized rigidity frames `J_A` and `J_B`;
4. branchwise logical bridge matrices `R` and `S`;
5. the relative gate `S*R`;
6. reference-charge return and environment closure for each route;
7. a frame anchor distinguishing the route pair from its common conjugate;
8. leakage, duration, support, and one-fault propagation bounds.

Only item 5 is an endpoint logical calculation. The other items establish
that the relative matrix belongs to executable physics.

## Complex-resource consequence

If both route matrices are real in the common electric frame, then

\[
S^*R\in O(3)
\]

up to global phase. The route pair still cannot supply a genuinely complex
qutrit gate.

A dyonic or flux-resolved route may produce a non-real `R` or `S`. Its
three-cycle orientation then appears directly in the relative holonomy. The
conjugate source model sends

\[
S^*R
\longmapsto
\overline{S^*R}.
\]

Pure charge measurements remain blind to this orientation reversal, so the
complex route pair needs an independent dyon or boundary frame reference.

## Bridge fault taxonomy

### Endpoint-correct holonomy fault

The charged path begins in `A`, ends in `B`, and returns the reference charge
correctly, but implements `R_delta R` rather than `R`. Total-charge checks
accept the fault.

### Shared route-frame fault

Both `R` and `S` are conjugated by the same unknown qutrit frame. Their
internal relative spectrum is stable while the named logical gate is wrong
relative to an external basis.

### Route-record dephasing

An environment distinguishes the two charged routes. Attempting a coherent
relative comparison then produces a mixture rather than the holonomy
`S*R`.

### Reference nonreturn

The data returns to the preferred charge sector while the compensating
reference remains route-correlated. Tracing it out dephases the logical
operation.

### Canonical-bridge circularity

The algebraic map `J_B J_A^-1` is declared physically realized solely because
it is the desired logical identity between sectors. A microscopic transport
or source symmetry must independently select it.

## Exact falsifiers

- Charge typing is claimed to determine the multiplicity matrix `R`.
- All unitary charged bridges are identified with the canonical bridge.
- The canonical sector swap is called a new qutrit gate.
- One bridge followed by its exact inverse is assigned nontrivial holonomy.
- A total-charge success record is claimed to certify the logical bridge
  matrix.
- Two route matrices differ while their relative holonomy is set to identity.
- A sector-only adaptive protocol is claimed to enlarge the logical gate
  algebra without any logical-sector coupling.
- A non-real relative holonomy is derived from two routes preserving the
  common real structure.
- A route-dependent environment record is discarded while coherent holonomy
  is retained.
- The compensating `B` reference returns to different states on the two paths
  while a unitary qutrit loop is claimed.
- The `U(3)` bridge torsor is treated as a menu of authorized physical gates.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies product decomposition, route comparison,
relative holonomy, reference-balanced transport, operator-Schmidt coupling,
and the distinction between endpoint typing and path action.

The quantum coefficient lens supplies fusion multiplicity spaces, unitary
bridge torsors, projective frame covariance, charge superselection, coherent
route interference, and complex conjugate orientation.

## Disposition

The minimal six-dimensional workspace is not yet a gate engine. Its canonical
`B`-charge bridge is logical identity tensored with a sector swap. Charge
typing permits a full `U(3)` torsor of other bridge actions but selects none of
them physically.

New logical control arises from relative charged-route holonomy. Two
independently compiled bridges `R` and `S` generate the closed-loop gate
`S*R`, while all total-charge records can remain identical. The next native
source task is therefore to derive two coherent `B`-transfer routes—at least
one with non-real dyonic content—and certify their relative multiplicity
holonomy, reference return, and fault filtration.

No build, checker, or Git operation was run for this research-only packet.
