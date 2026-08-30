# Local relation closure does not certify a global compiler frame

Owner: `marici.Kitaev`

## Question

Can every local compiler coherence cell close exactly while the assembled
physical compiler still carries an undetected global mismatch?

Yes. Local relation residuals measure curvature. They do not measure flat
holonomy. For an abelian constructor kernel, locally closed compiler frames
modulo vertex recalibration are classified by first cohomology. A global
compiler frame exists exactly when that class vanishes.

On a toroidal coherence complex, local relation syndrome leaves two
independent holonomies. Exactly two generating loop probes are needed to make
the readout faithful modulo local frame repairs. This is the same Carrier
geometry as the finite toric-code pilot, now applied to compiler coherence
rather than Pauli errors.

## Claim boundary

This packet concerns a frozen finite two-complex whose vertices, edges, and
faces already have source-derived compiler meanings. It does not authorize a
coherence complex merely because a matrix has the right dimensions.

The abelian theorem classifies frame defects valued in an admitted abelian
kernel. Quantum phases are one example. Record permutations, noncommutative
holonomies, and conditional ancilla actions require the nonabelian form given
later.

## Coherence complex

Let `X` be a finite connected two-dimensional cell complex.

- A vertex is a local compiler chart or calibrated constructor context.
- An oriented edge is a transition between two local charts.
- A face is a declared local coherence relation among the transitions on its
  boundary.

Let `A` be an abelian constructor-kernel group, written additively. An edge
assignment is a cochain

\[
a\in C^1(X;A).
\]

It records the kernel-valued mismatch on every oriented transition.

## Local frame repair

A change of local reference at each vertex is a zero-cochain

\[
\lambda\in C^0(X;A).
\]

It changes the edge assignment by

\[
a\longmapsto a+\delta_0\lambda.
\]

This is a local frame repair. It changes transition representatives but not
the global compiler represented by their gauge class.

The face or relation syndrome is

\[
s(a)=\delta_1a\in C^2(X;A).
\]

Because

\[
\delta_1\delta_0=0,
\]

local frame repair does not change the face syndrome.

## Local-closure theorem

Every local coherence cell closes exactly when

\[
\delta_1a=0.
\]

The locally closed assignments are therefore `ker(delta_1)`. Two assignments
differ only by local frame repair when their difference lies in
`im(delta_0)`.

Hence the flat compiler-frame classes are

\[
H^1(X;A)
=
\ker\delta_1/\operatorname{im}\delta_0.
\]

A globally trivial compiler frame exists exactly when the class of `a`
vanishes. Equivalently, there is a vertex calibration `lambda` such that

\[
a=\delta_0\lambda.
\]

Thus zero local syndrome is only a flatness statement. It does not select the
trivial flat class.

## Loop holonomy

Let `z` be a cellular one-cycle. Its kernel holonomy is the pairing

\[
W_z(a)=\langle a,z\rangle.
\]

If `a` is flat and `z` changes by a boundary, then

\[
\langle a,z+\partial c\rangle
=
\langle a,z\rangle
+
\langle\delta_1a,c\rangle
=
\langle a,z\rangle.
\]

If `a` changes by a local repair, then its pairing with a cycle is unchanged.
The loop readout therefore descends to the cohomology-homology pairing.

Local face syndrome and global loop holonomy occupy different degrees. Adding
more copies of the same face check cannot reconstruct a missing homology
coordinate.

## Faithful loop family

For field coefficients, choose cycles `z_1` through `z_m`. The map

\[
[a]\longmapsto
\bigl(
W_{z_1}(a),\ldots,W_{z_m}(a)
\bigr)
\]

is injective on `H^1(X;A)` exactly when the homology classes of the selected
cycles span `H_1(X;A)`.

For phase coefficients

\[
A=\mathbb R/2\pi\mathbb Z,
\]

one has

\[
H^1(X;A)
\simeq
\operatorname{Hom}
\bigl(H_1(X;\mathbb Z),A\bigr).
\]

Evaluation on a generating set of integral first homology is jointly
faithful. The minimum number of loop probes is therefore the minimum number of
generators of `H_1`, including any torsion coordinates visible to `A`.

## Smallest toroidal hostile model

Use a cell structure on the torus with one vertex, two oriented loop edges
`p,q`, and one face attached along the commutator word

\[
pqp^{-1}q^{-1}.
\]

For an abelian kernel, the face boundary has zero abelian incidence. Every
edge assignment

\[
a=(\alpha,\beta)
\]

therefore has zero face syndrome. There is also no nontrivial vertex-gradient
repair because both edges begin and end at the same vertex.

Consequently,

\[
H^1(X;A)\simeq A^2.
\]

The two loop probes return

\[
W_p(a)=\alpha,
\qquad
W_q(a)=\beta.
\]

One loop probe leaves the other coordinate invisible. Two generating probes
are necessary and sufficient.

This exactly reproduces the finite toric-code information pattern:

- local plaquette or star syndrome establishes closure;
- local repairs quotient exact boundaries or coboundaries;
- two noncontractible cycles label the remaining torus classes;
- syndrome does not choose a preferred correction to the trivial class.

The transported coefficient object has changed, but the Carrier incidence has
not.

## Compiler interpretation

Suppose independently calibrated regions each provide a local physical
compiler. Edge transitions translate between their constructor frames. Face
checks verify that neighboring translations agree around every elementary
rewrite cell.

Even if all face checks pass, transporting a constructor frame around a
noncontractible loop can return it shifted by a kernel element. That shift can
be invisible to the logical channel quotient while becoming visible under a
controlled operation, a shared phase reference, a record comparison, or
composition with another sector.

A globally coherent compiler therefore needs both:

1. local relation closure;
2. triviality of every retained global kernel holonomy.

The second item requires loop probes or a source theorem forcing the relevant
first cohomology class to vanish.

## Decoder nonuniqueness

Given nonzero face syndrome, one may choose an edge correction `c` satisfying

\[
\delta_1c=s(a).
\]

If `c` is one solution, then

\[
c+z
\]

is another for every flat one-cochain `z`. Local syndrome cannot distinguish
corrections that differ by a global flat class.

Thus relation syndrome does not select a preferred compiler recalibration.
The chosen repair needs a source reference, boundary condition, minimum-cost
rule, or independently measured loop sector. A decoder convention is not
evidence that the physical frame was trivial.

## Nonabelian kernel

Let the invisible constructor kernel be a possibly noncommutative group `K`.
Assign an element `k_e` to every oriented edge, with reversal mapped to the
inverse. A face is flat when its ordered boundary product is identity.

Vertex recalibration acts on an edge from `v` to `w` by left and right frame
changes. After fixing a spanning-tree gauge, a connected flat assignment is
classified by a homomorphism

\[
\rho:\pi_1(X)\longrightarrow K
\]

up to simultaneous conjugation in `K`.

The flat moduli are therefore

\[
\operatorname{Hom}(\pi_1(X),K)/K,
\]

not an ordinary vector-space cohomology group.

On the torus, a flat nonabelian assignment is a commuting pair

\[
(k_p,k_q)
\]

modulo simultaneous conjugation. The face relation tests the commutator, but
does not force either holonomy to identity.

Ordered Wilson loops replace additive loop sums. A scalar character of one
loop may identify its conjugacy class while failing to identify the joint
commuting pair or its relative centralizer frame. Joint faithfulness must be
proved on the full moduli quotient intended by the compiler.

## Curvature, holonomy, and realization

Three questions are now distinct.

### Local curvature

Do elementary constructor relations close?

### Global holonomy

Does closed transport around every retained cycle return the same compiler
frame?

### Physical realization

Are the transition maps, face checks, and loop probes executable with the
declared locality, coherence, and fault bounds?

The first two are algebraic after the coherence complex and coefficient
kernel are frozen. Neither supplies the third.

## Fault tolerance of loop certification

A set of loop probes can be algebraically faithful yet operationally fragile.
Repeated loop measurements sharing one controller or reference can suffer a
common-mode shift invisible to their internal comparisons.

Fault-tolerant certification additionally needs:

- independent causal support for repeated probes;
- a code or comparison graph for sparse probe faults;
- an external anchor for common frame displacement;
- conditioning bounds for noisy continuous holonomies;
- proof that measuring the loop does not destroy the coherent constructor it
  is meant to certify.

Loop count alone is not a fault-distance theorem.

## Hostile fixtures

### All faces pass, one torus holonomy remains

Set every local face syndrome to zero and choose `alpha` nonzero on the `p`
cycle. A compiler audit using only faces accepts the wrong global frame.

### One loop called complete

Measure only `p` on the torus and infer global triviality. The entire `q`
coordinate remains in the kernel.

### Decoder silently chooses the trivial sheet

Repair a face syndrome using one arbitrary solution and declare all global
holonomies zero without measuring them.

### Character trace replaces ordered nonabelian holonomy

Measure a scalar trace of each loop and infer the full joint flat connection.
Different commuting-pair frames can survive the scalar quotient.

### Contractible repetition

Add many redundant face checks but no noncontractible probes. Curvature
confidence improves while the flat sector remains completely unresolved.

### Algebraic probe without an instrument

Name a Wilson loop functional but provide no coherent physical operation that
couples it to a record without route dephasing or uncontrolled back-action.

## Falsifiers

- Zero face syndrome is claimed to imply a globally trivial compiler frame.
- A local frame repair is claimed to change loop holonomy.
- Contractible relation checks are claimed to span noncontractible cycles.
- One torus loop is claimed to distinguish both first-homology coordinates.
- An abelian cohomology quotient is used for a noncommutative record or
  holonomy kernel.
- Individual conjugacy-class readouts are promoted to a faithful joint
  nonabelian connection coordinate.
- A loop decoder convention is treated as a source-derived frame selection.
- Algebraic loop faithfulness is promoted to fault-tolerant physical
  certification.

## Shared Carrier geometry and coefficient lens

The cell complex, boundary and coboundary incidence, local-versus-global
degree separation, repair quotient, and need for noncontractible probes belong
to shared Carrier geometry.

The coefficient lens determines what is transported around an edge and how
holonomy composes:

- additive scalar mismatch gives cohomology;
- phase transport gives circle-valued holonomy;
- record permutations give a generally nonabelian transition group;
- quantum constructor transport gives ordered operator or channel holonomy.

The toric code and compiler-frame problem share the Carrier theorem. They do
not share coefficient authority automatically.

## Disposition

Local compiler coherence is a curvature test, not a global trivialization
theorem. For an abelian kernel, the exact residual sector is `H^1(X;A)`. A
jointly faithful loop family must generate the appropriate first homology. For
a nonabelian kernel, the residual object is the representation variety of the
fundamental group modulo conjugation.

The smallest toroidal model needs two independent loop probes even though
every local relation closes. This imports the finite toric-code lesson into
the physical compiler programme at the correct level: local syndrome detects
relation failure, while noncontractible holonomy detects the remaining global
constructor frame.

No checker, build, or Git operation was run for this research-only packet.
