# Coefficient lenses are quotients of constructor history

## Bounded question

What exactly changes when one Carrier path is read through an additive scalar
current, a determinant-line phase, or an ordered noncommutative holonomy?

## Frozen constructor history

Let \(E\) be a finite alphabet of typed elementary constructors. A composable
history is a word

\[
w=e_n\cdots e_2e_1.
\]

The Carrier supplies the admissible objects, arrows, endpoints, concatenations,
cycles, and cuts. A coefficient lens assigns each admitted history a value in a
target carrying its own composition law.

The lens is not merely a storage format. It determines which transformations of
history become equal.

## Additive scalar lens

Assign a scalar increment \(a(e)\) to each elementary constructor and define

\[
A(w)=\sum_{j=1}^{n}a(e_j).
\]

Then

\[
A(vw)=A(v)+A(w).
\]

The additive lens forgets ordering:

\[
A(e_2e_1)=A(e_1e_2).
\]

It retains only the total multiplicity-weighted contribution of the elementary
constructors. In algebraic language it factors through the abelianization of
the path monoid and then through a linear functional.

Cancellation is native to this lens. A nonempty history may have zero total
current.

## Multiplicative scalar and determinant lens

Assign a nonzero scalar \(z(e)\) and define

\[
Z(w)=\prod_{j=1}^{n}z(e_j).
\]

Then

\[
Z(vw)=Z(v)Z(w).
\]

Because scalar multiplication is commutative, this lens also forgets ordering.
It is a multiplicative character of the abelianized history.

For matrix or operator transports \(U_e\), the determinant-line lens is

\[
D(w)
=
\det(U_{e_n}\cdots U_{e_1})
=
\prod_{j=1}^{n}\det U_{e_j}.
\]

It preserves the total determinant magnitude and phase while erasing every
commutator and every determinant-one internal motion. It is therefore a
multiplicative abelian shadow, not an ordered noncommutative record.

## Ordered holonomy lens

Assign an operator \(U_e\) and define

\[
H(w)=U_{e_n}\cdots U_{e_1}.
\]

Composition is ordered:

\[
H(vw)=H(v)H(w).
\]

In general,

\[
H(e_2e_1)\neq H(e_1e_2).
\]

This lens can retain order, conjugation, and noncommutative loop information.
It still need not be faithful. Distinct histories collide whenever their
operator products agree, including collisions imposed by representation
relations or a nontrivial kernel.

Thus ordered holonomy is richer than an abelian shadow but is not automatically
the full constructor history.

## Smallest order witness

Take

\[
U_a=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
\qquad
U_b=
\begin{pmatrix}
1&0\\
1&1
\end{pmatrix}.
\]

Then

\[
U_bU_a
=
\begin{pmatrix}
1&1\\
1&2
\end{pmatrix},
\qquad
U_aU_b
=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix}.
\]

The two products differ, while

\[
\det(U_bU_a)=\det(U_aU_b)=1.
\]

Any additive lens depending only on one occurrence of \(a\) and one occurrence
of \(b\) also agrees on the two histories. Therefore additive and determinant
readouts cannot distinguish the order, while the operator holonomy does.

## The lens hierarchy

For one frozen operator representation, there are canonical forgetful maps

\[
H(w)\longmapsto\det H(w)
\]

and, when logarithms or valuations are typed,

\[
\det H(w)\longmapsto A(w).
\]

These maps are generally lossy. The reverse arrows require additional source
data and are not reconstruction theorems.

The hierarchy should therefore be read as:

1. additive current retains an abelian total;
2. determinant character retains an abelian multiplicative phase or scale;
3. ordered holonomy retains the chosen representation of constructor order;
4. full history retains the word and its typed intermediate carriers.

No level implies the one below is physically available unless the relevant
readout constructor exists. No lower level determines a higher one without a
faithful lifting theorem.

## Equivalence induced by each lens

Each lens defines a history equivalence:

\[
w\sim_Av
\quad\Longleftrightarrow\quad
A(w)=A(v),
\]

\[
w\sim_Dv
\quad\Longleftrightarrow\quad
D(w)=D(v),
\]

and

\[
w\sim_Hv
\quad\Longleftrightarrow\quad
H(w)=H(v).
\]

These are constructor congruences because each readout respects concatenation.
They need not be strictly nested for arbitrary unrelated assignments. A
hierarchy exists only when the lenses are linked by declared forgetful maps
from one common source representation.

This condition prevents comparing three independently fitted observables as if
they were projections of one constructor.

## Closed-loop sensitivity

For a closed history \(\gamma\), an additive current may vanish:

\[
A(\gamma)=0.
\]

The determinant phase may also be trivial:

\[
D(\gamma)=1.
\]

Yet the ordered holonomy may remain nontrivial:

\[
H(\gamma)\neq I.
\]

Conversely, even \(H(\gamma)=I\) does not prove that the physical history was
empty. It proves only that the chosen representation has trivial endpoint
holonomy on that loop. Cost, transient state, emitted records, or another
representation may distinguish it.

This sharpens the previous endpoint-reference result: returning to one frame
can hide a nontrivial path, and one holonomy can still hide a path in its kernel.

## Control-theory translation

The additive lens is an accumulated output functional:

\[
y_A=\sum_k c_k.
\]

The determinant lens is a scalar invariant of the state-transition product:

\[
y_D=\det(\Phi_n\cdots\Phi_1).
\]

The holonomy lens is the ordered transition operator itself:

\[
\Phi=\Phi_n\cdots\Phi_1.
\]

The accumulated output and determinant may be useful diagnostics of the plant.
They do not determine its realization. Even the total transition matrix does
not determine its internal factorization without intermediate ports.

Thus the scalar completed section is a shadow of the plant because it factors
through a quotient that erases constructor order and internal state transport.

## Software-architecture translation

The additive lens resembles an aggregate metric or fold over events. The
determinant lens resembles a compositional checksum, signature character, or
scalar invariant of a transaction chain. The ordered lens resembles an event
log, command pipeline, state-machine transition, or noncommutative patch
composition.

REST, streaming, and delta transfer are transport mechanics, not the three
lenses. Any of them can carry an additive total, determinant character, or
ordered constructor packet. The relevant distinction is semantic composition:

- commutative accumulation;
- commutative multiplicative character;
- ordered action on state.

An API that returns only the final scalar cannot generally reconstruct the
ordered commands that produced it. An event stream can preserve order only if
the producer, transport, retention, and consumer all type that order.

## Toric-code instance

The shared Carrier geometry supplies primal and dual paths, boundaries, cycles,
and intersections. The coefficient lens determines what those paths transport.

An additive binary syndrome records parity of local endpoints. A phase lens can
record a character of a loop class. Pauli string multiplication retains an
ordered operator algebra whose primal-dual intersection produces
anticommutation.

The cellular geometry alone does not create the Pauli commutator. The quantum
coefficient lens supplies the noncommutative multiplication and phase. Conversely,
the coefficient algebra alone does not identify which loops intersect; the
Carrier supplies that incidence.

## Theta/Tate hostile instance

A completed scalar section may retain an additive current or determinant-like
phase while forgetting the ordered source-to-boundary constructor and its seam
action. Equal scalar Tate readouts therefore establish equivalence only under
the scalar lens.

Recovering the tail-seam operator pair requires a lift whose ordered action is
source-derived, continuous in the declared rigging, and faithful on the scalar
kernel. No manipulation of the completed scalar alone supplies that lift.

The hostile example is useful precisely because it makes the loss visible. A
successful scalar identity can coexist with unresolved operator realization.

## DPC: every conclusion is lens-relative

The conjecture is:

> Every claimed equivalence of constructor histories should name the coefficient
> lens through which equality was proved, the composition law preserved by that
> lens, and its kernel. A scalar or determinant coincidence must not be promoted
> to ordered-constructor equivalence without a source-authorized faithful lift.

This is an explanatory demand. It identifies why order disappears and what new
constructor would be required to recover it.

## Critics

### A sufficiently rich collection of scalar probes can recover an operator

Correct. Joint scalar probes can be faithful when they span the required dual
space and are source-authorized. The theorem concerns one frozen scalar quotient,
not an arbitrary complete tomography packet.

### Determinants sometimes classify the relevant operator family

Correct. That is a special injectivity theorem on a restricted family. It must
be stated and proved; determinant equality alone does not supply it.

### Ordered products depend on arbitrary factorization

The factorization must come from admitted constructors. Inventing factors after
observing the product gives no source authority. When the factors are physical
operations, their order is part of the process.

### Holonomy is already the complete history

No. It is the image of history in one representation. Relations and kernel
elements remain invisible, and transient ports may record more.

### Addition and multiplication can both encode order with noncommuting values

Correct. The decisive feature is the target composition law. The additive and
determinant lenses here have commutative scalar targets; operator-valued sums or
products require separate typing.

## Exact falsifiers

- Two histories with equal additive totals claimed to have equal order.
- Equal determinants used to infer equal transition operators.
- A nontrivial determinant-one loop declared trivial.
- Equal ordered holonomy used to infer identical internal factorization without
  intermediate ports.
- Three independently fitted readouts presented as one lens hierarchy without
  declared forgetful maps.
- A transport protocol such as REST or streaming confused with the semantic
  composition law of the payload.
- A scalar completion used to manufacture an operator lift.

## Machine-readable lens packet

```json
{
  "code": "coefficient_lens_history_quotient",
  "carrier_history": "typed constructor word",
  "additive_target": "commutative scalar monoid",
  "determinant_target": "commutative multiplicative character",
  "holonomy_target": "ordered operator monoid",
  "additive_forgets_order": true,
  "determinant_forgets_commutators": true,
  "holonomy_representation_kernel": "unresolved",
  "common_source_representation_required": true,
  "physical_implementation_inferred": false
}
```

## Deutschian explanation

The same path can cast different shadows because each coefficient system asks
the path to compose in a different target. Addition retains a total. A
determinant retains a multiplicative character. Operator multiplication retains
order to the extent that the representation distinguishes it.

Information is lost exactly where the target composition identifies histories.
Recovering that information requires a richer source-derived lens, not a more
confident reading of the poorer shadow.

## Claim boundary

This packet proves the elementary factorization and collision properties of
additive, determinant, and operator-valued path readouts. It does not assert
that any particular physical sector supplies all three lenses or that a chosen
operator representation is faithful.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was an exact structural classification of
the three coefficient lenses.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. The lenses are now typed as history quotients with
additive, multiplicative-character, and ordered-representation composition
laws.
