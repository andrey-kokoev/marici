# Binary tetrahedral spinor bridge

## Question and claim boundary

Can the existing labelled tetrahedral construction be recovered from a
spinorial representation, and which of its projectors survive?

Operator stimulus: “do quantum numbers develop like our simplex? 1 2 4 ?”,
followed by approval of the bounded double-cover test. This selects a search
direction; it supplies no evidence for quantum numbers or physical doubling.

**Disposition:** the exact Pauli operator-space bridge passes. It preserves the
36-coordinate construction and its projector algebra. A genuine spinor state
is a different representation: it can be added as a tensor factor, yielding a
72-dimensional extension with a rank-two collective doublet, but is not
recovered as a vector already inside the original space.

Result strength: exact finite-group representation comparison, not a proton
spin, charge, mass, or dynamical derivation. The SCC obligation is forward
realization and route compatibility on the operator sector. All spaces here
are finite-dimensional with their standard Hermitian topology; no completion
or physical-time interpretation is used.

## Source, convention and composition

The source is the geometry in
[`check_twelve_triangle_positive_geometry.py`](checkers/check_twelve_triangle_positive_geometry.py):

- vertices A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1);
- seed permutations ABC and ADB, represented by `(1,2,0,3)` and `(3,0,2,1)`;
- left composition and column vectors, with rotations denoted \(r_x\).

Write a unit quaternion as \(q=(w,x,y,z)\) and fix

\[
U(q)=wI-i(x\sigma_x+y\sigma_y+z\sigma_z).
\]

The lift consists of the eight signed coordinate unit quaternions and the
sixteen quaternions \((\pm1,\pm1,\pm1,\pm1)/2\). The positive-scalar lifts of
the two labelled seeds are

\[
q_{ABC}=(1,1,1,-1)/2,\qquad q_{ADB}=(1,1,-1,1)/2.
\]

They generate all 24 elements; each cubes to -1 and has order six. Quaternion
multiplication agrees with multiplication of the unitary determinant-one
matrices \(U(q)\). Pauli conjugation gives the exact sequence

\[
1\longrightarrow\{\pm1\}\longrightarrow 2T\longrightarrow A_4\longrightarrow1,
\qquad Q_8\longrightarrow V_4.
\]

The quaternion units anticommute and square to -1; their images are commuting
axis half-turns. Every lift of a nonidentity element of \(V_4\) has order four,
so this extension has no homomorphic section. The lexicographic sign section
has 50 negative cocycle pairs out of 144; all 1,728 cocycle triples close.
The count 50 is section-dependent, not an invariant quantum number.

## The two-component state and four-dimensional operator space

For the defining doublet \(S=\mathbb C^2\), set

\[
\Phi(v)=\sum_{a=1}^3 v_a\sigma_a,\qquad
U(q)\Phi(v)U(q)^*=\Phi(r(q)v).
\]

Together with the scalar matrix this gives

\[
\operatorname{End}(S)=\mathbf1\oplus\mathbf3,
\qquad 2\otimes2^*=1+3.
\]

These dimensions describe different types: one scalar operator direction,
a two-component state space, and a four-dimensional complex operator space.
They are not three successive simplex sizes or a general quantum-number law.

The metric convention is

\[
\langle A,B\rangle_{HS}=\tfrac12\operatorname{Tr}(A^*B),
\qquad \langle\Phi(v),\Phi(w)\rangle_{HS}=v^*w.
\]

The Pauli basis is orthonormal for this pairing. The checker verifies every
labelled intertwining square and character norm one for the doublet and the
three-dimensional representation. The central element acts as -I on \(S\)
but as +I on \(\operatorname{End}(S)\).

## What survives from the 36-coordinate construction

The direct-sum map

\[
J=\bigoplus_{x\in A_4}\Phi:
\bigoplus_x\mathbb C^3\longrightarrow
\bigoplus_x\operatorname{End}_0(S)
\]

is an equivariant isometry, not a replacement by spinor state fibers. Both
sides have complex dimension 36. With

\[
v_0=(-2/3,\;1/3+i\sqrt3,\;-1/3+i\sqrt3),\qquad
v_x=r_xv_0,\qquad u=(v_x)_x,
\]

one has \(\|v_0\|^2=20/3\) and \(\|u\|^2=80\). The existing local,
symmetry, and collective projectors obey

\[
L^2=L,\quad R^2=R,\quad N^2=N,\quad LR=RL=N,
\qquad (\operatorname{rank}L,\operatorname{rank}R,\operatorname{rank}N)=(12,3,1).
\]

Under \(J\), these are Hilbert-Schmidt **superoperators**. For example, the
local action is

\[
A_x\longmapsto\Phi(v_x)
\frac{\langle\Phi(v_x),A_x\rangle_{HS}}{20/3}.
\]

The block \(R_{xy}=r_xr_y^{-1}/12\) becomes conjugation by a relative
quaternion lift, divided by 12; its sign cancels. The collective projector is
the analogous rank-one projector onto the tuple \((\Phi(v_x))_x\).
All these relations are tested exactly. The supports 108, 432, 1296 survive
in the inherited Pauli-coordinate basis only; no basis-independent arrow
count or physical mass is asserted.

## State-sector test and an explicit extension

Replacing the three-axis fiber by \(S\) gives
\(W=\mathbb C[A_4]\otimes S\), of dimension 24. With

\[
(T(q)\psi)_x=U(q)\psi_{r(q)^{-1}x},
\]

its center acts as -I, and its full group average is zero. Thus the original
rank-three invariant-mode projector does not survive that replacement.
More generally, any equivariant linear map from a central-even carrier to a
central-odd carrier is zero: equivariance at -1 would require \(F=-F\).

A different construction **adds** an independent doublet:

\[
\widetilde V=V_{36}\otimes S,\qquad
\widetilde L=L\otimes I_2,\quad
\widetilde R=R\otimes I_2,\quad
\widetilde N=N\otimes I_2.
\]

The ranks become 24, 6, 2, and
\(\widetilde L\widetilde R=\widetilde R\widetilde L=\widetilde N\).
The collective sector is exactly a doublet:

\[
E:S\longrightarrow\operatorname{im}\widetilde N,\qquad E(s)=u\otimes s,
\qquad (D(q)\otimes U(q))E=EU(q).
\]

Here \((D(q)v)_x=r(q)v_{r(q)^{-1}x}\) is the old vector action pulled back
to \(2T\). The checker tests both basis images for all 24 elements. The
center acts as \(-I_2\) on this sector. There is an invariant subspace but
no invariant nonzero vector. In particular, \(\widetilde R\) is the tensor
extension of the old projector, **not** the Reynolds average of the new
spinorial action (that average is zero).

This explains when 72 is legitimate: tensoring 36 by 2, not replacing a
three-component fiber with a two-component one. The extra spinor factor is
an explicit modelling input, not a derived particle degree of freedom.

## Falsification record

The governing conjecture was that the Pauli intertwiner preserves the
labelled rotations and projector algebra, but does not identify operator
vectors with spinor states. Rivals and discriminating tests:

| Rival | Exact test | Disposition |
|---|---|---|
| Opposite conjugation convention works unchanged | Replace \(U A U^*\) by \(U^* A U\) | 48 of 72 labelled Pauli squares fail |
| Spinors descend to ordinary A4 vectors | Test central action and order-two lifts | -I upstairs; order-four lifts; rejected |
| The local triangle cycle is an SU(2) conjugation | Test \(A_0^T A_0-I\), where \(A_0=X_0CX_0^{-1}\) | Nonzero; its (1,2) entry is -4/3 |
| The old collective vector directly supplies a pure spinor bilinear | Compute \(\det\Phi(v_0)\) and adjoint | Determinant 16/3, non-Hermitian; rejected |
| Replacing fibers preserves an invariant collective vector | Average the 24-dimensional spinor action | Rank zero |
| No commuting unit-charge operator exists on the 36-space | Test N and I | Universal charge no-go refuted |

The local cycle remains a valid order-three linear map and transports as a
superoperator; its nonorthogonality blocks only its proposed interpretation
as unitary spinor conjugation. Also
\(\Phi(v_0)^2=-16I/3\), whereas a rank-one traceless spinor bilinear has zero
determinant. A superoperator projector onto \(\Phi(v_0)\) is not the matrix
\(\Phi(v_0)\) itself and is not a spinor density projector.

## Correction and remaining physical requirements

The earlier [axis-charge note](tetrahedral-axis-sign-charge-operator.md)
overclaimed a universal no-go. Both I and N commute with the combined A4
action and give eigenvalue +1 on u; N has spectrum {0,1}, and 2N-I has
spectrum {-1,1}. These are algebraic counterexamples, not physical electric
charge identifications. The corrected checker distinguishes expectation
from eigenstate status: -3 times a half-turn has expectation +1 but variance 8.

No physical state-selection rule, whole-carrier continuous rotation action,
Hamiltonian, independently defined charge sectors, or electromagnetic coupling
is constructed here. Those missing inputs stop physical interpretation; the
finite operator-space comparison and optional doublet extension remain valid.

## Reproduction

```text
python research/nima/checkers/check_binary_tetrahedral_spinor_bridge.py
python research/nima/checkers/check_tetrahedral_axis_charge_operator.py
python research/aspect/scc/scc.py check binary-tetrahedral-spinor-bridge
```

The first checker uses exact four-rational coordinates for
\(\mathbb Q(\sqrt3,i)\), tests all 576 group products, and imports the original
geometry without consuming cached results. It writes source digests and the
positive tests, hostile residuals, and claim boundary to
`results/binary-tetrahedral-spinor-bridge.json`. The SCC registration is
[`scc-models/binary-tetrahedral-spinor-bridge.json`](scc-models/binary-tetrahedral-spinor-bridge.json).
SCC check and manifest validation passed, as did a fresh run of the original
twelve-triangle checker. SCC currently records exit-code-only receipts for
these checkers; their generated JSON supplies the detailed scientific results.

Durability at this closeout: preregistration event
`ev-000000015672-6d730726-d7c3-4326-96b7-301c26105914` and result event
`ev-000000015673-279ef537-b929-4258-bbaa-6e4fd6592046` are admitted, not truth
certifications. The interval 15672–15673 and the five source/packet/manifest
files linked here remain uncommitted; no commit or push was authorized.
No checker remains running.
